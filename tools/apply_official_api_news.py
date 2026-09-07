#!/usr/bin/env python3
"""Apply official Seller API News metadata to the Chrome-captured operation index."""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from pathlib import Path
from typing import Any, Dict, Iterable, List


Operation = Dict[str, Any]
NewsEntry = Dict[str, Any]
NewsUpdate = Dict[str, Any]

PATH_RE = re.compile(r"/v\d+(?:(?!/v\d+(?:/|$))/[A-Za-z0-9._-]+)+")
REPLACEMENT_MARKERS = (
    "请切换到",
    "请切换至",
    "请改用",
    "请使用",
    "切换到",
    "切换至",
    "改用",
    "使用",
)


def extract_paths(text: str) -> List[str]:
    """Extract versioned API paths and split concatenated paths from collapsed DOM text."""

    paths: List[str] = []
    for match in PATH_RE.finditer(str(text or "")):
        path = match.group(0).rstrip(".,;:，。；：")
        if path and path not in paths:
            paths.append(path)
    return paths


def _entry_source_url(entry: NewsEntry) -> str:
    source_url = str(entry.get("sourceUrl") or "")
    if source_url:
        return source_url
    entry_id = str(entry.get("id") or "").strip("#")
    return f"https://docs.ozon.ru/api/seller/zh/#{entry_id}" if entry_id else ""


def _classify_segment(segment: str) -> List[str]:
    labels: List[str] = []
    text = segment.replace(" ", "")

    field_context = bool(re.search(r"(参数|字段|方法响应|方法请求|请求中|响应中)", text))
    method_deprecated = bool(
        re.search(r"(该方法|该方式|这些方式|方法).{0,18}(已弃用|即将废弃|已过时|即将过时|未来停用|将于.{0,20}停用|关闭)", text)
    )
    method_removed = bool(
        re.search(r"(该方法|该方式|这些方式|方式|方法).{0,30}(已从.{0,12}(文件|文档)中删除|已从.{0,12}(文件|文档)中移除|已删除|已移除)", text)
        or re.search(r"(该方法|该方式|这些方式|方式|方法).{0,12}已过期.{0,30}(删除|移除)", text)
        or re.search(r"相关方法已从.{0,12}(文件|文档)中删除", text)
    )

    if "新增了用于" in text or re.search(r"(新增|添加|增加).{0,12}(beta)?方法(版本)?", text):
        labels.append("new_method")
    if method_deprecated and not (field_context and not re.search(r"(该方法|该方式|这些方式)", text)):
        labels.append("deprecated_method")
    if method_removed and not (field_context and not re.search(r"(该方法|该方式|这些方式|相关方法)", text)):
        labels.append("removed_method")
    if re.search(r"(新增|添加).{0,30}(参数|字段)", text):
        labels.append("added_field")
    if re.search(r"(参数|字段).{0,30}(已弃用|即将废弃|标记为已弃用|停止支持)", text) or re.search(
        r"已将.{0,30}(参数|字段).{0,10}标记为已弃用", text
    ):
        labels.append("deprecated_field")
    if re.search(r"(移除|删除).{0,30}(参数|字段)", text) or re.search(
        r"已从.{0,30}(方法|响应|请求).{0,10}(移除|删除).{0,30}(参数|字段)", text
    ) or re.search(
        r"(参数|字段).{0,30}(已过期|已从.{0,12}(文件|文档)中删除|已从.{0,12}(文件|文档)中移除)", text
    ):
        labels.append("removed_field")
    if "从Beta版迁移至正式版" in text or "从测试版移至正式版" in text:
        labels.append("graduated")
    if not labels and re.search(r"(更新|已更新|变更|改为|更改|新了)", text):
        labels.append("updated")

    unique: List[str] = []
    for label in labels:
        if label not in unique:
            unique.append(label)
    return unique


def _replacement_paths(current_path: str, segment: str) -> List[str]:
    replacements: List[str] = []
    marker_positions = [segment.find(marker) for marker in REPLACEMENT_MARKERS if marker in segment]
    if not marker_positions:
        return replacements

    tail = segment[min(marker_positions) :]
    for path in extract_paths(tail):
        if path != current_path and path not in replacements:
            replacements.append(path)
    return replacements


def _sentence_window(text: str, start: int) -> str:
    sentence_end = len(text)
    for delimiter in ("。", "\n"):
        position = text.find(delimiter, start)
        if position != -1:
            sentence_end = min(sentence_end, position + 1)
    return text[start:sentence_end].strip()


def _segments_for_paths(text: str) -> Iterable[tuple[str, str, str]]:
    matches = list(PATH_RE.finditer(text))
    index = 0
    while index < len(matches):
        match = matches[index]
        # Redoc collapses one table cell containing several endpoints into a
        # whitespace-separated path run. Keep the row's description attached
        # to every path in that run.
        group_end = index + 1
        while group_end < len(matches) and not text[matches[group_end - 1].end() : matches[group_end].start()].strip(" \t\r\n"):
            group_end += 1
        description_end = matches[group_end].start() if group_end < len(matches) else len(text)
        segment = text[match.start() : description_end].strip()
        replacement_window = _sentence_window(text, match.start())
        if group_end < len(matches):
            replacement_window = f"{segment} {_sentence_window(text, matches[group_end].start())}".strip()
        for grouped_match in matches[index:group_end]:
            path = grouped_match.group(0).rstrip(".,;:，。；：")
            yield path, segment, replacement_window
        index = group_end


def summarize_news_entry(entry: NewsEntry) -> List[NewsUpdate]:
    """Convert one News item into path-level update summaries."""

    date = str(entry.get("date") or "")
    source_url = _entry_source_url(entry)
    summaries: Dict[str, NewsUpdate] = {}

    # Fresh Chrome extraction keeps the method column as structured rows. Use
    # its href-derived methods because the visible label can be duplicated or
    # mistyped while the links still identify each endpoint correctly.
    structured_rows = entry.get("rows")
    if isinstance(structured_rows, list):
        row_segments = []
        for row in structured_rows:
            if not isinstance(row, dict):
                continue
            description = str(row.get("description") or "").strip()
            methods = row.get("methods")
            if not description or not isinstance(methods, list):
                continue
            for path in methods:
                path = str(path or "").strip()
                if path.startswith("/v"):
                    row_segments.append((path, f"{path} {description}"))
        path_segments = row_segments
    else:
        text = str(entry.get("text") or "").strip()
        path_segments = [(path, segment, sentence_window) for path, segment, sentence_window in _segments_for_paths(text)]

    for item in path_segments:
        path, segment = item[:2]
        sentence_window = segment if structured_rows is not None else item[2]
        labels = _classify_segment(segment)
        if not labels:
            continue

        replacements = _replacement_paths(path, sentence_window)
        display_text = segment
        if replacements and not any(replacement in display_text for replacement in replacements):
            display_text = f"{display_text} 替代方法：{', '.join(replacements)}"

        existing = summaries.setdefault(
            path,
            {
                "date": date,
                "path": path,
                "labels": [],
                "replacement_paths": [],
                "sourceUrl": source_url,
                "text": display_text,
            },
        )
        for label in labels:
            if label not in existing["labels"]:
                existing["labels"].append(label)
        if set(labels) & {"deprecated_method", "removed_method"}:
            existing["lifecycle_text"] = display_text
        for replacement_path in replacements:
            if replacement_path not in existing["replacement_paths"]:
                existing["replacement_paths"].append(replacement_path)
        if len(display_text) > len(str(existing.get("text") or "")):
            existing["text"] = display_text

    return list(summaries.values())


def _news_update_for_operation(summary: NewsUpdate) -> NewsUpdate:
    update: NewsUpdate = {
        "date": summary.get("date", ""),
        "labels": summary.get("labels", []),
        "text": summary.get("text", ""),
        "sourceUrl": summary.get("sourceUrl", ""),
    }
    if summary.get("replacement_paths"):
        update["replacement_paths"] = summary["replacement_paths"]
    return update


def _set_lifecycle(operation: Operation, summary: NewsUpdate) -> None:
    labels = set(summary.get("labels", []))
    if "removed_method" not in labels and "deprecated_method" not in labels:
        return

    status = "removed" if "removed_method" in labels else "deprecated"
    current = operation.get("lifecycle")
    if current and current.get("status") == "removed" and status == "deprecated":
        return
    if current and current.get("status") == status and str(current.get("date") or "") > str(summary.get("date") or ""):
        return

    lifecycle = {
        "status": status,
        "date": summary.get("date", ""),
        "sourceUrl": summary.get("sourceUrl", ""),
        "text": summary.get("lifecycle_text") or summary.get("text", ""),
    }
    if summary.get("replacement_paths"):
        lifecycle["replacement_paths"] = summary["replacement_paths"]
    operation["lifecycle"] = lifecycle


def apply_news_metadata(operations: List[Operation], news: Dict[str, Any]) -> Dict[str, Any]:
    """Attach News updates and lifecycle metadata to operation dictionaries."""

    operations_by_path = {str(operation.get("path") or ""): operation for operation in operations}
    removed_or_missing_methods: List[NewsUpdate] = []
    label_counts: Counter[str] = Counter()

    for operation in operations:
        operation.pop("news_updates", None)
        operation.pop("lifecycle", None)

    for entry in news.get("entries", []):
        for summary in summarize_news_entry(entry):
            labels = set(summary.get("labels", []))
            label_counts.update(labels)
            operation = operations_by_path.get(str(summary.get("path") or ""))
            if operation:
                operation.setdefault("news_updates", []).append(_news_update_for_operation(summary))
                _set_lifecycle(operation, summary)
            elif labels & {"deprecated_method", "removed_method"}:
                removed_or_missing_methods.append(summary)

    for operation in operations:
        if "news_updates" in operation:
            operation["news_updates"].sort(key=lambda item: str(item.get("date") or ""), reverse=True)

    return {
        "operations": operations,
        "label_counts": dict(sorted(label_counts.items())),
        "removed_or_missing_methods": removed_or_missing_methods,
    }


def _status_rows(operations: List[Operation]) -> List[str]:
    rows = ["| 方法 | 状态 | 日期 | 替代方法 | News |", "| --- | --- | --- | --- | --- |"]
    for operation in sorted(
        (item for item in operations if item.get("lifecycle")),
        key=lambda item: (str(item["lifecycle"].get("status")), str(item.get("path"))),
    ):
        lifecycle = operation["lifecycle"]
        replacements = ", ".join(f"`{path}`" for path in lifecycle.get("replacement_paths", [])) or "无"
        source_url = str(lifecycle.get("sourceUrl") or "")
        news_link = f"[来源]({source_url})" if source_url else "无"
        rows.append(
            "| "
            f"`{operation.get('path')}` | "
            f"`{lifecycle.get('status')}` | "
            f"{lifecycle.get('date') or '无'} | "
            f"{replacements} | "
            f"{news_link} |"
        )
    return rows


def _missing_rows(items: List[NewsUpdate]) -> List[str]:
    rows = ["| 方法 | 标记 | 日期 | 替代方法 | 摘要 |", "| --- | --- | --- | --- | --- |"]
    for item in items:
        replacements = ", ".join(f"`{path}`" for path in item.get("replacement_paths", [])) or "无"
        labels = ", ".join(f"`{label}`" for label in item.get("labels", [])) or "无"
        summary = _escape_markdown_table_cell(item.get("text", ""))
        rows.append(f"| `{item.get('path')}` | {labels} | {item.get('date') or '无'} | {replacements} | {summary} |")
    return rows


def _field_rows(operations: List[Operation]) -> List[str]:
    rows = ["| 方法 | 日期 | 标记 | 摘要 | News |", "| --- | --- | --- | --- | --- |"]
    field_labels = {"added_field", "deprecated_field", "removed_field"}
    for operation in sorted(operations, key=lambda item: str(item.get("path"))):
        for update in operation.get("news_updates", []):
            labels = set(update.get("labels", []))
            if not labels & field_labels:
                continue
            label_text = ", ".join(f"`{label}`" for label in update.get("labels", []))
            summary = _escape_markdown_table_cell(update.get("text", ""))
            source_url = str(update.get("sourceUrl") or "")
            news_link = f"[来源]({source_url})" if source_url else "无"
            rows.append(f"| `{operation.get('path')}` | {update.get('date') or '无'} | {label_text} | {summary} | {news_link} |")
    return rows


def _escape_markdown_table_cell(value: Any) -> str:
    """Keep derived Markdown table rows valid without changing captured text."""

    return str(value or "").strip().replace("|", "\\|").replace("\r\n", "<br>").replace("\n", "<br>").replace("\r", "<br>")


def render_news_summary(news: Dict[str, Any], result: Dict[str, Any]) -> str:
    operations = result["operations"]
    lifecycle_count = sum(1 for operation in operations if operation.get("lifecycle"))
    missing_items = result["removed_or_missing_methods"]
    label_counts = result["label_counts"]
    label_text = ", ".join(f"`{label}`: {count}" for label, count in label_counts.items()) or "无"

    lines = [
        "# 官方 Seller API News 更新索引",
        "",
        "> 由 `tools/apply_official_api_news.py` 根据 Chrome 抽取的 `indexes/official-seller-api.news.json` 生成。",
        "",
        "## 摘要",
        "",
        f"- News 条目数：{news.get('entry_count') or len(news.get('entries', []))}",
        f"- 当前方法页已标记废弃/移除：{lifecycle_count}",
        f"- News 中提到但当前 operation 索引不存在的废弃/移除方法：{len(missing_items)}",
        f"- 标签统计：{label_text}",
        "",
        "## 已在当前方法页标记的方法",
        "",
        *_status_rows(operations),
        "",
        "## News 中已移除或当前索引缺失的方法",
        "",
        *_missing_rows(missing_items),
        "",
        "## 字段级新增、废弃与移除",
        "",
        *_field_rows(operations),
        "",
    ]
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--operations", type=Path, default=Path("indexes/official-seller-api.operations.json"))
    parser.add_argument("--news", type=Path, default=Path("indexes/official-seller-api.news.json"))
    parser.add_argument("--summary", type=Path, default=Path("docs/api/seller-api-news.md"))
    args = parser.parse_args()

    operations_data = json.loads(args.operations.read_text(encoding="utf-8"))
    news_data = json.loads(args.news.read_text(encoding="utf-8"))
    operations = operations_data.get("operations", [])
    if not isinstance(operations, list):
        raise ValueError("operations JSON must contain an operations list")

    result = apply_news_metadata(operations, news_data)
    operations_data["operations"] = result["operations"]
    operations_data["news_entry_count"] = news_data.get("entry_count") or len(news_data.get("entries", []))
    operations_data["news_captured_at"] = news_data.get("captured_at")
    operations_data["news_label_counts"] = result["label_counts"]
    operations_data["news_removed_or_missing_methods"] = result["removed_or_missing_methods"]
    args.operations.write_text(json.dumps(operations_data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    args.summary.parent.mkdir(parents=True, exist_ok=True)
    args.summary.write_text(render_news_summary(news_data, result), encoding="utf-8")
    print(
        "applied news metadata: "
        f"{len(result['operations'])} operations, "
        f"{sum(1 for operation in result['operations'] if operation.get('lifecycle'))} lifecycle markers, "
        f"{len(result['removed_or_missing_methods'])} removed/missing methods"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

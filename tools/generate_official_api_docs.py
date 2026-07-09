#!/usr/bin/env python3
"""Generate per-operation Markdown docs from the Chrome-captured Seller API index."""

from __future__ import annotations

import argparse
import json
import re
from collections import defaultdict
from pathlib import Path
from typing import Any, Dict, Iterable, List


Operation = Dict[str, Any]


def slugify_operation(operation: Operation) -> str:
    method = str(operation.get("method") or "method").lower()
    path = str(operation.get("path") or "unknown")
    operation_id = str(operation.get("operationId") or operation.get("title") or "operation")
    path_part = path.strip("/").replace("/", "-") or "root"
    path_part = re.sub(r"[^A-Za-z0-9._-]+", "-", path_part).strip("-")
    operation_part = re.sub(r"[^A-Za-z0-9._-]+", "-", operation_id).strip("-")
    return f"{method}-{path_part}-{operation_part}.md"


def operation_group(operation: Operation) -> str:
    path = str(operation.get("path") or "").strip("/")
    parts = [part for part in path.split("/") if part]
    if len(parts) >= 2 and re.fullmatch(r"v\d+", parts[0]):
        return parts[1]
    if parts:
        return parts[0]
    return "other"


def _format_text_block(text: str) -> str:
    text = str(text or "").strip()
    return text if text else "无"


def _looks_like_json(text: str) -> bool:
    stripped = text.strip()
    return (stripped.startswith("{") and stripped.endswith("}")) or (
        stripped.startswith("[") and stripped.endswith("]")
    )


def _render_examples(examples: Iterable[Dict[str, Any]]) -> List[str]:
    lines: List[str] = []
    for example in examples:
        index = example.get("index", len(lines))
        text = _format_text_block(example.get("text", ""))
        lines.append(f"### 示例 {index}")
        if _looks_like_json(text):
            lines.extend(["", "```json", text, "```", ""])
        else:
            lines.extend(["", "```text", text, "```", ""])
    if not lines:
        return ["无"]
    return lines


def render_operation_doc(operation: Operation) -> str:
    title = str(operation.get("title") or operation.get("operationId") or "未命名方法")
    method = str(operation.get("method") or "").upper()
    path = str(operation.get("path") or "")
    operation_id = str(operation.get("operationId") or "")
    source_url = str(operation.get("sourceUrl") or "")
    headings = operation.get("headings") or []
    tables = operation.get("tables") or []
    examples = operation.get("examples") or []

    lines: List[str] = [
        f"# {title}",
        "",
        "> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。",
        "",
        "## 方法",
        "",
        f"- 请求：`{method} {path}`",
        f"- Operation ID：`{operation_id}`" if operation_id else "- Operation ID：无",
        f"- 官方锚点：{source_url}" if source_url else "- 官方锚点：无",
        f"- 分组：`{operation_group(operation)}`",
        "",
    ]

    if headings:
        lines.extend(["## 页面标题结构", ""])
        for heading in headings:
            lines.append(f"- {heading}")
        lines.append("")

    lines.extend(["## 参数与返回结构", ""])
    if tables:
        for table in tables:
            table_index = table.get("index", 0)
            lines.extend(
                [
                    f"### 表格 {table_index}",
                    "",
                    _format_text_block(table.get("text", "")),
                    "",
                ]
            )
    else:
        lines.extend(["无", ""])

    lines.extend(["## 示例", ""])
    lines.extend(_render_examples(examples))
    lines.extend(
        [
            "## 使用提醒",
            "",
            "- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。",
            "- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。",
            "- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。",
            "",
        ]
    )
    return "\n".join(lines)


def _render_readme(operations: List[Operation], file_names: Dict[int, str]) -> str:
    groups: Dict[str, List[Operation]] = defaultdict(list)
    for operation in operations:
        groups[operation_group(operation)].append(operation)

    lines: List[str] = [
        "# 官方 Seller API 方法文档",
        "",
        "## 用途",
        "",
        "这里按官方 Chrome 抽取索引展开为每个 operation 一个 Markdown 文件，方便 AI 和人工直接检索方法、参数、返回结构和示例。",
        "",
        "## 生成信息",
        "",
        f"- 方法页数量：{len(operations)}",
        "- 来源：`indexes/official-seller-api.operations.json`",
        "- 生成器：`tools/generate_official_api_docs.py`",
        "- 重新生成：`python3 tools/generate_official_api_docs.py`",
        "",
        "## 方法目录",
        "",
    ]

    for group in sorted(groups):
        lines.extend([f"### {group}", ""])
        for operation in sorted(groups[group], key=lambda item: (str(item.get("path")), str(item.get("operationId")))):
            idx = operations.index(operation)
            filename = file_names[idx]
            title = str(operation.get("title") or operation.get("operationId") or filename)
            operation_id = str(operation.get("operationId") or title)
            method = str(operation.get("method") or "").upper()
            path = str(operation.get("path") or "")
            label = title if title != operation_id else operation_id
            lines.append(f"- [{label}]({filename}) - `{method} {path}` - `{operation_id}`")
        lines.append("")

    return "\n".join(lines)


def _load_operations(index_path: Path) -> List[Operation]:
    data = json.loads(index_path.read_text(encoding="utf-8"))
    operations = data.get("operations", [])
    if not isinstance(operations, list):
        raise ValueError("official Seller API index must contain an operations list")
    return operations


def generate_docs(index_path: Path, output_dir: Path) -> int:
    operations = _load_operations(index_path)
    output_dir.mkdir(parents=True, exist_ok=True)
    for old_file in output_dir.glob("*.md"):
        old_file.unlink()

    file_names: Dict[int, str] = {}
    seen: Dict[str, int] = {}
    for idx, operation in enumerate(operations):
        filename = slugify_operation(operation)
        if filename in seen:
            seen[filename] += 1
            stem = filename[:-3]
            filename = f"{stem}-{seen[filename]}.md"
        else:
            seen[filename] = 1
        file_names[idx] = filename
        (output_dir / filename).write_text(render_operation_doc(operation), encoding="utf-8")

    readme = _render_readme(operations, file_names)
    (output_dir / "README.md").write_text(readme, encoding="utf-8")
    return len(operations)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--index",
        type=Path,
        default=Path("indexes/official-seller-api.operations.json"),
        help="Path to Chrome-captured official Seller API JSON index.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("docs/api/official"),
        help="Directory for generated Markdown docs.",
    )
    args = parser.parse_args()
    count = generate_docs(args.index, args.output)
    print(f"generated {count} operation docs")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

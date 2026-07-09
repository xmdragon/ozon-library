# Antibot Incident

## 用途

记录 Ozon abt-challenge incident 封禁页的识别和处理。

## AI 摘要

abt-challenge incident 会伪装成无网络连接页，但本质是反爬封禁/incident。AICollection 使用 `img[src*="abt-challenge/incidents"]`、带 `incident_id` 的 complaint/support 链接，以及 `fab_<segment>_<timestamp>` 文本识别。命中后应归入 antibot marker，并抑制 NoConnection，避免把可重试反爬误报成致命网络问题。

## 关键标记

| 标记 | 说明 |
| --- | --- |
| `img[src*="abt-challenge/incidents"]` | incident 专属图片路径。 |
| `a[href*="/complaint/support/"][href*="incident_id="]` | 投诉/支持链接。 |
| `fab_[a-z0-9]+_[0-9]{8,}` | challenge id 文本 fallback。 |
| 标题含 `нет соединения` | 可能是伪装，不可单独判 NoConnection。 |

## 处理流程

1. page-state 先检测 incident 专属 DOM。
2. 如果命中，设置 `is_antibot_incident=true`。
3. 加入 `antibot_markers: page:abt-challenge-incident`。
4. 抑制 `is_no_connection`。
5. 交给 antibot/recovery 链路，而不是网络错误分支。

## 异常与恢复

| 情况 | 处理 |
| --- | --- |
| incident reload 后降级到 slider | 重新跑 page-state；若出现 slider marker，再调 slider gate。 |
| 只有无网络文案无 incident DOM | 按 NoConnection 处理。 |
| 图床或链接变化 | 使用三重 fallback：图片、support 链接、fab 文本。 |

## 来源引用

- `/Users/eric/works/AICollection/src-tauri/crates/scraper/src/services/page_state.rs`
- `/Users/eric/works/AICollection/docs/changelog/2026-07-09-pr1406-ozon-block-page-flow.md`
- `indexes/dom-selectors.json`

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

## Chrome 无痕实测：`fab_nmk`（2026-09-29）

- 环境：macOS Chrome 新无痕窗口、未登录 Ozon。先直接访问中国商品搜索页，再关闭无痕窗口、重新打开并从 `https://www.ozon.ru/` 首页进入。两次都出现 Ozon 自身的事件页；首页没有搜索框，因此未能按页面流程继续搜索。普通 Chrome 会话中的同一搜索页当时仍能显示商品，不能仅凭无痕页文案推断本机断网。
- DevTools Network 对首页 `GET https://www.ozon.ru/` 的实测：`403 Forbidden`，`Content-Type: text/html`，`Ozon-Antibot: 1`，`Server: nginx`；响应时间头为 `Tue, 29 Sep 2026 01:26:43 GMT`，`Server-Timing` 的 RequestID 为 `9ac8a7b4d65f13b140483c0ffffe3e43`，资源大小约 5.3 kB。这是 HTML 文档响应，不是 `entrypoint-api.bx/page/json/v2` 的 200 JSON。
- 文档 `<title>`：`Похоже, нет соединения`；可见标题：`Похоже, нет соединения`；正文提示关闭 VPN、重启路由器或换网络。HTML 同时含 `abt-challenge/incidents/images/warn.png`、`/complaint/support/?incident_id=...&token=...` 和 `fab_nmk_20260929012643_01M3NCAWNKKVDPTX92T2774XAN`，足以将该“无连接”外观归入 Ozon antibot incident，而非仅按文案归类。
- 页内只有“刷新页面”和“联系支持”操作，没有可见滑块或验证码控件。搜索页地址被 Ozon 加上 `__rr=1`；刷新后仍是新的 `fab_nmk` 事件号。新无痕窗口从首页访问时也被重定向到 `/?__rr=1` 的同类事件页。
- 第三方 Cookie 对照：在另一个无痕会话的 `ozon.ru` 站点信息中，将“第三方 Cookie”从“已屏蔽”切为“已允许”；Chrome 地址栏随后明确显示“已允许使用第三方 Cookie”。再访问不带 `__rr` 的首页，仍返回 `fab_nmk_20260929013921_01M3ND2153EJPD2SQ3S7JPCWCD`；访问原搜索 URL，仍返回 `fab_nmk_20260929014009_01M3ND3FMZGJ0H1GF8PCBSHJZ3`。这说明**在该次已受拦截的无痕会话中，临时放行本身不足以解除事件页**；不能据此断言第三方 Cookie 是唯一根因，也不能排除先前站点数据、网络或风控状态的影响。未更改 Chrome 全局 Cookie 设置。
- [脱敏的完整 HTML 响应体](fixtures/fab-nmk-403-2026-09-29.html.txt) 保留原始标签、样式、图片路径、标题、事件号和刷新脚本；支持链接的 `token` 值已替换为 `[REDACTED]`。响应头中的 `Set-Cookie` 和请求 Cookie 不入库。
- 此样本**不能**证明 HTTP 200 验证 JSON 的验证码标记会落在第 2000 字符之后；它只证实无痕会话可遇到独立的 403 antibot incident 页面。

## 来源引用

- `/Users/eric/works/AICollection/src-tauri/crates/scraper/src/services/page_state.rs`
- `/Users/eric/works/AICollection/docs/changelog/2026-07-09-pr1406-ozon-block-page-flow.md`
- `indexes/dom-selectors.json`

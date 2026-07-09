# NoConnection 和 Block 页面

## 用途

记录 Ozon 自渲染无网络页、block 页、Chrome error 和 antibot incident 的区别。

## AI 摘要

Ozon 的 “NoConnection” 不一定是真网络断开。AICollection 将 `block.html`、俄文/中文无网络文案、Chrome error、abt-challenge incident 分开处理。abt-challenge incident 会伪装成“нет соединения”，但如果有 `abt-challenge/incidents` 图片、complaint/support incident 链接或 `fab_<id>_<timestamp>`，应归入 antibot，而不是致命无网络。

## 关键标记

| 标记 | 分类 |
| --- | --- |
| URL 包含 `/block.html` | Ozon block/no connection 页，通常进入限流/恢复。 |
| URL 包含 `/captcha.html` | captcha 页面。 |
| 标题/正文含 `нет связи`、`нет соединения`、`проверьте подключение` | NoConnection 文案。 |
| 正文含 `似乎没有网络连接`、`请关闭vpn`、`连接到其他网络` | 中文 NoConnection 文案。 |
| `chrome-error://` | 浏览器加载异常，不等同 Ozon 服务器限流。 |
| `img[src*="abt-challenge/incidents"]` | antibot incident。 |
| `a[href*="/complaint/support/"][href*="incident_id="]` | antibot incident。 |
| `fab_[a-z0-9]+_[0-9]{8,}` | incident 文本 fallback。 |

## 判定流程

1. 读取 URL、title、body preview、iframe marker。
2. 先判断 antibot incident，命中后抑制 `is_no_connection`。
3. 判断 block/captcha URL。
4. 判断 NoConnection 文案。
5. 检查是否有商品内容；如果有商品内容，不应因为正文词误判无网络。
6. 输出结构化 page state，交给 recovery。

## 异常与恢复

| 情况 | 处理 |
| --- | --- |
| Chrome error | 提示页面加载异常，用户可重试。 |
| Ozon block/no connection 且无商品内容 | 进入限流/profile 轮换或暂停。 |
| antibot incident | 作为可重试反爬处理，不能报普通无网络。 |
| 商品页正文含“连接”等词 | 因有商品内容，不能误判 NoConnection。 |

## 来源引用

- `/Users/eric/works/AICollection/src-tauri/crates/scraper/src/services/page_state.rs`
- `/Users/eric/works/AICollection/src-tauri/crates/scraper/src/services/ozon_rate_limit.rs`
- `indexes/dom-selectors.json`

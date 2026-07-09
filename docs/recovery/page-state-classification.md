# 页面状态分类

## 用途

记录 scraper/WebView 在 Ozon 页面上应如何分类当前状态。

## AI 摘要

AICollection 的 `PageStateProbe` 是当前最完整的状态模型。它输出 URL、标题、预览、是否有密码输入、reload 按钮、antibot markers、suspicious markers、slider DOM、商品内容、NoConnection、antibot incident、成人生日页、成人确认页、售罄、Chrome error、readyState、body 长度、店铺名等字段。

## 关键字段

| 字段 | 含义 |
| --- | --- |
| `antibot` | 是否命中明确反爬 marker。 |
| `antibot_markers` | 例如 `page:abt-challenge-incident`、硬限流页。 |
| `suspicious_markers` | captcha/block/slider/robot-check 等可疑信号。 |
| `has_slider_captcha_dom` | 同时看到 slider、背景、puzzle、captcha。 |
| `has_product_content` | 看到商品/列表内容 widget 或价格元素。 |
| `is_no_connection` | Ozon 自渲染无网络页；incident 会抑制该字段。 |
| `is_antibot_incident` | abt-challenge incident 封禁页。 |
| `has_adult_birthdate_form` | 成人生日输入页。 |
| `has_adult_confirm18` | 成人确认页。 |
| `is_sold_out` | 售罄状态。 |
| `is_chrome_error` | 浏览器加载错误。 |

## 分类顺序

1. 收集 URL、title、body text、iframe marker。
2. 判断 captcha/block URL。
3. 识别 antibot incident。
4. 识别 slider captcha 文本和 DOM。
5. 识别商品内容。
6. 识别 NoConnection，但 incident 命中时抑制。
7. 识别成人验证和售罄。
8. 输出 probe 给 rate-limit、recovery、collector 使用。

## 异常与恢复

状态分类不直接修复页面，只提供结构化信号。恢复策略见：

- `docs/recovery/slider-captcha.md`
- `docs/recovery/antibot-incident.md`
- `docs/buyer-page/adult-verification.md`
- `docs/buyer-page/no-connection-and-block.md`

## 来源引用

- `/Users/eric/works/AICollection/src-tauri/crates/scraper/src/services/page_state.rs`
- `/Users/eric/works/AICollection/src-tauri/crates/scraper/src/services/page_state_helpers.rs`

# 成人验证

## 用途

记录 Ozon 成人商品验证页/弹窗的检测和恢复策略。

## AI 摘要

成人验证常见形态有生日输入页和 confirm-only 页。AICollection 使用 `userAdultModal`、生日输入控件、俄文文案和确认文案识别成人验证。较新实现强调 DOM-first submit：生日页和 confirm-only 页不能混用请求体，确认页提交生日可能导致 403。遇到 antibot/captcha 时应短路交给 recovery，不要尝试成人确认。

## 关键 DOM/状态

| 标记 | 用途 |
| --- | --- |
| `[data-widget="userAdultModal"]` | 成人弹窗主容器。 |
| `input[type="date"]` | 生日输入。 |
| `input[name*="birth" i]`、`select[name*="birth" i]` | 生日控件 fallback。 |
| `предназначен только для лиц, достигших 18 лет` | 成人页文案。 |
| `подтвердите, что вы старше 18 лет` | confirm-only 文案。 |

## 流程

1. 先跑 page-state probe。
2. 如果页面是 antibot/captcha/block，交给 recovery。
3. 如果是生日页，在 `userAdultModal` 范围内定位生日控件并填入合规日期。
4. 如果是 confirm-only 页，只点击确认，不提交生日 payload。
5. 提交后重新检查商品内容、成人弹窗是否消失、是否进入 block/captcha。

## 异常与恢复

| 情况 | 处理 |
| --- | --- |
| 成人提示未检测到 | 返回 diagnostic，不要误判 completed。 |
| 提交按钮 disabled | 报 `submit_disabled`，等待或重试 DOM。 |
| 填生日失败 | 报 `fill_failed`，保留诊断信息。 |
| 页面转 antibot | 返回 `AntibotBlocked` 或 recovery 类型。 |
| confirm-only 带生日提交 | 禁止；项目注释指出会触发 403。 |

## 来源引用

- `/Users/eric/works/AICollection/src-tauri/crates/scraper/src/services/page_state.rs`
- `/Users/eric/works/AICollection/src-tauri/crates/scraper/src/services/queue/engine.rs`
- `/Users/eric/works/ZhiPin/ozon_spider/spider.py`

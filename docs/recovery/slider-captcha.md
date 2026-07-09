# 滑块验证码

## 用途

记录 Ozon slider captcha 的识别和恢复策略。

## AI 摘要

滑块验证码可通过文本和 DOM 双路径识别。AICollection 同时检查俄文、中文、英文提示，以及 `#slider`、`#slider-background`、`#puzzle`、`#captcha` 或相关 class。恢复时优先对真实 slider 调 slider gate；如果是 antibot incident 而没有 slider marker，则不应误调滑块。

## 关键标记

| 类型 | 标记 |
| --- | --- |
| URL | `/captcha.html`、`__rr=1` 且含 captcha 文案 |
| 俄文文案 | `передвиньте ползунок`、`чтобы пазл попал в контур`、`подтвердите, что вы не бот` |
| 中文文案 | `请拖动滑块`、`将拼图移入轮廓`、`请确认您不是机器人` |
| 英文文案 | `drag the slider`、`verify you are not a bot` |
| DOM | `#slider`、`#slider-background`、`#puzzle`、`#captcha`、`slider-handle`、`slider-track` |

## 恢复流程

1. page-state 先确认是 slider，而不是 incident。
2. 调用 slider gate 驱动页面前进。
3. 成功后再次等待终态：商品内容、列表内容、成人页或其他明确状态。
4. 如果 slider 后仍未到终态，回退 recovery/rotate。
5. pause/cancel 必须向上返回，不能吞掉。

## 异常与恢复

| 情况 | 处理 |
| --- | --- |
| slider DOM 不完整 | 不强行解，回到 page-state/recovery。 |
| incident 页图片也来自 abt-challenge | 必须用 `/incidents/` 收窄 incident 判断，避免误判普通 slider。 |
| 解锁失败 | 回退 rotate 或 profile/session 恢复。 |
| stop/pause | 立即停止或上抛。 |

## 来源引用

- `/Users/eric/works/AICollection/src-tauri/crates/scraper/src/services/page_state.rs`
- `/Users/eric/works/AICollection/src-tauri/crates/scraper/src/services/slider/`
- `/Users/eric/works/AICollection/src-tauri/crates/scraper/src/services/queue/engine.rs`

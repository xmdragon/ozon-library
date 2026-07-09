# AICollection 来源记录

## 用途

记录 `/Users/eric/works/AICollection` 对 Ozon 资料库的贡献范围、当前 revision 和优先阅读路径。

## AI 摘要

AICollection 是当前最重要的 Ozon scraper/WebView/recovery 来源。它提供较新的页面状态分类、NoConnection/block/antibot incident 识别、滑块处理、成人验证、队列恢复、Seller web 内部 API 和批量采集流程。

AICollection 的项目经验以 scraper/recovery、队列、WebView、扩展桥和 incident changelog 为主；官方 API 参数本身不从项目副本提取，只用源码中的实际调用方式和异常处理策略。

## 当前来源

- 路径：`/Users/eric/works/AICollection`
- 分支：`main`
- revision：`5ef346a13996c48024d9a13656357c91600b6586`
- 相关文件索引：见 `indexes/source-files.json`

## 重点贡献

| 主题 | 说明 | 优先路径 |
| --- | --- | --- |
| 页面状态分类 | content/no connection/chrome error/block/captcha/adult/antibot incident | `src-tauri/crates/scraper/src/services/page_state.rs` |
| 限流与 block | Ozon 页面阻塞、Seller API blocked status、rate-limit 分类 | `src-tauri/crates/scraper/src/services/ozon_rate_limit.rs` |
| Seller web API | `what_to_sell/data/v3`、`get_sellers`、`create-bundle`、Seller search | `src-tauri/crates/scraper/src/services/ozon_seller.rs`、`src-tauri/crates/scraper/src/browser/seller.rs` |
| 滑块 | slider gate、图片资源、鼠标轨迹、错误分类 | `src-tauri/crates/scraper/src/services/slider/` |
| 成人验证 | `userAdultModal`、生日页、confirm-only、DOM-first submit | `src-tauri/crates/scraper/src/services/queue/engine.rs` |
| 批量流程 | SKU 调度、collector、supplement、black price、sales | `src-tauri/crates/scraper/src/services/pipeline/` |
| 历史 incident | Ozon block、captcha、WebView、NoConnection、seller cookie 修复记录 | `docs/changelog/`、`tasks/` |

## 合并规则

AICollection 中较新的 scraper/recovery 行为通常作为当前行为优先写入主题文档。若 ZhiPin 或 simple-collection 中存在不同实现，需要在 source note 中记录差异，而不是覆盖 AICollection 的当前修复。

## 来源引用

- `indexes/source-files.json`
- `indexes/endpoint-cross-reference.json`
- `indexes/dom-selectors.json`

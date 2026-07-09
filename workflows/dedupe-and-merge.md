# 去重与合并流程

## 目标

把多个项目里的重复 Ozon 逻辑提炼成一份可复用主题文档，同时保留项目差异和来源证据。

## 合并步骤

1. 从索引中找出同一 endpoint、selector、状态标记或流程在多个项目中的出现位置。
2. 阅读最新实现和相关 tests/changelog，判断哪个实现代表当前可靠行为。
3. 把共享结论写入对应主题文档。
4. 把项目差异写入 `docs/source-notes/<project>.md`。
5. 如果来源冲突，保留冲突说明，不强行抹平。
6. 对不稳定 DOM 和内部 API 标注“观察到的行为”，并写明观察日期或来源 revision。

## 冲突处理

- AICollection 的较新 scraper/recovery 修复通常优先作为当前行为。
- ZhiPin 的旧 spider、后端 client 和 tests 常用于补充历史原因、fallback 和字段模型。
- simple-collection 的扩展实现常用于补充轻量 DOM 捕获、API 捕获和页面韧性。
- 官方 Seller API 与项目实现不一致时，主题文档同时记录官方定义和项目实际兼容逻辑。

## 文档落点

- 官方 Seller API：`docs/api/`
- Seller 登录态内部接口：`docs/seller-web/`
- Ozon 买家页 DOM：`docs/buyer-page/`
- 页面阻塞、滑块、成人验证、恢复：`docs/recovery/`
- 字段对照：`docs/fields/`
- 端到端流程：`docs/flows/`

## 保留来源

每篇主题文档末尾保留 `## 来源引用`，列出支持该文档的源码路径、operation ID 或索引文件。

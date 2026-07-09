# Ozon 资料库

这是一个面向 AI 使用、也方便人工查阅的 Ozon 资料库。它整合并提炼以下来源中的可复用知识：

- `/Users/eric/works/AICollection`
- `/Users/eric/works/simple-collection`
- `/Users/eric/works/ZhiPin`
- 当前 Chrome 中打开的 Ozon Seller API 官方文档

资料库按主题组织，不按项目重复堆内容。项目差异、历史实现和具体来源放在 `docs/source-notes/` 与 `indexes/` 中追溯。

## 快速导航

- `docs/api/`：官方 Seller API、后端调用方式、参数、返回值、限流和废弃接口。
- `docs/seller-web/`：需要 Seller 登录态的内部接口、登录流程、Seller 页面 API 和数据流。
- `docs/buyer-page/`：Ozon 买家页 DOM、列表页/商品页结构、价格字段、成人验证和 NoConnection。
- `docs/recovery/`：页面状态识别、滑块、反爬 incident、限流、WebView 恢复。
- `docs/fields/`：商品、库存、价格、订单、类目属性等字段对照。
- `docs/flows/`：SKU 采集、批量刊登、Seller cookie/session、类目属性同步等流程。
- `docs/source-notes/`：按来源记录每个项目贡献的知识和差异。
- `indexes/`：机器可读索引，供 AI 检索、差异比较和后续刷新使用。
- `workflows/`：维护资料库的操作流程。
- `skills/ozon-library-maintainer/`：仓库本地维护 skill，不安装到全局。

## 来源规则

官方 Seller API 文档必须通过 Chrome 当前页面抽取，不使用直接下载或外部抓取替代。抽取结果写入 `indexes/official-seller-api.operations.json`，再从索引整理到主题文档。

本地项目资料先进入索引，再进入主题文档。每条非显而易见的结论都应该能追溯到源码路径、官方 operation ID 或 source note。

## 复用提炼原则

同一逻辑在多个项目中出现时：

1. 共享知识写入主题文档。
2. 项目差异写入 `docs/source-notes/<project>.md`。
3. 新旧实现冲突时，优先记录当前更可靠的实现，同时保留旧实现暴露出的 fallback、legacy endpoint 或历史 incident。
4. Ozon DOM selector 和 Seller 内部 API 都按“不稳定观察值”处理，记录观察日期和来源。

## 安全边界

不要提交以下内容：

- API key、Client ID 实值、cookie、token、session、验证码、短信码。
- 真实账号私有信息、订单隐私、买家隐私或店铺敏感数据。
- 可直接复用到生产账号的私密请求头。

文档中可以记录字段名、header 名、接口路径、错误码、selector 和脱敏示例。

## 维护入口

未来更新资料库时，优先阅读：

1. `workflows/ozon-library-update.md`
2. `skills/ozon-library-maintainer/SKILL.md`
3. `indexes/source-files.json`
4. `docs/source-notes/`

设计和实施计划位于：

- `docs/superpowers/specs/2026-07-09-ozon-library-design.md`
- `docs/superpowers/plans/2026-07-09-ozon-library-implementation.md`

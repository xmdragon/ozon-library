# Ozon 资料库设计

## 目标

把 `xmdragon/ozon-library` 建成一个面向 AI 使用、也方便人工查阅的 Ozon 资料库。资料库需要整合四个来源：

- `/Users/eric/works/AICollection`
- `/Users/eric/works/simple-collection`
- `/Users/eric/works/ZhiPin`
- 当前 Chrome 打开的 Ozon Seller API 官方文档

资料库的重点不是把三个项目分别复制一遍，而是提炼可复用的 Ozon 知识单元。项目差异、历史实现和来源证据通过 source notes 和引用保留。

## 已观察到的上下文

`ozon-library` 当前是一个空仓库，分支为 `main`。

三个活跃本地项目位于 `/Users/eric/works`：

- `AICollection`：大型 Ozon 桌面端和 scraper 实现，包含 WebView、页面状态识别、滑块处理、成人验证、队列恢复、Seller web API、商品采集和大量 changelog。
- `ZhiPin`：大型 Ozon 后端、浏览器扩展、Seller API client、Seller 登录、Seller 内部 API、模型、迁移、Web UI 和较早的 spider 实现。
- `simple-collection`：较小的浏览器扩展/API 捕获项目，适合作为 Ozon DOM 捕获、API 捕获、列表/卡片提取、币种语言处理和运行时韧性的来源。
- Chrome Seller API 页面：`https://docs.ozon.ru/api/seller/zh/?__rr=1`，是 Redoc 渲染页面，约有 280 个 operation block。每个 operation block 都可以通过 Chrome DOM 中的 `id="operation/<operationId>"` 抽取，并包含 method/path、参数、请求 schema、响应 schema 和示例。

官方 Seller API 文档必须通过 Chrome 抓取，不能通过直接 `curl` 或外部下载替代。

## 设计决策

采用“主题优先 + 来源引用”的知识库结构。

这样可以避免 AICollection 和 ZhiPin 中的共享逻辑被重复写多遍。项目维度只保留溯源和差异说明，真正可复用的知识放到稳定主题文档里。

不采用的方案：

- 按来源项目组织：溯源简单，但重复内容多，AI 检索时噪音大。
- 只做机器索引：适合脚本，但人工阅读体验差，启动成本也更高。

最终方案是：Markdown 主题文档作为主资料，JSON 索引作为脚本刷新和 AI 查找的辅助。

## 仓库结构

```text
ozon-library/
  README.md
  docs/
    api/
      seller-api-index.md
      seller-api-auth.md
      product.md
      stock-price.md
      posting-fbs.md
      warehouse.md
      reports-finance-chat.md
    seller-web/
      login-flow.md
      seller-internal-apis.md
      seller-data-v3.md
      search-and-create-bundle.md
      delivery-template-apis.md
    buyer-page/
      product-page-dom.md
      list-page-dom.md
      price-fields.md
      adult-verification.md
      no-connection-and-block.md
    recovery/
      page-state-classification.md
      slider-captcha.md
      antibot-incident.md
      rate-limit.md
      webview-recovery.md
    fields/
      product-fields.md
      seller-fields.md
      stock-price-fields.md
      posting-fields.md
      category-attribute-fields.md
    flows/
      sku-collection.md
      batch-listing.md
      seller-cookie-session.md
      category-attribute-sync.md
      price-stock-sync.md
    source-notes/
      AICollection.md
      ZhiPin.md
      simple-collection.md
      official-seller-api-chrome.md
  indexes/
    official-seller-api.operations.json
    source-files.json
    endpoint-cross-reference.json
    dom-selectors.json
  workflows/
    ozon-library-update.md
    chrome-official-seller-api-extract.md
    project-source-extract.md
    dedupe-and-merge.md
  skills/
    ozon-library-maintainer/
      SKILL.md
      references/
        repository-map.md
        source-map.md
```

## 文档格式

每篇主题 Markdown 文档使用下面的结构：

```markdown
# 标题

## 用途
这块知识解决什么问题。

## AI 摘要
给 AI 优先读取的高密度结论。

## 适用范围
说明在哪些项目、运行时、页面或 API 场景下有效。

## 关键接口
用表格记录 API、DOM selector、字段、请求 payload、响应 payload、事件或状态值。

## 流程
实际调用顺序、DOM 检测顺序、状态流转或恢复步骤。

## 异常与恢复
已知错误、阻塞状态、限流、fallback、重试上限和停止条件。

## 来源引用
用于生成本文档的绝对本地源码路径，或官方 Chrome operation ID。
```

每条非显而易见的知识都要能追溯来源。如果同一个事实在多个项目中出现，公共行为写入主题文档，项目差异写入 `docs/source-notes/`。

## 官方 Seller API 抓取

官方 Seller API 内容必须来自 Chrome。

当前页面暴露了类似下面的 operation section：

- `operation/ProductAPI_ImportProductsV3`
- `operation/ProductAPI_ProductsStocksV2`
- `operation/PostingFbsList`
- `operation/AccessAPI_RolesByToken`

抽取器应使用 Chrome/Playwright DOM evaluation，把每个 operation block 投影成紧凑 JSON：

```json
{
  "operationId": "ProductAPI_ProductsStocksV2",
  "title": "更新库存商品的数量",
  "method": "post",
  "path": "/v2/products/stocks",
  "headings": [],
  "headerParameters": [],
  "requestSchemaText": "",
  "responseSchemaText": "",
  "requestExamples": [],
  "responseExamples": [],
  "sourceUrl": "https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/ProductAPI_ProductsStocksV2"
}
```

首轮抽取优先覆盖：

- 授权、`Client-Id`、`Api-Key`、密钥有效期、限流、CORS/backend-only 规则。
- 商品创建、属性、图片、商品列表、商品信息。
- 库存和价格更新。
- FBS/rFBS 货件。
- 仓库和配送方式。
- 报告、财务、聊天和角色。
- 已废弃端点及替代端点。

## 项目源码抽取

本地项目应先扫描成索引，再合并进文档。

重要来源类别：

- Seller API 后端 client：`ZhiPin/plugins/ef/channels/ozon/api/client.py` 和 `client_mixins/*`。
- Seller web 内部 API：`AICollection/src-tauri/crates/scraper/src/services/ozon_seller.rs`、`AICollection/src-tauri/crates/scraper/src/browser/seller.rs`、`ZhiPin/ozon_spider/seller_login.py`。
- 买家页 DOM 和商品数据抽取：AICollection scraper pipeline、ZhiPin extension product/list 模块、simple-collection extension。
- 页面状态与恢复：AICollection `page_state.rs`、`ozon_rate_limit.rs`、`challenge.rs`、slider 模块、queue recovery、adult verification 代码。
- 浏览器扩展 DOM 结构：ZhiPin extension 的 `seller-page`、`product-page`、`shop-binding`、`list-enhancer`；simple-collection 的 `content.js`、`api_parser.js`、`page_capture.js`。
- 数据库/模型字段：ZhiPin Ozon models 和 migrations，AICollection backend 与 Tauri stores。
- Changelog/incident：AICollection `docs/changelog/*ozon*`、相关 task notes，以及 ZhiPin 中说明行为修复的 tests/docs。

索引需要记录文件路径、匹配主题、endpoint、selector、状态字符串和重要注释。索引不能替代人工整理后的主题文档。

## 复用提炼规则

当多个项目中出现相同行为时：

1. 共享行为写入主题文档。
2. 实现差异写入 `docs/source-notes/<project>.md`。
3. 每条行为都链接支持它的源码路径。
4. 如果 AICollection 中的当前实现代表对 ZhiPin 旧逻辑的后续修复，优先采用 AICollection 的当前行为。
5. 如果 ZhiPin/simple-collection 的旧行为揭示了 fallback、legacy endpoint 或历史 incident，需要保留。
6. Ozon DOM selector 标注为“观察到的 selector”，不要当作永久契约。

可复用知识单元示例：

- Ozon 页面状态分类：内容页、NoConnection、Chrome error、block page、slider captcha、antibot incident、成人生日页、成人确认页。
- 滑块处理：检测标记、图片资源、解锁尝试、retry/rotate 行为、cancel/pause 传播。
- 成人验证：`userAdultModal`、生日输入、confirm-only 路径、403 敏感接口行为、较新代码中的 DOM-first submit。
- Seller API header 和限流。
- 需要已登录浏览器上下文和 `credentials: include` 的 Seller web 内部 API。
- Ozon 从 `webPrice` 切换到 `webSale` 后的商品价格提取。
- Seller 页面 widget 注入和 MutationObserver 重新注入。
- 通过 SKU search 加 create-bundle 获取 Seller 侧商品详情的流程。

## 仓库内 skill / workflow

创建仓库本地 skill：`skills/ozon-library-maintainer/SKILL.md`。

这个 skill 不安装到全局，只作为本仓库维护说明，供未来 Codex 会话使用。

它应指示 agent：

- 先读 `README.md`、`workflows/ozon-library-update.md` 和 `indexes/source-files.json`。
- 官方 Seller API 必须通过 Chrome 抽取。
- 三个本地项目通过源码扫描抽取。
- 编辑主题文档前先更新索引。
- 按可复用主题合并，不按项目重复堆内容。
- 对每条非显而易见的知识保留来源引用。
- 把 Ozon DOM 和 Seller 内部 API 当作不稳定接口，并标注观察日期。
- 不要提交 credential、API key、cookie、token 或账号私有数据。

## 工作流

`workflows/ozon-library-update.md` 定义顶层刷新顺序：

1. 确认 AICollection、simple-collection、ZhiPin 的源码路径和 Git revision。
2. 确认 Chrome 打开了官方 Seller API 页面。
3. 通过 Chrome DOM 抽取官方 operation，写入 `indexes/official-seller-api.operations.json`。
4. 扫描本地项目，写入 `indexes/source-files.json`、`endpoint-cross-reference.json` 和 `dom-selectors.json`。
5. 对比索引和现有文档。
6. 针对新增或变化的复用知识更新主题文档。
7. 用项目差异更新 source notes。
8. 运行链接/引用校验。
9. 提交时在 commit message 或更新记录里写明来源 revision。

`workflows/chrome-official-seller-api-extract.md` 记录 Chrome-only 官方文档抽取方法。

`workflows/project-source-extract.md` 记录 `rg` pattern、路径优先级和主题路由。

`workflows/dedupe-and-merge.md` 记录如何处理重复或冲突发现。

## 验收标准

第一版实现满足以下条件即可认为成功：

- 仓库拥有规划中的目录结构。
- README 说明人和 AI 应如何浏览资料库。
- 至少能通过 Chrome 生成官方 Seller API operation 索引，并且结构足以扩展到所有 operation。
- source indexes 覆盖三个本地项目，并按主题分类文件。
- 首批高价值主题文档已经存在：
  - Seller API 授权和请求规则。
  - 商品创建/list/info。
  - 库存和价格更新。
  - Seller web 内部 API。
  - 商品页/列表页 DOM。
  - 页面状态分类。
  - 滑块验证码。
  - 成人验证。
  - NoConnection/block/antibot incident recovery。
- 仓库本地 skill 和 workflows 已存在。
- 没有提交 secret、cookie、token 或账号私有数据。

## 实施说明

实施计划不应该试图一次性人工整理完 280 个官方 operation。第一阶段先完成：

- 仓库骨架；
- 抽取脚本或 Chrome snippet；
- 索引；
- 最高价值主题文档；
- maintainer workflow。

剩余官方 Seller API 内容可以之后从生成的 operation index 中逐步补齐。

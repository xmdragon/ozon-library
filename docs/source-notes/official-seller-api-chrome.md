# 官方 Seller API Chrome 来源记录

## 用途

记录官方 Ozon Seller API 文档的抽取方式、当前索引状态和使用限制。

## AI 摘要

官方 Seller API 资料必须通过 Chrome 当前页面抽取。当前索引文件为 `indexes/official-seller-api.operations.json`，来源页面标题为 `Ozon Seller API 文件`，本次从已渲染 DOM 中抽取到 264 个 `div[id^="operation/"]` operation block，并从 `#tag/News` 抽取到 149 条官方更新记录。

## 抽取方式

- 来源 URL：`https://docs.ozon.ru/api/seller/zh/?__rr=1`
- 抽取工具：Chrome browser control + Playwright DOM evaluation。
- 抽取 selector：`div[id^="operation/"]`。
- 抽取字段：`operationId`、`title`、`method`、`path`、`headings`、`tables`、`examples`、`sourceUrl`。
- `tables` 保留两种形态：`rows` 为 Chrome DOM 中 `tr` 的直接单元格结构，`text` 为兼容旧生成器的压平文本。
- 输出文件：`indexes/official-seller-api.operations.json`。
- News 输出文件：`indexes/official-seller-api.news.json`。
- News 合并脚本：`tools/apply_official_api_news.py`。
- News 总览文档：`docs/api/seller-api-news.md`。
- 展开文档：`docs/api/official/README.md` 和 264 个逐方法 Markdown 文件。
- 展开生成器：`tools/generate_official_api_docs.py`。

## 当前观察

- 页面由 Redoc 渲染。
- operation block 的 DOM id 形如 `operation/ProductAPI_ProductsStocksV2`。
- 每个 block 的 DOM 中通常包含：
  - 中文标题；
  - HTTP method 和 endpoint；
  - `header Parameters`；
  - `Request Body schema`；
  - `Response Schema`；
  - 请求/回复范例。
- Redoc 嵌套表格会产生父行和子行；生成 Markdown 时优先使用 `rows`，并跳过没有字段/说明两列的单列父行，避免 GitHub 上出现长段压缩文本。
- 当前渲染 DOM 抽取到 264 个 operation block。导航锚点数量可能更多，后续刷新时应记录 operation count 是否变化。
- 当前已从索引展开 264 个逐方法文档；重新抽取官方页面后，应先运行 `python3 tools/apply_official_api_news.py` 合并 News 生命周期与字段变更，再运行 `python3 tools/generate_official_api_docs.py` 更新方法页。
- News 当前识别出 9 个当前方法页的废弃标记，以及 30 个 News 中已移除或当前 operation 索引缺失的旧方法；这些旧方法应避免在新实现中使用。
- 参数或字段级别的弃用、移除、新增会保留在对应方法页的 `News 更新标记` 表格中，不会自动把整个方法标为废弃。

## 优先整理主题

- 授权：`AccessAPI_RolesByToken`、`Client-Id`、`Api-Key`、密钥有效期。
- 商品：`ProductAPI_ImportProductsV3`、`ProductAPI_GetProductList`、`ProductAPI_GetProductInfoList`、`ProductAPI_GetProductAttributesV4`。
- 库存/价格：`ProductAPI_ProductsStocksV2`、`ProductAPI_GetProductInfoStocks`、`ProductAPI_ImportProductsPrices`、`ProductAPI_GetProductInfoPrices`。
- FBS/rFBS 订单：`PostingFbsList`、`PostingAPI_GetFbsPostingV3`、`PostingAPI_ShipFbsPostingV4`。
- 仓库：`WarehouseListV2`、`WarehouseAPI_DeliveryMethodListV2`、FBS warehouse create/update/archive 系列。

## 限制

- 不通过直接下载、`curl` 或搜索引擎补齐官方文档。
- 不输入或保存真实 `Client-Id`、`Api-Key`。
- 官方文档示例可能包含公开样例姓名、地址和订单字段；用于字段理解时应继续按公开文档样例处理，不得混入真实账号数据。

## 来源引用

- Chrome 页面：`https://docs.ozon.ru/api/seller/zh/?__rr=1`
- Chrome News：`https://docs.ozon.ru/api/seller/zh/#tag/News`
- 索引：`indexes/official-seller-api.operations.json`
- News 索引：`indexes/official-seller-api.news.json`
- News 总览：`docs/api/seller-api-news.md`
- 全量方法目录：`docs/api/official/README.md`

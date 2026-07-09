# 官方 Seller API Chrome 来源记录

## 用途

记录官方 Ozon Seller API 文档的抽取方式、当前索引状态和使用限制。

## AI 摘要

官方 Seller API 资料必须通过 Chrome 当前页面抽取。当前索引文件为 `indexes/official-seller-api.operations.json`，来源页面标题为 `Ozon Seller API 文件`，本次从已渲染 DOM 中抽取到 264 个 `div[id^="operation/"]` operation block。

## 抽取方式

- 来源 URL：`https://docs.ozon.ru/api/seller/zh/?__rr=1`
- 抽取工具：Chrome browser control + Playwright DOM evaluation。
- 抽取 selector：`div[id^="operation/"]`。
- 抽取字段：`operationId`、`title`、`method`、`path`、`headings`、`tables`、`examples`、`sourceUrl`。
- 输出文件：`indexes/official-seller-api.operations.json`。

## 当前观察

- 页面由 Redoc 渲染。
- operation block 的 DOM id 形如 `operation/ProductAPI_ProductsStocksV2`。
- 每个 block 的文本中通常包含：
  - 中文标题；
  - HTTP method 和 endpoint；
  - `header Parameters`；
  - `Request Body schema`；
  - `Response Schema`；
  - 请求/回复范例。
- 当前渲染 DOM 抽取到 264 个 operation block。导航锚点数量可能更多，后续刷新时应记录 operation count 是否变化。

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
- 索引：`indexes/official-seller-api.operations.json`

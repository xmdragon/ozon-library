# Seller API 索引

## 用途

提供官方 Ozon Seller API 的主题导航，帮助 AI 和人工从 operation 索引快速定位文档。

## AI 摘要

官方 Seller API 当前通过 Chrome DOM 抽取到 `indexes/official-seller-api.operations.json`，包含 264 个 operation block。所有官方 API 调用都使用 `Client-Id` 和 `Api-Key` header，主流端点为 `POST /vN/...`。从 2025-05-16 起官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接请求会被 CORS 拒绝。

## 关键主题

| 主题 | 代表 operation | 说明 |
| --- | --- | --- |
| 授权 | `AccessAPI_RolesByToken` | 查询 API key 绑定的角色、方法和过期时间。 |
| 商品 | `ProductAPI_ImportProductsV3`、`ProductAPI_GetProductList`、`ProductAPI_GetProductInfoList` | 创建/更新商品、查询列表、按标识符获取详情。 |
| 类目属性 | `DescriptionCategoryAPI_GetTree`、`DescriptionCategoryAPI_GetAttributes`、`DescriptionCategoryAPI_GetAttributeValues` | 类目树、属性、字典值。 |
| 库存价格 | `ProductAPI_ProductsStocksV2`、`ProductAPI_ImportProductsPrices`、`ProductAPI_GetProductInfoPrices` | 更新库存、更新价格、查询价格。 |
| FBS/rFBS 货件 | `PostingFbsList`、`PostingAPI_GetFbsPostingV3`、`PostingAPI_ShipFbsPostingV4` | 查询、获取、组包/发货。 |
| 仓库 | `WarehouseListV2`、`WarehouseAPI_DeliveryMethodListV2` | 仓库列表、配送方式。 |
| 聊天/报告/财务 | `Chat*`、`Report*`、`Finance*` | 客服聊天、报表、财务数据。 |

## 使用方式

1. 先查 `indexes/official-seller-api.operations.json`。
2. 需要逐方法说明时，读 `docs/api/official/README.md`，里面链接到 264 个官方方法页。
3. 用 `operationId`、`path` 或中文标题定位 operation。
4. 再读对应主题文档，例如商品读 `docs/api/product.md`，库存价格读 `docs/api/stock-price.md`。
5. 如果项目实现和官方文档不一致，同时读 `docs/source-notes/ZhiPin.md` 和 endpoint cross-reference。

## 全量方法文档

- 目录：`docs/api/official/README.md`
- 生成器：`tools/generate_official_api_docs.py`
- 重新生成：`python3 tools/generate_official_api_docs.py`
- 当前数量：264 个 operation 方法页。

## 来源引用

- `indexes/official-seller-api.operations.json`
- `docs/source-notes/official-seller-api-chrome.md`

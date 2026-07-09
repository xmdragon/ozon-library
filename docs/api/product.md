# 商品 API

## 用途

记录商品创建、更新、查询、属性和图片相关的 Seller API 复用知识。

## AI 摘要

商品相关官方核心端点包括 `/v3/product/import`、`/v3/product/list`、`/v3/product/info/list`、`/v4/product/info/attributes`、`/v1/product/pictures/import`。ZhiPin 后端 client 以 `offer_id`、`product_id`、`sku` 三种标识之一查询，批量上限通常为 1000。商品创建/更新需要完整传递商品信息；属性、类目和值需要结合 description-category 系列接口。

## 关键接口

| 接口 | operation | 用途 | 关键字段 |
| --- | --- | --- | --- |
| `POST /v3/product/import` | `ProductAPI_ImportProductsV3` | 创建或更新商品 | `items`，返回 `task_id` |
| `POST /v1/product/import/info` | `ProductAPI_GetImportProductsInfo` | 查询导入任务状态 | `task_id` |
| `POST /v3/product/list` | `ProductAPI_GetProductList` | 商品列表 | `filter`、`last_id`、`limit` |
| `POST /v3/product/info/list` | `ProductAPI_GetProductInfoList` | 按标识符取详情 | `offer_id`、`product_id`、`sku` |
| `POST /v4/product/info/attributes` | `ProductAPI_GetProductAttributesV4` | 取商品属性 | `filter`、`limit`、`last_id` |
| `POST /v1/product/pictures/import` | `ProductAPI_ProductImportPictures` | 上传或更新图片 | `images`、`color_image`、`images360` |

## 流程

1. 用类目接口获取 `description_category_id`、类型和属性。
2. 准备商品 `items`，包括属性、条码、图片、尺寸、价格、币种。
3. 调 `/v3/product/import` 获取 `task_id`。
4. 调 `/v1/product/import/info` 轮询任务状态。
5. 用 `/v3/product/info/list` 或 `/v4/product/info/attributes` 校验最终商品详情。

## 异常与恢复

| 情况 | 处理 |
| --- | --- |
| 创建/更新超限 | 官方返回 429，并可能带 `Item-Retry-After`、`Item-Rate-Limit-Remaining`。 |
| 属性值不在 Ozon 字典 | 商品不会正确创建/更新，需先用 description-category 取值。 |
| 图片链接未变化 | 官方说明状态可能返回 `skipped`。 |
| `offer_id` 和 `product_id` 混用 | 查询接口通常要求同类型标识数组；价格接口中官方建议避免歧义。 |

## 来源引用

- 官方 operation：`ProductAPI_ImportProductsV3`、`ProductAPI_GetProductList`、`ProductAPI_GetProductInfoList`、`ProductAPI_GetProductAttributesV4`
- `/Users/eric/works/ZhiPin/plugins/ef/channels/ozon/api/client_mixins/products.py`
- `/Users/eric/works/ZhiPin/plugins/ef/channels/ozon/api/client_mixins/catalog.py`

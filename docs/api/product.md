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

## 同步数据分层

- `/v3/product/list` 适合做轻量成员清单：确认 `product_id`、`offer_id`、可见性和归档状态，不应因此自动拉取每个商品的全部 rich 数据。
- 详情、价格、库存、属性是四类独立数据。事件携带稳定 `product_id` 时优先定向刷新该商品；周期任务负责校验事件未覆盖的变化。
- ZhiPin 当前相关 endpoint 的单次官方上限并不完全相同。项目侧建议把 rich 批次统一限制为 500，使详情、价格、FBS 仓库库存和属性在同一内存边界内处理；这属于工程批次，不是官方统一上限。
- 商品创建或更新事件只有在定向读取和本地 upsert 成功后才算处理完成。未纳入持久任务结果的后台协程不能替代可重试同步。
- 稳定匹配先使用 Ozon `product_id`，再在同一店铺内用 `offer_id` 明确补充匹配；新商品不能因为本地尚无记录而直接跳过。

## 异常与恢复

| 情况 | 处理 |
| --- | --- |
| 创建/更新超限 | 官方返回 429，并可能带 `Item-Retry-After`、`Item-Rate-Limit-Remaining`。 |
| 属性值不在 Ozon 字典 | 商品不会正确创建/更新，需先用 description-category 取值。 |
| 图片链接未变化 | 官方说明状态可能返回 `skipped`。 |
| `offer_id` 和 `product_id` 混用 | 查询接口通常要求同类型标识数组；价格接口中官方建议避免歧义。 |
| 商品事件已确认但本地没有商品 | 定向同步必须执行 upsert，并让远端或数据库错误进入事件失败状态。 |
| 每日 rich 全量调用过多 | 先扩大受控批次，再将实时事件、轻量清单和低频 rich 校验明确拆分。 |

## 来源引用

- 官方 operation：`ProductAPI_ImportProductsV3`、`ProductAPI_GetProductList`、`ProductAPI_GetProductInfoList`、`ProductAPI_GetProductAttributesV4`
- `/Users/eric/works/ZhiPin/plugins/ef/channels/ozon/api/client_mixins/products.py`
- `/Users/eric/works/ZhiPin/plugins/ef/channels/ozon/api/client_mixins/catalog.py`

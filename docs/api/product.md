# 商品 API

## 用途

记录商品创建、更新、查询、属性和图片相关的 Seller API 复用知识。

## AI 摘要

商品相关官方核心端点包括 `/v3/product/import`、`/v3/product/list`、`/v3/product/info/list`、`/v4/product/info/attributes`、`/v1/product/pictures/import`。不同 endpoint 的官方批量上限不同；ZhiPin `6e19f3a` 当前实现使用多组不同的工程批次。商品创建/更新需要完整传递商品信息；属性、类目和值需要结合 description-category 系列接口。

## 关键接口

| 接口 | operation | 用途 | 关键字段 |
| --- | --- | --- | --- |
| `POST /v3/product/import` | `ProductAPI_ImportProductsV3` | 创建或更新商品 | `items`，返回 `task_id` |
| `POST /v1/product/import/info` | `ProductAPI_GetImportProductsInfo` | 查询导入任务状态 | `task_id` |
| `POST /v3/product/list` | `ProductAPI_GetProductList` | 商品列表 | `filter`、`last_id`、`limit` |
| `POST /v3/product/info/list` | `ProductAPI_GetProductInfoList` | 按标识符取详情 | `offer_id`、`product_id`、`sku` |
| `POST /v4/product/info/attributes` | `ProductAPI_GetProductAttributesV4` | 取商品属性 | `filter`、`limit`、`last_id` |
| `POST /v1/product/pictures/import` | `ProductAPI_ProductImportPictures` | 上传或更新图片 | `images`、`color_image`、`images360` |

## 已确认当前实现

- ZhiPin `origin/master` revision `6e19f3aedb3d732cad0f4b98191435d57b4ffa56` 的 `ProductFetcher` 使用 `/v3/product/list` 做列表分页，默认列表批次为 100；rich 详情、属性各为 100，价格为 1000，FBS 仓库库存为 500。它们是当前代码参数，不是官方统一上限。
- 商品同步服务会将列表结果与详情、价格、库存、属性读取后写入本地；这条周期同步链路不能证明商品 webhook 已经具备 durable upsert 语义。
- webhook ingress 会写入 `OzonWebhookEvent`，但 `product.create_or_update` handler 随后用 `spawn(_trigger_product_sync(...))` 启动定向读取；`_trigger_product_sync` 捕获异常并结束，`_update_product_from_api` 对本地不存在的商品直接记录并跳过。因而 `6e19f3a` 尚不能标为“商品 webhook 持久任务已完成”。

## 推荐模式

- 商品列表只确认成员和稳定标识，详情、价格、库存、属性按事件或校验计划定向读取；不要因列表返回就自动展开全部 rich 数据。
- 定向事件应进入可持久、可重试的任务，并等待按同店 `product_id` 优先、`offer_id` 次之的 upsert 结果；本地不存在的商品走创建路径，不能成功跳过。
- 将 rich 请求统一限制在工程批次 500 是推荐的内存边界，且不是官方统一上限；该目标未合并到 `origin/master`，不能写成 `6e19f3a` 已实现。

## 待运行观测参数

- 逐 endpoint 记录官方允许的 `limit`、请求次数、响应字节数、429/限流命中和单批内存占用，再决定是否采用 500；不能用一个 endpoint 的上限推断其他 endpoint。
- 记录 webhook 入库、定向读取、upsert 成功/失败和本地缺失商品数量；在这些运行数据可用前，不调整 rich 全量周期。
- 用低频完整校验比较 webhook 覆盖的商品与列表成员变化，确认定向同步没有遗漏后再降低 rich 全量读取频率。

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
| 商品事件已确认但本地没有商品 | 按推荐模式执行定向读取和 upsert，并让远端或数据库错误进入事件失败状态；当前 `6e19f3a` 的 handler 仍会跳过本地不存在的商品。 |
| 每日 rich 全量调用过多 | 先用运行观测验证受控批次，再将实时事件、轻量清单和低频 rich 校验明确拆分。 |

## 来源引用

- 官方 operation：`ProductAPI_ImportProductsV3`、`ProductAPI_GetProductList`、`ProductAPI_GetProductInfoList`、`ProductAPI_GetProductAttributesV4`
- 本地官方逐方法页：`docs/api/official/post-v3-product-list-ProductAPI_GetProductList.md`、`docs/api/official/post-v3-product-info-list-ProductAPI_GetProductInfoList.md`、`docs/api/official/post-v4-product-info-attributes-ProductAPI_GetProductAttributesV4.md`
- `/Users/eric/works/ZhiPin/plugins/ef/channels/ozon/api/client_mixins/products.py`
- `/Users/eric/works/ZhiPin/plugins/ef/channels/ozon/api/client_mixins/catalog.py`
- `/Users/eric/works/ZhiPin/plugins/ef/channels/ozon/services/sync/product_sync/product_fetcher.py`
- `/Users/eric/works/ZhiPin/plugins/ef/channels/ozon/webhooks/handler.py`

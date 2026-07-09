# 批量刊登流程

## 用途

记录 Ozon 批量刊登相关的高层流程，连接商品字段、类目属性、图片、价格、库存和任务状态。

## AI 摘要

批量刊登不是单个 API 调用，而是多阶段流程：准备 SKU/商品数据，匹配类目和属性，上传/准备图片，组装 `/v3/product/import` payload，提交后轮询 `/v1/product/import/info`，再更新价格和库存。AICollection 提供较新的批量队列、profile/session、补充采集和恢复逻辑；ZhiPin 提供后端模型、API client 和历史批量刊登服务。

## 流程

1. 准备商品基础数据：标题、描述、图片、尺寸、重量、价格、币种、条码、类目。
2. 类目属性同步：
   - `/v1/description-category/tree`
   - `/v1/description-category/attribute`
   - `/v1/description-category/attribute/values`
3. 组装 `items[]`。
4. 调 `/v3/product/import`，获取 `task_id`。
5. 调 `/v1/product/import/info` 轮询状态。
6. 上传/更新图片时注意 `/v1/product/pictures/import` 会用本次图片列表覆盖详情页图片。
7. 商品状态稳定后，更新价格 `/v1/product/import/prices`。
8. 更新库存 `/v2/products/stocks`。

## 异常与恢复

| 情况 | 处理 |
| --- | --- |
| 类目属性值不合法 | 回到类目字典值同步，不硬提交。 |
| 商品操作限流 | 读取 429 和 Item retry headers，进入队列节流。 |
| 图片链接不变 | 官方可能返回 `skipped`，需要按业务判断是否接受。 |
| 价格/库存局部失败 | 检查 `result[].errors`，逐条重试。 |
| 采集补充阶段被 block | 交给 page-state/recovery，不直接失败整批。 |

## 来源引用

- 官方 operation：`ProductAPI_ImportProductsV3`、`ProductAPI_GetImportProductsInfo`、`ProductAPI_ImportProductsPrices`、`ProductAPI_ProductsStocksV2`
- `/Users/eric/works/AICollection/src-tauri/crates/scraper/src/services/pipeline/`
- `/Users/eric/works/ZhiPin/plugins/ef/channels/ozon/services/batch_listing_service.py`
- `/Users/eric/works/ZhiPin/plugins/ef/channels/ozon/api/client_mixins/catalog.py`

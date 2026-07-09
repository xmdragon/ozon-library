# 库存和价格 API

## 用途

记录 Ozon 商品库存和价格更新、查询、限流及项目实现注意点。

## AI 摘要

库存更新使用 `POST /v2/products/stocks`，价格更新使用 `POST /v1/product/import/prices`。库存请求中每组商品-仓库需要 `warehouse_id`，官方说明一次最多 100 组商品-仓库，并且同一商品-仓库 30 秒内只能更新一次，否则 `result.errors` 可能出现 `TOO_MANY_REQUESTS`。价格更新一次最多 1000 个商品，ZhiPin 默认传 `currency_code`，并默认禁用自动定价/价格策略以避免手动价格被覆盖。

## 关键接口

| 接口 | operation | 用途 | 关键字段 |
| --- | --- | --- | --- |
| `POST /v2/products/stocks` | `ProductAPI_ProductsStocksV2` | 更新库存 | `stocks[].offer_id/product_id`、`stock`、`warehouse_id` |
| `POST /v4/product/info/stocks` | `ProductAPI_GetProductInfoStocks` | 查询 FBS/rFBS/FBP 库存 | `filter`、`cursor`、`limit` |
| `POST /v2/product/info/stocks-by-warehouse/fbs` | `GetProductInfoStocksByWarehouseFbsV2` | 查询 FBS 仓库库存 | `sku` 或 `offer_id` |
| `POST /v1/product/import/prices` | `ProductAPI_ImportProductsPrices` | 更新价格 | `prices[]` |
| `POST /v5/product/info/prices` | `ProductAPI_GetProductInfoPrices` | 查询价格 | `filter`、`cursor`、`limit` |

## 流程

库存：

1. 用 `/v2/warehouse/list` 或项目仓库缓存确定 `warehouse_id`。
2. 对每个库存项准备 `offer_id` 或 `product_id`、`stock`、`warehouse_id`。
3. 调 `/v2/products/stocks`。
4. 检查 `result[].updated` 和 `result[].errors`，不要只看 HTTP 200。

价格：

1. 准备 `offer_id` 或 `product_id`。
2. 传字符串形式 `price`，必要时传 `old_price`、`net_price`、`currency_code`。
3. 默认关闭自动动作或价格策略，避免覆盖手动价格。
4. 检查 `result[].updated` 和 `errors`。

## 异常与恢复

| 情况 | 处理 |
| --- | --- |
| 同一商品-仓库更新太密 | 等待 30 秒以上或进入队列节流。 |
| `warehouse_id` 缺失 | 先刷新仓库列表或走 Seller web/项目仓库缓存。 |
| 价格币种不匹配 | 使用店铺个人中心设置币种；项目中默认 CNY 仅适合特定场景。 |
| result 内局部失败 | 逐条处理 `errors`，不能把整批视为成功。 |

## 来源引用

- 官方 operation：`ProductAPI_ProductsStocksV2`、`ProductAPI_ImportProductsPrices`、`ProductAPI_GetProductInfoStocks`、`ProductAPI_GetProductInfoPrices`
- `/Users/eric/works/ZhiPin/plugins/ef/channels/ozon/api/client_mixins/products.py`
- `/Users/eric/works/AICollection/src-tauri/crates/scraper/src/services/queue/`

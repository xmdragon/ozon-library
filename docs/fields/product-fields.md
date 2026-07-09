# 商品字段

## 用途

整理 Ozon 商品相关标识和常用字段，避免在 Seller API、Seller web API、买家页 DOM 之间混淆。

## AI 摘要

常用标识包括 `sku`、`offer_id`、`product_id`、`variant_id`、`description_category_id`、`warehouse_id`。官方 Seller API 中 `sku` 是 Ozon 系统中的商品标识，`offer_id` 是卖家系统中的货号，`product_id` 是 Ozon 商品 ID。Seller web 内部 API 的 `variant_id` 常用于 `create-bundle-by-variant-id`。买家页 URL 中通常可以提取 SKU。

## 字段对照

| 字段 | 含义 | 常见来源 |
| --- | --- | --- |
| `sku` | Ozon 系统 SKU | 官方 API、买家页 URL、Seller web search |
| `offer_id` | 卖家系统商品货号 | 官方 API、ZhiPin models |
| `product_id` | Ozon 商品 ID | 官方 API、商品详情 |
| `variant_id` | Seller web 内部商品变体 ID | `/api/v1/search`、create-bundle |
| `description_category_id` | 类目标识 | 商品详情、类目属性接口 |
| `warehouse_id` | 仓库 ID | 库存/仓库 API |
| `posting_number` | FBS/rFBS 货件号 | posting API |
| `currency_code` | 币种 | 商品/价格接口 |

## 使用注意

- 官方 `product/info/list` 单次请求最多可按 `offer_id`、`product_id`、`sku` 传总计不超过 1000 个同类标识。
- 库存更新必须带 `warehouse_id`。
- 价格更新中同时传 `offer_id` 和 `product_id` 会造成歧义，官方建议只用一种。
- Seller web 的 `variant_id` 不是官方 Seller API 的主标识，主要用于内部 create-bundle。

## 来源引用

- 官方 operation：`ProductAPI_GetProductInfoList`、`ProductAPI_GetProductAttributesV4`、`ProductAPI_ProductsStocksV2`
- `/Users/eric/works/ZhiPin/plugins/ef/channels/ozon/models/`
- `/Users/eric/works/ZhiPin/ozon_spider/seller_login.py`
- `/Users/eric/works/AICollection/src-tauri/crates/scraper/src/services/ozon_seller.rs`

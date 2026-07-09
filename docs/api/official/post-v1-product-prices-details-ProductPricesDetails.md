# 获取商品价格的详细信息

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/product/prices/details`
- Operation ID：`ProductPricesDetails`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/ProductPricesDetails
- 分组：`product`

## 页面标题结构

- 获取商品价格的详细信息
- header Parameters
- Request Body schema: application/json
- 回复
- Response Schema: application/json
- 请求范例
- 回复范例

## 参数与返回结构

### 表格 0

Client-Id required string 用户识别号。 Api-Key required string API-密钥。

### 表格 1

skus required Array of strings <int64> [ 1 .. 1000 ] items SKU列表。

### 表格 2

pricesArray of objects 商品价格。 Array ()customer_priceobject 网站上的商品价格。 discount_percentnumber <float> Deprecated 由 Ozon 承担的折扣比例。 offer_idstring 卖家系统中的商品标识符（商品货号）。 priceobject 商品价格（已包含促销活动或推广优惠）。 price_indexesArray of objects 价格指数。 skuinteger <int64> Ozon 系统中的商品标识符——SKU。

### 表格 3

customer_priceobject 网站上的商品价格。 discount_percentnumber <float> Deprecated 由 Ozon 承担的折扣比例。 offer_idstring 卖家系统中的商品标识符（商品货号）。 priceobject 商品价格（已包含促销活动或推广优惠）。 price_indexesArray of objects 价格指数。 skuinteger <int64> Ozon 系统中的商品标识符——SKU。

## 示例

### 示例 0

```json
{"skus": ["string"]}
```

### 示例 1

```json
{"prices": [{"customer_price": {"amount": "string","currency": "string"},"discount_percent": 0,"offer_id": "string","price": {"amount": "string","currency": "string"},"price_indexes": [{"external_index_data": {"min_price": {"amount": "string","currency": "string"},"price_index": 0,"url": "string"},"self_index_data": {"min_price": {"amount": "string","currency": "string"},"price_index": 0,"url": "string"}}],"sku": 0}]}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

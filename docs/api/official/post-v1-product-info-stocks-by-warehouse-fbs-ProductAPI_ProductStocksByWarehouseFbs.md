# 关于卖家库存余额的信息

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/product/info/stocks-by-warehouse/fbs`
- Operation ID：`ProductAPI_ProductStocksByWarehouseFbs`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/ProductAPI_ProductStocksByWarehouseFbs
- 分组：`product`

## 页面标题结构

- 关于卖家库存余额的信息
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

sku required Array of strings <int64> Ozon系统中的商品识别码是SKU。 offer_idArray of strings <int64> 卖家系统中的商品识别码是卖家系统中的商品标识符是商品货号。

### 表格 2

resultArray of objects 该处理方法的结果。 Array ()skuinteger <int64> Ozon系统中的商品识别码是SKU。 offer_idstring <int64> 卖家系统中的商品识别码是卖家系统中的商品标识符是商品货号。 presentinteger <int64> 库存商品总量。 product_idinteger <int64> 卖家系统中的Ozon系统中商品的标识符 — product_id。 reservedinteger <int64> 仓库中的保留商品的数量。 warehouse_idinteger <int64> 仓库编号。 warehouse_namestring 仓库名称。

### 表格 3

skuinteger <int64> Ozon系统中的商品识别码是SKU。 offer_idstring <int64> 卖家系统中的商品识别码是卖家系统中的商品标识符是商品货号。 presentinteger <int64> 库存商品总量。 product_idinteger <int64> 卖家系统中的Ozon系统中商品的标识符 — product_id。 reservedinteger <int64> 仓库中的保留商品的数量。 warehouse_idinteger <int64> 仓库编号。 warehouse_namestring 仓库名称。

## 示例

### 示例 0

```json
{"sku": ["string"],"offer_id": ["string"]}
```

### 示例 1

```json
{"result": [{"sku": 0,"offer_id": "string","present": 0,"product_id": 0,"reserved": 0,"warehouse_id": 0,"warehouse_name": "string"}]}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

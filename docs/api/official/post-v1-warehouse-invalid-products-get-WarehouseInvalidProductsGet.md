# 获取配送受限商品列表

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/warehouse/invalid-products/get`
- Operation ID：`WarehouseInvalidProductsGet`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/WarehouseInvalidProductsGet
- 分组：`warehouse`

## 页面标题结构

- 获取配送受限商品列表
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

last_idinteger <int64> 页面上最后一个值的标识符。首次请求时请将此字段留空。 如需获取后续数据，请填写上次响应中的 last_id。 warehouse_id required integer <int64> 仓库标识符。请通过方法/v1/warehouse/warehouses-with-invalid-products获取该参数值。

### 表格 2

has_nextboolean 若响应中未包含全部商品，则为true。 last_idinteger <int64> 页面上最后一个值的标识符。要获取下一个批次的数据，请在下一个请求的 last_id 参数中传递上次获取的值。 validation_resultsArray of objects 检查结果。 warehouse_idinteger <int64> 仓库标识符。

## 示例

### 示例 0

```json
{"last_id": 0,"warehouse_id": 0}
```

### 示例 1

```json
{"has_next": true,"last_id": 0,"validation_results": [{"item": {"size": {"height_mm": 0,"length_mm": 0,"width_mm": 0},"sku": 0,"weight_g": 0},"state": "UNSPECIFIED","validation_errors": [{"characteristic": "UNSPECIFIED","restriction_price": {"currency": "string","value": 0},"restriction_vwc": 0,"template_id": 0,"type": "UNSPECIFIED"}]}],"warehouse_id": 0}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

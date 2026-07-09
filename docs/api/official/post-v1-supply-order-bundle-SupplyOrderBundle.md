# 交货或交货申请的商品组成

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/supply-order/bundle`
- Operation ID：`SupplyOrderBundle`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/SupplyOrderBundle
- 分组：`supply-order`

## 页面标题结构

- 交货或交货申请的商品组成
- Request Body schema: application/json
- 回复
- Response Schema: application/json
- 请求范例
- 回复范例

## 参数与返回结构

### 表格 0

| 字段 | 类型/说明 |
| --- | --- |
| `bundle_ids` required | Array of strings [ 1 .. 100 ] items 交货商品组成的标识符。可通过方法 /v3/supply-order/get 获取。 |
| `is_asc` | boolean 传入 true 表示按升序排序。 |
| `item_tags_calculation` | object 用于计算产品标签的仓库列表。 |
| `last_id` | string 当前页面中最后一个 SKU 值的标识符。 |
| `limit` required | integer <int32> [ 1 .. 100 ] 每页商品数量。 |
| `query` | string 搜索查询，例如按商品名称、货号或 SKU 搜索。 |
| `sort_field` | string Enum: "SKU" "NAME" "QUANTITY" "TOTAL_VOLUME_IN_LITRES" 排序参数： SKU——SKU； NAME——按商品名称； QUANTITY——按数量； TOTAL_VOLUME_IN_LITRES——按体积（升）。 |

### 表格 1

| 字段 | 类型/说明 |
| --- | --- |
| `items` | Array of objects 交货申请中的商品列表。 |
| `total_count` | integer <int32> 申请中的商品数量。 |
| `has_next` | boolean 响应中是否未返回全部商品： true——请使用不同的 last_id 值再次请求，以获取其余数据； false——响应已包含全部商品数据。 |
| `last_id` | string 当前页面最后一个值的标识符。 |

## 示例

### 示例 0

```text
true
```

### 示例 1

```text
SKU
```

### 示例 2

```text
NAME
```

### 示例 3

```text
QUANTITY
```

### 示例 4

```text
TOTAL_VOLUME_IN_LITRES
```

### 示例 5

```text
true
```

### 示例 6

```text
last_id
```

### 示例 7

```text
false
```

### 示例 8

```json
{"bundle_ids": ["string"],"is_asc": true,"item_tags_calculation": {"dropoff_warehouse_id": 0,"storage_warehouse_ids": ["string"]},"last_id": "string","limit": 100,"query": "string","sort_field": "NAME"}
```

### 示例 9

```json
{"items": [{"icon_path": "string","sku": 0,"name": "string","offer_id": "string","quantity": 0,"barcode": "string","product_id": 0,"quant": 0,"is_quant_editable": true,"volume_in_litres": 0,"total_volume_in_litres": 0,"contractor_item_code": "string","sfbo_attribute": "ITEM_SFBO_ATTRIBUTE_UNSPECIFIED","shipment_type": "BUNDLE_ITEM_SHIPMENT_TYPE_UNSPECIFIED","tags": ["EVSD_REQUIRED"],"placement_zone": "UNSPECIFIED"}],"total_count": 0,"has_next": true,"last_id": "string"}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

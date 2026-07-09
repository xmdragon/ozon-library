# 获取商品特征描述

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v4/product/info/attributes`
- Operation ID：`ProductAPI_GetProductAttributesV4`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/ProductAPI_GetProductAttributesV4
- 分组：`product`

## 页面标题结构

- 获取商品特征描述
- header Parameters
- Request Body schema: application/json
- 回复
- Response Schema: application/json
- 请求范例
- 回复范例

## 参数与返回结构

### 表格 0

| 字段 | 类型/说明 |
| --- | --- |
| `Client-Id` required | string 用户识别号。 |
| `Api-Key` required | string API-密钥。 |

### 表格 1

| 字段 | 类型/说明 |
| --- | --- |
| `filter` | object 商品过滤。 |
| `last_id` | string 页面上最后一个值的ID。运行第一个查询时，将此字段留空。 要检索以下数值，请从上一个查询的响应中指定last_id。 |
| `limit` | integer <int32> [ 1 .. 1000 ] К每页的值的数量。 |
| `sort_by` | string 商品排序参数： sku — 按Ozon系统中的商品标识符排序； offer_id — 按商品货号排序； id — 按商品标识符排序； title — 按商品名称排序。 |
| `sort_dir` | string 排序方向： asc — 升序， desc — 降序。 |

### 表格 2

| 字段 | 类型/说明 |
| --- | --- |
| `result` | Array of objects 查询结果。 |
| `attributes` | Array of objects 商品特性的数组。 |
| `attributes_with_defaults` | Array of integers <int64> 具有默认值的特征标识符列表。 |
| `barcode` | string 条形码。 |
| `barcodes` | array of strings 商品的所有条形码。 |
| `description_category_id` | integer <int64> 类目标识符。 请将其与以下方法结合使用：/v1/description-category/attribute 和 /v1/description-category/attribute/values。 |
| `color_image` | string 市场营销色彩。 |
| `complex_attributes` | Array of objects 嵌套特征列表。 |
| `depth` | integer <int64> 深度。 |
| `dimension_unit` | string 尺寸的测量单位。 mm —— 毫米， cm —— 厘米， in —— 英寸。 |
| `height` | integer <int64> 包装高度。 |
| `id` | integer <int64> Ozon系统中商品的标识符 — product_id。 |
| `images` | array of strings 商品图片链接数组。图片顺序与商品卡片中的顺序一致。 |
| `model_info` | object 型号信息。 |
| `name` | string <= 500 characters 商品名称。 |
| `offer_id` | string 卖家系统中的商品标识符 — 货号。 |
| `pdf_list` | Array of objects PDF文件列表。 |
| `primary_image` | string 商品主图链接。 |
| `sku` | string Ozon 系统中的商品标识符（SKU）。 |
| `type_id` | integer <int64> 商品类型的标识符。 |
| `weight` | integer <int64> 商品在包装中的重量。 |
| `weight_unit` | string 重量测量单位。 |
| `width` | integer <int64> 包装宽度。 |
| `last_id` | string 页面上最后一个值的ID。 要检索以下数值，请从上一个查询的响应中指定last_id。 |
| `total` | string <int64> 列表中的商品数量。 |

### 表格 3

| 字段 | 类型/说明 |
| --- | --- |
| `attributes` | Array of objects 商品特性的数组。 |
| `attributes_with_defaults` | Array of integers <int64> 具有默认值的特征标识符列表。 |
| `barcode` | string 条形码。 |
| `barcodes` | array of strings 商品的所有条形码。 |
| `description_category_id` | integer <int64> 类目标识符。 请将其与以下方法结合使用：/v1/description-category/attribute 和 /v1/description-category/attribute/values。 |
| `color_image` | string 市场营销色彩。 |
| `complex_attributes` | Array of objects 嵌套特征列表。 |
| `depth` | integer <int64> 深度。 |
| `dimension_unit` | string 尺寸的测量单位。 mm —— 毫米， cm —— 厘米， in —— 英寸。 |
| `height` | integer <int64> 包装高度。 |
| `id` | integer <int64> Ozon系统中商品的标识符 — product_id。 |
| `images` | array of strings 商品图片链接数组。图片顺序与商品卡片中的顺序一致。 |
| `model_info` | object 型号信息。 |
| `name` | string <= 500 characters 商品名称。 |
| `offer_id` | string 卖家系统中的商品标识符 — 货号。 |
| `pdf_list` | Array of objects PDF文件列表。 |
| `primary_image` | string 商品主图链接。 |
| `sku` | string Ozon 系统中的商品标识符（SKU）。 |
| `type_id` | integer <int64> 商品类型的标识符。 |
| `weight` | integer <int64> 商品在包装中的重量。 |
| `weight_unit` | string 重量测量单位。 |
| `width` | integer <int64> 包装宽度。 |

## 示例

### 示例 0

```text
offer_id
```

### 示例 1

```text
product_id
```

### 示例 2

```text
sku
```

### 示例 3

```text
last_id
```

### 示例 4

```text
sku
```

### 示例 5

```text
offer_id
```

### 示例 6

```text
id
```

### 示例 7

```text
title
```

### 示例 8

```text
asc
```

### 示例 9

```text
desc
```

### 示例 10

```text
mm
```

### 示例 11

```text
cm
```

### 示例 12

```text
in
```

### 示例 13

```text
product_id
```

### 示例 14

```text
last_id
```

### 示例 15

```json
{"filter": {"product_id": ["0"],"offer_id": ["string"],"sku": ["0"],"visibility": "ALL"},"limit": 100,"sort_dir": "ASC"}
```

### 示例 16

```json
{"result": [{"id": 213761435,"barcode": "","barcodes": ["123124123","123342455"],"name": "Пленка защитная для Xiaomi Redmi Note 10 Pro 5G","offer_id": "21470","type_id": 124572394,"height": 10,"depth": 210,"width": 140,"dimension_unit": "mm","weight": 50,"weight_unit": "g","primary_image": "https://ir-21.ozonru.cn/s3/multimedia-4/6804736960.jpg","sku": 423434534,"model_info": {"model_id": 43445453,"count": 4},"images": ["https://ir-21.ozonru.cn/s3/multimedia-4/6804736960.jpg","https://ir-21.ozonru.cn/s3/multimedia-j/6835412647.jpg"],"pdf_list": [ ],"attributes": [{"id": 5219,"complex_id": 0,"values": [{"dictionary_value_id": 970718176,"value": "универсальный"}]},{"id": 11051,"complex_id": 0,"values": [{"dictionary_value_id": 970736931,"value": "Прозрачный"}]},{"id": 10100,"complex_id": 0,"values": [{"dictionary_value_id": 0,"value": "false"}]},{"id": 11794,"complex_id": 0,"values": [{"dictionary_value_id": 970860783,"value": "safe"}]},{"id": 9048,"complex_id": 0,"values": [{"dictionary_value_id": 0,"value": "Пленка защитная для Xiaomi Redmi Note 10 Pro 5G"}]},{"id": 5076,"complex_id": 0,"values": [{"dictionary_value_id": 39638,"value": "Xiaomi"}]},{"id": 9024,"complex_id": 0,"values": [{"dictionary_value_id": 0,"value": "21470"}]},{"id": 10015,"complex_id": 0,"values": [{"dictionary_value_id": 0,"value": "false"}]},{"id": 85,"complex_id": 0,"values": [{"dictionary_value_id": 971034861,"value": "Brand"}]},{"id": 9461,"complex_id": 0,"values": [{"dictionary_value_id": 349824787,"value": "Защитная пленка для смартфона"}]},{"id": 4180,"complex_id": 0,"values": [{"dictionary_value_id": 0,"value": "Пленка защитная для Xiaomi Redmi Note 10 Pro 5G"}]},{"id": 4191,"complex_id": 0,"values": [{"dictionary_value_id": 0,"value": "Пленка предназначена для модели Xiaomi Redmi Note 10 Pro 5G. Защитная гидрогелевая пленка обеспечит защиту вашего смартфона от царапин, пыли, сколов и потертостей."}]},{"id": 8229,"complex_id": 0,"values": [{"dictionary_value_id": 91521,"value": "Защитная пленка"}]}],"attributes_with_defaults": [5435,3452],"complex_attributes": [ ],"color_image": "","description_category_id": 71107562}],"total": 1,"last_id": "onVsfA=="}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

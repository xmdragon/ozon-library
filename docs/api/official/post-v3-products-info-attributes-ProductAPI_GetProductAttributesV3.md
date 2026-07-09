# 获取商品特征描述

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v3/products/info/attributes`
- Operation ID：`ProductAPI_GetProductAttributesV3`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/ProductAPI_GetProductAttributesV3
- 分组：`products`

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
| `filter` required | object 商品过滤。 |
| `last_id` | string 页面上最后一个值的ID。运行第一个查询时，将此字段留空。 要检索以下数值，请从上一个查询的响应中指定last_id。 |
| `limit` required | integer <int64> 每页的值的数量。最小 —— 1，最大 —— 1000。 |
| `sort_by` | string 对商品进行分类的参数。 |
| `sort_dir` | string 分类方向。 |

### 表格 2

| 字段 | 类型/说明 |
| --- | --- |
| `result` | Array of objects 查询结果。 |
| `attributes` | Array of objects 商品特性的数组。 |
| `barcode` | string 条形码。 |
| `category_id` | integer <int64> Deprecated 类别ID。 请将其与以下方法结合使用：/v1/description-category/tree, /v1/description-category/attribute, /v1/description-category/attribute/values. 当上述方法被禁用时，此参数也将被禁用。 |
| `description_category_id` | integer <int64> 类别ID。 请将其与以下方法结合使用：/v1/description-category/attribute и /v1/description-category/attribute/values。 |
| `color_image` | string 市场营销色彩。 |
| `complex_attributes` | Array of objects 已录入的特性的数组。 |
| `depth` | integer <int32> 深度。 |
| `dimension_unit` | string 尺寸的测量单位。 mm —— 毫米， cm —— 厘米， in —— 英寸。 |
| `height` | integer <int32> 包装高度。 |
| `id` | integer <int64> 商品特性的识别码。 |
| `image_group_id` | string Deprecated 用于后续批量下载图像的识别码。 |
| `images` | Array of objects 产品图片链接的数组。 |
| `images360` | Array of objects 图像数组360。 |
| `name` | string 商品名称。最多500个字符。 |
| `offer_id` | string 卖家系统中的商品识别码是卖家系统中的商品标识符是商品货号。 |
| `pdf_list` | Array of objects PDF文件的阵列。 |
| `weight` | integer <int32> 商品在包装中的重量。 |
| `weight_unit` | string 重量测量单位。 |
| `type_id` | integer <int64> 商品类型的标识符。 |
| `width` | integer <int32> 包装宽度。 |
| `last_id` | string 页面上最后一个值的ID。运行第一个查询时，将此字段留空。 要检索以下数值，请从上一个查询的响应中指定last_id。 |
| `total` | string <int32> 列表中的商品数量。 |

### 表格 3

| 字段 | 类型/说明 |
| --- | --- |
| `attributes` | Array of objects 商品特性的数组。 |
| `barcode` | string 条形码。 |
| `category_id` | integer <int64> Deprecated 类别ID。 请将其与以下方法结合使用：/v1/description-category/tree, /v1/description-category/attribute, /v1/description-category/attribute/values. 当上述方法被禁用时，此参数也将被禁用。 |
| `description_category_id` | integer <int64> 类别ID。 请将其与以下方法结合使用：/v1/description-category/attribute и /v1/description-category/attribute/values。 |
| `color_image` | string 市场营销色彩。 |
| `complex_attributes` | Array of objects 已录入的特性的数组。 |
| `depth` | integer <int32> 深度。 |
| `dimension_unit` | string 尺寸的测量单位。 mm —— 毫米， cm —— 厘米， in —— 英寸。 |
| `height` | integer <int32> 包装高度。 |
| `id` | integer <int64> 商品特性的识别码。 |
| `image_group_id` | string Deprecated 用于后续批量下载图像的识别码。 |
| `images` | Array of objects 产品图片链接的数组。 |
| `images360` | Array of objects 图像数组360。 |
| `name` | string 商品名称。最多500个字符。 |
| `offer_id` | string 卖家系统中的商品识别码是卖家系统中的商品标识符是商品货号。 |
| `pdf_list` | Array of objects PDF文件的阵列。 |
| `weight` | integer <int32> 商品在包装中的重量。 |
| `weight_unit` | string 重量测量单位。 |
| `type_id` | integer <int64> 商品类型的标识符。 |
| `width` | integer <int32> 包装宽度。 |

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
last_id
```

### 示例 3

```text
mm
```

### 示例 4

```text
cm
```

### 示例 5

```text
in
```

### 示例 6

```text
last_id
```

### 示例 7

```json
{"filter": {"product_id": ["213761435"],"visibility": "ALL"},"limit": 100,"last_id": "okVsfA==«","sort_dir": "ASC"}
```

### 示例 8

```json
{"result": [{"id": 213761435,"barcode": "","category_id": 17038062,"name": "Пленка защитная для Xiaomi Redmi Note 10 Pro 5G","offer_id": "21470","height": 10,"depth": 210,"width": 140,"dimension_unit": "mm","weight": 50,"weight_unit": "g","images": [{"file_name": "https://ir-21.ozonru.cn/s3/multimedia-f/6190456071.jpg","default": true,"index": 0},{"file_name": "https://ir-21.ozonru.cn/s3/multimedia-7/6190456099.jpg","default": false,"index": 1},{"file_name": "https://ir-21.ozonru.cn/s3/multimedia-9/6190456065.jpg","default": false,"index": 2}],"images360": [ ],"pdf_list": [ ],"attributes": [{"attribute_id": 5219,"complex_id": 0,"values": [{"dictionary_value_id": 970718176,"value": "универсальный"}]},{"attribute_id": 11051,"complex_id": 0,"values": [{"dictionary_value_id": 970736931,"value": "Прозрачный"}]},{"attribute_id": 10100,"complex_id": 0,"values": [{"dictionary_value_id": 0,"value": "false"}]},{"attribute_id": 11794,"complex_id": 0,"values": [{"dictionary_value_id": 970860783,"value": "safe"}]},{"attribute_id": 9048,"complex_id": 0,"values": [{"dictionary_value_id": 0,"value": "Пленка защитная для Xiaomi Redmi Note 10 Pro 5G"}]},{"attribute_id": 5076,"complex_id": 0,"values": [{"dictionary_value_id": 39638,"value": "Xiaomi"}]},{"attribute_id": 9024,"complex_id": 0,"values": [{"dictionary_value_id": 0,"value": "21470"}]},{"attribute_id": 10015,"complex_id": 0,"values": [{"dictionary_value_id": 0,"value": "false"}]},{"attribute_id": 85,"complex_id": 0,"values": [{"dictionary_value_id": 971034861,"value": "Brand"}]},{"attribute_id": 9461,"complex_id": 0,"values": [{"dictionary_value_id": 349824787,"value": "Защитная пленка для смартфона"}]},{"attribute_id": 4180,"complex_id": 0,"values": [{"dictionary_value_id": 0,"value": "Пленка защитная для Xiaomi Redmi Note 10 Pro 5G"}]},{"attribute_id": 4191,"complex_id": 0,"values": [{"dictionary_value_id": 0,"value": "Пленка предназначена для модели Xiaomi Redmi Note 10 Pro 5G. Защитная гидрогелевая пленка обеспечит защиту вашего смартфона от царапин, пыли, сколов и потертостей."}]},{"attribute_id": 8229,"complex_id": 0,"values": [{"dictionary_value_id": 91521,"value": "Защитная пленка"}]}],"complex_attributes": [ ],"color_image": "","last_id": ""}],"total": 1,"last_id": "onVsfA=="}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

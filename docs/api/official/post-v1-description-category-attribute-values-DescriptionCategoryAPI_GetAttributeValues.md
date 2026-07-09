# 特征值指南

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/description-category/attribute/values`
- Operation ID：`DescriptionCategoryAPI_GetAttributeValues`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/DescriptionCategoryAPI_GetAttributeValues
- 分组：`description-category`

## 页面标题结构

- 特征值指南
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
| `attribute_id` required | integer <int64> 特性ID。可以使用方法 /v1/description-category/attribute获取。 |
| `description_category_id` required | integer <int64> 类别ID。可以使用方法 /v1/description-category/tree获取。 |
| `language` | string Default: "DEFAULT" Enum: "DEFAULT" "RU" "EN" "TR" "ZH_HANS" 回复语言： EN — 英语， RU — 俄语， TR — 土耳其语， ZH_HANS — 中文。 默认情况下，使用俄语。 |
| `last_value_id` | integer <int64> 启动响应的指南 ID。 如果last_value_id为 10，则响应将包含从第十一个开始的指南。 |
| `limit` required | integer <int64> 响应中值的数量： 最多 —— 2000， 最少 —— 1。 |
| `type_id` required | integer <int64> 商品类型ID。可以使用方法 /v1/description-category/tree获取。 |

### 表格 2

| 字段 | 类型/说明 |
| --- | --- |
| `has_next` | boolean 该特征表示响应中只返回了部分特性值： true —— 请用新参数 last_value_id 再次请求以获取其它值； false —— 响应包含了所有特性值。 |
| `result` | Array of objects 特性值。 |
| `id` | integer <int64> 特性值ID。 |
| `info` | string 附加描述。 |
| `picture` | string 图片链接。 |
| `value` | string 商品特性值。 |

### 表格 3

| 字段 | 类型/说明 |
| --- | --- |
| `id` | integer <int64> 特性值ID。 |
| `info` | string 附加描述。 |
| `picture` | string 图片链接。 |
| `value` | string 商品特性值。 |

## 示例

### 示例 0

```text
EN
```

### 示例 1

```text
RU
```

### 示例 2

```text
TR
```

### 示例 3

```text
ZH_HANS
```

### 示例 4

```text
last_value_id
```

### 示例 5

```text
true
```

### 示例 6

```text
last_value_id
```

### 示例 7

```text
false
```

### 示例 8

```json
{"attribute_id": 85,"description_category_id": 17054869,"language": "DEFAULT","last_value_id": 100,"limit": 100,"type_id": 97311}
```

### 示例 9

```json
{"result": [{"id": 5055881,"value": "Sunshine","info": "美容与健康","picture": "https://ir-21.ozonru.cn/s3/multimedia-i/6010930878.jpg"},{"id": 5056737,"value": "Essence","info": "美容与健康","picture": "https://ir-21.ozonru.cn/s3/multimedia-v/6088253599.jpg"}],"has_next": true}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

# 类别特征列表

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/description-category/attribute`
- Operation ID：`DescriptionCategoryAPI_GetAttributes`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/DescriptionCategoryAPI_GetAttributes
- 分组：`description-category`

## News 更新标记

| 日期 | 标记 | 摘要 | 来源 |
| --- | --- | --- | --- |
| 2025-07-22 | `updated` | /v1/description-category/attribute 更新了方法响应中 result.id 参数的描述。 | [官方 News](https://docs.ozon.ru/api/seller/zh/#section/2025722) |
| 2025-03-19 | `added_field` | /v1/description-category/attribute 在方法响应中添加了参数 result.complex_is_collection。 | [官方 News](https://docs.ozon.ru/api/seller/zh/#section/2025319) |

## 页面标题结构

- 类别特征列表
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
| `description_category_id` required | integer <int64> 类别ID。可以使用方法 /v1/description-category/tree获取。 |
| `language` | string Default: "DEFAULT" Enum: "DEFAULT" "RU" "EN" "TR" "ZH_HANS" 回复语言： EN — 英语， RU — 俄语， TR — 土耳其语， ZH_HANS — 中文。 默认情况下，使用俄语。 |
| `type_id` required | integer <int64> 商品类型ID。可以使用方法 /v1/description-category/tree获取。 |

### 表格 2

| 字段 | 类型/说明 |
| --- | --- |
| `result` | Array of objects 请求结果。 |
| `category_dependent` | boolean 字典属性值取决于类别的标志： true — 该属性对每个类别都有不一样的值。 false — 该属性对所有类别都有相同的值。 |
| `description` | string 特征描述。 |
| `dictionary_id` | integer <int64> 目录ID。 |
| `group_id` | integer <int64> 组别特征ID。 |
| `group_name` | string 特征组别名称。 |
| `id` | integer <int64> 特性ID。 |
| `is_aspect` | boolean 方面属性特征。方面属性：用于区分同类商品不同特征的属性。 例如，同款衣服和鞋子具有不同的颜色和尺寸，即：颜色、尺寸为方面属性。 字段值： true — 方面属性，在货物交付到仓库或出仓销售后不能更改。 false — 非方面属性，可在任何时间改变。 |
| `is_collection` | boolean 标志、特征 — 值集： true — 特征 — 值集, false — 特性由单个值组成。 |
| `is_required` | boolean 强制性特征标志: true — 强制性特征, false — 可不指出特征。 |
| `name` | string 名称。 |
| `type` | string 特征类型。 |
| `attribute_complex_id` | integer <int64> 复合属性的标识符。 |
| `max_value_count` | integer <int64> 属性的最大值数量。 |
| `complex_is_collection` | boolean 标志某个复合特征是否为值集合： true 表示该复合特征是一个值集合； false 表示该复合特征只有一个值。 |

### 表格 3

| 字段 | 类型/说明 |
| --- | --- |
| `category_dependent` | boolean 字典属性值取决于类别的标志： true — 该属性对每个类别都有不一样的值。 false — 该属性对所有类别都有相同的值。 |
| `description` | string 特征描述。 |
| `dictionary_id` | integer <int64> 目录ID。 |
| `group_id` | integer <int64> 组别特征ID。 |
| `group_name` | string 特征组别名称。 |
| `id` | integer <int64> 特性ID。 |
| `is_aspect` | boolean 方面属性特征。方面属性：用于区分同类商品不同特征的属性。 例如，同款衣服和鞋子具有不同的颜色和尺寸，即：颜色、尺寸为方面属性。 字段值： true — 方面属性，在货物交付到仓库或出仓销售后不能更改。 false — 非方面属性，可在任何时间改变。 |
| `is_collection` | boolean 标志、特征 — 值集： true — 特征 — 值集, false — 特性由单个值组成。 |
| `is_required` | boolean 强制性特征标志: true — 强制性特征, false — 可不指出特征。 |
| `name` | string 名称。 |
| `type` | string 特征类型。 |
| `attribute_complex_id` | integer <int64> 复合属性的标识符。 |
| `max_value_count` | integer <int64> 属性的最大值数量。 |
| `complex_is_collection` | boolean 标志某个复合特征是否为值集合： true 表示该复合特征是一个值集合； false 表示该复合特征只有一个值。 |

## 示例

### 示例 0

```text
dictionary_id
```

### 示例 2

```text
EN
```

### 示例 3

```text
RU
```

### 示例 4

```text
TR
```

### 示例 5

```text
ZH_HANS
```

### 示例 6

```text
true
```

### 示例 7

```text
false
```

### 示例 8

```text
true
```

### 示例 9

```text
false
```

### 示例 10

```text
true
```

### 示例 11

```text
false
```

### 示例 12

```text
true
```

### 示例 13

```text
false
```

### 示例 14

```text
true
```

### 示例 15

```text
false
```

### 示例 16

```json
{
  "description_category_id": 200000933,
  "language": "DEFAULT",
  "type_id": 93080
}
```

### 示例 17

```json
{
  "result": [
    {
      "id": 31,
      "attribute_complex_id": 32,
      "name": "服装和鞋类品牌",
      "description": "请填写生产该商品所使用的品牌名称。如果商品没有品牌，请使用“无品牌”值",
      "type": "string",
      "is_collection": false,
      "is_required": true,
      "is_aspect": false,
      "max_value_count": 30,
      "group_name": "",
      "group_id": 33,
      "dictionary_id": 28732849,
      "category_dependent": true,
      "complex_is_collection": true
    }
  ]
}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

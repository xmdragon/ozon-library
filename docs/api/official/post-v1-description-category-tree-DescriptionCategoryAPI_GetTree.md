# 商品类别和类型的树形图

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/description-category/tree`
- Operation ID：`DescriptionCategoryAPI_GetTree`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/DescriptionCategoryAPI_GetTree
- 分组：`description-category`

## 页面标题结构

- 商品类别和类型的树形图
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
| `language` | string Default: "DEFAULT" Enum: "DEFAULT" "RU" "EN" "TR" "ZH_HANS" 回复语言： EN — 英语， RU — 俄语， TR — 土耳其语， ZH_HANS — 中文。 默认情况下，使用俄语。 |

### 表格 2

| 字段 | 类型/说明 |
| --- | --- |
| `result` | Array of objects 类别清单。 |
| `description_category_id` | integer <int64> 类别ID。 |
| `category_name` | string 类别名称。 |
| `children` | Array of objects 子类别树形图。 |
| `disabled` | boolean 如果无法在类别中创建商品，则为true。 如果可能，为false。 |
| `type_id` | integer <int64> 商品类型ID。 |
| `type_name` | string 商品类型名称。 |

### 表格 3

| 字段 | 类型/说明 |
| --- | --- |
| `description_category_id` | integer <int64> 类别ID。 |
| `category_name` | string 类别名称。 |
| `children` | Array of objects 子类别树形图。 |
| `disabled` | boolean 如果无法在类别中创建商品，则为true。 如果可能，为false。 |
| `type_id` | integer <int64> 商品类型ID。 |
| `type_name` | string 商品类型名称。 |

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
true
```

### 示例 5

```text
false
```

### 示例 6

```json
{"language": "DEFAULT"}
```

### 示例 7

```json
{"result": [{"description_category_id": 0,"category_name": "string","disabled": false,"children": [{"description_category_id": 0,"category_name": "string","disabled": false,"children": [{"type_name": "sting","type_id": 0,"disabled": false,"children": [ ]}]}]}]}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

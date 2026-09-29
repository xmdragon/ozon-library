# 获取子特征的可能值

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/description-category/dependent-attributes/values`
- Operation ID：`DescriptionCategoryDependentAttributesValues`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/#operation/DescriptionCategoryDependentAttributesValues
- 分组：`description-category`

## 页面标题结构

- 获取子特征的可能值
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
| `child_attribute_id` required | integer <int64> 子特征的标识符。 |
| `cursor` | string 用于选择下一批数据的指针。 |
| `description_category_id` | integer <int64> 类目标识符，来自 /v1/description-category/tree 方法。 |
| `limit` | integer <int64> [ 1 .. 1000 ] Default: 100 响应中的值数量。 |
| `parent_attribute_id` required | integer <int64> 父特征的标识符。 |
| `type_id` | integer <int64> 商品类型标识符，来自 /v1/description-category/tree 方法。 |

### 表格 2

| 字段 | 类型/说明 |
| --- | --- |
| `cursor` | string 用于选择下一批数据的指针。 |
| `result` | Array of objects 依赖特征的信息。 |
| `children` | Array of objects 子特征的信息。 |
| `parent_value` | string 父特征的值。 |
| `parent_value_id` | integer <int64> 父特征值的标识符。 |

### 表格 3

| 字段 | 类型/说明 |
| --- | --- |
| `children` | Array of objects 子特征的信息。 |
| `parent_value` | string 父特征的值。 |
| `parent_value_id` | integer <int64> 父特征值的标识符。 |

## 示例

### 示例 0

```json
{
  "parent_attribute_id": 8229,
  "child_attribute_id": 23348,
  "description_category_id": 234123,
  "type_id": 123123,
  "limit": 4,
  "cursor": ""
}
```

### 示例 1

```json
{
  "cursor": "eyJwYXJlbnRfdmFsdWVfaWQiOjEwMDIsImNoaWxkX2luZGV4IjowfQ==",
  "result": [
    {
      "parent_value_id": 1001,
      "parent_value": "拉达",
      "children": [
        {
          "child_value_id": 2001,
          "child_value": "格兰塔"
        },
        {
          "child_value_id": 2002,
          "child_value": "普里奥拉"
        },
        {
          "child_value_id": 2003,
          "child_value": "维斯塔"
        }
      ]
    },
    {
      "parent_value_id": 1002,
      "parent_value": "丰田",
      "children": [
        {
          "child_value_id": 2004,
          "child_value": "卡罗拉"
        }
      ]
    }
  ]
}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

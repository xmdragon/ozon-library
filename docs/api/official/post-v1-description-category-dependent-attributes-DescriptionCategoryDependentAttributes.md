# 获取依赖特征

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/description-category/dependent-attributes`
- Operation ID：`DescriptionCategoryDependentAttributes`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/#operation/DescriptionCategoryDependentAttributes
- 分组：`description-category`

## 页面标题结构

- 获取依赖特征
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
| `description_category_id` required | integer <int64> 类目标识符，来自 /v1/description-category/tree 方法。 |
| `type_id` | integer <int64> 商品类型标识符，来自 /v1/description-category/tree 方法。 |

### 表格 2

| 字段 | 类型/说明 |
| --- | --- |
| `result` | Array of objects 依赖特征的信息。 |
| `child_attribute_id` | integer <int64> 子特征的标识符。 |
| `parent_attribute_id` | integer <int64> 父特征的标识符。 |

### 表格 3

| 字段 | 类型/说明 |
| --- | --- |
| `child_attribute_id` | integer <int64> 子特征的标识符。 |
| `parent_attribute_id` | integer <int64> 父特征的标识符。 |

## 示例

### 示例 0

```json
{
  "description_category_id": 234123,
  "type_id": 123123
}
```

### 示例 1

```json
{
  "result": [
    {
      "child_attribute_id": 4812,
      "parent_attribute_id": 8229
    }
  ]
}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

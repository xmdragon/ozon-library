# 标志代码验证

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v5/fbs/posting/product/exemplar/validate`
- Operation ID：`PostingAPI_FbsPostingProductExemplarValidateV5`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/PostingAPI_FbsPostingProductExemplarValidateV5
- 分组：`fbs`

## 页面标题结构

- 标志代码验证
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
| `posting_number` required | string 发货号。 |
| `products` required | Array of objects 商品清单。 |

### 表格 2

| 字段 | 类型/说明 |
| --- | --- |
| `products` | Array of objects 商品清单。 |
| `error` | string 错误代码。 |
| `exemplars` | Array of objects 副本信息。 |
| `product_id` | integer <int64> Ozon系统中的商品ID — SKU。 |
| `valid` | boolean 验证结果。如果所有样件的代码都符合要求，那么结果将为 true。 |

### 表格 3

| 字段 | 类型/说明 |
| --- | --- |
| `error` | string 错误代码。 |
| `exemplars` | Array of objects 副本信息。 |
| `product_id` | integer <int64> Ozon系统中的商品ID — SKU。 |
| `valid` | boolean 验证结果。如果所有样件的代码都符合要求，那么结果将为 true。 |

## 示例

### 示例 0

```text
true
```

### 示例 1

```json
{
  "posting_number": "string",
  "products": [
    {
      "exemplars": [
        {
          "gtd": "string",
          "marks": [
            {
              "mark": "string",
              "mark_type": "string"
            }
          ],
          "rnpt": "string"
        }
      ],
      "product_id": 0
    }
  ]
}
```

### 示例 2

```json
{
  "products": [
    {
      "error": "string",
      "exemplars": [
        {
          "errors": [
            "string"
          ],
          "gtd": "string",
          "marks": [
            {
              "errors": [
                "string"
              ],
              "mark": "string",
              "mark_type": "string",
              "valid": true
            }
          ],
          "rnpt": "string",
          "valid": true
        }
      ],
      "product_id": 0,
      "valid": true
    }
  ]
}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

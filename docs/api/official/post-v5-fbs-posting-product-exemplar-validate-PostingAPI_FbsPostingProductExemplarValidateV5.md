# 标志代码验证

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v5/fbs/posting/product/exemplar/validate`
- Operation ID：`PostingAPI_FbsPostingProductExemplarValidateV5`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/#operation/PostingAPI_FbsPostingProductExemplarValidateV5
- 分组：`fbs`

## News 更新标记

| 日期 | 标记 | 摘要 | 来源 |
| --- | --- | --- | --- |
| 2026-10-22 | `graduated` | /v5/fbs/posting/product/exemplar/validate 已将该方法从Beta版迁移至正式版。 | [官方 News](https://docs.ozon.ru/api/seller/zh/#section/20261022) |
| 2025-10-16 | `updated` | /v5/fbs/posting/product/exemplar/validate 更新了方法响应中的 products.exemplars.marks 参数描述。 | [官方 News](https://docs.ozon.ru/api/seller/zh/#section/20251016) |
| 2025-09-29 | `updated` | /v5/fbs/posting/product/exemplar/validate 已更新该方式的请求与响应中products.exemplars.marks参数的描述。 | [官方 News](https://docs.ozon.ru/api/seller/zh/#section/2025929) |
| 2025-02-17 | `new_method` | /v5/fbs/posting/product/exemplar/validate 新增 Beta 方法用于管理标志代码。 | [官方 News](https://docs.ozon.ru/api/seller/zh/#section/2025217) |

## 页面标题结构

- 标志代码验证
- HEADER PARAMETERS
- REQUEST BODY SCHEMA: application/json
- 回复
- RESPONSE SCHEMA: application/json
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

```json
{
  "posting_number": "43210543-0123-4",
  "products": [
    {
      "exemplars": [
        {
          "gtd": "GTD-100500/2026/0215",
          "marks": [
            {
              "mark": "01046000123456789ABCDEF12345678",
              "mark_type": "DATA_MATRIX"
            },
            {
              "mark": "QR-9876543210ABCDEF1234567890",
              "mark_type": "QR_CODE"
            }
          ],
          "rnpt": "RNPT-100200300400500",
          "weight": 1500
        },
        {
          "gtd": "GTD-200300/2026/0301",
          "marks": [
            {
              "mark": "01046000987654321FEDCBA654321",
              "mark_type": "DATA_MATRIX"
            }
          ],
          "rnpt": "RNPT-999888777666555",
          "weight": 2200
        }
      ],
      "product_id": 123456789
    },
    {
      "exemplars": [
        {
          "gtd": "",
          "marks": [
            {
              "mark": "INVALID-MARK-1234567890",
              "mark_type": "UNKNOWN"
            }
          ],
          "rnpt": "",
          "weight": 0
        }
      ],
      "product_id": 987654321
    }
  ]
}
```

### 示例 1

```json
{
  "products": [
    {
      "error": "该产品包含无效实例",
      "exemplars": [
        {
          "errors": [
            "未注明物品重量",
            "商品批次登记号缺失"
          ],
          "gtd": "GTD-100500/2026/0215",
          "marks": [
            {
              "errors": [],
              "mark": "01046000123456789ABCDEF12345678",
              "mark_type": "DATA_MATRIX",
              "valid": true
            },
            {
              "errors": [
                "标注格式无效"
              ],
              "mark": "INVALID-MARK-123",
              "mark_type": "UNKNOWN",
              "valid": false
            }
          ],
          "rnpt": "",
          "valid": false,
          "weight": 0
        },
        {
          "errors": [],
          "gtd": "GTD-200300/2026/0301",
          "marks": [
            {
              "errors": [],
              "mark": "01046000987654321FEDCBA654321",
              "mark_type": "DATA_MATRIX",
              "valid": true
            }
          ],
          "rnpt": "RNPT-999888777666555",
          "valid": true,
          "weight": 2200
        }
      ],
      "product_id": 123456789,
      "valid": false
    },
    {
      "error": "",
      "exemplars": [
        {
          "errors": [],
          "gtd": "GTD-300400/2026/0401",
          "marks": [
            {
              "errors": [],
              "mark": "QR-9876543210ABCDEF1234567890",
              "mark_type": "QR_CODE",
              "valid": true
            }
          ],
          "rnpt": "RNPT-555444333222111",
          "valid": true,
          "weight": 1500
        }
      ],
      "product_id": 987654321,
      "valid": true
    }
  ]
}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

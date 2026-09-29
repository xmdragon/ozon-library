# 获取可自动添加到促销活动中的商品列表

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v2/actions/auto-add/products/candidates`
- Operation ID：`ActionsAutoAddProductsCandidatesV2`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/#operation/ActionsAutoAddProductsCandidatesV2
- 分组：`actions`

## News 更新标记

| 日期 | 标记 | 摘要 | 来源 |
| --- | --- | --- | --- |
| 2026-09-23 | `new_method` | /v2/actions/auto-add/products/candidates 新增了操作Ozon促销活动的新方法。 | [官方 News](https://docs.ozon.ru/api/seller/zh/#section/2026923) |

## 页面标题结构

- 获取可自动添加到促销活动中的商品列表
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
| `action_id` required | integer <uint64> 促销活动标识符。 |
| `auto_add_date` required | string <date-time> 方法 /v1/actions 响应中 result.auto_add_dates 参数里的商品自动添加到促销活动中的日期和时间。 |
| `limit` required | integer <uint64> [ 1 .. 100 ] 响应中返回的值数量。 |
| `offset` | integer <uint64> Default: 0 在响应中将被跳过的项目数量。在响应中将被跳过的项目数量。 |

### 表格 2

| 字段 | 类型/说明 |
| --- | --- |
| `products` | Array of objects 可用于自动添加到促销活动中的商品列表。 |
| `total` | integer <uint64> 商品数量。 |

## 示例

### 示例 0

```json
{
  "action_id": 250204,
  "auto_add_date": "2025-01-01T00:00:00Z",
  "offset": 5,
  "limit": 100
}
```

### 示例 1

```json
{
  "products": [
    {
      "action_price_to_auto_add": {
        "amount": "1800",
        "currency": "RUB"
      },
      "base_price": {
        "amount": "1827",
        "currency": "RUB"
      },
      "currency": "RUB",
      "has_expired_min_seller_price": true,
      "id": 8888888,
      "is_manually_added": true,
      "marketplace_seller_price": {
        "amount": "70",
        "currency": "RUB"
      },
      "max_discount_price": {
        "amount": "62",
        "currency": "RUB"
      },
      "min_action_quantity": 1,
      "min_seller_price": {
        "amount": "1",
        "currency": "RUB"
      },
      "name": "Ароматизатор / Масло для бани / Эфирное масло \"Пихта\", 250 мл",
      "offer_id": "PS0000",
      "price": {
        "amount": "1827",
        "currency": "RUB"
      },
      "quantity_to_auto_add": 2,
      "sku": 8888888,
      "website_prices": {
        "price": {
          "amount": "54",
          "currency": "RUB"
        },
        "prices_by_schema": {
          "additionalProp1": {
            "black_price": {
              "amount": "1400",
              "currency": "RUB"
            },
            "green_price": {
              "amount": "18888",
              "currency": "RUB"
            }
          },
          "additionalProp2": {
            "black_price": {
              "amount": "1500",
              "currency": "RUB"
            },
            "green_price": {
              "amount": "1600",
              "currency": "RUB"
            }
          },
          "additionalProp3": {
            "black_price": {
              "amount": "1700",
              "currency": "RUB"
            },
            "green_price": {
              "amount": "1800",
              "currency": "RUB"
            }
          }
        }
      },
      "will_be_quarantined": false
    }
  ],
  "total": 219176
}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

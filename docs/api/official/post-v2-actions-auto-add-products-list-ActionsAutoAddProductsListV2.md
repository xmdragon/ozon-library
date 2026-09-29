# 获取促销活动自动添加列表中的商品列表

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v2/actions/auto-add/products/list`
- Operation ID：`ActionsAutoAddProductsListV2`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/#operation/ActionsAutoAddProductsListV2
- 分组：`actions`

## 页面标题结构

- 获取促销活动自动添加列表中的商品列表
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
| `offset` | integer <uint64> Default: 0 在响应中将被跳过的项目数量。 例如，如果 offset = 10 ，响应将从第11个找到的元素开始。 |

### 表格 2

| 字段 | 类型/说明 |
| --- | --- |
| `products` | Array of objects 启用自动添加的商品列表。 |
| `total` | integer <uint64> 商品数量。 |

### 表格 3

| 字段 | 类型/说明 |
| --- | --- |
| `products` | Array of objects 启用自动添加的商品列表。 |
| `action_price_to_auto_add` | object 商品的促销价格。 |
| `add_mode` | boolean 如果商品是手动添加的，则为 true 。 |
| `base_price` | object 商品折扣前价格。 |
| `currency` | string 价格货币。 |
| `has_expired_min_seller_price` | boolean 如果促销活动的限制已到期，则为 true 。 |
| `marketplace_seller_price` | object 计入促销活动后的商品价格，不包括由Ozon承担费用的促销活动。 |
| `max_discount_price` | object 商品可自动添加到促销活动中的最高价格。 |
| `min_action_quantity` | integer <uint64> “库存折扣”促销活动类型中的最低商品数量。 |
| `min_seller_price` | object 应用促销活动后的商品最低价格。 |
| `name` | string 商品名称。 |
| `offer_id` | string 卖家系统中的商品标识符——货号。 |
| `price` | object 商品无折扣价格。 |
| `product_id` | integer <uint64> Ozon系统中的商品标识符—— product_id 。 |
| `quantity_to_auto_add` | integer <uint64> 促销活动中的商品数量。 |
| `sku` | integer <uint64> Ozon系统中的商品标识符——SKU。 |
| `website_prices` | object 网站上的商品价格。 |
| `will_be_quarantined` | boolean 如果商品在自动添加后进入价格冻结，则为 true 。 |
| `total` | integer <uint64> 商品数量。 |

## 示例

### 示例 0

```json
{
  "action_id": 0,
  "auto_add_date": "2025-01-01T00:00:00Z",
  "offset": 0,
  "limit": 0
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
      "add_mode": true,
      "base_price": {
        "amount": "1827",
        "currency": "RUB"
      },
      "currency": "RUB",
      "has_expired_min_seller_price": true,
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
      "offer_id": "SR0000",
      "price": {
        "amount": "1827",
        "currency": "RUB"
      },
      "product_id": 8888888,
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
              "amount": "111",
              "currency": "RUB"
            },
            "green_price": {
              "amount": "222",
              "currency": "RUB"
            }
          },
          "additionalProp2": {
            "black_price": {
              "amount": "333",
              "currency": "RUB"
            },
            "green_price": {
              "amount": "444",
              "currency": "RUB"
            }
          },
          "additionalProp3": {
            "black_price": {
              "amount": "555",
              "currency": "RUB"
            },
            "green_price": {
              "amount": "666",
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

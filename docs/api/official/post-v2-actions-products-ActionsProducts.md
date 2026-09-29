# 获取参与活动的商品列表

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v2/actions/products`
- Operation ID：`ActionsProducts`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/#operation/ActionsProducts
- 分组：`actions`

## News 更新标记

| 日期 | 标记 | 摘要 | 来源 |
| --- | --- | --- | --- |
| 2026-09-23 | `new_method` | /v2/actions/products 新增了操作Ozon促销活动的新方法。 | [官方 News](https://docs.ozon.ru/api/seller/zh/#section/2026923) |

## 页面标题结构

- 获取参与活动的商品列表
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
| `action_id` required | integer <uint64> 促销活动标识符。可通过方法 /v1/actions 获取。 |
| `last_id` | string 页面上最后一个商品的标识符。如果是首次请求，请将该字段留空。 |
| `limit` required | integer <uint64> <= 100 К每页显示的数量。 |

### 表格 2

| 字段 | 类型/说明 |
| --- | --- |
| `last_id` | string 页面上最后一个商品的标识符。要获取下一个批次的数据，请在下一个请求的 last_id 参数中传递上次获取的值。 |
| `products` | Array of objects 商品列表。 |
| `total` | integer <uint64> 促销活动中的商品数量。 |

## 示例

### 示例 0

```json
{
  "action_id": 213139,
  "last_id": "3262247282",
  "limit": 100
}
```

### 示例 1

```json
{
  "products": [
    {
      "id": 99999,
      "price": {
        "amount": "4000",
        "currency": "RUB"
      },
      "action_price": {
        "amount": "4000",
        "currency": "RUB"
      },
      "max_action_price": {
        "amount": "3560",
        "currency": "RUB"
      },
      "add_mode": "SELLER",
      "stock": 2,
      "min_stock": 1,
      "recommended_stock": 10,
      "marketplace_seller_price": {
        "amount": "500",
        "currency": "RUB"
      },
      "alert_max_action_price_failed": false,
      "alert_max_action_price": {
        "amount": "4000",
        "currency": "RUB"
      },
      "current_boost": 12,
      "price_min_elastic": {
        "amount": "3560",
        "currency": "RUB"
      },
      "price_max_elastic": {
        "amount": "3560",
        "currency": "RUB"
      },
      "min_boost": 1,
      "max_boost": 12,
      "website_prices": {
        "price": {
          "amount": "382",
          "currency": "RUB"
        },
        "prices_by_schema": {}
      },
      "min_seller_price": {
        "amount": "4000",
        "currency": "RUB"
      },
      "is_quarantined": true
    }
  ],
  "total": 44,
  "last_id": "28743"
}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

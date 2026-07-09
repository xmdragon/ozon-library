# 按标识符获取货件信息

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/posting/fbp/get`
- Operation ID：`GetFbpPosting`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/GetFbpPosting
- 分组：`posting`

## News 更新标记

| 日期 | 标记 | 摘要 | 来源 |
| --- | --- | --- | --- |
| 2026-07-01 | `new_method` | /v1/posting/fbp/get 新增了用于按标识符获取FBP货件信息的beta方法。 | [官方 News](https://docs.ozon.ru/api/seller/zh/#section/202671) |

## 页面标题结构

- 按标识符获取货件信息
- Request Body schema: application/json
- 回复
- Response Schema: application/json
- 请求范例
- 回复范例

## 参数与返回结构

### 表格 0

| 字段 | 类型/说明 |
| --- | --- |
| `posting_number` required | string 货件标识符。 |

### 表格 1

| 字段 | 类型/说明 |
| --- | --- |
| `posting` | object 货件信息。 |
| `analytics_data` | object 分析数据。 |
| `cancellation` | object 取消信息。 |
| `financial_data` | object 财务数据。 |
| `in_process_at` | string <date-time> 货件开始处理的日期和时间。 |
| `order_date` | string <date-time> 订单的创建日期。 |
| `order_id` | integer <int64> 该货件所属订单的标识符。 |
| `order_number` | string 该货件所属订单的编号。 |
| `posting_number` | string 货件标识符。 |
| `products` | Array of objects 货件中商品列表。 |
| `status` | integer <int64> 货件状态。 |
| `substatus` | string 货件子状态。 |
| `tpl_provider_id` | integer <int64> 配送服务商标识符。 |

### 表格 2

| 字段 | 类型/说明 |
| --- | --- |
| `analytics_data` | object 分析数据。 |
| `cancellation` | object 取消信息。 |
| `financial_data` | object 财务数据。 |
| `in_process_at` | string <date-time> 货件开始处理的日期和时间。 |
| `order_date` | string <date-time> 订单的创建日期。 |
| `order_id` | integer <int64> 该货件所属订单的标识符。 |
| `order_number` | string 该货件所属订单的编号。 |
| `posting_number` | string 货件标识符。 |
| `products` | Array of objects 货件中商品列表。 |
| `status` | integer <int64> 货件状态。 |
| `substatus` | string 货件子状态。 |
| `tpl_provider_id` | integer <int64> 配送服务商标识符。 |

## 示例

### 示例 0

```json
{
  "posting_number": "string"
}
```

### 示例 1

```json
{
  "posting": {
    "analytics_data": {
      "city": "string",
      "delivery_date_begin": "2019-08-24T14:15:22Z",
      "delivery_date_end": "2019-08-24T14:15:22Z",
      "delivery_type": "string",
      "region": "string",
      "warehouse_id": 0
    },
    "cancellation": {
      "cancel_reason": "string",
      "cancel_reason_id": 0,
      "cancellation_initiator": "string",
      "cancellation_type": "string"
    },
    "financial_data": {
      "cluster_from": "string",
      "cluster_to": "string",
      "delivery_amount": 0,
      "products": [
        {
          "actions": [
            {
              "action_id": 0,
              "action_type": "string",
              "date_from": "2019-08-24T14:15:22Z",
              "date_to": "2019-08-24T14:15:22Z",
              "description": "string",
              "discount_percent": 0,
              "discount_value": 0
            }
          ],
          "commissions_price": {
            "amount": "string",
            "currency": "string"
          },
          "customer_price": {
            "amount": "string",
            "currency": "string"
          },
          "old_price": 0,
          "posting_commission": {
            "amount": 0,
            "payout": 0,
            "percent": 0
          },
          "quantity": 0,
          "return_commission": {
            "amount": 0,
            "payout": 0,
            "percent": 0
          },
          "seller_price": {
            "amount": "string",
            "currency": "string"
          },
          "sku": 0,
          "total_discount_percent": 0,
          "total_discount_value": 0
        }
      ]
    },
    "in_process_at": "2019-08-24T14:15:22Z",
    "order_date": "2019-08-24T14:15:22Z",
    "order_id": 0,
    "order_number": "string",
    "posting_number": "string",
    "products": [
      {
        "has_imei": true,
        "marketplace_seller_price": {
          "amount": "string",
          "currency": "string"
        },
        "name": "string",
        "offer_id": "string",
        "quantity": 0,
        "sku": 0,
        "weight_max": 0
      }
    ],
    "status": 0,
    "substatus": "string",
    "tpl_provider_id": 0
  }
}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

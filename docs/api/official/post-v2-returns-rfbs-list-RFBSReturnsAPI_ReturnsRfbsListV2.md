# 退货申请列表

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v2/returns/rfbs/list`
- Operation ID：`RFBSReturnsAPI_ReturnsRfbsListV2`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/RFBSReturnsAPI_ReturnsRfbsListV2
- 分组：`returns`

## News 更新标记

| 日期 | 标记 | 摘要 | 来源 |
| --- | --- | --- | --- |
| 2025-12-26 | `deprecated_field` | /v2/returns/rfbs/list 参数 returns.client_name 即将废弃，将于2026年2月2日停止支持。 | [官方 News](https://docs.ozon.ru/api/seller/zh/#section/20251226) |
| 2025-09-24 | `updated` | /v2/returns/rfbs/list 更新了该方法请求中参数 last_id 的描述。已更新回答示例。 | [官方 News](https://docs.ozon.ru/api/seller/zh/#section/2025924) |

## 页面标题结构

- 退货申请列表
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
| `filter` | object 筛选器。 |
| `last_id` | integer <int32> 页面上最后一个值的标识符——return_id。在第一次请求时，请将此字段留空。 |
| `limit` required | integer <int32> 响应中的值数量。 |

### 表格 2

| 字段 | 类型/说明 |
| --- | --- |
| `returns` | object 申请信息。 |
| `client_name` | string Deprecated 买家姓名。 |
| `created_at` | string <date-time> 创建日期。 |
| `order_number` | string 订单号。 |
| `posting_number` | string 货件编号。 |
| `product` | object 商品信息。 |
| `return_id` | integer <int64> 退货申请的标识符。 |
| `return_number` | string 退货申请编号。 |
| `state` | object 退货申请和退款状态。 |

### 表格 3

| 字段 | 类型/说明 |
| --- | --- |
| `client_name` | string Deprecated 买家姓名。 |
| `created_at` | string <date-time> 创建日期。 |
| `order_number` | string 订单号。 |
| `posting_number` | string 货件编号。 |
| `product` | object 商品信息。 |
| `return_id` | integer <int64> 退货申请的标识符。 |
| `return_number` | string 退货申请编号。 |
| `state` | object 退货申请和退款状态。 |

## 示例

### 示例 0

```text
return_id
```

### 示例 1

```json
{
  "filter": {
    "offer_id": "test-offer-123456",
    "posting_number": "789456123-0002-3",
    "group_state": [
      "New",
      "Approved"
    ],
    "created_at": {
      "from": "2026-02-01T00:00:00Z",
      "to": "2026-03-01T23:59:59Z"
    }
  },
  "last_id": 0,
  "limit": 1000
}
```

### 示例 2

```json
{
  "returns": [
    {
      "return_id": 8000123456,
      "return_number": "RET-2026-00123",
      "posting_number": "789456123-0002-3",
      "order_number": "123456789",
      "created_at": "2026-02-15T10:30:00Z",
      "product": {
        "sku": 1000123456,
        "offer_id": "test-offer-123456",
        "name": "string",
        "price": 2999,
        "currency_code": "RUB"
      },
      "state": {
        "group_state": "New",
        "state": "ON_APPROVAL",
        "state_name": "string"
      }
    }
  ]
}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

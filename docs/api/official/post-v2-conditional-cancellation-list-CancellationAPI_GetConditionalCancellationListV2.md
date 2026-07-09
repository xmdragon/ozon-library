# 获取 rFBS 取消申请列表

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v2/conditional-cancellation/list`
- Operation ID：`CancellationAPI_GetConditionalCancellationListV2`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/CancellationAPI_GetConditionalCancellationListV2
- 分组：`conditional-cancellation`

## News 更新标记

| 日期 | 标记 | 摘要 | 来源 |
| --- | --- | --- | --- |
| 2025-06-19 | `updated` | /v2/conditional-cancellation/list。 — 在 管理取消订单 模块，更新了获取rFBS取消申请的方法。 | [官方 News](https://docs.ozon.ru/api/seller/zh/#section/2025619) |

## 页面标题结构

- 获取 rFBS 取消申请列表
- Request Body schema: application/json
- 回复
- Response Schema: application/json
- 请求范例
- 回复范例

## 参数与返回结构

### 表格 0

| 字段 | 类型/说明 |
| --- | --- |
| `filters` | object 过滤器。 |
| `last_id` | integer <int64> 页面上最后一个值的标识符。在首次请求时此字段留空。 要获取后续值，请指定上一次请求响应中的 last_id。 |
| `limit` required | integer <int32> <= 500 响应中包含的申请总数。 |
| `with` | object 附加信息。 |

### 表格 1

| 字段 | 类型/说明 |
| --- | --- |
| `counter` | integer <int64> ON_APPROVAL 状态申请的计数器。 |
| `last_id` | integer <int64> 页面上最后一个值的标识符。 要获取后续值，请指定上一次请求响应中的 last_id。 |
| `result` | Array of objects 取消申请的详细信息。 |
| `approve_comment` | string 在确认或拒绝取消申请时填写的备注。 |
| `approve_date` | string <date-time> 取消申请确认或拒绝的日期。 |
| `auto_approve_date` | string <date-time> 申请将在此日期后自动确认。 |
| `cancellation_id` | integer <int64> 取消申请标识符。 |
| `cancellation_initiator` | string Enum: "OZON" "SELLER" "CLIENT" "SYSTEM" "DELIVERY" 取消发起人： SELLER — 卖家， CLIENT — 买家， OZON — Ozon, SYSTEM — 系统， DELIVERY — 配送服务。 |
| `cancellation_reason` | object 取消原因。 |
| `cancellation_reason_message` | string 取消申请中由取消发起人手动填写的备注。 |
| `cancelled_at` | string <date-time> 取消申请的创建日期。 |
| `order_date` | string <date-time> 订单的创建日期。 |
| `posting_number` | string 货件编号。 |
| `source_id` | integer <int64> 上一次取消申请的标识符。 用于保持向后兼容性。 |
| `state` | object 取消申请的状态。 |
| `tpl_integration_type` | string 与配送服务的集成类型。 |

### 表格 2

| 字段 | 类型/说明 |
| --- | --- |
| `approve_comment` | string 在确认或拒绝取消申请时填写的备注。 |
| `approve_date` | string <date-time> 取消申请确认或拒绝的日期。 |
| `auto_approve_date` | string <date-time> 申请将在此日期后自动确认。 |
| `cancellation_id` | integer <int64> 取消申请标识符。 |
| `cancellation_initiator` | string Enum: "OZON" "SELLER" "CLIENT" "SYSTEM" "DELIVERY" 取消发起人： SELLER — 卖家， CLIENT — 买家， OZON — Ozon, SYSTEM — 系统， DELIVERY — 配送服务。 |
| `cancellation_reason` | object 取消原因。 |
| `cancellation_reason_message` | string 取消申请中由取消发起人手动填写的备注。 |
| `cancelled_at` | string <date-time> 取消申请的创建日期。 |
| `order_date` | string <date-time> 订单的创建日期。 |
| `posting_number` | string 货件编号。 |
| `source_id` | integer <int64> 上一次取消申请的标识符。 用于保持向后兼容性。 |
| `state` | object 取消申请的状态。 |
| `tpl_integration_type` | string 与配送服务的集成类型。 |

## 示例

### 示例 0

```text
last_id
```

### 示例 1

```text
ON_APPROVAL
```

### 示例 2

```text
last_id
```

### 示例 3

```text
SELLER
```

### 示例 4

```text
CLIENT
```

### 示例 5

```text
OZON
```

### 示例 6

```text
SYSTEM
```

### 示例 7

```text
DELIVERY
```

### 示例 8

```json
{
  "filters": {
    "cancellation_initiator": [
      "CLIENT"
    ],
    "posting_number": [
      "34009011-0094-1"
    ],
    "state": "ALL"
  },
  "limit": 500,
  "last_id": 0,
  "with": {
    "counter": true
  }
}
```

### 示例 9

```json
{
  "result": [
    {
      "approve_comment": "string",
      "approve_date": "2024-11-27T12:31:43.621Z",
      "auto_approve_date": "2024-11-27T12:31:43.621Z",
      "cancellation_id": 0,
      "cancellation_initiator": "OZON",
      "cancellation_reason": {
        "id": 0,
        "name": "string"
      },
      "cancellation_reason_message": "string",
      "cancelled_at": "2024-11-27T12:31:43.621Z",
      "order_date": "2024-11-27T12:31:43.621Z",
      "posting_number": "string",
      "state": {
        "id": 0,
        "name": "string",
        "state": "ALL"
      },
      "tpl_integration_type": "string"
    }
  ],
  "counter": "1",
  "last_id": 283784254
}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

# 未处理货件列表 Deprecated

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v3/posting/fbs/unfulfilled/list`
- Operation ID：`PostingAPI_GetFbsPostingUnfulfilledList`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/PostingAPI_GetFbsPostingUnfulfilledList
- 分组：`posting`

## 页面标题结构

- 未处理货件列表 Deprecated
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
| `dir` | string 分类方向： asc — 从小到大， desc — 从大到小。 |
| `filter` required | object 请求过滤。 请按装运时间使用过滤器 — cutoff, 或者按照货件交付给快递的时间 — delivering_date。 如果一起使用，则会在响应中返回错误。 要按装运时间使用过滤器，请填 cutoff_from 和 cutoff_to字段。 要按货件交付给快递的时间使用过滤器, 请填 delivering_date_from 和 delivering_date_to字段。 |
| `limit` required | integer <int64> 响应中值的数量： 最大值 — 1000， 最小值 — 1。 |
| `offset` required | integer <int64> 将在响应中跳过的元素数。 例如，如果“offset=10”，那么响应将从找到的第11个元素开始。 |
| `with` | object 要添加到响应的附加字段。 |

### 表格 2

| 字段 | 类型/说明 |
| --- | --- |
| `result` | object 请求结果。 |
| `count` | integer <int64> 在响应中的元素计数器。 |
| `postings` | Array of objects 货件清单和每个货物的详细信息。 |

### 表格 3

| 字段 | 类型/说明 |
| --- | --- |
| `count` | integer <int64> 在响应中的元素计数器。 |
| `postings` | Array of objects 货件清单和每个货物的详细信息。 |

## 示例

### 示例 0

```text
awaiting_registration
```

### 示例 1

```text
acceptance_in_progress
```

### 示例 2

```text
awaiting_approve
```

### 示例 3

```text
awaiting_packaging
```

### 示例 4

```text
awaiting_deliver
```

### 示例 5

```text
arbitration
```

### 示例 6

```text
client_arbitration
```

### 示例 7

```text
delivering
```

### 示例 8

```text
driver_pickup
```

### 示例 9

```text
cancelled
```

### 示例 10

```text
not_accepted
```

### 示例 11

```text
asc
```

### 示例 12

```text
desc
```

### 示例 13

```text
cutoff
```

### 示例 14

```text
delivering_date
```

### 示例 15

```text
cutoff_from
```

### 示例 16

```text
cutoff_to
```

### 示例 17

```text
delivering_date_from
```

### 示例 18

```text
delivering_date_to
```

### 示例 19

```json
{
  "dir": "ASC",
  "filter": {
    "cutoff_from": "2021-08-24T14:15:22Z",
    "cutoff_to": "2021-08-31T14:15:22Z",
    "delivery_method_id": [],
    "provider_id": [],
    "status": "awaiting_packaging",
    "warehouse_id": []
  },
  "limit": 100,
  "offset": 0,
  "with": {
    "analytics_data": true,
    "barcodes": true,
    "financial_data": true,
    "legal_info": false,
    "translit": true
  }
}
```

### 示例 20

```json
{
  "has_next": true,
  "cursor": "eyJmaWVsZHMiOlt7Im5hbWUiOiJvc3AuY3V0b2ZmIiwiZGlyIjoiYXNjIiwidmFsIjoiMjAyNi0wMy0zMVQwOTowMDowMFoifSx7Im5hbWUiOiJvc3AuaW5fcHJvY2Vzc19hdCIsImRpciI6ImFzYyIsInZhbCI6IjIwMjYtMDMtMzBUMTE6MjY6MDhaIn0seyJuYW1lIjoib3NwLmlkIiwiZGlyIjoiYXNjIiwidmFsIjoiMTIwOTM3NTA2MiJ9LHsibmFtZSI6Im9zcC5pZCIsImRpciI6ImFzYyIsInZhbCI6IjEyMDkzNzUwNjIifV19",
  "postings": [
    {
      "posting_number": "0132112277-0102-1",
      "order_id": 35566808085,
      "order_number": "0132112277-0102",
      "pickup_code_verified_at": null,
      "status": "awaiting_packaging",
      "substatus": "posting_created",
      "delivery_method": {
        "id": 1020005003107121,
        "name": "Ozon自发货，诺金斯克",
        "warehouse_id": 1020005003107121,
        "warehouse": "FBS LikeSK",
        "tpl_provider_id": 24,
        "tpl_provider": "Ozon配送"
      },
      "delivery_schema": "fbs",
      "tracking_number": "",
      "tpl_integration_type": "ozon",
      "in_process_at": "2026-03-30T11:26:08Z",
      "shipment_date": "2026-03-31T09:00:00Z",
      "shipment_date_without_delay": "2026-04-04T16:59:00Z",
      "optional": {
        "products_with_possible_mandatory_mark": []
      },
      "cancellation": {
        "cancel_reason_id": 0,
        "cancel_reason": "",
        "cancellation_type": "",
        "cancelled_after_ship": false,
        "affect_cancellation_rating": false,
        "cancellation_initiator": ""
      },
      "customer": null,
      "products": [
        {
          "is_blr_traceable": false,
          "is_marketplace_buyout": false,
          "offer_id": "SK-58（深红色）",
          "name": "Cronier cr-2013专业非洲小卷卷发棒，9毫米",
          "sku": 827098843,
          "quantity": 1,
          "imei": [],
          "weight": 0.55,
          "product_color": "深红色",
          "price": {
            "amount": "1530",
            "currency": "RUB"
          }
        }
      ],
      "addressee": null,
      "barcodes": null,
      "analytics_data": null,
      "destination_place_id": 0,
      "destination_place_name": "",
      "financial_data": null,
      "is_express": false,
      "legal_info": null,
      "quantum_id": 0,
      "require_blr_traceable_attrs": false,
      "requirements": {
        "products_requiring_gtd": [],
        "products_requiring_country": [],
        "products_requiring_mandatory_mark": [],
        "products_requiring_rnpt": [],
        "products_requiring_jw_uin": [],
        "products_requiring_change_country": [],
        "products_requiring_imei": [],
        "products_requiring_weight": []
      },
      "tariffication": {
        "current_tariff_rate": 0,
        "current_tariff_type": "no_discount",
        "current_tariff_charge": {
          "amount": "0",
          "currency": "RUB"
        },
        "current_tariff_min_charge": null,
        "next_tariff_rate": 1,
        "next_tariff_type": "commission",
        "next_tariff_charge": {
          "amount": "50",
          "currency": "RUB"
        },
        "next_tariff_min_charge": {
          "amount": "50",
          "currency": "RUB"
        },
        "next_tariff_starts_at": "2026-03-31T09:00:01Z"
      },
      "external_order": {
        "is_external": false,
        "platform_name": ""
      },
      "volume_weight": 0,
      "is_click_and_collect": false,
      "delivering_date": null,
      "is_multibox": false,
      "multi_box_qty": 1,
      "is_presortable": false,
      "prr_option": "",
      "parent_posting_number": "",
      "available_actions": [
        "cancel",
        "has_barcode_for_printing",
        "product_cancel",
        "ship",
        "ship_async"
      ],
      "tariffication_steps": [
        {
          "min_charge": null,
          "tariff_charge": {
            "amount": "0",
            "currency": "RUB"
          },
          "tariff_deadline_at": "2026-03-31T09:00:00Z",
          "tariff_rate": 0,
          "tariff_type": "no_discount"
        },
        {
          "min_charge": {
            "amount": "50",
            "currency": "RUB"
          },
          "tariff_charge": {
            "amount": "50",
            "currency": "RUB"
          },
          "tariff_deadline_at": "2026-03-31T21:00:00Z",
          "tariff_rate": 1,
          "tariff_type": "commission"
        },
        {
          "min_charge": {
            "amount": "50",
            "currency": "RUB"
          },
          "tariff_charge": {
            "amount": "50",
            "currency": "RUB"
          },
          "tariff_deadline_at": "2026-04-01T09:00:00Z",
          "tariff_rate": 1,
          "tariff_type": "commission"
        },
        {
          "min_charge": {
            "amount": "100",
            "currency": "RUB"
          },
          "tariff_charge": {
            "amount": "100",
            "currency": "RUB"
          },
          "tariff_deadline_at": "2026-04-01T21:00:00Z",
          "tariff_rate": 2,
          "tariff_type": "commission"
        },
        {
          "min_charge": {
            "amount": "100",
            "currency": "RUB"
          },
          "tariff_charge": {
            "amount": "100",
            "currency": "RUB"
          },
          "tariff_deadline_at": "2026-04-02T09:00:00Z",
          "tariff_rate": 2,
          "tariff_type": "commission"
        },
        {
          "min_charge": {
            "amount": "150",
            "currency": "RUB"
          },
          "tariff_charge": {
            "amount": "150",
            "currency": "RUB"
          },
          "tariff_deadline_at": "9999-12-31T23:59:59.999999900Z",
          "tariff_rate": 3,
          "tariff_type": "commission"
        }
      ]
    }
  ],
  "count": 38
}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

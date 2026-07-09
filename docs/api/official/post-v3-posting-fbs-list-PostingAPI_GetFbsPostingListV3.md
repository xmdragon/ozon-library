# 货件列表 Deprecated

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v3/posting/fbs/list`
- Operation ID：`PostingAPI_GetFbsPostingListV3`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/PostingAPI_GetFbsPostingListV3
- 分组：`posting`

## 页面标题结构

- 货件列表 Deprecated
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
| `filter` required | object 过滤器。 |
| `limit` required | integer <int64> 响应中值的数量： 最大值 — 1000, 最小值 — 1。 |
| `offset` required | integer <int64> 将在响应中跳过的元素数。 例如，如果“offset=10”，那么响应将从找到的第11个元素开始。 |
| `with` | object 要添加到响应的附加字段。 |

### 表格 2

| 字段 | 类型/说明 |
| --- | --- |
| `result` | object 货运数组。 |
| `has_next` | boolean 响应中未返回整个货运数组的标志: true — 必须提出含其他值 offset的新请求，以获得其他货运信息； false — 响应中返回了在请求中提出的整个用于过滤的货运数组。 |
| `postings` | Array of objects 货运信息。 |

### 表格 3

| 字段 | 类型/说明 |
| --- | --- |
| `has_next` | boolean 响应中未返回整个货运数组的标志: true — 必须提出含其他值 offset的新请求，以获得其他货运信息； false — 响应中返回了在请求中提出的整个用于过滤的货运数组。 |
| `postings` | Array of objects 货运信息。 |

## 示例

### 示例 0

```text
has_next = true
```

### 示例 1

```text
offset
```

### 示例 2

```text
asc
```

### 示例 3

```text
desc
```

### 示例 4

```text
true
```

### 示例 5

```text
offset
```

### 示例 6

```text
false
```

### 示例 7

```json
{
  "dir": "ASC",
  "filter": {
    "delivery_method_id": [
      "21321684811000"
    ],
    "fbpFilter": "string",
    "last_changed_status_date": {
      "from": "2023-11-03T11:47:39.878Z",
      "to": "2023-11-03T11:47:39.878Z"
    },
    "order_id": 0,
    "provider_id": [
      "24"
    ],
    "since": "2023-11-03T11:47:39.878Z",
    "status": "awaiting_packaging",
    "to": "2023-11-03T11:47:39.878Z",
    "warehouse_id": [
      "21321684811000"
    ]
  },
  "limit": 100,
  "offset": 0,
  "with": {
    "analytics_data": true,
    "barcodes": true,
    "financial_data": true,
    "translit": true
  }
}
```

### 示例 8

```json
{
  "result": {
    "postings": [
      {
        "posting_number": "0132112277-0101-1",
        "order_id": 35566798085,
        "order_number": "0132112277-0101",
        "status": "awaiting_packaging",
        "delivery_method": {
          "id": 1020005003107121,
          "name": "Ozon自发货，诺金斯克",
          "warehouse_id": 1020005003107121,
          "warehouse": "FBS LikeSK",
          "tpl_provider_id": 24,
          "tpl_provider": "Ozon配送"
        },
        "tracking_number": "",
        "tpl_integration_type": "ozon",
        "in_process_at": "2026-03-30T11:26:00Z",
        "shipment_date": "2026-03-31T09:00:00Z",
        "delivering_date": null,
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
            "price": "1530.0000",
            "offer_id": "SK-58（深红色）",
            "name": "Cronier cr-2013专业非洲小卷卷发棒，9毫米",
            "sku": 827098843,
            "quantity": 1,
            "currency_code": "RUB",
            "is_blr_traceable": false,
            "is_marketplace_buyout": false,
            "imei": []
          }
        ],
        "addressee": null,
        "barcodes": {
          "upper_barcode": "711008270053000",
          "lower_barcode": "711008270053000"
        },
        "analytics_data": {
          "region": "",
          "city": "",
          "delivery_type": "PVZ",
          "is_premium": false,
          "payment_type_group_name": "Ozon Банк",
          "warehouse_id": 1020005003107121,
          "warehouse": "FBS LikeSK",
          "tpl_provider_id": 24,
          "tpl_provider": "Доставка Ozon",
          "delivery_date_begin": "2026-04-11T15:00:00Z",
          "delivery_date_end": "2026-04-11T16:00:00Z",
          "is_legal": false,
          "client_delivery_date_begin": null,
          "client_delivery_date_end": null
        },
        "financial_data": {
          "products": [
            {
              "commission_amount": 0,
              "commission_percent": 0,
              "payout": 0,
              "product_id": 827098843,
              "old_price": 1530,
              "price": 1530,
              "total_discount_value": 0,
              "total_discount_percent": 0,
              "actions": [
                "Округление"
              ],
              "quantity": 1,
              "currency_code": "RUB",
              "customer_currency_code": "RUB",
              "customer_price": 662.86
            }
          ],
          "cluster_from": "Moskva, MO i Dal`nie regiony`",
          "cluster_to": "Rostov"
        },
        "is_express": false,
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
        "parent_posting_number": "",
        "available_actions": [
          "cancel",
          "has_barcode_for_printing",
          "product_cancel",
          "ship",
          "ship_async"
        ],
        "multi_box_qty": 1,
        "is_multibox": false,
        "substatus": "posting_created",
        "prr_option": "",
        "quantum_id": 0,
        "tariffication": {
          "current_tariff_rate": 0,
          "current_tariff_type": "no_discount",
          "current_tariff_charge": "",
          "current_tariff_charge_currency_code": "RUB",
          "next_tariff_rate": 0,
          "next_tariff_type": "commission",
          "next_tariff_charge": "50",
          "next_tariff_starts_at": "2026-03-31T09:00:01Z",
          "next_tariff_charge_currency_code": "RUB"
        },
        "destination_place_id": 0,
        "destination_place_name": "",
        "is_presortable": false,
        "pickup_code_verified_at": null,
        "optional": {
          "products_with_possible_mandatory_mark": []
        },
        "legal_info": {
          "company_name": "",
          "inn": "",
          "kpp": ""
        },
        "shipment_date_without_delay": "2026-04-04T16:59:00Z",
        "require_blr_traceable_attrs": false,
        "is_click_and_collect": false,
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
    "has_next": false
  }
}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

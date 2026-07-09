# 获取货件列表

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v4/posting/fbs/list`
- Operation ID：`PostingFbsList`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/PostingFbsList
- 分组：`posting`

## News 更新标记

| 日期 | 标记 | 摘要 | 来源 |
| --- | --- | --- | --- |
| 2026-04-30 | `new_method` | /v4/posting/fbs/list 新增了用于获取FBS货件列表的方法新版本。 | [官方 News](https://docs.ozon.ru/api/seller/zh/#section/2026430) |

## 页面标题结构

- 获取货件列表
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
| `cursor` | string 用于选择下一批数据的指针。 |
| `filter` required | object 筛选器。 |
| `limit` required | integer <int64> [ 1 .. 100 ] 响应中返回的值数量。 |
| `sort_dir` | string Enum: "ASC" "DESC" 排序方向： ASC——升序； DESC——降序。 |
| `translit` | boolean 若为true，则启用将地址从西里尔字母转写为拉丁字母。 |
| `with` | object 需要添加到响应中的附加字段。 |

### 表格 2

| 字段 | 类型/说明 |
| --- | --- |
| `cursor` | string 用于选择下一批数据的指针。 |
| `has_next` | boolean 若响应中未返回全部货件，则为true。 |
| `postings` | Array of objects 货件列表。 |

## 示例

### 示例 0

```text
ASC
```

### 示例 1

```text
DESC
```

### 示例 2

```text
true
```

### 示例 3

```text
true
```

### 示例 4

```json
{
  "sort_dir": "asc",
  "filter": {
    "order_numbers": [
      "12345-1"
    ],
    "delivery_method_ids": [
      123456789
    ],
    "is_blr_traceable": false,
    "last_changed_status_date": {
      "from": "2026-04-01T19:47:39.878Z",
      "to": "2026-04-02T11:47:39.878Z"
    },
    "order_id": 123456,
    "since": "2026-04-01T19:47:39.878Z",
    "to": "2026-04-02T11:47:39.878Z",
    "statuses": [
      "awaiting_packaging",
      "awaiting_deliver",
      "delivering",
      "delivered"
    ],
    "provider_ids": [
      123
    ],
    "warehouse_ids": [
      3092889984
    ]
  },
  "limit": 100,
  "cursor": "",
  "with": {
    "analytics_data": true,
    "barcodes": true,
    "financial_data": true,
    "legal_info": true,
    "translit": true
  }
}
```

### 示例 5

```json
{
  "cursor": "eyJmaWVsZHMiOlt7Im5hbWUiOiJvc3AuaW5fcHJvY2Vzc19hdCIsImRpciI6ImFzYyIsInZhbCI6IjIwMjYtMDEtMTVUMTA6MzA6MDBaIn0seyJuYW1lIjoib3NwLmlkIiwiZGlyIjoiYXNjIiwidmFsIjoiMTIzNDU2Nzg5MCJ9XX0=",
  "has_next": false,
  "postings": [
    {
      "addressee": {
        "name": "Ivan Petrov"
      },
      "analytics_data": {
        "city": "莫斯科",
        "client_delivery_date_begin": "2026-05-20T08:00:00.000Z",
        "client_delivery_date_end": "2026-05-22T20:00:00.000Z",
        "delivery_date_begin": "2026-05-18T08:00:00.000Z",
        "delivery_date_end": "2026-05-19T20:00:00.000Z",
        "delivery_type": "PVZ",
        "is_legal": false,
        "is_premium": true,
        "payment_type_group_name": "银行卡",
        "region": "莫斯科州",
        "tpl_provider": "Ozon配送",
        "tpl_provider_id": 24,
        "warehouse": "索菲诺",
        "warehouse_id": 17023
      },
      "available_actions": [
        "pack",
        "ship",
        "cancel"
      ],
      "barcodes": {
        "lower_barcode": "601302481800001",
        "upper_barcode": "601302481800001"
      },
      "cancellation": {
        "affect_cancellation_rating": false,
        "cancel_reason": "",
        "cancel_reason_id": 0,
        "cancellation_initiator": "",
        "cancellation_type": "",
        "cancelled_after_ship": false
      },
      "container": {
        "cargo_type": "BOX",
        "container_date": "2026-05-14",
        "container_id": 100500,
        "container_number": 42
      },
      "container_sort_type": "standard",
      "customer": {
        "address": {
          "address_tail": "д. 15, кв. 78",
          "city": "莫斯科",
          "comment": "对讲机坏了",
          "country": "俄罗斯",
          "district": "中央行政区",
          "latitude": 55.7558,
          "longitude": 37.6176,
          "provider_pvz_code": "PVZ123",
          "pvz_code": 456,
          "region": "莫斯科",
          "zip_code": "101000"
        },
        "customer_email": "ivan.petrov@example.com",
        "customer_id": 12345678,
        "name": "Ivan Petrov",
        "phone": "+79031234567"
      },
      "delivering_date": "2026-05-19T15:30:00.000Z",
      "delivery_method": {
        "id": 20605650762000,
        "name": "Ozon配送（自发货），索菲诺",
        "tpl_provider": "Ozon配送",
        "tpl_provider_id": 24,
        "warehouse": "17023",
        "warehouse_id": 20605650762000
      },
      "delivery_schema": "fbs",
      "destination_place_id": 500,
      "destination_place_name": "特维尔大街上的取货点 123",
      "external_order": {
        "is_external": false,
        "platform_name": ""
      },
      "financial_data": {
        "cluster_from": "莫斯科",
        "cluster_to": "喀山",
        "products": [
          {
            "actions": [
              "四舍五入"
            ],
            "commission": {
              "amount": 120,
              "currency": "RUB",
              "percent": 10
            },
            "customer_price": {
              "amount": "2500.00",
              "currency": "RUB"
            },
            "old_price": 3000,
            "payout": 2100,
            "price": 2500,
            "product_id": 1904686181,
            "quantity": 2,
            "total_discount_percent": 16.67,
            "total_discount_value": 500
          }
        ]
      },
      "in_process_at": "2026-05-14T08:00:00.000Z",
      "is_click_and_collect": false,
      "is_express": false,
      "is_multibox": false,
      "is_presortable": true,
      "legal_info": {
        "company_name": "OOO 甘菊",
        "inn": "7701234567",
        "kpp": "770101001"
      },
      "multi_box_qty": 1,
      "optional": {
        "products_with_possible_mandatory_mark": []
      },
      "order_id": 33301885134,
      "order_number": "0208245774-0029",
      "parent_posting_number": "",
      "pickup_code_verified_at": null,
      "posting_number": "0208245774-0029-1",
      "products": [
        {
          "imei": [],
          "is_blr_traceable": false,
          "is_marketplace_buyout": true,
          "name": "小米Note 12智能手机",
          "offer_id": "b4408110",
          "price": {
            "amount": "12990.00",
            "currency": "RUB"
          },
          "product_color": "黑",
          "quantity": 1,
          "sku": 1904686181,
          "weight": 0.42
        },
        {
          "imei": [
            "123456789012345",
            "987654321098765"
          ],
          "is_blr_traceable": false,
          "is_marketplace_buyout": false,
          "name": "蓝牙耳机",
          "offer_id": "h667722",
          "price": {
            "amount": "3490.00",
            "currency": "RUB"
          },
          "product_color": "白",
          "quantity": 2,
          "sku": 1904686182,
          "weight": 0.15
        }
      ],
      "prr_option": "standard",
      "quantum_id": 98765,
      "require_blr_traceable_attrs": false,
      "requirements": {
        "products_requiring_change_country": [],
        "products_requiring_country": [],
        "products_requiring_gtd": [
          "1904686181"
        ],
        "products_requiring_imei": [],
        "products_requiring_jw_uin": [],
        "products_requiring_mandatory_mark": [],
        "products_requiring_rnpt": []
      },
      "shipment_date": "2026-05-18T12:00:00.000Z",
      "shipment_date_without_delay": "2026-05-18T12:00:00.000Z",
      "status": "awaiting_packaging",
      "substatus": "posting_created",
      "tariffication": {
        "current_tariff_charge": {
          "amount": "100.00",
          "currency": "RUB"
        },
        "current_tariff_min_charge": {
          "amount": "50.00",
          "currency": "RUB"
        },
        "current_tariff_rate": 2,
        "current_tariff_type": "commission",
        "next_tariff_charge": {
          "amount": "150.00",
          "currency": "RUB"
        },
        "next_tariff_min_charge": {
          "amount": "100.00",
          "currency": "RUB"
        },
        "next_tariff_rate": 2.5,
        "next_tariff_starts_at": "2026-05-20T00:00:00.000Z",
        "next_tariff_type": "commission"
      },
      "tariffication_steps": [
        {
          "min_charge": {
            "amount": "24.00",
            "currency": "RUB"
          },
          "tariff_charge": {
            "amount": "24.00",
            "currency": "RUB"
          },
          "tariff_deadline_at": "2026-05-15T23:59:59.000Z",
          "tariff_rate": 2,
          "tariff_type": "discount"
        }
      ],
      "tpl_integration_type": "ozon",
      "tracking_number": "TRK1234567890",
      "volume_weight": 1.2
    }
  ]
}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

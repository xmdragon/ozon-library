# 获取交货列表

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/fbp/order/list`
- Operation ID：`FbpAPI_FbpOrderList`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/FbpAPI_FbpOrderList
- 分组：`fbp`

## 页面标题结构

- 获取交货列表
- Request Body schema: application/json
- 回复
- Response Schema: application/json
- 请求范例
- 回复范例

## 参数与返回结构

### 表格 0

| 字段 | 类型/说明 |
| --- | --- |
| `count` required | integer <int32> 响应中的交货数量。 |
| `last_id` | integer <int64> 页面上最后一次交货的标识符。首次请求时请将此字段留空。 如需获取后续数据，请填写上一次请求响应中最后一次交货的id。 |

### 表格 1

| 字段 | 类型/说明 |
| --- | --- |
| `has_next` | boolean true，如果响应中未返回所有交货。 |
| `items` | Array of objects 交货。 |
| `last_id` | integer <int64> 页面上最后一次交货的标识符。 |

## 示例

### 示例 0

```text
id
```

### 示例 1

```text
true
```

### 示例 2

```json
{"count": 0,"last_id": 0}
```

### 示例 3

```json
{"has_next": true,"items": [{"attention_reasons": "ORDER_ATTENTION_TYPE_UNSPECIFIED","bundle_summary": {"rounded_total_volume_in_litres": 0,"total_item_count": 0,"total_quantity": 0},"can_be_cancelled": true,"cancellation_state": {"cancellation_error": {"error_code": "CODE_UNSPECIFIED","message": "string"},"cancellation_status": "STATUS_UNSPECIFIED"},"created_date": "2019-08-24T14:15:22Z","delivery_details": {"direct_details": {"by_seller_details": {"driver_name": "string","vehicle_registration_number": "string","vehicle_type": "string"},"by_tpl_details": {"tracking_number": "string","transport_company_name": "string"},"timeslot_details": {"timeslot": {"timeslot_end": "2019-08-24T14:15:22Z","timeslot_start": "2019-08-24T14:15:22Z"},"timeslot_reservation_id": "string"}},"drop_off_point": {"id": 0,"province_uuid": "string","timeslot": {"timeslot_end": "2019-08-24T14:15:22Z","timeslot_start": "2019-08-24T14:15:22Z"}},"pickup_details": {"address": "string","comment": "string","date": "2019-08-24T14:15:22Z","sender_name": "string","sender_phone": "string"},"supply_type": "SUPPLY_TYPE_UNSPECIFIED"},"has_consignment_note": true,"has_label": true,"id": 0,"locked": true,"order_number": "string","package_units_count": 0,"receive_date": "2019-08-24T14:15:22Z","status": "ORDER_STATUS_UNSPECIFIED","supply_id": "string","warehouse_id": 0}],"last_id": 0}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

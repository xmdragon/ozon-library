# 交货草稿列表

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/fbp/draft/list`
- Operation ID：`FbpAPI_FbpDraftList`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/FbpAPI_FbpDraftList
- 分组：`fbp`

## 页面标题结构

- 交货草稿列表
- Request Body schema: application/json
- 回复
- Response Schema: application/json
- 请求范例
- 回复范例

## 参数与返回结构

### 表格 0

| 字段 | 类型/说明 |
| --- | --- |
| `count` required | integer <int32> 响应中的商品数量。 |
| `last_id` | integer <int64> 页面上最后一个值的ID。运行第一个查询时，将此字段留空。 要检索以下数值，请从上一个查询的响应中指定last_id。 |

### 表格 1

| 字段 | 类型/说明 |
| --- | --- |
| `has_next` | boolean true，如果响应中没有返回所有值。 |
| `items` | Array of objects 草稿。 |
| `last_id` | integer <int64> 页面上最后一个值的标识符。 |

## 示例

### 示例 0

```text
last_id
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
{"has_next": true,"items": [{"bundle_id": "string","cancellation_state": {"cancellation_error": {"error_code": "CODE_UNSPECIFIED","message": "string"},"cancellation_status": "STATUS_UNSPECIFIED"},"created_at": "2019-08-24T14:15:22Z","deleted_at": "2019-08-24T14:15:22Z","delivery_details": {"direct_details": {"by_seller_details": {"driver_name": "string","vehicle_registration_number": "string","vehicle_type": "string"},"by_tpl_details": {"tracking_number": "string","transport_company_name": "string"},"timeslot_details": {"timeslot": {"timeslot_end": "2019-08-24T14:15:22Z","timeslot_start": "2019-08-24T14:15:22Z"},"timeslot_reservation_id": "string"}},"drop_off_point": {"id": 0,"province_uuid": "string","timeslot": {"timeslot_end": "2019-08-24T14:15:22Z","timeslot_start": "2019-08-24T14:15:22Z"}},"pickup_details": {"address": "string","comment": "string","date": "2019-08-24T14:15:22Z","sender_name": "string","sender_phone": "string"},"supply_type": "SUPPLY_TYPE_UNSPECIFIED"},"editable": true,"id": 0,"is_cancelable": true,"is_deletable": true,"locked": true,"package_units_count": 0,"status": "DRAFT_STATUS_UNSPECIFIED","supply_id": "string","warehouse_id": 0}],"last_id": 0}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

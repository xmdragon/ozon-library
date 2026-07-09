# 获取已完成交货列表

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/fbp/archive/list`
- Operation ID：`FbpAPI_FbpArchiveList`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/FbpAPI_FbpArchiveList
- 分组：`fbp`

## 页面标题结构

- 获取已完成交货列表
- Request Body schema: application/json
- 回复
- Response Schema: application/json
- 请求范例
- 回复范例

## 参数与返回结构

### 表格 0

count required string <int32> 响应中的元素数量。 last_idstring <int64> 页面上最后一个值的标识符。首次请求时请留空。 如需获取后续数据，请填写上次响应中的 last_id。

### 表格 1

has_nextboolean true，前提是本次响应未返回所有数据。 itemsArray of objects 已完成交货。 last_idinteger <int64> 页面上最后一个值的标识符。

## 示例

### 示例 0

```json
{"count": "string","last_id": "string"}
```

### 示例 1

```json
{"has_next": true,"items": [{"act_file_uuid": "string","bundle_id": "string","bundle_sku_summary": {"rounded_total_volume_in_litres": 0,"total_items_count": 0,"total_quantity": 0},"created_date": "2019-08-24T14:15:22Z","decline_reason": {"code": "DECLINE_REASON_CODE_UNSPECIFIED","message": "string"},"delivery_details": {"direct_details": {"by_seller_details": {"driver_name": "string","vehicle_registration_number": "string","vehicle_type": "string"},"by_tpl_details": {"tracking_number": "string","transport_company_name": "string"},"timeslot_details": {"timeslot": {"timeslot_end": "2019-08-24T14:15:22Z","timeslot_start": "2019-08-24T14:15:22Z"},"timeslot_reservation_id": "string"}},"drop_off_point": {"id": 0,"province_uuid": "string","timeslot": {"timeslot_end": "2019-08-24T14:15:22Z","timeslot_start": "2019-08-24T14:15:22Z"}},"pickup_details": {"address": "string","comment": "string","date": "2019-08-24T14:15:22Z","sender_name": "string","sender_phone": "string"},"supply_type": "SUPPLY_TYPE_UNSPECIFIED"},"external_order_id": "string","has_act": true,"has_label": true,"order_draft_id": 0,"package_units_count": 0,"receive_date": "2019-08-24T14:15:22Z","row_version": 0,"status": "ARCHIVE_STATUS_UNSPECIFIED","supply_id": "string","warehouse_id": 0,"whc_order_id": 0}],"last_id": 0}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

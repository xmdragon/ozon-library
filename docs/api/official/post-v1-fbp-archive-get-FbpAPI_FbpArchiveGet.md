# 获取已完成交货信息

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/fbp/archive/get`
- Operation ID：`FbpAPI_FbpArchiveGet`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/FbpAPI_FbpArchiveGet
- 分组：`fbp`

## 页面标题结构

- 获取已完成交货信息
- Request Body schema: application/json
- 回复
- Response Schema: application/json
- 请求范例
- 回复范例

## 参数与返回结构

### 表格 0

| 字段 | 类型/说明 |
| --- | --- |
| `supply_id` required | string 交货标识符。 |

### 表格 1

| 字段 | 类型/说明 |
| --- | --- |
| `act_file_uuid` | string 验收证明书标识符。 |
| `bundle_id` | string 已验证商品清单的标识符。 |
| `bundle_sku_summary` | object 交货商品汇总信息。 |
| `business_flow_type_id` | integer <int64> 交货类型标识符。 |
| `created_date` | string <date-time> 交货申请创建日期和时间。 |
| `decline_reason` | object 拒绝交货的原因。 |
| `delivery_details` | object 配送详情。 |
| `has_act` | boolean true，前提是已生成交接单。 |
| `has_label` | boolean true，前提是已生成标签。 |
| `id` | integer <int64> 档案记录编号。 |
| `order_draft_id` | integer <int64> 交货草稿标识符。 |
| `order_number` | string 已完成交货标识符。 |
| `package_units_count` | integer <int32> 货位数量。 |
| `receive_date` | string <date-time> 交货接收日期和时间。 |
| `row_version` | integer <int64> 草稿的当前版本标识符。 |
| `status` | string Default: "ARCHIVE_STATUS_UNSPECIFIED" Enum: "ARCHIVE_STATUS_UNSPECIFIED" "COMPLETED" "REJECTED_AT_SUPPLY_WAREHOUSE" "CANCELLED_BY_SELLER" 已完成的交货状态： ARCHIVE_STATUS_UNSPECIFIED：未指定； COMPLETED：已完成； REJECTED_AT_SUPPLY_WAREHOUSE：被仓库拒绝； CANCELLED_BY_SELLER：卖家取消。 |
| `supply_id` | string 交货标识符。 |
| `warehouse_id` | integer <int64> 仓库标识符。 |

## 示例

### 示例 0

```text
true
```

### 示例 1

```text
true
```

### 示例 2

```text
ARCHIVE_STATUS_UNSPECIFIED
```

### 示例 3

```text
COMPLETED
```

### 示例 4

```text
REJECTED_AT_SUPPLY_WAREHOUSE
```

### 示例 5

```text
CANCELLED_BY_SELLER
```

### 示例 6

```json
{"supply_id": "string"}
```

### 示例 7

```json
{"act_file_uuid": "string","bundle_id": "string","bundle_sku_summary": {"rounded_total_volume_in_litres": 0,"total_items_count": 0,"total_quantity": 0},"business_flow_type_id": 0,"created_date": "2019-08-24T14:15:22Z","decline_reason": {"code": "DECLINE_REASON_CODE_UNSPECIFIED","message": "string"},"delivery_details": {"direct_details": {"by_seller_details": {"driver_name": "string","vehicle_registration_number": "string","vehicle_type": "string"},"by_tpl_details": {"tracking_number": "string","transport_company_name": "string"},"timeslot_details": {"timeslot": {"timeslot_end": "2019-08-24T14:15:22Z","timeslot_start": "2019-08-24T14:15:22Z"},"timeslot_reservation_id": "string"}},"drop_off_point": {"id": 0,"province_uuid": "string","timeslot": {"timeslot_end": "2019-08-24T14:15:22Z","timeslot_start": "2019-08-24T14:15:22Z"}},"pickup_details": {"address": "string","comment": "string","date": "2019-08-24T14:15:22Z","sender_name": "string","sender_phone": "string"},"supply_type": "SUPPLY_TYPE_UNSPECIFIED"},"has_act": true,"has_label": true,"id": 0,"order_draft_id": 0,"order_number": "string","package_units_count": 0,"receive_date": "2019-08-24T14:15:22Z","row_version": 0,"status": "ARCHIVE_STATUS_UNSPECIFIED","supply_id": "string","warehouse_id": 0}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

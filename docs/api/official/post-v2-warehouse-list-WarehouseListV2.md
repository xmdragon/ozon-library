# 仓库列表

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v2/warehouse/list`
- Operation ID：`WarehouseListV2`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/WarehouseListV2
- 分组：`warehouse`

## 页面标题结构

- 仓库列表
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
| `limit` required | integer <= 200 响应中返回的值数量。 |
| `cursor` | string 后续数据的选择标志。 |
| `warehouse_ids` | Array of strings <int64> <= 200 仓库识别符。 |

### 表格 2

| 字段 | 类型/说明 |
| --- | --- |
| `cursor` | string 后续数据的选择标志。 |
| `warehouses` | Array of objects 仓库列表。 |
| `has_next` | boolean true，前提是本次响应未返回所有数据。 |

## 示例

### 示例 0

```text
true
```

### 示例 1

```json
{"cursor": "string","limit": 0,"warehouse_ids": [20605650762000]}
```

### 示例 2

```json
{"cursor": "string","warehouses": [{"address_info": {"address": "Россия, Московская Область, Софьино, промзона ССТ, к2, 2","latitude": 55.495093,"longitude": 38.172731,"utc": "UTC+03:00"},"carriage_label_type": "BIG","courier_comment": "","courier_phones": ["+7(999)999-99-99"],"created_at": "2025-03-11T11:57:51.811Z","first_mile": {"type": "PICK_UP","dropoff_point_id": "1020002075314000","timeslot_from": "20:59","timeslot_id": 287231,"timeslot_to": "21:00","first_mile_is_changing": false},"has_entrusted_acceptance": true,"has_postings_limit": false,"is_auto_assembly": true,"is_kgt": true,"is_rfbs": true,"is_waybill_enabled": true,"min_postings_limit": 2,"is_comfort": true,"is_express": true,"warehouse_type": "string","cut_in_time": 0,"name": "17023","phone": "+7(999)999-99-99","postings_limit": -1,"sla_cut_in": 2939,"status": "created","timetable": {"timetable_from": "2025-03-11T11:57:51.811Z","timetable_to": "2025-03-11T11:57:51.811Z","working_hours": [{"time_from": "2025-03-11T11:57:51.811Z","time_to": "2025-03-11T11:57:51.811Z"}]},"updated_at": "2025-03-11T11:57:51.811Z","warehouse_id": 20605650762000,"with_item_list": true,"working_days": ["MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY"]}],"has_next": "string"}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

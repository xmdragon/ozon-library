# 可供运输的列表

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/posting/carriage-available/list`
- Operation ID：`PostingAPI_GetCarriageAvailableList`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/PostingAPI_GetCarriageAvailableList
- 分组：`posting`

## 页面标题结构

- 可供运输的列表
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
| `delivery_method_id` required | integer <int64> 按照运输方式筛选。可以使用方法 /v1/delivery-method/list获取。 |
| `departure_date` | string <date-time> 装运日期。默认 —— 当前日期。 |

### 表格 2

| 字段 | 类型/说明 |
| --- | --- |
| `result` | Array of objects 方法操作结果。 |
| `carriage_id` | integer <int64> 运输ID（也是文件形成的任务编号）。 |
| `carriage_postings_count` | integer <int32> 运输中的货件数量。 |
| `carriage_status` | string 所请求的交付方式和装运日期的运输状态。 |
| `cutoff_at` | string <date-time> 需要收取货件的日期和时间。 |
| `delivery_method_id` | integer <int64> 快递方式ID。 |
| `delivery_method_name` | string 快递方式名称。 |
| `errors` | Array of objects 错误列表。 |
| `first_mile_type` | string 第一英里类型。 |
| `has_entrusted_acceptance` | boolean 信任接收的标志。 如果在仓库中启用了信任接收，则为“true”。 |
| `mandatory_postings_count` | integer <int32> 需要收取的货件数量。 |
| `mandatory_packaged_count` | integer <int32> 收取货件数量。 |
| `recommended_time_local` | string 推荐的本地发运时间（订单接收点）。 |
| `recommended_time_utc_offset_in_minutes` | number <int32> 推荐发运时间与UTC-0的时区偏移量（以分钟为单位）。 |
| `tpl_provider_icon_url` | string 快递服务图标的链接。 |
| `tpl_provider_name` | string 快递服务名称。 |
| `warehouse_city` | string 仓库所在城市。 |
| `warehouse_id` | integer <int64> 仓库ID。 |
| `warehouse_name` | string 仓库名称。 |
| `warehouse_timezone` | string 仓库所在时区。 |

### 表格 3

| 字段 | 类型/说明 |
| --- | --- |
| `carriage_id` | integer <int64> 运输ID（也是文件形成的任务编号）。 |
| `carriage_postings_count` | integer <int32> 运输中的货件数量。 |
| `carriage_status` | string 所请求的交付方式和装运日期的运输状态。 |
| `cutoff_at` | string <date-time> 需要收取货件的日期和时间。 |
| `delivery_method_id` | integer <int64> 快递方式ID。 |
| `delivery_method_name` | string 快递方式名称。 |
| `errors` | Array of objects 错误列表。 |
| `first_mile_type` | string 第一英里类型。 |
| `has_entrusted_acceptance` | boolean 信任接收的标志。 如果在仓库中启用了信任接收，则为“true”。 |
| `mandatory_postings_count` | integer <int32> 需要收取的货件数量。 |
| `mandatory_packaged_count` | integer <int32> 收取货件数量。 |
| `recommended_time_local` | string 推荐的本地发运时间（订单接收点）。 |
| `recommended_time_utc_offset_in_minutes` | number <int32> 推荐发运时间与UTC-0的时区偏移量（以分钟为单位）。 |
| `tpl_provider_icon_url` | string 快递服务图标的链接。 |
| `tpl_provider_name` | string 快递服务名称。 |
| `warehouse_city` | string 仓库所在城市。 |
| `warehouse_id` | integer <int64> 仓库ID。 |
| `warehouse_name` | string 仓库名称。 |
| `warehouse_timezone` | string 仓库所在时区。 |

## 示例

### 示例 0

```json
{"delivery_method_id": 0,"departure_date": "2019-08-24T14:15:22Z"}
```

### 示例 1

```json
{"result": [{"carriage_id": 0,"carriage_postings_count": 0,"carriage_status": "string","cutoff_at": "2019-08-24T14:15:22Z","delivery_method_id": 0,"delivery_method_name": "string","errors": [{"code": "string","status": "string"}],"first_mile_type": "string","has_entrusted_acceptance": true,"mandatory_postings_count": 0,"mandatory_packaged_count": 0,"recommended_time_local": "string","recommended_time_utc_offset_in_minutes": 0,"tpl_provider_icon_url": "string","tpl_provider_name": "string","warehouse_city": "string","warehouse_id": 0,"warehouse_name": "string","warehouse_timezone": "string"}]}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

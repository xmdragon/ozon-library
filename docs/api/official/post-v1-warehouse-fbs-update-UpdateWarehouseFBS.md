# 更新仓库

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/warehouse/fbs/update`
- Operation ID：`UpdateWarehouseFBS`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/UpdateWarehouseFBS
- 分组：`warehouse`

## 页面标题结构

- 更新仓库
- header Parameters
- Request Body schema: application/json
- 回复
- Response Schema: application/jsonapplication/jsonexample
- 请求范例
- 回复范例

## 参数与返回结构

### 表格 0

Client-Id required string 用户识别号。 Api-Key required string API-密钥。

### 表格 1

address_coordinates required object 仓库坐标。 namestring >= 100 characters 仓库名称。 optionsobject 仓库参数。 phonestring+7(XXX)XXX-XX-XX 仓库电话号码。 warehouse_id required integer <int64> 仓库ID。 working_daysArray of strings [ 5 .. 7 ] Items Enum: "MONDAY" "TUESDAY" "WEDNESDAY" "THURSDAY" "FRIDAY" "SATURDAY" "SUNDAY" 仓库工作日： MONDAY — 周一； TUESDAY — 周二； WEDNESDAY — 周三； THURSDAY — 周四； FRIDAY — 周五； SATURDAY — 周六； SUNDAY — 周日。

### 表格 2

operation_idstring 操作ID。通过方法 /v1/warehouse/operation/status 获取操作状态。

## 示例

### 示例 0

```text
MONDAY
```

### 示例 1

```text
TUESDAY
```

### 示例 2

```text
WEDNESDAY
```

### 示例 3

```text
THURSDAY
```

### 示例 4

```text
FRIDAY
```

### 示例 5

```text
SATURDAY
```

### 示例 6

```text
SUNDAY
```

### 示例 7

```json
{"address_coordinates": {"latitude": 55.69626,"longitude": 37.42686},"name": "Склад Балашиха","options": {"comment": "Заезд на склад через главные ворота","courier_phones": ["+7(999)999-99-99"],"is_auto_assembly": true,"is_waybill_enabled": true},"phone": "+7(XXX)XXX-XX-XX","warehouse_id": 1020002929332000,"working_days": ["MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY"]}
```

### 示例 8

```json
{"operation_id": "string"}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

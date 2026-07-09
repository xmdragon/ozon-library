# 获取接收点的营业时间表

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/fbp/draft/drop-off/point/timetable`
- Operation ID：`FbpDraftDropOffPointTimetable`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/FbpDraftDropOffPointTimetable
- 分组：`fbp`

## 页面标题结构

- 获取接收点的营业时间表
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
| `drop_off_point_id` required | integer <int64> 揽收点标识符。 |
| `province_uuid` required | string 省份唯一标识符。 |
| `warehouse_id` required | integer <int64> 仓库标识符。 |

### 表格 2

| 字段 | 类型/说明 |
| --- | --- |
| `calendar` | Array of objects 接收点的营业时间表。 |
| `calendar_item` | object 营业时间表。 |
| `day_of_week` | string Default: "DAY_OF_WEEK_UNSPECIFIED" Enum: "DAY_OF_WEEK_UNSPECIFIED" "MONDAY" "TUESDAY" "WEDNESDAY" "THURSDAY" "FRIDAY" "SATURDAY" "SUNDAY" 星期： DAY_OF_WEEK_UNSPECIFIED——未指定； MONDAY——星期一； TUESDAY——星期二； WEDNESDAY——星期三； THURSDAY——星期四； FRIDAY——星期五； SATURDAY——星期六； SUNDAY——星期日。 |

### 表格 3

| 字段 | 类型/说明 |
| --- | --- |
| `calendar_item` | object 营业时间表。 |
| `day_of_week` | string Default: "DAY_OF_WEEK_UNSPECIFIED" Enum: "DAY_OF_WEEK_UNSPECIFIED" "MONDAY" "TUESDAY" "WEDNESDAY" "THURSDAY" "FRIDAY" "SATURDAY" "SUNDAY" 星期： DAY_OF_WEEK_UNSPECIFIED——未指定； MONDAY——星期一； TUESDAY——星期二； WEDNESDAY——星期三； THURSDAY——星期四； FRIDAY——星期五； SATURDAY——星期六； SUNDAY——星期日。 |

## 示例

### 示例 0

```text
DAY_OF_WEEK_UNSPECIFIED
```

### 示例 1

```text
MONDAY
```

### 示例 2

```text
TUESDAY
```

### 示例 3

```text
WEDNESDAY
```

### 示例 4

```text
THURSDAY
```

### 示例 5

```text
FRIDAY
```

### 示例 6

```text
SATURDAY
```

### 示例 7

```text
SUNDAY
```

### 示例 8

```json
{"drop_off_point_id": 0,"province_uuid": "string","warehouse_id": 0}
```

### 示例 9

```json
{"calendar": [{"calendar_item": {"break_hours": {"timeslot_end": "string","timeslot_start": "string"},"is_holiday": true,"opening_hours": {"timeslot_end": "string","timeslot_start": "string"}},"day_of_week": "DAY_OF_WEEK_UNSPECIFIED"}]}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

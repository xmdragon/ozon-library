# 获取交货时间段列表

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/fbp/order/direct/timeslot/list`
- Operation ID：`FbpAPI_FbpAvailableTimeslotList`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/FbpAPI_FbpAvailableTimeslotList
- 分组：`fbp`

## 页面标题结构

- 获取交货时间段列表
- Request Body schema: application/json
- 回复
- Response Schema: application/json
- 请求范例
- 回复范例

## 参数与返回结构

### 表格 0

| 字段 | 类型/说明 |
| --- | --- |
| `interval_end` required | string <date-time> 可用时间段所需区间的结束日期。 |
| `interval_start` required | string <date-time> 可用时间段所需区间的开始日期。 |
| `supply_id` required | string 交货标识符。 |

### 表格 1

| 字段 | 类型/说明 |
| --- | --- |
| `reasons` | Array of stringsItems Enum: "EMPTY_TIMESLOTS_REASON_UNSPECIFIED" "LOGISTICS_UNKNOWN" "NO_ROUTE" "NO_ROUTE_SCHEDULES" "NO_LOGISTICS_CAPACITY" "SCHEDULE_UNKNOWN" "NOT_ENOUGH_CAPACITY" "NOT_ENOUGH_TRUCKS" "LIMITS_NOT_AVAILABLE" "CROSS_DOCK_RESERVE_MISSING" "SCHEDULE_RESERVE_MISSING" 缺少时间段的原因： EMPTY_TIMESLOTS_REASON_UNSPECIFIED——未定义； LOGISTICS_UNKNOWN——物流方未知错误； NO_ROUTE——没有路线； NO_ROUTE_SCHEDULES——路线上没有排期； NO_LOGISTICS_CAPACITY——路线上可用的时段不足； SCHEDULE_UNKNOWN——排期方未知错误； NOT_ENOUGH_CAPACITY——仓库可用时段不足； NOT_ENOUGH_TRUCKS——车辆车位不足； LIMITS_NOT_AVAILABLE——仓库未设置限制； CROSS_DOCK_RESERVE_MISSING——仓库未预留越库配送容量； SCHEDULE_RESERVE_MISSING——缺少必要的排期预留。 |
| `timeslots` | Array of objects 可用时间段列表。 |
| `warehouse_timezone_name` | string 卖家仓库的时区。 |

## 示例

### 示例 0

```text
EMPTY_TIMESLOTS_REASON_UNSPECIFIED
```

### 示例 1

```text
LOGISTICS_UNKNOWN
```

### 示例 2

```text
NO_ROUTE
```

### 示例 3

```text
NO_ROUTE_SCHEDULES
```

### 示例 4

```text
NO_LOGISTICS_CAPACITY
```

### 示例 5

```text
SCHEDULE_UNKNOWN
```

### 示例 6

```text
NOT_ENOUGH_CAPACITY
```

### 示例 7

```text
NOT_ENOUGH_TRUCKS
```

### 示例 8

```text
LIMITS_NOT_AVAILABLE
```

### 示例 9

```text
CROSS_DOCK_RESERVE_MISSING
```

### 示例 10

```text
SCHEDULE_RESERVE_MISSING
```

### 示例 11

```json
{"interval_end": "2019-08-24T14:15:22Z","interval_start": "2019-08-24T14:15:22Z","supply_id": "string"}
```

### 示例 12

```json
{"reasons": ["EMPTY_TIMESLOTS_REASON_UNSPECIFIED"],"timeslots": [{"timeslot_end": "2019-08-24T14:15:22Z","timeslot_start": "2019-08-24T14:15:22Z"}],"warehouse_timezone_name": "string"}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

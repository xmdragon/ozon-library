# 创建仓库

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/warehouse/fbs/create`
- Operation ID：`WarehouseAPI_CreateWarehouseFBS`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/WarehouseAPI_CreateWarehouseFBS
- 分组：`warehouse`

## 页面标题结构

- 创建仓库
- Request Body schema: application/json
- 回复
- Response Schema: application/json
- 请求范例
- 回复范例

## 参数与返回结构

### 表格 0

| 字段 | 类型/说明 |
| --- | --- |
| `address_coordinates` required | object 仓库地址坐标。 |
| `cut_in_time` required | integer <int64> 接单时间（分钟）。例如，如果传入 3000，则接单将在传入后50小时内结束。 |
| `drop_off_point_id` | integer <int64> 揽收点标识符。 |
| `first_mile_type` required | string Enum: "PICK_UP" "DROP_OFF" 头程物流类型： PICK_UP — 订单交给快递员； DROP_OFF — 订单送到接收点。 |
| `is_kgt` required | boolean true表示商品为超大。 |
| `name` required | string 仓库名称。 |
| `options` | object 仓库参数。 |
| `phone` required | string 仓库联系电话。请按格式填写：+7 (XXX) XXX-XX-XX。 |
| `timeslot_id` required | integer <int64> 时间段标识符。 |
| `working_days` | Array of strings <= 7 items Items Enum: "MONDAY" "TUESDAY" "WEDNESDAY" "THURSDAY" "FRIDAY" "SATURDAY" "SUNDAY" 仓库工作日： MONDAY — 星期一， TUESDAY — 星期二， WEDNESDAY — 星期三， THURSDAY — 星期四， FRIDAY — 星期五， SATURDAY — 星期六， SUNDAY — 星期天。 |

### 表格 1

| 字段 | 类型/说明 |
| --- | --- |
| `operation_id` | string 创建FBS仓库的操作标识符。要获取操作状态，请使用方法 /v1/warehouse/operation/status。 |

## 示例

### 示例 0

```text
3000
```

### 示例 1

```text
PICK_UP
```

### 示例 2

```text
DROP_OFF
```

### 示例 3

```text
true
```

### 示例 4

```text
MONDAY
```

### 示例 5

```text
TUESDAY
```

### 示例 6

```text
WEDNESDAY
```

### 示例 7

```text
THURSDAY
```

### 示例 8

```text
FRIDAY
```

### 示例 9

```text
SATURDAY
```

### 示例 10

```text
SUNDAY
```

### 示例 11

```json
{
  "address_coordinates": {
    "latitude": 55.69626,
    "longitude": 37.42686
  },
  "first_mile_type": "DROP_OFF",
  "drop_off_point_id": 1020002487458000,
  "cut_in_time": 0,
  "timeslot_id": 0,
  "is_kgt": false,
  "name": "Warehouse",
  "options": {
    "comment": "Comment",
    "courier_phones": [
      "+7(999)999-99-99"
    ],
    "is_auto_assembly": true,
    "is_waybill_enabled": true
  },
  "phone": "+7(999)999-99-99",
  "working_days": [
    "MONDAY",
    "TUESDAY",
    "WEDNESDAY",
    "THURSDAY",
    "FRIDAY"
  ]
}
```

### 示例 12

```json
{
  "operation_id": "a0cfefee-9a5a-4580-bc32-2f9a6c7973e3"
}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

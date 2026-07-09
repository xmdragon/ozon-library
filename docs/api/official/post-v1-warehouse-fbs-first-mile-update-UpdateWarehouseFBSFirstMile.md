# 更新头程物流

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/warehouse/fbs/first-mile/update`
- Operation ID：`UpdateWarehouseFBSFirstMile`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/UpdateWarehouseFBSFirstMile
- 分组：`warehouse`

## 页面标题结构

- 更新头程物流
- header Parameters
- Request Body schema: application/json
- 回复
- Response Schema: application/jsonapplication/jsonexample
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
| `cut_in_time` required | integer <int64> 接单时间（分钟）。例如，如果传入 3000，则接单将在传入后50小时内结束。 |
| `drop_off_point_id` | integer <int64> 订单发运点ID。如果first_mile_type = DROP_OFF，该参数必填。 |
| `first_mile_type` required | string Enum: "PICK_UP" "DROP_OFF" 第一英里类型： PICK_UP —发运给快递员； DROP_OFF —发运至接收点。 |
| `timeslot_id` required | integer <int64> 时间段标识符。 |
| `warehouse_id` required | integer <int64> 仓库ID。 |

### 表格 2

| 字段 | 类型/说明 |
| --- | --- |
| `operation_id` | string 操作ID。通过方法 /v1/warehouse/operation/status 获取操作状态。 |

## 示例

### 示例 0

```text
3000
```

### 示例 1

```text
first_mile_type = DROP_OFF
```

### 示例 2

```text
PICK_UP
```

### 示例 3

```text
DROP_OFF
```

### 示例 4

```json
{
  "first_mile_type": "DROP_OFF",
  "drop_off_point_id": 0,
  "cut_in_time": 0,
  "timeslot_id": 0,
  "warehouse_id": 0
}
```

### 示例 5

```json
{
  "operation_id": "string"
}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

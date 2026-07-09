# 编辑交货申请中的时间段

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/fbp/order/direct/timeslot/edit`
- Operation ID：`FbpAPI_FbpEditTimeslot`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/FbpAPI_FbpEditTimeslot
- 分组：`fbp`

## 页面标题结构

- 编辑交货申请中的时间段
- Request Body schema: application/json
- 回复
- Response Schema: application/json
- 请求范例
- 回复范例

## 参数与返回结构

### 表格 0

| 字段 | 类型/说明 |
| --- | --- |
| `row_version` required | integer <int64> 草稿的当前版本标识符。 |
| `supply_id` required | string 供货申请标识符。 |
| `timeslot_start` required | string <date-time> 时间段开始时间。 |

### 表格 1

| 字段 | 类型/说明 |
| --- | --- |
| `error_reasons` | Array of stringsItems Enum: "RESERVE_FAILURE_TYPE_UNSPECIFIED" "REQUEST_VALIDATION" "INVALID_RESERVE" "LOGISTICS_REASON" "SCHEDULE_REASON" 错误原因： RESERVE_FAILURE_TYPE_UNSPECIFIED——未定义； REQUEST_VALIDATION——请求中填写了过去的预定日期； INVALID_RESERVE——原始预留未找到、已失效或已包含申请，但尝试覆盖； LOGISTICS_REASON——物流方错误； SCHEDULE_REASON——排期方错误； NO_CAPACITY——无可用预定时段。 |
| `row_version` | integer <int64> 草稿的当前版本标识符。 |

## 示例

### 示例 0

```text
RESERVE_FAILURE_TYPE_UNSPECIFIED
```

### 示例 1

```text
REQUEST_VALIDATION
```

### 示例 2

```text
INVALID_RESERVE
```

### 示例 3

```text
LOGISTICS_REASON
```

### 示例 4

```text
SCHEDULE_REASON
```

### 示例 5

```text
NO_CAPACITY
```

### 示例 6

```json
{
  "row_version": 0,
  "supply_id": "string",
  "timeslot_start": "2019-08-24T14:15:22Z"
}
```

### 示例 7

```json
{
  "error_reasons": [
    "RESERVE_FAILURE_TYPE_UNSPECIFIED"
  ],
  "row_version": 0
}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

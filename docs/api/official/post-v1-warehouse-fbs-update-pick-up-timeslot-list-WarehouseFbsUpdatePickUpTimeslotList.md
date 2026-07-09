# 获取用于更新pick-up发运仓库的时间段列表

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/warehouse/fbs/update/pick-up/timeslot/list`
- Operation ID：`WarehouseFbsUpdatePickUpTimeslotList`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/WarehouseFbsUpdatePickUpTimeslotList
- 分组：`warehouse`

## 页面标题结构

- 获取用于更新pick-up发运仓库的时间段列表
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
| `warehouse_id` required | integer <int64> 仓库标识符。 |

### 表格 2

| 字段 | 类型/说明 |
| --- | --- |
| `timeslots` | Array of objects 时间段列表。 |
| `from` | string 时间段开始时间。 |
| `id` | integer <int64> 时间段标识符。 |
| `to` | string 时间段结束时间。 |

### 表格 3

| 字段 | 类型/说明 |
| --- | --- |
| `from` | string 时间段开始时间。 |
| `id` | integer <int64> 时间段标识符。 |
| `to` | string 时间段结束时间。 |

## 示例

### 示例 0

```json
{"warehouse_id": 987654321}
```

### 示例 1

```json
{"timeslots": [{"id": 1001,"from": "00:00","to": "00:00"},{"id": 1002,"from": "00:00","to": "00:00"}]}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

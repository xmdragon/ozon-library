# 通行证列表

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/pass/list`
- Operation ID：`PassList`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/PassList
- 分组：`pass`

## 页面标题结构

- 通行证列表
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
| `cursor` | string 用于获取下一批数据的指针。 |
| `filter` | object 筛选器。 |
| `limit` required | integer <int32> [ 1 .. 1000 ] Default: 1000 响应中记录数量的限制。 |

### 表格 2

| 字段 | 类型/说明 |
| --- | --- |
| `arrival_passes` | Array of objects 运输通行证列表。 |
| `cursor` | string 用于获取下一批数据的指针。 如果此参数为空，则没有更多数据。 |

## 示例

### 示例 0

```json
{"cursor": "","filter": {"arrival_pass_ids": ["5000123456","5000123457"],"arrival_reason": "FBS_DELIVERY","dropoff_point_ids": ["7000123456","7000123457"],"only_active_passes": true,"warehouse_ids": ["3000007863","3000007864"]},"limit": 1000}
```

### 示例 1

```json
{"arrival_passes": [{"arrival_pass_id": 5000123456,"arrival_reasons": ["FBS_DELIVERY","FBS_RETURN"],"arrival_time": "2026-03-16T10:00:00Z","driver_name": "string","driver_phone": "+79991234567","dropoff_point_id": 7000123456,"is_active": true,"vehicle_license_plate": "string","vehicle_model": "string","warehouse_id": 3000007863},{"arrival_pass_id": 5000123457,"arrival_reasons": ["FBS_RETURN"],"arrival_time": "2026-03-16T14:30:00Z","driver_name": "string","driver_phone": "+79997654321","dropoff_point_id": 7000123457,"is_active": true,"vehicle_license_plate": "string","vehicle_model": "Ford Transit","warehouse_id": 3000007864}],"cursor": "next-page-cursor-12345"}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

# 获取用于创建pick-up发运仓库的时间段列表

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/warehouse/fbs/create/pick-up/timeslot/list`
- Operation ID：`WarehouseFbsCreatePickUpTimeslotList`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/#operation/WarehouseFbsCreatePickUpTimeslotList
- 分组：`warehouse`

## News 更新标记

| 日期 | 标记 | 摘要 | 来源 |
| --- | --- | --- | --- |
| 2026-02-02 | `graduated` | /v1/warehouse/fbs/create/pick-up/timeslot/list 已将该方法从Beta版迁移至正式版。 | [官方 News](https://docs.ozon.ru/api/seller/zh/#section/202622) |
| 2025-10-17 | `new_method` | /v1/warehouse/fbs/create/pick-up/timeslot/list 新增了与时间段相关的Beta方法。 | [官方 News](https://docs.ozon.ru/api/seller/zh/#section/20251017) |

## 页面标题结构

- 获取用于创建pick-up发运仓库的时间段列表
- HEADER PARAMETERS
- REQUEST BODY SCHEMA: application/json
- 回复
- RESPONSE SCHEMA: application/json
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
| `address_coordinates` required | object 仓库坐标。 |
| `is_kgt` required | boolean 超大货物标志。 |

### 表格 2

| 字段 | 类型/说明 |
| --- | --- |
| `is_pickup_supported` | boolean 支持pick-up发运标志。 |
| `timeslots` | Array of objects 时间段列表。 |

## 示例

### 示例 0

```json
{
  "is_kgt": true,
  "address_coordinates": {
    "latitude": 55.7558,
    "longitude": 37.6173
  }
}
```

### 示例 1

```json
{
  "is_pickup_supported": true,
  "timeslots": [
    {
      "id": 123456789,
      "from": "00:00",
      "to": "00:00"
    },
    {
      "id": 987654321,
      "from": "00:00",
      "to": "00:00"
    }
  ]
}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

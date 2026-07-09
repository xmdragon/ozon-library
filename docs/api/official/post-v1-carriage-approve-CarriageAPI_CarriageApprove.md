# 发运确认

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/carriage/approve`
- Operation ID：`CarriageAPI_CarriageApprove`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/CarriageAPI_CarriageApprove
- 分组：`carriage`

## News 更新标记

| 日期 | 标记 | 摘要 | 来源 |
| --- | --- | --- | --- |
| 2026-06-03 | `new_method` | /v1/carriage/approve 新增了用于确认发运的方法。 | [官方 News](https://docs.ozon.ru/api/seller/zh/#section/202663) |

## 页面标题结构

- 发运确认
- header Parameters
- Request Body schema: application/json
- 回复
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
| `carriage_id` required | integer <int64> 发运标识符。 |
| `containers_count` | integer <int32> 货位数量。 如果您已开通信任验收，并按货位发运订单，请使用该参数。如果您未开通信任验收，请跳过该参数。 |

## 示例

### 示例 0

```json
{
  "carriage_id": 0,
  "containers_count": 0
}
```

### 示例 1

```json
{
  "code": 0,
  "details": [
    {
      "typeUrl": "string",
      "value": "string"
    }
  ],
  "message": "string"
}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

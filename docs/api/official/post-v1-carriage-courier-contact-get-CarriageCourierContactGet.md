# 获取向快递员提供的卖家联系方式

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/carriage/courier-contact/get`
- Operation ID：`CarriageCourierContactGet`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/#operation/CarriageCourierContactGet
- 分组：`carriage`

## News 更新标记

| 日期 | 标记 | 摘要 | 来源 |
| --- | --- | --- | --- |
| 2026-08-14 | `new_method` | /v1/carriage/courier-contact/get 新增了用于处理向快递员提供的卖家联系方式的方法。 | [官方 News](https://docs.ozon.ru/api/seller/zh/#section/2026814) |

## 页面标题结构

- 获取向快递员提供的卖家联系方式
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
| `carriage_id` required | integer <int64> 运输标识符。 |

### 表格 2

| 字段 | 类型/说明 |
| --- | --- |
| `contact` | Array of objects 卖家联系方式信息。 |

### 表格 3

| 字段 | 类型/说明 |
| --- | --- |
| `carriage_id` | integer <int64> 运输标识符。 |
| `phone` | string 卖家的电话号码。 |
| `wechat_nickname` | string 卖家的微信号。 |
| `comment` | string 给快递员的备注。 |
| `updated_at` | string <date-time> 记录最后更新的日期和时间（UTC格式）。 |

## 示例

### 示例 0

```json
{
  "carriage_id": 5435123
}
```

### 示例 1

```json
{
  "contact": [
    {
      "carriage_id": 5435123,
      "phone": "+86(123)4567-8901",
      "wechat_nickname": "string",
      "comment": "string",
      "updated_at": "2026-07-29T10:38:26.004Z"
    }
  ]
}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

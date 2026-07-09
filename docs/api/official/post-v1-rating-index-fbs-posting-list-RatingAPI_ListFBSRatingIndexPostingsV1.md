# 影响错误指数的货件列表：FBS 和 rFBS

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/rating/index/fbs/posting/list`
- Operation ID：`RatingAPI_ListFBSRatingIndexPostingsV1`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/RatingAPI_ListFBSRatingIndexPostingsV1
- 分组：`rating`

## News 更新标记

| 日期 | 标记 | 摘要 | 来源 |
| --- | --- | --- | --- |
| 2025-11-20 | `new_method` | /v1/rating/index/fbs/posting/list 新增了用于处理错误指数的测试版方法：FBS 和 rFBS。 | [官方 News](https://docs.ozon.ru/api/seller/zh/#section/20251120) |

## 页面标题结构

- 影响错误指数的货件列表：FBS 和 rFBS
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
| `filter` required | object 筛选器。 |
| `limit` required | integer <int64> <= 1000 返回结果中的数值数量。 |

### 表格 2

| 字段 | 类型/说明 |
| --- | --- |
| `cursor` | string 用于获取下一批数据的指针。 |
| `errors` | Array of objects 影响错误指数的货件。 |
| `has_next` | boolean true，表示查询结果未包含所有货件。 |

## 示例

### 示例 0

```text
true
```

### 示例 1

```json
{
  "cursor": "string",
  "filter": {
    "date_from": "2019-08-24T14:15:22Z",
    "date_to": "2019-08-24T14:15:22Z",
    "posting_numbers": [
      "string"
    ]
  },
  "limit": 0
}
```

### 示例 2

```json
{
  "cursor": "string",
  "errors": [
    {
      "charge_percent": 0,
      "charge_price": 0,
      "charge_price_currency_code": "string",
      "delivery_schema": "string",
      "error_at": "2019-08-24T14:15:22Z",
      "has_grace_status": true,
      "index": 0,
      "posting_error_type": "UNSPECIFIED",
      "posting_number": "string",
      "product_price": 0,
      "product_price_currency_code": "string"
    }
  ],
  "has_next": true
}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

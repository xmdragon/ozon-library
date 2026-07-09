# 获取评价列表

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v2/review/list`
- Operation ID：`ReviewListV2`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/ReviewListV2
- 分组：`review`

## 页面标题结构

- 获取评价列表
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
| `filters` | object 用于搜索评价的筛选条件。 |
| `last_id` | string 响应中最后一条评价的标识符。 |
| `limit` required | integer <int32> [ 20 .. 100 ] 响应中的评价数量。 |
| `sort_dir` | string Enum: "ASC" "DESC" 排序方向： ASC——升序； DESC——降序。 |

### 表格 2

| 字段 | 类型/说明 |
| --- | --- |
| `has_next` | boolean true，表示响应中未返回全部评价。 |
| `last_id` | string 页面中最后一个评价的标识符。 |
| `reviews` | Array of objects 评价列表。 |

## 示例

### 示例 0

```text
ASC
```

### 示例 1

```text
DESC
```

### 示例 2

```text
true
```

### 示例 3

```json
{
  "filters": {
    "sku": [
      0
    ],
    "order_status": "NEW",
    "status": "DELIVERED",
    "published_from": "2026-03-10T14:08:00.257Z",
    "published_to": "2026-03-10T14:08:00.257Z"
  },
  "last_id": "string",
  "limit": 0,
  "sort_dir": "ASC"
}
```

### 示例 4

```json
{
  "reviews": [
    {
      "id": "017c0d1c-66d3-b838-3d29-cf9b95a6ac48",
      "sku": "148591503",
      "text": "string",
      "published_at": "2024-10-10T07:23:55.970Z",
      "rating": 2,
      "status": "UNPROCESSED",
      "comments_amount": 0,
      "photos_amount": 0,
      "videos_amount": 0,
      "order_status": "DELIVERED",
      "is_rating_participant": true
    }
  ],
  "has_next": true,
  "last_id": "017c0d53-a7c8-81ef-53de-7d32fcbd7421"
}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

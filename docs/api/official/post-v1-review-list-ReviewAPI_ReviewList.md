# 获取评价列表 Deprecated

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/review/list`
- Operation ID：`ReviewAPI_ReviewList`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/ReviewAPI_ReviewList
- 分组：`review`

## 页面标题结构

- 获取评价列表 Deprecated
- Request Body schema: application/json
- 回复
- Response Schema: application/json
- 请求范例
- 回复范例

## 参数与返回结构

### 表格 0

| 字段 | 类型/说明 |
| --- | --- |
| `last_id` | string 页面中最后一个评价的标识符。 |
| `limit` required | integer <int32> 限制回复中的值数量。最少 — 20；最多 — 100。 |
| `sort_dir` | string 排序方向： ASC — 按升序。 DESC — 按降序。 |
| `status` | string 评价状态： ALL — 全部， UNPROCESSED — 未处理的， PROCESSED — 已处理的。 |

### 表格 1

| 字段 | 类型/说明 |
| --- | --- |
| `has_next` | boolean true：回复中未返回所有评价。 |
| `last_id` | string 页面中最后一个评价的标识符。 |
| `reviews` | Array of objects 评价信息。 |

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
ALL
```

### 示例 3

```text
UNPROCESSED
```

### 示例 4

```text
PROCESSED
```

### 示例 5

```text
true
```

### 示例 6

```json
{
  "last_id": "",
  "limit": 100,
  "sort_dir": "ASC",
  "status": "ALL"
}
```

### 示例 7

```json
{
  "has_next": true,
  "last_id": "string",
  "reviews": [
    {
      "comments_amount": 0,
      "id": "string",
      "is_rating_participant": true,
      "order_status": "string",
      "photos_amount": 0,
      "published_at": "2019-08-24T14:15:22Z",
      "rating": 0,
      "sku": 0,
      "status": "string",
      "text": "string",
      "videos_amount": 0
    }
  ]
}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

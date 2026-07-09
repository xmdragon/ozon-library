# 评价的评论列表

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/review/comment/list`
- Operation ID：`ReviewAPI_CommentList`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/ReviewAPI_CommentList
- 分组：`review`

## 页面标题结构

- 评价的评论列表
- Request Body schema: application/json
- 回复
- Response Schema: application/json
- 请求范例
- 回复范例

## 参数与返回结构

### 表格 0

| 字段 | 类型/说明 |
| --- | --- |
| `limit` required | integer <int32> 限制回复中的值数量。 最少 — 20；最多 — 100。 |
| `offset` | integer <int32> 从列表开头跳过的元素数量：例如，如果 offset = 10，那么回复将从找到的第11个元素开始。 |
| `review_id` required | string 评价标识符。 |
| `sort_dir` | string Default: "ASC" Enum: "ASC" "DESC" 排序方向： ASC — 按升序。 DESC — 按降序。 |

### 表格 1

| 字段 | 类型/说明 |
| --- | --- |
| `comments` | Array of objects 评论信息。 |
| `offset` | integer <int32> 搜索结果中的元素数量。 |

## 示例

### 示例 0

```text
offset = 10
```

### 示例 1

```text
ASC
```

### 示例 2

```text
DESC
```

### 示例 3

```json
{
  "limit": 100,
  "offset": 0,
  "review_id": "0187310a-97d9-dfcf-3039-82d809f0e233",
  "sort_dir": "ASC"
}
```

### 示例 4

```json
{
  "comments": [
    {
      "id": "string",
      "is_official": true,
      "is_owner": true,
      "parent_comment_id": "string",
      "published_at": "2019-08-24T14:15:22Z",
      "text": "string"
    }
  ],
  "offset": 0
}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

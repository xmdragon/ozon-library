# 对评价留下评论

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/review/comment/create`
- Operation ID：`ReviewAPI_CommentCreate`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/ReviewAPI_CommentCreate
- 分组：`review`

## 页面标题结构

- 对评价留下评论
- Request Body schema: application/json
- 回复
- Response Schema: application/json
- 请求范例
- 回复范例

## 参数与返回结构

### 表格 0

| 字段 | 类型/说明 |
| --- | --- |
| `mark_review_as_processed` | boolean 更新评论状态： true — 状态将变更为 Processed（已处理）； false — 状态不变。 |
| `parent_comment_id` | string 父级评论的标识符（您要回复的评论）。 |
| `review_id` required | string 评价标识符。 |
| `text` required | string 评论内容。 |

### 表格 1

| 字段 | 类型/说明 |
| --- | --- |
| `comment_id` | string 评论标识符。 |

## 示例

### 示例 0

```text
true
```

### 示例 1

```text
Processed
```

### 示例 2

```text
false
```

### 示例 3

```json
{
  "mark_review_as_processed": true,
  "parent_comment_id": "string",
  "review_id": "string",
  "text": "string"
}
```

### 示例 4

```json
{
  "comment_id": "string"
}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

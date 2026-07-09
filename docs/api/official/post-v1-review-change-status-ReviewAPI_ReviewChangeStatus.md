# 更改评价状态

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/review/change-status`
- Operation ID：`ReviewAPI_ReviewChangeStatus`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/ReviewAPI_ReviewChangeStatus
- 分组：`review`

## 页面标题结构

- 更改评价状态
- Request Body schema: application/json
- 回复
- Response Schema: application/json
- 请求范例
- 回复范例

## 参数与返回结构

### 表格 0

| 字段 | 类型/说明 |
| --- | --- |
| `review_ids` required | Array of strings 包含评价标识符的数组（数量在1到100之间）。 |
| `status` required | string 评价状态： PROCESSED — 已处理。 UNPROCESSED — 未处理。 |

## 示例

### 示例 0

```text
PROCESSED
```

### 示例 1

```text
UNPROCESSED
```

### 示例 2

```json
{
  "review_ids": [
    "string"
  ],
  "status": "string"
}
```

### 示例 3

```json
{}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

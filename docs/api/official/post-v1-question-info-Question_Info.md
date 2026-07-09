# 问题详情

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/question/info`
- Operation ID：`Question_Info`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/Question_Info
- 分组：`question`

## 页面标题结构

- 问题详情
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
| `question_id` required | string 问题标识符。 |

### 表格 2

| 字段 | 类型/说明 |
| --- | --- |
| `answers_count` | integer <int64> 问题的回答数量。 |
| `author_name` | string 问题作者。 |
| `id` | string 问题标识符。 |
| `product_url` | string 商品链接。 |
| `published_at` | timestamp 问题发布日期。 |
| `question_link` | string 问题链接。 |
| `sku` | integer <int64> Ozon 系统中的商品标识符——SKU。 |
| `status` | enum 问题状态： NEW——新的， ALL——全部问题， VIEWED——已查看， PROCESSED——已处理， UNPROCESSED——未处理。 |
| `text` | string 问题文本。 |

## 示例

### 示例 0

```text
NEW
```

### 示例 1

```text
ALL
```

### 示例 2

```text
VIEWED
```

### 示例 3

```text
PROCESSED
```

### 示例 4

```text
UNPROCESSED
```

### 示例 5

```json
{
  "question_id": "string"
}
```

### 示例 6

```json
{
  "answers_count": "0",
  "author_name": "string",
  "product_url": "https://www.ozon.ru/product/149829950/",
  "sku": 646399170,
  "id": "0192a009-769f-7ee9-b412-893045171a66",
  "text": "string",
  "question_link": "https://www.ozon.ru/product/149829950/questions/?qid=290125772&utm_campaign=reviews_sc_link&utm_medium=share_button&utm_source=smm",
  "published_at": "2024-10-08T10:09:29.099284Z",
  "status": "VIEWED"
}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

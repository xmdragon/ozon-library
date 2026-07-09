# 取消货运

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v2/posting/fbs/cancel`
- Operation ID：`PostingAPI_CancelFbsPosting`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/PostingAPI_CancelFbsPosting
- 分组：`posting`

## 页面标题结构

- 取消货运
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
| `cancel_reason_id` required | integer <int64> 取消运输的原因ID。 |
| `cancel_reason_message` | string 关于取消的附加信息。如果cancel_reason_id = 402，参数是必须的。 |
| `posting_number` required | string 货件ID。 |

### 表格 2

| 字段 | 类型/说明 |
| --- | --- |
| `result` | boolean 处理请求的结果。 如果请求执行时无误，则为“true”。 |

## 示例

### 示例 0

```text
cancelled
```

### 示例 1

```text
cancel_reason_id
```

### 示例 2

```text
352
```

### 示例 3

```text
400
```

### 示例 4

```text
401
```

### 示例 5

```text
402
```

### 示例 6

```text
665
```

### 示例 7

```text
666
```

### 示例 8

```text
667
```

### 示例 9

```text
cancel_reason_id = 402
```

### 示例 10

```json
{
  "cancel_reason_id": 352,
  "cancel_reason_message": "Product is out of stock",
  "posting_number": "33920113-1231-1"
}
```

### 示例 11

```json
{
  "result": true
}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

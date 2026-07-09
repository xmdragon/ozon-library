# 创建对问题的回答

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/question/answer/create`
- Operation ID：`QuestionAnswer_Create`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/QuestionAnswer_Create
- 分组：`question`

## 页面标题结构

- 创建对问题的回答
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
| `sku` required | integer <int64> Ozon 系统中的商品标识符——SKU。 |
| `text` required | string 回答文本，长度为 2 至 3000 个字符。 |

### 表格 2

| 字段 | 类型/说明 |
| --- | --- |
| `answer_id` | string 问题回答标识符。 |

## 示例

### 示例 0

```json
{"question_id": "string","sku": 0,"text": "string"}
```

### 示例 1

```json
{"answer_id": "0192e7ce-e12c-7a74-afc7-26e877799204"}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

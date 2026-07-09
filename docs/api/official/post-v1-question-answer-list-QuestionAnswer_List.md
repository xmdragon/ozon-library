# 问题回答列表

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/question/answer/list`
- Operation ID：`QuestionAnswer_List`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/QuestionAnswer_List
- 分组：`question`

## 页面标题结构

- 问题回答列表
- header Parameters
- Request Body schema: application/json
- 回复
- Response Schema: application/json
- 请求范例
- 回复范例

## 参数与返回结构

### 表格 0

Client-Id required string 用户识别号。 Api-Key required string API-密钥。

### 表格 1

last_id 页面上最后一个值的标识符。 如果是首次请求，请将该字段留空。 后续请求中，请传入上一次请求返回的 last_id。 question_id required string 问题标识符。 sku required integer <int64> Ozon 系统中的商品标识符——SKU。

### 表格 2

answersArray of objects 回答。 last_idstring 页面上最后一个值的标识符。 要获取下一个批次的数据，请在下一个请求的 last_id 参数中传递上次获取的值。

## 示例

### 示例 0

```json
{"last_id": "","question_id": "019228a7-91d8-76af-a73a-e989dfac7ac8","sku": 646399170}
```

### 示例 1

```json
{"answers": [{"author_name": "string","id": "string","published_at": "2024-08-14T11:44:35.352Z","question_id": "string","sku": 646399170,"status_publication": "","text": "string"}],"last_id": "string"}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

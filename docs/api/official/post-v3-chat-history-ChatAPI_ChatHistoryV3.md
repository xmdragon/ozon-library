# 聊天历史记录

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v3/chat/history`
- Operation ID：`ChatAPI_ChatHistoryV3`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/ChatAPI_ChatHistoryV3
- 分组：`chat`

## 页面标题结构

- 聊天历史记录
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
| `chat_id` required | string 聊天识别码。 |
| `direction` | string 信息排序方向： Forward — 从旧到新。 Backward — 从新到旧。 默认值是 — Backward。消息的数量可以在 limit参数中设置。 |
| `filter` | object 消息过滤器。 |
| `from_message_id` | integer <uint64> 从该信息开始整理聊天记录的消息识别码。默认为从最后一条可见信息。 当 direction = Forward 时，from_message_id 参数为必填。 |
| `limit` | integer <int64> 答复的信息数量。默认设置为50。最大值是1000。 |

### 表格 2

| 字段 | 类型/说明 |
| --- | --- |
| `has_next` | boolean 表示不是所有信息都在答复中返回。 |
| `messages` | Array of objects 根据请求正文中的direction参数排序的信息数组。 |

## 示例

### 示例 0

```text
Forward
```

### 示例 1

```text
Backward
```

### 示例 2

```text
Backward
```

### 示例 3

```text
limit
```

### 示例 4

```text
direction = Forward
```

### 示例 5

```text
from_message_id
```

### 示例 6

```text
direction
```

### 示例 7

```json
{"chat_id": "18b8e1f9-4ae7-461c-84ea-8e1f54d1a45e","direction": "Forward","filter": {"message_ids": ["3000000300211559667"]},"from_message_id": 3000000000118032000,"limit": 1}
```

### 示例 8

```json
{"has_next": true,"messages": [{"context": {"order_number": "123456789","sku": "987654321"},"created_at": "2019-08-24T14:15:22Z","data": ["Здравствуйте, у меня вопрос по вашему товару \"Стекло защитное для смартфонов\", артикул 11223. Подойдет ли он на данную [ модель ](https://www.ozon.ru/product/smartfon-samsung-galaxy-a03s-4-64-gb-chernyy) телефона?"],"is_image": true,"is_read": true,"message_id": "3000000000817031942","moderate_image_status": "SUCCESS","user": {"id": "115568","type": "Сustomer"}}]}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

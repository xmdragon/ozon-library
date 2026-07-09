# 将信息标记为已读

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v2/chat/read`
- Operation ID：`ChatAPI_ChatReadV2`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/ChatAPI_ChatReadV2
- 分组：`chat`

## 页面标题结构

- 将信息标记为已读
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
| `from_message_id` | integer <uint64> 信息识别码。 |

### 表格 2

| 字段 | 类型/说明 |
| --- | --- |
| `unread_count` | integer <int64> 聊天中未读消息的数量。 |

## 示例

### 示例 0

```json
{
  "chat_id": "99feb3fc-a474-469f-95d5-268b470cc607",
  "from_message_id": 3000000000118032000
}
```

### 示例 1

```json
{
  "unread_count": 0
}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

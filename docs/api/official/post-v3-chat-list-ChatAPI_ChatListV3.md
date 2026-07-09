# 聊天清单

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v3/chat/list`
- Operation ID：`ChatAPI_ChatListV3`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/ChatAPI_ChatListV3
- 分组：`chat`

## News 更新标记

| 日期 | 标记 | 摘要 | 来源 |
| --- | --- | --- | --- |
| 2026-06-30 | `updated` | /v3/chat/list 更新了方法响应中chats.chat.chat_type参数的描述。 | [官方 News](https://docs.ozon.ru/api/seller/zh/#section/2026630) |
| 2026-05-05 | `updated` | /v3/chat/list 更新了方法响应中参数chats.chat.chat_type的说明。 | [官方 News](https://docs.ozon.ru/api/seller/zh/#section/202655) |
| 2026-03-19 | `updated` | /v3/chat/list 更新了方法响应中 chats.chat.chat_type 参数的描。 | [官方 News](https://docs.ozon.ru/api/seller/zh/#section/2026319) |
| 2026-03-11 | `updated` | /v3/chat/list 更新了方法响应中的 chats.chat.chat_type 参数描述。 | [官方 News](https://docs.ozon.ru/api/seller/zh/#section/2026311) |
| 2025-10-16 | `updated` | /v3/chat/list 更新了该方法请求中参数 limit 的描述。 | [官方 News](https://docs.ozon.ru/api/seller/zh/#section/20251016) |
| 2025-07-28 | `new_method` | /v3/chat/list 新增了新版本方法，用于通过指定筛选器获取聊天信息。 | [官方 News](https://docs.ozon.ru/api/seller/zh/#section/2025728) |

## 页面标题结构

- 聊天清单
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
| `filter` | object 按聊天过滤。 |
| `limit` required | integer <int64> 回答中值的数量。默认值为30。最大值是100。 |
| `cursor` | string 后续数据的选择标志。 |

### 表格 2

| 字段 | 类型/说明 |
| --- | --- |
| `chats` | Array of objects 聊天数据。 |
| `total_unread_count` | integer <int64> 未读信息总数。 |
| `cursor` | string 后续数据的选择标志。 |
| `has_next` | boolean 表示响应中未包含全部聊天: true — 使用新的 cursor 参数重新发送请求以获取剩余聊天; false — 响应中已包含匹配请求筛选器的所有聊天。 |

## 示例

### 示例 0

```text
true
```

### 示例 1

```text
cursor
```

### 示例 2

```text
false
```

### 示例 3

```json
{
  "filter": {
    "chat_status": "OPENED",
    "unread_only": true
  },
  "limit": 1,
  "cursor": "304000402034"
}
```

### 示例 4

```json
{
  "chats": [
    {
      "chat": {
        "created_at": "2022-07-22T08:07:19.581Z",
        "chat_id": "5e767w03-b400-4y1b-a841-75319ca8a5c8",
        "chat_status": "OPENED",
        "chat_type": "SELLER_SUPPORT"
      },
      "first_unread_message_id": "3000000000118021931",
      "last_message_id": "30000000001280042740",
      "unread_count": 1
    }
  ],
  "total_unread_count": 5,
  "cursor": "30000002342123123",
  "has_next": "true"
}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

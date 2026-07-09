# 货件装运

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v2/posting/fbs/awaiting-delivery`
- Operation ID：`PostingAPI_MoveFbsPostingToAwaitingDelivery`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/PostingAPI_MoveFbsPostingToAwaitingDelivery
- 分组：`posting`

## News 更新标记

| 日期 | 标记 | 摘要 | 来源 |
| --- | --- | --- | --- |
| 2025-02-06 | `updated` | /v2/posting/fbs/awaiting-delivery 更新了该方法请求中参数 posting_number 的描述。 | [官方 News](https://docs.ozon.ru/api/seller/zh/#section/202526) |

## 页面标题结构

- 货件装运
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
| `posting_number` required | Array of strings 货运ID。一次请求中的最大数量——100。 |

### 表格 2

| 字段 | 类型/说明 |
| --- | --- |
| `result` | boolean 处理请求的结果。 如果请求执行时无误，则为“true”。 |

## 示例

### 示例 0

```text
awaiting_deliver
```

### 示例 1

```json
{
  "posting_number": [
    "33920143-1195-1"
  ]
}
```

### 示例 2

```json
{
  "result": true
}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

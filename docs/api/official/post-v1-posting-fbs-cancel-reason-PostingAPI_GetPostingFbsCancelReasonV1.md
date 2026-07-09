# 货运取消原因

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/posting/fbs/cancel-reason`
- Operation ID：`PostingAPI_GetPostingFbsCancelReasonV1`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/PostingAPI_GetPostingFbsCancelReasonV1
- 分组：`posting`

## 页面标题结构

- 货运取消原因
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
| `related_posting_numbers` required | Array of strings 货件号。 |

### 表格 2

| 字段 | 类型/说明 |
| --- | --- |
| `result` | Array of objects 请求结果。 |
| `posting_number` | string 货运号。 |
| `reasons` | Array of objects 取消订单原因。 |

### 表格 3

| 字段 | 类型/说明 |
| --- | --- |
| `posting_number` | string 货运号。 |
| `reasons` | Array of objects 取消订单原因。 |

## 示例

### 示例 0

```json
{"related_posting_numbers": ["73837363-0010-3"]}
```

### 示例 1

```json
{"result": [{"posting_number": "73837363-0010-3","reasons": [{"id": 352,"title": "在卖家仓库中已无商品","type_id": "seller"},{"id": 400,"title": "只剩下有缺陷的商品","type_id": "seller"},{"id": 402,"title": "其他（卖家的其他过错）","type_id": "seller"}]}]}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

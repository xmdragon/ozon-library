# 将订单拆分为不带备货的货件

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/posting/fbs/split`
- Operation ID：`FbsSplit`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/FbsSplit
- 分组：`posting`

## 页面标题结构

- 将订单拆分为不带备货的货件
- Request Body schema: application/json
- 回复
- Response Schema: application/json
- 请求范例
- 回复范例

## 参数与返回结构

### 表格 0

| 字段 | 类型/说明 |
| --- | --- |
| `posting_number` required | string 货件编号。 |
| `postings` required | Array of objects 要拆分订单的货件项列表。每个请求只能拆分一个订单。 |

### 表格 1

| 字段 | 类型/说明 |
| --- | --- |
| `parent_posting` | object 原始货件的信息。 |
| `postings` | Array of objects 订单被拆分后的货件列表。 |

## 示例

### 示例 0

```json
{"posting_number": "string","postings": [{"products": [{"product_id": 0,"quantity": 0}]}]}
```

### 示例 1

```json
{"parent_posting": {"posting_number": "string","products": [{"product_id": 0,"quantity": 0}]},"postings": [{"posting_number": "string","products": [{"product_id": 0,"quantity": 0}]}]}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

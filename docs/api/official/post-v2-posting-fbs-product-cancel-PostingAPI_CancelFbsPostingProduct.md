# 取消某些商品发货

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v2/posting/fbs/product/cancel`
- Operation ID：`PostingAPI_CancelFbsPostingProduct`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/PostingAPI_CancelFbsPostingProduct
- 分组：`posting`

## 页面标题结构

- 取消某些商品发货
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
| `cancel_reason_id` required | integer <int64> 货物取消发货原因ID。 |
| `cancel_reason_message` required | string 必填字段。关于取消的其他信息。 |
| `items` required | Array of objects 商品信息。 |
| `posting_number` required | string 货运ID。 |

### 表格 2

| 字段 | 类型/说明 |
| --- | --- |
| `result` | string 货运号。 |

## 示例

### 示例 0

```text
cancel_reason_id
```

### 示例 1

```json
{"cancel_reason_id": 352,"cancel_reason_message": "Product is out of stock","items": [{"quantity": 5,"sku": 150587396}],"posting_number": "33920113-1231-1"}
```

### 示例 2

```json
{"result": ""}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

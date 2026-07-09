# 获取货件列表

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/posting/fbp/list`
- Operation ID：`PostingFbpList`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/PostingFbpList
- 分组：`posting`

## 页面标题结构

- 获取货件列表
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

cursorstring 用于选择下一批数据的指针。 filterobject 用于搜索货件的筛选器。 limitinteger <int64> [ 1 .. 100 ] 响应中返回的值数量。 sort_bystring 货件排序参数： last_change_status_date——按最后一次状态变更日期排序； in_process_at——按开始处理日期排序。 sort_dirstring Enum: "ASC" "DESC" 排序方向： ASC——升序； DESC——降序。

### 表格 2

cursorstring 用于选择下一批数据的指针。 postingsArray of objects 货件列表。

## 示例

### 示例 0

```text
ASC
```

### 示例 1

```text
DESC
```

### 示例 2

```json
{"cursor": "string","filter": {"name": "string","offer_id": "string","posting_numbers": ["string"],"since": "2019-08-24T14:15:22Z","statuses": ["string"],"to": "2019-08-24T14:15:22Z"},"limit": 1,"sort_by": "string","sort_dir": "ASC"}
```

### 示例 3

```json
{"cursor": "string","postings": [{"financial_data": {"cluster_from": "string","cluster_to": "string","delivery_amount": 0,"products": [{"actions": [{"action_id": "string","date_from": "2019-08-24T14:15:22Z","date_to": "2019-08-24T14:15:22Z","discount_percent": 0,"discount_value": 0,"is_from_seller": true,"description": "string"}],"commissions_currency_code": "string","old_price": 0,"price": 0,"product_id": 0,"quantity": 0,"total_discount_percent": 0,"posting_commission": {"amount": 0,"payout": 0,"percent": 0},"return_commission": {"amount": 0,"payout": 0,"percent": 0},"total_discount_value": 0}]},"in_process_at": "2019-08-24T14:15:22Z","order_date": "2019-08-24T14:15:22Z","order_id": 0,"order_number": "string","posting_number": "string","products": [{"customer_price": {"amount": "string","currency": "string"},"name": "string","offer_id": "string","price": {"amount": "string","currency": "string"},"quantity": 0,"seller_price": {"amount": "string","currency": "string"},"sku": 0}],"provider_id": 0,"status": "string"}]}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

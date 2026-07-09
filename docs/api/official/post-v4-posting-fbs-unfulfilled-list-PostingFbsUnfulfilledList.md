# 获取未处理货件列表

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v4/posting/fbs/unfulfilled/list`
- Operation ID：`PostingFbsUnfulfilledList`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/PostingFbsUnfulfilledList
- 分组：`posting`

## 页面标题结构

- 获取未处理货件列表
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

cursorstring 用于选择下一批数据的指针。 filterobject 请求筛选器。 使用按备货时间的筛选器——cutoff，或按货件转移配送的日期筛选——delivering_date。 如果同时使用这两个筛选器，响应会返回错误。 要使用按备货时间的筛选器，请填写cutoff_from和cutoff_to字段。 要使用按货件转移配送日期的筛选器，请填写delivering_date_from和delivering_date_to字段。 limitinteger <int64> [ 1 .. 100 ] 响应中返回的值数量。 sort_dirstring Enum: "ASC" "DESC" 排序方向： ASC——升序； DESC——降序。 translitboolean 则启用将地址从西里尔字母转写为拉丁字母。 withobject 需要添加到响应中的附加字段。

### 表格 2

countinteger <int64> 在响应中的元素计数器。 cursorstring 用于选择下一批数据的指针。 has_nextboolean 若响应中未返回全部货件，则为true。 postingsArray of objects 货件列表。

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
{"sort_dir": "asc","limit": 100,"filter": {"cutoff_from": "2026-01-21T07:13:56.042Z","cutoff_to": "2026-01-21T07:13:56.042Z","delivery_method_ids": [123456],"statuses": ["awaiting_packaging","awaiting_deliver","delivering"],"warehouse_ids": [3092889984],"provider_ids": [57],"last_change_status_date": {"from": "2026-01-21T07:13:56.042Z","to": "2026-01-21T07:13:56.042Z"}},"cursor": "","with": {"barcodes": true,"analytics_data": true,"financial_data": true,"legal_info": true}}
```

### 示例 3

```text
{"has_next": true,"cursor": "eyJmaWVsZHMiOlt7Im5hbWUiOiJvc3AuY3V0b2ZmIiwiZGlyIjoiYXNjIiwidmFsIjoiMjAyNi0wNS0wNVQwNjo0NDozN1oifSx7Im5hbWUiOiJvc3AuaW5fcHJvY2Vzc19hdCIsImRpciI6ImFzYyIsInZhbCI6IjIwMjYtMDUtMDRUMDY6NDQ6MzdaIn0seyJuYW1lIjoib3NwLmlkIiwiZGlyIjoiYXNjIiwidmFsIjoiMTIwODk3MjIwMiJ9LHsibmFtZSI6Im9zcC5pZCIsImRpciI6ImFzYyIsInZhbCI6IjEyMDg5NzIyMDIifV19","postings": [{"posting_number": "41517061-0214-1","order_id": 34953320005,"order_number": "41517061-0214","pickup_code_verified_at": null,"status": "awaiting_deliver","substatus": "posting_in_carriage","delivery_method": {"id": 20605650762000,"name": "Ozon配送（自发货），索菲诺","warehouse_id": 20605650762000,"warehouse": "17023","tpl_provider_id": 24,"tpl_provider": "Ozon配送"},"delivery_schema": "fbs","tracking_number": "","tpl_integration_type": "ozon","in_process_at": "2026-05-04T06:44:37Z","shipment_date": "2026-05-05T06:44:37Z","shipment_date_without_delay": "2026-05-06T04:00:00Z","optional": {"products_with_possible_mandatory_mark": [4116250392]},"cancellation": {"cancel_reason_id": 0,"cancel_reason": "","cancellation_type": "","cancelled_after_ship": false,"affect_cancellation_rating": false,"cancellation_initiator": ""},"customer": null,"products": [{"is_blr_traceable": false,"is_marketplace_buyout": false,"offer_id": "S5200657-28","name": "男童半季真皮运动鞋","sku": 4116250392,"quantity": 1,"imei": [ ],"weight": 0.549,"product_color": "深蓝色","price": {"amount": "300","currency": "RUB"}}],"addressee": null,"barcodes": {"upper_barcode": "0","lower_barcode": "0"},"analytics_data": {"region": "","city": "","delivery_type": "PVZ","is_premium": false,"payment_type_group_name": "银行卡","warehouse_id": 20605650762000,"warehouse": "17023","tpl_provider_id": 24,"tpl_provider": "Ozon配送","delivery_date_begin": "2026-05-05T06:38:10Z","delivery_date_end": "2026-05-06T06:38:10Z","is_legal": true,"client_delivery_date_begin": null,"client_delivery_date_end": null},"destination_place_id": 0,"destination_place_name": "","financial_data": {"products": [{"payout": 0,"product_id": 4116250392,"old_price": 300,"price": 300,"total_discount_value": 0,"total_discount_percent": 0,"quantity": 1,"customer_price": {"amount": "300","currency": "RUB"},"actions": [ ],"commission": {"amount": 0,"percent": 0,"currency": "RUB"}}],"cluster_from": "莫斯科、莫斯科州和偏远地区","cluster_to": "莫斯科、莫斯科州和偏远地区"},"is_express": false,"legal_info": {"company_name": "","inn": "","kpp"
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

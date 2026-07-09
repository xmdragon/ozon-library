# FBO和FBS退货信息

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/returns/list`
- Operation ID：`returnsList`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/returnsList
- 分组：`returns`

## 页面标题结构

- FBO和FBS退货信息
- Request Body schema: application/json
- 回复
- Response Schema: application/json
- 请求范例
- 回复范例

## 参数与返回结构

### 表格 0

| 字段 | 类型/说明 |
| --- | --- |
| `filter` | object 筛选条件。在请求中仅使用一个筛选器：logistic_return_date、storage_tariffication_start_date 或visual_status_change_moment，否则会返回错误。 |
| `limit` required | integer <int32> <= 500 加载的退货数量。 |
| `last_id` | integer <int64> 最后加载的退货ID。 |

### 表格 1

| 字段 | 类型/说明 |
| --- | --- |
| `returns` | Array of objects 退货信息。 |
| `has_next` | boolean 如果卖家有其他退货，显示true。 |

## 示例

### 示例 0

```text
logistic_return_date
```

### 示例 1

```text
storage_tariffication_start_date
```

### 示例 2

```text
visual_status_change_moment
```

### 示例 3

```text
true
```

### 示例 4

```json
{"filter": {"logistic_return_date": {"time_from": "2026-02-01T00:00:00Z","time_to": "2026-03-01T23:59:59Z"},"order_id": "7000123456","posting_numbers": ["789456123-0002-3","123456789-0001-1"],"product_name": "string","offer_id": "test-offer-123456","visual_status_name": "ArrivedAtReturnPlace","warehouse_id": "3000007863","barcode": "test-barcode-123456789","return_schema": "FBS"},"limit": 500,"last_id": 0}
```

### 示例 5

```json
{"returns": [{"exemplars": [{"id": "1019562967545956"}],"id": "1000015552","company_id": "3058","return_reason_name": "买家拒绝取货：对商品质量不满意","type": "FullReturn","schema": "Fbs","order_id": "24540784250","order_number": "58544282-0057","place": {"id": "23869688194000","name": "string","address": "string"},"target_place": {"id": "23869688194000","name": "string","address": "string"},"storage": {"sum": {"currency_code": "RUB","price": "1231"},"tariffication_first_date": "2024-07-30T06:15:48.998146Z","tariffication_start_date": "2024-07-29T06:15:48.998146Z","arrived_moment": "2024-07-29T06:15:48.998146Z","days": "0","utilization_sum": {"currency_code": "RUB","price": "1231"},"utilization_forecast_date": "2024-07-29T06:15:48.998146Z"},"product": {"sku": "1100526203","offer_id": "81451","name": "Cry Babies Dressy Dotty","price": {"currency_code": "RUB","price": "3318"},"price_without_commission": {"currency_code": "RUB","price": "3318"},"commission_percent": "1.2","commission": {"currency_code": "RUB","price": "2312"}},"logistic": {"technical_return_moment": "2024-07-29T06:15:48.998146Z","final_moment": "2024-07-29T06:15:48.998146Z","cancelled_with_compensation_moment": "2024-07-29T06:15:48.998146Z","return_date": "2024-07-29T06:15:48.998146Z","barcode": "ii5275210303"},"visual": {"status": {"id": 3,"display_name": "在取货点","sys_name": "ArrivedAtReturnPlace"},"change_moment": "2024-07-29T06:15:48.998146Z"},"additional_info": {"is_opened": true,"is_super_econom": false},"source_id": "90426223","posting_number": "58544282-0057-1","clearing_id": "21190893156000","return_clearing_id": null,"compensation_status": {"status": {"id": 2,"display_name": "您已收到赔偿","sys_name": "Received"},"change_moment": "2025-11-06T16:06:56.639Z"}}],"has_next": false}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

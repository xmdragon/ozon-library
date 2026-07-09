# 交易清单

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v3/finance/transaction/list`
- Operation ID：`FinanceAPI_FinanceTransactionListV3`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/FinanceAPI_FinanceTransactionListV3
- 分组：`finance`

## 页面标题结构

- 交易清单
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
| `filter` | posting_number (object) or date (object) 过滤器。 |
| `page` required | integer <int64> 请求中返回的页码。 |
| `page_size` required | integer <int64> <= 1000 每页的元素数。 |

### 表格 2

| 字段 | 类型/说明 |
| --- | --- |
| `result` | object 询问结果。 |
| `operations` | Array of objects 操作信息。 |
| `page_count` | integer <int64> 页数。如果为0，则说明已无页面。 |
| `row_count` | integer <int64> 所有页面上的交易数量。如果为0，说明已无交易。 |

### 表格 3

| 字段 | 类型/说明 |
| --- | --- |
| `operations` | Array of objects 操作信息。 |
| `page_count` | integer <int64> 页数。如果为0，则说明已无页面。 |
| `row_count` | integer <int64> 所有页面上的交易数量。如果为0，说明已无交易。 |

## 示例

### 示例 0

```text
posting_number
```

### 示例 1

```json
{"filter": {"date": {"from": "2021-11-01T00:00:00.000Z","to": "2021-11-02T00:00:00.000Z"},"operation_type": [ ],"posting_number": "","transaction_type": "all"},"page": 1,"page_size": 1000}
```

### 示例 2

```json
{"result": {"operations": [{"operation_id": 11401182187840,"operation_type": "MarketplaceMarketingActionCostOperation","operation_date": "2021-11-01 00:00:00","operation_type_name": "商品推销服务","delivery_charge": 0,"return_delivery_charge": 0,"accruals_for_sale": 0,"sale_commission": 0,"amount": -6.46,"type": "services","posting": {"delivery_schema": "","order_date": "","posting_number": "","warehouse_id": 0},"items": [ ],"services": [ ]}],"page_count": 1,"row_count": 355}}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

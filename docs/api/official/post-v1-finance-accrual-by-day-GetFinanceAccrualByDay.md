# 获取某日应计项目

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/finance/accrual/by-day`
- Operation ID：`GetFinanceAccrualByDay`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/GetFinanceAccrualByDay
- 分组：`finance`

## 页面标题结构

- 获取某日应计项目
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
| `date` required | string YYYY-MM-DD 应计日期。最早可查询日期为2022年1月1日。 |
| `last_id` required | string 页面上最后一个值的标识符。首次请求请留空。 要获取后续值，请指定上一次请求响应中的 last_id。 |

### 表格 2

| 字段 | 类型/说明 |
| --- | --- |
| `accruals` | Array of objects 应计项目列表。 |
| `last_id` | string 页面中最后一个值的标识符。 |

## 示例

### 示例 0

```text
last_id
```

### 示例 1

```json
{"date": "string","last_id": "string"}
```

### 示例 2

```json
{"accruals": [{"accrued_category": "UNSPECIFIED","date": "string","item_fees": {"fees": [{"fees": [{"accrued": {"amount": "string","currency": "string"},"type_id": 0}],"sku": 0}]},"non_item_fee": {"accrued": {"amount": "string","currency": "string"},"type_id": 0},"posting": {"delivery_schema": "string","delivery_speed": 0,"products": [{"commission": {"bonus": {"amount": "string","currency": "string"},"coinvestment": {"amount": "string","currency": "string"},"commission": {"amount": "string","currency": "string"},"commission_ratio": "string","sale_amount": {"amount": "string","currency": "string"},"sale_commission": {"amount": "string","currency": "string"},"sale_price": {"amount": "string","currency": "string"},"seller_price": {"amount": "string","currency": "string"}},"delivery": {"services": [{"accrued": {"amount": null,"currency": null},"type_id": 0}],"total_accrued": {"amount": "string","currency": "string"}},"sku": 0}]},"total_amount": {"amount": "string","currency": "string"},"accrual_id": 0,"unit_number": "string"}],"last_id": "string"}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

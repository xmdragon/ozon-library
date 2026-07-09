# 商品销售报告 （第2版）

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v2/finance/realization`
- Operation ID：`FinanceAPI_GetRealizationReportV2`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/FinanceAPI_GetRealizationReportV2
- 分组：`finance`

## 页面标题结构

- 商品销售报告 （第2版）
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
| `month` required | integer <int32> 月。 |
| `year` required | integer <int32> 年。 |

### 表格 2

| 字段 | 类型/说明 |
| --- | --- |
| `result` | object 请求结果。 |
| `header` | object 报告标题页。 |
| `rows` | Array of objects 报告表格。 |

### 表格 3

| 字段 | 类型/说明 |
| --- | --- |
| `header` | object 报告标题页。 |
| `rows` | Array of objects 报告表格。 |

## 示例

### 示例 0

```json
{
  "month": 0,
  "year": 0
}
```

### 示例 1

```json
{
  "result": {
    "header": {
      "contract_date": "string",
      "contract_number": "string",
      "currency_sys_name": "string",
      "doc_date": "string",
      "number": "string",
      "payer_inn": "string",
      "payer_kpp": "string",
      "payer_name": "string",
      "receiver_inn": "string",
      "receiver_kpp": "string",
      "receiver_name": "string",
      "start_date": "string",
      "stop_date": "string"
    },
    "rows": [
      {
        "commission_ratio": 0,
        "delivery_commission": {
          "amount": 0,
          "bonus": 0,
          "commission": 0,
          "compensation": 0,
          "price_per_instance": 0,
          "quantity": 0,
          "standard_fee": 0,
          "bank_coinvestment": 0,
          "stars": 0,
          "total": 0
        },
        "item": {
          "barcode": "string",
          "name": "string",
          "offer_id": "string",
          "sku": 0
        },
        "return_commission": {
          "amount": 0,
          "bonus": 0,
          "commission": 0,
          "compensation": 0,
          "price_per_instance": 0,
          "quantity": 0,
          "standard_fee": 0,
          "bank_coinvestment": 0,
          "stars": 0,
          "total": 0
        },
        "rowNumber": 0,
        "seller_price_per_instance": 0
      }
    ]
  }
}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

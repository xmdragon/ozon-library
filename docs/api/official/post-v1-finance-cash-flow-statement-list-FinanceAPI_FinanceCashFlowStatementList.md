# 财务报告

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/finance/cash-flow-statement/list`
- Operation ID：`FinanceAPI_FinanceCashFlowStatementList`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/FinanceAPI_FinanceCashFlowStatementList
- 分组：`finance`

## 页面标题结构

- 财务报告
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
| `date` required | object 报告期限。 |
| `page` required | integer <int32> 请求返回中的页码。 |
| `with_details` | boolean true，如果需要在响应中添加附加参数。 |
| `page_size` required | integer <int32> 页面上的元素数量。 |

### 表格 2

| 字段 | 类型/说明 |
| --- | --- |
| `result` | object 方法操作结果。 |
| `cash_flows` | Array of objects 报告清单。 |
| `details` | Array of objects 细节信息。 |
| `page_count` | integer <int64> 含有报告的页数。 |

### 表格 3

| 字段 | 类型/说明 |
| --- | --- |
| `cash_flows` | Array of objects 报告清单。 |
| `details` | Array of objects 细节信息。 |
| `page_count` | integer <int64> 含有报告的页数。 |

## 示例

### 示例 0

```text
true
```

### 示例 1

```json
{
  "date": {
    "from": "2022-01-01T00:00:00.000Z",
    "to": "2022-12-31T00:00:00.000Z"
  },
  "with_details": true,
  "page": 1,
  "page_size": 1
}
```

### 示例 2

```json
{
  "result": {
    "cash_flows": [
      {
        "commission_amount": 1437,
        "currency_code": "string",
        "item_delivery_and_return_amount": 1991,
        "orders_amount": 1000,
        "period": {
          "begin": "2023-04-03T09:12:10.239Z",
          "end": "2023-04-03T09:12:10.239Z",
          "id": 11567022278500
        },
        "returns_amount": -3000,
        "services_amount": 8471.28
      }
    ],
    "details": {
      "period": {
        "begin": "2023-04-03T09:12:10.239Z",
        "end": "2023-04-03T09:12:10.239Z",
        "id": 11567022278500
      },
      "payments": [
        {
          "payment": 0,
          "currency_code": "string"
        }
      ],
      "begin_balance_amount": 0,
      "delivery": {
        "total": 0,
        "amount": 0,
        "delivery_services": {
          "total": 0,
          "items": [
            {
              "name": "string",
              "price": 0
            }
          ]
        }
      },
      "return": {
        "total": 0,
        "amount": 0,
        "return_services": {
          "total": 0,
          "items": [
            {
              "name": "string",
              "price": 0
            }
          ]
        }
      },
      "loan": 0,
      "invoice_transfer": 0,
      "rfbs": {
        "total": 0,
        "transfer_delivery": 0,
        "transfer_delivery_return": 0,
        "compensation_delivery_return": 0,
        "partial_compensation": 0,
        "partial_compensation_return": 0
      },
      "services": {
        "total": 0,
        "items": [
          {
            "name": "string",
            "price": 0
          }
        ]
      },
      "others": {
        "total": 0,
        "items": [
          {
            "name": "string",
            "price": 0
          }
        ]
      },
      "end_balance_amount": 0
    }
  },
  "page_count": 15
}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

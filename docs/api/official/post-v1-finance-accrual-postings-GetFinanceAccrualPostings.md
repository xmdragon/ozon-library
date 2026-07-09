# 获取按货件统计的应计项目

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/finance/accrual/postings`
- Operation ID：`GetFinanceAccrualPostings`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/GetFinanceAccrualPostings
- 分组：`finance`

## 页面标题结构

- 获取按货件统计的应计项目
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
| `posting_numbers` required | Array of strings [ 1 .. 200 ] items 货件编号。 |

### 表格 2

| 字段 | 类型/说明 |
| --- | --- |
| `posting_accruals` | Array of objects 按货件统计的应计项目列表。 |
| `accruals` | Array of objects 应计项目列表。 |
| `posting_number` | string 货件编号。 |

### 表格 3

| 字段 | 类型/说明 |
| --- | --- |
| `accruals` | Array of objects 应计项目列表。 |
| `posting_number` | string 货件编号。 |

## 示例

### 示例 0

```json
{"posting_numbers": ["string"]}
```

### 示例 1

```json
{"posting_accruals": [{"accruals": [{"accrual_date": "string","accrued": {"amount": "string","currency": "string"},"quantity": 0,"seller_price": {"amount": "string","currency": "string"},"sku": 0,"type_id": 0}],"posting_number": "string"}]}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

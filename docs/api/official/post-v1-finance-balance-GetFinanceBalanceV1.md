# 获取余额报告

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/finance/balance`
- Operation ID：`GetFinanceBalanceV1`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/GetFinanceBalanceV1
- 分组：`finance`

## 页面标题结构

- 获取余额报告
- Request Body schema: application/json
- 回复
- Response Schema: application/json
- 请求范例
- 回复范例

## 参数与返回结构

### 表格 0

date_from required string <date-time> 报告期开始日期，格式为 YYYY-MM-DD。 date_to required string <date-time> 报告期结束日期，格式为 YYYY-MM-DD。date_from 与 date_to 之间的最⻓间隔为30 天。

### 表格 1

cashflowsobject 收入和支出信息。 totalobject 周期内的余额总体数据。

## 示例

### 示例 0

```text
YYYY-MM-DD
```

### 示例 1

```text
YYYY-MM-DD
```

### 示例 2

```json
{"date_from": "2019-08-24","date_to": "2019-09-24"}
```

### 示例 3

```json
{"cashflows": {"returns": {"amount": {"currency_code": "string","value": 0},"amount_details": {"partner_programs": {"currency_code": "string","value": 0},"points_for_discounts": "string","revenue": {"currency_code": "string","value": 0}},"fee": {"currency_code": "string","value": 0}},"sales": {"amount": {"currency_code": "string","value": 0},"amount_details": {"partner_programs": {"currency_code": "string","value": 0},"points_for_discounts": "string","revenue": {"currency_code": "string","value": 0}},"fee": {"currency_code": "string","value": 0}},"services": [{"amount": {"currency_code": "string","value": 0},"name": "string"}]},"total": {"accrued": {"currency_code": "string","value": 0},"closing_balance": {"currency_code": "string","value": 0},"opening_balance": {"currency_code": "string","value": 0},"payments": [{"currency_code": "string","value": 0}]}}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

# 生成带有标记商品的销售报告

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/report/marked-products-sales/create`
- Operation ID：`CreateCompanyMarkedProductsSalesReport`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/CreateCompanyMarkedProductsSalesReport
- 分组：`report`

## 页面标题结构

- 生成带有标记商品的销售报告
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

dateobject 报告生成周期。

### 表格 2

resultobject 请求结果。 codestring 报告的唯一识别码。要获取报告，请将此值传递到方法 /v1/report/info。

### 表格 3

codestring 报告的唯一识别码。要获取报告，请将此值传递到方法 /v1/report/info。

## 示例

### 示例 0

```json
{"date": {"from": "string","to": "string"}}
```

### 示例 1

```json
{"result": {"code": "string"}}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

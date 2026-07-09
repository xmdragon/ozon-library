# 赔偿返还报告

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/finance/decompensation`
- Operation ID：`ReportAPI_GetDecompensationReport`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/ReportAPI_GetDecompensationReport
- 分组：`finance`

## 页面标题结构

- 赔偿返还报告
- Request Body schema: application/json
- 回复
- Response Schema: application/json
- 请求范例
- 回复范例

## 参数与返回结构

### 表格 0

date required string 报告周期格式为 YYYY-MM。 languagestring Default: "RU" 报告语言： RU — 俄语， EN — 英语。

### 表格 1

resultobject 请求结果。 codestring 报告的唯一标识符。要获取报告，请将该值传递到方法 /v1/report/info。

### 表格 2

codestring 报告的唯一标识符。要获取报告，请将该值传递到方法 /v1/report/info。

## 示例

### 示例 0

```text
YYYY-MM
```

### 示例 1

```json
{"date": "2023-09","language": "RU"}
```

### 示例 2

```json
{"result": {"code": "string"}}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

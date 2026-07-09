# 发运组成商品更改

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/carriage/set-postings`
- Operation ID：`CarriageAPI_SetPostings`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/CarriageAPI_SetPostings
- 分组：`carriage`

## 页面标题结构

- 发运组成商品更改
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

carriage_id required integer <int64> 发运识别符。 posting_numbers required Array of strings 最新货件列表。

### 表格 2

resultArray of objects Array ()errorstring 错误描述。 posting_numberstring 货件编号。 resultboolean 请求处理结果：若请求处理成功，返回值为true。

### 表格 3

errorstring 错误描述。 posting_numberstring 货件编号。 resultboolean 请求处理结果：若请求处理成功，返回值为true。

## 示例

### 示例 0

```json
{"carriage_id": 0,"posting_numbers": ["string"]}
```

### 示例 1

```json
{"result": [{"error": "string","posting_number": "string","result": true}]}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

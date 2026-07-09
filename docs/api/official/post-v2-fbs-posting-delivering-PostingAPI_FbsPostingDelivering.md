# 将状态改成“运输中”

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v2/fbs/posting/delivering`
- Operation ID：`PostingAPI_FbsPostingDelivering`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/PostingAPI_FbsPostingDelivering
- 分组：`fbs`

## 页面标题结构

- 将状态改成“运输中”
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

posting_number required Array of strings 货件ID。

### 表格 2

resultArray of objects 方法操作结果。 Array ()errorstring 处理请求时出错。 posting_numberstring 发货号。 resultboolean 如果执行请求无误 — true。

### 表格 3

errorstring 处理请求时出错。 posting_numberstring 发货号。 resultboolean 如果执行请求无误 — true。

## 示例

### 示例 0

```json
{"posting_number": ["33920157-0018-1"]}
```

### 示例 1

```json
{"result": [{"error": [ ],"posting_number": "33920157-0018-1","result": true}]}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

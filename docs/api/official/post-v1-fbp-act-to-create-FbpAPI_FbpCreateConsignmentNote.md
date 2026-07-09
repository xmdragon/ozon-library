# 生成货物运单

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/fbp/act-to/create`
- Operation ID：`FbpAPI_FbpCreateConsignmentNote`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/FbpAPI_FbpCreateConsignmentNote
- 分组：`fbp`

## 页面标题结构

- 生成货物运单
- Request Body schema: application/json
- 回复
- Response Schema: application/json
- 请求范例
- 回复范例

## 参数与返回结构

### 表格 0

supply_id required string 交货标识符。

### 表格 1

codestring 货物运单标识符。

## 示例

### 示例 0

```json
{"supply_id": "string"}
```

### 示例 1

```json
{"code": "string"}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

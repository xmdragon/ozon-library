# 创建发运

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/carriage/create`
- Operation ID：`CarriageAPI_CarriageCreate`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/CarriageAPI_CarriageCreate
- 分组：`carriage`

## 页面标题结构

- 创建发运
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

all_blr_traceableboolean true，表示需要创建包含可追溯商品的发运。 delivery_method_idinteger <int64> 配送方式标识符。 departure_datestring <date-time> 发运日期。默认值为当前日期。

### 表格 2

carriage_idinteger <int64> 运输标识符。

## 示例

### 示例 0

```json
{"all_blr_traceable": true,"delivery_method_id": 0,"departure_date": "2019-08-24T14:15:22Z"}
```

### 示例 1

```json
{"carriage_id": 0}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

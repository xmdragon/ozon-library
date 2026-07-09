# 从档案中还原商品

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/product/unarchive`
- Operation ID：`ProductAPI_ProductUnarchive`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/ProductAPI_ProductUnarchive
- 分组：`product`

## 页面标题结构

- 从档案中还原商品
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

product_id required Array of integers <int64> Ozon系统中商品的标识符 — product_id。您一次最多可以传递100个标识符。 在一天内，您最多可以从档案中恢复100件自动归档的商品。 限额在莫斯科时间03：00更新。 手动归档的商品没有解除归档的限制。

### 表格 2

resultboolean 查询的处理结果。true，如果查询的执行无误。

## 示例

### 示例 0

```json
{"product_id": ["125529926","987654321"]}
```

### 示例 1

```json
{"result": true}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

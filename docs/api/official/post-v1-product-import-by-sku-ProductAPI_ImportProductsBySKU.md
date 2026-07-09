# 通过SKU创建商品

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/product/import-by-sku`
- Operation ID：`ProductAPI_ImportProductsBySKU`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/ProductAPI_ImportProductsBySKU
- 分组：`product`

## 页面标题结构

- 通过SKU创建商品
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

itemsArray of objects <= 1000 items 商品信息。

### 表格 2

resultobject task_idinteger <int64> 进口货物任务代码。 unmatched_sku_listArray of integers <int64> 商品Id列表。

### 表格 3

task_idinteger <int64> 进口货物任务代码。 unmatched_sku_listArray of integers <int64> 商品Id列表。

## 示例

### 示例 0

```text
429
```

### 示例 1

```json
{"items": [{"sku": 298789742,"name": "杯子","offer_id": "91132","currency_code": "RUB","old_price": "2590","price": "2300","vat": "0.1"}]}
```

### 示例 2

```json
{"result": {"task_id": 176594213,"unmatched_sku_list": [ ]}}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

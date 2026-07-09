# 在促销活动中增加一个商品

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/actions/products/activate`
- Operation ID：`PromosProductsActivate`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/PromosProductsActivate
- 分组：`actions`

## 页面标题结构

- 在促销活动中增加一个商品
- Request Body schema: application/json
- 回复
- Response Schema: application/json
- 请求范例
- 回复范例

## 参数与返回结构

### 表格 0

action_id required number <double> 活动识别号。可以使用方法 /v1/actions获取。 products required Array of objects <= 1000 items 商品清单。

### 表格 1

resultobject 请求结果。 product_idsArray of numbers <double> 已添加到促销活动中的商品ID列表。 rejectedArray of objects 无法添加到促销活动中的商品列表。

### 表格 2

product_idsArray of numbers <double> 已添加到促销活动中的商品ID列表。 rejectedArray of objects 无法添加到促销活动中的商品列表。

## 示例

### 示例 0

```json
{"action_id": 60564,"products": [{"action_price": 356,"product_id": 1389,"stock": 10}]}
```

### 示例 1

```json
{"result": {"product_ids": [1389],"rejected": [ ]}}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

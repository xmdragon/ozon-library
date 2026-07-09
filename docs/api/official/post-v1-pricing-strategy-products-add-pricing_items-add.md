# 将商品添加到策略

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/pricing-strategy/products/add`
- Operation ID：`pricing_items-add`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/pricing_items-add
- 分组：`pricing-strategy`

## 页面标题结构

- 将商品添加到策略
- Request Body schema: application/json
- 回复
- Response Schema: application/json
- 请求范例
- 回复范例

## 参数与返回结构

### 表格 0

product_id required Array of strings <int64> 商品ID列表。 最大数量为 50。 strategy_id required string 策略ID。

### 表格 1

resultobject 方法操作结果。 errorsArray of objects 有错误的商品。 failed_product_countinteger <int32> 有错误的商品数量。

### 表格 2

errorsArray of objects 有错误的商品。 failed_product_countinteger <int32> 有错误的商品数量。

## 示例

### 示例 0

```json
{"product_id": ["29209"],"strategy_id": "e29114f0-177d-4160-8d06-2bc528470dda"}
```

### 示例 1

```json
{"result": {"failed_product_count": 0}}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

# 更新价格

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/product/import/prices`
- Operation ID：`ProductAPI_ImportProductsPrices`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/ProductAPI_ImportProductsPrices
- 分组：`product`

## 页面标题结构

- 更新价格
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

pricesArray of objects <= 1000 items 商品价格信息。

### 表格 2

resultArray of objects 搜索结果。 Array ()errorsArray of objects 在搜索处理过程中发生的数组错误。 offer_idstring 卖家系统中的商品编号是 — 商品代码。 product_idinteger <int64> Ozon系统中商品的标识符 — product_id。 updatedboolean 如果商品信息已被成功更新 — true。

### 表格 3

errorsArray of objects 在搜索处理过程中发生的数组错误。 offer_idstring 卖家系统中的商品编号是 — 商品代码。 product_idinteger <int64> Ozon系统中商品的标识符 — product_id。 updatedboolean 如果商品信息已被成功更新 — true。

## 示例

### 示例 0

```json
{"prices": [{"auto_action_enabled": "UNKNOWN","currency_code": "RUB","manage_elastic_boosting_through_price": true,"min_price": "800","min_price_for_auto_actions_enabled": true,"net_price": "650","offer_id": "","old_price": "0","price": "1448","price_strategy_enabled": "UNKNOWN","product_id": 1386,"vat": "0.1"}]}
```

### 示例 1

```json
{"result": [{"product_id": 1386,"offer_id": "PH8865","updated": true,"errors": [ ]}]}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

# 从卖家的系统中改变商品货号

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/product/update/offer-id`
- Operation ID：`ProductAPI_ProductUpdateOfferID`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/ProductAPI_ProductUpdateOfferID
- 分组：`product`

## 页面标题结构

- 从卖家的系统中改变商品货号
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

update_offer_id required Array of objects [ 1 .. 25 ] items 具有新旧货号价值的配对列表。

### 表格 2

errorsArray of objects 错误清单。 Array ()messagestring 错误信息。 offer_idstring 无法更改的卖家系统中的商品标识符是商品货号。

### 表格 3

messagestring 错误信息。 offer_idstring 无法更改的卖家系统中的商品标识符是商品货号。

## 示例

### 示例 0

```text
OFFER_ID_ALREADY_EXISTS
```

### 示例 1

```text
429
```

### 示例 2

```json
{"update_offer_id": [{"new_offer_id": "haval","offer_id": "chery"}]}
```

### 示例 3

```json
{"errors": [{"offer_id": "haval","message": "货号为haval的商品已存在。"}]}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

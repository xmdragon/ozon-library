# 获取可自动添加到促销活动中的商品列表

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/actions/auto-add/products/candidates`
- Operation ID：`ActionsAutoAddProductsCandidates`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/ActionsAutoAddProductsCandidates
- 分组：`actions`

## 页面标题结构

- 获取可自动添加到促销活动中的商品列表
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

action_id required integer <uint64> 促销活动标识符。 auto_add_date required string <date-time> 方法/v1/actions响应中result.auto_add_dates参数里的商品自动添加到促销活动中的日期和时间。 limit required integer <uint64> [ 1 .. 100 ] 响应中返回的值数量。 offsetinteger <uint64> Default: 0 在响应中将被跳过的项目数量。例如，如果offset = 10，响应将从第11个找到的元素开始。

### 表格 2

productsArray of objects 可用于自动添加到促销活动中的商品列表。 totalinteger <uint64> 商品总数。

## 示例

### 示例 0

```json
{"action_id": "250204","auto_add_date": "2035-08-28T14:00:00Z","limit": "1","offset": "0"}
```

### 示例 1

```json
{"products": [{"produсt_id": "14903","offer_id": "PS0007","sku": "146279508","name": "香薰 / 浴用油 / 精油 \"冷杉\"，250毫升","price": 114,"base_price": 346,"max_discount_price": 79,"min_seller_price:": 50,"marketplace_seller_price": 59,"action_price_to_auto_add": 79,"min_action_quantity": "0","quantity_to_auto_add": "10","currency": "RUB"}],"total": "443"}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

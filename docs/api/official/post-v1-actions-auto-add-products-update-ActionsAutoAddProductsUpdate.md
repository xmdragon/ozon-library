# 在促销活动自动添加列表中添加或更新商品

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/actions/auto-add/products/update`
- Operation ID：`ActionsAutoAddProductsUpdate`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/ActionsAutoAddProductsUpdate
- 分组：`actions`

## 页面标题结构

- 在促销活动自动添加列表中添加或更新商品
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

action_idinteger <uint64> 促销活动标识符。 auto_add_datestring <date-time> 方法/v1/actions响应中result.auto_add_dates参数里的商品自动添加到促销活动中的日期和时间。 to_updateArray of objects 需要添加到自动添加中或在自动添加中更新的商品列表。

### 表格 2

below_min_priceArray of objects 价格低于最低价格的商品列表。 extremely_low_priceArray of objects 折扣幅度超过70%的商品列表。 failed_priceArray of objects 未通过价格校验的商品列表。 rejectedArray of objects 未能添加或更新的商品ID。 updated_idsArray of strings <uint64> 已成功添加或更新的商品ID。

## 示例

### 示例 0

```json
{"action_id": "250204","auto_add_dates": "2035-08-28T14:00:00Z","to_update": [{"currency": "RUB","product_id": "14914","quantity": 10,"action_price": 100}]}
```

### 示例 1

```json
{"updated_ids": ["14914"],"rejected": [ ],"below_min_price": [{"key": "14914","value": 100}],"extremely_low_price": [ ],"failed_price": [ ]}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

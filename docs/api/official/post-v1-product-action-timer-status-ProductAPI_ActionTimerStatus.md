# 获取已设置计时器状态

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/product/action/timer/status`
- Operation ID：`ProductAPI_ActionTimerStatus`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/ProductAPI_ActionTimerStatus
- 分组：`product`

## 页面标题结构

- 获取已设置计时器状态
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

product_idsnumber <= 1000 卖家系统中的商品识别符列表——product_id。

### 表格 2

statusesArray of objects Array ()expired_atstring <date-time> 计时器结束时间。如果该参数为空，则没有有效的计时器。 min_price_for_auto_actions_enabledboolean 如果Ozon在添加商品至促销活动时会参考最低价格，则返回值为true。 product_idinteger <int64> 卖家系统中的商品识别符——product_id。

### 表格 3

expired_atstring <date-time> 计时器结束时间。如果该参数为空，则没有有效的计时器。 min_price_for_auto_actions_enabledboolean 如果Ozon在添加商品至促销活动时会参考最低价格，则返回值为true。 product_idinteger <int64> 卖家系统中的商品识别符——product_id。

## 示例

### 示例 0

```json
{"product_ids": 0}
```

### 示例 1

```json
{"statuses": [{"expired_at": "2019-08-24T14:15:22Z","min_price_for_auto_actions_enabled": true,"product_id": 0}]}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

# 活动清单

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`GET /v1/actions`
- Operation ID：`Promos`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/Promos
- 分组：`actions`

## 页面标题结构

- 活动清单
- 回复
- Response Schema: application/json
- 回复范例

## 参数与返回结构

### 表格 0

| 字段 | 类型/说明 |
| --- | --- |
| `result` | Array of objects 请求结果。 |
| `id` | number <double> 活动识别号。 |
| `title` | string 活动名称。 |
| `action_type` | string 活动类型。 |
| `description` | string 活动描述。 |
| `date_start` | string 活动开始日期。 |
| `date_end` | string 活动结束日期。 |
| `auto_add_dates` | Array of strings <date-time> 商品自动添加到促销活动中的日期和时间。 |
| `freeze_date` | string 活动暂停的日期。 如果该空白被填写，卖家就不能提高价格，改变商品清单或减少促销活动的单位数量。 卖方可以降低价格，增加促销的单位数量。 |
| `potential_products_count` | number <double> 可供活动的商品数量。 |
| `participating_products_count` | number <double> 参加促销的商品数量。 |
| `is_participating` | boolean 无论你是否参加这项活动。 |
| `is_voucher_action` | boolean 此迹象表明买家需要促销代码才能参加。 |
| `banned_products_count` | number <double> 被封商品数量。 |
| `with_targeting` | boolean 此迹象表明该活动是与目标受众一起进行的。 |
| `order_amount` | number <double> 预定金额。 |
| `discount_type` | string 折扣类型。 |
| `discount_value` | number <double> 折扣力度。 |

### 表格 1

| 字段 | 类型/说明 |
| --- | --- |
| `id` | number <double> 活动识别号。 |
| `title` | string 活动名称。 |
| `action_type` | string 活动类型。 |
| `description` | string 活动描述。 |
| `date_start` | string 活动开始日期。 |
| `date_end` | string 活动结束日期。 |
| `auto_add_dates` | Array of strings <date-time> 商品自动添加到促销活动中的日期和时间。 |
| `freeze_date` | string 活动暂停的日期。 如果该空白被填写，卖家就不能提高价格，改变商品清单或减少促销活动的单位数量。 卖方可以降低价格，增加促销的单位数量。 |
| `potential_products_count` | number <double> 可供活动的商品数量。 |
| `participating_products_count` | number <double> 参加促销的商品数量。 |
| `is_participating` | boolean 无论你是否参加这项活动。 |
| `is_voucher_action` | boolean 此迹象表明买家需要促销代码才能参加。 |
| `banned_products_count` | number <double> 被封商品数量。 |
| `with_targeting` | boolean 此迹象表明该活动是与目标受众一起进行的。 |
| `order_amount` | number <double> 预定金额。 |
| `discount_type` | string 折扣类型。 |
| `discount_value` | number <double> 折扣力度。 |

## 示例

### 示例 0

```json
{"result": [{"id": 71342,"title": "test voucher #2","date_start": "2021-11-22T09:46:38Z","date_end": "2021-11-30T20:59:59Z","auto_add_dates": ["2025-12-30T20:59:59Z"],"potential_products_count": 0,"is_participating": true,"participating_products_count": 5,"description": "","action_type": "DISCOUNT","banned_products_count": 0,"with_targeting": false,"discount_type": "UNKNOWN","discount_value": 0,"order_amount": 0,"freeze_date": "","is_voucher_action": true}]}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

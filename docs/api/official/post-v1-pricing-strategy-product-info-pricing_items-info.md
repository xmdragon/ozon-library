# 竞争对手 的商品价格

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/pricing-strategy/product/info`
- Operation ID：`pricing_items-info`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/pricing_items-info
- 分组：`pricing-strategy`

## News 更新标记

| 日期 | 标记 | 摘要 | 来源 |
| --- | --- | --- | --- |
| 2025-06-19 | `deprecated_field` | /v1/pricing-strategy/product/info 并将参数 result.strategy_competitor_id 标记为已弃用。 | [官方 News](https://docs.ozon.ru/api/seller/zh/#section/2025619) |

## 页面标题结构

- 竞争对手 的商品价格
- header Parameters
- Request Body schema: application/json
- 回复
- Response Schema: application/json
- 请求范例
- 回复范例

## 参数与返回结构

### 表格 0

| 字段 | 类型/说明 |
| --- | --- |
| `Client-Id` required | string 用户识别号。 |
| `Api-Key` required | string API-密钥。 |

### 表格 1

| 字段 | 类型/说明 |
| --- | --- |
| `product_id` required | integer <int64> Ozon系统中商品的标识符 — product_id。 |

### 表格 2

| 字段 | 类型/说明 |
| --- | --- |
| `result` | object 方法操作结果。 |
| `strategy_id` | string 策略ID。 |
| `is_enabled` | boolean true, 如果商品参与定价策略。 |
| `strategy_product_price` | integer <int32> 定价策略。 |
| `price_downloaded_at` | string 定价策略设定日期。 |
| `strategy_competitor_id` | integer <int64> Deprecated 竞争对手ID。 |
| `strategy_competitor_product_url` | string 竞争对手商品链接。 |

### 表格 3

| 字段 | 类型/说明 |
| --- | --- |
| `strategy_id` | string 策略ID。 |
| `is_enabled` | boolean true, 如果商品参与定价策略。 |
| `strategy_product_price` | integer <int32> 定价策略。 |
| `price_downloaded_at` | string 定价策略设定日期。 |
| `strategy_competitor_id` | integer <int64> Deprecated 竞争对手ID。 |
| `strategy_competitor_product_url` | string 竞争对手商品链接。 |

## 示例

### 示例 0

```text
product_id
```

### 示例 1

```text
true
```

### 示例 2

```json
{
  "product_id": 7856197312
}
```

### 示例 3

```json
{
  "result": {
    "strategy_id": "b7cd30e6-5667-424d-b105-fbec30a52477",
    "is_enabled": true,
    "strategy_product_price": 500,
    "price_downloaded_at": "2022-11-17T15:33:53.936Z",
    "strategy_competitor_id": "b7cd30e6-5667-424d-b105-fbec30a52477",
    "strategy_competitor_product_url": "http://primerurl/pricing-strategy/product/info.ru"
  }
}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

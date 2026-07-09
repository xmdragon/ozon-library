# 参与 活动的商品列表

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/actions/products`
- Operation ID：`PromosProducts`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/PromosProducts
- 分组：`actions`

## 页面标题结构

- 参与 活动的商品列表
- Request Body schema: application/json
- 回复
- Response Schema: application/json
- 请求范例
- 回复范例

## 参数与返回结构

### 表格 0

| 字段 | 类型/说明 |
| --- | --- |
| `action_id` | number <double> 活动识别号。可以使用方法 /v1/actions获取。 |
| `limit` | number <double> 每页的答复数量。在默认情况下 — 100。 |
| `last_id` | number <double> 页面上最后一个值的ID。运行第一个查询时，将此字段留空。 |

### 表格 1

| 字段 | 类型/说明 |
| --- | --- |
| `result` | object 请求结果。 |
| `products` | Array of objects 商品清单。 |
| `total` | number <double> 可用于活动的商品总数。 |
| `last_id` | number <double> 页面上最后一个值的ID。运行第一个查询时，将此字段留空。 要检索以下数值，请从上一个查询的响应中指定last_id。 |

### 表格 2

| 字段 | 类型/说明 |
| --- | --- |
| `products` | Array of objects 商品清单。 |
| `total` | number <double> 可用于活动的商品总数。 |
| `last_id` | number <double> 页面上最后一个值的ID。运行第一个查询时，将此字段留空。 要检索以下数值，请从上一个查询的响应中指定last_id。 |

## 示例

### 示例 0

```text
last_id
```

### 示例 1

```json
{
  "action_id": 66011,
  "limit": 10,
  "last_id": "bnVсbA=="
}
```

### 示例 2

```json
{
  "result": {
    "products": [
      {
        "id": 28745,
        "price": 99,
        "action_price": 50,
        "alert_max_action_price_failed": true,
        "alert_max_action_price": 31,
        "max_action_price": 32,
        "add_mode": "MANUAL",
        "stock": 20,
        "min_stock": 3,
        "current_boost": 1,
        "price_min_elastic": 2,
        "price_max_elastic": 5,
        "min_boost": 10,
        "max_boost": 15
      }
    ],
    "total": 263,
    "last_id": "bnVсbA=="
  }
}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

# 可用的促销商品清单

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/actions/candidates`
- Operation ID：`PromosCandidates`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/PromosCandidates
- 分组：`actions`

## 页面标题结构

- 可用的促销商品清单
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
  "action_id": 63337,
  "limit": 10,
  "last_id": "bnVсbA==123123das"
}
```

### 示例 2

```json
{
  "result": {
    "products": [
      {
        "id": 226,
        "price": 250,
        "action_price": 10,
        "alert_max_action_price_failed": true,
        "alert_max_action_price": 31,
        "max_action_price": 175,
        "add_mode": "NOT_SET",
        "stock": 2,
        "min_stock": 1,
        "current_boost": 3,
        "price_min_elastic": 150,
        "price_max_elastic": 300,
        "min_boost": 12,
        "max_boost": 15
      }
    ],
    "total": 2,
    "last_id": "bnVсbA=="
  }
}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

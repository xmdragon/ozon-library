# 在促销活动自动添加列表中添加或更新商品

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v2/actions/auto-add/products/update`
- Operation ID：`ActionsAutoAddProductsUpdateV2`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/#operation/ActionsAutoAddProductsUpdateV2
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

| 字段 | 类型/说明 |
| --- | --- |
| `Client-Id` required | string 用户识别号。 |
| `Api-Key` required | string API-密钥。 |

### 表格 1

| 字段 | 类型/说明 |
| --- | --- |
| `action_id` required | integer <uint64> 促销活动标识符。 |
| `auto_add_date` required | string <date-time> 方法 /v1/actions 响应中 result.auto_add_dates 参数里的商品自动添加到促销活动中的日期和时间。 |
| `products` required | Array of objects [ 1 .. 1000 ] items 需要添加到自动添加中或在自动添加中更新的商品列表。 |

### 表格 2

| 字段 | 类型/说明 |
| --- | --- |
| `below_min_price` | Array of objects 价格低于最低价格的商品列表。 |
| `deactivated_ids` | Array of strings <uint64> 已移出促销活动的商品ID。 |
| `extremely_low_price` | Array of objects 折扣幅度超过70%的商品列表。 |
| `failed_price` | Array of objects 未通过价格校验的商品列表。 |
| `product_ids` | Array of strings <uint64> 已成功添加或更新的商品ID。 |
| `rejected` | Array of objects 未能添加或更新的商品ID。 |
| `warnings` | Array of objects 商品警告列表。 |

## 示例

### 示例 0

```json
{
  "action_id": 250204,
  "auto_add_date": "2026-09-22T11:37:38.940Z",
  "products": [
    {
      "action_price": {
        "amount": "1000",
        "currency": "RUB"
      },
      "id": 88888,
      "stock": 10
    }
  ]
}
```

### 示例 1

```json
{
  "product_ids": [
    "    88888  "
  ],
  "deactivated_ids": [
    0
  ],
  "rejected": [
    {
      "product_id": 0,
      "reason": ""
    }
  ],
  "warnings": [
    {
      "product_id": 0,
      "reason": ""
    }
  ],
  "below_min_price": {
    "key": 0,
    "value": ""
  },
  "extremely_low_price": {
    "key": 0,
    "value": ""
  },
  "failed_price": {
    "key": 0,
    "value": ""
  }
}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

# 将商品加入促销活动或更新商品

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/actions/products/update`
- Operation ID：`ActionsProductsUpdate`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/#operation/ActionsProductsUpdate
- 分组：`actions`

## 页面标题结构

- 将商品加入促销活动或更新商品
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
| `action_id` required | integer <uint64> 促销活动标识符。可通过方法 /v1/actions 获取。 |
| `products` required | Array of objects <= 1000 items 商品列表。 |

### 表格 2

| 字段 | 类型/说明 |
| --- | --- |
| `active_product_ids` | Array of strings <uint64> 已加入促销活动的商品ID列表。 |
| `deactivated_product_ids` | Array of strings <uint64> 已移出促销活动的商品ID列表。 |
| `rejected` | Array of objects 未能加入促销活动的商品列表。 |
| `warnings` | Array of objects 关于商品被移出促销活动的原因信息。 |

## 示例

### 示例 0

```json
{
  "action_id": 258568,
  "products": [
    {
      "action_price": {
        "amount": "88",
        "currency": "RUB"
      },
      "product_id": 88888,
      "stock": "8"
    }
  ]
}
```

### 示例 1

```json
{
  "active_product_ids": [
    88888
  ],
  "deactivated_product_ids": [],
  "rejected": [],
  "warnings": []
}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

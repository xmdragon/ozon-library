# 获取促销活动可用商品列表

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/seller-actions/products/candidates`
- Operation ID：`SellerActionsProductsCandidates`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/SellerActionsProductsCandidates
- 分组：`seller-actions`

## 页面标题结构

- 获取促销活动可用商品列表
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
| `action_id` required | integer <uint64> 促销活动标识符。请通过方法/v1/seller-actions/list获取该参数的值。 |
| `cursor` | integer <uint64> 用于选择下一批数据的指针。 |
| `limit` required | integer <int64> [ 1 .. 100 ] Default: 100 响应中的最大元素数量。 |

### 表格 2

| 字段 | 类型/说明 |
| --- | --- |
| `cursor` | integer <uint64> 用于选择下一批数据的指针。 |
| `has_next` | boolean 响应中仅返回了部分值的标志： true——请使用新的cursor参数重复请求，以获取其余值； false——响应中已包含所有值。 |
| `products` | Array of objects 商品信息。 |

## 示例

### 示例 0

```text
true
```

### 示例 1

```text
cursor
```

### 示例 2

```text
false
```

### 示例 3

```json
{
  "action_id": 0,
  "cursor": 0,
  "limit": 100
}
```

### 示例 4

```json
{
  "cursor": 0,
  "has_next": true,
  "products": [
    {
      "action_price": 0,
      "base_price": 0,
      "currency": "string",
      "discount_percent": 0,
      "is_active": true,
      "min_seller_price": 0,
      "name": "string",
      "offer_id": "string",
      "price": 0,
      "product_id": 0,
      "quant_size": 0,
      "quant_type": "UNSPECIFIED",
      "sku": [
        "string"
      ]
    }
  ]
}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

# 订阅该商品的用户数

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/product/info/subscription`
- Operation ID：`ProductAPI_GetProductInfoSubscription`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/ProductAPI_GetProductInfoSubscription
- 分组：`product`

## 页面标题结构

- 订阅该商品的用户数
- Request Body schema: application/json
- 回复
- Response Schema: application/json
- 请求范例
- 回复范例

## 参数与返回结构

### 表格 0

| 字段 | 类型/说明 |
| --- | --- |
| `skus` required | Array of strings <int64> Ozon 系统中的 SKU、商品标识符列表。 |

### 表格 1

| 字段 | 类型/说明 |
| --- | --- |
| `result` | Array of objects 操作方法结果。 |
| `count` | integer <int64> 订阅用户的数量。 |
| `sku` | integer <int64> Ozon 系统中的商品ID、SKU。 |

### 表格 2

| 字段 | 类型/说明 |
| --- | --- |
| `count` | integer <int64> 订阅用户的数量。 |
| `sku` | integer <int64> Ozon 系统中的商品ID、SKU。 |

## 示例

### 示例 0

```json
{
  "skus": [
    "889283932",
    "123456789",
    "987654321"
  ]
}
```

### 示例 1

```json
{
  "result": [
    {
      "count": 3,
      "sku": 889283932
    }
  ]
}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

# 从存档删除没有SKU的商品

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v2/products/delete`
- Operation ID：`ProductAPI_DeleteProducts`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/ProductAPI_DeleteProducts
- 分组：`products`

## 页面标题结构

- 从存档删除没有SKU的商品
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
| `products` required | Array of objects Ozon系统中商品的标识符 — product_id。 |

### 表格 2

| 字段 | 类型/说明 |
| --- | --- |
| `status` | Array of objects 请求的处理情况。 |
| `error` | string 处理该请求时发生错误的原因。 |
| `is_deleted` | boolean 如果查询的执行没有错误且商品被删除 —— true。 |
| `offer_id` | string 卖家系统中的商品识别码是卖家系统中的商品标识符是商品货号。 |

### 表格 3

| 字段 | 类型/说明 |
| --- | --- |
| `error` | string 处理该请求时发生错误的原因。 |
| `is_deleted` | boolean 如果查询的执行没有错误且商品被删除 —— true。 |
| `offer_id` | string 卖家系统中的商品识别码是卖家系统中的商品标识符是商品货号。 |

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
  "products": [
    {
      "offer_id": "033"
    }
  ]
}
```

### 示例 3

```json
{
  "status": [
    {
      "offer_id": "033",
      "is_deleted": true,
      "error": ""
    }
  ]
}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

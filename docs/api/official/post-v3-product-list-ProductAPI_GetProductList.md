# 品列表的

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v3/product/list`
- Operation ID：`ProductAPI_GetProductList`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/ProductAPI_GetProductList
- 分组：`product`

## 页面标题结构

- 品列表的
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
| `filter` | object 商品过滤。 |
| `last_id` | string 页面上最后一个值的ID。运行第一个查询时，将此字段留空。 要检索以下数值，请从上一个查询的响应中指定 last_id。 |
| `limit` | integer <int64> 答复的信息数量。默认设置为1。最大值是1000。 |

### 表格 2

| 字段 | 类型/说明 |
| --- | --- |
| `result` | object 结果。 |
| `items` | Array of objects 品列表的。 |
| `last_id` | string 页面上最后一个值的ID。 要检索以下数值，请从上一个查询的响应中指定 last_id。 |
| `total` | integer <int32> 品牌总数。 |

### 表格 3

| 字段 | 类型/说明 |
| --- | --- |
| `items` | Array of objects 品列表的。 |
| `last_id` | string 页面上最后一个值的ID。 要检索以下数值，请从上一个查询的响应中指定 last_id。 |
| `total` | integer <int32> 品牌总数。 |

## 示例

### 示例 0

```text
offer_id
```

### 示例 1

```text
product_id
```

### 示例 2

```text
limit
```

### 示例 3

```text
last_id
```

### 示例 4

```text
last_id
```

### 示例 5

```text
last_id
```

### 示例 6

```json
{
  "filter": {
    "offer_id": [
      "136748"
    ],
    "product_id": [
      "223681945"
    ],
    "visibility": "ALL"
  },
  "last_id": "",
  "limit": 100
}
```

### 示例 7

```json
{
  "result": {
    "items": [
      {
        "product_id": 3397917680,
        "offer_id": "2026-01-13 16:56:03 PDF",
        "has_fbo_stocks": false,
        "has_fbs_stocks": false,
        "archived": false,
        "is_discounted": false,
        "quants": []
      }
    ],
    "total": 1,
    "last_id": "WzMzOTc5MTc2ODAsMzM5NzkxNzY4MF0="
  }
}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

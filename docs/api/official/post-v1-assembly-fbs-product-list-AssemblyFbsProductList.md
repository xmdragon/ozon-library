# 获取货件中的商品列表

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/assembly/fbs/product/list`
- Operation ID：`AssemblyFbsProductList`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/AssemblyFbsProductList
- 分组：`assembly`

## 页面标题结构

- 获取货件中的商品列表
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
| `filter` required | object 筛选器。 |
| `limit` required | integer <int64> <= 1000 每页显示的数量。 |
| `offset` | integer <int64> 在响应中将被跳过的项目数量。例如，如果 offset = 10，则响应将从第 11 个找到的项目开始。 |
| `sort_dir` | string Enum: "ASC" "DESC" 排序方向： ASC——升序， DESC——降序。 |

### 表格 2

| 字段 | 类型/说明 |
| --- | --- |
| `has_next` | boolean 响应中是否包含全部商品： true——请使用新的 offset值重新请求以获取剩余数据； false——响应中已包含所有值。 |
| `products` | Array of objects 商品列表。 |
| `products_count` | integer <int32> 商品数量。 |

## 示例

### 示例 0

```text
offset = 10
```

### 示例 1

```text
ASC
```

### 示例 2

```text
DESC
```

### 示例 3

```text
true
```

### 示例 4

```text
offset
```

### 示例 5

```text
false
```

### 示例 6

```json
{
  "filter": {
    "cutoff_from": "2019-08-24T14:15:22Z",
    "cutoff_to": "2019-08-24T14:15:22Z",
    "delivery_method_id": 0
  },
  "limit": 0,
  "offset": 0,
  "sort_dir": "ASC"
}
```

### 示例 7

```json
{
  "products": [
    {
      "sku": 1000123456,
      "offer_id": "test-offer-123456",
      "product_name": "string",
      "picture_url": "https://test-example.com/images/product-123456.jpg",
      "quantity": 15,
      "postings": [
        {
          "posting_number": "789456123-0002-3",
          "quantity": 2
        },
        {
          "posting_number": "123456789-0001-1",
          "quantity": 3
        },
        {
          "posting_number": "456123789-0003-5",
          "quantity": 1
        }
      ]
    },
    {
      "sku": 1000123457,
      "offer_id": "test-offer-123457",
      "product_name": "string",
      "picture_url": "https://test-example.com/images/product-123457.jpg",
      "quantity": 8,
      "postings": [
        {
          "posting_number": "321654987-0004-2",
          "quantity": 2
        },
        {
          "posting_number": "987321654-0005-7",
          "quantity": 1
        },
        {
          "posting_number": "789456123-0006-8",
          "quantity": 3
        },
        {
          "posting_number": "123456789-0007-9",
          "quantity": 2
        }
      ]
    },
    {
      "sku": 1000123458,
      "offer_id": "test-offer-123458",
      "product_name": "string",
      "picture_url": "https://test-example.com/images/product-123458.jpg",
      "quantity": 23,
      "postings": [
        {
          "posting_number": "456123789-0008-1",
          "quantity": 5
        },
        {
          "posting_number": "321654987-0009-3",
          "quantity": 4
        },
        {
          "posting_number": "987321654-0010-2",
          "quantity": 3
        },
        {
          "posting_number": "789456123-0011-4",
          "quantity": 6
        },
        {
          "posting_number": "123456789-0012-6",
          "quantity": 5
        }
      ]
    },
    {
      "sku": 1000123459,
      "offer_id": "test-offer-123459",
      "product_name": "string",
      "picture_url": "https://test-example.com/images/product-123459.jpg",
      "quantity": 5,
      "postings": [
        {
          "posting_number": "456123789-0013-8",
          "quantity": 2
        },
        {
          "posting_number": "321654987-0014-1",
          "quantity": 3
        }
      ]
    },
    {
      "sku": 1000123460,
      "offer_id": "test-offer-123460",
      "product_name": "string",
      "picture_url": "https://test-example.com/images/product-123460.jpg",
      "quantity": 12,
      "postings": [
        {
          "posting_number": "987321654-0015-3",
          "quantity": 4
        },
        {
          "posting_number": "789456123-0016-5",
          "quantity": 3
        },
        {
          "posting_number": "123456789-0017-7",
          "quantity": 5
        }
      ]
    }
  ],
  "products_count": 5,
  "has_next": true
}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

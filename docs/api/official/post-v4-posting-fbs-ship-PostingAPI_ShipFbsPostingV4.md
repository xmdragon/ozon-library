# 搜集订单 (第4方案)

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v4/posting/fbs/ship`
- Operation ID：`PostingAPI_ShipFbsPostingV4`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/PostingAPI_ShipFbsPostingV4
- 分组：`posting`

## 页面标题结构

- 搜集订单 (第4方案)
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
| `packages` required | Array of objects 包装清单。 每个包装都包含订单分成的发货清单。 |
| `posting_number` required | string 发货号。 |
| `with` | object 附加信息。 |

### 表格 2

| 字段 | 类型/说明 |
| --- | --- |
| `additional_data` | Array of objects 与发货有关的附加信息。 |
| `result` | Array of strings 货运装配结果。 |

## 示例

### 示例 0

```text
awaiting_deliver
```

### 示例 1

```text
packages
```

### 示例 2

```text
products
```

### 示例 3

```text
products
```

### 示例 4

```text
packages
```

### 示例 5

```json
{
  "packages": [
    {
      "products": [
        {
          "product_id": 185479045,
          "quantity": 2
        }
      ]
    }
  ],
  "posting_number": "89491381-0072-1"
}
```

### 示例 6

```json
{
  "packages": [
    {
      "products": [
        {
          "product_id": 185479045,
          "quantity": 2
        }
      ]
    }
  ],
  "posting_number": "89491381-0072-1"
}
```

### 示例 7

```json
{
  "packages": [
    {
      "products": [
        {
          "product_id": 185479045,
          "quantity": 1
        }
      ]
    },
    {
      "products": [
        {
          "product_id": 185479045,
          "quantity": 1
        }
      ]
    }
  ],
  "posting_number": "89491381-0072-1"
}
```

### 示例 8

```json
{
  "packages": [
    {
      "products": [
        {
          "product_id": 185479045,
          "quantity": 1
        }
      ]
    },
    {
      "products": [
        {
          "product_id": 185479045,
          "quantity": 1
        }
      ]
    }
  ],
  "posting_number": "89491381-0072-1"
}
```

### 示例 9

```json
{
  "packages": [
    {
      "products": [
        {
          "product_id": 185479045,
          "quantity": 1
        }
      ]
    }
  ],
  "posting_number": "89491381-0072-1",
  "with": {
    "additional_data": true
  }
}
```

### 示例 10

```json
{
  "additional_data": [
    {
      "posting_number": "89491381-0072-1",
      "products": [
        {
          "currency_code": "RUB",
          "mandatory_mark": [
            "123"
          ],
          "name": "string",
          "offer_id": "17125",
          "price": "2000",
          "quantity": 1,
          "sku": 149618972
        }
      ]
    }
  ],
  "result": [
    "89491381-0072-1"
  ]
}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

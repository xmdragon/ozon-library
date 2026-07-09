# 单据中的货件列表

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v2/posting/fbs/act/get-postings`
- Operation ID：`PostingAPI_ActPostingList`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/PostingAPI_ActPostingList
- 分组：`posting`

## 页面标题结构

- 单据中的货件列表
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
| `id` required | int <int64> 单据标识符。请通过方法/v1/carriage/create获取参数值。 |

### 表格 2

| 字段 | 类型/说明 |
| --- | --- |
| `result` | Array of objects 货件信息。 |
| `id` | integer <int64> 单据标识符。 |
| `multi_box_qty` | integer <int32> 商品包装所用箱数。 |
| `posting_number` | string 货件编号。 |
| `status` | string 货件状态。 |
| `seller_error` | string 错误代码说明。 |
| `updated_at` | string <date-time> 货件记录的更新日期和时间。 |
| `created_at` | string <date-time> 货件记录的创建日期和时间。 |
| `products` | Array of objects 货件中商品列表。 |

### 表格 3

| 字段 | 类型/说明 |
| --- | --- |
| `id` | integer <int64> 单据标识符。 |
| `multi_box_qty` | integer <int32> 商品包装所用箱数。 |
| `posting_number` | string 货件编号。 |
| `status` | string 货件状态。 |
| `seller_error` | string 错误代码说明。 |
| `updated_at` | string <date-time> 货件记录的更新日期和时间。 |
| `created_at` | string <date-time> 货件记录的创建日期和时间。 |
| `products` | Array of objects 货件中商品列表。 |

## 示例

### 示例 0

```json
{
  "id": 900000250859000
}
```

### 示例 1

```json
{
  "result": [
    {
      "id": 0,
      "multi_box_qty": 0,
      "posting_number": "string",
      "status": "string",
      "seller_error": "string",
      "updated_at": "2019-08-24T14:15:22Z",
      "created_at": "2019-08-24T14:15:22Z",
      "products": [
        {
          "name": "string",
          "offer_id": "string",
          "price": "string",
          "quantity": 0,
          "sku": 0
        }
      ]
    }
  ]
}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

# 按条形码获取有关货件的信息

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v2/posting/fbs/get-by-barcode`
- Operation ID：`PostingAPI_GetFbsPostingByBarcode`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/PostingAPI_GetFbsPostingByBarcode
- 分组：`posting`

## 页面标题结构

- 按条形码获取有关货件的信息
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
| `barcode` required | string 货运条形码。可以使用以下方法获取： /v3/posting/fbs/get、/v3/posting/fbs/list 和 /v3/posting/fbs/unfulfilled/list， 在barcodes数组中获取数据。 |

### 表格 2

| 字段 | 类型/说明 |
| --- | --- |
| `result` | object 请求结果。 |
| `barcodes` | object 货件条形码。 |
| `cancel_reason_id` | integer <int64> 取消装运原因ID。 |
| `created_at` | string <date-time> 创建装运日期和时间。 |
| `in_process_at` | string <date-time> 开始处理货件的日期和时间。 |
| `order_id` | integer <int64> 货运所属订单ID。 |
| `order_number` | string 货运所属的订单号。 |
| `posting_number` | string 货运号。 |
| `products` | Array of objects 货运商品列表。 |
| `shipment_date` | string <date-time> 必须收取货件的日期和时间。 如果在此日期之前未完成配货，则货运自动取消。 |
| `status` | string 货运状态。 |

### 表格 3

| 字段 | 类型/说明 |
| --- | --- |
| `barcodes` | object 货件条形码。 |
| `cancel_reason_id` | integer <int64> 取消装运原因ID。 |
| `created_at` | string <date-time> 创建装运日期和时间。 |
| `in_process_at` | string <date-time> 开始处理货件的日期和时间。 |
| `order_id` | integer <int64> 货运所属订单ID。 |
| `order_number` | string 货运所属的订单号。 |
| `posting_number` | string 货运号。 |
| `products` | Array of objects 货运商品列表。 |
| `shipment_date` | string <date-time> 必须收取货件的日期和时间。 如果在此日期之前未完成配货，则货运自动取消。 |
| `status` | string 货运状态。 |

## 示例

### 示例 0

```text
barcodes
```

### 示例 1

```json
{
  "barcode": "20325804886000"
}
```

### 示例 2

```json
{
  "result": {
    "order_id": 47558522075,
    "order_number": "2130415463-0013",
    "posting_number": "2130415463-0013-1",
    "status": "delivered",
    "cancel_reason_id": 0,
    "created_at": "2025-01-29T08:58:07Z",
    "in_process_at": "2025-01-29T08:59:40Z",
    "shipment_date": "2025-01-29T18:00:00Z",
    "products": [
      {
        "sku": 498274975,
        "name": "",
        "quantity": 1,
        "offer_id": "6460551001",
        "price": "2300.0000"
      }
    ],
    "barcodes": {
      "upper_barcode": "%101%10293145035",
      "lower_barcode": "201864523528000"
    }
  }
}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

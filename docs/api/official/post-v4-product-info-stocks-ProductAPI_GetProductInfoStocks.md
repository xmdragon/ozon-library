# 关于商品数量的信息

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v4/product/info/stocks`
- Operation ID：`ProductAPI_GetProductInfoStocks`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/ProductAPI_GetProductInfoStocks
- 分组：`product`

## 页面标题结构

- 关于商品数量的信息
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
| `cursor` | string 后续数据的选择标志。 |
| `filter` required | object 商品筛选器。 |
| `limit` required | integer <int32> 页面上的值数量。最低为1，最高为1000。 |

### 表格 2

| 字段 | 类型/说明 |
| --- | --- |
| `cursor` | string 后续数据的选择标志。 |
| `items` | Array of objects 商品信息。 |
| `total` | integer <int32> 显示库存信息的独特商品数量。 |

## 示例

### 示例 0

```json
{
  "cursor": "",
  "filter": {
    "offer_id": [
      "1233213232"
    ],
    "product_id": [
      "313455276"
    ],
    "visibility": "ALL",
    "with_quant": {
      "created": true,
      "exists": true
    }
  },
  "limit": 100
}
```

### 示例 1

```json
{
  "items": [
    {
      "offer_id": "test-offer-123456",
      "product_id": 1000123456,
      "stocks": [
        {
          "sku": 1000123456,
          "type": "fbs",
          "present": 150,
          "reserved": 25,
          "shipment_type": "SHIPMENT_TYPE_GENERAL"
        },
        {
          "sku": 1000123456,
          "type": "fbo",
          "present": 75,
          "reserved": 10,
          "shipment_type": "SHIPMENT_TYPE_GENERAL"
        }
      ]
    },
    {
      "offer_id": "test-offer-123457",
      "product_id": 1000123457,
      "stocks": [
        {
          "sku": 1000123457,
          "type": "fbs",
          "present": 45,
          "reserved": 5,
          "shipment_type": "SHIPMENT_TYPE_BOX"
        }
      ]
    }
  ],
  "cursor": "next-cursor-12345",
  "total": 2
}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

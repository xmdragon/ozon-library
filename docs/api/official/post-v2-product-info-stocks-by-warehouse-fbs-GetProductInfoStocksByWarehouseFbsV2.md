# 获取卖家仓库库存信息

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v2/product/info/stocks-by-warehouse/fbs`
- Operation ID：`GetProductInfoStocksByWarehouseFbsV2`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/GetProductInfoStocksByWarehouseFbsV2
- 分组：`product`

## News 更新标记

| 日期 | 标记 | 摘要 | 来源 |
| --- | --- | --- | --- |
| 2026-05-14 | `new_method` | /v2/product/info/stocks-by-warehouse/fbs 新增了用于处理卖家仓库库存的方法。 | [官方 News](https://docs.ozon.ru/api/seller/zh/#section/2026514) |

## 页面标题结构

- 获取卖家仓库库存信息
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
| `limit` required | integer <uint64> <= 1000 响应中返回的值数量。 |
| `offer_id` | Array of strings <= 1000 items 卖家系统中的商品识别码是卖家系统中的商品标识符是商品货号。 |
| `sku` required | Array of strings <int64> <= 1000 items Ozon系统中的商品标识符——SKU。 |

### 表格 2

| 字段 | 类型/说明 |
| --- | --- |
| `cursor` | string 用于获取下一批数据的指针。 |
| `has_next` | boolean 如果响应中未返回所有商品，则为true。 |
| `products` | Array of objects 商品库存。 |

## 示例

### 示例 0

```text
true
```

### 示例 1

```json
{
  "cursor": "string",
  "limit": 0,
  "offer_id": [
    "string"
  ],
  "sku": [
    "string"
  ]
}
```

### 示例 2

```json
{
  "cursor": "string",
  "has_next": true,
  "products": [
    {
      "free_stock": 0,
      "offer_id": "string",
      "present": 0,
      "product_id": 0,
      "reserved": 0,
      "sku": 0,
      "warehouse_id": 0,
      "warehouse_name": "string"
    }
  ]
}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

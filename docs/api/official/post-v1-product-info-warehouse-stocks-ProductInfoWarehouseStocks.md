# 获取FBS和rFBS仓库库存信息

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/product/info/warehouse/stocks`
- Operation ID：`ProductInfoWarehouseStocks`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/ProductInfoWarehouseStocks
- 分组：`product`

## 页面标题结构

- 获取FBS和rFBS仓库库存信息
- Request Body schema: application/json
- 回复
- Response Schema: application/json
- 请求范例
- 回复范例

## 参数与返回结构

### 表格 0

| 字段 | 类型/说明 |
| --- | --- |
| `cursor` | string 用于选择下一批数据的指针。 |
| `limit` required | integer <int64> [ 1 .. 1000 ] 每页显示的数量。 |
| `warehouse_id` required | integer <int64> 仓库标识符。 |

### 表格 1

| 字段 | 类型/说明 |
| --- | --- |
| `cursor` | string 用于选择下一批数据的指针。 如果该参数为空，则没有更多数据了。 |
| `has_next` | boolean 标记是否返回了所有商品： true——请使用不同的cursor值重新请求，以获取剩余的值； false——响应中已包含所有值。 |
| `stocks` | Array of objects 商品库存信息。 |

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
  "cursor": "",
  "limit": 10,
  "warehouse_id": 1020003080073000
}
```

### 示例 4

```json
{
  "stocks": [
    {
      "sku": 147035011,
      "product_id": 28743,
      "offer_id": "02105020-35",
      "warehouse_id": 1020003080073000,
      "present": 1000,
      "reserved": 0,
      "free_stock": 1000,
      "updated_at": "2025-09-15T10:36:24.417498Z"
    }
  ],
  "has_next": false,
  "cursor": "147035011"
}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

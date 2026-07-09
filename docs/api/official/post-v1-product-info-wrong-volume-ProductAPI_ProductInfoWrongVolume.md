# 体积重量特征不正确的商品列表

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/product/info/wrong-volume`
- Operation ID：`ProductAPI_ProductInfoWrongVolume`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/ProductAPI_ProductInfoWrongVolume
- 分组：`product`

## News 更新标记

| 日期 | 标记 | 摘要 | 来源 |
| --- | --- | --- | --- |
| 2026-05-05 | `updated` | /v1/product/info/wrong-volume 更新了方法描述。 | [官方 News](https://docs.ozon.ru/api/seller/zh/#section/202655) |
| 2025-03-26 | `new_method` | /v1/product/info/wrong-volume 我们已为获取体积重量特征不正确的商品的列表添加了Beta方法。 | [官方 News](https://docs.ozon.ru/api/seller/zh/#section/2025326) |

## 页面标题结构

- 体积重量特征不正确的商品列表
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
| `cursor` | string 用于获取下一批数据的指针。 |
| `limit` required | integer <int64> [ 1 .. 1000 ] 响应中记录数量的限制。 |

### 表格 2

| 字段 | 类型/说明 |
| --- | --- |
| `cursor` | string 用于获取下一批数据的指针。 |
| `products` | Array of objects 商品列表。 |

## 示例

### 示例 0

```json
{
  "cursor": "",
  "limit": 1000
}
```

### 示例 1

```json
{
  "cursor": "string",
  "products": [
    {
      "height": 0,
      "length": 0,
      "name": "string",
      "offer_id": "string",
      "product_id": 0,
      "sku": 0,
      "weight": 0,
      "width": 0
    }
  ]
}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

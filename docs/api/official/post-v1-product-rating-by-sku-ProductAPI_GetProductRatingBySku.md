# 按SKU获得商品的内容排名

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/product/rating-by-sku`
- Operation ID：`ProductAPI_GetProductRatingBySku`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/ProductAPI_GetProductRatingBySku
- 分组：`product`

## 页面标题结构

- 按SKU获得商品的内容排名
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
| `skus` required | Array of strings <int64> 需要返回内容评级的商品SKU列表。 |

### 表格 2

| 字段 | 类型/说明 |
| --- | --- |
| `products` | Array of objects 商品内容分级。 |
| `sku` | integer <int64> Ozon 系统中的商品标识符（SKU）。 |
| `rating` | number <float> 产品内容评级: 从0到100。 |
| `groups` | Array of objects 构成内容评级的各组特征。 |

### 表格 3

| 字段 | 类型/说明 |
| --- | --- |
| `sku` | integer <int64> Ozon 系统中的商品标识符（SKU）。 |
| `rating` | number <float> 产品内容评级: 从0到100。 |
| `groups` | Array of objects 构成内容评级的各组特征。 |

## 示例

### 示例 0

```json
{
  "skus": [
    "179737222"
  ]
}
```

### 示例 1

```json
{
  "products": [
    {
      "sku": 179737222,
      "rating": 42.5,
      "groups": [
        {
          "key": "media",
          "name": "媒体",
          "rating": 70,
          "weight": 25,
          "conditions": [
            {
              "key": "media_images_2",
              "description": "已添加2张图片",
              "fulfilled": true,
              "cost": 50
            },
            {
              "key": "media_video",
              "description": "已添加视频",
              "fulfilled": false,
              "cost": 15
            }
          ],
          "improve_attributes": [
            {
              "id": 4074,
              "name": "视频码"
            }
          ],
          "improve_at_least": 2
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

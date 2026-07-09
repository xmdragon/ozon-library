# 上传或更新商品图片

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/product/pictures/import`
- Operation ID：`ProductAPI_ProductImportPictures`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/ProductAPI_ProductImportPictures
- 分组：`product`

## 页面标题结构

- 上传或更新商品图片
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
| `color_image` | string 市场营销色彩。 |
| `images` | Array of strings 数组图片链接。 最多30件。 数组中的图像是按照它们在网站上出现的顺序排列的。 数组中的第一个图像将是主图像。 |
| `images360` | Array of strings 360图片的数组。多达70张图片。 格式：公共云存储中的图像链接地址。链接图片的格式是JPG。 |
| `product_id` required | integer <int64> Ozon系统中商品的标识符 — product_id。 |

### 表格 2

| 字段 | 类型/说明 |
| --- | --- |
| `result` | object 该方法的结果。 |
| `pictures` | Array of objects |

### 表格 3

| 字段 | 类型/说明 |
| --- | --- |
| `pictures` | Array of objects |

## 示例

### 示例 0

```text
images
```

### 示例 1

```text
images360
```

### 示例 2

```text
color_image
```

### 示例 3

```text
images
```

### 示例 4

```text
images360
```

### 示例 5

```text
color_image
```

### 示例 6

```text
result.items.status
```

### 示例 7

```text
skipped
```

### 示例 8

```text
429
```

### 示例 9

```text
message
```

### 示例 10

```text
Item-Retry-After
```

### 示例 11

```text
Item-Rate-Limit-Remaining
```

### 示例 12

```text
product_id
```

### 示例 13

```json
{
  "color_image": "https://example.com/cloud-storage/color/marketing-color-red.jpg",
  "images": [
    "https://example.com/cloud-storage/images/main-image-front.jpg",
    "https://example.com/cloud-storage/images/secondary-image-side.jpg",
    "https://example.com/cloud-storage/images/secondary-image-back.jpg",
    "https://example.com/cloud-storage/images/secondary-image-detail1.jpg",
    "https://example.com/cloud-storage/images/secondary-image-detail2.jpg"
  ],
  "images360": [
    "https://example.com/cloud-storage/images360/360-view-001.jpg",
    "https://example.com/cloud-storage/images360/360-view-002.jpg",
    "https://example.com/cloud-storage/images360/360-view-003.jpg",
    "https://example.com/cloud-storage/images360/360-view-004.jpg",
    "https://example.com/cloud-storage/images360/360-view-005.jpg"
  ],
  "product_id": 123456789
}
```

### 示例 14

```json
{
  "result": {
    "pictures": [
      {
        "is_360": true,
        "is_color": true,
        "is_primary": true,
        "product_id": 123456789,
        "state": "uploaded",
        "url": "https://example.com/cloud-storage/images360/360-view-001.jpg"
      }
    ]
  }
}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

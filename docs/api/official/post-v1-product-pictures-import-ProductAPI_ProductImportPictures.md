# 上传或更新商品图片 Deprecated

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

> [!WARNING]
> 官方 News 标记此方法为 `deprecated`，日期：2026-09-03。替代方法：`/v2/product/pictures/import`。 官方 News：https://docs.ozon.ru/api/seller/zh/#section/202693
> News 原文摘要：/v1/product/pictures/import 该方法即将弃用，将于2026年10月1日停用。请切换到/v2/product/pictures/import。

## 方法

- 请求：`POST /v1/product/pictures/import`
- Operation ID：`ProductAPI_ProductImportPictures`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/#operation/ProductAPI_ProductImportPictures
- 分组：`product`

## News 更新标记

| 日期 | 标记 | 摘要 | 来源 |
| --- | --- | --- | --- |
| 2026-09-03 | `deprecated_method` | /v1/product/pictures/import 该方法即将弃用，将于2026年10月1日停用。请切换到/v2/product/pictures/import。 | [官方 News](https://docs.ozon.ru/api/seller/zh/#section/202693) |
| 2026-07-10 | `removed_field` | /v1/product/pictures/import 已从方法请求中删除了images360参数。
已从方法响应中删除了result.pictures.is_360参数。
更新了方法描述。 | [官方 News](https://docs.ozon.ru/api/seller/zh/#section/2026710) |
| 2026-05-12 | `updated` | /v1/product/pictures/import 已更新方法说明。 | [官方 News](https://docs.ozon.ru/api/seller/zh/#section/2026512) |
| 2026-05-05 | `updated` | /v1/product/pictures/import 更新了方法描述。 | [官方 News](https://docs.ozon.ru/api/seller/zh/#section/202655) |
| 2025-10-08 | `updated` | /v1/product/pictures/import 更新了该方法请求中参数 images 的描述。
更新了方法描述。 | [官方 News](https://docs.ozon.ru/api/seller/zh/#section/2025108) |

## 页面标题结构

- 上传或更新商品图片 Deprecated
- HEADER PARAMETERS
- REQUEST BODY SCHEMA: application/json
- 回复
- RESPONSE SCHEMA: application/json
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
| `product_id` required | integer <int64> Ozon系统中商品的标识符 — product_id。 |

### 表格 2

| 字段 | 类型/说明 |
| --- | --- |
| `result` | object 该方法的结果。 |

### 表格 3

| 字段 | 类型/说明 |
| --- | --- |
| `pictures` | Array of objects |

## 示例

### 示例 0

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
  "product_id": 123456789
}
```

### 示例 1

```json
{
  "result": {
    "pictures": [
      {
        "is_color": true,
        "is_primary": true,
        "product_id": 123456789,
        "state": "uploaded",
        "url": ""
      }
    ]
  }
}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

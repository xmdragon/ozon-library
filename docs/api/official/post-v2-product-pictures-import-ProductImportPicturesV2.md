# 上传或更新商品图片

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v2/product/pictures/import`
- Operation ID：`ProductImportPicturesV2`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/#operation/ProductImportPicturesV2
- 分组：`product`

## News 更新标记

| 日期 | 标记 | 摘要 | 来源 |
| --- | --- | --- | --- |
| 2026-09-03 | `new_method` | /v2/product/pictures/import 新增了商品图片上传或更新方法的新版本。 | [官方 News](https://docs.ozon.ru/api/seller/zh/#section/202693) |

## 页面标题结构

- 上传或更新商品图片
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
| `items` | Array of objects <= 100 items 商品信息。 |

### 表格 2

| 字段 | 类型/说明 |
| --- | --- |
| `offer_id` required | string 卖家系统中的商品标识符——货号。 |
| `primary_image` | string 商品主图。 |
| `color_image` | string 营销颜色。 |
| `images` | Array of strings <= 30 items 图片链接列表。 数组中的图片按其在网站上的显示顺序排列。如果请求中未传递primary_image，数组中的第一张图片将成为主图。 |

### 表格 3

| 字段 | 类型/说明 |
| --- | --- |
| `task_id` | integer <int64> 任务标识符。要检查图片状态，请将获取的值传递到方法/v1/product/import/info。 |

## 示例

### 示例 0

```json
{
  "items": [
    {
      "offer_id": "PROD-2023-001",
      "primary_image": "https://example.com/cloud-storage/images/main-image-front.jpg",
      "color_image": "",
      "images": []
    }
  ]
}
```

### 示例 1

```json
{
  "task_id": 0
}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

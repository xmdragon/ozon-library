# 检查合作伙伴仓库商品列表

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/fbp/draft/direct/product/validate`
- Operation ID：`FbpDraftDirectProductValidate`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/FbpDraftDirectProductValidate
- 分组：`fbp`

## 页面标题结构

- 检查合作伙伴仓库商品列表
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
| `skus` required | Array of objects 商品标识符（SKU）列表。 |
| `warehouse_id` required | integer <int64> 仓库标识符。 |

### 表格 2

| 字段 | 类型/说明 |
| --- | --- |
| `approved_items` | Array of objects 已确认商品。 |
| `bundle_generated` | boolean true，前提是已创建校验商品列表。 |
| `bundle_id` | string 校验商品列表标识符。 |
| `rejected_items` | Array of objects 被拒绝的商品。 |

## 示例

### 示例 0

```text
true
```

### 示例 1

```json
{
  "skus": [
    {
      "count": 0,
      "sku": 0
    }
  ],
  "warehouse_id": 0
}
```

### 示例 2

```json
{
  "approved_items": [
    {
      "barcode": "string",
      "icon_name": "string",
      "name": "string",
      "offer_id": "string",
      "quantity": 0,
      "sku": 0,
      "volume": 0
    }
  ],
  "bundle_generated": true,
  "bundle_id": "string",
  "rejected_items": [
    {
      "barcode": "string",
      "icon_name": "string",
      "name": "string",
      "offer_id": "string",
      "quantity": 0,
      "rejection_reasons": "BUNDLE_ITEM_ERROR_UNSPECIFIED",
      "sku": 0,
      "volume": 0
    }
  ]
}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

# 通过SKU创建商品

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/product/import-by-sku`
- Operation ID：`ProductAPI_ImportProductsBySKU`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/#operation/ProductAPI_ImportProductsBySKU
- 分组：`product`

## News 更新标记

| 日期 | 标记 | 摘要 | 来源 |
| --- | --- | --- | --- |
| 2026-07-10 | `updated` | /v1/product/import-by-sku 更新了方法描述。 | [官方 News](https://docs.ozon.ru/api/seller/zh/#section/2026710) |
| 2026-05-12 | `updated` | /v1/product/import-by-sku 已更新方法说明。 | [官方 News](https://docs.ozon.ru/api/seller/zh/#section/2026512) |
| 2026-02-12 | `updated` | /v1/product/import-by-sku 更新了方法描述。 | [官方 News](https://docs.ozon.ru/api/seller/zh/#section/2026212) |
| 2025-12-30 | `updated` | /v1/product/import-by-sku 更新了方法请求中的 items.vat 参数描述。 | [官方 News](https://docs.ozon.ru/api/seller/zh/#section/20251230) |
| 2025-05-06 | `removed_field` | /v1/product/import-by-sku 已从方法请求中移除参数 items.premium_price。 | [官方 News](https://docs.ozon.ru/api/seller/zh/#section/202556) |
| 2024-12-24 | `updated` | /v1/product/import-by-sku 更新了方法请求中参数 items.vat 的描述。 | [官方 News](https://docs.ozon.ru/api/seller/zh/#section/20241224) |

## 页面标题结构

- 通过SKU创建商品
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
| `items` | Array of objects <= 1000 items 商品信息。 |

### 表格 2

| 字段 | 类型/说明 |
| --- | --- |
| `result` | object |

### 表格 3

| 字段 | 类型/说明 |
| --- | --- |
| `task_id` | integer <int64> 进口货物任务代码。 |
| `unmatched_sku_list` | Array of integers <int64> 商品Id列表。 |

## 示例

### 示例 0

```json
{
  "items": [
    {
      "sku": 298789742,
      "name": "杯子",
      "offer_id": "91132",
      "currency_code": "RUB",
      "old_price": "2590",
      "price": "2300",
      "vat": "0.1"
    }
  ]
}
```

### 示例 1

```json
{
  "result": {
    "task_id": 176594213,
    "unmatched_sku_list": []
  }
}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

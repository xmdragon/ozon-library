# 获取商品价格信息

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v5/product/info/prices`
- Operation ID：`ProductAPI_GetProductInfoPrices`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/ProductAPI_GetProductInfoPrices
- 分组：`product`

## News 更新标记

| 日期 | 标记 | 摘要 | 来源 |
| --- | --- | --- | --- |
| 2026-05-28 | `updated` | /v5/product/info/prices 更新了方法响应中items.marketing_actions、items.marketing_actions.actions、items.marketing_actions.actions.date_from、items.marketing_actions.actions.date_to、items.marketing_actions.actions.title和items.marketing_actions.actions.value参数的说明。 | [官方 News](https://docs.ozon.ru/api/seller/zh/#section/2026528) |
| 2026-05-12 | `new_method` | /v5/product/info/prices 已新增方法描述。 | [官方 News](https://docs.ozon.ru/api/seller/zh/#section/2026512) |
| 2026-05-05 | `updated` | /v5/product/info/prices 更新了方法请求中参数 filter.visibility 的描述。 | [官方 News](https://docs.ozon.ru/api/seller/zh/#section/202655) |
| 2026-02-10 | `updated` | /v5/product/info/prices 更新了方法请求中参数 filter.visibility 的描述。 | [官方 News](https://docs.ozon.ru/api/seller/zh/#section/2026210) |
| 2025-12-25 | `updated` | /v5/product/info/prices 已更新方法响应中参数 items.price.retail_price 的说明。 | [官方 News](https://docs.ozon.ru/api/seller/zh/#section/20251225) |
| 2025-11-12 | `removed_field` | /v5/product/info/prices 在方法回答该price.marketing_price参数已过期，我们已将其从文件中删除。 | [官方 News](https://docs.ozon.ru/api/seller/zh/#section/20251112) |
| 2025-10-06 | `deprecated_field` | /v5/product/info/prices 参数 items.price.marketing_price 即将废弃，我们将于2025年11月12日关闭该参数。 | [官方 News](https://docs.ozon.ru/api/seller/zh/#section/2025106) |
| 2025-05-28 | `added_field` | /v5/product/info/prices 在方法的响应中新增了参数items.price.net_price。 | [官方 News](https://docs.ozon.ru/api/seller/zh/#section/2025528) |
| 2025-03-07 | `graduated` | /v5/product/info/prices 已将该方法从 Beta 版迁移至正式版。 | [官方 News](https://docs.ozon.ru/api/seller/zh/#section/202537) |

## 页面标题结构

- 获取商品价格信息
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
| `cursor` | string 用于选择数据的指针。 |
| `filter` required | object 商品筛选器。 |
| `limit` required | integer <int32> [ 1 .. 1000 ] 每页显示的数值数量。 |

### 表格 2

| 字段 | 类型/说明 |
| --- | --- |
| `cursor` | string 用于选择数据的指针。 |
| `items` | Array of objects 商品列表。 |
| `total` | integer <int32> 商品列表中的商品数量。 |

## 示例

### 示例 0

```json
{
  "cursor": "",
  "filter": {
    "offer_id": [
      "356792"
    ],
    "product_id": [
      "243686911"
    ],
    "visibility": "ALL"
  },
  "limit": 100
}
```

### 示例 1

```json
{
  "items": [
    {
      "product_id": 1000123456,
      "offer_id": "test-offer-123456",
      "price": {
        "price": 2999.99,
        "old_price": 3499.99,
        "min_price": 2799.99,
        "net_price": 2000,
        "currency_code": "RUB",
        "vat": 0.2,
        "auto_action_enabled": true,
        "auto_add_to_ozon_actions_list_enabled": true
      },
      "commissions": {
        "sales_percent_fbo": 15,
        "sales_percent_fbs": 12,
        "fbo_deliv_to_customer_amount": 14.75,
        "fbs_deliv_to_customer_amount": 60,
        "fbo_return_flow_amount": 50,
        "fbs_return_flow_amount": 40
      },
      "price_indexes": {
        "color_index": "GREEN",
        "ozon_index_data": {
          "min_price": 2899.99,
          "min_price_currency": "RUB",
          "price_index_value": 0.95
        },
        "external_index_data": {
          "min_price": 2799.99,
          "min_price_currency": "RUB",
          "price_index_value": 0.93
        }
      },
      "marketing_actions": {
        "ozon_actions_exist": true,
        "current_period_from": "2026-03-01T00:00:00Z",
        "current_period_to": "2026-03-31T23:59:59Z",
        "actions": [
          {
            "title": "电子产品15%折扣",
            "value": 15,
            "date_from": "2026-03-01T00:00:00Z",
            "date_to": "2026-03-31T23:59:59Z"
          }
        ]
      },
      "acquiring": 1.5,
      "volume_weight": 0.5
    },
    {
      "product_id": 1000123457,
      "offer_id": "test-offer-123457",
      "price": {
        "price": 5999.99,
        "old_price": 6999.99,
        "min_price": 5499.99,
        "net_price": 4000,
        "currency_code": "RUB",
        "vat": 0.2,
        "auto_action_enabled": false,
        "auto_add_to_ozon_actions_list_enabled": false
      },
      "commissions": {
        "sales_percent_fbo": 10,
        "sales_percent_fbs": 8,
        "fbo_deliv_to_customer_amount": 25.5,
        "fbs_deliv_to_customer_amount": 75,
        "fbo_return_flow_amount": 60,
        "fbs_return_flow_amount": 50
      },
      "price_indexes": {
        "color_index": "YELLOW",
        "ozon_index_data": {
          "min_price": 5899.99,
          "min_price_currency": "RUB",
          "price_index_value": 0.98
        }
      },
      "marketing_actions": {
        "ozon_actions_exist": false
      },
      "acquiring": 1.8,
      "volume_weight": 0.8
    }
  ],
  "cursor": "",
  "total": 2
}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

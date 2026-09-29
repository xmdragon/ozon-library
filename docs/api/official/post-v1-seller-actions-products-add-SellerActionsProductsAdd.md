# 将商品添加到促销活动中

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/seller-actions/products/add`
- Operation ID：`SellerActionsProductsAdd`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/#operation/SellerActionsProductsAdd
- 分组：`seller-actions`

## News 更新标记

| 日期 | 标记 | 摘要 | 来源 |
| --- | --- | --- | --- |
| 2026-09-28 | `added_field` | /v1/seller-actions/products/add 在方式的请求中添加了 products.action_price 参数。 更新了方法请求中的 products.discount_percent 参数描述。 | [官方 News](https://docs.ozon.ru/api/seller/zh/#section/2026928) |
| 2026-03-24 | `new_method` | /v1/seller-actions/products/add 新增了用于管理卖家促销活动的Beta方法。 | [官方 News](https://docs.ozon.ru/api/seller/zh/#section/2026324) |

## 页面标题结构

- 将商品添加到促销活动中
- HEADER PARAMETERS
- REQUEST BODY SCHEMA: application/json
- 回复
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
| `action_id` required | integer <uint64> 促销活动标识符。请通过方法 /v1/seller-actions/list 获取该参数的值。 |
| `products` required | Array of action_price (object) or discount_percent (object) <= 100 items 商品信息。 |

### 表格 2：products[]：action_price 方案

| 字段 | 类型/说明 |
| --- | --- |
| `action_price` required | number <double> 商品的促销价格。 |
| `currency` | string Default: "RUB" Enum: "RUB" "BYN" "KZT" "EUR" "USD" "CNY" 货币： RUB ——俄罗斯卢布； BYN ——白俄罗斯卢布； KZT ——坚戈； EUR ——欧元； USD ——美元； CNY ——人民币。 |
| `discount_percent` | number <double> 百分比折扣值。如果您选择了“折扣”或“促销码折扣”促销活动机制，并且在 /v1/seller-actions/list 方法中获得了 actions.action_parameters.discount_type = PERCENT ，请传递该参数。 |
| `sku` required | integer <uint64> Ozon系统中的商品标识符——SKU。 |

### 表格 3：products[]：discount_percent 方案

| 字段 | 类型/说明 |
| --- | --- |
| `action_price` | number <double> 商品的促销价格。 |
| `currency` | string Default: "RUB" Enum: "RUB" "BYN" "KZT" "EUR" "USD" "CNY" 货币： RUB ——俄罗斯卢布； BYN ——白俄罗斯卢布； KZT ——坚戈； EUR ——欧元； USD ——美元； CNY ——人民币。 |
| `discount_percent` required | number <double> 百分比折扣值。如果您选择了“折扣”或“促销码折扣”促销活动机制，并且在 /v1/seller-actions/list 方法中获得了 actions.action_parameters.discount_type = PERCENT ，请传递该参数。 |
| `sku` required | integer <uint64> Ozon系统中的商品标识符——SKU。 |

## 示例

### 示例 0

```json
{
  "action_id": 0,
  "products": [
    {}
  ]
}
```

### 示例 1

```json
{
  "code": 0,
  "details": [
    {
      "typeUrl": "string",
      "value": "string"
    }
  ],
  "message": "string"
}
```

## 请求填写示意

以下示意根据官方字段结构整理，须替换为真实活动与商品 ID。

### action_price 方案

填写商品促销价格；action_id、sku 均需替换为真实标识。

```json
{
  "action_id": 0,
  "products": [
    {
      "action_price": 100,
      "currency": "RUB",
      "sku": 0
    }
  ]
}
```

### discount_percent 方案

仅在“折扣”或“促销码折扣”活动且 actions.action_parameters.discount_type 为 PERCENT 时填写；action_id、sku 均需替换为真实标识。

```json
{
  "action_id": 0,
  "products": [
    {
      "discount_percent": 10,
      "currency": "RUB",
      "sku": 0
    }
  ]
}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

# 创建采用"基于订单总额的折扣"机制的促销活动

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/seller-actions/create/discount-with-condition`
- Operation ID：`SellerActionsCreateDiscountWithCondition`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/SellerActionsCreateDiscountWithCondition
- 分组：`seller-actions`

## 页面标题结构

- 创建采用"基于订单总额的折扣"机制的促销活动
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
| `date_end` required | string <date-time> 促销活动结束日期与时间。 |
| `date_start` required | string <date-time> 促销活动开始日期与时间。 |
| `discount_type` required | string Enum: "PERCENT" "CURRENCY" 折扣类型： PERCENT——百分比折扣； CURRENCY——按金额折扣。 |
| `discount_value` required | number <float> 折扣幅度。 |
| `min_order_amount` required | number <double> 折扣生效的订单金额门槛。 |
| `title` | string [ 1 .. 256 ] characters 促销活动名称。 |

### 表格 2

| 字段 | 类型/说明 |
| --- | --- |
| `action_id` | integer <uint64> 促销活动标识符。 |

## 示例

### 示例 0

```text
PERCENT
```

### 示例 1

```text
CURRENCY
```

### 示例 2

```json
{
  "date_end": "2019-08-24T14:15:22Z",
  "date_start": "2019-08-24T14:15:22Z",
  "discount_type": "PERCENT",
  "discount_value": 0,
  "min_order_amount": 0,
  "title": "string"
}
```

### 示例 3

```json
{
  "action_id": 0
}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

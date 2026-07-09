# 申请折扣列表

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

> [!WARNING]
> 官方 News 标记此方法为 `deprecated`，日期：2026-01-29。替代方法：`/v2/actions/discounts-task/list`。 官方 News：https://docs.ozon.ru/api/seller/zh/#section/2026129
> News 原文摘要：/v1/actions/discounts-task/list 该方法已弃用，并将在未来停用。请切换至 替代方法：/v2/actions/discounts-task/list

## 方法

- 请求：`POST /v1/actions/discounts-task/list`
- Operation ID：`promos_task_list`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/promos_task_list
- 分组：`actions`

## News 更新标记

| 日期 | 标记 | 摘要 | 来源 |
| --- | --- | --- | --- |
| 2026-01-29 | `deprecated_method` | /v1/actions/discounts-task/list 该方法已弃用，并将在未来停用。请切换至 替代方法：/v2/actions/discounts-task/list | [官方 News](https://docs.ozon.ru/api/seller/zh/#section/2026129) |

## 页面标题结构

- 申请折扣列表
- Request Body schema: application/json
- 回复
- Response Schema: application/json
- 请求范例
- 回复范例

## 参数与返回结构

### 表格 0

| 字段 | 类型/说明 |
| --- | --- |
| `status` required | string Default: "UNKNOWN" Enum: "NEW" "SEEN" "APPROVED" "PARTLY_APPROVED" "DECLINED" "AUTO_DECLINED" "DECLINED_BY_USER" "COUPON" "PURCHASED" 折扣申请状态： NEW — 新的， SEEN — 已查看的， APPROVED — 已批准的， PARTLY_APPROVED — 部分批准的， DECLINED — 取消的， AUTO_DECLINED — 自动取消的， DECLINED_BY_USER — 买家取消的， COUPON — 优惠券折扣， PURCHASED — 已购买的。 |
| `page` required | integer <uint64> 需要从中下载折扣申请列表的页面。 |
| `limit` required | integer <uint64> 页面上申请最大数量。 |

### 表格 1

| 字段 | 类型/说明 |
| --- | --- |
| `result` | Array of objects 申请列表。 |
| `id` | integer <uint64> 申请ID。 |
| `created_at` | string <date-time> 申请创建日期。 |
| `end_at` | string <date-time> 申请到期时间。 |
| `edited_till` | string <date-time> 决定改变时间。 |
| `status` | string 申请状态。 |
| `customer_name` | string 买家姓名。 |
| `sku` | integer <uint64> Ozon系统中的商品ID —— SKU。 |
| `user_comment` | string 买家对申请的评论。 |
| `seller_comment` | string 卖家对申请的评论。 |
| `requested_price` | number <double> 申请价格。 |
| `approved_price` | number <double> 批准的价格。 |
| `original_price` | number <double> 折扣前的商品价格。 |
| `discount` | number <double> 卢布折扣。 |
| `discount_percent` | number <double> 折扣百分比。 |
| `base_price` | number <double> 如果不参与促销活动，商品在Ozon上销售的基础价。 |
| `min_auto_price` | number <double> 自动应用折扣和促销后的最低价格值。 |
| `prev_task_id` | integer <uint64> 该商品买家先前申请ID。 |
| `is_damaged` | boolean 商品是否打折。如果打折，true。 |
| `moderated_at` | string <date-time> 审核日期：审核、批准或拒绝申请。 |
| `approved_discount` | number <double> 卖家同意的以卢布显示的折扣。 如果卖家不批准订单，则传递值“0”。 |
| `approved_discount_percent` | number <double> 卖家批准的折扣百分比。请传递值 0，如果卖家不批准申请。 |
| `is_purchased` | boolean 用户是否购买了商品。 true，如果购买。 |
| `is_auto_moderated` | boolean 申请是否自动审核。 true，如果自动审核。 |
| `offer_id` | string 卖家系统中的商品标识符是商品货号。 |
| `email` | string 处理请求的卖家员工电子邮件地址。 |
| `last_name` | string 处理申请的卖家员工姓氏。 |
| `first_name` | string 处理请求的卖家员工姓名。 |
| `patronymic` | string 处理请求的卖家员工父称。 |
| `approved_quantity_min` | integer <uint64> 商品数量批准的最小值。 |
| `approved_quantity_max` | integer <uint64> 商品数量批准的最大值。 |
| `requested_quantity_min` | integer <uint64> 商品请求数量最小值。 |
| `requested_quantity_max` | integer <uint64> 商品请求数量最大值。 |
| `requested_price_with_fee` | number <double> 带有区域加价的价格申请。 |
| `approved_price_with_fee` | number <double> 批准的含区域加价的价格。 |
| `approved_price_fee_percent` | number <double> 按百分比显示的区域加价。 |

### 表格 2

| 字段 | 类型/说明 |
| --- | --- |
| `id` | integer <uint64> 申请ID。 |
| `created_at` | string <date-time> 申请创建日期。 |
| `end_at` | string <date-time> 申请到期时间。 |
| `edited_till` | string <date-time> 决定改变时间。 |
| `status` | string 申请状态。 |
| `customer_name` | string 买家姓名。 |
| `sku` | integer <uint64> Ozon系统中的商品ID —— SKU。 |
| `user_comment` | string 买家对申请的评论。 |
| `seller_comment` | string 卖家对申请的评论。 |
| `requested_price` | number <double> 申请价格。 |
| `approved_price` | number <double> 批准的价格。 |
| `original_price` | number <double> 折扣前的商品价格。 |
| `discount` | number <double> 卢布折扣。 |
| `discount_percent` | number <double> 折扣百分比。 |
| `base_price` | number <double> 如果不参与促销活动，商品在Ozon上销售的基础价。 |
| `min_auto_price` | number <double> 自动应用折扣和促销后的最低价格值。 |
| `prev_task_id` | integer <uint64> 该商品买家先前申请ID。 |
| `is_damaged` | boolean 商品是否打折。如果打折，true。 |
| `moderated_at` | string <date-time> 审核日期：审核、批准或拒绝申请。 |
| `approved_discount` | number <double> 卖家同意的以卢布显示的折扣。 如果卖家不批准订单，则传递值“0”。 |
| `approved_discount_percent` | number <double> 卖家批准的折扣百分比。请传递值 0，如果卖家不批准申请。 |
| `is_purchased` | boolean 用户是否购买了商品。 true，如果购买。 |
| `is_auto_moderated` | boolean 申请是否自动审核。 true，如果自动审核。 |
| `offer_id` | string 卖家系统中的商品标识符是商品货号。 |
| `email` | string 处理请求的卖家员工电子邮件地址。 |
| `last_name` | string 处理申请的卖家员工姓氏。 |
| `first_name` | string 处理请求的卖家员工姓名。 |
| `patronymic` | string 处理请求的卖家员工父称。 |
| `approved_quantity_min` | integer <uint64> 商品数量批准的最小值。 |
| `approved_quantity_max` | integer <uint64> 商品数量批准的最大值。 |
| `requested_quantity_min` | integer <uint64> 商品请求数量最小值。 |
| `requested_quantity_max` | integer <uint64> 商品请求数量最大值。 |
| `requested_price_with_fee` | number <double> 带有区域加价的价格申请。 |
| `approved_price_with_fee` | number <double> 批准的含区域加价的价格。 |
| `approved_price_fee_percent` | number <double> 按百分比显示的区域加价。 |

## 示例

### 示例 0

```text
NEW
```

### 示例 1

```text
SEEN
```

### 示例 2

```text
APPROVED
```

### 示例 3

```text
PARTLY_APPROVED
```

### 示例 4

```text
DECLINED
```

### 示例 5

```text
AUTO_DECLINED
```

### 示例 6

```text
DECLINED_BY_USER
```

### 示例 7

```text
COUPON
```

### 示例 8

```text
PURCHASED
```

### 示例 9

```text
true
```

### 示例 11

```text
true
```

### 示例 12

```text
true
```

### 示例 13

```json
{
  "status": "UNKNOWN",
  "page": 1,
  "limit": 50
}
```

### 示例 14

```json
{
  "result": [
    {
      "id": 12345,
      "created_at": "2023-10-15T09:30:00Z",
      "end_at": "2023-10-20T18:45:00Z",
      "edited_till": "2023-10-18T12:00:00Z",
      "status": "approved",
      "customer_name": "Ivan Ivanov",
      "sku": 100500,
      "user_comment": "商品急需，请加快处理",
      "seller_comment": "已与经理确认，折扣已提供",
      "requested_price": 15000,
      "approved_price": 14500,
      "original_price": 16000,
      "discount": 1000,
      "discount_percent": 6.25,
      "base_price": 15500,
      "min_auto_price": 14000,
      "prev_task_id": 12344,
      "is_damaged": false,
      "moderated_at": "2023-10-16T10:15:00Z",
      "approved_discount": 500,
      "approved_discount_percent": 3.125,
      "is_purchased": true,
      "is_auto_moderated": false,
      "offer_id": "OFFER-2023-1001",
      "email": "ivan.ivanov@example.com",
      "last_name": "Ivanov",
      "first_name": "Ivan",
      "patronymic": "Petrovich",
      "approved_quantity_min": 1,
      "approved_quantity_max": 5,
      "requested_quantity_min": 2,
      "requested_quantity_max": 10,
      "requested_price_with_fee": 15500,
      "approved_price_with_fee": 15000,
      "approved_price_fee_percent": 3.2
    }
  ]
}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

# 获取促销活动列表

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/seller-actions/list`
- Operation ID：`SellerActionsList`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/SellerActionsList
- 分组：`seller-actions`

## 页面标题结构

- 获取促销活动列表
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
| `action_ids` | Array of strings <uint64> <= 100 items 促销活动标识符列表。 |
| `action_type` | Array of stringsItems Enum: "DISCOUNT" "VOUCHER_DISCOUNT" "DISCOUNT_WITH_CONDITION" "INSTALLMENT" "INDIVIDUAL_DISCOUNT_BY_PRODUCTS" "OZON_ACCOUNT_DISCOUNT" "MULTI_LEVEL_DISCOUNT_ON_AMOUNT" 促销活动机制： DISCOUNT——折扣； VOUCHER_DISCOUNT——促销码折扣； DISCOUNT_WITH_CONDITION——基于订单总额的折扣； INSTALLMENT——免息分期付款； INDIVIDUAL_DISCOUNT_BY_PRODUCTS——卖家积分； OZON_ACCOUNT_DISCOUNT——Ozon银行卡专享额外折扣； MULTI_LEVEL_DISCOUNT_ON_AMOUNT——多级满额折扣。 |
| `limit` required | integer <uint64> [ 1 .. 100 ] 每页显示的数量。 |
| `offset` | integer <uint64> 在响应中将被跳过的项目数量。例如，当offset = 10时，响应将从第11个找到的元素开始。 |
| `search` | string >= 3 characters 按促销活动名称搜索。 |
| `status` | Array of stringsItems Enum: "ACTIVE" "ENDED" "PLANNED" "PAUSED" 促销活动状态： ACTIVE—— 活跃； ENDED——已结束； PLANNED——已计划； PAUSED——已暂停。 |

### 表格 2

| 字段 | 类型/说明 |
| --- | --- |
| `actions` | Array of objects 促销活动列表。 |
| `total` | integer <uint64> 促销活动总数。 |

## 示例

### 示例 0

```text
DISCOUNT
```

### 示例 1

```text
VOUCHER_DISCOUNT
```

### 示例 2

```text
DISCOUNT_WITH_CONDITION
```

### 示例 3

```text
INSTALLMENT
```

### 示例 4

```text
INDIVIDUAL_DISCOUNT_BY_PRODUCTS
```

### 示例 5

```text
OZON_ACCOUNT_DISCOUNT
```

### 示例 6

```text
MULTI_LEVEL_DISCOUNT_ON_AMOUNT
```

### 示例 7

```text
offset = 10
```

### 示例 8

```text
ACTIVE
```

### 示例 9

```text
ENDED
```

### 示例 10

```text
PLANNED
```

### 示例 11

```text
PAUSED
```

### 示例 12

```json
{"action_ids": ["string"],"action_type": ["DISCOUNT"],"limit": 1,"offset": 0,"search": "string","status": ["ACTIVE"]}
```

### 示例 13

```json
{"actions": [{"action_id": 0,"action_parameters": {"addresses": ["string"],"auto_stop_action_reason": "UNSPECIFIED","budget": 0,"budget_spent": 0,"date_end": "2019-08-24T14:15:22Z","date_start": "2019-08-24T14:15:22Z","discount_levels": [{"discount_value": 0,"order_amount": 0}],"discount_type": "UNSPECIFIED","discount_value": 0,"is_legal_entities_segment": true,"min_action_percent": 0,"min_order_amount": 0,"picked_segments": [{"segments": [{"description": "string","id": 0,"name": "string","type": "UNSPECIFIED"}]}],"status": "ACTIVE","title": "string","type": "DISCOUNT","voucher_parameters": {"count_codes": 0,"is_private": true,"type": "UNSPECIFIED"},"warehouses": ["string"]},"allow_delete": true,"highlight_url": "string","is_editable": true,"is_participated": true,"is_turn_on": true,"sku_count": 0}],"total": 0}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

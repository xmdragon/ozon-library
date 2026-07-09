# 获取折扣申请列表

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v2/actions/discounts-task/list`
- Operation ID：`GetDiscountTaskListV2`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/GetDiscountTaskListV2
- 分组：`actions`

## 页面标题结构

- 获取折扣申请列表
- header Parameters
- Request Body schema: application/json
- 回复
- Response Schema: application/json
- 请求范例
- 回复范例

## 参数与返回结构

### 表格 0

Client-Id required string 用户识别号。 Api-Key required string API-密钥。

### 表格 1

last_idinteger <int64> 页面上最后一个值的标识符。首次请求请留空。 limitinteger <int64> <= 50 Default: 50 Enum: 5 10 15 20 30 50 每页最大申请数量。 statusstring Default: "ALL" Enum: "ALL" "NEW" "APPROVED" "DECLINED" 折扣申请状态： ALL——全部状态， NEW——新建， APPROVED——已批准， DECLINED——已拒绝。

### 表格 2

tasksArray of objects 申请列表。 Array ()approved_discountnumber <double> 卖家批准的折扣金额（卢布）。如果卖家未批准申请，请传入 0。 approved_pricenumber <double> 批准价格。 approved_quantity_maxinteger <uint64> 批准的最大商品数量。 auto_moderated_infoobject 申请自动审核信息。 created_atstring <date-time> 申请创建日期。 edited_tillstring <date-time> YYYY-MM-DD 可修改决定的时间。 edited_till_durationinteger <uint64> 可修改决定的时间（秒）。 emailstring 处理申请的卖家员工邮箱地址。 end_atstring <date-time> 申请有效期结束时间。 end_at_durationinteger <uint64> 申请有效期结束时间（秒）。 first_namestring 处理申请的卖家员工名字。 idinteger <uint64> 申请标识符。 is_auto_moderatedboolean true，表示审核为自动审核。 last_namestring 处理申请的卖家员工姓氏。 min_auto_pricenumber <double> 自动应用折扣与促销后的最低价格值。 moderated_atstring <date-time> 审核日期：查看、批准或拒绝申请的日期。 namestring 商品名称。 original_pricenumber <double> 商品在所有折扣前的价格。 patronymicstring 处理申请的卖家员工父名（中间名）。 reduction_factornumber <double> 创建申请时买家价格与卖家价格之间的差值。 requested_discountnumber <double> 折扣百分比。 requested_pricenumber <double> 申请价格。 requested_quantity_maxinteger <uint64> 请求的最大商品数量。 skuinteger <uint64> Ozon 系统中的商品标识符——SKU。 statusstring Default: "ALL" Enum: "ALL" "NEW" "APPROVED" "DECLINED" 折扣申请状态： ALL——全部状态， NEW——新建， APPROVED——已批准， DECLINED——已拒绝。

### 表格 3

approved_discountnumber <double> 卖家批准的折扣金额（卢布）。如果卖家未批准申请，请传入 0。 approved_pricenumber <double> 批准价格。 approved_quantity_maxinteger <uint64> 批准的最大商品数量。 auto_moderated_infoobject 申请自动审核信息。 created_atstring <date-time> 申请创建日期。 edited_tillstring <date-time> YYYY-MM-DD 可修改决定的时间。 edited_till_durationinteger <uint64> 可修改决定的时间（秒）。 emailstring 处理申请的卖家员工邮箱地址。 end_atstring <date-time> 申请有效期结束时间。 end_at_durationinteger <uint64> 申请有效期结束时间（秒）。 first_namestring 处理申请的卖家员工名字。 idinteger <uint64> 申请标识符。 is_auto_moderatedboolean true，表示审核为自动审核。 last_namestring 处理申请的卖家员工姓氏。 min_auto_pricenumber <double> 自动应用折扣与促销后的最低价格值。 moderated_atstring <date-time> 审核日期：查看、批准或拒绝申请的日期。 namestring 商品名称。 original_pricenumber <double> 商品在所有折扣前的价格。 patronymicstring 处理申请的卖家员工父名（中间名）。 reduction_factornumber <double> 创建申请时买家价格与卖家价格之间的差值。 requested_discountnumber <double> 折扣百分比。 requested_pricenumber <double> 申请价格。 requested_quantity_maxinteger <uint64> 请求的最大商品数量。 skuinteger <uint64> Ozon 系统中的商品标识符——SKU。 statusstring Default: "ALL" Enum: "ALL" "NEW" "APPROVED" "DECLINED" 折扣申请状态： ALL——全部状态， NEW——新建， APPROVED——已批准， DECLINED——已拒绝。

## 示例

### 示例 0

```text
ALL
```

### 示例 1

```text
NEW
```

### 示例 2

```text
APPROVED
```

### 示例 3

```text
DECLINED
```

### 示例 4

```text
ALL
```

### 示例 5

```text
NEW
```

### 示例 6

```text
APPROVED
```

### 示例 7

```text
DECLINED
```

### 示例 8

```json
{"last_id": 0,"limit": 50,"status": "ALL"}
```

### 示例 9

```json
{"tasks": [{"approved_discount": 0,"approved_price": 0,"approved_quantity_max": 0,"auto_moderated_info": {"max_percent": 0,"max_price": 0,"min_percent": 0,"min_price": 0},"created_at": "2019-08-24T14:15:22Z","edited_till": "2019-08-24T14:15:22Z","edited_till_duration": 0,"email": "string","end_at": "2019-08-24T14:15:22Z","end_at_duration": 0,"first_name": "string","id": 0,"is_auto_moderated": true,"last_name": "string","min_auto_price": 0,"moderated_at": "2019-08-24T14:15:22Z","name": "string","original_price": 0,"patronymic": "string","reduction_factor": 0,"requested_discount": 0,"requested_price": 0,"requested_quantity_max": 0,"sku": 0,"status": "ALL"}]}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

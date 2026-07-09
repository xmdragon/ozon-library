# 仓库清单

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/warehouse/list`
- Operation ID：`WarehouseAPI_WarehouseList`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/WarehouseAPI_WarehouseList
- 分组：`warehouse`

## 页面标题结构

- 仓库清单
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

limit required integer <int64> <= 200 响应中返回的值数量。 offsetinteger <int64> 在响应中将被跳过的项目数量。例如，如果 offset = 10，则响应将从第 11 个找到的项目开始。 withobject 需要添加到响应中的附加字段。

### 表格 2

resultArray of objects 仓库清单。 Array ()has_entrusted_acceptanceboolean 会表明受信任的接受。true, 如果库存中启用了受信任的接受方式。 is_rfbsboolean 在 rFBS 计划下运作的仓库的标志： true — 仓库在 rFBS 计划下运行； false — 仓库没有在 rFBS 计划下运行。 namestring 仓库名称。 warehouse_idinteger <int64> 仓库识别号。 can_print_act_in_advanceboolean 有可能提前打印收发证书。 true, 如果可以提前打印的话。 first_mile_typeobject 第一英里 FBS。 has_postings_limitboolean 该迹象表明对最小订单数有限制。true, 如果有限制。 is_karantinboolean 该迹象表明仓库因隔离而停止运作。 is_kgtboolean 该迹象表明仓库接受大宗商品。 is_able_to_set_priceboolean 如果可以设置价格，则为true。 is_presortedboolean 如果发运是预先分拣的，则为true。 is_timetable_editableboolean 该迹象表明可以改变仓库运行时间表。 min_postings_limitinteger <int32> 限制的最小值是指在一次供货中可以带来的订单数量。 postings_limitinteger <int32> 极限值。 -1, 如果没有限制 min_working_daysinteger <int64> 仓库运行天数。 statusstring 仓库状况。 仓库状态与个人账户中的状态的对应关系: 状态 Seller API 个人账户中的状态 new 正在激活 created 已激活 disabled 存档 blocked 已封禁 disabled_due_to_limit 暂停中 error 错误 working_daysArray of stringsItems Enum: "1" "2" "3" "4" "5" "6" "7" 仓库运行天数。

### 表格 3

has_entrusted_acceptanceboolean 会表明受信任的接受。true, 如果库存中启用了受信任的接受方式。 is_rfbsboolean 在 rFBS 计划下运作的仓库的标志： true — 仓库在 rFBS 计划下运行； false — 仓库没有在 rFBS 计划下运行。 namestring 仓库名称。 warehouse_idinteger <int64> 仓库识别号。 can_print_act_in_advanceboolean 有可能提前打印收发证书。 true, 如果可以提前打印的话。 first_mile_typeobject 第一英里 FBS。 has_postings_limitboolean 该迹象表明对最小订单数有限制。true, 如果有限制。 is_karantinboolean 该迹象表明仓库因隔离而停止运作。 is_kgtboolean 该迹象表明仓库接受大宗商品。 is_able_to_set_priceboolean 如果可以设置价格，则为true。 is_presortedboolean 如果发运是预先分拣的，则为true。 is_timetable_editableboolean 该迹象表明可以改变仓库运行时间表。 min_postings_limitinteger <int32> 限制的最小值是指在一次供货中可以带来的订单数量。 postings_limitinteger <int32> 极限值。 -1, 如果没有限制 min_working_daysinteger <int64> 仓库运行天数。 statusstring 仓库状况。 仓库状态与个人账户中的状态的对应关系: 状态 Seller API 个人账户中的状态 new 正在激活 created 已激活 disabled 存档 blocked 已封禁 disabled_due_to_limit 暂停中 error 错误 working_daysArray of stringsItems Enum: "1" "2" "3" "4" "5" "6" "7" 仓库运行天数。

### 表格 4

状态 Seller API 个人账户中的状态 new 正在激活 created 已激活 disabled 存档 blocked 已封禁 disabled_due_to_limit 暂停中 error 错误

## 示例

### 示例 0

```json
{"limit": 1,"offset": 1,"with": {"able_to_set_price": true}}
```

### 示例 1

```json
{"result": [{"warehouse_id": 17777777788000,"name": "BlueMarketplace","is_rfbs": false,"is_able_to_set_price": false,"has_entrusted_acceptance": true,"first_mile_type": {"dropoff_point_id": "1121111996024111","dropoff_timeslot_id": 294144,"first_mile_is_changing": false,"first_mile_type": "DropOff"},"is_kgt": false,"can_print_act_in_advance": false,"min_working_days": 5,"is_karantin": false,"has_postings_limit": false,"postings_limit": -1,"working_days": [1,2,3,4,5,6,7],"min_postings_limit": 2,"is_timetable_editable": false,"status": "created","is_economy": false,"is_presorted": false}]}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

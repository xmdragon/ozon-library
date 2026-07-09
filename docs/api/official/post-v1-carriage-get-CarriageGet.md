# 运输信息

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/carriage/get`
- Operation ID：`CarriageGet`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/CarriageGet
- 分组：`carriage`

## 页面标题结构

- 运输信息
- Request Body schema: application/json
- 回复
- Response Schema: application/json
- 请求范例
- 回复范例

## 参数与返回结构

### 表格 0

carriage_id required integer <int64> 运输标识符。

### 表格 1

act_typestring 交接单类型。针对FBS卖家。 arrival_pass_idsArray of strings <int64> 为运输生成的通行证标识符列表。 available_actionsArray of strings 运输的可用操作： get_shipping_list——获取发运清单； get_act_of_acceptance——获取验收证明书； get_waybill——获取 PDF 格式的货单； set_arrival_passes——创建通行证。 cancel_availabilityobject 是否可以取消。 carriage_idinteger <int64> 运输标识符。 company_idinteger <int64> 卖家标识符。 containers_countinteger <int32> 货位数量。 created_atstring <date-time> 运输创建日期。 delivery_method_idinteger <int64> 物流方式标识符。 departure_datestring 运输完成日期。 first_mile_typestring 头程物流类型。 has_postings_for_next_carriageboolean true, 如果有未能进行运输，但需要发运的货件。 integration_typestring 运输类型。 is_container_label_printedboolean true, 如果您已经打印了货位标签。 is_partialboolean true, 如果是部分运输。 partial_numinteger <int64> 部分运输序列号。 retry_countinteger <int32> 运输创建重复尝试数量。 statusstring 运输状态。 tpl_provider_idinteger <int64> 配送服务商标识符。 updated_atstring <date-time> 运输信息最后一次更新日期。 warehouse_idinteger <int64> 仓库标识符。

## 示例

### 示例 0

```json
{"carriage_id": 0}
```

### 示例 1

```json
{"act_type": "string","arrival_pass_ids": ["string"],"available_actions": ["string"],"cancel_availability": {"is_cancel_available": true,"reason": "string"},"carriage_id": 0,"company_id": 0,"containers_count": 0,"created_at": "2019-08-24T14:15:22Z","delivery_method_id": 0,"departure_date": "string","first_mile_type": "string","has_postings_for_next_carriage": true,"integration_type": "string","is_container_label_printed": true,"is_partial": true,"partial_num": 0,"retry_count": 0,"status": "string","tpl_provider_id": 0,"updated_at": "2019-08-24T14:15:22Z","warehouse_id": 0}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

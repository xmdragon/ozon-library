# 按照ID获取货件信息

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v3/posting/fbs/get`
- Operation ID：`PostingAPI_GetFbsPostingV3`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/PostingAPI_GetFbsPostingV3
- 分组：`posting`

## 页面标题结构

- 按照ID获取货件信息
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

posting_number required string 货件ID。 withobject 需要添加到响应中的附加字段。

### 表格 2

resultobject 货件信息。 additional_dataArray of objects addresseeobject 收件人联系方式。 analytics_dataobject 分析数据。 available_actionsArray of strings 可用的操作和货件信息包括： arbitration — 提出争议； awaiting_delivery — 转为“等待发运”状态； can_create_chat — 与买家开启聊天； cancel — 取消货件； click_track_number — 在个人中心通过追踪号查看状态历史； customer_phone_available — 获取买家电话号码； has_weight_products — 货件中包含以重量结算； hide_region_and_city — 在报告中隐藏买家的地区和城市； invoice_get — 获取发票信息； invoice_send — 创建发票； invoice_update — 编辑发票； label_download_big — 下载大标签； label_download_small — 下载小标签； label_download — 下载标签； non_int_delivered — 转为“可能已收”状态； non_int_delivering — 转为“运输中”状态； non_int_last_mile — 转为“快递员派件中”状态； product_cancel — 取消部分货件中的商品； set_cutoff — 需要指定发货日期，请使用方法/v1/posting/cutoff/set； set_timeslot — 修改买家的送货时间； set_track_number — 指定或更改追踪号； ship_async_in_process — 货件备货中； ship_async_retry — 发生错误后重新发货； ship_async — 备货货件； ship_with_additional_info — 需要填写额外信息； ship — 备货货件; update_cis — 修改附加信息。 barcodesobject 货件条码。 cancellationobject 取消原因。 courierobject 快递员信息。 customerobject 买家信息。 delivering_datestring <date-time> 货件交付物流的时间。 delivery_methodobject 快递方式。 delivery_pricestring 物流价格。 fact_delivery_datestring <date-time> 货件实际转移配送的日期。 financial_dataobject 有关商品成本、折扣幅度、付款和佣金的信息。 in_process_atstring <date-time> 开始处理货件的日期和时间。 is_expressboolean 如果使用了快速物流Ozon Express —— true。 legal_infoobject 买方的法律信息。 optionalobject 带有附加特征的商品列表。 order_idinteger <int64> 货件所属的订单ID。 order_numberstring 货件所属的订单号。 parent_posting_numberstring 母件编号，由该母件拆分出了该货件。 posting_numberstring 货件号。 product_exemplarsobject 有关产品及其副本的信息。 响应包含 product_exemplars字段, 如果在请求中传递标志 with.product_exemplars = true。 pro

### 表格 3

additional_dataArray of objects addresseeobject 收件人联系方式。 analytics_dataobject 分析数据。 available_actionsArray of strings 可用的操作和货件信息包括： arbitration — 提出争议； awaiting_delivery — 转为“等待发运”状态； can_create_chat — 与买家开启聊天； cancel — 取消货件； click_track_number — 在个人中心通过追踪号查看状态历史； customer_phone_available — 获取买家电话号码； has_weight_products — 货件中包含以重量结算； hide_region_and_city — 在报告中隐藏买家的地区和城市； invoice_get — 获取发票信息； invoice_send — 创建发票； invoice_update — 编辑发票； label_download_big — 下载大标签； label_download_small — 下载小标签； label_download — 下载标签； non_int_delivered — 转为“可能已收”状态； non_int_delivering — 转为“运输中”状态； non_int_last_mile — 转为“快递员派件中”状态； product_cancel — 取消部分货件中的商品； set_cutoff — 需要指定发货日期，请使用方法/v1/posting/cutoff/set； set_timeslot — 修改买家的送货时间； set_track_number — 指定或更改追踪号； ship_async_in_process — 货件备货中； ship_async_retry — 发生错误后重新发货； ship_async — 备货货件； ship_with_additional_info — 需要填写额外信息； ship — 备货货件; update_cis — 修改附加信息。 barcodesobject 货件条码。 cancellationobject 取消原因。 courierobject 快递员信息。 customerobject 买家信息。 delivering_datestring <date-time> 货件交付物流的时间。 delivery_methodobject 快递方式。 delivery_pricestring 物流价格。 fact_delivery_datestring <date-time> 货件实际转移配送的日期。 financial_dataobject 有关商品成本、折扣幅度、付款和佣金的信息。 in_process_atstring <date-time> 开始处理货件的日期和时间。 is_expressboolean 如果使用了快速物流Ozon Express —— true。 legal_infoobject 买方的法律信息。 optionalobject 带有附加特征的商品列表。 order_idinteger <int64> 货件所属的订单ID。 order_numberstring 货件所属的订单号。 parent_posting_numberstring 母件编号，由该母件拆分出了该货件。 posting_numberstring 货件号。 product_exemplarsobject 有关产品及其副本的信息。 响应包含 product_exemplars字段, 如果在请求中传递标志 with.product_exemplars = true。 productsArray of objec

## 示例

### 示例 0

```json
{"posting_number": "57195475-0050-3","with": {"analytics_data": false,"barcodes": false,"financial_data": false,"legal_info": false,"product_exemplars": false,"related_postings": true,"translit": false}}
```

### 示例 1

```text
{"result": {"posting_number": "0132112277-0101-1","order_id": 35566798085,"order_number": "0132112277-0101","status": "awaiting_packaging","delivery_method": {"id": 1020005003107121,"name": "Ozon自发货，诺金斯克","warehouse_id": 1020005003107121,"warehouse": "FBS LikeSK","tpl_provider_id": 24,"tpl_provider": "Ozon配送"},"tracking_number": "","tpl_integration_type": "ozon","in_process_at": "2026-03-30T11:26:00Z","shipment_date": "2026-03-31T09:00:00Z","delivering_date": null,"provider_status": "","delivery_price": "","cancellation": {"cancel_reason_id": 0,"cancel_reason": "","cancellation_type": "","cancelled_after_ship": false,"affect_cancellation_rating": false,"cancellation_initiator": ""},"customer": null,"addressee": null,"products": [{"price": "1530.0000","offer_id": "SK-58（深红色）","name": "Cronier cr-2013专业非洲小卷卷发棒，9毫米","sku": 827098843,"quantity": 1,"dimensions": {"height": "150.00","length": "500.00","weight": "550","width": "300.00"},"currency_code": "RUB","is_blr_traceable": false,"is_marketplace_buyout": false,"has_imei": false,"weight_max": 0.55,"weight_min": 0,"is_weight_needed": false}],"barcodes": null,"analytics_data": null,"financial_data": null,"additional_data": [ ],"is_express": false,"requirements": {"products_requiring_gtd": [ ],"products_requiring_country": [ ],"products_requiring_mandatory_mark": [ ],"products_requiring_rnpt": [ ],"products_requiring_jw_uin": [ ],"products_requiring_change_country": [ ],"products_requiring_imei": [ ],"products_requiring_weight": [ ]},"product_exemplars": null,"courier": null,"parent_posting_number": "","related_postings": null,"available_actions": ["cancel","has_barcode_for_printing","product_cancel","ship","ship_async"],"multi_box_qty": 1,"is_multibox": false,"substatus": "posting_created","previous_substatus": "posting_split_pending","prr_option": {"code": "","price": "","currency_code": "RUB","floor": ""},"tariffication": {"current_tariff_rate": 1,"current_tariff_type": "no_discount","current_tariff_charge": "","current_tariff_charge_currency_code": "RUB","next_tariff_rate": 1,"next_tariff_type": "commission","next_tariff_charge": "50","next_tariff_starts_at": "2026-03-31T09:00:01Z","next_tariff_charge_currency_code": "RUB"},"destination_place_id": 0,"destination_place_name": "","is_presortable": false,"pickup_code_verified_at": null,"optional": {"products_with_possible_mandatory_mark": [ ]},"fact_delivery_date
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

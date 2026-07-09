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

| 字段 | 类型/说明 |
| --- | --- |
| `Client-Id` required | string 用户识别号。 |
| `Api-Key` required | string API-密钥。 |

### 表格 1

| 字段 | 类型/说明 |
| --- | --- |
| `posting_number` required | string 货件ID。 |
| `with` | object 需要添加到响应中的附加字段。 |

### 表格 2

| 字段 | 类型/说明 |
| --- | --- |
| `result` | object 货件信息。 |
| `additional_data` | Array of objects |
| `addressee` | object 收件人联系方式。 |
| `analytics_data` | object 分析数据。 |
| `available_actions` | Array of strings 可用的操作和货件信息包括： arbitration — 提出争议； awaiting_delivery — 转为“等待发运”状态； can_create_chat — 与买家开启聊天； cancel — 取消货件； click_track_number — 在个人中心通过追踪号查看状态历史； customer_phone_available — 获取买家电话号码； has_weight_products — 货件中包含以重量结算； hide_region_and_city — 在报告中隐藏买家的地区和城市； invoice_get — 获取发票信息； invoice_send — 创建发票； invoice_update — 编辑发票； label_download_big — 下载大标签； label_download_small — 下载小标签； label_download — 下载标签； non_int_delivered — 转为“可能已收”状态； non_int_delivering — 转为“运输中”状态； non_int_last_mile — 转为“快递员派件中”状态； product_cancel — 取消部分货件中的商品； set_cutoff — 需要指定发货日期，请使用方法/v1/posting/cutoff/set； set_timeslot — 修改买家的送货时间； set_track_number — 指定或更改追踪号； ship_async_in_process — 货件备货中； ship_async_retry — 发生错误后重新发货； ship_async — 备货货件； ship_with_additional_info — 需要填写额外信息； ship — 备货货件; update_cis — 修改附加信息。 |
| `barcodes` | object 货件条码。 |
| `cancellation` | object 取消原因。 |
| `courier` | object 快递员信息。 |
| `customer` | object 买家信息。 |
| `delivering_date` | string <date-time> 货件交付物流的时间。 |
| `delivery_method` | object 快递方式。 |
| `delivery_price` | string 物流价格。 |
| `fact_delivery_date` | string <date-time> 货件实际转移配送的日期。 |
| `financial_data` | object 有关商品成本、折扣幅度、付款和佣金的信息。 |
| `in_process_at` | string <date-time> 开始处理货件的日期和时间。 |
| `is_express` | boolean 如果使用了快速物流Ozon Express —— true。 |
| `legal_info` | object 买方的法律信息。 |
| `optional` | object 带有附加特征的商品列表。 |
| `order_id` | integer <int64> 货件所属的订单ID。 |
| `order_number` | string 货件所属的订单号。 |
| `parent_posting_number` | string 母件编号，由该母件拆分出了该货件。 |
| `posting_number` | string 货件号。 |
| `product_exemplars` | object 有关产品及其副本的信息。 响应包含 product_exemplars字段, 如果在请求中传递标志 with.product_exemplars = true。 |
| `products` | Array of objects 货物装运的数组。 |
| `provider_status` | string 快递服务状态。 |
| `related_postings` | object 相关货件。 |
| `requirements` | object 需提供制造国、货运报关单号、商品批次登记号、“诚实标志”、其他标识或重量的商品列表，以便将货件状态更新至下一阶段。 |
| `shipment_date` | string <date-time> 必须收取货件的日期和时间。 超出该时间后将适用新费率，相关信息请查看字段 tariffication。 |
| `shipment_date_without_delay` | string <date-time> 不逾期发运日期和时间。 |
| `status` | string 货运状态: acceptance_in_progress —— 正在验收， arbitration —— 仲裁， awaiting_approve —— 等待确认， awaiting_deliver —— 等待装运， awaiting_packaging —— 等待包装， awaiting_registration —— 等待注册， awaiting_verification —— 已创建， cancelled —— 已取消， cancelled_from_split_pending——因货件拆分而取消， client_arbitration —— 快递客户仲裁， delivered —— 已送达， delivering —— 运输中， driver_pickup —— 司机处， not_accepted —— 分拣中心未接受， |
| `substatus` | string 发货子状态： posting_acceptance_in_progress —— 正在验收， posting_in_arbitration —— 仲裁， posting_created —— 已创建， posting_in_carriage —— 在运输途中， posting_not_in_carriage —— 未在运输中， posting_registered —— 已登记， posting_transferring_to_delivery (status=awaiting_deliver) —— 移交给快递， posting_awaiting_passport_data —— 等待护照资料， posting_created —— 已创建， posting_awaiting_registration —— 等待注册， posting_registration_error —— 注册错误， posting_transferring_to_delivery (status=awaiting_registration) —— 交给快递员, posting_split_pending —— 已创建， posting_canceled —— 已取消， posting_in_client_arbitration —— 快递会员仲裁， posting_delivered —— 已送达， posting_received —— 已收到， posting_conditionally_delivered —— 暂时送到， posting_in_courier_service —— 快递员正在路上， posting_in_pickup_point —— 在取货点， posting_on_way_to_city —— 发往城市途中， posting_on_way_to_pickup_point —— 正发往取货点， posting_returned_to_warehouse —— 返回仓库， posting_transferred_to_courier_service —— 转交给快递员， posting_driver_pick_up —— 在司机那儿， posting_not_in_sort_center —— 集散中心未收到， ship_failed —— 备货失败。 |
| `previous_substatus` | string 货件的前一个子状态。可能的取值： posting_acceptance_in_progress —— 正在验收， posting_in_arbitration —— 仲裁， posting_created —— 已创建， posting_in_carriage —— 在运输途中， posting_not_in_carriage —— 未在运输中， posting_registered —— 已登记， posting_transferring_to_delivery (status=awaiting_deliver) —— 移交给快递， posting_awaiting_passport_data —— 等待护照资料， posting_created —— 已创建， posting_awaiting_registration —— 等待注册， posting_registration_error —— 注册错误， posting_transferring_to_delivery (status=awaiting_registration) —— 交给快递员, posting_split_pending —— 已创建， posting_canceled —— 已取消， posting_in_client_arbitration —— 快递会员仲裁， posting_delivered —— 已送达， posting_received —— 已收到， posting_conditionally_delivered —— 暂时送到， posting_in_courier_service —— 快递员正在路上， posting_in_pickup_point —— 在取货点， posting_on_way_to_city —— 发往城市途中， posting_on_way_to_pickup_point —— 正发往取货点， posting_returned_to_warehouse —— 返回仓库， posting_transferred_to_courier_service —— 转交给快递员， posting_driver_pick_up —— 在司机那儿， posting_not_in_sort_center —— 集散中心未收到。 |
| `tpl_integration_type` | string 快递服务集成类型： ozon —— 通过Ozon物流的快递。 aggregator —— 外部服务快递，Ozon注册订单。 3pl_tracking —— 外部服务快递，卖家注册订单。 non_integrated —— 卖家自行配送物流。 |
| `tracking_number` | string 货件跟踪号。 |
| `tariffication` | object 发运的计费信息。 |
| `tariffication_steps` | Array of objects 计费阶段。 |

### 表格 3

| 字段 | 类型/说明 |
| --- | --- |
| `additional_data` | Array of objects |
| `addressee` | object 收件人联系方式。 |
| `analytics_data` | object 分析数据。 |
| `available_actions` | Array of strings 可用的操作和货件信息包括： arbitration — 提出争议； awaiting_delivery — 转为“等待发运”状态； can_create_chat — 与买家开启聊天； cancel — 取消货件； click_track_number — 在个人中心通过追踪号查看状态历史； customer_phone_available — 获取买家电话号码； has_weight_products — 货件中包含以重量结算； hide_region_and_city — 在报告中隐藏买家的地区和城市； invoice_get — 获取发票信息； invoice_send — 创建发票； invoice_update — 编辑发票； label_download_big — 下载大标签； label_download_small — 下载小标签； label_download — 下载标签； non_int_delivered — 转为“可能已收”状态； non_int_delivering — 转为“运输中”状态； non_int_last_mile — 转为“快递员派件中”状态； product_cancel — 取消部分货件中的商品； set_cutoff — 需要指定发货日期，请使用方法/v1/posting/cutoff/set； set_timeslot — 修改买家的送货时间； set_track_number — 指定或更改追踪号； ship_async_in_process — 货件备货中； ship_async_retry — 发生错误后重新发货； ship_async — 备货货件； ship_with_additional_info — 需要填写额外信息； ship — 备货货件; update_cis — 修改附加信息。 |
| `barcodes` | object 货件条码。 |
| `cancellation` | object 取消原因。 |
| `courier` | object 快递员信息。 |
| `customer` | object 买家信息。 |
| `delivering_date` | string <date-time> 货件交付物流的时间。 |
| `delivery_method` | object 快递方式。 |
| `delivery_price` | string 物流价格。 |
| `fact_delivery_date` | string <date-time> 货件实际转移配送的日期。 |
| `financial_data` | object 有关商品成本、折扣幅度、付款和佣金的信息。 |
| `in_process_at` | string <date-time> 开始处理货件的日期和时间。 |
| `is_express` | boolean 如果使用了快速物流Ozon Express —— true。 |
| `legal_info` | object 买方的法律信息。 |
| `optional` | object 带有附加特征的商品列表。 |
| `order_id` | integer <int64> 货件所属的订单ID。 |
| `order_number` | string 货件所属的订单号。 |
| `parent_posting_number` | string 母件编号，由该母件拆分出了该货件。 |
| `posting_number` | string 货件号。 |
| `product_exemplars` | object 有关产品及其副本的信息。 响应包含 product_exemplars字段, 如果在请求中传递标志 with.product_exemplars = true。 |
| `products` | Array of objects 货物装运的数组。 |
| `provider_status` | string 快递服务状态。 |
| `related_postings` | object 相关货件。 |
| `requirements` | object 需提供制造国、货运报关单号、商品批次登记号、“诚实标志”、其他标识或重量的商品列表，以便将货件状态更新至下一阶段。 |
| `shipment_date` | string <date-time> 必须收取货件的日期和时间。 超出该时间后将适用新费率，相关信息请查看字段 tariffication。 |
| `shipment_date_without_delay` | string <date-time> 不逾期发运日期和时间。 |
| `status` | string 货运状态: acceptance_in_progress —— 正在验收， arbitration —— 仲裁， awaiting_approve —— 等待确认， awaiting_deliver —— 等待装运， awaiting_packaging —— 等待包装， awaiting_registration —— 等待注册， awaiting_verification —— 已创建， cancelled —— 已取消， cancelled_from_split_pending——因货件拆分而取消， client_arbitration —— 快递客户仲裁， delivered —— 已送达， delivering —— 运输中， driver_pickup —— 司机处， not_accepted —— 分拣中心未接受， |
| `substatus` | string 发货子状态： posting_acceptance_in_progress —— 正在验收， posting_in_arbitration —— 仲裁， posting_created —— 已创建， posting_in_carriage —— 在运输途中， posting_not_in_carriage —— 未在运输中， posting_registered —— 已登记， posting_transferring_to_delivery (status=awaiting_deliver) —— 移交给快递， posting_awaiting_passport_data —— 等待护照资料， posting_created —— 已创建， posting_awaiting_registration —— 等待注册， posting_registration_error —— 注册错误， posting_transferring_to_delivery (status=awaiting_registration) —— 交给快递员, posting_split_pending —— 已创建， posting_canceled —— 已取消， posting_in_client_arbitration —— 快递会员仲裁， posting_delivered —— 已送达， posting_received —— 已收到， posting_conditionally_delivered —— 暂时送到， posting_in_courier_service —— 快递员正在路上， posting_in_pickup_point —— 在取货点， posting_on_way_to_city —— 发往城市途中， posting_on_way_to_pickup_point —— 正发往取货点， posting_returned_to_warehouse —— 返回仓库， posting_transferred_to_courier_service —— 转交给快递员， posting_driver_pick_up —— 在司机那儿， posting_not_in_sort_center —— 集散中心未收到， ship_failed —— 备货失败。 |
| `previous_substatus` | string 货件的前一个子状态。可能的取值： posting_acceptance_in_progress —— 正在验收， posting_in_arbitration —— 仲裁， posting_created —— 已创建， posting_in_carriage —— 在运输途中， posting_not_in_carriage —— 未在运输中， posting_registered —— 已登记， posting_transferring_to_delivery (status=awaiting_deliver) —— 移交给快递， posting_awaiting_passport_data —— 等待护照资料， posting_created —— 已创建， posting_awaiting_registration —— 等待注册， posting_registration_error —— 注册错误， posting_transferring_to_delivery (status=awaiting_registration) —— 交给快递员, posting_split_pending —— 已创建， posting_canceled —— 已取消， posting_in_client_arbitration —— 快递会员仲裁， posting_delivered —— 已送达， posting_received —— 已收到， posting_conditionally_delivered —— 暂时送到， posting_in_courier_service —— 快递员正在路上， posting_in_pickup_point —— 在取货点， posting_on_way_to_city —— 发往城市途中， posting_on_way_to_pickup_point —— 正发往取货点， posting_returned_to_warehouse —— 返回仓库， posting_transferred_to_courier_service —— 转交给快递员， posting_driver_pick_up —— 在司机那儿， posting_not_in_sort_center —— 集散中心未收到。 |
| `tpl_integration_type` | string 快递服务集成类型： ozon —— 通过Ozon物流的快递。 aggregator —— 外部服务快递，Ozon注册订单。 3pl_tracking —— 外部服务快递，卖家注册订单。 non_integrated —— 卖家自行配送物流。 |
| `tracking_number` | string 货件跟踪号。 |
| `tariffication` | object 发运的计费信息。 |
| `tariffication_steps` | Array of objects 计费阶段。 |

## 示例

### 示例 0

```text
arbitration
```

### 示例 1

```text
awaiting_delivery
```

### 示例 2

```text
can_create_chat
```

### 示例 3

```text
cancel
```

### 示例 4

```text
click_track_number
```

### 示例 5

```text
customer_phone_available
```

### 示例 6

```text
has_weight_products
```

### 示例 7

```text
hide_region_and_city
```

### 示例 8

```text
invoice_get
```

### 示例 9

```text
invoice_send
```

### 示例 10

```text
invoice_update
```

### 示例 11

```text
label_download_big
```

### 示例 12

```text
label_download_small
```

### 示例 13

```text
label_download
```

### 示例 14

```text
non_int_delivered
```

### 示例 15

```text
non_int_delivering
```

### 示例 16

```text
non_int_last_mile
```

### 示例 17

```text
product_cancel
```

### 示例 18

```text
set_cutoff
```

### 示例 19

```text
set_timeslot
```

### 示例 20

```text
set_track_number
```

### 示例 21

```text
ship_async_in_process
```

### 示例 22

```text
ship_async_retry
```

### 示例 23

```text
ship_async
```

### 示例 24

```text
ship_with_additional_info
```

### 示例 25

```text
ship
```

### 示例 26

```text
update_cis
```

### 示例 27

```text
true
```

### 示例 28

```text
product_exemplars
```

### 示例 29

```text
with.product_exemplars = true
```

### 示例 30

```text
tariffication
```

### 示例 31

```text
acceptance_in_progress
```

### 示例 32

```text
arbitration
```

### 示例 33

```text
awaiting_approve
```

### 示例 34

```text
awaiting_deliver
```

### 示例 35

```text
awaiting_packaging
```

### 示例 36

```text
awaiting_registration
```

### 示例 37

```text
awaiting_verification
```

### 示例 38

```text
cancelled
```

### 示例 39

```text
cancelled_from_split_pending
```

### 示例 40

```text
client_arbitration
```

### 示例 41

```text
delivered
```

### 示例 42

```text
delivering
```

### 示例 43

```text
driver_pickup
```

### 示例 44

```text
not_accepted
```

### 示例 45

```text
posting_acceptance_in_progress
```

### 示例 46

```text
posting_in_arbitration
```

### 示例 47

```text
posting_created
```

### 示例 48

```text
posting_in_carriage
```

### 示例 49

```text
posting_not_in_carriage
```

### 示例 50

```text
posting_registered
```

### 示例 51

```text
posting_transferring_to_delivery
```

### 示例 52

```text
status=awaiting_deliver
```

### 示例 53

```text
posting_awaiting_passport_data
```

### 示例 54

```text
posting_created
```

### 示例 55

```text
posting_awaiting_registration
```

### 示例 56

```text
posting_registration_error
```

### 示例 57

```text
posting_transferring_to_delivery
```

### 示例 58

```text
status=awaiting_registration
```

### 示例 59

```text
posting_split_pending
```

### 示例 60

```text
posting_canceled
```

### 示例 61

```text
posting_in_client_arbitration
```

### 示例 62

```text
posting_delivered
```

### 示例 63

```text
posting_received
```

### 示例 64

```text
posting_conditionally_delivered
```

### 示例 65

```text
posting_in_courier_service
```

### 示例 66

```text
posting_in_pickup_point
```

### 示例 67

```text
posting_on_way_to_city
```

### 示例 68

```text
posting_on_way_to_pickup_point
```

### 示例 69

```text
posting_returned_to_warehouse
```

### 示例 70

```text
posting_transferred_to_courier_service
```

### 示例 71

```text
posting_driver_pick_up
```

### 示例 72

```text
posting_not_in_sort_center
```

### 示例 73

```text
ship_failed
```

### 示例 74

```text
posting_acceptance_in_progress
```

### 示例 75

```text
posting_in_arbitration
```

### 示例 76

```text
posting_created
```

### 示例 77

```text
posting_in_carriage
```

### 示例 78

```text
posting_not_in_carriage
```

### 示例 79

```text
posting_registered
```

### 示例 80

```text
posting_transferring_to_delivery
```

### 示例 81

```text
status=awaiting_deliver
```

### 示例 82

```text
posting_awaiting_passport_data
```

### 示例 83

```text
posting_created
```

### 示例 84

```text
posting_awaiting_registration
```

### 示例 85

```text
posting_registration_error
```

### 示例 86

```text
posting_transferring_to_delivery
```

### 示例 87

```text
status=awaiting_registration
```

### 示例 88

```text
posting_split_pending
```

### 示例 89

```text
posting_canceled
```

### 示例 90

```text
posting_in_client_arbitration
```

### 示例 91

```text
posting_delivered
```

### 示例 92

```text
posting_received
```

### 示例 93

```text
posting_conditionally_delivered
```

### 示例 94

```text
posting_in_courier_service
```

### 示例 95

```text
posting_in_pickup_point
```

### 示例 96

```text
posting_on_way_to_city
```

### 示例 97

```text
posting_on_way_to_pickup_point
```

### 示例 98

```text
posting_returned_to_warehouse
```

### 示例 99

```text
posting_transferred_to_courier_service
```

### 示例 100

```text
posting_driver_pick_up
```

### 示例 101

```text
posting_not_in_sort_center
```

### 示例 102

```text
ozon
```

### 示例 103

```text
aggregator
```

### 示例 104

```text
3pl_tracking
```

### 示例 105

```text
non_integrated
```

### 示例 106

```json
{
  "posting_number": "57195475-0050-3",
  "with": {
    "analytics_data": false,
    "barcodes": false,
    "financial_data": false,
    "legal_info": false,
    "product_exemplars": false,
    "related_postings": true,
    "translit": false
  }
}
```

### 示例 107

```json
{
  "result": {
    "posting_number": "0132112277-0101-1",
    "order_id": 35566798085,
    "order_number": "0132112277-0101",
    "status": "awaiting_packaging",
    "delivery_method": {
      "id": 1020005003107121,
      "name": "Ozon自发货，诺金斯克",
      "warehouse_id": 1020005003107121,
      "warehouse": "FBS LikeSK",
      "tpl_provider_id": 24,
      "tpl_provider": "Ozon配送"
    },
    "tracking_number": "",
    "tpl_integration_type": "ozon",
    "in_process_at": "2026-03-30T11:26:00Z",
    "shipment_date": "2026-03-31T09:00:00Z",
    "delivering_date": null,
    "provider_status": "",
    "delivery_price": "",
    "cancellation": {
      "cancel_reason_id": 0,
      "cancel_reason": "",
      "cancellation_type": "",
      "cancelled_after_ship": false,
      "affect_cancellation_rating": false,
      "cancellation_initiator": ""
    },
    "customer": null,
    "addressee": null,
    "products": [
      {
        "price": "1530.0000",
        "offer_id": "SK-58（深红色）",
        "name": "Cronier cr-2013专业非洲小卷卷发棒，9毫米",
        "sku": 827098843,
        "quantity": 1,
        "dimensions": {
          "height": "150.00",
          "length": "500.00",
          "weight": "550",
          "width": "300.00"
        },
        "currency_code": "RUB",
        "is_blr_traceable": false,
        "is_marketplace_buyout": false,
        "has_imei": false,
        "weight_max": 0.55,
        "weight_min": 0,
        "is_weight_needed": false
      }
    ],
    "barcodes": null,
    "analytics_data": null,
    "financial_data": null,
    "additional_data": [],
    "is_express": false,
    "requirements": {
      "products_requiring_gtd": [],
      "products_requiring_country": [],
      "products_requiring_mandatory_mark": [],
      "products_requiring_rnpt": [],
      "products_requiring_jw_uin": [],
      "products_requiring_change_country": [],
      "products_requiring_imei": [],
      "products_requiring_weight": []
    },
    "product_exemplars": null,
    "courier": null,
    "parent_posting_number": "",
    "related_postings": null,
    "available_actions": [
      "cancel",
      "has_barcode_for_printing",
      "product_cancel",
      "ship",
      "ship_async"
    ],
    "multi_box_qty": 1,
    "is_multibox": false,
    "substatus": "posting_created",
    "previous_substatus": "posting_split_pending",
    "prr_option": {
      "code": "",
      "price": "",
      "currency_code": "RUB",
      "floor": ""
    },
    "tariffication": {
      "current_tariff_rate": 1,
      "current_tariff_type": "no_discount",
      "current_tariff_charge": "",
      "current_tariff_charge_currency_code": "RUB",
      "next_tariff_rate": 1,
      "next_tariff_type": "commission",
      "next_tariff_charge": "50",
      "next_tariff_starts_at": "2026-03-31T09:00:01Z",
      "next_tariff_charge_currency_code": "RUB"
    },
    "destination_place_id": 0,
    "destination_place_name": "",
    "is_presortable": false,
    "pickup_code_verified_at": null,
    "optional": {
      "products_with_possible_mandatory_mark": []
    },
    "fact_delivery_date": null,
    "legal_info": {
      "company_name": "",
      "inn": "",
      "kpp": ""
    },
    "related_weight_postings": [],
    "shipment_date_without_delay": "2026-04-04T16:59:00Z",
    "require_blr_traceable_attrs": false,
    "is_click_and_collect": false,
    "tariffication_steps": [
      {
        "min_charge": null,
        "tariff_charge": {
          "amount": "0",
          "currency": "RUB"
        },
        "tariff_deadline_at": "2026-03-31T09:00:00Z",
        "tariff_rate": 0,
        "tariff_type": "no_discount"
      },
      {
        "min_charge": {
          "amount": "50",
          "currency": "RUB"
        },
        "tariff_charge": {
          "amount": "50",
          "currency": "RUB"
        },
        "tariff_deadline_at": "2026-03-31T21:00:00Z",
        "tariff_rate": 1,
        "tariff_type": "commission"
      },
      {
        "min_charge": {
          "amount": "50",
          "currency": "RUB"
        },
        "tariff_charge": {
          "amount": "50",
          "currency": "RUB"
        },
        "tariff_deadline_at": "2026-04-01T09:00:00Z",
        "tariff_rate": 1,
        "tariff_type": "commission"
      },
      {
        "min_charge": {
          "amount": "100",
          "currency": "RUB"
        },
        "tariff_charge": {
          "amount": "100",
          "currency": "RUB"
        },
        "tariff_deadline_at": "2026-04-01T21:00:00Z",
        "tariff_rate": 2,
        "tariff_type": "commission"
      },
      {
        "min_charge": {
          "amount": "100",
          "currency": "RUB"
        },
        "tariff_charge": {
          "amount": "100",
          "currency": "RUB"
        },
        "tariff_deadline_at": "2026-04-02T09:00:00Z",
        "tariff_rate": 2,
        "tariff_type": "commission"
      },
      {
        "min_charge": {
          "amount": "150",
          "currency": "RUB"
        },
        "tariff_charge": {
          "amount": "150",
          "currency": "RUB"
        },
        "tariff_deadline_at": "9999-12-31T23:59:59.999999900Z",
        "tariff_rate": 3,
        "tariff_type": "commission"
      }
    ]
  }
}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

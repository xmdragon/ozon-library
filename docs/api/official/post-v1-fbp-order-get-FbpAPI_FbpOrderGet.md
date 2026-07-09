# 获取关于特定交货的信息

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/fbp/order/get`
- Operation ID：`FbpAPI_FbpOrderGet`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/FbpAPI_FbpOrderGet
- 分组：`fbp`

## 页面标题结构

- 获取关于特定交货的信息
- Request Body schema: application/json
- 回复
- Response Schema: application/json
- 请求范例
- 回复范例

## 参数与返回结构

### 表格 0

| 字段 | 类型/说明 |
| --- | --- |
| `supply_id` required | string 交货标识符。 |

### 表格 1

| 字段 | 类型/说明 |
| --- | --- |
| `attention_reasons` | Array of strings Default: "ORDER_ATTENTION_TYPE_UNSPECIFIED"Items Enum: "ORDER_ATTENTION_TYPE_UNSPECIFIED" "OLD" "TIME_SLOT_EXPIRED" 警告原因： ORDER_ATTENTION_TYPE_UNSPECIFIED——未指定； OLD——过期申请； TIME_SLOT_EXPIRED——时间段已过期。 |
| `bundle_uuid` | string 组成商品标识符。 |
| `can_be_cancelled` | boolean true，如果申请可以取消。 |
| `cancellation_state` | object 取消原因。 |
| `created_date` | string <date-time> 交货创建日期。 |
| `delivery_details` | object 配送详情。 |
| `draft_id` | integer <int64> 草稿标识符。 |
| `has_consignment_note` | boolean true，如果有已签署的文件。 |
| `has_label` | boolean true，如果有标签。 |
| `id` | integer <int64> 交货申请标识符。 |
| `locked` | boolean true，如果无法编辑交货。 |
| `order_number` | string 交货编号。 |
| `package_units_count` | integer <int32> 货位数量。 |
| `receive_date` | string <date-time> 交货接收日期和时间。 |
| `row_version` | integer <int64> 草稿的当前版本标识符。 |
| `status` | string Default: "ORDER_STATUS_UNSPECIFIED" Enum: "ORDER_STATUS_UNSPECIFIED" "READY_TO_SUPPLY" "FILLING_DELIVERY_DETAILS" "COURIER_ASSIGNED" "COURIER_PICKED_UP" "ACCEPTANCE_AT_DROP_OFF_POINT" "IN_TRANSIT_TO_STORAGE_WAREHOUSE" "ACCEPTANCE_AT_STORAGE_WAREHOUSE" "CANCELLED" 订单状态： ORDER_STATUS_UNSPECIFIED——未指定； READY_TO_SUPPLY——准备发运； FILLING_DELIVERY_DETAILS——填写交货数据； COURIER_ASSIGNED——已分配快递员； COURIER_PICKED_UP——快递员已取件； ACCEPTANCE_AT_DROP_OFF_POINT——已在揽收点接收； IN_TRANSIT_TO_STORAGE_WAREHOUSE——在运往存储仓库的途中； ACCEPTANCE_AT_STORAGE_WAREHOUSE——仓库验收中； CANCELLED——申请已取消。 |
| `supply_id` | string 交货申请标识符。 |
| `warehouse_id` | integer <int64> 仓库标识符。 |

## 示例

### 示例 0

```text
ORDER_ATTENTION_TYPE_UNSPECIFIED
```

### 示例 1

```text
OLD
```

### 示例 2

```text
TIME_SLOT_EXPIRED
```

### 示例 3

```text
true
```

### 示例 4

```text
true
```

### 示例 5

```text
true
```

### 示例 6

```text
true
```

### 示例 7

```text
ORDER_STATUS_UNSPECIFIED
```

### 示例 8

```text
READY_TO_SUPPLY
```

### 示例 9

```text
FILLING_DELIVERY_DETAILS
```

### 示例 10

```text
COURIER_ASSIGNED
```

### 示例 11

```text
COURIER_PICKED_UP
```

### 示例 12

```text
ACCEPTANCE_AT_DROP_OFF_POINT
```

### 示例 13

```text
IN_TRANSIT_TO_STORAGE_WAREHOUSE
```

### 示例 14

```text
ACCEPTANCE_AT_STORAGE_WAREHOUSE
```

### 示例 15

```text
CANCELLED
```

### 示例 16

```json
{
  "supply_id": "string"
}
```

### 示例 17

```json
{
  "attention_reasons": "ORDER_ATTENTION_TYPE_UNSPECIFIED",
  "bundle_uuid": "string",
  "can_be_cancelled": true,
  "cancellation_state": {
    "cancellation_error": {
      "error_code": "CODE_UNSPECIFIED",
      "message": "string"
    },
    "cancellation_status": "STATUS_UNSPECIFIED"
  },
  "created_date": "2019-08-24T14:15:22Z",
  "delivery_details": {
    "direct_details": {
      "by_seller_details": {
        "driver_name": "string",
        "vehicle_registration_number": "string",
        "vehicle_type": "string"
      },
      "by_tpl_details": {
        "tracking_number": "string",
        "transport_company_name": "string"
      },
      "timeslot_details": {
        "timeslot": {
          "timeslot_end": "2019-08-24T14:15:22Z",
          "timeslot_start": "2019-08-24T14:15:22Z"
        },
        "timeslot_reservation_id": "string"
      }
    },
    "drop_off_point": {
      "id": 0,
      "province_uuid": "string",
      "timeslot": {
        "timeslot_end": "2019-08-24T14:15:22Z",
        "timeslot_start": "2019-08-24T14:15:22Z"
      }
    },
    "pickup_details": {
      "address": "string",
      "comment": "string",
      "date": "2019-08-24T14:15:22Z",
      "sender_name": "string",
      "sender_phone": "string"
    },
    "supply_type": "SUPPLY_TYPE_UNSPECIFIED"
  },
  "draft_id": 0,
  "has_consignment_note": true,
  "has_label": true,
  "id": 0,
  "locked": true,
  "order_number": "string",
  "package_units_count": 0,
  "receive_date": "2019-08-24T14:15:22Z",
  "row_version": 0,
  "status": "ORDER_STATUS_UNSPECIFIED",
  "supply_id": "string",
  "warehouse_id": 0
}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

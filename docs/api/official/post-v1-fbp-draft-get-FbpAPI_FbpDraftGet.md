# 获取交货草稿信息

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/fbp/draft/get`
- Operation ID：`FbpAPI_FbpDraftGet`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/FbpAPI_FbpDraftGet
- 分组：`fbp`

## 页面标题结构

- 获取交货草稿信息
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
| `bundle_id` | string 验证后商品的列表标识符。 |
| `cancellation_state` | object 取消原因。 |
| `created_at` | string <date-time> 草稿创建日期。 |
| `decline_reason` | object 拒绝原因。 |
| `deleted_at` | string <date-time> 草稿删除日期。 |
| `delivery_details` | object 配送详细信息。 |
| `editable` | boolean true，如果草稿可以修改。 |
| `id` | integer <int64> 草稿标识符。 |
| `is_cancelable` | boolean true，如果草稿可以取消。 |
| `is_deletable` | boolean true，如果草稿可以删除。 |
| `is_registration_available` | boolean true，如果可注册。 |
| `locked` | boolean true，如果草稿被封锁。 |
| `package_units_count` | integer <int32> 货位数量。 |
| `row_version` | integer <int64> 草稿的当前版本标识符。 |
| `status` | string Default: "DRAFT_STATUS_UNSPECIFIED" Enum: "DRAFT_STATUS_UNSPECIFIED" "NEW" "SUPPLY_VARIANT_CONFIRMATION" "SUPPLY_NOT_CONFIRMED" 草稿状态: DRAFT_STATUS_UNSPECIFIED — 未定义; NEW — 新的; SUPPLY_VARIANT_CONFIRMATION — 等待确认; SUPPLY_NOT_CONFIRMED — 仓库拒收. |
| `supply_id` | string 交货标识符。 |
| `warehouse_id` | integer <int64> 仓库标识符。 |

## 示例

### 示例 0

```text
true
```

### 示例 1

```text
true
```

### 示例 2

```text
true
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
DRAFT_STATUS_UNSPECIFIED
```

### 示例 6

```text
NEW
```

### 示例 7

```text
SUPPLY_VARIANT_CONFIRMATION
```

### 示例 8

```text
SUPPLY_NOT_CONFIRMED
```

### 示例 9

```json
{
  "supply_id": "string"
}
```

### 示例 10

```json
{
  "bundle_id": "string",
  "cancellation_state": {
    "cancellation_error": {
      "error_code": "CODE_UNSPECIFIED",
      "message": "string"
    },
    "cancellation_status": "STATUS_UNSPECIFIED"
  },
  "created_at": "2019-08-24T14:15:22Z",
  "decline_reason": {
    "failed_sku_ids": [
      "string"
    ],
    "message": "string"
  },
  "deleted_at": "2019-08-24T14:15:22Z",
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
  "editable": true,
  "id": 0,
  "is_cancelable": true,
  "is_deletable": true,
  "is_registration_available": true,
  "locked": true,
  "package_units_count": 0,
  "row_version": 0,
  "status": "DRAFT_STATUS_UNSPECIFIED",
  "supply_id": "string",
  "warehouse_id": 0
}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

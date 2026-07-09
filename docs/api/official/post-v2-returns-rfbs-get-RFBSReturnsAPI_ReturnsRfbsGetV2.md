# 退货申请信息

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v2/returns/rfbs/get`
- Operation ID：`RFBSReturnsAPI_ReturnsRfbsGetV2`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/RFBSReturnsAPI_ReturnsRfbsGetV2
- 分组：`returns`

## 页面标题结构

- 退货申请信息
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
| `return_id` required | integer <int64> 退货申请标识符。通过方法 /v2/returns/rfbs/list 获取。 |

### 表格 2

| 字段 | 类型/说明 |
| --- | --- |
| `returns` | object 申请信息。 |
| `available_actions` | Array of objects 申请的可用操作的信息。 |
| `client_name` | string Deprecated 买家姓名。 |
| `client_photo` | Array of strings 商品照片链接。 |
| `client_return_method_type` | object 退货方式信息。 |
| `comment` | string 买家评论。 |
| `created_at` | string <date-time> 申请创建日期。 |
| `order_number` | string 订单号。 |
| `posting_number` | string 货件编号。 |
| `product` | object 商品信息。 |
| `rejection_comment` | string 有关申请被拒绝的备注。 |
| `rejection_reason` | Array of objects 申请被拒绝的原因的信息。 |
| `return_method_description` | string 商品退货方式。 |
| `return_number` | string 退货申请编号。 |
| `return_reason` | object 退货原因信息。 |
| `ru_post_tracking_number` | string 跟踪号码。 |
| `state` | object 退货状态信息。 |
| `warehouse_id` | integer <int64> 仓库标识符。 |

### 表格 3

| 字段 | 类型/说明 |
| --- | --- |
| `available_actions` | Array of objects 申请的可用操作的信息。 |
| `client_name` | string Deprecated 买家姓名。 |
| `client_photo` | Array of strings 商品照片链接。 |
| `client_return_method_type` | object 退货方式信息。 |
| `comment` | string 买家评论。 |
| `created_at` | string <date-time> 申请创建日期。 |
| `order_number` | string 订单号。 |
| `posting_number` | string 货件编号。 |
| `product` | object 商品信息。 |
| `rejection_comment` | string 有关申请被拒绝的备注。 |
| `rejection_reason` | Array of objects 申请被拒绝的原因的信息。 |
| `return_method_description` | string 商品退货方式。 |
| `return_number` | string 退货申请编号。 |
| `return_reason` | object 退货原因信息。 |
| `ru_post_tracking_number` | string 跟踪号码。 |
| `state` | object 退货状态信息。 |
| `warehouse_id` | integer <int64> 仓库标识符。 |

## 示例

### 示例 0

```json
{
  "return_id": 0
}
```

### 示例 1

```json
{
  "returns": {
    "available_actions": [
      {
        "action": {
          "id": 0,
          "name": "string"
        }
      }
    ],
    "client_name": "string",
    "client_photo": [
      "string"
    ],
    "client_return_method_type": {
      "id": 0,
      "name": "string"
    },
    "comment": "string",
    "created_at": "2025-09-04T13:49:20.340Z",
    "order_number": "string",
    "posting_number": "string",
    "product": {
      "currency_code": "string",
      "name": "string",
      "offer_id": "string",
      "price": 0,
      "sku": 0
    },
    "rejection_comment": "string",
    "rejection_reason": [
      {
        "hint": "string",
        "id": 0,
        "is_comment_required": true,
        "name": "string"
      }
    ],
    "return_method_description": "string",
    "return_number": "string",
    "return_reason": {
      "id": 0,
      "is_defect": true,
      "name": "string"
    },
    "ru_post_tracking_number": "string",
    "state": {
      "state": "string",
      "state_name": "string"
    },
    "warehouse_id": 0
  }
}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

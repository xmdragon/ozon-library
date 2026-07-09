# 更新“基于订单总额的折扣”机制的促销活动

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/seller-actions/update/discount-with-condition`
- Operation ID：`SellerActionsUpdateDiscountWithCondition`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/SellerActionsUpdateDiscountWithCondition
- 分组：`seller-actions`

## 页面标题结构

- 更新“基于订单总额的折扣”机制的促销活动
- header Parameters
- Request Body schema: application/json
- 回复
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
| `action_id` | integer <uint64> 促销活动标识符。 |
| `action_parameters` | object 促销活动参数。 |

## 示例

### 示例 0

```json
{"action_id": 0,"action_parameters": {"date_end": "2019-08-24T14:15:22Z","date_start": "2019-08-24T14:15:22Z","discount_value": 0,"min_order_amount": 0,"title": "string"}}
```

### 示例 1

```json
{"code": 0,"details": [{"typeUrl": "string","value": "string"}],"message": "string"}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

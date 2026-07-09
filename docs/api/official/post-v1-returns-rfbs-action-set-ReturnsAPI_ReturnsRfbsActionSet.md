# 传递 rFBS 退货的可用操作

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/returns/rfbs/action/set`
- Operation ID：`ReturnsAPI_ReturnsRfbsActionSet`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/ReturnsAPI_ReturnsRfbsActionSet
- 分组：`returns`

## 页面标题结构

- 传递 rFBS 退货的可用操作
- Request Body schema: application/json
- 回复
- 请求范例
- 回复范例

## 参数与返回结构

### 表格 0

| 字段 | 类型/说明 |
| --- | --- |
| `comment` | string 卖家评论。 对于 id: -1 和 id: -10，备注为必填项。 |
| `compensation_amount` | number <double> 赔偿金额。 对于 id: 1020，备注也为必填项。 |
| `id` | integer <int32> 操作标识符。 获取可用操作 returns.available_actions ，请使用方法 /v2/returns/rfbs/get。 |
| `rejection_reason_id` | integer <int32> 取消原因的标识符。 对于 id: -1 和 id: -10，备注为必填项。 获取可用取消原因 returns.rejection_reason，请使用方法 /v2/returns/rfbs/get。 |
| `return_for_back_way` | number <double> 退还给买家的商品运费金额。 负值将被视为 0。 |
| `return_id` required | integer <int64> 退货申请的标识符。 |

## 示例

### 示例 0

```text
id: -1
```

### 示例 1

```text
id: -10
```

### 示例 2

```text
id: 1020
```

### 示例 3

```text
returns.available_actions
```

### 示例 4

```text
id: -1
```

### 示例 5

```text
id: -10
```

### 示例 6

```text
returns.rejection_reason
```

### 示例 8

```json
{"comment": "string","compensation_amount": 0,"id": 0,"rejection_reason_id": 0,"return_for_back_way": 0,"return_id": 0}
```

### 示例 9

```json
{"code": 0,"details": [{"typeUrl": "string","value": "string"}],"message": "string"}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

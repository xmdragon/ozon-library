# 拒绝退货申请

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v2/returns/rfbs/reject`
- Operation ID：`RFBSReturnsAPI_ReturnsRfbsRejectV2`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/RFBSReturnsAPI_ReturnsRfbsRejectV2
- 分组：`returns`

## 页面标题结构

- 拒绝退货申请
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
| `return_id` required | integer <int64> 退货申请的标识符。 |
| `comment` | string 备注。 如果 /v2/returns/rfbs/get 方法的响应中 rejection_reason.is_comment_required 参数为 true，则传递备注。 |
| `rejection_reason_id` required | integer <int64> 取消原因的标识符。 从 /v2/returns/rfbs/get 响应中获取的原因列表中传递标识符，参数为 rejection_reason。 |

## 示例

### 示例 0

```text
comment
```

### 示例 1

```text
rejection_reason.is_comment_required
```

### 示例 2

```text
true
```

### 示例 3

```text
rejection_reason
```

### 示例 4

```json
{"return_id": 0,"comment": "string","rejection_reason_id": 0}
```

### 示例 5

```json
{ }
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

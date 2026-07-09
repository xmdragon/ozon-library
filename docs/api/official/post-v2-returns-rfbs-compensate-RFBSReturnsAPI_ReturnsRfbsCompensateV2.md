# 退还部分商品金额

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v2/returns/rfbs/compensate`
- Operation ID：`RFBSReturnsAPI_ReturnsRfbsCompensateV2`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/RFBSReturnsAPI_ReturnsRfbsCompensateV2
- 分组：`returns`

## 页面标题结构

- 退还部分商品金额
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
| `compensation_amount` | string 赔偿金额。 |
| `return_id` required | integer <int64> 退货申请的标识符。 |

## 示例

### 示例 0

```json
{
  "compensation_amount": "string",
  "return_id": 0
}
```

### 示例 1

```json
{}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

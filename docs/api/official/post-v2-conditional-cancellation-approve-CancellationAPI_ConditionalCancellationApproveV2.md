# 确认 rFBS 取消申请

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v2/conditional-cancellation/approve`
- Operation ID：`CancellationAPI_ConditionalCancellationApproveV2`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/CancellationAPI_ConditionalCancellationApproveV2
- 分组：`conditional-cancellation`

## 页面标题结构

- 确认 rFBS 取消申请
- Request Body schema: application/json
- 回复
- 请求范例
- 回复范例

## 参数与返回结构

### 表格 0

cancellation_id required integer <int64> 取消申请标识符。 commentstring 备注。

## 示例

### 示例 0

```text
ON_APPROVAL
```

### 示例 1

```json
{"cancellation_id": 0,"comment": "string"}
```

### 示例 2

```json
{"code": 0,"details": [{"typeUrl": "string","value": "string"}],"message": "string"}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

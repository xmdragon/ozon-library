# 货件取消原因

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v2/posting/fbs/cancel-reason/list`
- Operation ID：`PostingAPI_GetPostingFbsCancelReasonList`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/PostingAPI_GetPostingFbsCancelReasonList
- 分组：`posting`

## 页面标题结构

- 货件取消原因
- header Parameters
- 回复
- Response Schema: application/json
- 回复范例

## 参数与返回结构

### 表格 0

Client-Id required string 用户识别号。 Api-Key required string API-密钥。

### 表格 1

resultArray of objects 方法操作结果。 Array ()idinteger <int64> 取消原因ID。 is_available_for_cancellationboolean 取消装运结果。 true, 如果请求可以取消。 titlestring 类别名称。 type_idstring 取消货件ID： buyer — 买家， seller — 卖家。

### 表格 2

idinteger <int64> 取消原因ID。 is_available_for_cancellationboolean 取消装运结果。 true, 如果请求可以取消。 titlestring 类别名称。 type_idstring 取消货件ID： buyer — 买家， seller — 卖家。

## 示例

### 示例 0

```json
{"result": [{"id": 352,"title": "在卖家仓库中已无商品","type_id": "seller","is_available_for_cancellation": true},{"id": 401,"title": "卖家拒绝了仲裁","type_id": "seller","is_available_for_cancellation": false},{"id": 402,"title": "其他（卖家的其他过错）","type_id": "seller","is_available_for_cancellation": true},{"id": 666,"title": "快递服务退货：在该区域没有快递","type_id": "seller","is_available_for_cancellation": false}]}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

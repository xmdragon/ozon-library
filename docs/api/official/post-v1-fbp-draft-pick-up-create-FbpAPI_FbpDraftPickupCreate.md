# 创建 pick-up 交货申请草稿

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/fbp/draft/pick-up/create`
- Operation ID：`FbpAPI_FbpDraftPickupCreate`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/FbpAPI_FbpDraftPickupCreate
- 分组：`fbp`

## 页面标题结构

- 创建 pick-up 交货申请草稿
- Request Body schema: application/json
- 回复
- Response Schema: application/json
- 请求范例
- 回复范例

## 参数与返回结构

### 表格 0

| 字段 | 类型/说明 |
| --- | --- |
| `bundle_id` required | string 已校验商品列表的标识符。 |
| `delivery_details` required | object 配送详细信息。 |
| `package_units_count` required | integer <int32> 包装单位数量。 |
| `warehouse_id` required | integer <int64> 仓库标识符。 |

### 表格 1

| 字段 | 类型/说明 |
| --- | --- |
| `draft_id` | integer <int64> 草稿标识符。 |
| `row_version` | integer <int64> 草稿的当前版本标识符。 |
| `supply_id` | string 交货标识符。 |

## 示例

### 示例 0

```json
{
  "bundle_id": "string",
  "delivery_details": {
    "address": "string",
    "comment": "string",
    "date": "2019-08-24T14:15:22Z",
    "sender_name": "string",
    "sender_phone": "string"
  },
  "package_units_count": 0,
  "warehouse_id": 0
}
```

### 示例 1

```json
{
  "draft_id": 0,
  "row_version": 0,
  "supply_id": "string"
}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

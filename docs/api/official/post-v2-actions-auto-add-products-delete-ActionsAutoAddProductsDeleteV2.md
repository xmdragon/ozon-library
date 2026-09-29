# 从促销活动自动添加列表中删除商品

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v2/actions/auto-add/products/delete`
- Operation ID：`ActionsAutoAddProductsDeleteV2`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/#operation/ActionsAutoAddProductsDeleteV2
- 分组：`actions`

## 页面标题结构

- 从促销活动自动添加列表中删除商品
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
| `action_id` required | integer <uint64> 促销活动标识符。 |
| `auto_add_date` required | string <date-time> 方法 /v1/actions 响应中 result.auto_add_dates 参数里的商品自动添加到促销活动中的日期和时间。 |
| `product_ids` required | Array of strings <uint64> <= 1000 items Ozon系统中的商品标识符，即 product_id 。 |

### 表格 2

| 字段 | 类型/说明 |
| --- | --- |
| `product_ids` | Array of strings <uint64> 已从自动添加中删除的商品ID。 |

## 示例

### 示例 0

```json
{
  "action_id": 250204,
  "product_ids": [
    88888
  ],
  "auto_add_date": "2025-01-01T00:00:00Z"
}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

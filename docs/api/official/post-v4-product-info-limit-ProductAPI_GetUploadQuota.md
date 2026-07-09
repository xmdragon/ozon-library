# 品类限制、商品的创建和更新

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v4/product/info/limit`
- Operation ID：`ProductAPI_GetUploadQuota`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/ProductAPI_GetUploadQuota
- 分组：`product`

## News 更新标记

| 日期 | 标记 | 摘要 | 来源 |
| --- | --- | --- | --- |
| 2026-06-09 | `added_field` | /v4/product/info/limit 在方法的响应中添加了参数 operation_limits和total.quota_by_category的说明。 | [官方 News](https://docs.ozon.ru/api/seller/zh/#section/202669) |
| 2025-09-24 | `updated` | /v4/product/info/limit 更新了方法响应中的 total.limit、daily_create.limit 和 daily_update.limit 参数描述。 | [官方 News](https://docs.ozon.ru/api/seller/zh/#section/2025924) |

## 页面标题结构

- 品类限制、商品的创建和更新
- header Parameters
- 回复
- Response Schema: application/json
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
| `daily_create` | object 创建商品的每日限制。 |
| `daily_update` | object 商品更新的每日限制。 |
| `operation_limits` | object 商品操作的可用限额。 |
| `total` | object 品类限制。 |

## 示例

### 示例 0

```json
{
  "daily_create": {
    "limit": 0,
    "reset_at": "2019-08-24T14:15:22Z",
    "usage": 0
  },
  "daily_update": {
    "limit": 0,
    "reset_at": "2019-08-24T14:15:22Z",
    "usage": 0
  },
  "operation_limits": {
    "limit": 0,
    "limit_type": "UNSPECIFIED"
  },
  "total": {
    "limit": 0,
    "usage": 0,
    "quota_by_category": {
      "category_id": 0,
      "limit": 0,
      "usage": 0
    }
  }
}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

# 策略列表

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/pricing-strategy/list`
- Operation ID：`pricing_list`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/pricing_list
- 分组：`pricing-strategy`

## 页面标题结构

- 策略列表
- Request Body schema: application/json
- 回复
- Response Schema: application/json
- 请求范例
- 回复范例

## 参数与返回结构

### 表格 0

| 字段 | 类型/说明 |
| --- | --- |
| `page` required | integer <int64> 卸载策略的列表页面。 最小值为1。 |
| `limit` required | integer <int64> 每页的最大策略数。有效值是从1到50。 |

### 表格 1

| 字段 | 类型/说明 |
| --- | --- |
| `strategies` | Array of objects 策略列表。 |
| `total` | integer <int32> 策略总数。 |

## 示例

### 示例 2

```text
50
```

### 示例 3

```json
{
  "page": 1,
  "limit": 20
}
```

### 示例 4

```json
{
  "strategies": [
    {
      "id": "2fb3e6a3-3db5-4bb4-8430-b2de39fc3265",
      "name": "策略_来自_CID7",
      "type": "COMP_PRICE",
      "update_type": "strategyEnabled",
      "updated_at": "2024-05-02 14:47:02.594774+00",
      "products_count": 1,
      "competitors_count": 1,
      "enabled": true
    }
  ],
  "total": 5
}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

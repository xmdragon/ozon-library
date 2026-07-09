# 竞争对手名单

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/pricing-strategy/competitors/list`
- Operation ID：`pricing_competitors`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/pricing_competitors
- 分组：`pricing-strategy`

## 页面标题结构

- 竞争对手名单
- Request Body schema: application/json
- 回复
- Response Schema: application/json
- 请求范例
- 回复范例

## 参数与返回结构

### 表格 0

| 字段 | 类型/说明 |
| --- | --- |
| `page` required | integer <int64> 需要下载竞争对手的列表页面。 最小值为1。 |
| `limit` required | integer <int64> 每页的最大竞争对手数。有效值是从1到50。 |

### 表格 1

| 字段 | 类型/说明 |
| --- | --- |
| `competitor` | Array of objects 竞争对手列表。 |
| `total` | integer <int32> 竞争对手总数。 |

## 示例

### 示例 2

```text
50
```

### 示例 3

```json
{"page": 1,"limit": 20}
```

### 示例 4

```json
{"competitor": [{"id": 7820251,"name": "grenmarketshop.ru"}],"total": 33}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

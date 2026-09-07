# 获取按文本筛选的搜索查询列表

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/search-queries/text`
- Operation ID：`SearchQueriesAPI_SearchQueriesText`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/#operation/SearchQueriesAPI_SearchQueriesText
- 分组：`search-queries`

## News 更新标记

| 日期 | 标记 | 摘要 | 来源 |
| --- | --- | --- | --- |
| 2025-11-11 | `new_method` | /v1/search-queries/text 已新增用于处理搜索查询的方法。 | [官方 News](https://docs.ozon.ru/api/seller/zh/#section/20251111) |

## 页面标题结构

- 获取按文本筛选的搜索查询列表
- HEADER PARAMETERS
- REQUEST BODY SCHEMA: application/json
- 回复
- RESPONSE SCHEMA: application/json
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
| `limit` required | string <int64> <= 50 每页的结果数量。 |
| `offset` required | string <int64> <= 50 响应中将被跳过的项目数量。 |
| `sort_by` | string Enum: "CLIENT_COUNT" "ADD_TO_CART" "CONVERSION_TO_CART" "AVG_PRICE" 排序搜索查询的参数： CLIENT_COUNT——查询的受欢迎程度； ADD_TO_CART——添加到购物车的次数； CONVERSION_TO_CART——购物车转化率； AVG_PRICE——平均价格。 |
| `sort_dir` | string Enum: "ASC" "DESC" 排序方向： ASC——升序； DESC——降序。 |
| `text` required | string 按文本搜索。 |

### 表格 2

| 字段 | 类型/说明 |
| --- | --- |
| `offset` | string <int64> К每页显示的搜索查询数量。 |
| `search_queries` | Array of objects 搜索查询信息。 |
| `total` | string <int64> 搜索查询总数。 |

## 示例

### 示例 0

```json
{
  "limit": "50",
  "offset": "0",
  "sort_by": "CLIENT_COUNT",
  "sort_dir": "ASC",
  "text": "string"
}
```

### 示例 1

```json
{
  "search_queries": [
    {
      "avg_price": 3786.6,
      "conversion_to_cart": 0.163,
      "client_count": 165418,
      "items_views": 140.828,
      "query": "куртка женская демисезон",
      "add_to_cart": 26977,
      "sellers_count": 63.833
    },
    {
      "avg_price": 3786.6,
      "conversion_to_cart": 0.163,
      "client_count": 165418,
      "items_views": 140.828,
      "query": "куртка женская демисезон",
      "add_to_cart": 26977,
      "sellers_count": 63.833
    }
  ],
  "offset": "string",
  "total": "string"
}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

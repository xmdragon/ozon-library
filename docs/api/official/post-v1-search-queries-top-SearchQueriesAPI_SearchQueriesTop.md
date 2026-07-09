# 获取热门搜索查询列表

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/search-queries/top`
- Operation ID：`SearchQueriesAPI_SearchQueriesTop`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/SearchQueriesAPI_SearchQueriesTop
- 分组：`search-queries`

## 页面标题结构

- 获取热门搜索查询列表
- header Parameters
- Request Body schema: application/json
- 回复
- Response Schema: application/json
- 请求范例
- 回复范例

## 参数与返回结构

### 表格 0

Client-Id required string 用户识别号。 Api-Key required string API-密钥。

### 表格 1

limit required string <int64> <= 50 每页的结果数量。 offset required string <int64> <= 1000 响应中将被跳过的项目数量。

### 表格 2

offsetstring <int64> 每页显示的搜索查询数量。 search_queriesArray of objects 搜索查询信息。 totalstring <int64> 搜索查询总数。

## 示例

### 示例 0

```json
{"limit": "50","offset": "0"}
```

### 示例 1

```json
{"search_queries": [{"avg_price": 3786.6,"conversion_to_cart": 0.163,"client_count": 165418,"items_views": 140.828,"query": "куртка женская демисезон","add_to_cart": 26977,"sellers_count": 63.833}],"offset": "1","total": "1"}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

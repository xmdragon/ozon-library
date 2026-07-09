# 有关特定商品查询的信息

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/analytics/product-queries/details`
- Operation ID：`AnalyticsAPI_AnalyticsProductQueriesDetails`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/AnalyticsAPI_AnalyticsProductQueriesDetails
- 分组：`analytics`

## 页面标题结构

- 有关特定商品查询的信息
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

date_from required string <date-time> 分析数据的起始日期。 date_tostring <date-time> 分析数据的结束日期。 limit_by_sku required integer <int32> 单个SKU的查询数量限制。最大值为15次查询。 pageinteger <int32> 请求返回的页码。最小值为0。 page_size required integer <int32> 每页包含的商品数量。最大值为100。 skus required Array of strings <int64> SKU 列表，即 Ozon 系统中的商品标识符。根据这些 SKU 返回搜索查询的分析数据。最多可查询 1000 个 SKU。 sort_bystring Default: "BY_SEARCHES" Enum: "BY_SEARCHES" "BY_VIEWS" "BY_POSITION" "BY_CONVERSION" "BY_GMV" 按具体参数对商品进行排序。可能的取值： BY_SEARCHES— 按搜索次数； BY_VIEWS— 按浏览量； BY_POSITION— 按商品的平均排名； BY_CONVERSION— 按转化率； BY_GMV — 按搜索查询的销售额。 只有 Premium 或 Premium Plus 订阅，才能按 BY_VIEWS、BY_POSITION 和 BY_CONVERSION 排序。 sort_dirstring Default: "DESCENDING" Enum: "DESCENDING" "ASCENDING" 排序方向： DESCENDING— 降序； ASCENDING— 升序。

### 表格 2

analytics_periodobject 数据分析的时间范围。 page_countinteger <int64> 总页数。 queriesArray of objects 查询列表。 totalinteger <int64> 搜索请求的总数。

## 示例

### 示例 0

```text
BY_SEARCHES
```

### 示例 1

```text
BY_VIEWS
```

### 示例 2

```text
BY_POSITION
```

### 示例 3

```text
BY_CONVERSION
```

### 示例 4

```text
BY_GMV
```

### 示例 5

```text
BY_VIEWS
```

### 示例 6

```text
BY_POSITION
```

### 示例 7

```text
BY_CONVERSION
```

### 示例 8

```text
DESCENDING
```

### 示例 9

```text
ASCENDING
```

### 示例 10

```json
{"date_from": "2019-08-24T14:15:22Z","date_to": "2019-08-24T14:15:22Z","limit_by_sku": 0,"page": 0,"page_size": 1000,"skus": ["string"],"sort_by": "BY_SEARCHES","sort_dir": "DESCENDING"}
```

### 示例 11

```json
{"analytics_period": {"date_from": "string","date_to": "string"},"page_count": 0,"queries": [{"currency": "string","gmv": 0,"order_count": 0,"position": 0,"query": "string","query_index": 0,"sku": 0,"unique_search_users": 0,"unique_view_users": 0,"view_conversion": 0}],"total": 0}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

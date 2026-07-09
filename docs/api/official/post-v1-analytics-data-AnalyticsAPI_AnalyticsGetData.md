# 分析数据

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/analytics/data`
- Operation ID：`AnalyticsAPI_AnalyticsGetData`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/AnalyticsAPI_AnalyticsGetData
- 分组：`analytics`

## 页面标题结构

- 分析数据
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

date_from required string 数据将出现在报告中的日期。 若您没有Premium订阅，请指定过去三个月内的日期。 date_to required string 数据将出现在报告中的截止日期。 dimension required Array of stringsItems Enum: "unknownDimension" "sku" "spu" "day" "week" "month" "year" "category1" "category2" "brand" "modelID" "descriptionType" 报告中的分组数据。 所有卖家可用的分组方法： unknownDimension — 未知商品标识符； sku — 商品标识符； spu — 商品标识符 — 统一商品卡片； day — 日； week — 星期； month — 月。 只有Premium订阅卖家才能使用的分组方法： year — 年； category1 — 一级类别； category2 — 二级类别； brand — 品牌； modelID — 型号； descriptionType — 商品类型。 filtersArray of objects 过滤器。 limit required integer <int64> 响应的值个数： 最大值 — 1000， 最小值 — 1. metrics required Array of stringsItems Enum: "unknown_metric" "hits_view_search" "hits_view_pdp" "hits_view" "hits_tocart_search" "hits_tocart_pdp" "hits_tocart" "session_view_search" "session_view_pdp" "session_view" "conv_tocart_search" "conv_tocart_pdp" "conv_tocart" "revenue" "returns" "cancellations" "ordered_units" "delivered_units" "adv_view_pdp" "adv_view_search_category" "adv_view_all" "adv_sum_all" "position_category" "postings" "postings_premium" 最多指定14个指标。如有更多，您将收到 InvalidArgument的错误。 生成报告所依据的指标列表。 所有卖家可用的指标： revenue — 订购的金额， ordered_units — 订购的商品。 仅对Premium订阅卖家可用的指标： unknown_metric — 未知指标。 hits_view_search — 在搜索和类别中的指标。 hits_view_pdp — 商品卡片上的指标。 hits_view — 总展示次数。 hits_tocart_search — 从搜索或类别添加到购物车。 hits_tocart_pdp — 从商品卡片添加到购物车。 hits_tocart — 添加到购物车的总数。 session_view_search — 带有在搜索结果或目录中展示的会话。计算在搜索结果或目录中有浏览的唯一身份访问者。 session_view_pdp — 在商品卡片上显示的会话。计算查看过商品卡片的唯一身份访问者。 session_view — 所有会话。计算唯一身份访问者。 conv_tocart_search — 从商品卡片转换到购物车。 conv_tocart_pdp — 从商品卡片转换到购物车的总转化率。 conv_toca

### 表格 2

resultobject 查询结果。 dataArray of objects 数据组。 totalsArray of numbers <double> 指标总计和平均值。 timestampstring 报告创建时间。

### 表格 3

dataArray of objects 数据组。 totalsArray of numbers <double> 指标总计和平均值。

## 示例

### 示例 0

```json
{"date_from": "2020-09-01","date_to": "2021-10-15","metrics": ["hits_view_search"],"dimension": ["sku","day"],"filters": [ ],"sort": [{"key": "hits_view_search","order": "DESC"}],"limit": 1000,"offset": 0}
```

### 示例 1

```json
{"result": {"data": [ ],"totals": [0]},"timestamp": "2021-11-25 15:19:21"}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

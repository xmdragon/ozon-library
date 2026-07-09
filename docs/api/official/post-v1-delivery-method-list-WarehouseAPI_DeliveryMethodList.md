# 仓库物流方式清单

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/delivery-method/list`
- Operation ID：`WarehouseAPI_DeliveryMethodList`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/WarehouseAPI_DeliveryMethodList
- 分组：`delivery-method`

## 页面标题结构

- 仓库物流方式清单
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

filterobject 查找快递方式的过滤器。 limit required integer <int64> 回答中的元素数量。最多50，最少1。 offsetinteger <int64> 回答中会被略过的元素数量。例如，如果offset = 10，回答将从发现的第11个元素开始。

### 表格 2

has_nextboolean 以下该迹象会表明在查询中只送回了部分快递方式。 true — 请用新的 offset 参数重新请求，以获得剩余的方式； false — 回答中包含了所有应要求的快递方式。 resultArray of objects 查询结果。 Array ()company_idinteger <int64> 卖家识别号。 created_atstring <date-time> 创建快递方式的日期和时间。 cutoffstring 卖方必须在此之前备货的时间。 idinteger <int64> 快递方式识别号。 namestring 快递方式名称。 provider_idinteger <int64> 快递服务识别号。 sla_cut_ininteger <int64> 根据仓库设置，订单备货的最短时间（以分钟为单位）。 statusstring 快递方式状态: NEW — 已创建, EDITED — 正在编辑, ACTIVE — 已激活, DISABLED — 未激活。 template_idinteger <int64> 订单快递服务识别号。 updated_atstring <date-time> 快递方式最后更新的日期和时间。 warehouse_idinteger <int64> 仓库识别号。

### 表格 3

company_idinteger <int64> 卖家识别号。 created_atstring <date-time> 创建快递方式的日期和时间。 cutoffstring 卖方必须在此之前备货的时间。 idinteger <int64> 快递方式识别号。 namestring 快递方式名称。 provider_idinteger <int64> 快递服务识别号。 sla_cut_ininteger <int64> 根据仓库设置，订单备货的最短时间（以分钟为单位）。 statusstring 快递方式状态: NEW — 已创建, EDITED — 正在编辑, ACTIVE — 已激活, DISABLED — 未激活。 template_idinteger <int64> 订单快递服务识别号。 updated_atstring <date-time> 快递方式最后更新的日期和时间。 warehouse_idinteger <int64> 仓库识别号。

## 示例

### 示例 0

```text
NEW
```

### 示例 1

```text
EDITED
```

### 示例 2

```text
ACTIVE
```

### 示例 3

```text
DISABLED
```

### 示例 4

```json
{"filter": {"provider_id": 424,"status": "ACTIVE","warehouse_id": 15588127982000},"limit": 100,"offset": 0}
```

### 示例 5

```json
{"result": [{"id": 15588127982000,"company_id": 1,"name": "Ozon物流快递员，Yesipovo","status": "ACTIVE","cutoff": "13:00","provider_id": 24,"template_id": 0,"warehouse_id": 15588127982000,"created_at": "2019-04-04T15:22:31.048202Z","updated_at": "2021-08-15T10:21:44.854209Z","sla_cut_in": 1440}],"has_next": false}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

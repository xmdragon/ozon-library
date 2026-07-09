# 获取用于创建仓库的揽收点列表

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/warehouse/fbs/create/drop-off/list`
- Operation ID：`WarehouseAPI_ListDropOffPointsForCreateFBSWarehouse`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/WarehouseAPI_ListDropOffPointsForCreateFBSWarehouse
- 分组：`warehouse`

## 页面标题结构

- 获取用于创建仓库的揽收点列表
- Request Body schema: application/json
- 回复
- Response Schema: application/json
- 请求范例
- 回复范例

## 参数与返回结构

### 表格 0

coordinatesobject 坐标。 country_code required string ISO 2格式的国家代码。 is_kgt required boolean true表示商品为超大。 searchobject 搜索参数。

### 表格 1

pointsArray of objects 点位列表。 Array ()addressstring 揽收点地址。 coordinatesobject 揽收点坐标。 discount_percentnumber <float> 交付货件的折扣百分比。 idstring 揽收点标识符。 last_transit_time_localobject 为获得发运折扣，需要在此时间前交付货件。 typestring Enum: "PVZ" "PPZ" "SC" D揽收点类型： PVZ — 订单取货点， PPZ — 订单接收点， SC — 分拣中心。

### 表格 2

addressstring 揽收点地址。 coordinatesobject 揽收点坐标。 discount_percentnumber <float> 交付货件的折扣百分比。 idstring 揽收点标识符。 last_transit_time_localobject 为获得发运折扣，需要在此时间前交付货件。 typestring Enum: "PVZ" "PPZ" "SC" D揽收点类型： PVZ — 订单取货点， PPZ — 订单接收点， SC — 分拣中心。

## 示例

### 示例 0

```text
PVZ
```

### 示例 1

```text
PPZ
```

### 示例 2

```json
{"country_code": "RU","is_kgt": false,"coordinates": {"latitude": 55,"longitude": 37},"search": {"address": "москва","types": ["PPZ"]}}
```

### 示例 3

```json
{"points": [{"address": "Россия, Москва, Москва, Россия, г. Москва, Никольская улица, 7-9 строение 4","discount_percent": 1,"id": "1020002487458000","last_transit_time_local": {"hours": 12,"minutes": 0,"nanos": 0,"seconds": 0},"coordinates": {"latitude": 55.756107,"longitude": 37.620426},"type": "PVZ"}]}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

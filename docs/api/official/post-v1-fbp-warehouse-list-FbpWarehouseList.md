# 获取合作伙伴仓库列表

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/fbp/warehouse/list`
- Operation ID：`FbpWarehouseList`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/FbpWarehouseList
- 分组：`fbp`

## 页面标题结构

- 获取合作伙伴仓库列表
- header Parameters
- 回复
- Response Schema: application/json
- 回复范例

## 参数与返回结构

### 表格 0

Client-Id required string 用户识别号。 Api-Key required string API-密钥。

### 表格 1

warehousesArray of objects 仓库列表。 Array ()address_detailingobject 地址详情。 idinteger <int64> 仓库标识符。 is_bondedboolean true，表示该仓库为保税仓。 namestring 仓库名称。 partner_namestring 合作伙伴名称。 supply_typesArray of integers <int32> 交货类型。 timezone_namestring 仓库所在时区。

### 表格 2

address_detailingobject 地址详情。 idinteger <int64> 仓库标识符。 is_bondedboolean true，表示该仓库为保税仓。 namestring 仓库名称。 partner_namestring 合作伙伴名称。 supply_typesArray of integers <int32> 交货类型。 timezone_namestring 仓库所在时区。

## 示例

### 示例 0

```json
{"warehouses": [{"address_detailing": {"city": "string","country": "string","house": "string","region": "string","street": "string","zipcode": "string"},"id": 0,"is_bonded": true,"name": "string","partner_name": "string","supply_types": [0],"timezone_name": "string"}]}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

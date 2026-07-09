# 获取省份列表

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/fbp/draft/drop-off/province/list`
- Operation ID：`FbpDraftDropOffProvinceList`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/FbpDraftDropOffProvinceList
- 分组：`fbp`

## 页面标题结构

- 获取省份列表
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

warehouse_id required integer <int64> 仓库标识符。

### 表格 2

provincesArray of objects 省份列表。 Array ()namestring 省份名称。 points_countinteger <int32> 地图上接收点数量。 province_uuidstring 省份唯一标识符。

### 表格 3

namestring 省份名称。 points_countinteger <int32> 地图上接收点数量。 province_uuidstring 省份唯一标识符。

## 示例

### 示例 0

```json
{"warehouse_id": 0}
```

### 示例 1

```json
{"provinces": [{"name": "string","points_count": 0,"province_uuid": "string"}]}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

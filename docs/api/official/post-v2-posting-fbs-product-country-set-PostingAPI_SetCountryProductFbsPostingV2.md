# 添加商品产地信息

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v2/posting/fbs/product/country/set`
- Operation ID：`PostingAPI_SetCountryProductFbsPostingV2`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/PostingAPI_SetCountryProductFbsPostingV2
- 分组：`posting`

## 页面标题结构

- 添加商品产地信息
- Request Body schema: application/json
- 回复
- Response Schema: application/json
- 请求范例
- 回复范例

## 参数与返回结构

### 表格 0

posting_number required string 货运号。 product_id required integer <int64> 产品ID。 country_iso_code required string 根据标准ISO_3166-1添加的国家的两个字母代码 制造国家列表及其ISO代码可以使用该方法获得/v2/posting/fbs/product/country/list。

### 表格 1

product_idinteger <int64> 产品ID。 is_gtd_neededboolean 有必要传送产品和货运的货物报关单（Cargo Customs Declaration）编号的标志。

## 示例

### 示例 0

```json
{"country_iso_code": "NO","posting_number": "57195475-0050-3","product_id": 180550365}
```

### 示例 1

```json
{"product_id": 180550365,"is_gtd_needed": true}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

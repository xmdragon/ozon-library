# 根据属性的参考值进行搜索

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/description-category/attribute/values/search`
- Operation ID：`DescriptionCategoryAPI_SearchAttributeValues`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/DescriptionCategoryAPI_SearchAttributeValues
- 分组：`description-category`

## 页面标题结构

- 根据属性的参考值进行搜索
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

attribute_id required integer <int64> 属性的标识符。可以使用方法 /v1/description-category/attribute获取。 description_category_id required integer <int64> 类目的标识符。可以使用方法 /v1/description-category/tree获取。 limit required integer <int64> 返回结果中的值数量：: 最大值 — 100， 最小值 — 1。 type_id required integer <int64> 商品类型的标识符。可以使用方法 /v1/description-category/tree获取。 value required string 系统将根据此值搜索参考值。最少需要2个字符。

### 表格 2

resultArray of objects 属性值。 Array ()idinteger <int64> 属性值的标识符。 infostring 额外信息。 picturestring 图片链接。 valuestring

### 表格 3

idinteger <int64> 属性值的标识符。 infostring 额外信息。 picturestring 图片链接。 valuestring

## 示例

### 示例 0

```json
{"attribute_id": 85,"description_category_id": 17054869,"limit": 100,"type_id": 97311,"value": "Name"}
```

### 示例 1

```json
{"result": [{"id": 1,"info": "黑色商品","picture": "https://example.com/images/color_black.jpg","value": "黑色"}]}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

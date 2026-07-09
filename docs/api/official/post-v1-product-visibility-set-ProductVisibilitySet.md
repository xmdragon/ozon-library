# 新增了用于设置商品在Ozon和Ozon Select橱窗可见性的Beta方法。

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/product/visibility/set`
- Operation ID：`ProductVisibilitySet`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/ProductVisibilitySet
- 分组：`product`

## 页面标题结构

- 新增了用于设置商品在Ozon和Ozon Select橱窗可见性的Beta方法。
- Request Body schema: application/json
- 回复
- Response Schema: application/json
- 请求范例
- 回复范例

## 参数与返回结构

### 表格 0

item_placement required Array of objects 商品可见性信息。

### 表格 1

itemsArray of objects 商品可见性信息。 items_errorsArray of objects 存在错误的商品。

## 示例

### 示例 0

```json
{"item_placement": [{"placement": "OZON","sku": 0}]}
```

### 示例 1

```json
{"items": [{"select_permission": "UNSPECIFIED","seller_item_placement": "UNSPECIFIED","seller_item_placement_list": ["UNSPECIFIED"],"showcases_visibility": "UNSPECIFIED","showcases_visibility_list": ["UNSPECIFIED"],"sku": 0,"warnings": ["string"]}],"items_errors": [{"code": "string","sku": 0}]}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

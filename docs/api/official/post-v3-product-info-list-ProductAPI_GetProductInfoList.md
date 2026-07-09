# 根据标识符获取商品信息

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v3/product/info/list`
- Operation ID：`ProductAPI_GetProductInfoList`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/ProductAPI_GetProductInfoList
- 分组：`product`

## 页面标题结构

- 根据标识符获取商品信息
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

offer_idArray of strings 商品在卖家系统中的标识符 — 货号。 product_idArray of strings <int64> Ozon系统中商品的标识符 — product_id。 skuArray of strings <int64> 商品在 Ozon 系统中的标识符 — SKU。

### 表格 2

itemsArray of objects 数据数组。 Array ()availabilitiesArray of objects 商品可售数量信息。 barcodesArray of strings 商品的所有条形码。 color_imageArray of strings 商品颜色图片。 commissionsArray of objects 佣金信息。 created_atstring <date-time> 商品的创建日期和时间。 currency_codestring 货币单位。 description_category_idinteger <int64> 类目标识符。 可与 /v1/description-category/attribute 和 /v1/description-category/attribute/values 方法配合使用。 discounted_fbo_stocksinteger <int32> Ozon 仓库中减价商品的库存。 errorsArray of objects 创建或验证商品时的错误信息。 has_discounted_fbo_itemboolean 商品在 Ozon 仓库中是否有减价版的同款商品。 idinteger <int64> 商品标识符。 imagesArray of strings 图片链接数组。 图片在数组中的顺序与网站上的展示顺序一致。 如果 primary_image 参数未指定，则数组中的第一张图片为商品主图。 images360Array of strings 360° 商品图片数组。 is_archivedboolean 如果商品是手动归档的，则为 true。 is_autoarchivedboolean 如果商品是自动归档的，则为 true。 is_discountedboolean 商品是否为减价商品： 如果商品是由卖家作为减价商品创建的，则为 true。 如果商品不是减价商品或是由Ozon减价的，则为 false。 is_kgtboolean true，表示商品为超大。仅适用于FBS模式。 is_prepayment_allowedboolean Deprecated 如果支持预付款，则为 true。 is_superboolean 超级商品标识。 有关超级商品的详细信息，请参考卖家知识库 min_pricestring 应用促销后的最低价格。 model_infoobject 商品型号信息。 namestring 名称。 offer_idstring 商品在卖家系统中的标识符 — 货号。 old_pricestring 不含折扣价格。在商品卡片上显示为划线价。 pricestring 商品的含折扣价格。该值将在商品卡片上显示。 price_indexesobject 商品价格指数。 primary_imageArray of strings 商品的主图。 promotionsArray of objects 促销活动。 skuinteger <int64> 商品在 Ozon 系统中的标识符 — SKU。 sourcesArray of objects 商品创建来源信息。自2023年7月1日起，卖家按SDS模式创建商品。 statusesobject 商品状态信息。 stocksobject 商品库存信息。 type_idinteger <int64> 商品类型标识符。 updated_atstring <date-time> 商品的最后更新时间。 vatstring 商品的增值税税率。 visibility_detailsobject 商品的可见性设置。 volume_weightnumber <double> 商品的体积重量。

### 表格 3

availabilitiesArray of objects 商品可售数量信息。 barcodesArray of strings 商品的所有条形码。 color_imageArray of strings 商品颜色图片。 commissionsArray of objects 佣金信息。 created_atstring <date-time> 商品的创建日期和时间。 currency_codestring 货币单位。 description_category_idinteger <int64> 类目标识符。 可与 /v1/description-category/attribute 和 /v1/description-category/attribute/values 方法配合使用。 discounted_fbo_stocksinteger <int32> Ozon 仓库中减价商品的库存。 errorsArray of objects 创建或验证商品时的错误信息。 has_discounted_fbo_itemboolean 商品在 Ozon 仓库中是否有减价版的同款商品。 idinteger <int64> 商品标识符。 imagesArray of strings 图片链接数组。 图片在数组中的顺序与网站上的展示顺序一致。 如果 primary_image 参数未指定，则数组中的第一张图片为商品主图。 images360Array of strings 360° 商品图片数组。 is_archivedboolean 如果商品是手动归档的，则为 true。 is_autoarchivedboolean 如果商品是自动归档的，则为 true。 is_discountedboolean 商品是否为减价商品： 如果商品是由卖家作为减价商品创建的，则为 true。 如果商品不是减价商品或是由Ozon减价的，则为 false。 is_kgtboolean true，表示商品为超大。仅适用于FBS模式。 is_prepayment_allowedboolean Deprecated 如果支持预付款，则为 true。 is_superboolean 超级商品标识。 有关超级商品的详细信息，请参考卖家知识库 min_pricestring 应用促销后的最低价格。 model_infoobject 商品型号信息。 namestring 名称。 offer_idstring 商品在卖家系统中的标识符 — 货号。 old_pricestring 不含折扣价格。在商品卡片上显示为划线价。 pricestring 商品的含折扣价格。该值将在商品卡片上显示。 price_indexesobject 商品价格指数。 primary_imageArray of strings 商品的主图。 promotionsArray of objects 促销活动。 skuinteger <int64> 商品在 Ozon 系统中的标识符 — SKU。 sourcesArray of objects 商品创建来源信息。自2023年7月1日起，卖家按SDS模式创建商品。 statusesobject 商品状态信息。 stocksobject 商品库存信息。 type_idinteger <int64> 商品类型标识符。 updated_atstring <date-time> 商品的最后更新时间。 vatstring 商品的增值税税率。 visibility_detailsobject 商品的可见性设置。 volume_weightnumber <double> 商品的体积重量。

## 示例

### 示例 0

```json
{"offer_id": ["2026113PDF"],"product_id": ["3339791176800"],"sku": ["33373353831"]}
```

### 示例 1

```text
{"items": [{"availabilities": [{"availability": "in_stock","reasons": [{"human_text": {"text": "商品仓库有货"},"id": 12345}],"sku": 987654321,"source": "main_warehouse"}],"barcodes": ["123456789012"],"color_image": ["https://example.com/color_image_123.jpg"],"commissions": [{"delivery_amount": 150,"percent": 10,"return_amount": 50,"sale_schema": "standard","value": 200}],"created_at": "2023-01-15T10:30:00Z","currency_code": "RUB","description_category_id": 42,"discounted_fbo_stocks": 5,"errors": [{"attribute_id": 101,"code": "INVALID_PRICE","field": "price","level": "ERROR","state": "pending","texts": {"attribute_name": "价格","description": "价格不能为负数","hint_code": "PRICE_NEGATIVE","message": "请修改价格","params": [{"name": "min_price","value": "100"}],"short_description": "价格错误"}}],"has_discounted_fbo_item": false,"id": 100001,"images": ["https://example.com/image1.jpg","https://example.com/image2.jpg"],"images360": ["https://example.com/360_image1.jpg"],"is_archived": false,"is_autoarchived": false,"is_discounted": true,"is_kgt": false,"is_prepayment_allowed": true,"is_super": false,"min_price": "999.99","model_info": {"count": 3,"model_id": 777},"name": "测试商品123","offer_id": "OFFER_123456789","old_price": "1499.99","price": "1299.99","price_indexes": {"color_index": "RED","external_index_data": {"minimal_price": "1199.99","minimal_price_currency": "RUB","price_index_value": 85},"ozon_index_data": {"minimal_price": "1250.00","minimal_price_currency": "RUB","price_index_value": 90},"self_marketplaces_index_data": {"minimal_price": "1200.00","minimal_price_currency": "RUB","price_index_value": 88}},"primary_image": ["https://example.com/primary_image.jpg"],"promotions": [{"is_enabled": true,"type": "DISCOUNT"}],"sku": 123456789,"sources": [{"created_at": "2023-01-10T09:15:00Z","quant_code": "QUANT_123","shipment_type": "EXPRESS","sku": 123456789,"source": "supplier_1"}],"statuses": {"is_created": true,"moderate_status": "approved","status": "active","status_description": "商品可销售","status_failed": "none","status_name": "已激活","status_tooltip": "商品已通过审核","status_updated_at": "2023-01-14T11:20:00Z","validation_status": "valid"},"stocks": {"has_stock": true,"stocks": [{"present": 50,"reserved": 5,"sku": 123456789,"source": "main_warehouse"}]},"type_id": 1,"updated_at": "2023-01-16T12:45:00Z","vat": "20%","visibility_details": {"has_price": true,"has_stock": true},"volume_weigh
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

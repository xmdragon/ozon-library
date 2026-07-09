# 获取商品图片

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v2/product/pictures/info`
- Operation ID：`ProductAPI_ProductInfoPicturesV2`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/ProductAPI_ProductInfoPicturesV2
- 分组：`product`

## 页面标题结构

- 获取商品图片
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

product_id required Array of strings <int64> <= 1000 items 商品识别码的清单。

### 表格 2

itemsArray of objects 商品图片。 Array ()product_idinteger <int64> Ozon系统中商品的标识符 — product_id。 primary_photoArray of strings 主图链接。 photoArray of strings 商品照片链接。 color_photoArray of strings 上传的颜色样本链接。 photo_360Array of strings 360度图片链接。 errorsArray of objects 商品图片相关错误列表。

### 表格 3

product_idinteger <int64> Ozon系统中商品的标识符 — product_id。 primary_photoArray of strings 主图链接。 photoArray of strings 商品照片链接。 color_photoArray of strings 上传的颜色样本链接。 photo_360Array of strings 360度图片链接。 errorsArray of objects 商品图片相关错误列表。

## 示例

### 示例 0

```json
{"product_id": ["89898989"]}
```

### 示例 1

```json
{"items": [{"product_id": 100500,"primary_photo": ["https://test-test.ru/images/products/100500/primary.jpg"],"photo": ["https://test-test.ru/images/products/100500/photo1.jpg","https://test-test.ru/images/products/100500/photo2.jpg"],"color_photo": ["https://test-test.ru/images/products/100500/color_red.jpg","https://test-test.ru/images/products/100500/color_blue.jpg"],"photo_360": ["https://test-test.ru/images/products/100500/360_view1.jpg","https://test-test.ru/images/products/100500/360_view2.jpg"],"errors": [{"message": "无法上传附加图片：文件大小超限","url": "https://test-test.ru/api/v1/products/100500/errors/12345"},{"message": "缺少颜色“绿色”的描述","url": "https://test-test.ru/api/v1/products/100500/errors/12346"}]}]}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

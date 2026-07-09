# 获取评价信息

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/review/info`
- Operation ID：`ReviewAPI_ReviewInfo`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/ReviewAPI_ReviewInfo
- 分组：`review`

## 页面标题结构

- 获取评价信息
- Request Body schema: application/json
- 回复
- Response Schema: application/json
- 请求范例
- 回复范例

## 参数与返回结构

### 表格 0

review_id required string 评价标识符。

### 表格 1

comments_amountinteger <int32> 评价的回复数量。 dislikes_amountinteger <int32> 评价的踩数量。 idstring 评价标识符。 is_rating_participantboolean true：评论是由官方人员留下的；false：评论是由买家留下的。 likes_amountinteger <int32> 评价的点赞数量。 order_statusstring 买家留下评价的订单状态： DELIVERED— 已送达， CANCELLED — 已取消。 photosArray of objects 图片信息。 photos_amountinteger <int32> 评价中的图片数量。 published_atstring <date-time> 评价的发布日期。 ratinginteger <int32> 评价评分。 skuinteger <int64> Ozon系统中的商品识别符——SKU。 statusstring 评价状态： UNPROCESSED — 未处理， PROCESSED — 已处理。 textstring 评价文字。 videosArray of objects 视频信息。 videos_amountinteger <int32> 评价中的视频数量。

## 示例

### 示例 0

```text
DELIVERED
```

### 示例 1

```text
CANCELLED
```

### 示例 2

```text
UNPROCESSED
```

### 示例 3

```text
PROCESSED
```

### 示例 4

```json
{"review_id": "string"}
```

### 示例 5

```json
{"comments_amount": 0,"dislikes_amount": 0,"id": "string","is_rating_participant": true,"likes_amount": 0,"order_status": "string","photos": [{"height": 0,"url": "string","width": 0}],"photos_amount": 0,"published_at": "2019-08-24T14:15:22Z","rating": 0,"sku": 0,"status": "string","text": "string","videos": [{"height": 0,"preview_url": "string","short_video_preview_url": "string","url": "string","width": 0}],"videos_amount": 0}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

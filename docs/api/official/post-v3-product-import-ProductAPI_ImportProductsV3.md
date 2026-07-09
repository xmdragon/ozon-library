# 创建或更新商品

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v3/product/import`
- Operation ID：`ProductAPI_ImportProductsV3`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/ProductAPI_ImportProductsV3
- 分组：`product`

## 页面标题结构

- 创建或更新商品
- 加载图片
- 上传视频
- 视频封面上传
- 上传尺寸表
- header Parameters
- Request Body schema: application/json
- 回复
- Response Schema: application/json
- 请求范例
- 回复范例

## 参数与返回结构

### 表格 0

| 字段 | 类型/说明 |
| --- | --- |
| `Client-Id` required | string 用户识别号。 |
| `Api-Key` required | string API-密钥。 |

### 表格 1

| 字段 | 类型/说明 |
| --- | --- |
| `items` | Array of objects 数据组。 |

### 表格 2

| 字段 | 类型/说明 |
| --- | --- |
| `result` | object 查询结果。 |
| `task_id` | integer <int64> 装卸任务的编号。 |

### 表格 3

| 字段 | 类型/说明 |
| --- | --- |
| `task_id` | integer <int64> 装卸任务的编号。 |

## 示例

### 示例 0

```text
item_limit_exceeded
```

### 示例 1

```text
429
```

### 示例 2

```text
message
```

### 示例 3

```text
Item-Retry-After
```

### 示例 4

```text
Item-Rate-Limit-Remaining
```

### 示例 5

```text
items
```

### 示例 6

```text
RUB
```

### 示例 7

```text
CNY
```

### 示例 8

```text
depth
```

### 示例 9

```text
width
```

### 示例 10

```text
height
```

### 示例 11

```text
dimension_unit
```

### 示例 12

```text
weight
```

### 示例 13

```text
weight_unit
```

### 示例 14

```text
items.statuses.moderate_status
```

### 示例 15

```text
items
```

### 示例 16

```text
9048
```

### 示例 17

```text
attributes
```

### 示例 18

```text
images
```

### 示例 19

```text
primary_image
```

### 示例 20

```text
primary_image
```

### 示例 21

```text
images
```

### 示例 22

```text
result.id = 23500
```

### 示例 23

```text
id = 23500
```

### 示例 24

```text
items.attributes.values.value
```

### 示例 25

```text
primary_image
```

### 示例 26

```text
images
```

### 示例 27

```text
primary_image
```

### 示例 28

```text
images
```

### 示例 29

```text
images360
```

### 示例 30

```text
color_image
```

### 示例 31

```text
images
```

### 示例 32

```text
images360
```

### 示例 33

```text
color_image
```

### 示例 34

```text
complex_attributes
```

### 示例 35

```text
attributes
```

### 示例 36

```text
complex_id = 100001
```

### 示例 37

```text
id = 21841
```

### 示例 38

```text
values
```

### 示例 39

```json
{
  "complex_id": 100001,
  "id": 21841,
  "values": [
    {
      "value": "https://www.youtube.com/watch?v=ZwM0iBn03dY"
    }
  ]
}
```

### 示例 40

```json
{
  "complex_id": 100001,
  "id": 21841,
  "values": [
    {
      "value": "https://www.youtube.com/watch?v=ZwM0iBn03dY"
    }
  ]
}
```

### 示例 41

```text
id = 21837
```

### 示例 42

```text
values
```

### 示例 43

```json
{
  "complex_id": 100001,
  "id": 21837,
  "values": [
    {
      "value": "videoName_1"
    }
  ]
}
```

### 示例 44

```json
{
  "complex_id": 100001,
  "id": 21837,
  "values": [
    {
      "value": "videoName_1"
    }
  ]
}
```

### 示例 45

```text
values
```

### 示例 46

```json
{ "complex_id": 100001, "id": 21837, "values": [ { "value": "videoName_1" }, { "value": "videoName_2" } ] }, { "complex_id": 100001, "id": 21841, "values": [ { "value": "https://www.youtube.com/watch?v=ZwM0iBn03dY" }, { "value": "https://www.youtube.com/watch?v=dQw4w9WgXcQ" } ] }
```

### 示例 47

```json
{ "complex_id": 100001, "id": 21837, "values": [ { "value": "videoName_1" }, { "value": "videoName_2" } ] }, { "complex_id": 100001, "id": 21841, "values": [ { "value": "https://www.youtube.com/watch?v=ZwM0iBn03dY" }, { "value": "https://www.youtube.com/watch?v=dQw4w9WgXcQ" } ] }
```

### 示例 48

```text
complex_attributes
```

### 示例 49

```text
"complex_attributes": [ { "attributes": [ { "id": 21845, "complex_id": 100002, "values": [ { "dictionary_value_id": 0, "value": "https://v.ozone.ru/vod/video-10/01GFATWQVCDE7G5B721421P1231Q7/asset_1.mp4" } ] } ] } ]
```

### 示例 50

```text
"complex_attributes": [ { "attributes": [ { "id": 21845, "complex_id": 100002, "values": [ { "dictionary_value_id": 0, "value": "https://v.ozone.ru/vod/video-10/01GFATWQVCDE7G5B721421P1231Q7/asset_1.mp4" } ] } ] } ]
```

### 示例 51

```text
attributes
```

### 示例 52

```text
id = 13164
```

### 示例 53

```json
{
  "items": [
    {
      "attributes": [
        {
          "complex_id": 0,
          "id": 5076,
          "values": [
            {
              "dictionary_value_id": 971082156,
              "value": "麦克风架"
            }
          ]
        },
        {
          "complex_id": 0,
          "id": 9048,
          "values": [
            {
              "value": "一套X3NFC保护膜。 深色棉质"
            }
          ]
        },
        {
          "complex_id": 0,
          "id": 8229,
          "values": [
            {
              "dictionary_value_id": 95911,
              "value": "一套X3NFC保护膜。深色棉质"
            }
          ]
        },
        {
          "complex_id": 0,
          "id": 85,
          "values": [
            {
              "dictionary_value_id": 5060050,
              "value": "Samsung"
            }
          ]
        },
        {
          "complex_id": 0,
          "id": 10096,
          "values": [
            {
              "dictionary_value_id": 61576,
              "value": "灰色的"
            }
          ]
        }
      ],
      "barcode": "112772873170",
      "description_category_id": 17028922,
      "new_description_category_id": 0,
      "color_image": "",
      "complex_attributes": [],
      "currency_code": "RUB",
      "depth": 10,
      "dimension_unit": "mm",
      "height": 250,
      "images": [],
      "images360": [],
      "name": "一套X3NFC的保护膜。深色棉质",
      "offer_id": "143210608",
      "old_price": "1100",
      "pdf_list": [],
      "price": "1000",
      "primary_image": "",
      "promotions": [
        {
          "operation": "UNKNOWN",
          "type": "REVIEWS_PROMO"
        }
      ],
      "type_id": 91565,
      "vat": "0.1",
      "weight": 100,
      "weight_unit": "g",
      "width": 150
    }
  ]
}
```

### 示例 54

```json
{
  "result": {
    "task_id": 172549793
  }
}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

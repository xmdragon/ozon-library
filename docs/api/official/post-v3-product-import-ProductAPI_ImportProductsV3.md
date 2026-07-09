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

Client-Id required string 用户识别号。 Api-Key required string API-密钥。

### 表格 1

itemsArray of objects 数据组。

### 表格 2

resultobject 查询结果。 task_idinteger <int64> 装卸任务的编号。

### 表格 3

task_idinteger <int64> 装卸任务的编号。

## 示例

### 示例 0

```text
429
```

### 示例 1

```text
RUB
```

### 示例 2

```text
CNY
```

### 示例 3

```text
9048
```

### 示例 4

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

### 示例 5

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

### 示例 6

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

### 示例 7

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

### 示例 8

```json
{
    "complex_id": 100001,
    "id": 21837,
    "values": [
      {
        "value": "videoName_1"
      },
      {
        "value": "videoName_2"
      }
    ]
  },
  {
    "complex_id": 100001,
    "id": 21841,
    "values": [
      {
        "value": "https://www.youtube.com/watch?v=ZwM0iBn03dY"
      },
      {
        "value": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
      }
    ]
  }
```

### 示例 9

```json
{
    "complex_id": 100001,
    "id": 21837,
    "values": [
      {
        "value": "videoName_1"
      },
      {
        "value": "videoName_2"
      }
    ]
  },
  {
    "complex_id": 100001,
    "id": 21841,
    "values": [
      {
        "value": "https://www.youtube.com/watch?v=ZwM0iBn03dY"
      },
      {
        "value": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
      }
    ]
  }
```

### 示例 10

```json
{"items": [{"attributes": [{"complex_id": 0,"id": 5076,"values": [{"dictionary_value_id": 971082156,"value": "麦克风架"}]},{"complex_id": 0,"id": 9048,"values": [{"value": "一套X3NFC保护膜。 深色棉质"}]},{"complex_id": 0,"id": 8229,"values": [{"dictionary_value_id": 95911,"value": "一套X3NFC保护膜。深色棉质"}]},{"complex_id": 0,"id": 85,"values": [{"dictionary_value_id": 5060050,"value": "Samsung"}]},{"complex_id": 0,"id": 10096,"values": [{"dictionary_value_id": 61576,"value": "灰色的"}]}],"barcode": "112772873170","description_category_id": 17028922,"new_description_category_id": 0,"color_image": "","complex_attributes": [ ],"currency_code": "RUB","depth": 10,"dimension_unit": "mm","height": 250,"images": [ ],"images360": [ ],"name": "一套X3NFC的保护膜。深色棉质","offer_id": "143210608","old_price": "1100","pdf_list": [ ],"price": "1000","primary_image": "","promotions": [{"operation": "UNKNOWN","type": "REVIEWS_PROMO"}],"type_id": 91565,"vat": "0.1","weight": 100,"weight_unit": "g","width": 150}]}
```

### 示例 11

```json
{"result": {"task_id": 172549793}}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

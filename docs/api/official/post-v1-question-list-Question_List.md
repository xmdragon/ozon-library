# 问题列表

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/question/list`
- Operation ID：`Question_List`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/Question_List
- 分组：`question`

## 页面标题结构

- 问题列表
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

filterobject 筛选器。 last_idstring 页面上最后一个值的ID。运行第一个查询时，将此字段留空。 要检索以下数值，请从上一个查询的响应中指定last_id。 limitinteger <int64> <= 100 响应中返回的值数量。 sort_dirstring Default: "DESC" Enum: "DESC" "ASC" 排序方向： DESC——降序； ASC——升序。

### 表格 2

questionsArray of objects [ 0 .. 10 ] items 问题。 last_idstring 页面上最后一个值的标识符。 要获取下一个批次的数据，请在下一个请求的 last_id 参数中传递上次获取的值。 has_nextboolean 如果响应中未返回所有问题，则为true。

## 示例

### 示例 0

```text
DESC
```

### 示例 1

```text
ASC
```

### 示例 2

```json
{"filter": {"date_from": "2019-08-24T14:15:22Z","date_to": "2019-08-24T14:15:22Z","status": "ALL"},"limit": 100,"last_id": "","sort_dir": "ASC"}
```

### 示例 3

```json
{"has_next": true,"questions": [{"answers_count": 1,"author_name": "string","id": "019294ff-6888-7009-89d8-26569e4e450d","sku": 646399170,"product_url": "https://www.ozon.ru/product/1649246352/","published_at": "2024-08-14T12:02:01.889Z","question_link": "https://www.ozon.ru/product/1649246352/questions/?qid=290180206&utm_campaign=reviews_sc_link&utm_medium=share_button&utm_source=smm","text": "string","status": "PROCESSED"}],"last_id": "019228a7-91d8-76af-a73a-e989dfac7ac8"}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

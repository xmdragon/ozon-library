# 获取货件列表

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/assembly/fbs/posting/list`
- Operation ID：`AssemblyFbsPostingList`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/AssemblyFbsPostingList
- 分组：`assembly`

## 页面标题结构

- 获取货件列表
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

cursorstring 用于选择下一批数据的指针。 filter required object 筛选器。 limit required integer <int64> <= 1000 每页显示的数量。 sort_dir required string Enum: "ASC" "DESC" 排序方向： ASC——升序， DESC——降序。

### 表格 2

cursorstring 用于选择下一批数据的指针。如果该参数为空，则没有更多数据了。 cutoffstring <date-time> 卖家需在此时间前完成订单备货。 postingsArray of objects 货件列表。

## 示例

### 示例 0

```text
ASC
```

### 示例 1

```text
DESC
```

### 示例 2

```json
{"filter": {"cutoff_from": "2026-03-01T00:00:00Z","cutoff_to": "2026-03-07T23:59:59Z","delivery_method_id": 323123321},"limit": 50,"sort_dir": "ASC","cursor": ""}
```

### 示例 3

```json
{"cutoff": "2026-03-07T10:00:00Z","postings": [{"posting_number": "789456123-0002-3","assembly_code": "test-assembly-code-12345","products": [{"sku": 1000123456,"offer_id": "test-offer-123456","product_name": "string","picture_url": "https://test-example.com/images/product-123456.jpg","quantity": 2},{"sku": 1000123457,"offer_id": "test-offer-123457","product_name": "string","picture_url": "https://test-example.com/images/product-123457.jpg","quantity": 1}]},{"posting_number": "123456789-0001-1","assembly_code": "test-assembly-code-12346","products": [{"sku": 1000123458,"offer_id": "test-offer-123458","product_name": "string","picture_url": "https://test-example.com/images/product-123458.jpg","quantity": 3}]},{"posting_number": "456123789-0003-5","assembly_code": "test-assembly-code-12347","products": [{"sku": 1000123459,"offer_id": "test-offer-123459","product_name": "string","picture_url": "https://test-example.com/images/product-123459.jpg","quantity": 1},{"sku": 1000123460,"offer_id": "test-offer-123460","product_name": "string","picture_url": "https://test-example.com/images/product-123460.jpg","quantity": 2},{"sku": 1000123461,"offer_id": "test-offer-123461","product_name": "string","picture_url": "https://test-example.com/images/product-123461.jpg","quantity": 1}]}],"cursor": "test-cursor-next-page-67890"}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

# 获取发运中的商品列表

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/assembly/carriage/product/list`
- Operation ID：`AssemblyCarriageProductList`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/AssemblyCarriageProductList
- 分组：`assembly`

## 页面标题结构

- 获取发运中的商品列表
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
| `cursor` | string 用于选择下一批数据的指针。 |
| `filter` required | object 筛选器。 |
| `limit` required | integer <int64> <= 100 每页显示的数量。 |

### 表格 2

| 字段 | 类型/说明 |
| --- | --- |
| `cursor` | string 用于选择下一批数据的指针。如果该参数为空，则没有更多数据了。 |
| `products` | Array of objects 商品列表。 |

## 示例

### 示例 0

```json
{"cursor": "string","filter": {"carriage_id": 0,"cutoff_from": "2019-08-24T14:15:22Z","cutoff_to": "2019-08-24T14:15:22Z","delivery_method_id": 0},"limit": 0}
```

### 示例 1

```json
{"cursor": "string","products": [{"offer_id": "string","picture_url": "string","posting_numbers": ["string"],"product_name": "string","quantity": 0,"sku": 0}]}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

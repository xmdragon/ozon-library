# 获取相关SKU

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/product/related-sku/get`
- Operation ID：`ProductAPI_ProductGetRelatedSKU`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/ProductAPI_ProductGetRelatedSKU
- 分组：`product`

## 页面标题结构

- 获取相关SKU
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
| `sku` required | Array of strings <int64> SKU列表。 |

### 表格 2

| 字段 | 类型/说明 |
| --- | --- |
| `items` | Array of objects 相关SKU信息。 |
| `errors` | Array of objects 错误。 |

## 示例

### 示例 0

```json
{"sku": ["88997766"]}
```

### 示例 1

```json
{"items": [{"availability": "AVAILABLE","deleted_at": "2019-08-24T14:15:22Z","delivery_schema": "SDS","product_id": "door","sku": "88997766"}],"errors": [{"code": "das","sku": "88997766","message": "sku does not exist"}]}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

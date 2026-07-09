# 更新库存商品的数量

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v2/products/stocks`
- Operation ID：`ProductAPI_ProductsStocksV2`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/ProductAPI_ProductsStocksV2
- 分组：`products`

## 页面标题结构

- 更新库存商品的数量
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
| `stocks` required | Array of objects 仓库中商品的信息。 |

### 表格 2

| 字段 | 类型/说明 |
| --- | --- |
| `result` | Array of objects |
| `errors` | Array of objects 在搜索处理过程中发生的数组错误。 |
| `offer_id` | string 卖家系统中的商品编号是 — 商品代码。 |
| `product_id` | integer <int64> Ozon系统中商品的标识符 — product_id。 |
| `updated` | boolean 如果商品信息已被成功更新 — true。 |
| `warehouse_id` | integer <int64> 仓库编号。 |

### 表格 3

| 字段 | 类型/说明 |
| --- | --- |
| `errors` | Array of objects 在搜索处理过程中发生的数组错误。 |
| `offer_id` | string 卖家系统中的商品编号是 — 商品代码。 |
| `product_id` | integer <int64> Ozon系统中商品的标识符 — product_id。 |
| `updated` | boolean 如果商品信息已被成功更新 — true。 |
| `warehouse_id` | integer <int64> 仓库编号。 |

## 示例

### 示例 0

```text
result.errors
```

### 示例 1

```text
TOO_MANY_REQUESTS
```

### 示例 2

```text
price_sent
```

### 示例 3

```text
offer_id
```

### 示例 4

```text
product_id
```

### 示例 5

```text
offer_id
```

### 示例 6

```text
product_id
```

### 示例 7

```text
true
```

### 示例 8

```json
{"stocks": [{"offer_id": "PH11042","product_id": 313455276,"stock": 100,"warehouse_id": 22142605386000}]}
```

### 示例 9

```json
{"result": [{"warehouse_id": 22142605386000,"product_id": 118597312,"offer_id": "PH11042","updated": true,"errors": [ ]}]}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

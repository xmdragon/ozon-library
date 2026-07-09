# 为打折商品设置折扣

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/product/update/discount`
- Operation ID：`ProductAPI_ProductUpdateDiscount`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/ProductAPI_ProductUpdateDiscount
- 分组：`product`

## 页面标题结构

- 为打折商品设置折扣
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
| `discount` required | integer <int32> 折扣力度：从3%到99%。 |
| `product_id` required | integer <int64> Ozon系统中商品的标识符 — product_id。 |

### 表格 2

| 字段 | 类型/说明 |
| --- | --- |
| `result` | boolean 方式工作结果 true, 如果正确完成请求。 |

## 示例

### 示例 0

```text
product_id
```

### 示例 1

```text
true
```

### 示例 2

```json
{
  "discount": 10,
  "product_id": 876763232
}
```

### 示例 3

```json
{
  "result": true
}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

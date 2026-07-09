# 创建商品条形码

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/barcode/generate`
- Operation ID：`generate-barcode`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/generate-barcode
- 分组：`barcode`

## 页面标题结构

- 创建商品条形码
- Request Body schema: application/json
- 回复
- Response Schema: application/json
- 请求范例
- 回复范例

## 参数与返回结构

### 表格 0

| 字段 | 类型/说明 |
| --- | --- |
| `product_ids` required | Array of strings <int64> 需要生成条形码的商品标识符。 |

### 表格 1

| 字段 | 类型/说明 |
| --- | --- |
| `errors` | Array of objects 生成条形码时出现的错误。 |
| `code` | string 错误代码。 |
| `error` | string 错误描述。 |
| `barcode` | string 生成条形码时出错的条形码。 |
| `product_id` | integer <int64> 未能成功生成条形码的商品标识符。 |

### 表格 2

| 字段 | 类型/说明 |
| --- | --- |
| `code` | string 错误代码。 |
| `error` | string 错误描述。 |
| `barcode` | string 生成条形码时出错的条形码。 |
| `product_id` | integer <int64> 未能成功生成条形码的商品标识符。 |

## 示例

### 示例 0

```json
{
  "product_ids": [
    "99887766"
  ]
}
```

### 示例 1

```json
{
  "errors": [
    {
      "code": "123-123",
      "error": "does not exist",
      "barcode": "112772873170",
      "product_id": 9988776612
    }
  ]
}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

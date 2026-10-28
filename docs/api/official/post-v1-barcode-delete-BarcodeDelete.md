# 将条形码与商品解除绑定

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/barcode/delete`
- Operation ID：`BarcodeDelete`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/#operation/BarcodeDelete
- 分组：`barcode`

## News 更新标记

| 日期 | 标记 | 摘要 | 来源 |
| --- | --- | --- | --- |
| 2026-10-06 | `new_method` | /v1/barcode/delete 新增了用于将条形码与商品解除绑定的方法。 | [官方 News](https://docs.ozon.ru/api/seller/zh/#section/2026106) |

## 页面标题结构

- 将条形码与商品解除绑定
- HEADER PARAMETERS
- REQUEST BODY SCHEMA: application/json
- 回复
- RESPONSE SCHEMA: application/json
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
| `barcodes` required | Array of objects [ 1 .. 100 ] items 需要解除绑定的条形码与商品对的列表。 |

### 表格 2

| 字段 | 类型/说明 |
| --- | --- |
| `errors` | Array of objects 错误列表。如果列表为空，则所有条形码均已成功解除绑定。 |
| `barcode` | string 未能解除绑定的条形码。 |
| `code` | string 错误代码。 |
| `error` | string 错误描述。 |
| `sku` | integer <int64> 未能与条形码解除绑定的商品的标识符。 |

### 表格 3

| 字段 | 类型/说明 |
| --- | --- |
| `barcode` | string 未能解除绑定的条形码。 |
| `code` | string 错误代码。 |
| `error` | string 错误描述。 |
| `sku` | integer <int64> 未能与条形码解除绑定的商品的标识符。 |

## 示例

### 示例 0

```json
{
  "barcodes": [
    {
      "barcode": "string",
      "sku": 0
    }
  ]
}
```

### 示例 1

```json
{
  "errors": [
    {
      "barcode": "string",
      "code": "string",
      "error": "string",
      "sku": 0
    }
  ]
}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

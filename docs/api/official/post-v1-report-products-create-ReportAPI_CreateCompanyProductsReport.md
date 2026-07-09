# 商品报告

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/report/products/create`
- Operation ID：`ReportAPI_CreateCompanyProductsReport`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/ReportAPI_CreateCompanyProductsReport
- 分组：`report`

## 页面标题结构

- 商品报告
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
| `language` | string Default: "DEFAULT" 回答所用语言： RU — 俄语， EN — 英语。 |
| `offer_id` | Array of strings 卖家系统中的商品标识符是商品货号。 |
| `search` | string 在记录内容中搜索，检查现货。 |
| `sku` | Array of integers <int64> Ozon 系统中的商品标识符（SKU）。 |
| `visibility` | string Default: "ALL" Enum: "ALL" "VALIDATION_STATE_FAIL" "TO_SUPPLY" "IN_SALE" "REMOVED_FROM_SALE" "PARTIAL_APPROVED" "IMAGE_ABSENT" "ARCHIVED" "AUTO_ARCHIVED" "MANUAL_ARCHIVED" 按商品可见度过滤。 ALL——除了档案中的所有商品； VALIDATION_STATE_FAIL——预审时未被验证器检查的商品； TO_SUPPLY——准备出售的货物； IN_SALE——正在销售的商品； REMOVED_FROM_SALE——对买家隐藏的商品； PARTIAL_APPROVED——商品存在警告，需要修改； IMAGE_ABSENT——无图片的商品； ARCHIVED——已归档商品； AUTO_ARCHIVED——自动归档的商品； MANUAL_ARCHIVED——手动归档的商品。 |

### 表格 2

| 字段 | 类型/说明 |
| --- | --- |
| `result` | object 请求结果。 |
| `code` | string 报告的唯一识别码。要获取报告，请将此值传递到方法 /v1/report/info。 |

### 表格 3

| 字段 | 类型/说明 |
| --- | --- |
| `code` | string 报告的唯一识别码。要获取报告，请将此值传递到方法 /v1/report/info。 |

## 示例

### 示例 0

```text
product_id
```

### 示例 1

```text
product_id
```

### 示例 2

```text
product_id
```

### 示例 3

```text
product_id
```

### 示例 4

```text
RU
```

### 示例 5

```text
EN
```

### 示例 6

```text
ALL
```

### 示例 7

```text
VALIDATION_STATE_FAIL
```

### 示例 8

```text
TO_SUPPLY
```

### 示例 9

```text
IN_SALE
```

### 示例 10

```text
REMOVED_FROM_SALE
```

### 示例 11

```text
PARTIAL_APPROVED
```

### 示例 12

```text
IMAGE_ABSENT
```

### 示例 13

```text
ARCHIVED
```

### 示例 14

```text
AUTO_ARCHIVED
```

### 示例 15

```text
MANUAL_ARCHIVED
```

### 示例 16

```json
{
  "language": "DEFAULT",
  "offer_id": [],
  "search": "",
  "sku": [],
  "visibility": "ALL"
}
```

### 示例 17

```json
{
  "result": {
    "code": "REPORT_seller_products_924336_1720170405_a9ea2f27-a473-4b13-99f9-d0cfcb5b1a69"
  }
}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

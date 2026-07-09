# 管理按数量折扣

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/product/stairway-discount/by-quantity/set`
- Operation ID：`ProductAPI_SetProductStairwayDiscountByQuantity`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/ProductAPI_SetProductStairwayDiscountByQuantity
- 分组：`product`

## 页面标题结构

- 管理按数量折扣
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
| `stairways` required | Array of objects 多个商品的按数量折扣信息。 |
| `suppress_warnings` | boolean 传递 true 可忽略警告并设置折扣。 |

### 表格 2

| 字段 | 类型/说明 |
| --- | --- |
| `accepted` | boolean true，表示请求已接收。请使用方法/v1/product/stairway-discount/by-quantity/get来查看折扣修改结果。 |
| `errors` | Array of objects 错误描述。 |
| `warnings` | Array of objects 警告描述。 |

## 示例

### 示例 0

```text
true
```

### 示例 1

```text
true
```

### 示例 2

```json
{"stairways": [{"enabled": true,"sku": 0,"stairway": {"steps": [{"discount": 0,"quantity": 0,"step": 0}]}}],"suppress_warnings": true}
```

### 示例 3

```json
{"accepted": true,"errors": [{"data": [{"code": "string","field": "string","message": "string","step": 0,"value": "string"}],"sku": 0}],"warnings": [{"data": [{"code": "string","field": "string","message": "string","step": 0,"value": "string"}],"sku": 0}]}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

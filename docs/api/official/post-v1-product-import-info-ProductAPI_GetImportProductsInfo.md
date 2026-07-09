# 查询商品添加或更新状态

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/product/import/info`
- Operation ID：`ProductAPI_GetImportProductsInfo`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/ProductAPI_GetImportProductsInfo
- 分组：`product`

## 页面标题结构

- 查询商品添加或更新状态
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
| `task_id` required | integer <int64> 进口商品的任务代码。按照运输方式筛选。可以使用方法 /v3/product/import获取。 |

### 表格 2

| 字段 | 类型/说明 |
| --- | --- |
| `result` | object |
| `items` | Array of objects 商品有关信息。 |
| `total` | integer <int32> 在卖方系统中的卖家系统中的商品标识符 — product_id。 |

### 表格 3

| 字段 | 类型/说明 |
| --- | --- |
| `items` | Array of objects 商品有关信息。 |
| `total` | integer <int32> 在卖方系统中的卖家系统中的商品标识符 — product_id。 |

## 示例

### 示例 0

```text
result.items.status
```

### 示例 1

```text
skipped
```

### 示例 2

```text
product_id
```

### 示例 3

```json
{
  "task_id": "172549793"
}
```

### 示例 4

```json
{
  "result": {
    "items": [
      {
        "offer_id": "143210608",
        "product_id": 137285792,
        "status": "imported",
        "errors": []
      }
    ],
    "total": 1
  }
}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

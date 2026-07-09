# 获取含有配送受限商品的仓库列表

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/warehouse/warehouses-with-invalid-products`
- Operation ID：`WarehouseWithInvalidProducts`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/WarehouseWithInvalidProducts
- 分组：`warehouse`

## 页面标题结构

- 获取含有配送受限商品的仓库列表
- header Parameters
- 回复
- Response Schema: application/json
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
| `warehouse_ids` | Array of strings <int64> 包含至少 1 件无法从该仓库发运的受限商品的仓库标识符列表。如需获取受限商品列表，请使用方法 /v1/warehouse/invalid-products/get。 |

## 示例

### 示例 0

```json
{"warehouse_ids": ["string"]}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

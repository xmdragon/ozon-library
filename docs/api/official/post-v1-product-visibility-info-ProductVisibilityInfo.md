# 获取商品可见性信息

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/product/visibility/info`
- Operation ID：`ProductVisibilityInfo`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/ProductVisibilityInfo
- 分组：`product`

## 页面标题结构

- 获取商品可见性信息
- header Parameters
- Request Body schema: application/json
- 回复
- Response Schema: application/json
- 请求范例
- 回复范例

## 参数与返回结构

### 表格 0

Client-Id required string 用户识别号。 Api-Key required string API-密钥。

### 表格 1

skusArray of strings <int64> [ 1 .. 350 ] items Ozon系统中的商品标识符—— SKU。

### 表格 2

itemsArray of objects 商品列表。 Array ()showcases_visibilitystring Default: "UNSPECIFIED" Enum: "UNSPECIFIED" "OZON" "SELECT" "OZON_SELECT" "NONE" 商品展示在哪些橱窗中： UNSPECIFIED——未指定； OZON——仅在Ozon展示； SELECT——仅在Select展示； OZON_SELECT——在Select和Ozon展示； NONE——商品在所有橱窗均隐藏。 skuinteger <int64> 商品在Ozon系统中的标识符——SKU。

### 表格 3

showcases_visibilitystring Default: "UNSPECIFIED" Enum: "UNSPECIFIED" "OZON" "SELECT" "OZON_SELECT" "NONE" 商品展示在哪些橱窗中： UNSPECIFIED——未指定； OZON——仅在Ozon展示； SELECT——仅在Select展示； OZON_SELECT——在Select和Ozon展示； NONE——商品在所有橱窗均隐藏。 skuinteger <int64> 商品在Ozon系统中的标识符——SKU。

## 示例

### 示例 0

```text
UNSPECIFIED
```

### 示例 1

```text
OZON
```

### 示例 2

```text
SELECT
```

### 示例 3

```text
OZON_SELECT
```

### 示例 4

```text
NONE
```

### 示例 5

```json
{"skus": ["string"]}
```

### 示例 6

```json
{"items": [{"showcases_visibility": "UNSPECIFIED","sku": 0}]}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

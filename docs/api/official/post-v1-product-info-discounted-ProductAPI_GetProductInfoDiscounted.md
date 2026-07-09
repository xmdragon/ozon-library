# 通过减价商品的SKU查找减价商品和主商品的信息

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/product/info/discounted`
- Operation ID：`ProductAPI_GetProductInfoDiscounted`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/ProductAPI_GetProductInfoDiscounted
- 分组：`product`

## 页面标题结构

- 通过减价商品的SKU查找减价商品和主商品的信息
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
| `discounted_skus` required | Array of strings <int64> 降价的商品SKU清单。 |

### 表格 2

| 字段 | 类型/说明 |
| --- | --- |
| `items` | Array of objects 关于减价和主要商品的信息。 |
| `comment_reason_damaged` | string 对损坏原因的评论。 |
| `condition` | string 商品的状态 — 新的或二手的。 |
| `condition_estimation` | string 商品的状况，以1至7分为标准。 1 — 令人满意。 2 — 良好。 3 — 非常好。 4 — 优秀。 5-7 — 像新的一样。 |
| `defects` | string 商品缺陷。 |
| `discounted_sku` | integer <int64> 折扣商品的SKU。 |
| `mechanical_damage` | string 机械性损坏的说明。 |
| `package_damage` | string 包装损坏的说明。 |
| `packaging_violation` | string 篡改包装的痕迹。 |
| `reason_damaged` | string 损害原因。 |
| `repair` | string 商品已被修理的痕迹。 |
| `shortage` | string 表示商品不完整。 |
| `sku` | integer <int64> 主要商品的SKU。 |
| `warranty_type` | string 商品有有效保修的证明。 |

### 表格 3

| 字段 | 类型/说明 |
| --- | --- |
| `comment_reason_damaged` | string 对损坏原因的评论。 |
| `condition` | string 商品的状态 — 新的或二手的。 |
| `condition_estimation` | string 商品的状况，以1至7分为标准。 1 — 令人满意。 2 — 良好。 3 — 非常好。 4 — 优秀。 5-7 — 像新的一样。 |
| `defects` | string 商品缺陷。 |
| `discounted_sku` | integer <int64> 折扣商品的SKU。 |
| `mechanical_damage` | string 机械性损坏的说明。 |
| `package_damage` | string 包装损坏的说明。 |
| `packaging_violation` | string 篡改包装的痕迹。 |
| `reason_damaged` | string 损害原因。 |
| `repair` | string 商品已被修理的痕迹。 |
| `shortage` | string 表示商品不完整。 |
| `sku` | integer <int64> 主要商品的SKU。 |
| `warranty_type` | string 商品有有效保修的证明。 |

## 示例

### 示例 0

```json
{"discounted_skus": ["635548518"]}
```

### 示例 1

```json
{"items": [{"discounted_sku": 635548518,"sku": 320067758,"condition_estimation": "4","packaging_violation": "","warranty_type": "","reason_damaged": "Механическое повреждение","comment_reason_damaged": "повреждена заводская упаковка","defects": "","mechanical_damage": "","package_damage": "","shortage": "","repair": "","condition": ""}]}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

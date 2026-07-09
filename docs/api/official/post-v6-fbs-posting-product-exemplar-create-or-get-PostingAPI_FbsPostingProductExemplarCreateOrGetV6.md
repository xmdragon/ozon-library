# 获取已创建样件数据

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v6/fbs/posting/product/exemplar/create-or-get`
- Operation ID：`PostingAPI_FbsPostingProductExemplarCreateOrGetV6`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/PostingAPI_FbsPostingProductExemplarCreateOrGetV6
- 分组：`fbs`

## 页面标题结构

- 获取已创建样件数据
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
| `posting_number` required | string 发货号。 |

### 表格 2

| 字段 | 类型/说明 |
| --- | --- |
| `multi_box_qty` | integer <int32> 商品包装的箱子数量。 |
| `posting_number` | string 发货号。 |
| `products` | Array of objects 商品清单。 |

## 示例

### 示例 0

```text
exemplar_id
```

### 示例 1

```json
{"posting_number": "string"}
```

### 示例 2

```json
{"multi_box_qty": 0,"posting_number": "string","products": [{"exemplars": [{"exemplar_id": 0,"gtd": "string","is_gtd_absent": true,"is_rnpt_absent": true,"marks": [{"mark": "string","mark_type": "string"}],"rnpt": "string"}],"has_imei": true,"is_gtd_needed": true,"is_jw_uin_needed": true,"is_mandatory_mark_needed": true,"is_mandatory_mark_possible": true,"is_rnpt_needed": true,"product_id": 0,"quantity": 0}]}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

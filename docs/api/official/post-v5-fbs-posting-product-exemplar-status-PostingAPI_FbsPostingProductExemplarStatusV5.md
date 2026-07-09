# 获取样件添加状态

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v5/fbs/posting/product/exemplar/status`
- Operation ID：`PostingAPI_FbsPostingProductExemplarStatusV5`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/PostingAPI_FbsPostingProductExemplarStatusV5
- 分组：`fbs`

## 页面标题结构

- 获取样件添加状态
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
| `posting_number` | string 发货号。 |
| `products` | Array of objects 商品清单。 |
| `status` | string 所有样件和备货可用性的验证状态： ship_available——可以备货， ship_not_available——无法备货， validation_in_process——样件正在验证中， update_available——可以编辑商品实例信息， update_not_available——无法编辑商品实例信息。 |

## 示例

### 示例 0

```text
ship_available
```

### 示例 1

```text
ship_not_available
```

### 示例 2

```text
validation_in_process
```

### 示例 3

```text
update_available
```

### 示例 4

```text
update_not_available
```

### 示例 5

```json
{"posting_number": "string"}
```

### 示例 6

```json
{"posting_number": "string","products": [{"exemplars": [{"exemplar_id": 0,"gtd": "string","gtd_check_status": "string","gtd_error_codes": ["string"],"is_gtd_absent": true,"is_rnpt_absent": true,"marks": [{"check_status": "string","error_codes": ["string"],"mark": "string","mark_type": "string"}],"rnpt": "string","rnpt_check_status": "string","rnpt_error_codes": ["string"]}],"product_id": 0}],"status": "string"}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

# 状态改为“最后一英里”

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v2/fbs/posting/last-mile`
- Operation ID：`PostingAPI_FbsPostingLastMile`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/PostingAPI_FbsPostingLastMile
- 分组：`fbs`

## 页面标题结构

- 状态改为“最后一英里”
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
| `posting_number` required | Array of strings 货件ID。 |

### 表格 2

| 字段 | 类型/说明 |
| --- | --- |
| `result` | Array of objects 方法操作结果。 |
| `error` | string 处理请求时出错。 |
| `posting_number` | string 发货号。 |
| `result` | boolean 如果执行请求无误 — true。 |

### 表格 3

| 字段 | 类型/说明 |
| --- | --- |
| `error` | string 处理请求时出错。 |
| `posting_number` | string 发货号。 |
| `result` | boolean 如果执行请求无误 — true。 |

## 示例

### 示例 0

```text
true
```

### 示例 1

```json
{"posting_number": ["48173252-0033-2"]}
```

### 示例 2

```json
{"result": [{"error": [ ],"posting_number": "48173252-0033-2","result": true}]}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

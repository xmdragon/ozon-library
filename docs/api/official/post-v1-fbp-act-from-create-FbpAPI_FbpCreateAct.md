# 生成验收证明书

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/fbp/act-from/create`
- Operation ID：`FbpAPI_FbpCreateAct`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/FbpAPI_FbpCreateAct
- 分组：`fbp`

## 页面标题结构

- 生成验收证明书
- Request Body schema: application/json
- 回复
- Response Schema: application/json
- 请求范例
- 回复范例

## 参数与返回结构

### 表格 0

| 字段 | 类型/说明 |
| --- | --- |
| `supply_id` required | string 交货标识符。 |

### 表格 1

| 字段 | 类型/说明 |
| --- | --- |
| `errors` | Array of strings Default: "CREATE_ACT_ERROR_REASON_UNSPECIFIED"Items Enum: "CREATE_ACT_ERROR_REASON_UNSPECIFIED" "INVALID_ORDER_TYPE" 错误原因： CREATE_ACT_ERROR_REASON_UNSPECIFIED ——未定义； INVALID_ORDER_TYPE ——无法为指定标识符创建验收证明书。 |
| `file_uuid` | string 验收证明书标识符。 |
| `is_success` | boolean true，前提是请求中没有错误。 |

## 示例

### 示例 0

```text
CREATE_ACT_ERROR_REASON_UNSPECIFIED
```

### 示例 1

```text
INVALID_ORDER_TYPE
```

### 示例 2

```text
true
```

### 示例 3

```json
{"supply_id": "string"}
```

### 示例 4

```json
{"errors": ["CREATE_ACT_ERROR_REASON_UNSPECIFIED"],"file_uuid": "string","is_success": true}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

# 获取验收证明书生成状态

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/fbp/act-from/get`
- Operation ID：`FbpAPI_FbpCheckActState`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/FbpAPI_FbpCheckActState
- 分组：`fbp`

## 页面标题结构

- 获取验收证明书生成状态
- Request Body schema: application/json
- 回复
- Response Schema: application/json
- 请求范例
- 回复范例

## 参数与返回结构

### 表格 0

| 字段 | 类型/说明 |
| --- | --- |
| `file_uuid` required | string 验收证明书标识符。 |

### 表格 1

| 字段 | 类型/说明 |
| --- | --- |
| `cdn_url` | string 验收证明书链接。 |
| `error` | string Default: "ERROR_REASON_UNSPECIFIED" Enum: "ERROR_REASON_UNSPECIFIED" "INVALID_COMPANY" "FILE_NOT_FOUND" "GENERATE_TIMEOUT_REACHED" "GENERATION_ERROR" 生成错误： ERROR_REASON_UNSPECIFIED ——未定义； INVALID_COMPANY ——公司无效； FILE_NOT_FOUND ——文件未找到； GENERATE_TIMEOUT_REACHED ——超出生成时间； GENERATION_ERROR ——生成过程中出错。 |
| `status` | string Default: "STATUS_UNSPECIFIED" Enum: "STATUS_UNSPECIFIED" "NOT_EXIST" "PROCESSING" "EXIST" "ERROR" 生成状态： STATUS_UNSPECIFIED ——未定义； NOT_EXIST ——不存在； PROCESSING ——处理中； EXIST ——已完成； ERROR ——错误。 |

## 示例

### 示例 0

```text
ERROR_REASON_UNSPECIFIED
```

### 示例 1

```text
INVALID_COMPANY
```

### 示例 2

```text
FILE_NOT_FOUND
```

### 示例 3

```text
GENERATE_TIMEOUT_REACHED
```

### 示例 4

```text
GENERATION_ERROR
```

### 示例 5

```text
STATUS_UNSPECIFIED
```

### 示例 6

```text
NOT_EXIST
```

### 示例 7

```text
PROCESSING
```

### 示例 8

```text
EXIST
```

### 示例 9

```text
ERROR
```

### 示例 10

```json
{
  "file_uuid": "string"
}
```

### 示例 11

```json
{
  "cdn_url": "string",
  "error": "ERROR_REASON_UNSPECIFIED",
  "status": "STATUS_UNSPECIFIED"
}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

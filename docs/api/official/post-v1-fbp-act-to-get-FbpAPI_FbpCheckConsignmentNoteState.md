# 获取货物运单生成状态

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/fbp/act-to/get`
- Operation ID：`FbpAPI_FbpCheckConsignmentNoteState`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/FbpAPI_FbpCheckConsignmentNoteState
- 分组：`fbp`

## 页面标题结构

- 获取货物运单生成状态
- Request Body schema: application/json
- 回复
- Response Schema: application/json
- 请求范例
- 回复范例

## 参数与返回结构

### 表格 0

| 字段 | 类型/说明 |
| --- | --- |
| `code` required | string 货物运单标识符。 |
| `supply_id` required | string 交货标识符。 |

### 表格 1

| 字段 | 类型/说明 |
| --- | --- |
| `error_message` | string 错误描述。 |
| `label_url` | string 交货标签链接。 |
| `state` | string Default: "STATE_TYPE_UNSPECIFIED" Enum: "STATE_TYPE_UNSPECIFIED" "IN_PROGRESS" "FINISHED" "FAILED" 生成状态： STATE_TYPE_UNSPECIFIED ——未定义； IN_PROGRESS ——进行中； FINISHED ——成功完成； FAILED ——错误。 |

## 示例

### 示例 0

```text
STATE_TYPE_UNSPECIFIED
```

### 示例 1

```text
IN_PROGRESS
```

### 示例 2

```text
FINISHED
```

### 示例 3

```text
FAILED
```

### 示例 4

```json
{
  "code": "string",
  "supply_id": "string"
}
```

### 示例 5

```json
{
  "error_message": "string",
  "label_url": "string",
  "state": "STATE_TYPE_UNSPECIFIED"
}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

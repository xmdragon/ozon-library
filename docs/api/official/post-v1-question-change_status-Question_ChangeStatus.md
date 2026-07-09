# 更改问题状态

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/question/change_status`
- Operation ID：`Question_ChangeStatus`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/Question_ChangeStatus
- 分组：`question`

## 页面标题结构

- 更改问题状态
- header Parameters
- Request Body schema: application/json
- 回复
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
| `question_ids` required | Array of strings 问题标识符。 |
| `status` required | string 问题状态： NEW——新的， VIEWED——已查看， PROCESSED——已处理。 |

## 示例

### 示例 0

```text
NEW
```

### 示例 1

```text
VIEWED
```

### 示例 2

```text
PROCESSED
```

### 示例 3

```json
{
  "question_ids": [
    "string"
  ],
  "status": "VIEWED"
}
```

### 示例 4

```json
{
  "code": 0,
  "details": "string",
  "message": "string"
}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

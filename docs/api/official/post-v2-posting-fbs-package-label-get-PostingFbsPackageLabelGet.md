# 获取标签文件

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v2/posting/fbs/package-label/get`
- Operation ID：`PostingFbsPackageLabelGet`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/#operation/PostingFbsPackageLabelGet
- 分组：`posting`

## News 更新标记

| 日期 | 标记 | 摘要 | 来源 |
| --- | --- | --- | --- |
| 2026-10-15 | `new_method` | /v2/posting/fbs/package-label/get 新增了获取标签文件方法的新版本。 | [官方 News](https://docs.ozon.ru/api/seller/zh/#section/20261015) |

## 页面标题结构

- 获取标签文件
- HEADER PARAMETERS
- REQUEST BODY SCHEMA: application/json
- 回复
- RESPONSE SCHEMA: application/json
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
| `task_id` required | integer <int64> 任务ID，取自方法/v3/posting/fbs/package-label/create的响应。 |

### 表格 2

| 字段 | 类型/说明 |
| --- | --- |
| `error` | object 生成标签时出现的错误。 |
| `file_url` | string 标签文件链接。 |
| `status` | object 任务状态。 |

## 示例

### 示例 0

```json
{
  "task_id": 0
}
```

### 示例 1

```json
{
  "error": {
    "code": "string",
    "message": "string"
  },
  "file_url": "string",
  "status": {
    "code": "string",
    "postings_count": 0,
    "printed_postings_count": 0,
    "unprinted_postings": [
      {
        "message": "string",
        "posting_number": "string"
      }
    ]
  }
}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

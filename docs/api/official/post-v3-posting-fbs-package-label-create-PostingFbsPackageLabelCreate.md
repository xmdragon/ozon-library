# 创建标签生成任务

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v3/posting/fbs/package-label/create`
- Operation ID：`PostingFbsPackageLabelCreate`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/#operation/PostingFbsPackageLabelCreate
- 分组：`posting`

## News 更新标记

| 日期 | 标记 | 摘要 | 来源 |
| --- | --- | --- | --- |
| 2026-10-15 | `new_method` | /v3/posting/fbs/package-label/create 新增了创建标签生成任务方法的新版本。 | [官方 News](https://docs.ozon.ru/api/seller/zh/#section/20261015) |

## 页面标题结构

- 创建标签生成任务
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
| `posting_numbers` required | Array of strings [ 1 .. 1000 ] items 需要标签的货件编号。 |

### 表格 2

| 字段 | 类型/说明 |
| --- | --- |
| `tasks` | Array of objects 任务列表。 |
| `task_id` | integer <int64> 任务ID。 请通过方法/v2/posting/fbs/package-label/get获取标签文件。 |
| `task_type` | string 任务类型： big_label——用于常规标签； small_label——用于小标签。 |

### 表格 3

| 字段 | 类型/说明 |
| --- | --- |
| `task_id` | integer <int64> 任务ID。 请通过方法/v2/posting/fbs/package-label/get获取标签文件。 |
| `task_type` | string 任务类型： big_label——用于常规标签； small_label——用于小标签。 |

## 示例

### 示例 0

```json
{
  "posting_numbers": [
    "string"
  ]
}
```

### 示例 1

```json
{
  "tasks": [
    {
      "task_id": 0,
      "task_type": "string"
    }
  ]
}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

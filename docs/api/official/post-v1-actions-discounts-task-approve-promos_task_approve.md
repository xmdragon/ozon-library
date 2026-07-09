# 同意折扣申请

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/actions/discounts-task/approve`
- Operation ID：`promos_task_approve`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/promos_task_approve
- 分组：`actions`

## 页面标题结构

- 同意折扣申请
- Request Body schema: application/json
- 回复
- Response Schema: application/json
- 请求范例
- 回复范例

## 参数与返回结构

### 表格 0

| 字段 | 类型/说明 |
| --- | --- |
| `tasks` required | Array of objects 申请列表。 |

### 表格 1

| 字段 | 类型/说明 |
| --- | --- |
| `result` | object 方法操作结果。 |
| `fail_details` | Array of objects 创建申请时的错误。 |
| `success_count` | integer <int32> 状态更改成功的申请数量。 |
| `fail_count` | integer <int32> 未能更改状态的申请数量。 |

### 表格 2

| 字段 | 类型/说明 |
| --- | --- |
| `fail_details` | Array of objects 创建申请时的错误。 |
| `success_count` | integer <int32> 状态更改成功的申请数量。 |
| `fail_count` | integer <int32> 未能更改状态的申请数量。 |

## 示例

### 示例 0

```text
NEW
```

### 示例 1

```text
SEEN
```

### 示例 2

```json
{"tasks": [{"id": 78901,"approved_price": 12500,"seller_comment": "ok","approved_quantity_min": 3,"approved_quantity_max": 7}]}
```

### 示例 3

```json
{"result": {"fail_details": [{"task_id": 78901,"error_for_user": "折扣已拒绝"}],"success_count": 5,"fail_count": 1}}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

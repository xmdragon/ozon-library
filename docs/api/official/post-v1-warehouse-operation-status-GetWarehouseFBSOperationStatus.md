# 获取操作状态

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/warehouse/operation/status`
- Operation ID：`GetWarehouseFBSOperationStatus`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/#operation/GetWarehouseFBSOperationStatus
- 分组：`warehouse`

## News 更新标记

| 日期 | 标记 | 摘要 | 来源 |
| --- | --- | --- | --- |
| 2026-02-02 | `graduated` | /v1/warehouse/operation/status 已将该方法从Beta版迁移至正式版。 | [官方 News](https://docs.ozon.ru/api/seller/zh/#section/202622) |

## 页面标题结构

- 获取操作状态
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
| `operation_id` required | string 操作ID。 |

### 表格 2

| 字段 | 类型/说明 |
| --- | --- |
| `error` | object 处理操作时出错。 |
| `result` | object 操作结果。 |
| `status` | string Default: "UNSPECIFIED" Enum: "UNSPECIFIED" "IN_PROGRESS" "SUCCESS" "ERROR" 操作状态： UNSPECIFIED — 未定义； IN_PROGRESS — 进行中； SUCCESS — 已完成； ERROR — 出错结束。 |
| `type` | string Default: "UNSPECIFIED" Enum: "UNSPECIFIED" "CREATE_FBS_WAREHOUSE" "UPDATE_FBS_WAREHOUSE" "SET_FIRST_MILE" "WAREHOUSE_ENABLE_DISABLE" 操作类型： UNSPECIFIED — 未定义； CREATE_FBS_WAREHOUSE — 创建FBS仓库； UPDATE_FBS_WAREHOUSE — 更新FBS仓库； SET_FIRST_MILE — 设置头程物流； WAREHOUSE_ENABLE_DISABLE — 归档或取消归档FBS仓库。 |

### 表格 3

| 字段 | 类型/说明 |
| --- | --- |
| `entity_id` | integer <int64> 正在处理的实体ID。如果操作为 CREATE_FBS_WAREHOUSE，则返回仓库ID。 |

## 示例

### 示例 0

```json
{
  "operation_id": "a0cfefee-9a5a-4580-bc32-2f9a6c7973e3"
}
```

### 示例 1

```json
{
  "error": {
    "code": "string",
    "message": "string"
  },
  "result": {
    "warehouse_id": 1020005000219156
  },
  "status": "SUCCESS",
  "type": "CREATE_FBS_WAREHOUSE"
}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

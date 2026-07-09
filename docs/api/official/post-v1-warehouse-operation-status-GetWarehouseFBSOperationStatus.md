# 获取操作状态

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/warehouse/operation/status`
- Operation ID：`GetWarehouseFBSOperationStatus`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/GetWarehouseFBSOperationStatus
- 分组：`warehouse`

## 页面标题结构

- 获取操作状态
- header Parameters
- Request Body schema: application/json
- 回复
- Response Schema: application/json
- 请求范例
- 回复范例

## 参数与返回结构

### 表格 0

Client-Id required string 用户识别号。 Api-Key required string API-密钥。

### 表格 1

operation_id required string 操作ID。

### 表格 2

errorobject 处理操作时出错。 resultobject 操作结果。 entity_idinteger <int64> 正在处理的实体ID。如果操作为 CREATE_FBS_WAREHOUSE，则返回仓库ID。 statusstring Default: "UNSPECIFIED" Enum: "UNSPECIFIED" "IN_PROGRESS" "SUCCESS" "ERROR" 操作状态： UNSPECIFIED — 未定义； IN_PROGRESS — 进行中； SUCCESS — 已完成； ERROR — 出错结束。 typestring Default: "UNSPECIFIED" Enum: "UNSPECIFIED" "CREATE_FBS_WAREHOUSE" "UPDATE_FBS_WAREHOUSE" "SET_FIRST_MILE" "WAREHOUSE_ENABLE_DISABLE" 操作类型： UNSPECIFIED — 未定义； CREATE_FBS_WAREHOUSE — 创建FBS仓库； UPDATE_FBS_WAREHOUSE — 更新FBS仓库； SET_FIRST_MILE — 设置头程物流； WAREHOUSE_ENABLE_DISABLE — 归档或取消归档FBS仓库。

### 表格 3

entity_idinteger <int64> 正在处理的实体ID。如果操作为 CREATE_FBS_WAREHOUSE，则返回仓库ID。

## 示例

### 示例 0

```text
CREATE_FBS_WAREHOUSE
```

### 示例 1

```text
UNSPECIFIED
```

### 示例 2

```text
IN_PROGRESS
```

### 示例 3

```text
SUCCESS
```

### 示例 4

```text
ERROR
```

### 示例 5

```text
UNSPECIFIED
```

### 示例 6

```text
CREATE_FBS_WAREHOUSE
```

### 示例 7

```text
UPDATE_FBS_WAREHOUSE
```

### 示例 8

```text
SET_FIRST_MILE
```

### 示例 9

```text
WAREHOUSE_ENABLE_DISABLE
```

### 示例 10

```json
{"operation_id": "a0cfefee-9a5a-4580-bc32-2f9a6c7973e3"}
```

### 示例 11

```json
{"error": {"code": "string","message": "string"},"result": {"warehouse_id": 1020005000219156},"status": "SUCCESS","type": "CREATE_FBS_WAREHOUSE"}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

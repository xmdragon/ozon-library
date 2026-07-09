# 创建通行证

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/carriage/pass/create`
- Operation ID：`carriagePassCreate`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/carriagePassCreate
- 分组：`carriage`

## 页面标题结构

- 创建通行证
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

arrival_passes required Array of objects 通行证列表。 carriage_id required integer <int64> 运输ID。

### 表格 2

arrival_pass_idsArray of strings <int64> 通行证ID。

## 示例

### 示例 0

```json
{"carriage_id": 5000123456,"arrival_passes": [{"arrival_time": "string","driver_name": "string","driver_phone": "+79991234567","tracking_number": "string","tracking_url": "string","vehicle_license_plate": "string","vehicle_model": "string","with_returns": true}]}
```

### 示例 1

```json
{"arrival_pass_ids": [6000123456]}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

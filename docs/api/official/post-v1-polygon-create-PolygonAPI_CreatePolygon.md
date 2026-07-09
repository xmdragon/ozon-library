# 创建一个快递的设施

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/polygon/create`
- Operation ID：`PolygonAPI_CreatePolygon`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/PolygonAPI_CreatePolygon
- 分组：`polygon`

## 页面标题结构

- 创建一个快递的设施
- header Parameters
- Request Body schema: application/json
- 回复
- Response Schema: application/json
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
| `coordinates` required | string 快递设施的坐标，格式为 [[[lat long]]]。 |

### 表格 2

| 字段 | 类型/说明 |
| --- | --- |
| `polygon_id` | integer <int64> 设施识别号。 |

## 示例

### 示例 0

```json
[[[long lat]]]
```

### 示例 1

```json
[[[lat long]]]
```

### 示例 2

```json
{"coordinates": "[[[30.149574279785153,59.86550435303646],[30.21205902099609,59.846884387977326],[30.255661010742184,59.86240174913176],[30.149574279785153,59.86550435303646]]]"}
```

### 示例 3

```json
{"polygonId": "1323"}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

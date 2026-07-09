# 根据状态统计的评价数量

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/review/count`
- Operation ID：`ReviewAPI_ReviewCount`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/ReviewAPI_ReviewCount
- 分组：`review`

## 页面标题结构

- 根据状态统计的评价数量
- Request Body schema: application/json
- 回复
- Response Schema: application/json
- 请求范例
- 回复范例

## 参数与返回结构

### 表格 0

| 字段 | 类型/说明 |
| --- | --- |
| `processed` | integer <int32> 已处理评价的数量。 |
| `total` | integer <int32> 评价的总数量。 |
| `unprocessed` | integer <int32> 未处理评价的数量。 |

## 示例

### 示例 0

```json
{ }
```

### 示例 1

```json
{"processed": 0,"total": 0,"unprocessed": 0}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

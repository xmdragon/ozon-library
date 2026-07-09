# 按状态统计问题数量

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/question/count`
- Operation ID：`Question_Count`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/Question_Count
- 分组：`question`

## 页面标题结构

- 按状态统计问题数量
- header Parameters
- 回复
- Response Schema: application/json
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
| `all` | integer <int64> 问题总数。 |
| `new` | integer <int64> 新问题数量。 |
| `processed` | integer <int64> 已处理问题数量。 |
| `unprocessed` | integer <int64> 未处理问题数量。 |
| `viewed` | integer <int64> 已查看问题数量。 |

## 示例

### 示例 0

```json
{
  "all": 10,
  "new": 3,
  "processed": 4,
  "unprocessed": 1,
  "viewed": 1
}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

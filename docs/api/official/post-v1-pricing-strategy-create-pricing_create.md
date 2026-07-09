# 创建策略

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/pricing-strategy/create`
- Operation ID：`pricing_create`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/pricing_create
- 分组：`pricing-strategy`

## 页面标题结构

- 创建策略
- Request Body schema: application/json
- 回复
- Response Schema: application/json
- 请求范例
- 回复范例

## 参数与返回结构

### 表格 0

| 字段 | 类型/说明 |
| --- | --- |
| `competitors` required | Array of objects 竞争对手名单。 |
| `strategy_name` required | string 策略名称。 |

### 表格 1

| 字段 | 类型/说明 |
| --- | --- |
| `result` | object 方法操作结果。 |
| `strategy_id` | string 策略ID。 |

### 表格 2

| 字段 | 类型/说明 |
| --- | --- |
| `strategy_id` | string 策略ID。 |

## 示例

### 示例 0

```json
{
  "strategy_name": "新策略",
  "competitors": [
    {
      "competitor_id": 1008426,
      "coefficient": 1
    },
    {
      "competitor_id": 204,
      "coefficient": 1
    },
    {
      "competitor_id": 91,
      "coefficient": 1
    },
    {
      "competitor_id": 48,
      "coefficient": 1
    }
  ],
  "company_id": 7
}
```

### 示例 1

```json
{
  "result": {
    "id": "4f3a1d4c-5833-4f04-b69b-495cbc1f6f1c"
  }
}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

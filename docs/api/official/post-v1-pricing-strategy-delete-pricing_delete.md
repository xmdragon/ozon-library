# 删除策略

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/pricing-strategy/delete`
- Operation ID：`pricing_delete`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/pricing_delete
- 分组：`pricing-strategy`

## 页面标题结构

- 删除策略
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
| `strategy_id` required | string 策略ID。 |

## 示例

### 示例 0

```json
{
  "strategy_id": "b7cd30e6-5667-424d-b105-fbec30a52477"
}
```

### 示例 1

```json
{}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

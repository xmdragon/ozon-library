# 更改策略状态

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/pricing-strategy/status`
- Operation ID：`pricing_status`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/pricing_status
- 分组：`pricing-strategy`

## 页面标题结构

- 更改策略状态
- Request Body schema: application/json
- 回复
- Response Schema: application/json
- 请求范例
- 回复范例

## 参数与返回结构

### 表格 0

enabledboolean 策略状态： true —— 打开， false —— 关闭。 strategy_id required string 策略ID。

## 示例

### 示例 0

```json
{"strategy_id": "c7516438-7124-4e2c-85d3-ccd92b6b9b65","enabled": true}
```

### 示例 1

```json
{ }
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

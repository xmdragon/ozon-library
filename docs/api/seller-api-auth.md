# Seller API 授权和请求规则

## 用途

记录官方 Seller API 的认证 header、调用边界、限流和错误处理。

## AI 摘要

Seller API 使用 `Client-Id` 和 `Api-Key` 两个 header。ZhiPin 后端 client 通过 `httpx.AsyncClient` 设置 base URL、这两个 header 和 `Content-Type: application/json`，并在每次请求加 `X-Request-Id`。官方文档说明 key 有有效期，且从一个 Client ID 向所有方法每秒最多 50 个请求。浏览器直接请求官方 Seller API 会因 CORS 被拒绝，应该从后端调用。

## 关键接口

| 项 | 内容 |
| --- | --- |
| 官方角色查询 | `POST /v1/roles`，operation `AccessAPI_RolesByToken` |
| 必需 header | `Client-Id`、`Api-Key` |
| 响应字段 | `expires_at`、`roles[].methods` |
| 后端测试连接 | ZhiPin 使用 `POST /v3/product/list`，limit 1 |
| 默认限流 | ZhiPin RateLimiter 对 products/orders/postings/categories/default 等设为 50 req/s |

## 流程

1. 从卖家个人中心创建 API key。
2. 后端保存 `client_id` 和 `api_key`，不要暴露给浏览器。
3. 请求时设置 `Client-Id`、`Api-Key`、`Content-Type`。
4. 按资源类型进入限流器。
5. 请求失败时区分 401、403、429、5xx、timeout/connection error。

## 异常与恢复

| 情况 | 处理 |
| --- | --- |
| 401 | 凭证无效，提示重新配置。 |
| 403 | 权限不足、key 失效或店铺状态异常；ZhiPin 会检查 `deactivated`、`invalid api-key` 等消息并停用店铺。 |
| 429 | 读取 `Retry-After`，等待后重试。 |
| 5xx | ZhiPin 对服务端错误做最多 3 次指数退避重试。 |
| timeout/connect error | 可重试；最终失败要暴露网络/连接错误。 |
| 二进制响应 | ZhiPin 对无法 UTF-8 解码的响应单独报错，避免把 PDF 当 JSON。 |

## 来源引用

- 官方 operation：`AccessAPI_RolesByToken`
- `/Users/eric/works/ZhiPin/plugins/ef/channels/ozon/api/client_mixins/base.py`
- `indexes/official-seller-api.operations.json`

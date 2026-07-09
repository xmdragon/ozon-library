# 使用API密钥获取角色和方式列表

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/roles`
- Operation ID：`AccessAPI_RolesByToken`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/AccessAPI_RolesByToken
- 分组：`roles`

## 页面标题结构

- 使用API密钥获取角色和方式列表
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
| `expires_at` | string <date-time> 密钥到期日期。 |
| `roles` | Array of objects 可用角色和方式信息。 |

## 示例

### 示例 0

```json
{"expires_at": "2026-02-18T09:54:23.296Z","roles": [{"name": "Admin","methods": ["/v1/actions"]},{"name": "Posting FBS","methods": ["/v1/posting"]}]}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

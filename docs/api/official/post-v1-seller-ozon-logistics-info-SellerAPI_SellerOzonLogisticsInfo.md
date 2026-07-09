# Ozon配送开通信息

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/seller/ozon-logistics/info`
- Operation ID：`SellerAPI_SellerOzonLogisticsInfo`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/SellerAPI_SellerOzonLogisticsInfo
- 分组：`seller`

## News 更新标记

| 日期 | 标记 | 摘要 | 来源 |
| --- | --- | --- | --- |
| 2026-05-05 | `updated` | /v1/seller/ozon-logistics/info 更新了方法名称。更新了方法响应中参数ozon_logistics_enabled的说明。 | [官方 News](https://docs.ozon.ru/api/seller/zh/#section/202655) |

## 页面标题结构

- Ozon配送开通信息
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
| `available_schemas` | Array of strings Default: "UNKNOWN"Items Enum: "UNKNOWN" "FBO" "FBS" 可用模式类型： UNKNOWN——未指定； FBO——从Ozon仓库配送； FBS——从自有仓库配送。 |
| `ozon_logistics_enabled` | boolean true，表示Ozon配送已开通。 |

## 示例

### 示例 0

```text
UNKNOWN
```

### 示例 1

```text
FBO
```

### 示例 2

```text
FBS
```

### 示例 3

```text
true
```

### 示例 4

```json
{
  "available_schemas": [
    "UNKNOWN"
  ],
  "ozon_logistics_enabled": true
}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

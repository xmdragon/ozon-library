# 获取每订单商品销售报告

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/report/realization/posting/create`
- Operation ID：`CreateCompanyFinanceRealizationPostingReport`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/#operation/CreateCompanyFinanceRealizationPostingReport
- 分组：`report`

## 页面标题结构

- 获取每订单商品销售报告
- HEADER PARAMETERS
- REQUEST BODY SCHEMA: application/json
- 回复
- RESPONSE SCHEMA: application/json
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
| `month` required | integer <int32> 月份。 |
| `year` required | integer <int32> 年份。 |

### 表格 2

| 字段 | 类型/说明 |
| --- | --- |
| `code` | string 报告的唯一标识符。使用方法/v1/report/info获取报告。 |

## 示例

### 示例 0

```json
{
  "month": 0,
  "year": 0
}
```

### 示例 1

```json
{
  "code": "string"
}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

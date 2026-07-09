# 发货报告

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/report/postings/create`
- Operation ID：`ReportAPI_CreateCompanyPostingsReport`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/ReportAPI_CreateCompanyPostingsReport
- 分组：`report`

## 页面标题结构

- 发货报告
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
| `filter` required | object 过滤器。 |
| `language` | string Default: "DEFAULT" 回答所用语言： RU — 俄语， EN — 英语。 |
| `with` | object 额外的字段，需要添加到响应中。 |

### 表格 2

| 字段 | 类型/说明 |
| --- | --- |
| `result` | object 请求结果。 |
| `code` | string 报告的唯一识别码。要获取报告，请将此值传递到方法 /v1/report/info。 |

### 表格 3

| 字段 | 类型/说明 |
| --- | --- |
| `code` | string 报告的唯一识别码。要获取报告，请将此值传递到方法 /v1/report/info。 |

## 示例

### 示例 0

```text
RU
```

### 示例 1

```text
EN
```

### 示例 2

```json
{
  "filter": {
    "processed_at_from": "2021-09-02T17:10:54.861Z",
    "processed_at_to": "2021-11-02T17:10:54.861Z",
    "delivery_schema": [
      "fbs"
    ],
    "is_express": true,
    "sku": [],
    "cancel_reason_id": [],
    "offer_id": "",
    "status_alias": [],
    "statuses": [],
    "title": ""
  },
  "language": "DEFAULT",
  "with": {
    "additional_data": false,
    "analytics_data": false,
    "customer_data": false,
    "jewelry_codes": false
  }
}
```

### 示例 3

```json
{
  "result": {
    "code": "REPORT_seller_postings_514893_1722847571_32a3508c-6b53-408c-a212-6c97138d23ed"
  }
}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

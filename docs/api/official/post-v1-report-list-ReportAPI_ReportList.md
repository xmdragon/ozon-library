# 报告清单

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/report/list`
- Operation ID：`ReportAPI_ReportList`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/ReportAPI_ReportList
- 分组：`report`

## News 更新标记

| 日期 | 标记 | 摘要 | 来源 |
| --- | --- | --- | --- |
| 2026-02-03 | `updated` | /v1/report/list 更新了方法请求中的 report_type 参数描述。已更新方法响应中 result.reports.report_type 参数的描述。 | [官方 News](https://docs.ozon.ru/api/seller/zh/#section/202623) |
| 2026-01-16 | `updated` | /v1/report/list 已更新方法请求中 report_type 参数以及方法响应中 result.reports.report_type 的描述。 | [官方 News](https://docs.ozon.ru/api/seller/zh/#section/2026116) |
| 2025-11-18 | `added_field` | /v1/report/list 在方法的响应中新增参数result.reports.expires_at。 | [官方 News](https://docs.ozon.ru/api/seller/zh/#section/20251118) |
| 2025-05-05 | `updated` | /v1/report/list 更新了 report_type 参数在方法请求和响应中的描述。 | [官方 News](https://docs.ozon.ru/api/seller/zh/#section/202555) |

## 页面标题结构

- 报告清单
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
| `page` required | integer <int32> 页数。 |
| `page_size` required | integer <int32> 每页的值的数量： 默认值 — 100， 最大值 — 1,000。 |
| `report_type` | string Default: "ALL" 报告类型： ALL— 所有报告， SELLER_PRODUCTS — 商品报告， SELLER_STOCK — 商品库存报告， SELLER_RETURNS — 退货报告， SELLER_POSTINGS — 发货报告， SELLER_DISCOUNTED — 减价商品报告， MUTUAL_SETTLEMENT — 结算报告， DOCUMENT_B2B_SALES — 面向法人客户的销售报告， COMPENSATION_REPORT — 赔偿报告， DECOMPENSATION_REPORT — 赔偿返还报告， MARKED_PRODUCTS_SALES — 标签销售报告， SELLER_PLACEMENT_BY_PRODUCTS — 按商品维度的存储服务费用报告， SELLER_PLACEMENT_BY_SUPPLIES — 按交货维度的存储服务费用报告。 |

### 表格 2

| 字段 | 类型/说明 |
| --- | --- |
| `result` | object 请求结果。 |
| `reports` | Array of objects 包含所有生成的报告的数组。 |
| `total` | integer <int32> 累计报告数。 |

### 表格 3

| 字段 | 类型/说明 |
| --- | --- |
| `reports` | Array of objects 包含所有生成的报告的数组。 |
| `total` | integer <int32> 累计报告数。 |

## 示例

### 示例 0

```text
ALL
```

### 示例 1

```text
SELLER_PRODUCTS
```

### 示例 2

```text
SELLER_STOCK
```

### 示例 3

```text
SELLER_RETURNS
```

### 示例 4

```text
SELLER_POSTINGS
```

### 示例 5

```text
SELLER_DISCOUNTED
```

### 示例 6

```text
MUTUAL_SETTLEMENT
```

### 示例 7

```text
DOCUMENT_B2B_SALES
```

### 示例 8

```text
COMPENSATION_REPORT
```

### 示例 9

```text
DECOMPENSATION_REPORT
```

### 示例 10

```text
MARKED_PRODUCTS_SALES
```

### 示例 11

```text
SELLER_PLACEMENT_BY_PRODUCTS
```

### 示例 12

```text
SELLER_PLACEMENT_BY_SUPPLIES
```

### 示例 13

```json
{
  "page": 1,
  "page_size": 1000,
  "report_type": "ALL"
}
```

### 示例 14

```json
{
  "result": {
    "reports": [
      {
        "code": "REPORT_seller_products_924336_1720170405_a9ea2f27-a473-4b13-99f9-d0cfcb5b1a69",
        "status": "success",
        "error": "",
        "expires_at": "2025-11-12T19:55:28.249Z",
        "file": "https://ir-21.ozonru.cn/s3/item-picture-6/f3/ce/f4ceae54b323213d3e61e59c323bd8e5.csv",
        "report_type": "seller_products",
        "params": {
          "visibility": "3"
        },
        "created_at": "2019-02-06T12:09:47.258062Z"
      },
      {
        "code": "REPORT_seller_products_924336_1720170405_a9ea2f27-a473-4b13-99f9-d0cfcb5b1a69",
        "status": "success",
        "error": "",
        "file": "https://ir-21.ozonru.cn/s3/item-picture-6/f3/ce/f4ceae54b323213d3e61e59c323bd8e5.csv",
        "report_type": "seller_products",
        "params": {
          "visibility": "3"
        },
        "created_at": "2019-02-15T08:34:32.267178Z"
      }
    ],
    "total": 2
  }
}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

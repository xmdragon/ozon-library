# 报告信息

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/report/info`
- Operation ID：`ReportAPI_ReportInfo`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/ReportAPI_ReportInfo
- 分组：`report`

## 页面标题结构

- 报告信息
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
| `code` required | string 报告的唯一识别码。 |

### 表格 2

| 字段 | 类型/说明 |
| --- | --- |
| `result` | object 关于报告的信息。 |
| `code` | string 报告的唯一识别码。 |
| `created_at` | string <date-time> 报告创建日期。 |
| `error` | string 生成报告时的错误代码。 |
| `expires_at` | string <date-time> 报告链接的有效日期和时间。 如果报告生成于 2025 年 10 月 14 日之前，该字段将为空。 |
| `file` | string XLSX文件的链接。 SELLER_RETURNS 类型的报告，链接有效期为5分钟。 |
| `params` | object 一个数组，包含卖家创建报告时指定的过滤器。 |
| `report_type` | string 报告类型： SELLER_PRODUCTS — 商品报告， SELLER_STOCK — 商品库存报告， SELLER_RETURNS — 退货报告， SELLER_POSTINGS — 发货报告， SELLER_DISCOUNTED — 减价商品报告， MUTUAL_SETTLEMENT — 结算报告， DOCUMENT_B2B_SALES — 面向法人客户的销售报告， COMPENSATION_REPORT — 赔偿报告， DECOMPENSATION_REPORT — 赔偿返还报告， MARKED_PRODUCTS_SALES — 标签销售报告， SELLER_PLACEMENT_BY_PRODUCTS — 按商品维度的存储服务费用报告， SELLER_PLACEMENT_BY_SUPPLIES — 按交货维度的存储服务费用报告。 |
| `status` | string 报告生成状态： waiting—在等待队列中待处理， processing—正在处理， success， failed。 |

### 表格 3

| 字段 | 类型/说明 |
| --- | --- |
| `code` | string 报告的唯一识别码。 |
| `created_at` | string <date-time> 报告创建日期。 |
| `error` | string 生成报告时的错误代码。 |
| `expires_at` | string <date-time> 报告链接的有效日期和时间。 如果报告生成于 2025 年 10 月 14 日之前，该字段将为空。 |
| `file` | string XLSX文件的链接。 SELLER_RETURNS 类型的报告，链接有效期为5分钟。 |
| `params` | object 一个数组，包含卖家创建报告时指定的过滤器。 |
| `report_type` | string 报告类型： SELLER_PRODUCTS — 商品报告， SELLER_STOCK — 商品库存报告， SELLER_RETURNS — 退货报告， SELLER_POSTINGS — 发货报告， SELLER_DISCOUNTED — 减价商品报告， MUTUAL_SETTLEMENT — 结算报告， DOCUMENT_B2B_SALES — 面向法人客户的销售报告， COMPENSATION_REPORT — 赔偿报告， DECOMPENSATION_REPORT — 赔偿返还报告， MARKED_PRODUCTS_SALES — 标签销售报告， SELLER_PLACEMENT_BY_PRODUCTS — 按商品维度的存储服务费用报告， SELLER_PLACEMENT_BY_SUPPLIES — 按交货维度的存储服务费用报告。 |
| `status` | string 报告生成状态： waiting—在等待队列中待处理， processing—正在处理， success， failed。 |

## 示例

### 示例 0

```text
SELLER_RETURNS
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

```text
waiting
```

### 示例 14

```text
processing
```

### 示例 15

```text
success
```

### 示例 16

```text
failed
```

### 示例 17

```json
{"code": "REPORT_seller_products_924336_1720170405_a9ea2f27-a473-4b13-99f9-d0cfcb5b1a69"}
```

### 示例 18

```json
{"result": {"code": "REPORT_seller_products_924336_1720170405_a9ea2f27-a473-4b13-99f9-d0cfcb5b1a69","status": "success","error": "","expires_at": "2025-11-12T19:53:08.770Z","file": "https://ir-21.ozonru.cn/s3/item-picture-6/f3/ce/f4ceae54b323213d3e61e59c323bd8e5.csv","report_type": "seller_products","params": { },"created_at": "2021-11-25T14:54:55.688260Z"}}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

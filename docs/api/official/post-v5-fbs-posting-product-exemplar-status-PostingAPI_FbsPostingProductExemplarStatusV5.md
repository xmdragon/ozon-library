# 获取样件添加状态

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v5/fbs/posting/product/exemplar/status`
- Operation ID：`PostingAPI_FbsPostingProductExemplarStatusV5`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/#operation/PostingAPI_FbsPostingProductExemplarStatusV5
- 分组：`fbs`

## News 更新标记

| 日期 | 标记 | 摘要 | 来源 |
| --- | --- | --- | --- |
| 2026-10-22 | `graduated` | /v5/fbs/posting/product/exemplar/status 已将该方法从Beta版迁移至正式版。 | [官方 News](https://docs.ozon.ru/api/seller/zh/#section/20261022) |
| 2025-12-25 | `updated` | /v5/fbs/posting/product/exemplar/status 已更新方法响应中参数 products.exemplars.marks.check_status 的说明。 | [官方 News](https://docs.ozon.ru/api/seller/zh/#section/20251225) |
| 2025-12-16 | `updated` | /v5/fbs/posting/product/exemplar/status 更新了方法响应中的 status 参数描述。 | [官方 News](https://docs.ozon.ru/api/seller/zh/#section/20251216) |
| 2025-09-29 | `updated` | /v5/fbs/posting/product/exemplar/status 更新了方法响应中products.exemplars.marks参数的描述。 | [官方 News](https://docs.ozon.ru/api/seller/zh/#section/2025929) |
| 2025-02-17 | `new_method` | /v5/fbs/posting/product/exemplar/status 新增 Beta 方法用于管理标志代码。 | [官方 News](https://docs.ozon.ru/api/seller/zh/#section/2025217) |

## 页面标题结构

- 获取样件添加状态
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
| `posting_number` required | string 发货号。 |

### 表格 2

| 字段 | 类型/说明 |
| --- | --- |
| `posting_number` | string 发货号。 |
| `products` | Array of objects 商品清单。 |
| `status` | string 所有样件和备货可用性的验证状态： ship_available——可以备货， ship_not_available——无法备货， validation_in_process——样件正在验证中， update_available——可以编辑商品实例信息， update_not_available——无法编辑商品实例信息。 |

## 示例

### 示例 0

```json
{
  "posting_number": "789456123-0002-3"
}
```

### 示例 1

```json
{
  "posting_number": "789456123-0002-3",
  "products": [
    {
      "exemplars": [
        {
          "exemplar_id": 10001,
          "gtd": "GTD100500700/2026/0215",
          "gtd_check_status": "SUCCESS",
          "gtd_error_codes": [],
          "is_gtd_absent": false,
          "is_rnpt_absent": false,
          "marks": [
            {
              "check_status": "SUCCESS",
              "error_codes": [],
              "mark": "01046000123456789ABCDEF12345678",
              "mark_type": "DATA_MATRIX"
            },
            {
              "check_status": "WARNING",
              "error_codes": [
                "MARK_EXPIRED"
              ],
              "mark": "QR1234567890ABCDEF987654321",
              "mark_type": "QR_CODE"
            }
          ],
          "rnpt": "RNPT100200300400500",
          "rnpt_check_status": "SUCCESS",
          "rnpt_error_codes": [],
          "weight": 1250,
          "weight_check_status": "SUCCESS",
          "weight_error_codes": []
        },
        {
          "exemplar_id": 10002,
          "gtd": "",
          "gtd_check_status": "ERROR",
          "gtd_error_codes": [
            "GTD_MISSING"
          ],
          "is_gtd_absent": true,
          "is_rnpt_absent": true,
          "marks": [
            {
              "check_status": "ERROR",
              "error_codes": [
                "MARK_INVALID_FORMAT"
              ],
              "mark": "INVALID_MARK_123",
              "mark_type": "UNKNOWN"
            }
          ],
          "rnpt": "",
          "rnpt_check_status": "ERROR",
          "rnpt_error_codes": [
            "RNPT_MISSING"
          ],
          "weight": 0,
          "weight_check_status": "ERROR",
          "weight_error_codes": [
            "WEIGHT_ZERO"
          ]
        }
      ],
      "product_id": 123456789
    },
    {
      "exemplars": [
        {
          "exemplar_id": 20001,
          "gtd": "GTD200300400/2026/0301",
          "gtd_check_status": "WARNING",
          "gtd_error_codes": [
            "GTD_EXPIRED"
          ],
          "is_gtd_absent": false,
          "is_rnpt_absent": false,
          "marks": [
            {
              "check_status": "SUCCESS",
              "error_codes": [],
              "mark": "01046000987654321FEDCBA654321",
              "mark_type": "DATA_MATRIX"
            }
          ],
          "rnpt": "RNPT999888777666555",
          "rnpt_check_status": "WARNING",
          "rnpt_error_codes": [
            "RNPT_PARTIALLY_VALID"
          ],
          "weight": 3200,
          "weight_check_status": "SUCCESS",
          "weight_error_codes": []
        }
      ],
      "product_id": 987654321
    }
  ],
  "status": "PROCESSING_COMPLETED"
}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

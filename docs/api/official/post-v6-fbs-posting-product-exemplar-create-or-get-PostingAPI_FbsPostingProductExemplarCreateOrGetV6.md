# 获取已创建样件数据

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v6/fbs/posting/product/exemplar/create-or-get`
- Operation ID：`PostingAPI_FbsPostingProductExemplarCreateOrGetV6`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/#operation/PostingAPI_FbsPostingProductExemplarCreateOrGetV6
- 分组：`fbs`

## News 更新标记

| 日期 | 标记 | 摘要 | 来源 |
| --- | --- | --- | --- |
| 2026-10-22 | `graduated` | /v6/fbs/posting/product/exemplar/create-or-get 已将该方法从Beta版迁移至正式版。 | [官方 News](https://docs.ozon.ru/api/seller/zh/#section/20261022) |
| 2025-09-29 | `added_field` | /v6/fbs/posting/product/exemplar/create-or-get 已更新products.exemplars.marks参数的描述，并在方式响应中添加了products.has_imei参数。 | [官方 News](https://docs.ozon.ru/api/seller/zh/#section/2025929) |
| 2025-02-17 | `new_method` | /v6/fbs/posting/product/exemplar/create-or-get 新增 Beta 方法用于管理标志代码。 | [官方 News](https://docs.ozon.ru/api/seller/zh/#section/2025217) |

## 页面标题结构

- 获取已创建样件数据
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
| `multi_box_qty` | integer <int32> 商品包装的箱子数量。 |
| `posting_number` | string 发货号。 |
| `products` | Array of objects 商品清单。 |

## 示例

### 示例 0

```json
{
  "posting_number": "200039812931"
}
```

### 示例 1

```json
{
  "multi_box_qty": 2,
  "posting_number": "200039812931",
  "products": [
    {
      "exemplars": [
        {
          "exemplar_id": 1005001,
          "gtd": "10702020/1234567/А0123456",
          "is_gtd_absent": false,
          "is_rnpt_absent": false,
          "marks": [
            {
              "mark": "04612345678901!RU123456789ABC",
              "mark_type": "CIS"
            },
            {
              "mark": "01046123456789012121ABCDEFGHIJKLMNO",
              "mark_type": "GTIN"
            }
          ],
          "rnpt": "R0123456789",
          "weight": 1500
        },
        {
          "exemplar_id": 1005002,
          "gtd": null,
          "is_gtd_absent": true,
          "is_rnpt_absent": false,
          "marks": [
            {
              "mark": "04612345678902!RU987654321XYZ",
              "mark_type": "CIS"
            }
          ],
          "rnpt": "R9876543210",
          "weight": 1500
        }
      ],
      "has_imei": false,
      "is_gtd_needed": false,
      "is_jw_uin_needed": false,
      "is_mandatory_mark_needed": true,
      "is_mandatory_mark_possible": true,
      "is_rnpt_needed": true,
      "product_id": 987654321,
      "quantity": 2,
      "is_weight_needed": true,
      "weight_max": 2000,
      "weight_min": 1000
    },
    {
      "exemplars": [
        {
          "exemplar_id": 1005003,
          "gtd": null,
          "is_gtd_absent": true,
          "is_rnpt_absent": true,
          "marks": [],
          "rnpt": null,
          "weight": 0
        }
      ],
      "has_imei": true,
      "is_gtd_needed": false,
      "is_jw_uin_needed": false,
      "is_mandatory_mark_needed": false,
      "is_mandatory_mark_possible": false,
      "is_rnpt_needed": false,
      "product_id": 987654322,
      "quantity": 1,
      "is_weight_needed": false,
      "weight_max": 0,
      "weight_min": 0
    }
  ]
}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

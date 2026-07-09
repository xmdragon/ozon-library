# realFBS仓库的配送方式列表

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v2/delivery-method/list`
- Operation ID：`WarehouseAPI_DeliveryMethodListV2`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/WarehouseAPI_DeliveryMethodListV2
- 分组：`delivery-method`

## News 更新标记

| 日期 | 标记 | 摘要 | 来源 |
| --- | --- | --- | --- |
| 2026-05-22 | `added_field` | /v2/delivery-method/list 在方法响应中新增了参数delivery_methods.tpl_dropoff_point。 — 在错误板块中，已为 | [官方 News](https://docs.ozon.ru/api/seller/zh/#section/2026522) |
| 2026-03-04 | `new_method` | /v2/delivery-method/list 新增了用于获取rFBS仓库配送方式的方法。 | [官方 News](https://docs.ozon.ru/api/seller/zh/#section/202634) |

## 页面标题结构

- realFBS仓库的配送方式列表
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
| `cursor` | string 用于选择下一批数据的指针。 |
| `filter` | object 用于搜索配送方式的筛选条件。 |
| `limit` required | integer <int64> [ 1 .. 100 ] 响应中返回的值数量。 |
| `sort_dir` | string Enum: "ASC" "DESC" 排序方向： ASC：升序， DESC：降序。 |

### 表格 2

| 字段 | 类型/说明 |
| --- | --- |
| `cursor` | string 用于选择下一批数据的指针。 |
| `has_next` | boolean true，表示响应中未返回全部配送方式。 |
| `delivery_methods` | Array of objects 配送方式。 |

## 示例

### 示例 0

```text
ASC
```

### 示例 1

```text
DESC
```

### 示例 2

```text
true
```

### 示例 3

```json
{
  "cursor": "string",
  "filter": {
    "delivery_method_ids": [
      "string"
    ],
    "provider_ids": [
      "string"
    ],
    "status": [
      "NEW"
    ],
    "warehouse_ids": [
      "string"
    ]
  },
  "limit": 1,
  "sort_dir": "ASC"
}
```

### 示例 4

```json
{
  "cursor": "string",
  "has_next": true,
  "delivery_methods": [
    {
      "created_at": "2019-08-24T14:15:22Z",
      "cutoff": "string",
      "id": 0,
      "is_express": true,
      "name": "string",
      "provider_id": 0,
      "sla_cut_in": 0,
      "status": "NEW",
      "template_id": 0,
      "tpl_dropoff_point": {
        "address": "string",
        "address_coordinates": {
          "latitude": 0,
          "longitude": 0
        },
        "code": "string",
        "name": "string"
      },
      "tpl_integration_type": "string",
      "updated_at": "2019-08-24T14:15:22Z",
      "warehouse_id": 0
    }
  ]
}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

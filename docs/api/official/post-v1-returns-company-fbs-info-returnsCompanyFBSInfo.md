# FBS退货数量

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/returns/company/fbs/info`
- Operation ID：`returnsCompanyFBSInfo`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/returnsCompanyFBSInfo
- 分组：`returns`

## 页面标题结构

- FBS退货数量
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
| `filter` | object 筛选器。 |
| `pagination` required | object 方法响应的分割。 |

### 表格 2

| 字段 | 类型/说明 |
| --- | --- |
| `drop_off_points` | Array of objects 揽收点信息。 |
| `has_next` | boolean 是否还有其他揽收点等待卖家退货的标志。 |

## 示例

### 示例 0

```json
{
  "filter": {
    "place_id": 0
  },
  "pagination": {
    "last_id": 0,
    "limit": 500
  }
}
```

### 示例 1

```json
{
  "drop_off_points": [
    {
      "address": "string",
      "box_count": 0,
      "id": 0,
      "name": "string",
      "pass_info": {
        "count": 0,
        "is_required": true
      },
      "place_id": 0,
      "returns_count": 0,
      "utc_offset": "string",
      "warehouses_ids": [
        "string"
      ]
    }
  ],
  "has_next": true
}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

# 可用产地名单

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v2/posting/fbs/product/country/list`
- Operation ID：`PostingAPI_ListCountryProductFbsPostingV2`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/PostingAPI_ListCountryProductFbsPostingV2
- 分组：`posting`

## 页面标题结构

- 可用产地名单
- Request Body schema: application/json
- 回复
- Response Schema: application/json
- 请求范例
- 回复范例

## 参数与返回结构

### 表格 0

| 字段 | 类型/说明 |
| --- | --- |
| `name_search` | string 按行过滤。 |

### 表格 1

| 字段 | 类型/说明 |
| --- | --- |
| `result` | Array of objects 制造国和ISO代码列表。 |
| `name` | string 国家俄语名称 |
| `country_iso_code` | string ISO国家代码。 |

### 表格 2

| 字段 | 类型/说明 |
| --- | --- |
| `name` | string 国家俄语名称 |
| `country_iso_code` | string ISO国家代码。 |

## 示例

### 示例 0

```json
{
  "name_search": ""
}
```

### 示例 1

```json
{
  "result": [
    {
      "name": "阿尔及利亚",
      "country_iso_code": "DZ"
    },
    {
      "name": "安圭拉",
      "country_iso_code": "AI"
    },
    {
      "name": "维京群岛 （英国）",
      "country_iso_code": "VG"
    }
  ]
}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

# 获取错误指数：FBS 和 rFBS

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/rating/index/fbs/info`
- Operation ID：`RatingAPI_GetFBSRatingIndexInfoV1`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/RatingAPI_GetFBSRatingIndexInfoV1
- 分组：`rating`

## 页面标题结构

- 获取错误指数：FBS 和 rFBS
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
| `currency_code` | string 错误处理费用的币种代码。 |
| `defects` | Array of objects 按天计算的错误指数。 |
| `index` | number <double> 周期内的错误指数数值。 |
| `period_from` | string 计算周期开始日期（格式YYYY-MM-DD）。 |
| `period_to` | string 计算周期结束日期（格式YYYY-MM-DD）。 |
| `processing_costs_sum` | number <double> 周期内的错误处理费用。 |

## 示例

### 示例 0

```text
YYYY-MM-DD
```

### 示例 1

```text
YYYY-MM-DD
```

### 示例 2

```json
{
  "currency_code": "string",
  "defects": [
    {
      "date": "string",
      "index_by_date": 0,
      "processing_costs_sum_by_date": 0
    }
  ],
  "index": 0,
  "period_from": "string",
  "period_to": "string",
  "processing_costs_sum": 0
}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

# 最低价格时效性计时器更新

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/product/action/timer/update`
- Operation ID：`ProductAPI_ActionTimerUpdate`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/ProductAPI_ActionTimerUpdate
- 分组：`product`

## News 更新标记

| 日期 | 标记 | 摘要 | 来源 |
| --- | --- | --- | --- |
| 2025-08-21 | `updated` | /v1/product/action/timer/update 已为最低价格时效性计时器更新添加方式。 | [官方 News](https://docs.ozon.ru/api/seller/zh/#section/2025821) |

## 页面标题结构

- 最低价格时效性计时器更新
- header Parameters
- Request Body schema: application/json
- 回复
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
| `product_ids` | Array of strings <int64> <= 1000 items 卖家系统中的商品识别符列表——product_id。 |

## 示例

### 示例 0

```text
product_ids
```

### 示例 1

```text
product_id
```

### 示例 2

```json
{
  "product_ids": 88787267123
}
```

### 示例 3

```json
{
  "code": 0,
  "details": [
    {
      "typeUrl": "string",
      "value": "string"
    }
  ],
  "message": "string"
}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

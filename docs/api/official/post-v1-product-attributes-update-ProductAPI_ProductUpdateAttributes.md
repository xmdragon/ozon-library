# 更新商品特征

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/product/attributes/update`
- Operation ID：`ProductAPI_ProductUpdateAttributes`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/ProductAPI_ProductUpdateAttributes
- 分组：`product`

## 页面标题结构

- 更新商品特征
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
| `items` | Array of objects <= 100 items 需要更新的商品和特征。 |

### 表格 2

| 字段 | 类型/说明 |
| --- | --- |
| `task_id` | integer <int64> 商品更新任务号码。 为检查更新状态，请将接收到的值传至方法 /v1/product/import/info。 |

## 示例

### 示例 0

```text
429
```

### 示例 1

```text
message
```

### 示例 2

```text
Item-Retry-After
```

### 示例 3

```text
Item-Rate-Limit-Remaining
```

### 示例 4

```json
{"items": [{"offer_id": "PROD-2023-001","attributes": [{"complex_id": 1,"id": 1,"values": [{"dictionary_value_id": 1001,"value": "蓝色"}]},{"complex_id": 2,"id": 2,"values": [{"dictionary_value_id": 2001,"value": "42"}]},{"complex_id": 3,"id": 3,"values": [{"dictionary_value_id": 3001,"value": "棉"},{"dictionary_value_id": 3002,"value": "聚酯纤维"}]}]}]}
```

### 示例 5

```json
{"task_id": 0}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

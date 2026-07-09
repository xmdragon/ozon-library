# 获取按数量折扣信息

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/product/stairway-discount/by-quantity/get`
- Operation ID：`ProductAPI_GetProductStairwayDiscountByQuantity`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/ProductAPI_GetProductStairwayDiscountByQuantity
- 分组：`product`

## 页面标题结构

- 获取按数量折扣信息
- header Parameters
- Request Body schema: application/json
- 回复
- Response Schema: application/json
- 请求范例
- 回复范例

## 参数与返回结构

### 表格 0

Client-Id required string 用户识别号。 Api-Key required string API-密钥。

### 表格 1

skus required Array of strings <int64> <= 5000 items 需要返回内容评级的商品SKU列表。

### 表格 2

stairwaysArray of objects 单个商品的按数量折扣信息。 Array ()enabledboolean true，表示数量折扣已启用。 skuinteger <int64> Ozon系统中的商品标识符——SKU。 stairwayobject 按数量折扣等级信息。 statusstring Enum: "IN_PROCESS" "ERROR" "SUCCESS" 按数量折扣变更状态。可能的取值： ERROR——修改折扣时出错。请再次调用方法 /v1/product/stairway-discount/by-quantity/set。 IN_PROCESS——修正正在处理中。 SUCCESS——折扣修改已成功应用到商品。

### 表格 3

enabledboolean true，表示数量折扣已启用。 skuinteger <int64> Ozon系统中的商品标识符——SKU。 stairwayobject 按数量折扣等级信息。 statusstring Enum: "IN_PROCESS" "ERROR" "SUCCESS" 按数量折扣变更状态。可能的取值： ERROR——修改折扣时出错。请再次调用方法 /v1/product/stairway-discount/by-quantity/set。 IN_PROCESS——修正正在处理中。 SUCCESS——折扣修改已成功应用到商品。

## 示例

### 示例 0

```text
ERROR
```

### 示例 1

```text
IN_PROCESS
```

### 示例 2

```text
SUCCESS
```

### 示例 3

```json
{"skus": ["string"]}
```

### 示例 4

```json
{"stairways": [{"enabled": true,"sku": 0,"stairway": {"steps": [{"discount": 0,"quantity": 0,"step": 0}]},"status": "IN_PROCESS"}]}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

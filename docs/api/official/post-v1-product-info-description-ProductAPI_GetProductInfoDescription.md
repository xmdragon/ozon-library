# 获取商品详细信息

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v1/product/info/description`
- Operation ID：`ProductAPI_GetProductInfoDescription`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/ProductAPI_GetProductInfoDescription
- 分组：`product`

## 页面标题结构

- 获取商品详细信息
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

offer_id required string 卖家系统中的商品识别码是卖家系统中的商品标识符是商品货号。 product_idinteger <int64> Ozon系统中商品的标识符 — product_id。

### 表格 2

resultobject descriptionstring 描述。 idinteger <int64> 识别码。 namestring 名称。 offer_idstring 卖家系统中的商品识别码是卖家系统中的商品标识符是商品货号。

### 表格 3

descriptionstring 描述。 idinteger <int64> 识别码。 namestring 名称。 offer_idstring 卖家系统中的商品识别码是卖家系统中的商品标识符是商品货号。

## 示例

### 示例 0

```json
{"offer_id": "5","product_id": 73453843}
```

### 示例 1

```json
{"result": {"id": 73453843,"offer_id": "5","name": "狗狗训练课程 \"三周内拥有乖顺的狗\"","description": "快速课程为全课程的缩减版 \"狗： 训练教程\", 给予最基础的知识、技能、能力。这是迈出训狗教学第一步的最佳选择！<br/><br/>快速课程带来什么:<ul><li>与狗狗交流 </li></ul>快速课程将要结束之时，您将获得在任何时候都伴您左右的温顺小狗陪伴者。<ul><li>安全信心</li></ul>理想狗狗: 再也不会挣脱狗绳、追赶猫猫、吃街上的食物等。<ul><li>Комфортная жизнь</li></ul>更高水平的沟通、对动物行为没有愤怒、喊叫、不满。"}}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

# 清单数目

> 此文件由 `tools/generate_official_api_docs.py` 从 Chrome 抽取索引生成。不要在这里写入真实账号、密钥、cookie 或 token。

## 方法

- 请求：`POST /v3/finance/transaction/totals`
- Operation ID：`FinanceAPI_FinanceTransactionTotalV3`
- 官方锚点：https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/FinanceAPI_FinanceTransactionTotalV3
- 分组：`finance`

## 页面标题结构

- 清单数目
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

dateobject 按日期过滤。 posting_number required string 发货号。 transaction_typestring 操作类型： all — 所有, orders — 订单, returns — 退货和取消, services — 服务费, compensation — 补贴, transferDelivery — 快递费用, other — 其他。

### 表格 2

resultobject 询问结果。 accruals_for_salenumber <double> 指定期间内商品的总成本和退货。 compensation_amountnumber <double> 补贴。 money_transfernumber <double> 根据“卖方选择交货”计划工作时的交货和退货费用。 others_amountnumber <double> 其他应计费用。 processing_and_deliverynumber <double> 运输处理、订单装配、干线、最后一英里以及自2021年2月1日起引入新的佣金和费率前的快递服务费。 干线 —— 集群之间的货物交付。 最后一英里 —— 从订单交付点、自提点和快递员到买家处的快递。 refunds_and_cancellationsnumber <double> 干线返回、退货处理、取消和非赎回、2021年2月1日起引入新佣金和税率之前退货价格。 干线 —— 集群之间的货物交付。 最后一英里 —— 从订单交付点、自提点和快递员到买家处的快递。 sale_commissionnumber <double> 商品预售时预扣的佣金数额，退货时返还的佣金数。 services_amountnumber <double> 与商品交付和退货没有直接关系的附加服务成本。例如，促销或商品放置。

### 表格 3

accruals_for_salenumber <double> 指定期间内商品的总成本和退货。 compensation_amountnumber <double> 补贴。 money_transfernumber <double> 根据“卖方选择交货”计划工作时的交货和退货费用。 others_amountnumber <double> 其他应计费用。 processing_and_deliverynumber <double> 运输处理、订单装配、干线、最后一英里以及自2021年2月1日起引入新的佣金和费率前的快递服务费。 干线 —— 集群之间的货物交付。 最后一英里 —— 从订单交付点、自提点和快递员到买家处的快递。 refunds_and_cancellationsnumber <double> 干线返回、退货处理、取消和非赎回、2021年2月1日起引入新佣金和税率之前退货价格。 干线 —— 集群之间的货物交付。 最后一英里 —— 从订单交付点、自提点和快递员到买家处的快递。 sale_commissionnumber <double> 商品预售时预扣的佣金数额，退货时返还的佣金数。 services_amountnumber <double> 与商品交付和退货没有直接关系的附加服务成本。例如，促销或商品放置。

## 示例

### 示例 0

```json
{"date": {"from": "2021-11-01T00:00:00.000Z","to": "2021-11-02T00:00:00.000Z"},"posting_number": "","transaction_type": "all"}
```

### 示例 1

```json
{"result": {"accruals_for_sale": 96647.58,"sale_commission": -11456.65,"processing_and_delivery": -24405.68,"refunds_and_cancellations": -330,"services_amount": -1307.57,"compensation_amount": 0,"money_transfer": 0,"others_amount": 113.05}}
```

## 使用提醒

- Seller API 通常需要 `Client-Id` 和 `Api-Key` header。
- 官方文档提示 Seller API 仅支持后端到后端调用，浏览器直接调用可能被 CORS 拒绝。
- 本页保留官方 DOM 抽取文本；字段含义不清时先回到官方锚点和原始 JSON 索引核对。

# Ozon 财务应计类型目录

## 结论

Ozon 财务至少存在两套不同的类型 ID：

1. Seller API `type_id`：来自 `POST /v1/finance/accrual/types`，并出现在 `by-day`、`postings` 响应中。
2. Seller 页面内部 `accrual_type_ids`：来自 `seller.ozon.ru/api/site/self-gateway/api/accruals/types`，用于页面明细和汇总筛选。

两套 ID 不是同一个枚举，不能直接互换。例如：

| 费用 | Seller API `type_id` | Seller 页面内部 ID |
| --- | ---: | ---: |
| 销售佣金 / Ozon代理佣金 | 69 | 14 |
| 国际物流代理服务费 / 组织国际运输合同的订立服务 | 66 | 177 |
| 物流服务费重新计费 / 国际配送服务 | 67 | 106 |

机器可读的完整已知目录见 [`indexes/finance-accrual-types.json`](../../indexes/finance-accrual-types.json)。

## 已验证的 Seller API 类型

| `type_id` | API `name` | 费用语义 | ZhiPin 费用键 | 订单投影字段 | 状态 |
| ---: | --- | --- | --- | --- | --- |
| 1 | `Acquiring` | 收单/支付手续费 | `支付手续费（收单费）` | `first_mile_fee_cny` | 已验证；两段 order 级费用需按 posting 金额分摊 |
| 3 | `BrandCommission` | 品牌推广佣金 | `Продвижение бренда` | — | 仅保存交易流水 |
| 10 | 尚未从 types API 取得 | 部分补偿买家 | `部分补偿买家` | `compensation_cny` | 已通过同 posting 的旧 v3 operation 交叉确认语义 |
| 29 | `LastMileCourier` | 末端配送至取货点 | 未标准化 key | — | 生产库已出现，需决定投影政策 |
| 30 | 尚未从 types API 取得 | 物流平台聚合的末端配送重计费 | `物流平台聚合末端配送费` | `last_mile_delivery_fee_cny` | 2026-09-01 业务确认并入尾程 |
| 32 | `Logistic` | 物流费用 | 未标准化 key | — | 生产库已出现，需决定物流字段边界 |
| 41 | `PayPerClick` | 按点击付费推广 | `Оплата за клик` | — | 仅保存交易流水 |
| 51 | `PremiumMembership` | Premium Pro 比例费用 | `Подписка Premium Pro (процент)` | — | 仅保存交易流水 |
| 54 | `Promotion` | 商品推广 | `Продвижение товара` | — | 仅保存交易流水 |
| 66 | `RfbsGlobalAgentFee` | realFBS 国际运输代理费 | `国际物流代理服务费` | `last_mile_delivery_fee_cny` | ZhiPin 当前行为已验证 |
| 67 | `RfbsGlobalDelivery` | realFBS 国际配送重计费 | `物流服务费重新计费` | `international_logistics_fee_cny` | 已验证 |
| 69 | `SaleCommission` | 销售佣金及冲销 | `销售佣金` | `ozon_commission_cny` | 已验证；按 posting 汇总净额 |
| 74 | `StarsMembership` | 星星商品服务费 | `Звёздные товары` | — | 仅保存交易流水 |
| 93 | `DefectFineErrors` | 错误指数超标罚款 | 未标准化 key | — | 生产库已出现，需决定是否并入错误费 |

## 生产数据库枚举现状

2026-09-01 对生产 `ozon_finance_transactions` 的只读快照显示：

- 117,332 条流水；
- 30 种 `operation_type`、30 种 `operation_type_name`；
- 31 种 `fees_json` key；
- 表中没有 `type_id` 列；
- 数据库中没有 accrual/finance type reference 表。

因此生产库当前不是完整财务类型目录。它只保存规范化后的字符串；除 key 中显式保留 `accrual:<id>` 的未知类型外，无法仅凭数据库反推出数字 ID。

线上已经出现但旧映射未覆盖的明确例子：

| API `type_id` | `name` | 生产 fee key | 当前处理 |
| ---: | --- | --- | --- |
| 29 | `LastMileCourier` | `LastMileCourier/Доставка до места выдачи/accrual:29` | 未投影 |
| 32 | `Logistic` | `Logistic/Логистика/accrual:32` | 未投影 |
| 93 | `DefectFineErrors` | `DefectFineErrors/Превышение индекса ошибок/accrual:93` | 未投影 |

所有 31 个实际 fee key 已保存在机器索引的 `observed_database_fee_keys`，但该数组是观察快照，不替代 `/v1/finance/accrual/types` 的动态参考信息。

长期建议是在交易行保存 `accrual_type_id`，或建立带 `observed_at` 的类型快照表；否则 Ozon 修改名称后，历史字符串不能稳定关联原始类型。

## 10 和 30 的证据边界

`/v1/finance/accrual/types` 在 2026-09-01 的运行探针中持续返回 `429 Retry-After: 60`，因此没有把英文 `name` 猜写进目录。

- `type_id=10`：同一 posting、同一日期、同一金额在旧 `POST /v3/finance/transaction/list` 中对应 `OperationMarketplaceServicePartialCompensationToClient`，俄文名称为 `Частичная компенсация покупателю`（部分补偿买家）。
- `type_id=30`：同一 posting、同一日期、同一金额在旧 v3 `services[]` 中对应 `MarketplaceServiceItemRedistributionLastMilePVZ`。2026-09-01 已明确业务政策：与 `type_id=66` 先按 signed RUB 求净额，再统一写入 `last_mile_delivery_fee_cny`。

Seller 页面筛选中存在“与物流平台聚合的服务费”候选标签，但当前证据不足以把它的页面内部 ID 与 Seller API `type_id=30` 写成已验证映射，因此只在机器索引的 `seller_ui_label_candidate_zh` 中保留线索。页面 ID 未确认不影响已确认的订单投影政策。

没有确认英文名不妨碍保存原始交易：未知类型仍应以包含 `type_id` 的稳定 key 入库；但在没有政策前不能静默投影到某个订单金额字段。

## 聚合与订单投影规则

### Posting 级费用

`POST /v1/finance/accrual/postings` 的稳定业务键为：

```text
(posting_number, UTC accrual_date, type_id, sku)
```

同键金额先按符号相加，再投影到订单。退款或冲销可能产生正数，不能逐行取绝对值后相加；应先求净额，再按目标字段的费用展示规则取绝对值。

### Order 级收单费

`Acquiring` 可能只出现在两段 order 编号上，而订单表使用三段 posting 编号。分摊规则为：

```text
posting_first_mile = order_acquiring
                     × posting_order_total_price
                     ÷ same_order_all_postings_total_price
```

因此只调用 `accrual/postings` 不构成完整财务同步；还要按应计日期读取 `accrual/by-day`，补齐 parent order 记录。

### 当前 ZhiPin 字段边界

| 订单字段 | 来源费用 |
| --- | --- |
| `ozon_commission_cny` | `SaleCommission` / `销售佣金` |
| `last_mile_delivery_fee_cny` | 当前为 `RfbsGlobalAgentFee` / `国际物流代理服务费` |
| `international_logistics_fee_cny` | `RfbsGlobalDelivery` / `物流服务费重新计费` |
| `first_mile_fee_cny` | 两段 order 级 `Acquiring` 分摊 |
| `compensation_cny` | `Compensation`、`ItemCompensation`；运行证据显示 `type_id=10` 为部分补偿 |
| `refund_cny` | `ClientReturn`、`Cancellation`、`PartialReturn` |
| `error_fee_cny` | `DefectRate` |

`ClientReturn` 等英文名的数字 ID 尚未全部取得，目录在 `unresolved_seller_api_names` 中显式保留，不能用历史猜测填充。

## 如何查询

按 Seller API ID：

```bash
jq '.entries[] | select(.seller_api_type_id == 69)' indexes/finance-accrual-types.json
```

查所有会写入订单字段的类型：

```bash
jq '.entries[] | select(.projection_field != null)' indexes/finance-accrual-types.json
```

查仍需政策或名称确认的类型：

```bash
jq '.entries[] | select(.seller_api_name == null or .projection_status == "needs_policy")' \
  indexes/finance-accrual-types.json
```

## 来源引用

- `GetFinanceAccrualTypes`：`POST /v1/finance/accrual/types`
- `GetFinanceAccrualPostings`：`POST /v1/finance/accrual/postings`
- `GetFinanceAccrualByDay`：`POST /v1/finance/accrual/by-day`
- `indexes/finance-accrual-types.json`
- `/Users/eric/works/ZhiPin/plugins/ef/channels/ozon/services/finance_transactions_sync_service.py`
- `/Users/eric/works/ZhiPin/plugins/ef/channels/ozon/services/finance_translations.py`
- `/Users/eric/works/ZhiPin/plugins/ef/channels/ozon/services/ozon_finance_sync_service.py`
- Seller 页面只读观察（2026-09-01）：`https://seller.ozon.ru/app/finances/accruals`
- Seller 财务微前端只读观察（2026-09-01）：`finances.66fb3611.js`

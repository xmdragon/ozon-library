# Seller API 同步策略

## 用途

记录订单、商品和财务数据在事件、定向 API、周期校验和本地投影之间的职责边界。目标是在不把事件当作唯一真相的前提下减少重复请求与大响应。

## 证据边界

本文把 `origin/master` revision `6e19f3aedb3d732cad0f4b98191435d57b4ffa56` 的只读源码事实与推荐架构分开。`indexes/` 仍是 2026-07-09 的 revision `75b2e572df48eaa9d986d8b28d8b5abd927332a5` 快照；本次只读复核不等于全量重扫，也不把未合并分支的目标当作当前实现。

## 已确认当前实现

### 订单

- `plugins/ef/channels/ozon/api/client_mixins/orders.py` 仍调用已于 2026-06-01 停用的 `/v3/posting/fbs/list`，分页状态是 `offset`；其增量参数把 `last_changed_status_date` 放在请求体顶层，而官方 `PostingAPI_GetFbsPostingListV3` / `PostingFbsList` 示例要求它位于 `filter`。
- `OrderFetcher` 默认按 3 小时窗口读取并以 offset 翻页。虽然模型中有 `OzonSyncCheckpoint`，相关订单同步入口在该 revision 没有读写持久 checkpoint；不能把 checkpoint 语义写成已上线。

### 商品

- `ProductFetcher` 的当前工程批次分别是列表 100、详情 100、价格 1000、FBS 仓库库存 500、属性 100；它们不是官方统一批量上限。
- webhook ingress 会保存 `OzonWebhookEvent`，但商品创建/更新 handler 以 `spawn` 启动定向读取，异常被记录后结束；本地不存在的商品在 `_update_product_from_api` 中跳过。因此当前实现不能证明 durable product webhook upsert 已完成。

### 财务

- `FinanceTransactionsSyncService` 及历史同步任务仍通过 `FinanceAPI_FinanceTransactionListV3` 调用 `/v3/finance/transaction/list`，分页 `page_size` 为 1000；官方 News `section/202656` 说明该接口已于 2026-07-06 停用。
- `OzonFinanceSyncService` 在本地交易缺失时仍自行扫描同一个 v3 接口，说明 `6e19f3a` 还不是单一 finance producer；现有水位/任务状态不能替代共享 producer 的已验证语义。

## 推荐模式

### 订单

- 新入口使用 `PostingFbsList` 对应的 `/v4/posting/fbs/list + cursor`；`last_changed_status_date` 严格嵌套在 `filter`，并按需关闭 `with` 扩展字段。
- 以持久 checkpoint 记录窗口边界，只在所有页面、数据库提交和必要投影成功后推进；首次运行与增量运行显式区分。

### 商品

- 轻量商品列表只维护成员和稳定键；详情、价格、库存、属性由 webhook 定向任务和低频完整校验分别承担。
- durable webhook 任务按同店 `product_id` 优先、`offer_id` 次之幂等 upsert，并将远端/数据库错误保留为可重试失败。
- rich 请求统一 500 是推荐的工程内存边界，不是官方统一上限，也不是 `6e19f3a` 已实现值。

### 财务

- `/v3/finance/transaction/list` 仅保留为历史兼容读取；推荐迁移由 `GetFinanceAccrualPostings`（`/v1/finance/accrual/postings`）、`GetFinanceAccrualTypes`（`/v1/finance/accrual/types`）和 `GetFinanceAccrualByDay`（`/v1/finance/accrual/by-day`）组成。
- 迁移前必须独立验证三接口的 posting 聚合、类型映射、日边界、退款/赔偿和金额币种语义；不能把 v3 写成当前推荐 producer。
- 远端财务读取由一个 producer 按 operation/accrual 粒度写入本地原始表，费用、退款、赔偿和利润只从本地 projector 读取。

## 待运行观测参数

- 订单：观测 v4 cursor 连续性、`received_count`、`updated_count`、`skipped_count`、webhook 命中率、分页失败率和响应字节数，再确定重叠窗口与调度周期。
- 商品：逐 endpoint 记录请求上限、批次内存、429 命中、事件定向成功率和列表校验发现数，再决定是否采用 500 与 rich 校验频率。
- 财务：用脱敏 fixture 或受控 Seller API 样本对三条 accrual 接口与现有 v3 结果做独立对账；验证通过前不切换 producer，也不假定三接口自动等价。
- 所有实体都应记录任务开始/结束、失败页、原始响应字节数和本地写入计数；未完成的页面或提交失败不得推进水位。

## 来源引用

- 官方 operation：`PostingFbsList`（推荐 v4）、`PostingAPI_GetFbsPostingListV3`（停用 v3）、`ProductAPI_GetProductList`、`ProductAPI_GetProductInfoList`、`FinanceAPI_FinanceTransactionListV3`（停用 v3）、`GetFinanceAccrualPostings`、`GetFinanceAccrualTypes`、`GetFinanceAccrualByDay`
- 官方 News：`https://docs.ozon.ru/api/seller/zh/#section/2026430`、`https://docs.ozon.ru/api/seller/zh/#section/202656`
- 本地官方逐方法页：`docs/api/official/post-v3-posting-fbs-list-PostingAPI_GetFbsPostingListV3.md`、`docs/api/official/post-v4-posting-fbs-list-PostingFbsList.md`、`docs/api/official/post-v3-finance-transaction-list-FinanceAPI_FinanceTransactionListV3.md`、`docs/api/official/post-v1-finance-accrual-postings-GetFinanceAccrualPostings.md`、`docs/api/official/post-v1-finance-accrual-types-GetFinanceAccrualTypes.md`、`docs/api/official/post-v1-finance-accrual-by-day-GetFinanceAccrualByDay.md`
- News 汇总：`docs/api/seller-api-news.md`
- `/Users/eric/works/ZhiPin/plugins/ef/channels/ozon/api/client_mixins/orders.py`
- `/Users/eric/works/ZhiPin/plugins/ef/channels/ozon/services/sync/order_sync/order_fetcher.py`
- `/Users/eric/works/ZhiPin/plugins/ef/channels/ozon/services/sync/product_sync/product_fetcher.py`
- `/Users/eric/works/ZhiPin/plugins/ef/channels/ozon/services/finance_transactions_sync_service.py`
- `/Users/eric/works/ZhiPin/plugins/ef/channels/ozon/services/ozon_finance_sync_service.py`
- `/Users/eric/works/ZhiPin/plugins/ef/channels/ozon/api/client_mixins/finance.py`
- `/Users/eric/works/ZhiPin/plugins/ef/channels/ozon/arq_tasks/finance_tasks.py`
- `/Users/eric/works/ZhiPin/plugins/ef/channels/ozon/arq_tasks/finance_history_sync.py`
- `/Users/eric/works/ZhiPin/plugins/ef/channels/ozon/webhooks/handler.py`
- `indexes/official-seller-api.operations.json`
- `indexes/source-files.json`
- `indexes/endpoint-cross-reference.json`

# Seller API 同步策略

## 用途

记录订单、商品和财务数据在事件、定向 API、周期校验和本地投影之间的职责边界。目标是在不把事件当作唯一真相的前提下减少重复请求与大响应。

## 核心原则

1. 实时变化由 webhook 触发定向同步。
2. 周期任务只校验事件可能遗漏的范围，不重复执行完整实时链路。
3. 持久化进度只在所有分页和数据库提交成功后推进。
4. 请求使用最小响应字段；rich 数据按稳定标识符定向获取。
5. API ingestion 与本地 projection 单向连接，同一实体只有一个远端数据生产者。

## 实体策略矩阵

| 实体 | 稳定键 | 实时变化来源 | 补偿读取 | 推荐重叠 | 本地消费 |
| --- | --- | --- | --- | --- | --- |
| FBS posting | `(shop_id, posting_number)` | 新货件、取消、状态变化 webhook | `filter.last_changed_status_date` 列表 | 从上次完整成功时间向前固定短窗口 | 状态、物流、商品快照、操作状态 |
| Product | Ozon `product_id` | 创建/更新、库存变化 webhook | 轻量商品清单加低频 rich 校验 | rich 批次最多 500 | 商品主表、图片、尺寸、属性、价格、库存 |
| Finance operation | `(shop_id, operation_id)` | 无可靠实时事件 | 按 operation date 和持久水位读取 | 重放一个完整自然日 | transaction 表先入库，费用/利润随后投影 |

## 订单

- v3 货件列表的变化时间必须位于 `filter.last_changed_status_date`。
- `filter.since/to` 可以覆盖较长的订单创建范围；只要变化时间条件有效，返回值仍限于目标变化窗口。
- 周期任务使用持久 checkpoint。无 checkpoint 是明确 bootstrap 流程；已有 checkpoint 是 incremental 流程。
- webhook 负责低延迟，周期任务负责最终一致。调整周期前先观测 webhook 命中率、列表收到量、实际更新量和未变化跳过量。
- 当前资料只能支持“先修正请求契约再降频”的顺序；具体周期属于部署参数，需要运行数据验证。

## 商品

- 商品列表与 rich 数据拆开。列表确认成员和稳定标识；详情、价格、库存、属性根据事件或校验计划读取。
- 定向事件处理必须等待本地 upsert 结果。商品不存在是创建路径，不是成功跳过路径。
- 批次 500 是 ZhiPin 的工程内存边界建议；官方各 endpoint 上限仍以对应 operation 文档为准。
- 降低 rich 全量频率之前，先证明定向任务可重试，并保留低频完整校验来发现事件缺口。

## 财务

- transaction list 只有一个服务负责调用并按 operation 粒度持久化。
- 费用、退款、赔偿和利润计算只读取本地 transaction 表。缺历史 operation 时通过明确的历史同步入口补录，再运行投影。
- 水位读取区间应包含一个完整自然日重叠；唯一键消除重复，内容变化才更新已有 operation。
- API 页失败或数据库提交失败都不能推进水位。下一轮从旧水位恢复并覆盖失败区间。

## 观测指标

- `api_calls`：按 endpoint、shop、task 统计请求次数。
- `response_bytes`：原始响应字节数，不记录私有响应正文。
- `received_count`、`inserted_count`、`updated_count`、`skipped_count`。
- `overlap_ratio = skipped_count / received_count`。
- checkpoint 的开始、结束、状态和失败页。
- webhook 定向同步成功率，以及周期校验发现但事件未落库的实体数。

## 来源引用

- 官方 operation：`PostingAPI_GetFbsPostingListV3`、`PostingFbsList`、`ProductAPI_GetProductList`、`ProductAPI_GetProductInfoList`、`FinanceAPI_FinanceTransactionListV3`
- `/Users/eric/works/ZhiPin/plugins/ef/channels/ozon/api/client_mixins/orders.py`
- `/Users/eric/works/ZhiPin/plugins/ef/channels/ozon/services/sync/order_sync/order_fetcher.py`
- `/Users/eric/works/ZhiPin/plugins/ef/channels/ozon/services/sync/product_sync/product_fetcher.py`
- `/Users/eric/works/ZhiPin/plugins/ef/channels/ozon/services/finance_transactions_sync_service.py`
- `/Users/eric/works/ZhiPin/plugins/ef/channels/ozon/services/ozon_finance_sync_service.py`
- `/Users/eric/works/ZhiPin/plugins/ef/channels/ozon/webhooks/handler.py`
- `indexes/official-seller-api.operations.json`
- `indexes/source-files.json`
- `indexes/endpoint-cross-reference.json`

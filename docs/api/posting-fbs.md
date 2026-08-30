# FBS/rFBS 货件 API

## 用途

记录 FBS/rFBS 货件列表、详情、发货、取消和标签相关 API。

## AI 摘要

官方推荐货件列表接口为 `POST /v4/posting/fbs/list`；News `section/2026430` 说明 `POST /v3/posting/fbs/list` 已于 2026-06-01 停用，只能作为历史兼容路径追溯。详情接口常用 `/v3/posting/fbs/get`，发货使用 `/v4/posting/fbs/ship`，标签使用 `/v2/posting/fbs/package-label`。请求通常需要 `Client-Id`、`Api-Key`，v4 列表接口使用 `filter`、`limit`、`cursor` 和按需开启的 `with` 字段。

## 关键接口

| 接口 | operation | 用途 | 关键字段 |
| --- | --- | --- | --- |
| `POST /v4/posting/fbs/list` | `PostingFbsList` | 获取货件列表 | `filter`、`limit`、`cursor`、`with` |
| `POST /v3/posting/fbs/list` | `PostingAPI_GetFbsPostingListV3` | 2026-06-01 停用的历史兼容路径 | 仅追溯项目兼容实现 |
| `POST /v3/posting/fbs/get` | `PostingAPI_GetFbsPostingV3` | 按 `posting_number` 获取详情 | `posting_number`、`with` |
| `POST /v4/posting/fbs/ship` | `PostingAPI_ShipFbsPostingV4` | 组包/发货 | `posting_number`、`packages` |
| `POST /v2/posting/fbs/cancel` | `PostingAPI_CancelFbsPosting` | 取消货件 | 取消原因 |
| `POST /v2/posting/fbs/package-label` | `PostingAPI_PostingFBSPackageLabel` | 下载标签 | 可能返回二进制/PDF |

## 已确认当前实现

- 官方逐方法请求示例 `PostingAPI_GetFbsPostingListV3` 与 `PostingFbsList` 都把 `last_changed_status_date` 放在 `filter` 对象内。这一嵌套位置是官方请求契约；放在请求体顶层不会形成有效的增量筛选。
- ZhiPin `origin/master` revision `6e19f3aedb3d732cad0f4b98191435d57b4ffa56` 的 `plugins/ef/channels/ozon/api/client_mixins/orders.py` 仍调用 `POST /v3/posting/fbs/list`，使用 `offset`，并把 `last_changed_status_date` 写在顶层；相关同步 fetcher 默认以 3 小时窗口和 offset 翻页。该 revision 没有锁定字段嵌套位置的请求契约测试。
- 官方 News `section/2026430` 的原文是“已弃用，并将于 2026 年 6 月 1 日停用”，因此 v3 只能标为停用后的历史兼容路径。当前推荐 producer 是 `POST /v4/posting/fbs/list`，Operation ID 为 `PostingFbsList`。

## 推荐模式

- 新的同步入口使用 `POST /v4/posting/fbs/list`，按返回的 `cursor` 继续请求直到 `has_next=false`；不要把 v3 的 `offset` 状态迁移成 v4 的游标。
- 将 `last_changed_status_date` 嵌套在 `filter` 内是官方契约，也是当前推荐修复；`filter.since/to` 仍表达订单创建时间，不能与状态最后变化时间混用。
- `with.financial_data`、`with.analytics_data`、`with.barcodes` 等扩展字段按消费者逐项开启。列表同步不需要的字段保持关闭，详情调用再按 posting 定向读取。
- 使用持久 checkpoint 记录一轮同步的边界，只在所有页面处理和数据库提交成功后推进；这属于推荐架构，不能写成 `6e19f3a` 已实现事实。

## 待运行观测参数

- v4 的 `limit`、cursor 失效、空页和重试行为需要在可用 Seller API 环境观测；官方逐方法页给出的 v4 `limit` 范围为 1–100。
- 通过 `received_count`、`updated_count`、`skipped_count`、页数、响应字节数和 API 错误记录，估计固定重叠窗口和同步周期；具体数值不是当前资料已验证的结论。
- 在真实运行前分别验证 webhook 命中率与列表补偿量。分页失败时不得将已取页面当作完整成功，下一轮应从上一次完整成功边界重放明确的重叠窗口。

## 流程

1. 推荐入口按时间、状态、仓库等 `filter` 调用 v4 列表。
2. 用返回的 `cursor` 翻页，直到 `has_next=false`。
3. 对需要操作的货件调用 `/v3/posting/fbs/get` 获取详情和可用动作。
4. 发货前按官方 schema 准备 packages。
5. 标签接口可能返回非 JSON，需要后端特殊处理二进制响应。

## 异常与恢复

| 情况 | 处理 |
| --- | --- |
| v3 列表已停用 | News `section/2026430` 指定 2026-06-01 停用；新调用使用 `/v4/posting/fbs/list`，旧调用只作为历史兼容记录。 |
| 标签接口返回二进制 | 不按 JSON 解析；记录 content-type 和大小。 |
| 状态不正确 | Ozon 可能返回业务错误，如状态不可发货或已发货。 |
| 列表时间跨度过大 | 官方要求列表时间段不超过一年。 |
| 增量结果仍固定翻很多页 | 先检查官方契约要求的 `filter.last_changed_status_date`，再记录每轮收到、更新、跳过数量。 |
| 分页中途失败 | 不把已获取的前几页标记为完整成功；下一轮从上次完整成功时间减去已观测的重叠窗口重新拉取。 |

## 来源引用

- 官方 operation：`PostingFbsList`（v4 推荐列表）、`PostingAPI_GetFbsPostingListV3`（v3 历史兼容列表）、`PostingAPI_GetFbsPostingV3`、`PostingAPI_ShipFbsPostingV4`
- 官方 News：`https://docs.ozon.ru/api/seller/zh/#section/2026430`（v3 于 2026-06-01 停用）
- 本地官方逐方法页：`docs/api/official/post-v4-posting-fbs-list-PostingFbsList.md`、`docs/api/official/post-v3-posting-fbs-list-PostingAPI_GetFbsPostingListV3.md`
- `/Users/eric/works/ZhiPin/plugins/ef/channels/ozon/api/client_mixins/orders.py`
- `indexes/official-seller-api.operations.json`

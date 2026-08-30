# FBS/rFBS 货件 API

## 用途

记录 FBS/rFBS 货件列表、详情、发货、取消和标签相关 API。

## AI 摘要

官方新货件列表接口为 `POST /v4/posting/fbs/list`，旧 `POST /v3/posting/fbs/list` 在项目中仍有使用。详情接口常用 `/v3/posting/fbs/get`，发货使用 `/v4/posting/fbs/ship`，标签使用 `/v2/posting/fbs/package-label`。请求通常需要 `Client-Id`、`Api-Key`，列表接口支持 `filter`、`limit`、`cursor` 和 `with` 扩展字段。

## 关键接口

| 接口 | operation | 用途 | 关键字段 |
| --- | --- | --- | --- |
| `POST /v4/posting/fbs/list` | `PostingFbsList` | 获取货件列表 | `filter`、`limit`、`cursor`、`with` |
| `POST /v3/posting/fbs/list` | `PostingAPI_GetFbsPostingListV3` | 旧列表接口 | 项目兼容使用 |
| `POST /v3/posting/fbs/get` | `PostingAPI_GetFbsPostingV3` | 按 `posting_number` 获取详情 | `posting_number`、`with` |
| `POST /v4/posting/fbs/ship` | `PostingAPI_ShipFbsPostingV4` | 组包/发货 | `posting_number`、`packages` |
| `POST /v2/posting/fbs/cancel` | `PostingAPI_CancelFbsPosting` | 取消货件 | 取消原因 |
| `POST /v2/posting/fbs/package-label` | `PostingAPI_PostingFBSPackageLabel` | 下载标签 | 可能返回二进制/PDF |

## 流程

1. 按时间、状态、仓库等 filter 拉取货件列表。
2. 用 `cursor` 翻页，直到 `has_next=false`。
3. 对需要操作的货件调用 `/v3/posting/fbs/get` 获取详情和可用动作。
4. 发货前按官方 schema 准备 packages。
5. 标签接口可能返回非 JSON，需要后端特殊处理二进制响应。

## 增量同步与最小响应

- `/v3/posting/fbs/list` 的 `last_changed_status_date` 属于 `filter`；放在请求体顶层不会形成有效的增量筛选。项目 client 应用请求体契约测试锁定嵌套位置。
- `filter.since/to` 约束订单创建时间，`filter.last_changed_status_date` 约束状态最后变化时间。捕获旧订单的新状态时，两组时间的职责不能互换。
- `with.financial_data`、`with.analytics_data`、`with.barcodes` 等扩展字段按消费者需要逐项开启。列表同步不消费的扩展字段应保持关闭，详情操作再按 posting 定向获取。
- `/v3` 使用 `offset`；`/v4` 使用 `cursor`。迁移到 `/v4` 时必须以返回 cursor 推进，不能把旧 offset 状态直接复用。
- 任一分页失败都应让本轮同步失败；持久化进度只能在所有页面处理并提交成功后推进。

## 异常与恢复

| 情况 | 处理 |
| --- | --- |
| 旧接口 deprecated | 新文档优先记录 `/v4/posting/fbs/list`，项目兼容保留 `/v3`。 |
| 标签接口返回二进制 | 不按 JSON 解析；记录 content-type 和大小。 |
| 状态不正确 | Ozon 可能返回业务错误，如状态不可发货或已发货。 |
| 列表时间跨度过大 | 官方要求列表时间段不超过一年。 |
| 增量结果仍固定翻很多页 | 检查 `last_changed_status_date` 是否位于 `filter`，并记录每轮收到、更新、跳过数量。 |
| 分页中途失败 | 不把已获取的前几页标记为完整成功；下一轮从上次完整成功时间减去明确重叠窗口重新拉取。 |

## 来源引用

- 官方 operation：`PostingFbsList`、`PostingAPI_GetFbsPostingV3`、`PostingAPI_ShipFbsPostingV4`
- `/Users/eric/works/ZhiPin/plugins/ef/channels/ozon/api/client_mixins/orders.py`
- `indexes/official-seller-api.operations.json`

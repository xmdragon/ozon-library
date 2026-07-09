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

## 异常与恢复

| 情况 | 处理 |
| --- | --- |
| 旧接口 deprecated | 新文档优先记录 `/v4/posting/fbs/list`，项目兼容保留 `/v3`。 |
| 标签接口返回二进制 | 不按 JSON 解析；记录 content-type 和大小。 |
| 状态不正确 | Ozon 可能返回业务错误，如状态不可发货或已发货。 |
| 列表时间跨度过大 | 官方要求列表时间段不超过一年。 |

## 来源引用

- 官方 operation：`PostingFbsList`、`PostingAPI_GetFbsPostingV3`、`PostingAPI_ShipFbsPostingV4`
- `/Users/eric/works/ZhiPin/plugins/ef/channels/ozon/api/client_mixins/orders.py`
- `indexes/official-seller-api.operations.json`

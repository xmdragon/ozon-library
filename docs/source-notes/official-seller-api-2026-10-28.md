# Seller API 增量核对：2026-10-28

- 来源：[Ozon 官方 News](https://docs.ozon.ru/api/seller/zh/#tag/News)，在用户 Chrome 已打开页面中按 `workflows/chrome-official-seller-api-extract.md` 抽取；上一轮索引截至 2026-09-28。
- operation 由 273 个更新到 276 个，无删除；News 条目由 170 条更新到 175 条。内容有变化的 32 个 operation 用新抓取数据覆盖，其余保留旧对象以避免 Redoc 折叠状态造成的噪音。
- 例外保留旧版：`SellerActionsProductsAdd`（新页面把 `action_price` / `discount_percent` 两个请求变体渲染成空 `{ }`）和 `ProductImportPicturesV2`（嵌套 `items` 表格折叠，内容未变）。
- 补抓 2025-05-14 条目：`/v1/returns/company/fbs/info` 响应新增 `box_count`、`utc_offset`，删除 `company_id`。上轮漏抓是因为该页面标题少了“日”字。2026-09-02 条目的官方措辞改为“在 授权 → 如何获取API 密钥 部分更新了API密钥的有效期”。

## 新增 News

- [10 月 6 日](https://docs.ozon.ru/api/seller/zh/#section/2026106)：新增 `POST /v1/barcode/delete`（`BarcodeDelete`），按 `barcodes[]`（`barcode` + `sku`，1..100 对）解除条形码与商品绑定，响应 `errors[]` 为空表示全部成功。`/v1/product/prices/details` 响应新增 `prices.weight_index`。
- [10 月 13 日](https://docs.ozon.ru/api/seller/zh/#section/20261013)：`/v2/posting/fbs/act/get-postings` 的 `result.is_blr_traceable`、`result.scanit` 标记弃用；调用方应容忍字段缺失。
- [10 月 15 日](https://docs.ozon.ru/api/seller/zh/#section/20261015)：`/v2/posting/fbs/package-label` 弃用，2026-11-02 停用；改用 `/v3/posting/fbs/package-label/create` + `/v2/posting/fbs/package-label/get` 的异步任务流程。迁移要点见 [FBS/rFBS 货件 API](../api/posting-fbs.md#标签打印迁移2026-10-15-news)。
- [10 月 22 日](https://docs.ozon.ru/api/seller/zh/#section/20261022)：FBS 商品实例方法 `/v6/fbs/posting/product/exemplar/set`、`/v6/fbs/posting/product/exemplar/create-or-get`、`/v5/fbs/posting/product/exemplar/status`、`/v5/fbs/posting/product/exemplar/validate`、`/v1/fbs/posting/product/exemplar/update` 从 Beta 转为正式版。

## 停用时间线（迁移优先级）

| 停用日期 | 旧调用 | 替代 |
| --- | --- | --- |
| 2026-10-13（已过） | `/v1/actions/candidates`、`/v1/actions/products`、`/v1/actions/products/deactivate`、`/v1/actions/auto-add/products/*` | 对应 `/v2/...` |
| 2026-10-13（已过） | `/v1/actions/products/activate` | `/v1/actions/products/update` |
| 2026-11-02 | `/v2/posting/fbs/package-label` | `/v3/posting/fbs/package-label/create` + `/v2/posting/fbs/package-label/get` |
| 2026-11-23 | `/v3/product/list` 的 `result.total`；`/v4/product/info/stocks`、`/v5/product/info/prices` 的 `total` | 同层级 `total_items` |

## 代码影响

两个项目里实际需要迁移的只有标签打印：

- AICollection [PR #2309](https://github.com/xmdragon/AICollection/pull/2309)：`erp_fbs_package_labels` 改为 create（优先 `big_label`）→ 轮询 get（约 22 秒上限）→ 下载并校验 PDF，新逻辑在 `src-tauri/src/services/ozon_seller_api/package_label.rs`。调用方 `erp_order_labels.rs` 仍拿 PDF 字节，未就绪或超时返回 `NotReady`。Rust 编译和单测未在本轮运行。
- ZhiPin [PR #555](https://github.com/xmdragon/ZhiPin/pull/555)：`plugins/ef/channels/ozon/api/client_mixins/orders.py` 的 `get_package_labels` 同样改为异步流程，每次请求都走本地与共享限流，新增 `PackageLabelTaskError`（`not_ready`、`unprinted_postings`）；`services/label_service.py` 返回 `label_not_ready` / `label_task_failed`。mock server 新增 create/get/下载端点，`/v3/product/list` 返回 `total_items`，exemplar status 改为 v5。
- 无需改：ZhiPin 促销已使用 `/v2/actions/auto-add/products/*`，商品同步已读 `result.total_items`；两个项目都没有调用其他 `/v1/actions/*`、exemplar、`act/get-postings` 或 `/v1/product/prices/details`。

以上两个 PR 在 2026-10-28 尚未合并；合并前需要用真实店铺试打一次标签，确认 `file_url` 的下载鉴权。

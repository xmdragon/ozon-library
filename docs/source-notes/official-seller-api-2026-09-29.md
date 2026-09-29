# Seller API 增量核对：2026-09-29

- 来源：[Ozon 官方 News](https://docs.ozon.ru/api/seller/zh/#tag/News)，在 Chrome 已打开页面保存的 DOM 中核对；主线原索引截至 2026-09-03，本次新增 2026-09-10 至 2026-09-28 的 7 条记录。
- 当前页面包含 273 个 operation；索引由 262 个更新到 273 个。本次只刷新新增方法与这 7 条 News 命中的已有方法详情。原始更新记录见 `indexes/official-seller-api.news.json`，具体字段见 `docs/api/official/`。
- [9 月 23 日更新](https://docs.ozon.ru/api/seller/zh/#section/2026923)：八个旧促销方法将在 2026-10-13 停用；自动添加商品列表、候选、更新、删除分别迁到 `/v2/actions/auto-add/products/*`。[新版列表](https://docs.ozon.ru/api/seller/zh/#operation/ActionsAutoAddProductsListV2)的展开字段说明明确：`add_mode=true` 表示**手动**添加，因此自动添加商品应筛选 `false`；缺失或非布尔值不得当成可删除商品。
- [9 月 24 日更新](https://docs.ozon.ru/api/seller/zh/#section/2026924)：`/v3/product/list` 的 `result.total` 及库存、价格接口顶层 `total` 将于 2026-11-23 关闭，分别使用同层级 `total_items`。
- [9 月 25 日更新](https://docs.ozon.ru/api/seller/zh/#section/2026925)为商品可见性筛选增加 `SHOWCASE_SELECT_ACTIVE`；这是新增可选值，不要求现有调用改变筛选条件。
- [9 月 28 日更新](https://docs.ozon.ru/api/seller/zh/#section/2026928)为 `/v1/seller-actions/products/add` 添加可选的 `products.action_price`；现有调用不必凭此强制补值。

代码影响核对：AICollection 的桌面促销清理使用旧自动添加列表和删除接口；ZhiPin 的促销清理也使用这两个接口，其商品同步与连接测试还读取旧的 `result.total`。本次未发现两个仓库调用 9 月 23 日列出的其他旧促销接口。新版响应只按官方文档核对，尚未使用真实卖家账户执行删除或分页。

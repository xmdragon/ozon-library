# Seller API 增量核对：2026-11-01

- 来源：[Ozon 官方 News](https://docs.ozon.ru/api/seller/zh/#tag/News)，在用户 Chrome 已打开页面中按 `workflows/chrome-official-seller-api-extract.md` 抽取；上一轮索引截至 2026-10-28。
- operation 仍为 276 个，无新增、无删除；News 条目由 175 条更新到 176 条。逐个比对 operation 页面文本哈希后，只有两个已知例外和旧版不同：`SellerActionsProductsAdd`、`ProductImportPicturesV2`，按惯例保留旧版。因此本轮没有覆盖任何 operation 内容，只更新了 `captured_at` 和由 News 派生的 `news_updates`。
- 旧的 175 条 News 文本全部和页面一致，没有被改写。
- 两个方法改的字段都在 Redoc 默认折叠的嵌套行里，折叠状态下抓到的索引文本没有变化。新描述是在 Chrome 中展开 `prices`、`products` 两行后读取的，记录在 [库存和价格 API](../api/stock-price.md#统一价格语义2026-10-29-news)。

## 新增 News

- [10 月 29 日](https://docs.ozon.ru/api/seller/zh/#section/20261029)：`/v1/product/import/prices` 更新了请求中 `prices.price` 的描述；`/v1/actions/products/update` 更新了请求中 `products.action_price` 的描述。两处都只改了文案，字段结构、必填项和示例都没变。新文案统一了“最高价格”的说法：两个方法中任意一个改最高价，商品卡片上的值都会同步更新。`action_price` 在“促销码”促销之外会直接改卡片最高价，并按“弹性提升”/“最大提升”的限额决定加入还是移出促销。

## 代码影响

只改了描述，没有字段增删，也没有新的停用日期，两个项目都不需要改代码：

- AICollection：`src-tauri/src/services/ozon_seller_api.rs` 的 `update_prices_once` 调 `/v1/product/import/prices`，`PriceUpdateEntry` 只发 `product_id`、`price`（字符串）和 `currency_code`，结构和新文档一致。项目里没有调用 `/v1/actions/products/update`。
- ZhiPin：`plugins/ef/channels/ozon/api/client_mixins/products.py` 的 `update_prices` 和 `ozon-mock-server/app/api/products.py` 的 mock 都按字符串处理 `price`，和新文档一致。项目里没有调用 `/v1/actions/products/update`。
- 不属于本轮 News、但需要留意：ZhiPin `update_prices` 默认仍发送 `auto_action_enabled: DISABLED`，该字段已在 2026-09-11 标记弃用（还没删除）。
- 以后如果项目用 `/v1/actions/products/update` 管理促销，要注意它会改商品卡片上的最高价，和改价流程共用同一个值。

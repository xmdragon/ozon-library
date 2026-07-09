# 官方 Seller API News 更新索引

> 由 `tools/apply_official_api_news.py` 根据 Chrome 抽取的 `indexes/official-seller-api.news.json` 生成。

## 摘要

- News 条目数：149
- 当前方法页已标记废弃/移除：9
- News 中提到但当前 operation 索引不存在的废弃/移除方法：30
- 标签统计：`added_field`: 50, `deprecated_field`: 9, `deprecated_method`: 23, `graduated`: 16, `new_method`: 33, `removed_field`: 11, `removed_method`: 22, `updated`: 104

## 已在当前方法页标记的方法

| 方法 | 状态 | 日期 | 替代方法 | News |
| --- | --- | --- | --- | --- |
| `/v1/actions/discounts-task/list` | `deprecated` | 2026-01-29 | `/v2/actions/discounts-task/list` | [来源](https://docs.ozon.ru/api/seller/zh/#section/2026129) |
| `/v1/delivery-method/list` | `deprecated` | 2026-03-24 | `/v2/delivery-method/list` | [来源](https://docs.ozon.ru/api/seller/zh/#section/2026324) |
| `/v1/posting/carriage-available/list` | `deprecated` | 2026-02-16 | `/v2/carriage/delivery/list` | [来源](https://docs.ozon.ru/api/seller/zh/#section/2026216) |
| `/v1/review/list` | `deprecated` | 2026-06-11 | `/v2/review/list` | [来源](https://docs.ozon.ru/api/seller/zh/#section/2026611) |
| `/v1/warehouse/list` | `deprecated` | 2026-03-24 | `/v2/warehouse/list` | [来源](https://docs.ozon.ru/api/seller/zh/#section/2026324) |
| `/v3/finance/transaction/list` | `deprecated` | 2026-05-06 | `/v1/finance/accrual/postings`, `/v1/finance/accrual/types`, `/v1/finance/accrual/by-day` | [来源](https://docs.ozon.ru/api/seller/zh/#section/202656) |
| `/v3/finance/transaction/totals` | `deprecated` | 2026-05-06 | `/v1/finance/accrual/postings`, `/v1/finance/accrual/types`, `/v1/finance/accrual/by-day` | [来源](https://docs.ozon.ru/api/seller/zh/#section/202656) |
| `/v3/posting/fbs/list` | `deprecated` | 2026-04-30 | `/v4/posting/fbs/list` | [来源](https://docs.ozon.ru/api/seller/zh/#section/2026430) |
| `/v3/posting/fbs/unfulfilled/list` | `deprecated` | 2026-04-30 | `/v4/posting/fbs/unfulfilled/list` | [来源](https://docs.ozon.ru/api/seller/zh/#section/2026430) |

## News 中已移除或当前索引缺失的方法

| 方法 | 标记 | 日期 | 替代方法 | 摘要 |
| --- | --- | --- | --- | --- |
| `/v2/chat/list` | `removed_method` | 2026-06-09 | `/v3/chat/list` | /v2/chat/list 该方式已过期，我们已将其从文件中删除。请使用 替代方法：/v3/chat/list |
| `/v1/analytics/average-delivery-time/summary` | `removed_method` | 2026-05-19 | 无 | /v1/analytics/average-delivery-time/summary 该方式已过期，我们已将其从文件中删除。 |
| `/v1/seller-actions/update/ozon-card-discount` | `removed_method` | 2026-04-14 | 无 | /v1/seller-actions/update/ozon-card-discount 该促销活动已无法使用，相关方法已从文档中删除。 |
| `/v2/chat/history` | `removed_method` | 2026-02-20 | `/v3/chat/history` | /v2/chat/history 该方式已过期，我们已将其从文件中删除。请使用 替代方法：/v3/chat/history |
| `/v2/fbs/posting/sent-by-seller` | `removed_method` | 2026-01-20 | 无 | /v2/fbs/posting/sent-by-seller 该方式已过期，我们已将其从文件中删除。 — 在 方法操作顺序 → 管理订单 → rFBS Crossborder 模式 和 方法操作顺序 → 管理订单 → rFBS Crossborder 模式含集成物流服务 部分，更新了有关方法操作的描述。 |
| `/v4/fbs/posting/product/exemplar/validate` | `deprecated_method`, `removed_method` | 2026-01-13 | 无 | /v4/fbs/posting/product/exemplar/validate 方法已过时， 已从 文档中移除。 |
| `/v2/posting/fbs/product/change` | `removed_method` | 2025-12-25 | 无 | /v2/posting/fbs/product/change 该方式已过期，我们已将其从文件中删除。 |
| `/v1/conditional-cancellation/list` | `removed_method` | 2025-09-03 | `/v2/conditional-cancellation/list` | /v1/conditional-cancellation/list 这些方式已过期，我们已将其从文件中删除。请使用 替代方法：/v2/conditional-cancellation/list |
| `/v1/conditional-cancellation/approve` | `removed_method` | 2025-09-03 | `/v2/conditional-cancellation/approve` | /v1/conditional-cancellation/approve 该方式已过期，我们已将其从文件中删除。请使用 替代方法：/v2/conditional-cancellation/approve |
| `/v1/conditional-cancellation/reject` | `removed_method` | 2025-09-03 | `/v2/conditional-cancellation/reject` | /v1/conditional-cancellation/reject 该方式已过期，我们已将其从文件中删除。请使用 替代方法：/v2/conditional-cancellation/reject |
| `/v2/chat/list` | `deprecated_method` | 2025-07-28 | `/v3/chat/list` | /v2/chat/list 该方法将于未来停用。请改用 替代方法：/v3/chat/list |
| `/v1/product/upload_digital_codes/info` | `deprecated_method`, `removed_method` | 2025-07-01 | 无 | /v1/product/upload_digital_codes/info 方法已过时， 已从 文档中移除。 — 在 方法操作顺序 → 上传和更新商品 部分，更新了有关方法操作的描述。 |
| `/v3/product/info/attributes` | `deprecated_method` | 2025-06-19 | `/v4/product/info/attributes` | /v3/product/info/attributes 该方法已过时。请切换到新版本 替代方法：/v4/product/info/attributes |
| `/v1/conditional-cancellation/get` | `deprecated_method` | 2025-06-19 | `/v2/conditional-cancellation/list` | /v1/conditional-cancellation/get 方法即将过时，并将于2025年8月3日停用。请改用 替代方法：/v2/conditional-cancellation/list |
| `/v1/conditional-cancellation/list` | `deprecated_method` | 2025-06-03 | `/v2/conditional-cancellation/list` | /v1/conditional-cancellation/list 方法即将过时，并将于2025年8月3日停用。请切换到新版本 替代方法：/v2/conditional-cancellation/list |
| `/v1/conditional-cancellation/approve` | `deprecated_method` | 2025-06-03 | `/v2/conditional-cancellation/approve` | /v1/conditional-cancellation/approve 方法即将过时，并将于2025年8月3日停用。请切换到新版本 替代方法：/v2/conditional-cancellation/approve |
| `/v1/conditional-cancellation/reject` | `deprecated_method` | 2025-06-03 | `/v2/conditional-cancellation/reject` | /v1/conditional-cancellation/reject 方法即将过时，并将于2025年8月3日停用。请切换到新版本 替代方法：/v2/conditional-cancellation/reject |
| `/v1/product/import/stocks` | `deprecated_method`, `removed_method` | 2025-05-27 | `/v2/products/stock` | /v1/product/import/stocks 该方法已过时，已从文档中删除。请改用 替代方法：/v2/products/stock |
| `/v2/chat/history` | `deprecated_method` | 2025-05-13 | `/v3/chat/history` | /v2/chat/history 方法即将过时，并将于2025年7月13日停用。请切换到新版本 替代方法：/v3/chat/history |
| `/v1/finance/realization` | `deprecated_method`, `removed_method` | 2025-05-06 | `/v2/finance/realization` | /v1/finance/realization 该方法已过时，已从文档中删除。 请改用 替代方法：/v2/finance/realization |
| `/v1/product/import/stocks` | `deprecated_method` | 2025-05-06 | `/v2/products/stocks` | /v1/product/import/stocks 方法将于2025年5月27日停用。请改用 替代方法：/v2/products/stocks |
| `/v1/actions/hotsales/products` | `deprecated_method`, `removed_method` | 2025-03-11 | 无 | /v1/actions/hotsales/products 方法已过时，已从文档中移除。 |
| `/v2/product/info` | `removed_method` | 2025-03-10 | `/v3/product/info/list` | /v2/product/info 该方法已过期，我们已将其从文件中删除。请使用 替代方法：/v3/product/info/list |
| `/v4/product/info/prices` | `removed_method` | 2025-02-18 | 无 | /v4/product/info/prices 该方式已过期，我们已将其从文件中删除。 |
| `/v3/returns/company/fbs` | `removed_method` | 2025-02-18 | `/v1/returns/list`, `/v1/report/returns/create` | /v3/returns/company/fbs 该方式已过期，我们已将其从文件中删除。请使用 替代方法：/v1/returns/list, /v1/report/returns/create |
| `/v1/report/returns/create` | `removed_method` | 2025-02-18 | 无 | /v1/report/returns/create 该方式已过期，我们已将其从文件中删除。 |
| `/v2/product/info/list` | `removed_method` | 2025-02-17 | `/v3/product/info/list` | /v2/product/info/list 该方式已过期，我们已将其从文件中删除。请使用 替代方法：/v3/product/info/list |
| `/v2/product/list` | `removed_method` | 2025-02-11 | 无 | /v2/product/list 该方式已过期，我们已将其从文件中删除。 |
| `/v3/product/info/stocks` | `removed_method` | 2025-02-10 | 无 | /v3/product/info/stocks 该方式已过期，我们已将其从文件中删除。 |
| `/v1/product/pictures/info` | `removed_method` | 2025-02-10 | `/v2/product/pictures/info` | /v1/product/pictures/info 该方式已过期，我们已将其从文件中删除。请使用 替代方法：/v2/product/pictures/info |

## 字段级新增、废弃与移除

| 方法 | 日期 | 标记 | 摘要 | News |
| --- | --- | --- | --- | --- |
| `/v1/actions` | 2026-05-12 | `added_field` | /v1/actions 新增了参数result.auto_add_dates至方法响应中。 | [来源](https://docs.ozon.ru/api/seller/zh/#section/2026512) |
| `/v1/actions/products` | 2025-12-23 | `added_field` | /v1/actions/products 添加了参数 result.products.current_boost、result.products.price_min_elastic、result.products.price_max_elastic、result.products.min_boost 和 result.products.max_boost 到方法的响应中。 | [来源](https://docs.ozon.ru/api/seller/zh/#section/20251223) |
| `/v1/actions/products` | 2025-05-15 | `added_field` | /v1/actions/products 添加了参数 result.products.alert_max_action_price_failed 和 result.products.alert_max_action_price 到方法的响应中。 | [来源](https://docs.ozon.ru/api/seller/zh/#section/2025515) |
| `/v1/actions/products` | 2025-03-13 | `added_field`, `deprecated_field` | /v1/actions/products 我们已将 offset 参数标记为已弃用，并添加了 last_id分页参数。 | [来源](https://docs.ozon.ru/api/seller/zh/#section/2025313) |
| `/v1/carriage/pass/update` | 2026-07-07 | `added_field` | /v1/carriage/pass/update 在方法请求中添加了参数arrival_passes.arrival_time、arrival_passes.tracking_number和arrival_passes.tracking_url。 | [来源](https://docs.ozon.ru/api/seller/zh/#section/202677) |
| `/v1/delivery-method/list` | 2024-12-26 | `added_field` | /v1/delivery-method/list 添加字段 result.sla_cut_in 在方法响应。 | [来源](https://docs.ozon.ru/api/seller/zh/#section/20241226) |
| `/v1/description-category/attribute` | 2025-03-19 | `added_field` | /v1/description-category/attribute 在方法响应中添加了参数 result.complex_is_collection。 | [来源](https://docs.ozon.ru/api/seller/zh/#section/2025319) |
| `/v1/finance/realization/posting` | 2025-12-25 | `removed_field` | /v1/finance/realization/posting 已从方法响应中移除参数 header.doc_amount 和 header.vat_amount。 | [来源](https://docs.ozon.ru/api/seller/zh/#section/20251225) |
| `/v1/posting/fbp/list` | 2026-06-30 | `added_field` | /v1/posting/fbp/list 已在方法响应中添加参数postings.financial_data.products.posting_commission和postings.financial_data.products.return_commission。 | [来源](https://docs.ozon.ru/api/seller/zh/#section/2026630) |
| `/v1/pricing-strategy/product/info` | 2025-06-19 | `deprecated_field` | /v1/pricing-strategy/product/info 并将参数 result.strategy_competitor_id 标记为已弃用。 | [来源](https://docs.ozon.ru/api/seller/zh/#section/2025619) |
| `/v1/product/import-by-sku` | 2025-05-06 | `removed_field` | /v1/product/import-by-sku 已从方法请求中移除参数 items.premium_price。 | [来源](https://docs.ozon.ru/api/seller/zh/#section/202556) |
| `/v1/product/import/info` | 2025-05-06 | `removed_field` | /v1/product/import/info 已从方法响应中移除参数 result.items.errors.optional_description_elements。 | [来源](https://docs.ozon.ru/api/seller/zh/#section/202556) |
| `/v1/product/import/prices` | 2025-10-22 | `added_field` | /v1/product/import/prices 已添加参数 prices.manage_elastic_boosting_through_price 到方法请求。 | [来源](https://docs.ozon.ru/api/seller/zh/#section/20251022) |
| `/v1/product/import/prices` | 2025-02-24 | `added_field` | /v1/product/import/prices 在方法请求中添加了参数 prices.net_price，用于指定商品的成本价。 | [来源](https://docs.ozon.ru/api/seller/zh/#section/2025224) |
| `/v1/product/import/prices` | 2025-01-15 | `added_field` | /v1/product/import/prices 添加字段 prices.min_price_for_auto_actions_enabled 在方法请求。 | [来源](https://docs.ozon.ru/api/seller/zh/#section/2025115) |
| `/v1/product/import/prices` | 2024-12-24 | `added_field` | /v1/product/import/prices 在方法请求中添加了参数 prices.vat。 | [来源](https://docs.ozon.ru/api/seller/zh/#section/20241224) |
| `/v1/product/info/stocks-by-warehouse/fbs` | 2025-10-23 | `added_field` | /v1/product/info/stocks-by-warehouse/fbs 在请求中添加了参数 offer_id，并在方法响应中添加了参数 results.offer_id。 | [来源](https://docs.ozon.ru/api/seller/zh/#section/20251023) |
| `/v1/product/prices/details` | 2026-05-19 | `added_field`, `deprecated_field` | /v1/product/prices/details 在方法响应中：新增了prices.price_indexes参数；将prices.discount_percent参数标记为已弃用；更新了prices.customer_price参数的说明。 | [来源](https://docs.ozon.ru/api/seller/zh/#section/2026519) |
| `/v1/question/answer/list` | 2026-05-19 | `added_field` | /v1/question/answer/list 在方法响应中新增了answers.status_publication参数。 | [来源](https://docs.ozon.ru/api/seller/zh/#section/2026519) |
| `/v1/question/list` | 2026-05-19 | `added_field` | /v1/question/list 在方法请求中新增了sort_dir和limit参数。在方法响应中新增了has_next参数。 | [来源](https://docs.ozon.ru/api/seller/zh/#section/2026519) |
| `/v1/report/info` | 2025-11-18 | `added_field` | /v1/report/info 在方法的响应中新增参数result.expires_at。 | [来源](https://docs.ozon.ru/api/seller/zh/#section/20251118) |
| `/v1/report/list` | 2025-11-18 | `added_field` | /v1/report/list 在方法的响应中新增参数result.reports.expires_at。 | [来源](https://docs.ozon.ru/api/seller/zh/#section/20251118) |
| `/v1/report/postings/create` | 2025-09-29 | `added_field` | /v1/report/postings/create 已添加以下参数filter.warehouse_id、filter.delivery_method_id、filter.is_express、with.additional_data、with.analytics_data、with.customer_data 和 with.jewelry_codes 到方法请求。 | [来源](https://docs.ozon.ru/api/seller/zh/#section/2025929) |
| `/v1/returns/list` | 2025-12-12 | `removed_field` | /v1/returns/list 移除了方法请求中参数 filter.visual_status_name 的值 ReturnCompensated。 | [来源](https://docs.ozon.ru/api/seller/zh/#section/20251212) |
| `/v1/returns/list` | 2025-11-20 | `added_field` | /v1/returns/list 已添加参数 filter.compensation_status_id到方法请求。在方法的响应中添加了参数 returns.compensation_status。 | [来源](https://docs.ozon.ru/api/seller/zh/#section/20251120) |
| `/v1/roles` | 2026-03-04 | `added_field` | /v1/roles 在方法的响应中新增了参数 expires_at。 | [来源](https://docs.ozon.ru/api/seller/zh/#section/202634) |
| `/v1/warehouse/fbs/first-mile/update` | 2025-10-17 | `added_field` | /v1/warehouse/fbs/first-mile/update 在方法请求中新增了参数 cut_in_time 和 timeslot_id。 | [来源](https://docs.ozon.ru/api/seller/zh/#section/20251017) |
| `/v1/warehouse/list` | 2026-04-30 | `added_field` | /v1/warehouse/list 在方式的请求中添加了with.able_to_set_price参数。在方式的响应中添加了result.is_able_to_set_price和result.is_presorted参数。 | [来源](https://docs.ozon.ru/api/seller/zh/#section/2026430) |
| `/v1/warehouse/list` | 2025-12-18 | `added_field` | /v1/warehouse/list 在方法请求中添加了参数 limit 和 offset。 | [来源](https://docs.ozon.ru/api/seller/zh/#section/20251218) |
| `/v2/delivery-method/list` | 2026-05-22 | `added_field` | /v2/delivery-method/list 在方法响应中新增了参数delivery_methods.tpl_dropoff_point。 — 在错误板块中，已为 | [来源](https://docs.ozon.ru/api/seller/zh/#section/2026522) |
| `/v2/finance/realization` | 2025-12-25 | `removed_field` | /v2/finance/realization 已从方法响应中移除参数 result.header.doc_amount 和 result.header.vat_amount。 | [来源](https://docs.ozon.ru/api/seller/zh/#section/20251225) |
| `/v2/posting/fbs/get-by-barcode` | 2025-10-16 | `removed_field` | /v2/posting/fbs/get-by-barcode 已从方法响应中移除参数 result.analytics_data 和 result.financial_data。 | [来源](https://docs.ozon.ru/api/seller/zh/#section/20251016) |
| `/v2/posting/fbs/get-by-barcode` | 2025-05-06 | `removed_field` | /v2/posting/fbs/get-by-barcode 已从方法响应中移除参数 result.financial_data.products.client_price，result.financial_data.products.picking 和 result.products.mandatory_mark。 | [来源](https://docs.ozon.ru/api/seller/zh/#section/202556) |
| `/v2/product/pictures/info` | 2025-06-04 | `added_field` | /v2/product/pictures/info 在方法的响应中新增了参数items.errors。 | [来源](https://docs.ozon.ru/api/seller/zh/#section/202564) |
| `/v2/returns/rfbs/list` | 2025-12-26 | `deprecated_field` | /v2/returns/rfbs/list 参数 returns.client_name 即将废弃，将于2026年2月2日停止支持。 | [来源](https://docs.ozon.ru/api/seller/zh/#section/20251226) |
| `/v2/warehouse/list` | 2025-12-18 | `added_field` | /v2/warehouse/list 在方法请求中添加了参数 limit 和 cursor。在方法的响应中添加了参数 cursor。 | [来源](https://docs.ozon.ru/api/seller/zh/#section/20251218) |
| `/v2/warehouse/list` | 2025-12-16 | `added_field` | /v2/warehouse/list 在方法的响应中添加了参数 has_next 和 cursor。 | [来源](https://docs.ozon.ru/api/seller/zh/#section/20251216) |
| `/v3/posting/fbs/get` | 2026-04-17 | `added_field` | /v3/posting/fbs/get 在方法响应中新增参数result.tariffication_steps。 | [来源](https://docs.ozon.ru/api/seller/zh/#section/2026417) |
| `/v3/posting/fbs/get` | 2025-11-27 | `added_field` | /v3/posting/fbs/get 在方法的响应中：更新了参数 result.analytics_data.payment_type_group_name 的描述；新增了参数 result.analytics_data.client_delivery_date_begin 和result.analytics_data.client_delivery_date_end。 | [来源](https://docs.ozon.ru/api/seller/zh/#section/20251127) |
| `/v3/posting/fbs/get` | 2025-10-21 | `added_field` | /v3/posting/fbs/get 在方法的响应中添加了参数 result.shipment_date_without_delay。 — 在 Ozon发送的通知 → 新的发货 部分中，更新了新发货通知的示例。 | [来源](https://docs.ozon.ru/api/seller/zh/#section/20251021) |
| `/v3/posting/fbs/get` | 2025-09-24 | `added_field` | /v3/posting/fbs/get 在方法响应中： • 添加了参数 result.financial_data.products.customer_price； • 更新了 result.requirements.products_requiring_gtd、result.requirements.products_requiring_mandatory_mark、result.requirements.products_requiring_jw_uin、result.requirements.products_requiring_rnpt、result.status、result.substatus、result.previous_substatus、result.financial_data.products.price、result.financial_data.products.old_price、result.customer.phone、result.addressee.phone 和 result.products.is_marketplace_buyout 参数描述。 | [来源](https://docs.ozon.ru/api/seller/zh/#section/2025924) |
| `/v3/posting/fbs/get` | 2025-07-02 | `added_field` | /v3/posting/fbs/get 在方法的响应中新增了参数result.requirements.products_requiring_change_country。 | [来源](https://docs.ozon.ru/api/seller/zh/#section/202572) |
| `/v3/posting/fbs/get` | 2025-06-05 | `added_field` | /v3/posting/fbs/get 在方法请求中添加了参数 with.legal_info 参数的 和 result.legal_info 到方法的响应中。 | [来源](https://docs.ozon.ru/api/seller/zh/#section/202565) |
| `/v3/posting/fbs/get` | 2025-02-27 | `added_field` | /v3/posting/fbs/get 在方法响应中添加了参数 result.previous_substatus。 | [来源](https://docs.ozon.ru/api/seller/zh/#section/2025227) |
| `/v3/posting/fbs/list` | 2026-04-30 | `deprecated_method`, `added_field` | /v3/posting/fbs/list 在方式的响应中添加了参数result.postings.is_presortable、result.postings.destination_place_id、result.postings.destination_place_name和result.postings.customer.customer_email。 | [来源](https://docs.ozon.ru/api/seller/zh/#section/2026430) |
| `/v3/posting/fbs/list` | 2025-09-24 | `added_field` | /v3/posting/fbs/list 在方法响应中： • 添加了参数 result.postings.financial_data.products.customer_price； • 更新了 result.postings.requirements.products_requiring_gtd、result.postings.requirements.products_requiring_mandatory_mark、result.postings.requirements.products_requiring_jw_uin、result.postings.requirements.products_requiring_rnpt、result.postings.financial_data.products.price、result.postings.financial_data.products.old_price、result.postings.customer.phone、result.postings.addressee.phone 和 result.postings.products.is_marketplace_buyout 参数描述。 | [来源](https://docs.ozon.ru/api/seller/zh/#section/2025924) |
| `/v3/posting/fbs/list` | 2025-07-02 | `added_field` | /v3/posting/fbs/list 在方法的响应中新增了参数result.postings.requirements.products_requiring_change_country。 | [来源](https://docs.ozon.ru/api/seller/zh/#section/202572) |
| `/v3/posting/fbs/list` | 2025-06-05 | `added_field` | /v3/posting/fbs/list 在方法请求中添加了参数 with.legal_info 参数的 和 result.postings.legal_info 到方法的响应中。 | [来源](https://docs.ozon.ru/api/seller/zh/#section/202565) |
| `/v3/posting/fbs/unfulfilled/list` | 2026-04-17 | `added_field` | /v3/posting/fbs/unfulfilled/list 在各方法响应中新增参数result.postings.tariffication_steps。 | [来源](https://docs.ozon.ru/api/seller/zh/#section/2026417) |
| `/v3/posting/fbs/unfulfilled/list` | 2025-11-27 | `added_field` | /v3/posting/fbs/unfulfilled/list 在各方法的响应中：更新了参数 result.analytics_data.payment_type_group_name 的描述；新增了参数 result.analytics_data.client_delivery_date_begin 和result.analytics_data.client_delivery_date_end。 | [来源](https://docs.ozon.ru/api/seller/zh/#section/20251127) |
| `/v3/posting/fbs/unfulfilled/list` | 2025-10-21 | `added_field` | /v3/posting/fbs/unfulfilled/list 在方法的响应中添加了参数result.postings.shipment_date_without_delay。 | [来源](https://docs.ozon.ru/api/seller/zh/#section/20251021) |
| `/v3/posting/fbs/unfulfilled/list` | 2025-05-06 | `removed_field` | /v3/posting/fbs/unfulfilled/list 已从方法响应中移除参数 result.postings.financial_data.products.client_price，result.postings.financial_data.products.picking 和 result.postings.products.mandatory_mark。 | [来源](https://docs.ozon.ru/api/seller/zh/#section/202556) |
| `/v3/product/import` | 2025-05-22 | `added_field` | /v3/product/import 添加字段 items.promotions 在方法请求。 | [来源](https://docs.ozon.ru/api/seller/zh/#section/2025522) |
| `/v3/product/import` | 2025-05-06 | `removed_field` | /v3/product/import 已从方法请求中移除参数 items.image_group_id 和 items.premium_price。 | [来源](https://docs.ozon.ru/api/seller/zh/#section/202556) |
| `/v3/product/info/list` | 2025-11-12 | `removed_field` | /v3/product/info/list 在方法回答该items.marketing_price参数已过期，我们已将其从文件中删除。 | [来源](https://docs.ozon.ru/api/seller/zh/#section/20251112) |
| `/v3/product/info/list` | 2025-10-06 | `deprecated_field`, `added_field` | /v3/product/info/list 参数 items.marketing_price 即将废弃，我们将于2025年11月12日关闭该参数。 | [来源](https://docs.ozon.ru/api/seller/zh/#section/2025106) |
| `/v3/product/info/list` | 2025-08-14 | `added_field` | /v3/product/info/list 在方法的响应中新增了参数 items.promotions、items.promotions.is_enabled、items.promotions.type 和 items.sku。 | [来源](https://docs.ozon.ru/api/seller/zh/#section/2025814) |
| `/v3/product/info/list` | 2025-08-05 | `deprecated_field` | /v3/product/info/list 已将参数 items.is_prepayment_allowed 标记为已弃用。 | [来源](https://docs.ozon.ru/api/seller/zh/#section/202585) |
| `/v4/product/info/limit` | 2026-06-09 | `added_field` | /v4/product/info/limit 在方法的响应中添加了参数 operation_limits和total.quota_by_category的说明。 | [来源](https://docs.ozon.ru/api/seller/zh/#section/202669) |
| `/v4/product/info/stocks` | 2025-12-18 | `deprecated_field` | /v4/product/info/stocks 已将方法响应中的参数 items.stocks.warehouse_ids 标记为已弃用。 | [来源](https://docs.ozon.ru/api/seller/zh/#section/20251218) |
| `/v4/product/info/stocks` | 2025-06-11 | `added_field` | /v4/product/info/stocks 在方法的响应中新增了参数items.stocks.warehouse_ids。 | [来源](https://docs.ozon.ru/api/seller/zh/#section/2025611) |
| `/v5/product/info/prices` | 2025-11-12 | `removed_field` | /v5/product/info/prices 在方法回答该price.marketing_price参数已过期，我们已将其从文件中删除。 | [来源](https://docs.ozon.ru/api/seller/zh/#section/20251112) |
| `/v5/product/info/prices` | 2025-10-06 | `deprecated_field` | /v5/product/info/prices 参数 items.price.marketing_price 即将废弃，我们将于2025年11月12日关闭该参数。 | [来源](https://docs.ozon.ru/api/seller/zh/#section/2025106) |
| `/v5/product/info/prices` | 2025-05-28 | `added_field` | /v5/product/info/prices 在方法的响应中新增了参数items.price.net_price。 | [来源](https://docs.ozon.ru/api/seller/zh/#section/2025528) |

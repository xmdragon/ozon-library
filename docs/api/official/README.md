# 官方 Seller API 方法文档

## 用途

这里按官方 Chrome 抽取索引展开为每个 operation 一个 Markdown 文件，方便 AI 和人工直接检索方法、参数、返回结构和示例。

## 生成信息

- 方法页数量：264
- 来源：`indexes/official-seller-api.operations.json`
- 生成器：`tools/generate_official_api_docs.py`
- 重新生成：`python3 tools/generate_official_api_docs.py`

## 方法目录

### actions

- [活动清单](get-v1-actions-Promos.md) - `GET /v1/actions` - `Promos`
- [获取可自动添加到促销活动中的商品列表](post-v1-actions-auto-add-products-candidates-ActionsAutoAddProductsCandidates.md) - `POST /v1/actions/auto-add/products/candidates` - `ActionsAutoAddProductsCandidates`
- [从促销活动自动添加列表中删除商品](post-v1-actions-auto-add-products-delete-ActionsAutoAddProductsDelete.md) - `POST /v1/actions/auto-add/products/delete` - `ActionsAutoAddProductsDelete`
- [获取促销活动自动添加列表中的商品列表](post-v1-actions-auto-add-products-list-ActionsAutoAddProductsList.md) - `POST /v1/actions/auto-add/products/list` - `ActionsAutoAddProductsList`
- [在促销活动自动添加列表中添加或更新商品](post-v1-actions-auto-add-products-update-ActionsAutoAddProductsUpdate.md) - `POST /v1/actions/auto-add/products/update` - `ActionsAutoAddProductsUpdate`
- [可用的促销商品清单](post-v1-actions-candidates-PromosCandidates.md) - `POST /v1/actions/candidates` - `PromosCandidates`
- [同意折扣申请](post-v1-actions-discounts-task-approve-promos_task_approve.md) - `POST /v1/actions/discounts-task/approve` - `promos_task_approve`
- [取消折扣申请](post-v1-actions-discounts-task-decline-promos_task_decline.md) - `POST /v1/actions/discounts-task/decline` - `promos_task_decline`
- [申请折扣列表](post-v1-actions-discounts-task-list-promos_task_list.md) - `POST /v1/actions/discounts-task/list` - `promos_task_list`
- [参与 活动的商品列表](post-v1-actions-products-PromosProducts.md) - `POST /v1/actions/products` - `PromosProducts`
- [在促销活动中增加一个商品](post-v1-actions-products-activate-PromosProductsActivate.md) - `POST /v1/actions/products/activate` - `PromosProductsActivate`
- [从活动中删除商品](post-v1-actions-products-deactivate-PromosProductsDeactivate.md) - `POST /v1/actions/products/deactivate` - `PromosProductsDeactivate`
- [获取折扣申请列表](post-v2-actions-discounts-task-list-GetDiscountTaskListV2.md) - `POST /v2/actions/discounts-task/list` - `GetDiscountTaskListV2`

### analytics

- [分析数据](post-v1-analytics-data-AnalyticsAPI_AnalyticsGetData.md) - `POST /v1/analytics/data` - `AnalyticsAPI_AnalyticsGetData`
- [获取商品搜索查询信息](post-v1-analytics-product-queries-AnalyticsAPI_AnalyticsProductQueries.md) - `POST /v1/analytics/product-queries` - `AnalyticsAPI_AnalyticsProductQueries`
- [有关特定商品查询的信息](post-v1-analytics-product-queries-details-AnalyticsAPI_AnalyticsProductQueriesDetails.md) - `POST /v1/analytics/product-queries/details` - `AnalyticsAPI_AnalyticsProductQueriesDetails`

### assembly

- [获取发运中的货件列表](post-v1-assembly-carriage-posting-list-AssemblyCarriagePostingList.md) - `POST /v1/assembly/carriage/posting/list` - `AssemblyCarriagePostingList`
- [获取发运中的商品列表](post-v1-assembly-carriage-product-list-AssemblyCarriageProductList.md) - `POST /v1/assembly/carriage/product/list` - `AssemblyCarriageProductList`
- [获取货件列表](post-v1-assembly-fbs-posting-list-AssemblyFbsPostingList.md) - `POST /v1/assembly/fbs/posting/list` - `AssemblyFbsPostingList`
- [获取货件中的商品列表](post-v1-assembly-fbs-product-list-AssemblyFbsProductList.md) - `POST /v1/assembly/fbs/product/list` - `AssemblyFbsProductList`

### barcode

- [为商品绑定条形码](post-v1-barcode-add-add-barcode.md) - `POST /v1/barcode/add` - `add-barcode`
- [创建商品条形码](post-v1-barcode-generate-generate-barcode.md) - `POST /v1/barcode/generate` - `generate-barcode`

### carriage

- [发运确认](post-v1-carriage-approve-CarriageAPI_CarriageApprove.md) - `POST /v1/carriage/approve` - `CarriageAPI_CarriageApprove`
- [发运删除](post-v1-carriage-cancel-CarriageAPI_CarriageCancel.md) - `POST /v1/carriage/cancel` - `CarriageAPI_CarriageCancel`
- [创建发运](post-v1-carriage-create-CarriageAPI_CarriageCreate.md) - `POST /v1/carriage/create` - `CarriageAPI_CarriageCreate`
- [运输信息](post-v1-carriage-get-CarriageGet.md) - `POST /v1/carriage/get` - `CarriageGet`
- [创建通行证](post-v1-carriage-pass-create-carriagePassCreate.md) - `POST /v1/carriage/pass/create` - `carriagePassCreate`
- [删除通行证](post-v1-carriage-pass-delete-carriagePassDelete.md) - `POST /v1/carriage/pass/delete` - `carriagePassDelete`
- [更新通行证](post-v1-carriage-pass-update-carriagePassUpdate.md) - `POST /v1/carriage/pass/update` - `carriagePassUpdate`
- [发运组成商品更改](post-v1-carriage-set-postings-CarriageAPI_SetPostings.md) - `POST /v1/carriage/set-postings` - `CarriageAPI_SetPostings`

### chat

- [发送文件](post-v1-chat-send-file-ChatAPI_ChatSendFile.md) - `POST /v1/chat/send/file` - `ChatAPI_ChatSendFile`
- [发送信息](post-v1-chat-send-message-ChatAPI_ChatSendMessage.md) - `POST /v1/chat/send/message` - `ChatAPI_ChatSendMessage`
- [创建新聊天](post-v1-chat-start-ChatAPI_ChatStart.md) - `POST /v1/chat/start` - `ChatAPI_ChatStart`
- [将信息标记为已读](post-v2-chat-read-ChatAPI_ChatReadV2.md) - `POST /v2/chat/read` - `ChatAPI_ChatReadV2`
- [聊天历史记录](post-v3-chat-history-ChatAPI_ChatHistoryV3.md) - `POST /v3/chat/history` - `ChatAPI_ChatHistoryV3`
- [聊天清单](post-v3-chat-list-ChatAPI_ChatListV3.md) - `POST /v3/chat/list` - `ChatAPI_ChatListV3`

### conditional-cancellation

- [确认 rFBS 取消申请](post-v2-conditional-cancellation-approve-CancellationAPI_ConditionalCancellationApproveV2.md) - `POST /v2/conditional-cancellation/approve` - `CancellationAPI_ConditionalCancellationApproveV2`
- [获取 rFBS 取消申请列表](post-v2-conditional-cancellation-list-CancellationAPI_GetConditionalCancellationListV2.md) - `POST /v2/conditional-cancellation/list` - `CancellationAPI_GetConditionalCancellationListV2`
- [拒绝 rFBS 取消申请](post-v2-conditional-cancellation-reject-CancellationAPI_ConditionalCancellationRejectV2.md) - `POST /v2/conditional-cancellation/reject` - `CancellationAPI_ConditionalCancellationRejectV2`

### delivery-method

- [仓库物流方式清单](post-v1-delivery-method-list-WarehouseAPI_DeliveryMethodList.md) - `POST /v1/delivery-method/list` - `WarehouseAPI_DeliveryMethodList`
- [realFBS仓库的配送方式列表](post-v2-delivery-method-list-WarehouseAPI_DeliveryMethodListV2.md) - `POST /v2/delivery-method/list` - `WarehouseAPI_DeliveryMethodListV2`

### description-category

- [类别特征列表](post-v1-description-category-attribute-DescriptionCategoryAPI_GetAttributes.md) - `POST /v1/description-category/attribute` - `DescriptionCategoryAPI_GetAttributes`
- [特征值指南](post-v1-description-category-attribute-values-DescriptionCategoryAPI_GetAttributeValues.md) - `POST /v1/description-category/attribute/values` - `DescriptionCategoryAPI_GetAttributeValues`
- [根据属性的参考值进行搜索](post-v1-description-category-attribute-values-search-DescriptionCategoryAPI_SearchAttributeValues.md) - `POST /v1/description-category/attribute/values/search` - `DescriptionCategoryAPI_SearchAttributeValues`
- [获取用于确定商品类目的提示](post-v1-description-category-tips-DescriptionCategoryTips.md) - `POST /v1/description-category/tips` - `DescriptionCategoryTips`
- [商品类别和类型的树形图](post-v1-description-category-tree-DescriptionCategoryAPI_GetTree.md) - `POST /v1/description-category/tree` - `DescriptionCategoryAPI_GetTree`

### fbp

- [生成验收证明书](post-v1-fbp-act-from-create-FbpAPI_FbpCreateAct.md) - `POST /v1/fbp/act-from/create` - `FbpAPI_FbpCreateAct`
- [获取验收证明书生成状态](post-v1-fbp-act-from-get-FbpAPI_FbpCheckActState.md) - `POST /v1/fbp/act-from/get` - `FbpAPI_FbpCheckActState`
- [生成货物运单](post-v1-fbp-act-to-create-FbpAPI_FbpCreateConsignmentNote.md) - `POST /v1/fbp/act-to/create` - `FbpAPI_FbpCreateConsignmentNote`
- [获取货物运单生成状态](post-v1-fbp-act-to-get-FbpAPI_FbpCheckConsignmentNoteState.md) - `POST /v1/fbp/act-to/get` - `FbpAPI_FbpCheckConsignmentNoteState`
- [获取已完成交货信息](post-v1-fbp-archive-get-FbpAPI_FbpArchiveGet.md) - `POST /v1/fbp/archive/get` - `FbpAPI_FbpArchiveGet`
- [获取已完成交货列表](post-v1-fbp-archive-list-FbpAPI_FbpArchiveList.md) - `POST /v1/fbp/archive/list` - `FbpAPI_FbpArchiveList`
- [创建不指定配送方法的交货申请草稿](post-v1-fbp-draft-direct-create-FbpDraftDirectCreate.md) - `POST /v1/fbp/draft/direct/create` - `FbpDraftDirectCreate`
- [删除交货申请草稿](post-v1-fbp-draft-direct-delete-FbpDraftDirectDelete.md) - `POST /v1/fbp/draft/direct/delete` - `FbpDraftDirectDelete`
- [检查合作伙伴仓库商品列表](post-v1-fbp-draft-direct-product-validate-FbpDraftDirectProductValidate.md) - `POST /v1/fbp/draft/direct/product/validate` - `FbpDraftDirectProductValidate`
- [将草稿单转为正式交货](post-v1-fbp-draft-direct-registrate-FbpDraftDirectRegistrate.md) - `POST /v1/fbp/draft/direct/registrate` - `FbpDraftDirectRegistrate`
- [创建由卖家配送的草稿](post-v1-fbp-draft-direct-seller-dlv-create-FbpDraftDirectSellerDlvCreate.md) - `POST /v1/fbp/draft/direct/seller-dlv/create` - `FbpDraftDirectSellerDlvCreate`
- [更新草稿中由卖家配送的信息](post-v1-fbp-draft-direct-seller-dlv-edit-FbpDraftDirectSellerDlvEdit.md) - `POST /v1/fbp/draft/direct/seller-dlv/edit` - `FbpDraftDirectSellerDlvEdit`
- [编辑草稿中的时间段](post-v1-fbp-draft-direct-timeslot-edit-FbpDraftDirectTimeslotEdit.md) - `POST /v1/fbp/draft/direct/timeslot/edit` - `FbpDraftDirectTimeslotEdit`
- [获取直供的时间段列表](post-v1-fbp-draft-direct-timeslot-get-FbpDraftDirectGetTimeslot.md) - `POST /v1/fbp/draft/direct/timeslot/get` - `FbpDraftDirectGetTimeslot`
- [创建第三方物流公司配送的申请草稿](post-v1-fbp-draft-direct-tpl-dlv-create-FbpAPI_FbpDraftDirectTplDlvCreate.md) - `POST /v1/fbp/draft/direct/tpl-dlv/create` - `FbpAPI_FbpDraftDirectTplDlvCreate`
- [编辑采用第三方承运商配送方法的交货草稿](post-v1-fbp-draft-direct-tpl-dlv-edit-FbpAPI_FbpDraftDirectTplDlvEdit.md) - `POST /v1/fbp/draft/direct/tpl-dlv/edit` - `FbpAPI_FbpDraftDirectTplDlvEdit`
- [创建接收点配送草稿](post-v1-fbp-draft-drop-off-create-FbpDraftDropOffCreate.md) - `POST /v1/fbp/draft/drop-off/create` - `FbpDraftDropOffCreate`
- [删除接收点配送草稿](post-v1-fbp-draft-drop-off-delete-FbpDraftDropOffDelete.md) - `POST /v1/fbp/draft/drop-off/delete` - `FbpDraftDropOffDelete`
- [编辑接收点配送草稿的配送详情](post-v1-fbp-draft-drop-off-dlv-edit-FbpDraftDropOffDlvEdit.md) - `POST /v1/fbp/draft/drop-off/dlv/edit` - `FbpDraftDropOffDlvEdit`
- [获取省份内接收点列表](post-v1-fbp-draft-drop-off-point-list-FbpDraftDropOffPointList.md) - `POST /v1/fbp/draft/drop-off/point/list` - `FbpDraftDropOffPointList`
- [获取接收点的营业时间表](post-v1-fbp-draft-drop-off-point-timetable-FbpDraftDropOffPointTimetable.md) - `POST /v1/fbp/draft/drop-off/point/timetable` - `FbpDraftDropOffPointTimetable`
- [检查合作伙伴仓库可接收的商品列表](post-v1-fbp-draft-drop-off-product-validate-FbpDraftDropOffProductValidate.md) - `POST /v1/fbp/draft/drop-off/product/validate` - `FbpDraftDropOffProductValidate`
- [获取省份列表](post-v1-fbp-draft-drop-off-province-list-FbpDraftDropOffProvinceList.md) - `POST /v1/fbp/draft/drop-off/province/list` - `FbpDraftDropOffProvinceList`
- [将草稿转为正式交货](post-v1-fbp-draft-drop-off-registrate-FbpDraftDropOffRegistrate.md) - `POST /v1/fbp/draft/drop-off/registrate` - `FbpDraftDropOffRegistrate`
- [获取交货草稿信息](post-v1-fbp-draft-get-FbpAPI_FbpDraftGet.md) - `POST /v1/fbp/draft/get` - `FbpAPI_FbpDraftGet`
- [交货草稿列表](post-v1-fbp-draft-list-FbpAPI_FbpDraftList.md) - `POST /v1/fbp/draft/list` - `FbpAPI_FbpDraftList`
- [创建 pick-up 交货申请草稿](post-v1-fbp-draft-pick-up-create-FbpAPI_FbpDraftPickupCreate.md) - `POST /v1/fbp/draft/pick-up/create` - `FbpAPI_FbpDraftPickupCreate`
- [取消 pick-up 交货申请草稿](post-v1-fbp-draft-pick-up-delete-FbpAPI_FbpDraftPickUpDelete.md) - `POST /v1/fbp/draft/pick-up/delete` - `FbpAPI_FbpDraftPickUpDelete`
- [修改 pick-up 交货申请](post-v1-fbp-draft-pick-up-dlv-edit-FbpAPI_FbpDraftPickupDlvEdit.md) - `POST /v1/fbp/draft/pick-up/dlv/edit` - `FbpAPI_FbpDraftPickupDlvEdit`
- [验证用于 pick-up 交货的商品列表](post-v1-fbp-draft-pick-up-product-validate-FbpAPI_FbpDraftPickUpProductValidate.md) - `POST /v1/fbp/draft/pick-up/product/validate` - `FbpAPI_FbpDraftPickUpProductValidate`
- [将草稿单转为正式交货](post-v1-fbp-draft-pick-up-registrate-FbpDraftPickUpRegistrate.md) - `POST /v1/fbp/draft/pick-up/registrate` - `FbpDraftPickUpRegistrate`
- [创建标签生成任务](post-v1-fbp-label-create-FbpAPI_FbpCreateLabel.md) - `POST /v1/fbp/label/create` - `FbpAPI_FbpCreateLabel`
- [获取标签生成任务状态](post-v1-fbp-label-get-FbpAPI_FbpGetLabel.md) - `POST /v1/fbp/label/get` - `FbpAPI_FbpGetLabel`
- [取消交货](post-v1-fbp-order-direct-cancel-FbpAPI_FbpOrderDirectCancel.md) - `POST /v1/fbp/order/direct/cancel` - `FbpAPI_FbpOrderDirectCancel`
- [更新卖家自配送信息](post-v1-fbp-order-direct-seller-dlv-edit-FbpAPI_FbpOrderDirectSellerDlvEdit.md) - `POST /v1/fbp/order/direct/seller-dlv/edit` - `FbpAPI_FbpOrderDirectSellerDlvEdit`
- [编辑交货申请中的时间段](post-v1-fbp-order-direct-timeslot-edit-FbpAPI_FbpEditTimeslot.md) - `POST /v1/fbp/order/direct/timeslot/edit` - `FbpAPI_FbpEditTimeslot`
- [获取交货时间段列表](post-v1-fbp-order-direct-timeslot-list-FbpAPI_FbpAvailableTimeslotList.md) - `POST /v1/fbp/order/direct/timeslot/list` - `FbpAPI_FbpAvailableTimeslotList`
- [取消 drop-off 交货](post-v1-fbp-order-drop-off-cancel-FbpAPI_FbpOrderDropOffCancel.md) - `POST /v1/fbp/order/drop-off/cancel` - `FbpAPI_FbpOrderDropOffCancel`
- [编辑收货点的送货信息](post-v1-fbp-order-drop-off-dlv-edit-FbpAPI_FbpOrderDropOffDlvEdit.md) - `POST /v1/fbp/order/drop-off/dlv/edit` - `FbpAPI_FbpOrderDropOffDlvEdit`
- [获取接收点的营业时间表](post-v1-fbp-order-drop-off-timetable-FbpAPI_FbpOrderDropOffTimetable.md) - `POST /v1/fbp/order/drop-off/timetable` - `FbpAPI_FbpOrderDropOffTimetable`
- [获取关于特定交货的信息](post-v1-fbp-order-get-FbpAPI_FbpOrderGet.md) - `POST /v1/fbp/order/get` - `FbpAPI_FbpOrderGet`
- [获取交货列表](post-v1-fbp-order-list-FbpAPI_FbpOrderList.md) - `POST /v1/fbp/order/list` - `FbpAPI_FbpOrderList`
- [取消上门揽收交货](post-v1-fbp-order-pick-up-cancel-FbpAPI_FbpOrderPickUpCancel.md) - `POST /v1/fbp/order/pick-up/cancel` - `FbpAPI_FbpOrderPickUpCancel`
- [更改取货地点信息](post-v1-fbp-order-pick-up-dlv-edit-FbpAPI_FbpOrderPickUpDlvEdit.md) - `POST /v1/fbp/order/pick-up/dlv/edit` - `FbpAPI_FbpOrderPickUpDlvEdit`
- [获取合作伙伴仓库列表](post-v1-fbp-warehouse-list-FbpWarehouseList.md) - `POST /v1/fbp/warehouse/list` - `FbpWarehouseList`

### fbs

- [Обновить данные экземпляров](post-v1-fbs-posting-product-exemplar-update-PostingAPI_FbsPostingProductExemplarUpdate.md) - `POST /v1/fbs/posting/product/exemplar/update` - `PostingAPI_FbsPostingProductExemplarUpdate`
- [将状态改成“已送达”](post-v2-fbs-posting-delivered-PostingAPI_FbsPostingDelivered.md) - `POST /v2/fbs/posting/delivered` - `PostingAPI_FbsPostingDelivered`
- [将状态改成“运输中”](post-v2-fbs-posting-delivering-PostingAPI_FbsPostingDelivering.md) - `POST /v2/fbs/posting/delivering` - `PostingAPI_FbsPostingDelivering`
- [状态改为“最后一英里”](post-v2-fbs-posting-last-mile-PostingAPI_FbsPostingLastMile.md) - `POST /v2/fbs/posting/last-mile` - `PostingAPI_FbsPostingLastMile`
- [添加跟踪号](post-v2-fbs-posting-tracking-number-set-PostingAPI_FbsPostingTrackingNumberSet.md) - `POST /v2/fbs/posting/tracking-number/set` - `PostingAPI_FbsPostingTrackingNumberSet`
- [获取样件添加状态](post-v5-fbs-posting-product-exemplar-status-PostingAPI_FbsPostingProductExemplarStatusV5.md) - `POST /v5/fbs/posting/product/exemplar/status` - `PostingAPI_FbsPostingProductExemplarStatusV5`
- [标志代码验证](post-v5-fbs-posting-product-exemplar-validate-PostingAPI_FbsPostingProductExemplarValidateV5.md) - `POST /v5/fbs/posting/product/exemplar/validate` - `PostingAPI_FbsPostingProductExemplarValidateV5`
- [获取已创建样件数据](post-v6-fbs-posting-product-exemplar-create-or-get-PostingAPI_FbsPostingProductExemplarCreateOrGetV6.md) - `POST /v6/fbs/posting/product/exemplar/create-or-get` - `PostingAPI_FbsPostingProductExemplarCreateOrGetV6`
- [检查并保存份数数据](post-v6-fbs-posting-product-exemplar-set-PostingAPI_FbsPostingProductExemplarSetV6.md) - `POST /v6/fbs/posting/product/exemplar/set` - `PostingAPI_FbsPostingProductExemplarSetV6`

### finance

- [获取某日应计项目](post-v1-finance-accrual-by-day-GetFinanceAccrualByDay.md) - `POST /v1/finance/accrual/by-day` - `GetFinanceAccrualByDay`
- [获取按货件统计的应计项目](post-v1-finance-accrual-postings-GetFinanceAccrualPostings.md) - `POST /v1/finance/accrual/postings` - `GetFinanceAccrualPostings`
- [获取应计项目参考信息](post-v1-finance-accrual-types-GetFinanceAccrualTypes.md) - `POST /v1/finance/accrual/types` - `GetFinanceAccrualTypes`
- [获取余额报告](post-v1-finance-balance-GetFinanceBalanceV1.md) - `POST /v1/finance/balance` - `GetFinanceBalanceV1`
- [财务报告](post-v1-finance-cash-flow-statement-list-FinanceAPI_FinanceCashFlowStatementList.md) - `POST /v1/finance/cash-flow-statement/list` - `FinanceAPI_FinanceCashFlowStatementList`
- [赔偿报告](post-v1-finance-compensation-ReportAPI_GetCompensationReport.md) - `POST /v1/finance/compensation` - `ReportAPI_GetCompensationReport`
- [赔偿返还报告](post-v1-finance-decompensation-ReportAPI_GetDecompensationReport.md) - `POST /v1/finance/decompensation` - `ReportAPI_GetDecompensationReport`
- [每日商品销售报告](post-v1-finance-realization-by-day-FinanceAPI_GetRealizationByDayReportV1.md) - `POST /v1/finance/realization/by-day` - `FinanceAPI_GetRealizationByDayReportV1`
- [按订单细分的商品销售报告](post-v1-finance-realization-posting-FinanceAPI_GetRealizationReportV1.md) - `POST /v1/finance/realization/posting` - `FinanceAPI_GetRealizationReportV1`
- [商品销售报告 （第2版）](post-v2-finance-realization-FinanceAPI_GetRealizationReportV2.md) - `POST /v2/finance/realization` - `FinanceAPI_GetRealizationReportV2`
- [交易清单](post-v3-finance-transaction-list-FinanceAPI_FinanceTransactionListV3.md) - `POST /v3/finance/transaction/list` - `FinanceAPI_FinanceTransactionListV3`
- [清单数目](post-v3-finance-transaction-totals-FinanceAPI_FinanceTransactionTotalV3.md) - `POST /v3/finance/transaction/totals` - `FinanceAPI_FinanceTransactionTotalV3`

### pass

- [通行证列表](post-v1-pass-list-PassList.md) - `POST /v1/pass/list` - `PassList`

### polygon

- [将快递方式与快递设施联系起来](post-v1-polygon-bind-PolygonAPI_BindPolygon.md) - `POST /v1/polygon/bind` - `PolygonAPI_BindPolygon`
- [创建一个快递的设施](post-v1-polygon-create-PolygonAPI_CreatePolygon.md) - `POST /v1/polygon/create` - `PolygonAPI_CreatePolygon`

### posting

- [可供运输的列表](post-v1-posting-carriage-available-list-PostingAPI_GetCarriageAvailableList.md) - `POST /v1/posting/carriage-available/list` - `PostingAPI_GetCarriageAvailableList`
- [确认货件发运日期](post-v1-posting-cutoff-set-PostingAPI_SetPostingCutoff.md) - `POST /v1/posting/cutoff/set` - `PostingAPI_SetPostingCutoff`
- [按标识符获取货件信息](post-v1-posting-fbp-get-GetFbpPosting.md) - `POST /v1/posting/fbp/get` - `GetFbpPosting`
- [获取货件列表](post-v1-posting-fbp-list-PostingFbpList.md) - `POST /v1/posting/fbp/list` - `PostingFbpList`
- [货运取消原因](post-v1-posting-fbs-cancel-reason-PostingAPI_GetPostingFbsCancelReasonV1.md) - `POST /v1/posting/fbs/cancel-reason` - `PostingAPI_GetPostingFbsCancelReasonV1`
- [将订单拆分为不带备货的货件](post-v1-posting-fbs-split-FbsSplit.md) - `POST /v1/posting/fbs/split` - `FbsSplit`
- [货位标签](post-v2-posting-fbs-act-get-container-labels-PostingAPI_PostingFBSActGetContainerLabels.md) - `POST /v2/posting/fbs/act/get-container-labels` - `PostingAPI_PostingFBSActGetContainerLabels`
- [单据中的货件列表](post-v2-posting-fbs-act-get-postings-PostingAPI_ActPostingList.md) - `POST /v2/posting/fbs/act/get-postings` - `PostingAPI_ActPostingList`
- [货件装运](post-v2-posting-fbs-awaiting-delivery-PostingAPI_MoveFbsPostingToAwaitingDelivery.md) - `POST /v2/posting/fbs/awaiting-delivery` - `PostingAPI_MoveFbsPostingToAwaitingDelivery`
- [取消货运](post-v2-posting-fbs-cancel-PostingAPI_CancelFbsPosting.md) - `POST /v2/posting/fbs/cancel` - `PostingAPI_CancelFbsPosting`
- [货件取消原因](post-v2-posting-fbs-cancel-reason-list-PostingAPI_GetPostingFbsCancelReasonList.md) - `POST /v2/posting/fbs/cancel-reason/list` - `PostingAPI_GetPostingFbsCancelReasonList`
- [按条形码获取有关货件的信息](post-v2-posting-fbs-get-by-barcode-PostingAPI_GetFbsPostingByBarcode.md) - `POST /v2/posting/fbs/get-by-barcode` - `PostingAPI_GetFbsPostingByBarcode`
- [打印标签](post-v2-posting-fbs-package-label-PostingAPI_PostingFBSPackageLabel.md) - `POST /v2/posting/fbs/package-label` - `PostingAPI_PostingFBSPackageLabel`
- [取消某些商品发货](post-v2-posting-fbs-product-cancel-PostingAPI_CancelFbsPostingProduct.md) - `POST /v2/posting/fbs/product/cancel` - `PostingAPI_CancelFbsPostingProduct`
- [可用产地名单](post-v2-posting-fbs-product-country-list-PostingAPI_ListCountryProductFbsPostingV2.md) - `POST /v2/posting/fbs/product/country/list` - `PostingAPI_ListCountryProductFbsPostingV2`
- [添加商品产地信息](post-v2-posting-fbs-product-country-set-PostingAPI_SetCountryProductFbsPostingV2.md) - `POST /v2/posting/fbs/product/country/set` - `PostingAPI_SetCountryProductFbsPostingV2`
- [按照ID获取货件信息](post-v3-posting-fbs-get-PostingAPI_GetFbsPostingV3.md) - `POST /v3/posting/fbs/get` - `PostingAPI_GetFbsPostingV3`
- [货件列表 Deprecated](post-v3-posting-fbs-list-PostingAPI_GetFbsPostingListV3.md) - `POST /v3/posting/fbs/list` - `PostingAPI_GetFbsPostingListV3`
- [未处理货件列表 Deprecated](post-v3-posting-fbs-unfulfilled-list-PostingAPI_GetFbsPostingUnfulfilledList.md) - `POST /v3/posting/fbs/unfulfilled/list` - `PostingAPI_GetFbsPostingUnfulfilledList`
- [获取货件列表](post-v4-posting-fbs-list-PostingFbsList.md) - `POST /v4/posting/fbs/list` - `PostingFbsList`
- [搜集订单 (第4方案)](post-v4-posting-fbs-ship-PostingAPI_ShipFbsPostingV4.md) - `POST /v4/posting/fbs/ship` - `PostingAPI_ShipFbsPostingV4`
- [货件的部分装配 (第4方案)](post-v4-posting-fbs-ship-package-PostingAPI_ShipFbsPostingPackage.md) - `POST /v4/posting/fbs/ship/package` - `PostingAPI_ShipFbsPostingPackage`
- [获取未处理货件列表](post-v4-posting-fbs-unfulfilled-list-PostingFbsUnfulfilledList.md) - `POST /v4/posting/fbs/unfulfilled/list` - `PostingFbsUnfulfilledList`

### pricing-strategy

- [竞争对手名单](post-v1-pricing-strategy-competitors-list-pricing_competitors.md) - `POST /v1/pricing-strategy/competitors/list` - `pricing_competitors`
- [创建策略](post-v1-pricing-strategy-create-pricing_create.md) - `POST /v1/pricing-strategy/create` - `pricing_create`
- [删除策略](post-v1-pricing-strategy-delete-pricing_delete.md) - `POST /v1/pricing-strategy/delete` - `pricing_delete`
- [策略信息](post-v1-pricing-strategy-info-pricing_info.md) - `POST /v1/pricing-strategy/info` - `pricing_info`
- [策略列表](post-v1-pricing-strategy-list-pricing_list.md) - `POST /v1/pricing-strategy/list` - `pricing_list`
- [竞争对手 的商品价格](post-v1-pricing-strategy-product-info-pricing_items-info.md) - `POST /v1/pricing-strategy/product/info` - `pricing_items-info`
- [将商品添加到策略](post-v1-pricing-strategy-products-add-pricing_items-add.md) - `POST /v1/pricing-strategy/products/add` - `pricing_items-add`
- [从策略中删除商品](post-v1-pricing-strategy-products-delete-pricing_items-delete.md) - `POST /v1/pricing-strategy/products/delete` - `pricing_items-delete`
- [策略中的商品列表](post-v1-pricing-strategy-products-list-pricing_items-list.md) - `POST /v1/pricing-strategy/products/list` - `pricing_items-list`
- [更改策略状态](post-v1-pricing-strategy-status-pricing_status.md) - `POST /v1/pricing-strategy/status` - `pricing_status`
- [策略ID列表](post-v1-pricing-strategy-strategy-ids-by-product-ids-pricing_ids.md) - `POST /v1/pricing-strategy/strategy-ids-by-product-ids` - `pricing_ids`
- [更新策略](post-v1-pricing-strategy-update-pricing_update.md) - `POST /v1/pricing-strategy/update` - `pricing_update`

### product

- [获取已设置计时器状态](post-v1-product-action-timer-status-ProductAPI_ActionTimerStatus.md) - `POST /v1/product/action/timer/status` - `ProductAPI_ActionTimerStatus`
- [最低价格时效性计时器更新](post-v1-product-action-timer-update-ProductAPI_ActionTimerUpdate.md) - `POST /v1/product/action/timer/update` - `ProductAPI_ActionTimerUpdate`
- [将商品归档](post-v1-product-archive-ProductAPI_ProductArchive.md) - `POST /v1/product/archive` - `ProductAPI_ProductArchive`
- [更新商品特征](post-v1-product-attributes-update-ProductAPI_ProductUpdateAttributes.md) - `POST /v1/product/attributes/update` - `ProductAPI_ProductUpdateAttributes`
- [通过SKU创建商品](post-v1-product-import-by-sku-ProductAPI_ImportProductsBySKU.md) - `POST /v1/product/import-by-sku` - `ProductAPI_ImportProductsBySKU`
- [查询商品添加或更新状态](post-v1-product-import-info-ProductAPI_GetImportProductsInfo.md) - `POST /v1/product/import/info` - `ProductAPI_GetImportProductsInfo`
- [更新价格](post-v1-product-import-prices-ProductAPI_ImportProductsPrices.md) - `POST /v1/product/import/prices` - `ProductAPI_ImportProductsPrices`
- [获取商品详细信息](post-v1-product-info-description-ProductAPI_GetProductInfoDescription.md) - `POST /v1/product/info/description` - `ProductAPI_GetProductInfoDescription`
- [通过减价商品的SKU查找减价商品和主商品的信息](post-v1-product-info-discounted-ProductAPI_GetProductInfoDiscounted.md) - `POST /v1/product/info/discounted` - `ProductAPI_GetProductInfoDiscounted`
- [关于卖家库存余额的信息](post-v1-product-info-stocks-by-warehouse-fbs-ProductAPI_ProductStocksByWarehouseFbs.md) - `POST /v1/product/info/stocks-by-warehouse/fbs` - `ProductAPI_ProductStocksByWarehouseFbs`
- [订阅该商品的用户数](post-v1-product-info-subscription-ProductAPI_GetProductInfoSubscription.md) - `POST /v1/product/info/subscription` - `ProductAPI_GetProductInfoSubscription`
- [获取FBS和rFBS仓库库存信息](post-v1-product-info-warehouse-stocks-ProductInfoWarehouseStocks.md) - `POST /v1/product/info/warehouse/stocks` - `ProductInfoWarehouseStocks`
- [体积重量特征不正确的商品列表](post-v1-product-info-wrong-volume-ProductAPI_ProductInfoWrongVolume.md) - `POST /v1/product/info/wrong-volume` - `ProductAPI_ProductInfoWrongVolume`
- [上传或更新商品图片](post-v1-product-pictures-import-ProductAPI_ProductImportPictures.md) - `POST /v1/product/pictures/import` - `ProductAPI_ProductImportPictures`
- [获取商品价格的详细信息](post-v1-product-prices-details-ProductPricesDetails.md) - `POST /v1/product/prices/details` - `ProductPricesDetails`
- [按SKU获得商品的内容排名](post-v1-product-rating-by-sku-ProductAPI_GetProductRatingBySku.md) - `POST /v1/product/rating-by-sku` - `ProductAPI_GetProductRatingBySku`
- [获取相关SKU](post-v1-product-related-sku-get-ProductAPI_ProductGetRelatedSKU.md) - `POST /v1/product/related-sku/get` - `ProductAPI_ProductGetRelatedSKU`
- [获取按数量折扣信息](post-v1-product-stairway-discount-by-quantity-get-ProductAPI_GetProductStairwayDiscountByQuantity.md) - `POST /v1/product/stairway-discount/by-quantity/get` - `ProductAPI_GetProductStairwayDiscountByQuantity`
- [管理按数量折扣](post-v1-product-stairway-discount-by-quantity-set-ProductAPI_SetProductStairwayDiscountByQuantity.md) - `POST /v1/product/stairway-discount/by-quantity/set` - `ProductAPI_SetProductStairwayDiscountByQuantity`
- [从档案中还原商品](post-v1-product-unarchive-ProductAPI_ProductUnarchive.md) - `POST /v1/product/unarchive` - `ProductAPI_ProductUnarchive`
- [为打折商品设置折扣](post-v1-product-update-discount-ProductAPI_ProductUpdateDiscount.md) - `POST /v1/product/update/discount` - `ProductAPI_ProductUpdateDiscount`
- [从卖家的系统中改变商品货号](post-v1-product-update-offer-id-ProductAPI_ProductUpdateOfferID.md) - `POST /v1/product/update/offer-id` - `ProductAPI_ProductUpdateOfferID`
- [获取商品可见性信息](post-v1-product-visibility-info-ProductVisibilityInfo.md) - `POST /v1/product/visibility/info` - `ProductVisibilityInfo`
- [新增了用于设置商品在Ozon和Ozon Select橱窗可见性的Beta方法。](post-v1-product-visibility-set-ProductVisibilitySet.md) - `POST /v1/product/visibility/set` - `ProductVisibilitySet`
- [获取卖家仓库库存信息](post-v2-product-info-stocks-by-warehouse-fbs-GetProductInfoStocksByWarehouseFbsV2.md) - `POST /v2/product/info/stocks-by-warehouse/fbs` - `GetProductInfoStocksByWarehouseFbsV2`
- [获取商品图片](post-v2-product-pictures-info-ProductAPI_ProductInfoPicturesV2.md) - `POST /v2/product/pictures/info` - `ProductAPI_ProductInfoPicturesV2`
- [创建或更新商品](post-v3-product-import-ProductAPI_ImportProductsV3.md) - `POST /v3/product/import` - `ProductAPI_ImportProductsV3`
- [根据标识符获取商品信息](post-v3-product-info-list-ProductAPI_GetProductInfoList.md) - `POST /v3/product/info/list` - `ProductAPI_GetProductInfoList`
- [品列表的](post-v3-product-list-ProductAPI_GetProductList.md) - `POST /v3/product/list` - `ProductAPI_GetProductList`
- [获取商品特征描述](post-v4-product-info-attributes-ProductAPI_GetProductAttributesV4.md) - `POST /v4/product/info/attributes` - `ProductAPI_GetProductAttributesV4`
- [品类限制、商品的创建和更新](post-v4-product-info-limit-ProductAPI_GetUploadQuota.md) - `POST /v4/product/info/limit` - `ProductAPI_GetUploadQuota`
- [关于商品数量的信息](post-v4-product-info-stocks-ProductAPI_GetProductInfoStocks.md) - `POST /v4/product/info/stocks` - `ProductAPI_GetProductInfoStocks`
- [获取商品价格信息](post-v5-product-info-prices-ProductAPI_GetProductInfoPrices.md) - `POST /v5/product/info/prices` - `ProductAPI_GetProductInfoPrices`

### products

- [从存档删除没有SKU的商品](post-v2-products-delete-ProductAPI_DeleteProducts.md) - `POST /v2/products/delete` - `ProductAPI_DeleteProducts`
- [更新库存商品的数量](post-v2-products-stocks-ProductAPI_ProductsStocksV2.md) - `POST /v2/products/stocks` - `ProductAPI_ProductsStocksV2`
- [获取商品特征描述](post-v3-products-info-attributes-ProductAPI_GetProductAttributesV3.md) - `POST /v3/products/info/attributes` - `ProductAPI_GetProductAttributesV3`

### question

- [创建对问题的回答](post-v1-question-answer-create-QuestionAnswer_Create.md) - `POST /v1/question/answer/create` - `QuestionAnswer_Create`
- [删除问题回答](post-v1-question-answer-delete-QuestionAnswer_Delete.md) - `POST /v1/question/answer/delete` - `QuestionAnswer_Delete`
- [问题回答列表](post-v1-question-answer-list-QuestionAnswer_List.md) - `POST /v1/question/answer/list` - `QuestionAnswer_List`
- [更改问题状态](post-v1-question-change_status-Question_ChangeStatus.md) - `POST /v1/question/change_status` - `Question_ChangeStatus`
- [按状态统计问题数量](post-v1-question-count-Question_Count.md) - `POST /v1/question/count` - `Question_Count`
- [问题详情](post-v1-question-info-Question_Info.md) - `POST /v1/question/info` - `Question_Info`
- [问题列表](post-v1-question-list-Question_List.md) - `POST /v1/question/list` - `Question_List`
- [提问数量最多的商品](post-v1-question-top-sku-Question_TopSku.md) - `POST /v1/question/top-sku` - `Question_TopSku`

### rating

- [获取错误指数：FBS 和 rFBS](post-v1-rating-index-fbs-info-RatingAPI_GetFBSRatingIndexInfoV1.md) - `POST /v1/rating/index/fbs/info` - `RatingAPI_GetFBSRatingIndexInfoV1`
- [影响错误指数的货件列表：FBS 和 rFBS](post-v1-rating-index-fbs-posting-list-RatingAPI_ListFBSRatingIndexPostingsV1.md) - `POST /v1/rating/index/fbs/posting/list` - `RatingAPI_ListFBSRatingIndexPostingsV1`

### report

- [减价商品报告](post-v1-report-discounted-create-ReportAPI_CreateDiscountedReport.md) - `POST /v1/report/discounted/create` - `ReportAPI_CreateDiscountedReport`
- [报告信息](post-v1-report-info-ReportAPI_ReportInfo.md) - `POST /v1/report/info` - `ReportAPI_ReportInfo`
- [报告清单](post-v1-report-list-ReportAPI_ReportList.md) - `POST /v1/report/list` - `ReportAPI_ReportList`
- [生成带有标记商品的销售报告](post-v1-report-marked-products-sales-create-CreateCompanyMarkedProductsSalesReport.md) - `POST /v1/report/marked-products-sales/create` - `CreateCompanyMarkedProductsSalesReport`
- [发货报告](post-v1-report-postings-create-ReportAPI_CreateCompanyPostingsReport.md) - `POST /v1/report/postings/create` - `ReportAPI_CreateCompanyPostingsReport`
- [商品报告](post-v1-report-products-create-ReportAPI_CreateCompanyProductsReport.md) - `POST /v1/report/products/create` - `ReportAPI_CreateCompanyProductsReport`
- [关于FBS仓库库存报告](post-v1-report-warehouse-stock-ReportAPI_CreateStockByWarehouseReport.md) - `POST /v1/report/warehouse/stock` - `ReportAPI_CreateStockByWarehouseReport`

### return

- [创建退货通行证](post-v1-return-pass-create-returnPassCreate.md) - `POST /v1/return/pass/create` - `returnPassCreate`
- [删除退货通行证](post-v1-return-pass-delete-returnPassDelete.md) - `POST /v1/return/pass/delete` - `returnPassDelete`
- [更新退货通行证](post-v1-return-pass-update-returnPassUpdate.md) - `POST /v1/return/pass/update` - `returnPassUpdate`

### returns

- [FBS退货数量](post-v1-returns-company-fbs-info-returnsCompanyFBSInfo.md) - `POST /v1/returns/company/fbs/info` - `returnsCompanyFBSInfo`
- [FBO和FBS退货信息](post-v1-returns-list-returnsList.md) - `POST /v1/returns/list` - `returnsList`
- [传递 rFBS 退货的可用操作](post-v1-returns-rfbs-action-set-ReturnsAPI_ReturnsRfbsActionSet.md) - `POST /v1/returns/rfbs/action/set` - `ReturnsAPI_ReturnsRfbsActionSet`
- [退还部分商品金额](post-v2-returns-rfbs-compensate-RFBSReturnsAPI_ReturnsRfbsCompensateV2.md) - `POST /v2/returns/rfbs/compensate` - `RFBSReturnsAPI_ReturnsRfbsCompensateV2`
- [退货申请信息](post-v2-returns-rfbs-get-RFBSReturnsAPI_ReturnsRfbsGetV2.md) - `POST /v2/returns/rfbs/get` - `RFBSReturnsAPI_ReturnsRfbsGetV2`
- [退货申请列表](post-v2-returns-rfbs-list-RFBSReturnsAPI_ReturnsRfbsListV2.md) - `POST /v2/returns/rfbs/list` - `RFBSReturnsAPI_ReturnsRfbsListV2`
- [确认收到待检查商品](post-v2-returns-rfbs-receive-return-RFBSReturnsAPI_ReturnsRfbsReceiveReturnV2.md) - `POST /v2/returns/rfbs/receive-return` - `RFBSReturnsAPI_ReturnsRfbsReceiveReturnV2`
- [拒绝退货申请](post-v2-returns-rfbs-reject-RFBSReturnsAPI_ReturnsRfbsRejectV2.md) - `POST /v2/returns/rfbs/reject` - `RFBSReturnsAPI_ReturnsRfbsRejectV2`
- [向买家退款](post-v2-returns-rfbs-return-money-RFBSReturnsAPI_ReturnsRfbsReturnMoneyV2.md) - `POST /v2/returns/rfbs/return-money` - `RFBSReturnsAPI_ReturnsRfbsReturnMoneyV2`
- [批准退货申请](post-v2-returns-rfbs-verify-RFBSReturnsAPI_ReturnsRfbsVerifyV2.md) - `POST /v2/returns/rfbs/verify` - `RFBSReturnsAPI_ReturnsRfbsVerifyV2`

### review

- [更改评价状态](post-v1-review-change-status-ReviewAPI_ReviewChangeStatus.md) - `POST /v1/review/change-status` - `ReviewAPI_ReviewChangeStatus`
- [对评价留下评论](post-v1-review-comment-create-ReviewAPI_CommentCreate.md) - `POST /v1/review/comment/create` - `ReviewAPI_CommentCreate`
- [删除对评价的评论](post-v1-review-comment-delete-ReviewAPI_CommentDelete.md) - `POST /v1/review/comment/delete` - `ReviewAPI_CommentDelete`
- [评价的评论列表](post-v1-review-comment-list-ReviewAPI_CommentList.md) - `POST /v1/review/comment/list` - `ReviewAPI_CommentList`
- [根据状态统计的评价数量](post-v1-review-count-ReviewAPI_ReviewCount.md) - `POST /v1/review/count` - `ReviewAPI_ReviewCount`
- [获取评价信息](post-v1-review-info-ReviewAPI_ReviewInfo.md) - `POST /v1/review/info` - `ReviewAPI_ReviewInfo`
- [获取评价列表 Deprecated](post-v1-review-list-ReviewAPI_ReviewList.md) - `POST /v1/review/list` - `ReviewAPI_ReviewList`
- [获取评价列表](post-v2-review-list-ReviewListV2.md) - `POST /v2/review/list` - `ReviewListV2`

### roles

- [使用API密钥获取角色和方式列表](post-v1-roles-AccessAPI_RolesByToken.md) - `POST /v1/roles` - `AccessAPI_RolesByToken`

### search-queries

- [获取按文本筛选的搜索查询列表](post-v1-search-queries-text-SearchQueriesAPI_SearchQueriesText.md) - `POST /v1/search-queries/text` - `SearchQueriesAPI_SearchQueriesText`
- [获取热门搜索查询列表](post-v1-search-queries-top-SearchQueriesAPI_SearchQueriesTop.md) - `POST /v1/search-queries/top` - `SearchQueriesAPI_SearchQueriesTop`

### seller

- [卖家个人中心信息](post-v1-seller-info-SellerAPI_SellerInfo.md) - `POST /v1/seller/info` - `SellerAPI_SellerInfo`
- [Ozon配送开通信息](post-v1-seller-ozon-logistics-info-SellerAPI_SellerOzonLogisticsInfo.md) - `POST /v1/seller/ozon-logistics/info` - `SellerAPI_SellerOzonLogisticsInfo`

### seller-actions

- [将促销活动归档](post-v1-seller-actions-archive-SellerActionsArchive.md) - `POST /v1/seller-actions/archive` - `SellerActionsArchive`
- [启用或关闭活动](post-v1-seller-actions-change-activity-SellerActionsChangeActivity.md) - `POST /v1/seller-actions/change-activity` - `SellerActionsChangeActivity`
- [创建采用"折扣"机制的促销活动](post-v1-seller-actions-create-discount-SellerActionsCreateDiscount.md) - `POST /v1/seller-actions/create/discount` - `SellerActionsCreateDiscount`
- [创建采用"基于订单总额的折扣"机制的促销活动](post-v1-seller-actions-create-discount-with-condition-SellerActionsCreateDiscountWithCondition.md) - `POST /v1/seller-actions/create/discount-with-condition` - `SellerActionsCreateDiscountWithCondition`
- [创建采用"免息分期付款"机制的促销活动](post-v1-seller-actions-create-installment-SellerActionsCreateInstallment.md) - `POST /v1/seller-actions/create/installment` - `SellerActionsCreateInstallment`
- [创建采用"多级满额折扣"机制的促销活动](post-v1-seller-actions-create-multi-level-discount-SellerActionsCreateMultiLevelDiscount.md) - `POST /v1/seller-actions/create/multi-level-discount` - `SellerActionsCreateMultiLevelDiscount`
- [创建采用"促销码折扣"机制的促销活动](post-v1-seller-actions-create-voucher-SellerActionsCreateVoucher.md) - `POST /v1/seller-actions/create/voucher` - `SellerActionsCreateVoucher`
- [获取促销活动列表](post-v1-seller-actions-list-SellerActionsList.md) - `POST /v1/seller-actions/list` - `SellerActionsList`
- [将商品添加到促销活动中](post-v1-seller-actions-products-add-SellerActionsProductsAdd.md) - `POST /v1/seller-actions/products/add` - `SellerActionsProductsAdd`
- [获取促销活动可用商品列表](post-v1-seller-actions-products-candidates-SellerActionsProductsCandidates.md) - `POST /v1/seller-actions/products/candidates` - `SellerActionsProductsCandidates`
- [从促销活动中移除商品](post-v1-seller-actions-products-delete-SellerActionsProductsDelete.md) - `POST /v1/seller-actions/products/delete` - `SellerActionsProductsDelete`
- [获取参与活动的商品列表](post-v1-seller-actions-products-list-SellerActionsProductsList.md) - `POST /v1/seller-actions/products/list` - `SellerActionsProductsList`
- [更新“折扣”机制的促销活动](post-v1-seller-actions-update-discount-SellerActionsUpdateDiscount.md) - `POST /v1/seller-actions/update/discount` - `SellerActionsUpdateDiscount`
- [更新“基于订单总额的折扣”机制的促销活动](post-v1-seller-actions-update-discount-with-condition-SellerActionsUpdateDiscountWithCondition.md) - `POST /v1/seller-actions/update/discount-with-condition` - `SellerActionsUpdateDiscountWithCondition`
- [更新“免息分期付款”机制的促销活动](post-v1-seller-actions-update-installment-SellerActionsUpdateInstallment.md) - `POST /v1/seller-actions/update/installment` - `SellerActionsUpdateInstallment`
- [更新“多级满额折扣”机制的促销活动](post-v1-seller-actions-update-multi-level-discount-SellerActionsUpdateMultiLevelDiscount.md) - `POST /v1/seller-actions/update/multi-level-discount` - `SellerActionsUpdateMultiLevelDiscount`
- [更新“促销码折扣”机制的促销活动](post-v1-seller-actions-update-voucher-SellerActionsUpdateVoucher.md) - `POST /v1/seller-actions/update/voucher` - `SellerActionsUpdateVoucher`
- [获取CSV格式的促销码文件](post-v1-seller-actions-voucher-get-SellerActionsVoucherGet.md) - `POST /v1/seller-actions/voucher/get` - `SellerActionsVoucherGet`

### supply-order

- [交货或交货申请的商品组成](post-v1-supply-order-bundle-SupplyOrderBundle.md) - `POST /v1/supply-order/bundle` - `SupplyOrderBundle`

### warehouse

- [将仓库归档](post-v1-warehouse-archive-ArchiveWarehouseFBS.md) - `POST /v1/warehouse/archive` - `ArchiveWarehouseFBS`
- [创建仓库](post-v1-warehouse-fbs-create-WarehouseAPI_CreateWarehouseFBS.md) - `POST /v1/warehouse/fbs/create` - `WarehouseAPI_CreateWarehouseFBS`
- [获取用于创建仓库的揽收点列表](post-v1-warehouse-fbs-create-drop-off-list-WarehouseAPI_ListDropOffPointsForCreateFBSWarehouse.md) - `POST /v1/warehouse/fbs/create/drop-off/list` - `WarehouseAPI_ListDropOffPointsForCreateFBSWarehouse`
- [获取用于创建drop-off发运仓库的时间段列表](post-v1-warehouse-fbs-create-drop-off-timeslot-list-WarehouseFbsCreateDropOffTimeslotList.md) - `POST /v1/warehouse/fbs/create/drop-off/timeslot/list` - `WarehouseFbsCreateDropOffTimeslotList`
- [获取用于创建pick-up发运仓库的时间段列表](post-v1-warehouse-fbs-create-pick-up-timeslot-list-WarehouseFbsCreatePickUpTimeslotList.md) - `POST /v1/warehouse/fbs/create/pick-up/timeslot/list` - `WarehouseFbsCreatePickUpTimeslotList`
- [更新头程物流](post-v1-warehouse-fbs-first-mile-update-UpdateWarehouseFBSFirstMile.md) - `POST /v1/warehouse/fbs/first-mile/update` - `UpdateWarehouseFBSFirstMile`
- [更新仓库](post-v1-warehouse-fbs-update-UpdateWarehouseFBS.md) - `POST /v1/warehouse/fbs/update` - `UpdateWarehouseFBS`
- [获取用于修改仓库信息的揽收点列表](post-v1-warehouse-fbs-update-drop-off-list-WarehouseAPI_ListDropOffPointsForUpdateFBSWarehouse.md) - `POST /v1/warehouse/fbs/update/drop-off/list` - `WarehouseAPI_ListDropOffPointsForUpdateFBSWarehouse`
- [获取用于更新drop-off发运仓库的时间段列表](post-v1-warehouse-fbs-update-drop-off-timeslot-list-WarehouseFbsUpdateDropOffTimeslotList.md) - `POST /v1/warehouse/fbs/update/drop-off/timeslot/list` - `WarehouseFbsUpdateDropOffTimeslotList`
- [获取用于更新pick-up发运仓库的时间段列表](post-v1-warehouse-fbs-update-pick-up-timeslot-list-WarehouseFbsUpdatePickUpTimeslotList.md) - `POST /v1/warehouse/fbs/update/pick-up/timeslot/list` - `WarehouseFbsUpdatePickUpTimeslotList`
- [获取配送受限商品列表](post-v1-warehouse-invalid-products-get-WarehouseInvalidProductsGet.md) - `POST /v1/warehouse/invalid-products/get` - `WarehouseInvalidProductsGet`
- [仓库清单](post-v1-warehouse-list-WarehouseAPI_WarehouseList.md) - `POST /v1/warehouse/list` - `WarehouseAPI_WarehouseList`
- [获取操作状态](post-v1-warehouse-operation-status-GetWarehouseFBSOperationStatus.md) - `POST /v1/warehouse/operation/status` - `GetWarehouseFBSOperationStatus`
- [将仓库解除归档](post-v1-warehouse-unarchive-UnarchiveWarehouseFBS.md) - `POST /v1/warehouse/unarchive` - `UnarchiveWarehouseFBS`
- [获取含有配送受限商品的仓库列表](post-v1-warehouse-warehouses-with-invalid-products-WarehouseWithInvalidProducts.md) - `POST /v1/warehouse/warehouses-with-invalid-products` - `WarehouseWithInvalidProducts`
- [仓库列表](post-v2-warehouse-list-WarehouseListV2.md) - `POST /v2/warehouse/list` - `WarehouseListV2`

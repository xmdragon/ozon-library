# 官方 Seller API Chrome 全量同步（2026-09-07）

本轮由父 Agent 在当前 Chrome 官方页面 `https://docs.ozon.ru/api/seller/zh/` 通过可见 DOM 一次性采集，采集时间为 `2026-09-07T10:12:31.254Z`（operations）与 `2026-09-07T10:14:38.290Z`（News）。本次加工仅替换官方索引、运行既有 News 标记脚本和文档生成器；未重扫 AICollection、simple-collection 或 ZhiPin，也未将项目快照当作当前官方来源。

采集得到 262 个 operation 和 163 条 News。相对上一版，新增 `/v2/product/pictures/import`、两个 `/v1/carriage/courier-contact/*` 方法及 `/v1/report/realization/posting/create`；当前文档移除 5 个 `/v2/returns/rfbs/*` 方法与 `/v3/products/info/attributes`，共 6 个，并在 News 汇总中保留退役记录。News 保留 Chrome section 原始 ID/href；结构化方法列和变更列用于逐 endpoint 标记。

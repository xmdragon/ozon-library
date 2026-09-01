# ZhiPin 来源记录

## 用途

记录 `/Users/eric/works/ZhiPin` 对 Ozon 资料库的贡献范围、当前 revision 和优先阅读路径。

## AI 摘要

ZhiPin 是 Ozon 后端模型、官方 Seller API client、Seller 登录、旧 spider、浏览器扩展和 Web 管理端的重要来源。它适合补齐字段模型、API payload、数据库结构、业务流程和历史兼容行为。

ZhiPin 中的 `docs/OzonAPI/`、官方 API HTML 导出和纯官方参数表不作为本资料库的项目经验来源。官方 Seller API 以 Chrome 官方文档抓取和 News 更新为准；ZhiPin 只贡献调用实现、字段映射、登录态、扩展上下文、页面结构和历史兼容行为。

## 证据边界

### 索引快照

- 路径：`/Users/eric/works/ZhiPin`
- 分支：`master`
- 索引快照 revision：`75b2e572df48eaa9d986d8b28d8b5abd927332a5`
- `indexes/source-files.json` 与 `indexes/endpoint-cross-reference.json` 是 2026-07-09 生成的真实快照（文件数 3036），相关文件索引见这两个文件。

### 本次只读复核

- 本次只读复核对象：`origin/master` revision `6e19f3aedb3d732cad0f4b98191435d57b4ffa56`（短号 `6e19f3a`）。
- 复核范围是订单、商品 webhook/同步和财务调用链的指定源码路径；它不是全量扫描，也不替换上面的索引快照 revision。
- 复核确认：该 revision 仍调用停用的 `/v3/posting/fbs/list`（官方停用日 2026-06-01）与 `/v3/finance/transaction/list`（官方停用日 2026-07-06）；订单 `last_changed_status_date` 仍在顶层且没有对应契约测试；商品 durable webhook 与单一 finance producer 仍属于推荐/未合并目标。
- 财务迁移的官方替代 operation ID 是 `GetFinanceAccrualPostings`、`GetFinanceAccrualTypes`、`GetFinanceAccrualByDay`；三接口聚合语义尚未由本次只读复核验证。

### 迁移 PR 历史

- [PR #367](https://github.com/xmdragon/ZhiPin/pull/367)：订单 `/v4/posting/fbs/list + cursor` 迁移；匿名同窗口 v3/v4 posting 集合完全一致。
- [PR #369](https://github.com/xmdragon/ZhiPin/pull/369)：财务 `types/by-day/postings` 迁移；匿名四日对账的 649 个 unit 覆盖、total amount 与 sale commission 全部一致。
- 本节保留迁移期间的 PR 与匿名读取证据。2026-09-01 的当前源码复核确认 v4 posting 与 finance accrual 实现已进入 `origin/master`；是否部署仍以各生产环境运行元数据为准。

### 2026-09-01 财务类型与投影复核

- 复核使用 ZhiPin `origin/master` 当前财务适配器、脱敏的 Seller API 运行响应、Seller 页面 `/app/finances/accruals` 和旧 v3 transaction 交叉证据。
- 确认 Seller API `type_id` 与 Seller 页面 `accrual_type_ids` 是两套不同枚举：API `69/66/67` 分别对应页面内部 `14/177/106`，不能把页面筛选 ID 写进 Seller API 交易表。
- 确认 `accrual/postings` 只覆盖 posting 级应计；首程收单费仍需从 `accrual/by-day` 的两段 parent order 记录分摊。
- 复核暴露的实现缺口：仅补 `SaleCommission` 会漏掉 `RfbsGlobalAgentFee`、`RfbsGlobalDelivery`、order 级 `Acquiring` 以及补偿/退款/错误费。完整财务修复必须先入库全部应计，再统一投影所有订单费用字段和利润。
- `type_id=10` 与旧 v3 部分补偿 operation 对齐；`type_id=30` 与 `MarketplaceServiceItemRedistributionLastMilePVZ` 对齐。两者的 `/types` 英文名在探针被 429 限流时未取得，资料库显式保留证据边界，不猜名称。
- 生产库只读审计显示 `ozon_finance_transactions` 不保存 `type_id` 且没有类型参考表；117,332 条流水中出现 30 种 operation name、31 种 fee key，并已有未映射的 `29 LastMileCourier`、`32 Logistic`、`93 DefectFineErrors`。
- 2026-09-01 业务确认 `type_id=30` 并入 `last_mile_delivery_fee_cny`；实现约束是和 `type_id=66` 的 signed RUB 先求净额，禁止逐项取绝对值后相加。
- 结构化目录：`indexes/finance-accrual-types.json`；主题说明：`docs/api/finance-accrual-types.md`。

## 重点贡献

| 主题 | 说明 | 优先路径 |
| --- | --- | --- |
| 官方 Seller API client | `/v3/product/list`、`/v3/product/info/list`、库存、价格、仓库、订单、聊天、财务 | `plugins/ef/channels/ozon/api/client.py`、`plugins/ef/channels/ozon/api/client_mixins/` |
| 字段和数据模型 | product、posting、warehouse、finance、listing、collection、global settings | `plugins/ef/channels/ozon/models/`、`alembic/versions/` |
| Seller 登录和内部 API | 登录、验证码、Seller search、create-bundle、what_to_sell、delivery template | `ozon_spider/seller_login.py` |
| 买家页 spider | 商品页抓取、滑块、成人验证、稳定页检测 | `ozon_spider/spider.py`、`ozon_spider/slider_solver.py` |
| 浏览器扩展 DOM | 商品页、列表增强、Seller 页面、店铺绑定、通知配置 | `extension/src/content/` |
| 浏览器扩展请求上下文 | Cookie/company id、Seller tab MAIN world fetch、动态 Ozon header、MV3 后台任务 | `extension/src/shared/`、`extension/src/background/` |
| Web 管理端流程 | 商品、仓库、订单、刊登、库存、报表页面 | `web/src/pages/ozon/`、`web/src/services/ozon/` |
| 测试约束 | API 行为、桌面路由、同步、权限、字段转换 | `tests/` |
| 同步路径（只读复核） | 订单 offset 增量、商品定向 webhook、财务 operation 入库与费用投影的当前边界 | `plugins/ef/channels/ozon/services/sync/`、`plugins/ef/channels/ozon/services/finance_transactions_sync_service.py`、`plugins/ef/channels/ozon/services/ozon_finance_sync_service.py` |

## 合并规则

ZhiPin 的后端 client 和模型适合补齐字段、payload、数据状态；旧 spider 适合记录历史兼容和异常路径。若与 AICollection 新实现冲突，主题文档同时记录“当前推荐行为”和“历史兼容行为”。

若 ZhiPin 的本地官方文档副本与 Chrome 官方文档或 News 冲突，Chrome 官方文档优先。项目副本只保留为历史线索，不直接进入 `docs/api/official/`。

## 来源引用

- `indexes/source-files.json`
- `indexes/endpoint-cross-reference.json`
- `indexes/dom-selectors.json`

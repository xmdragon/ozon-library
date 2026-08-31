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

### 待合并迁移 PR

- [PR #367](https://github.com/xmdragon/ZhiPin/pull/367)：订单 `/v4/posting/fbs/list + cursor` 迁移；匿名同窗口 v3/v4 posting 集合完全一致。
- [PR #369](https://github.com/xmdragon/ZhiPin/pull/369)：财务 `types/by-day/postings` 迁移；匿名四日对账的 649 个 unit 覆盖、total amount 与 sale commission 全部一致。
- 两个 PR 均未部署。本节记录实现与匿名读取证据，不把分支状态写成 `master` 当前行为。

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

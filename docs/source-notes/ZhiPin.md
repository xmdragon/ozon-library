# ZhiPin 来源记录

## 用途

记录 `/Users/eric/works/ZhiPin` 对 Ozon 资料库的贡献范围、当前 revision 和优先阅读路径。

## AI 摘要

ZhiPin 是 Ozon 后端模型、官方 Seller API client、Seller 登录、旧 spider、浏览器扩展和 Web 管理端的重要来源。它适合补齐字段模型、API payload、数据库结构、业务流程和旧版 fallback。

## 当前来源

- 路径：`/Users/eric/works/ZhiPin`
- 分支：`master`
- revision：`75b2e572df48eaa9d986d8b28d8b5abd927332a5`
- 相关文件索引：见 `indexes/source-files.json`

## 重点贡献

| 主题 | 说明 | 优先路径 |
| --- | --- | --- |
| 官方 Seller API client | `/v3/product/list`、`/v3/product/info/list`、库存、价格、仓库、订单、聊天、财务 | `plugins/ef/channels/ozon/api/client.py`、`plugins/ef/channels/ozon/api/client_mixins/` |
| 字段和数据模型 | product、posting、warehouse、finance、listing、collection、global settings | `plugins/ef/channels/ozon/models/`、`alembic/versions/` |
| Seller 登录和内部 API | 登录、验证码、Seller search、create-bundle、what_to_sell、delivery template | `ozon_spider/seller_login.py` |
| 买家页 spider | 商品页抓取、滑块、成人验证、稳定页检测 | `ozon_spider/spider.py`、`ozon_spider/slider_solver.py` |
| 浏览器扩展 DOM | 商品页、列表增强、Seller 页面、店铺绑定、通知配置 | `extension/src/content/` |
| Web 管理端流程 | 商品、仓库、订单、刊登、库存、报表页面 | `web/src/pages/ozon/`、`web/src/services/ozon/` |
| 测试约束 | API 行为、桌面路由、同步、权限、字段转换 | `tests/` |

## 合并规则

ZhiPin 的后端 client 和模型适合补齐字段、payload、数据状态；旧 spider 适合记录历史 fallback 和异常路径。若与 AICollection 新实现冲突，主题文档同时记录“当前推荐行为”和“历史兼容行为”。

## 来源引用

- `indexes/source-files.json`
- `indexes/endpoint-cross-reference.json`
- `indexes/dom-selectors.json`

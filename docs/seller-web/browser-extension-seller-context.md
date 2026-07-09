# Seller 浏览器扩展上下文

## 用途

整理三个项目中围绕 `seller.ozon.ru` 登录态、Cookie、浏览器上下文 fetch、Seller 内部接口和扩展任务调度的实现经验。这里记录的是项目实现观察，不重复官方 Seller API 文档。

## AI 摘要

ZhiPin 扩展把 Seller 内部 API 当作“需要真实浏览器登录态的页面接口”处理：Chrome 下不能简单从 Manifest V3 Service Worker 请求 `seller.ozon.ru/api/...`，因为 forbidden headers、SameSite Cookie 和 Client Hints 会导致 403；可靠做法是在已登录的 seller 标签页 MAIN world 执行 fetch。Edge 等 Chromium 浏览器可回退为 Service Worker 直接请求。AICollection 的 Seller webview 则把 Seller 请求与 buyer 请求分组限流和暂停，避免一次 403 后其它 worker 继续打接口。

## 请求上下文规则

| 场景 | 推荐方式 | 原因 |
| --- | --- | --- |
| Chrome 扩展请求 `seller.ozon.ru/api/...` | 在 seller 标签页 MAIN world 执行 fetch | SW 请求的 `Sec-Fetch-Site`、Cookie、Client Hints 不可完全伪造，容易 403。 |
| Edge/非 Chrome 扩展 | 可尝试 SW fetch + `credentials: include` | ZhiPin 观察到 Edge 路径限制较少。 |
| Seller company id | 从 `sc_company_id` cookie 优先取，兼容 `contentId`、`company_id` | 内部 API header 和请求体通常都需要 company id。 |
| Seller session 可用性 | 调 `POST /api/user/get-language` 探测 | 返回 `language` 代表登录态和 company id 基本可用。 |
| Cookie 失效 | 缓存短期失效状态，等待用户重新登录后清除 | 防止后台反复打开 tab 或重复探测。 |

## 必要 Header

Seller 内部接口不是官方 Seller API，不用 `Client-Id` 和 `Api-Key`。项目实现中常见 header：

| Header | 典型值 | 用途 |
| --- | --- | --- |
| `Content-Type` | `application/json` | JSON 请求体。 |
| `x-o3-company-id` | `sc_company_id` | 选择当前 Seller 公司。 |
| `x-o3-app-name` | `seller-ui` | 模拟 Seller 前端。 |
| `x-o3-language` | `zh-Hans` | 中文界面。 |
| `x-o3-page-type` | `products-other`、`product-analytics` | 不同内部模块需要不同 page type。 |
| `Accept-Language` | `zh-Hans,zh;q=0.9,en;q=0.8` | 页面语言。 |

## SKU 到 Seller Bundle

项目中复用最多的 Seller 内部流程是 SKU 查完整商品属性：

1. 构造 cookie string，合并 `chrome.cookies` 和当前 document cookie。
2. 解析 company id，失败时返回 `NO_SELLER_ID`，提示先登录 Seller。
3. 调 `POST https://seller.ozon.ru/api/v1/search`：
   - 请求体使用 `filter.children_nodes` 按 SKU 精确搜索；
   - `pagination.limit` 通常设为 `"50"`；
   - 从 `variants[0].variant_id` 取 variant id。
4. 调 `POST https://seller.ozon.ru/api/site/seller-prototype/create-bundle-by-variant-id`：
   - 请求体包含 `company_id`、`variant_id`、`source: SOURCE_UI_COPY_MERGED`；
   - 从 `item` 解析标题、属性、尺寸和变体。
5. 尺寸优先用 `item.weight/depth/width/height`，缺失时回退 attribute id：
   - `4497` → weight；
   - `9454` → length；
   - `9455` → width；
   - `9456` → height。
6. 同 SKU 并发请求要共享同一个 Promise，避免商品页多个 provider 同时触发重复请求。

## 可用性与标签页管理

- 扩展只关闭自己创建的 seller 标签页，不关闭用户手动打开的 tab。
- 扩展创建的 tab 如果跳出 `seller.ozon.ru`，要从“可关闭集合”移除，避免误关用户页面。
- Seller 标签页 `complete` 后延迟约 2.5 秒再补跑挂起任务，避开页面初始化抖动。
- 未登录或 session 过期时，后台任务不应继续发 Seller 内部 API。
- `401/403` 后不要立即反复打开 Seller tab；ZhiPin 使用短期 cookie invalid cache，AICollection 使用 seller group pause/cooldown。

## 与官方 Seller API 的边界

- 本页接口都是 Seller Web 内部接口，不稳定，不作为长期契约。
- 如果只是官方 endpoint 的参数/返回，应查 `docs/api/official/`，不要从项目源码重复抄一份。
- 项目源码有价值的是：登录态、同源上下文、限流、字段回退、错误恢复和任务调度。

## 来源引用

- `/Users/eric/works/ZhiPin/extension/src/shared/api/ozon-seller-api.ts`
- `/Users/eric/works/ZhiPin/extension/src/shared/seller-auth.ts`
- `/Users/eric/works/ZhiPin/extension/src/shared/seller-tab-context.ts`
- `/Users/eric/works/ZhiPin/extension/src/shared/api/data-sources/providers/seller-dimensions-provider.ts`
- `/Users/eric/works/ZhiPin/extension/src/background/service-worker.ts`
- `/Users/eric/works/AICollection/src-tauri/crates/scraper/src/services/ozon_rate_limit.rs`
- `/Users/eric/works/ZhiPin/ozon_spider/seller_login.py`

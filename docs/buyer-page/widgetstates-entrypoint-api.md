# Buyer WidgetStates 与 Entrypoint API

## 用途

整理项目中对 `www.ozon.ru/api/entrypoint-api.bx/page/json/v2`、`widgetStates`、页面注入 fetch、列表/商品页 API 捕获的实践。这里是 Ozon 前端页面观察值，不是官方 Seller API。

## AI 摘要

simple-collection 和 ZhiPin 都发现：Ozon 买家页真正有用的数据常在 `entrypoint-api.bx/page/json/v2` 的 `widgetStates` 中，而不是稳定 DOM 中。可靠采集策略是“页面上下文请求 + widget key 模糊匹配 + DOM fallback”：列表页找 `tileGridDesktop`，商品页找 `webSale`、`webGallery`、`webProductHeading`、`webAspects`、`webAspectsModal`、描述/特征 widget，店铺页找 Seller 相关 widget。Content Script 或 Service Worker 直接请求容易 403，ZhiPin 改为在页面 MAIN world 发 fetch。

## 为什么要页面上下文请求

| 请求位置 | 风险 | 项目结论 |
| --- | --- | --- |
| Service Worker 直接请求 `www.ozon.ru/api/...` | 缺少完整同源请求上下文，可能 403 或触发反爬。 | 只作为 fallback。 |
| Content Script fetch | 仍可能缺少页面主世界的请求特征。 | ZhiPin 使用注入脚本转发。 |
| 页面 MAIN world fetch | 与 Ozon 前端同源，Cookie 和浏览器特征自然携带。 | 商品页、Modal API、Page2 API 优先使用。 |
| Hook fetch/XHR | 可被动捕获真实响应。 | simple-collection 用于列表采集。 |

## 标准入口

| 入口 | 用途 | 处理方式 |
| --- | --- | --- |
| `/api/entrypoint-api.bx/page/json/v2?url=<encoded>` | 获取页面 widgetStates | `url` 是页面路径，如 `/product/<sku>/`。 |
| `/modal/aspectsNew?product_id=<id>` | 变体 modal 数据 | 再包进 entrypoint API。 |
| `/product/<sku>/?layout_container=pdpPage2column&layout_page_index=2` | 描述、属性、typeNameRu | 商品详情 Page2。 |
| `/highlight/...`、`/category/...`、`/seller/...` | 列表/店铺页 | simple-collection 会规范化 `country=20`。 |

## widgetStates 解析规则

| Widget key/信号 | 数据 | 注意 |
| --- | --- | --- |
| `tileGridDesktop` | 列表商品卡片 | simple-collection 要求 `columnsCount === 4` 并从 `items[]` 解析。 |
| `webSale` | 商品价格 | Ozon 已从旧 `webPrice` 迁移；绿价/黑价要结合 DOM 或 widget 字段判断。 |
| `webGallery`、`pdpGallery` | 图片 | 图片 URL 可去掉 `/wc\d+/` 获得高清图。 |
| `webProductHeading` | 标题 | 作为商品页已加载信号。 |
| `webAspects` | 当前页变体轻量信息 | URL SKU 可先不解析完整 widget。 |
| `webAspectsModal` | 全量颜色×尺码变体 | 从 Modal API 获取，更适合完整变体采集。 |
| `webCharacteristics`、描述 widget | 属性、description、typeNameRu | 通常在 Page2 API。 |
| Seller widget | 店铺名称和 URL | 可从商品页 widgetStates 抽出店铺采集入口。 |
| `userAdultModal` | 成人验证拦截 | 不是无数据，应走成人验证流程。 |

## 列表页捕获流程

1. 注入页面脚本，hook `history.pushState`、`history.replaceState`、`fetch`、`XMLHttpRequest`。
2. 对 `/highlight/`、`/category/`、`/seller/` URL 自动补 `country=20`；`/highlight/` 空路径可改到中国商品 highlight。
3. 只检查 `/api/entrypoint-api.bx/page/json/v2` 响应。
4. 从 `widgetStates` 中找 `tileGridDesktop`。
5. 过滤非商品卡片：必须有 SKU、商品链接和评价/评分信号。
6. 输出 `{ sku, link, rating, comments }`，按 SKU 去重。
7. DOM 扫描只做补漏和 UI 展示，不作为唯一数据源。

## 商品页采集流程

1. 从 URL 提取 SKU，不用 DOM fallback；遇到新 URL 格式应补正则。
2. 页面上下文请求商品页 entrypoint API。
3. 从 `widgetStates` 解析标题、图片、价格、当前变体。
4. Page2 API 补描述、属性、`typeNameRu`。
5. Modal API 补全量变体，变体结果写入 30 分钟本地缓存。
6. 对每个变体可再请求其链接的 entrypoint API 补齐独立 description/attributes/dimensions。
7. 价格解析要兼容：
   - `3 007,80 ¥`；
   - `1 234,56 ₽`；
   - `$1,234.56`；
   - `€ 1.234,56`；
   - `1,234.56 HK$`。

## Header 与版本

ZhiPin 扩展会拦截真实 Ozon 请求中的版本 header，缓存 24 小时，再用于主动请求：

- `X-O3-App-Version`
- `X-O3-Manifest-Version`
- `X-O3-Parent-Requestid`
- `X-Page-View-Id`
- `x-o3-service-name`
- `sec-ch-ua`
- `User-Agent`

版本失效时回退到硬编码默认值，但这只是降级路径。AICollection 也记录过：给 Ozon buyer API 伪造半套 dweb header 反而会触发 403/fab incident，因此 header 要么来自真实拦截，要么尽量走页面上下文。

## 与官方 API 的边界

- `entrypoint-api.bx` 是 Ozon 前端页面 API，不属于官方 Seller API docs。
- 本文只记录项目观察到的 widget、fallback 和反爬规避，不作为稳定契约。
- 如果需要商品上传、库存、价格等官方方法参数，去 `docs/api/official/` 查。

## 来源引用

- `/Users/eric/works/simple-collection/extension/src/api_parser.js`
- `/Users/eric/works/simple-collection/extension/src/page_capture.js`
- `/Users/eric/works/simple-collection/extension/src/content.js`
- `/Users/eric/works/ZhiPin/extension/src/content/parsers/product-detail.ts`
- `/Users/eric/works/ZhiPin/extension/src/content/product-page/index.ts`
- `/Users/eric/works/ZhiPin/extension/src/shared/ozon-headers.ts`
- `/Users/eric/works/ZhiPin/extension/src/shared/api/ozon-buyer-api.ts`
- `/Users/eric/works/AICollection/src-tauri/crates/scraper/src/services/ozon_client_headers.rs`

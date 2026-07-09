# Seller web 内部 API

## 用途

记录需要 Seller 登录态的 `seller.ozon.ru/api/...` 内部接口和使用边界。

## AI 摘要

Seller web 内部 API 不是官方 Seller API。它们通常需要浏览器登录态、同源页面上下文和 `credentials: include`。AICollection 和 ZhiPin 都使用过 `/api/v1/search`、`/api/site/seller-prototype/create-bundle-by-variant-id`、`/api/site/seller-analytics/what_to_sell/data/v3`、`/api/site/seller-analytics/what_to_sell/get_sellers`。这些接口按不稳定观察值记录，不应当作长期契约。

浏览器扩展中调用 Seller web 内部 API 时，还要参考 `docs/seller-web/browser-extension-seller-context.md`。该文档整理了 ZhiPin 扩展里 MAIN world fetch、Seller tab 复用、Cookie/company id、动态 Ozon header 和 MV3 后台任务的实现经验。

## 关键接口

| URL | 用途 | 来源 |
| --- | --- | --- |
| `https://seller.ozon.ru/api/v1/search` | 按 SKU 或条件搜索，拿 variant/product 信息 | AICollection、ZhiPin |
| `https://seller.ozon.ru/api/site/seller-prototype/create-bundle-by-variant-id` | 通过 `variant_id` 获取完整商品 bundle/属性/尺寸 | AICollection、ZhiPin |
| `https://seller.ozon.ru/api/site/seller-analytics/what_to_sell/data/v3` | “卖什么好”数据，支持 seller/category/filter 维度 | AICollection、ZhiPin |
| `https://seller.ozon.ru/api/site/seller-analytics/what_to_sell/get_sellers` | 按名称搜索 seller | AICollection、ZhiPin |
| `https://seller.ozon.ru/api/delivery-method-service/...` | delivery template/location/category/speed 相关数据 | ZhiPin |

## 流程

SKU search + create-bundle：

1. 在已登录 Seller 页面上下文中请求 `/api/v1/search`。
2. 从 search 响应中取 `variant_id` 或完整 variant。
3. 请求 `create-bundle-by-variant-id`。
4. 从 bundle `item` 中提取属性、尺寸、模型等信息。
5. 如果 search 成功但 create-bundle 返回空或 5xx，视为临时故障，可重试。

what_to_sell：

1. 调 `get_sellers` 可按 seller 名称查 company。
2. 调 `data/v3` 可按 `filter.company_ids`、`filter.categories` 或原生 filter 查询。
3. AICollection 中相关请求通过页面 JS fetch 执行，带 `credentials: include`。

## 异常与恢复

| 情况 | 处理 |
| --- | --- |
| 未登录或 session 失效 | 先恢复 Seller 登录态，不要用官方 API key 替代。 |
| 403/429 | 视为 Seller web 阻塞或限流，进入恢复/重登/换 profile 流程。 |
| 空响应/5xx | create-bundle 和 what_to_sell 可作为临时失败处理。 |
| 字段变化 | 更新 `docs/seller-web/` 和 `indexes/endpoint-cross-reference.json`，标注观察日期。 |

## 来源引用

- `/Users/eric/works/AICollection/src-tauri/crates/scraper/src/services/ozon_seller.rs`
- `/Users/eric/works/AICollection/src-tauri/crates/scraper/src/browser/seller.rs`
- `/Users/eric/works/ZhiPin/ozon_spider/seller_login.py`
- `/Users/eric/works/ZhiPin/extension/src/shared/api/ozon-seller-api.ts`
- `/Users/eric/works/ZhiPin/extension/src/shared/seller-tab-context.ts`
- `indexes/endpoint-cross-reference.json`

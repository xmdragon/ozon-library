# 项目源码抽取流程

## 来源项目

- `/Users/eric/works/AICollection`
- `/Users/eric/works/simple-collection`
- `/Users/eric/works/ZhiPin`

## 扫描目标

优先抽取以下主题：

- Seller API 后端调用：`/vN/...` endpoint、headers、限流、错误处理。
- Seller web 内部 API：`seller.ozon.ru/api/...`、`credentials: include`、登录态请求。
- 买家页 DOM：`data-widget`、商品页/列表页 selector、价格字段。
- 页面状态：NoConnection、Chrome error、block page、captcha、adult、antibot。
- 恢复逻辑：slider gate、rotate、reload、WebView recovery、pause/cancel。
- 字段模型：product、sku、offer_id、warehouse_id、posting、category attribute。
- 历史 incident：changelog、task notes、tests 中的回归说明。

## 排除项

三个项目里可能包含官方 Seller API 的本地镜像、HTML 导出、复制来的参数表或示例响应。这些内容不作为项目经验来源，避免和 Chrome 官方文档重复或冲突。

- 官方 Seller API 参数、返回值、方法废弃和 News 更新只从 Chrome 官方文档进入 `docs/api/official/` 与 `docs/api/seller-api-news.md`。
- 项目源码只提炼实现层知识：实际调用上下文、Cookie/header、Seller tab fetch、DOM 结构、`widgetStates`、字段 fallback、限流、异常恢复、任务流程和测试约束。
- 如果项目中的官方文档副本与 Chrome 官方文档冲突，以 Chrome 官方文档和 News 为准；项目副本最多作为历史线索，不进入主题结论。

## 推荐 rg 关键词

```bash
rg -l -i 'ozon|seller|captcha|slider|adult|NoConnection|no connection|client[-_ ]?id|api[-_ ]?key|x-o3|posting|offer_id|sku|warehouse|验证码|滑块|成人|登录|异常' /Users/eric/works/AICollection
rg -l -i 'ozon|seller|captcha|slider|adult|NoConnection|no connection|client[-_ ]?id|api[-_ ]?key|x-o3|posting|offer_id|sku|warehouse|验证码|滑块|成人|登录|异常' /Users/eric/works/simple-collection
rg -l -i 'ozon|seller|captcha|slider|adult|NoConnection|no connection|client[-_ ]?id|api[-_ ]?key|x-o3|posting|offer_id|sku|warehouse|验证码|滑块|成人|登录|异常' /Users/eric/works/ZhiPin
```

## 路径优先级

AICollection：

- `src-tauri/crates/scraper/src/services/page_state.rs`
- `src-tauri/crates/scraper/src/services/ozon_rate_limit.rs`
- `src-tauri/crates/scraper/src/services/ozon_seller.rs`
- `src-tauri/crates/scraper/src/browser/seller.rs`
- `src-tauri/crates/scraper/src/services/slider/*`
- `src-tauri/crates/scraper/src/services/queue/*`
- `docs/changelog/*ozon*`

ZhiPin：

- `plugins/ef/channels/ozon/api/client.py`
- `plugins/ef/channels/ozon/api/client_mixins/*`
- `plugins/ef/channels/ozon/models/*`
- `ozon_spider/seller_login.py`
- `ozon_spider/spider.py`
- `extension/src/content/product-page/*`
- `extension/src/content/list-enhancer/*`
- `extension/src/content/seller-page/*`
- `extension/src/content/shop-binding/*`
- `extension/src/shared/api/ozon-seller-api.ts`
- `extension/src/shared/seller-auth.ts`
- `extension/src/shared/seller-tab-context.ts`
- `extension/src/shared/ozon-headers.ts`
- `extension/src/background/service-worker.ts`
- `extension/src/background/auto-collector.ts`

simple-collection：

- `extension/src/content.js`
- `extension/src/api_parser.js`
- `extension/src/page_capture.js`
- `tests/test_extension_api_capture.py`
- `tests/test_ozon_brand_breadcrumb.py`
- `tests/test_runtime_resilience.py`

## 索引输出

`indexes/source-files.json`：文件级主题索引。

`indexes/endpoint-cross-reference.json`：endpoint/API URL 到来源文件的映射。

`indexes/dom-selectors.json`：selector、widget、页面标记到来源文件的映射。

索引是入口，不是最终资料。重要知识必须整理到 `docs/` 主题文档。

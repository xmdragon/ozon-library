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

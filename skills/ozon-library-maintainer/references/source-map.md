# 来源地图

## 官方 Seller API

- 来源：当前 Chrome 标签页 `https://docs.ozon.ru/api/seller/zh/?__rr=1`
- 抽取方式：Chrome DOM，只读 `div[id^="operation/"]`
- 输出：`indexes/official-seller-api.operations.json`
- 约束：不使用直接下载或外部抓取替代

## AICollection

重点：

- 新版 Ozon scraper/WebView/recovery 实现。
- 页面状态分类、NoConnection、block、antibot incident。
- 滑块处理、adult verification、queue recovery。
- Seller web API 和批量采集流程。

优先路径：

- `/Users/eric/works/AICollection/src-tauri/crates/scraper/src/services/page_state.rs`
- `/Users/eric/works/AICollection/src-tauri/crates/scraper/src/services/ozon_rate_limit.rs`
- `/Users/eric/works/AICollection/src-tauri/crates/scraper/src/services/ozon_seller.rs`
- `/Users/eric/works/AICollection/src-tauri/crates/scraper/src/browser/seller.rs`
- `/Users/eric/works/AICollection/src-tauri/crates/scraper/src/services/slider/`
- `/Users/eric/works/AICollection/docs/changelog/`

## ZhiPin

重点：

- Ozon 后端 API client、models、migrations。
- 旧 spider 和 Seller 登录流程。
- 浏览器扩展中的商品页、列表页、Seller 页、店铺绑定 DOM。
- Tests 中的行为约束和历史 bug。

优先路径：

- `/Users/eric/works/ZhiPin/plugins/ef/channels/ozon/api/client.py`
- `/Users/eric/works/ZhiPin/plugins/ef/channels/ozon/api/client_mixins/`
- `/Users/eric/works/ZhiPin/plugins/ef/channels/ozon/models/`
- `/Users/eric/works/ZhiPin/ozon_spider/`
- `/Users/eric/works/ZhiPin/extension/src/content/`
- `/Users/eric/works/ZhiPin/tests/`

## simple-collection

重点：

- 轻量 Ozon 扩展采集。
- API 捕获、页面捕获、列表页卡片解析。
- 运行时韧性和测试样例。

优先路径：

- `/Users/eric/works/simple-collection/extension/src/content.js`
- `/Users/eric/works/simple-collection/extension/src/api_parser.js`
- `/Users/eric/works/simple-collection/extension/src/page_capture.js`
- `/Users/eric/works/simple-collection/tests/`

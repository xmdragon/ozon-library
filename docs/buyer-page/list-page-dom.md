# 列表页 DOM

## 用途

记录 Ozon 列表页/搜索页卡片采集和列表增强相关 DOM 观察值。

## AI 摘要

列表页常见内容锚点包括 `data-widget="searchResultsV2"`、`data-widget="tileGridDesktop"`、`data-widget="megaPaginator"`。simple-collection 用 `div[data-component*="shortCard"], div.tile-root` 扫卡片，并从 `a[href*="/product/"]` 提取 SKU。ZhiPin list-enhancer 也以商品链接和容器 MutationObserver 处理 SPA 重渲染。

列表页不能只依赖 DOM selector。simple-collection 的 API capture 会解析页面请求里的 `widgetStates`，尤其是 `tileGridDesktop` 和四列布局商品卡片，可作为 DOM 缺字段时的补充路径。详见 `docs/buyer-page/widgetstates-entrypoint-api.md`。

## 关键 DOM

| Selector/标记 | 用途 | 来源 |
| --- | --- | --- |
| `[data-widget="searchResultsV2"]` | 搜索结果容器 | AICollection page state、ZhiPin list-enhancer |
| `[data-widget="tileGridDesktop"]` | 商品网格 | AICollection page state |
| `[data-widget="megaPaginator"]` | 分页/列表内容信号 | AICollection/simple-collection |
| `div[data-component*="shortCard"]` | 商品卡片 | simple-collection |
| `div.tile-root` | 商品卡片 fallback | simple-collection |
| `a[href*="/product/"]` | 商品链接/SKU | ZhiPin/simple-collection |

## 采集流程

1. 等待列表容器出现。
2. 扫描卡片容器，排除推荐块或不符合布局的卡片。
3. 从商品链接提取 SKU。
4. 提取价格、评分、评论、图片等 DOM 信息。
5. 滚动加载，遇到页面底部或采集上限停止。
6. 对 SPA 重渲染使用 MutationObserver 或周期扫描补漏。

## 异常与恢复

| 情况 | 处理 |
| --- | --- |
| 卡片 selector 变化 | fallback 到商品链接 `a[href*="/product/"]`。 |
| 虚拟列表/懒加载 | 滚动后再次扫描，按 SKU 去重。 |
| 推荐块混入 | 根据布局、评论/评分、链接和位置过滤。 |
| 页面被 block/captcha | 转到 recovery 文档处理，不继续扫 DOM。 |

## 来源引用

- `/Users/eric/works/simple-collection/extension/src/content.js`
- `/Users/eric/works/simple-collection/extension/src/api_parser.js`
- `/Users/eric/works/simple-collection/extension/src/page_capture.js`
- `/Users/eric/works/ZhiPin/extension/src/content/list-enhancer/index.ts`
- `/Users/eric/works/AICollection/src-tauri/crates/scraper/src/services/page_state.rs`
- `indexes/dom-selectors.json`

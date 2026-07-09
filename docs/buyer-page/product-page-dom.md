# 商品页 DOM

## 用途

记录 Ozon 买家商品页中用于采集价格、商品 ID、图片、标题和状态的 DOM 观察值。

## AI 摘要

商品页价格锚点已从旧 `webPrice` 变化到 `data-widget="webSale"`。ZhiPin 当前商品页扩展优先用 `webSale`，在其中通过 `span[class*="tsHeadline"]` 和俄文标签区分绿价/黑价。AICollection page state 仍把 `webPrice`、`webGallery`、`webProductHeading` 等作为“有商品内容”的信号之一。DOM selector 应视为观察值，必须保留 fallback。

商品页也可通过 `entrypoint-api.bx` 里的 `widgetStates` 补充 DOM 取不到的字段，尤其是 `webSale`、`webAspects`、`webAspectsModal` 和成人弹窗状态。详见 `docs/buyer-page/widgetstates-entrypoint-api.md`。

## 关键 DOM

| Selector/标记 | 用途 | 说明 |
| --- | --- | --- |
| `[data-widget="webSale"]` | 商品价格区域 | 当前价格提取主锚点。 |
| `[data-widget="webPrice"]` | 旧价格区域/内容信号 | 旧实现或 fallback。 |
| `[data-widget="webGallery"]`、`[data-widget="pdpGallery"]` | 商品图片内容信号 | 可判断商品页已加载。 |
| `[data-widget="webProductHeading"]` | 商品标题内容信号 | 可判断商品页已加载。 |
| `[data-widget="webOutOfStock"]` | 售罄状态 | AICollection 识别缺货。 |
| URL `/product/...-<sku>` | SKU 提取 | simple-collection 和 ZhiPin 都用 URL 正则提取。 |

## 价格提取流程

1. 定位 `[data-widget="webSale"]`。
2. 在 widget 内查找 `span[class*="tsHeadline"]`。
3. 优先按文字标签区分：
   - `Ozon Банком`：绿价。
   - `без Ozon Банка`：黑价。
4. 如果标签语言变化，按 headline 顺序 fallback。
5. 解析价格时兼容空格、NBSP、逗号/点小数、多字符货币符号。

## 异常与恢复

| 情况 | 处理 |
| --- | --- |
| 找不到 `webSale` | fallback 到旧 `webPrice` 或页面 API。 |
| 文案语言变化 | 不依赖单一文案，保留 headline 顺序 fallback。 |
| SPA 重新渲染 | 用 MutationObserver 重新提取。 |
| 售罄 | 识别 `webOutOfStock` 或固定文案，不当作采集失败。 |

## 来源引用

- `/Users/eric/works/ZhiPin/extension/src/content/product-page/index.ts`
- `/Users/eric/works/ZhiPin/extension/src/content/product-page/calculator.ts`
- `/Users/eric/works/ZhiPin/extension/src/content/parsers/product-detail.ts`
- `/Users/eric/works/AICollection/src-tauri/crates/scraper/src/services/page_state.rs`
- `indexes/dom-selectors.json`

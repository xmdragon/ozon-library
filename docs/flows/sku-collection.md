# SKU 采集流程

## 用途

记录从 Ozon 买家页/Seller web 获取 SKU 和补充商品信息的复用流程。

## AI 摘要

SKU 可以从买家页 URL、列表页商品链接、Seller web search 和项目数据表中获得。批量采集通常先从列表/输入获得 SKU，再用买家页 DOM/API 或 Seller web 内部 API 补充价格、属性、尺寸、销量和跟卖信息。Seller web 补充常见两步是 `/api/v1/search` 获取 variant，再用 `create-bundle-by-variant-id` 取完整 item。

浏览器扩展侧的自动采集、后台队列、来源超时和店铺任务流程见 `docs/flows/extension-collection-and-shop-tasks.md`。

## 流程

1. 输入来源：
   - 手动 SKU；
   - Ozon 列表页卡片；
   - 商品页 URL；
   - Seller 店铺/what_to_sell 数据。
2. 去重并规范化 SKU。
3. 买家页补充：
   - 打开 `/product/...`；
   - 识别 page state；
   - 处理 slider/adult/block；
   - 提取价格、标题、图片、评分等。
4. Seller web 补充：
   - 登录 Seller；
   - `/api/v1/search`；
   - `create-bundle-by-variant-id`；
   - 解析属性、尺寸和 Seller 侧字段。
5. 写入队列/结果表。

## 异常与恢复

| 情况 | 处理 |
| --- | --- |
| SKU 页面进入 slider | 调 recovery slider gate。 |
| 成人商品 | 走 adult verification。 |
| Seller search 有结果但 bundle 空 | 视为临时 Seller web 故障，重试或延后。 |
| 页面 NoConnection/block | 停止当前 profile 或进入恢复链路。 |
| URL 无 SKU | fallback 到页面 API 或跳过。 |

## 来源引用

- `/Users/eric/works/AICollection/src-tauri/crates/scraper/src/services/pipeline/`
- `/Users/eric/works/AICollection/src-tauri/crates/scraper/src/services/ozon_seller.rs`
- `/Users/eric/works/ZhiPin/ozon_spider/seller_login.py`
- `/Users/eric/works/ZhiPin/extension/src/background/auto-collector.ts`
- `/Users/eric/works/simple-collection/extension/src/content.js`

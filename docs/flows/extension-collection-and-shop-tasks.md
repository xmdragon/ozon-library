# 扩展采集与店铺任务流程

## 用途

整理 ZhiPin 和 simple-collection 扩展中可复用的页面采集、店铺绑定、通知配置、评论促销关闭、自动采集和后台任务调度流程。这里关注业务流程和 DOM 操作韧性，不重复官方 API 文档。

## AI 摘要

ZhiPin 扩展已经不只是“页面上抓 SKU”：它包含自动采集队列、商品页店铺采集、Seller 店铺页增强、店铺绑定生成 API key、通知 URL 配置、评论促销关闭、后台 shop task runner、WebSocket 保活和 Seller 可用性定时探测。simple-collection 则提供轻量采集面板、API 捕获、滚动采集和 TXT 导出。可复用经验是：对 Ozon SPA 必须等待 DOM 稳定、限定弹窗搜索范围、记录进度并可恢复、用户未登录时不要执行后台任务。

## 自动采集队列

1. 扩展登录后从后端获取待采集地址队列。
2. 按用户配置控制：
   - 最大并发 tab，默认 1；
   - 单地址超时，默认 10 分钟；
   - 每地址目标商品数，默认 100；
   - 自动上传；
   - 采集后关闭 tab。
3. 每个 source 先更新为 `collecting`，打开 tab 后发采集消息。
4. 采集结果非空时上传并更新 collected count。
5. 单任务失败写 errors，连续错误达到上限后停止。
6. stop 时向所有活跃 tab 发 `STOP_COLLECTION`，再关闭扩展创建的 tab。

## simple-collection 轻量面板

- 在 Ozon 页面注入固定面板，支持登录、开始、暂停、清空、导出。
- 注入 `api_parser.js` 和 `page_capture.js` 后捕获 entrypoint API 响应。
- 自动把 `/highlight/`、`/category/`、`/seller/` 导航规范到 `country=20`。
- 滚动采集使用上限和分片缓冲，按 SKU 去重。
- 只提取 SKU、评分、评论和链接，不承担 Seller 登录态任务。

## Seller 店铺页增强

| 步骤 | 说明 |
| --- | --- |
| 等待 island | ZhiPin 观察到店铺 widget 从 `webSeller` 改为 `sellerTransparency`。 |
| 等 DOM 稳定 | 监控 island，300ms 无变化后注入按钮，最长等 10 秒。 |
| 注入按钮 | 在店铺信息容器加入“采集店铺”按钮。 |
| 检查已添加 | 登录后向后端查 collection source 是否存在。 |
| 重新注入 | Ozon SPA 替换节点时，MutationObserver 重新注入按钮。 |

店铺名称不能只靠 URL；商品页可从 widgetStates 提取 seller 名称和 URL，再规范化为 `https://www.ozon.ru/seller/...`。

## 店铺绑定与 API Key 创建

ZhiPin 的 shop binding 不是官方 API 调用，而是自动化 Seller 页面 DOM：

1. 打开 Seller API key 设置页面。
2. 等待元素出现，使用 label 文本定位输入框。
3. 设置 input 值时调用原生 setter，并派发 `input/change`。
4. 下拉选择“供外部服务/应用使用”等 key usage。
5. 弹窗内按钮查找限定到 `#ods-window-target-container`，避免误点页面外层同名按钮。
6. 排除“取消/Cancel/Отмена”按钮，只点击可见未禁用的确认按钮。
7. 多语言候选文本并存：中文、英文、俄文都要保留。

这个流程说明的是 UI 自动化经验，不应把生成出来的真实 key 写入资料库。

## 通知配置与评论促销

| 任务 | 页面 | 技术点 |
| --- | --- | --- |
| 通知 API 配置 | `/app/settings/notifications-api` | 若不在目标页，保存 pending start 后跳转；到页后恢复进度。 |
| 店铺切换 | Seller 顶部店铺选择 | 通过 `sc_company_id` cookie 和页面脚本读取/切换当前店铺。 |
| 通知类型勾选 | 通知配置表单 | 按配置列表逐项启用，记录进度。 |
| 评论促销关闭 | review-promotion block | 找 `[data-onboarding-target="review-promotion-block"]` 内 checkbox。 |

这些流程都应保存进度到 `chrome.storage.local`，避免页面跳转、SW 重启或用户刷新后丢失。

## 后台任务调度

- MV3 Service Worker 可能空闲终止，ZhiPin 用 `chrome.alarms` 做 WebSocket keepalive。
- 所有认证后任务先等 `initializeAfterAuth` 完成；如果 token 校验失败，后续请求不发。
- Seller 可用性每 180 分钟定时检查一次，也会在 Seller tab 加载完成后清 cookie invalid cache。
- “用户打开 seller 页”不应自动触发任务；只有存在 pending forced run 时才补跑。
- 后台任务失败时要把 pending 写回去，避免登录后强制任务被静默丢弃。

## 排除项

- 不把项目中的官方 API HTML/Markdown 镜像当作项目经验。
- 不记录真实账号、cookie、API key、通知 URL 实值。
- 不把 UI 自动化 selector 当稳定契约；必须保留来源和观察时间。

## 来源引用

- `/Users/eric/works/ZhiPin/extension/src/background/auto-collector.ts`
- `/Users/eric/works/ZhiPin/extension/src/background/service-worker.ts`
- `/Users/eric/works/ZhiPin/extension/src/content/seller-page/index.ts`
- `/Users/eric/works/ZhiPin/extension/src/content/product-page/seller-collect.ts`
- `/Users/eric/works/ZhiPin/extension/src/content/shop-binding/binding-operations.ts`
- `/Users/eric/works/ZhiPin/extension/src/content/notification-setup/NotificationSetupPanel.ts`
- `/Users/eric/works/ZhiPin/extension/src/content/notification-setup/dom-operations.ts`
- `/Users/eric/works/ZhiPin/extension/src/content/review-promotion/dom-operations.ts`
- `/Users/eric/works/simple-collection/extension/src/content.js`

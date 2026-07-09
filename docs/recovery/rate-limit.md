# 限流和阻塞

## 用途

记录官方 Seller API、Seller web 内部 API 和买家页采集中的限流/阻塞处理。

## AI 摘要

官方 Seller API 文档提示同一 Client ID 每秒最多 50 个请求。ZhiPin 后端 client 对资源类型设 50 req/s，并对 429 读取 `Retry-After` 后重试。AICollection 买家页侧把 antibot、block marker、无商品内容的 NoConnection 视为 Ozon 页面限流/阻塞；Seller API blocked status 包括 403 和 429。

## 关键规则

| 场景 | 判定 | 处理 |
| --- | --- | --- |
| 官方 API 429 | HTTP 429 | 等待 `Retry-After` 后重试。 |
| 官方 API 5xx | HTTP 500-599 | 指数退避重试。 |
| API key 失效 | 403 + `deactivated`/`invalid api-key` 等 | 停用店铺或提示重新配置。 |
| 买家页 block | `url:block.html` 或 antibot marker | 暂停/恢复/换 profile。 |
| NoConnection 且无商品内容 | `is_no_connection && !has_product_content` | 当作页面阻塞或网络异常处理。 |
| Chrome error | `chrome-error://` | 浏览器加载异常，不计入 Ozon 服务限流 streak。 |

## 项目实现要点

- ZhiPin `_request` 在请求前进入 `RateLimiter.acquire(resource_type)`。
- ZhiPin 对 429 使用 `Retry-After`，对 5xx 和 timeout/connect error 做有限重试。
- AICollection `is_seller_api_blocked_status` 把 403 和 429 视为 Seller API blocked。
- AICollection `is_ozon_terminal_page_block` 包含 Chrome error 和 Ozon page rate limited，但 NoConnection 判定必须叠加 `!has_product_content`。

## 来源引用

- 官方 Seller API 总描述和授权章节。
- `/Users/eric/works/ZhiPin/plugins/ef/channels/ozon/api/client_mixins/base.py`
- `/Users/eric/works/AICollection/src-tauri/crates/scraper/src/services/ozon_rate_limit.rs`

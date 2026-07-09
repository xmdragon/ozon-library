# Chrome 官方 Seller API 抽取流程

## 适用范围

用于从当前 Chrome 中打开的 Ozon Seller API 官方文档抽取 operation 索引和 News 更新索引。不要用直接下载、`curl` 或搜索引擎替代。

## 前置条件

- Chrome 已打开 `https://docs.ozon.ru/api/seller/zh/?__rr=1`。
- Chrome 已能访问 `https://docs.ozon.ru/api/seller/zh/#tag/News`。
- 页面标题应类似 `Ozon Seller API 文件`。
- 页面由 Redoc 渲染，operation block 形如 `div[id^="operation/"]`。

## 抽取字段

每个 operation 至少抽取：

- `operationId`
- `title`
- `method`
- `path`
- `headings`
- `tables`
- `examples`
- `sourceUrl`

索引根对象包含：

- `captured_at`
- `source_url`
- `title`
- `operation_count`
- `operations`

News 索引包含：

- `captured_at`
- `source_url`
- `title`
- `entry_count`
- `entries`

每个 News entry 至少包含 `date`、`id`、`text`、`paths`、`links` 和 `sourceUrl`。

## DOM 抽取策略

通过 Chrome browser control 的 `tab.playwright.evaluate` 在页面里执行只读 DOM 投影：

1. 选择 `div[id^="operation/"]`。
2. 从 `id` 去掉 `operation/` 得到 `operationId`。
3. 从块文本中匹配 `get|post|put|delete|patch` 和 `/vN/...` 路径。
4. 收集块内 `h1` 到 `h5` 作为 headings。
5. 收集 `table` 的 `tr` 直接子单元格为 `rows`，同时保留纯文本 `text` 作为兼容字段。
6. 收集 `pre, code` 中较长的 JSON 示例和重要错误码。
7. 写入 `indexes/official-seller-api.operations.json`。
8. 在同一个 Chrome 页面切换到 `#tag/News`，抽取 News 条目，写入 `indexes/official-seller-api.news.json`。
9. 运行 `python3 tools/apply_official_api_news.py`，把废弃方法、已移除旧方法、新增字段、废弃字段和迁移到正式版等标记合并回 operation 索引，并生成 `docs/api/seller-api-news.md`。
10. 运行 `python3 tools/generate_official_api_docs.py`，把索引展开到 `docs/api/official/`。

## 注意事项

- 只读页面，不输入 Client ID、API key 或任何账号信息。
- 如果页面未加载完整 operation，先滚动或等待 Redoc 渲染完成，再抽取。
- 如果 operation count 明显小于预期，记录失败原因，不要用非 Chrome 来源补齐。
- 保留中文官方标题和说明，endpoint、operation ID、字段名保持原文。
- 逐方法 Markdown 是生成产物；修改官方方法内容时优先改 Chrome 抽取索引或生成器，不要只手改单个生成页。
- News 中“参数/字段已弃用或已删除”只能作为字段级标记，不应把整个方法标为废弃；只有官方明确写“该方法/该方式/这些方式已弃用、将停用、已从文档删除”等句子时，才升级为方法生命周期标记。
- News 中已从文档删除、当前 operation 索引不存在的方法会记录在 `docs/api/seller-api-news.md` 的“News 中已移除或当前索引缺失的方法”中，供 AI 避免误用。

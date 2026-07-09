# Chrome 官方 Seller API 抽取流程

## 适用范围

用于从当前 Chrome 中打开的 Ozon Seller API 官方文档抽取 operation 索引。不要用直接下载、`curl` 或搜索引擎替代。

## 前置条件

- Chrome 已打开 `https://docs.ozon.ru/api/seller/zh/?__rr=1`。
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

## DOM 抽取策略

通过 Chrome browser control 的 `tab.playwright.evaluate` 在页面里执行只读 DOM 投影：

1. 选择 `div[id^="operation/"]`。
2. 从 `id` 去掉 `operation/` 得到 `operationId`。
3. 从块文本中匹配 `get|post|put|delete|patch` 和 `/vN/...` 路径。
4. 收集块内 `h1` 到 `h5` 作为 headings。
5. 收集前几个 `table` 的纯文本作为 schema/参数表。
6. 收集 `pre, code` 中较长的 JSON 示例和重要错误码。
7. 写入 `indexes/official-seller-api.operations.json`。
8. 运行 `python3 tools/generate_official_api_docs.py`，把索引展开到 `docs/api/official/`。

## 注意事项

- 只读页面，不输入 Client ID、API key 或任何账号信息。
- 如果页面未加载完整 operation，先滚动或等待 Redoc 渲染完成，再抽取。
- 如果 operation count 明显小于预期，记录失败原因，不要用非 Chrome 来源补齐。
- 保留中文官方标题和说明，endpoint、operation ID、字段名保持原文。
- 逐方法 Markdown 是生成产物；修改官方方法内容时优先改 Chrome 抽取索引或生成器，不要只手改单个生成页。

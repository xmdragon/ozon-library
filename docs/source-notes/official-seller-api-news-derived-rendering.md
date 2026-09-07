# 官方 Seller API News 派生标记与渲染记录

2026-09-07：针对 Chrome fresh News 抽取中的真实文本，补充两种保守分类：`增加了获取交付物成分的方法。` 识别为 `new_method`，`新了方法响应中...` 识别为 `updated`。分类只写入 `indexes/official-seller-api.operations.json` 的派生 `news_updates`，不修改 `indexes/official-seller-api.news.json` 的原始 rows、description 或 raw_text。

News 摘要和逐方法页的 Markdown 表格单元格在渲染边界将换行转为 `<br>`，以保持每条 pipe table row 为单行，同时保留原始文本内容。来源为 Chrome 官方 Seller API News 页面；重建入口是 `tools/apply_official_api_news.py` 和 `tools/generate_official_api_docs.py`。

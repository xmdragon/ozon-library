# 仓库地图

## 顶层目录

- `README.md`：人工和 AI 的入口。
- `docs/api/`：官方 Seller API 与后端调用。
- `docs/api/official/`：由 Chrome 官方索引生成的逐方法 API 文档。
- `docs/seller-web/`：Seller 登录态内部接口和页面流程。
- `docs/buyer-page/`：买家页 DOM、列表页、商品页、成人验证、NoConnection。
- `docs/recovery/`：页面状态、滑块、反爬 incident、限流和 WebView 恢复。
- `docs/fields/`：字段对照。
- `docs/flows/`：端到端流程。
- `docs/source-notes/`：来源项目说明和差异。
- `indexes/`：机器可读索引。
- `tools/generate_official_api_docs.py`：把官方 operation 索引展开为逐方法 Markdown。
- `workflows/`：维护流程。
- `skills/ozon-library-maintainer/`：仓库本地 skill。

## 先读顺序

维护资料库时：

1. `README.md`
2. `workflows/ozon-library-update.md`
3. `indexes/source-files.json`
4. `docs/source-notes/`
5. 目标主题文档

新增主题时，先检查是否已经存在相近主题，避免按项目重复创建。

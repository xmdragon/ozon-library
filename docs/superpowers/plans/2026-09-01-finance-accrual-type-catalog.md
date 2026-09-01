# Finance Accrual Type Catalog Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 建立可机器查询、可人工核对的 Ozon 财务应计类型目录，并明确 Seller API `type_id` 与 Seller 页面内部 `accrual_type_ids` 是两个不同命名空间。

**Architecture:** `indexes/finance-accrual-types.json` 保存结构化映射、证据等级和 ZhiPin 投影字段；`docs/api/finance-accrual-types.md` 解释接口、类型语义、聚合规则和未知项处理。官方 operation 结构沿用 Chrome 抽取文档，运行时 ID 映射来自脱敏的生产 API、Seller 页面源码/筛选请求和 ZhiPin 实现证据。

**Tech Stack:** JSON、Markdown、Python `unittest`。

## Global Constraints

- 不记录真实账号、Client ID、API key、cookie、posting number 或金额。
- `seller_api_type_id` 与 `seller_ui_accrual_type_id` 不得互换。
- 未得到 `/v1/finance/accrual/types` 英文名的条目必须保留 `seller_api_name: null` 和证据说明，禁止猜名称。
- 只有 ZhiPin 当前明确消费的费用才能填写 `projection_field`；其余标为 `transaction_only` 或 `needs_policy`。

---

### Task 1: 结构化类型目录

**Files:**
- Create: `indexes/finance-accrual-types.json`
- Create: `tests/test_finance_accrual_types_catalog.py`

**Interfaces:**
- Produces: `entries[].seller_api_type_id` 作为 Seller API 主键。
- Produces: `entries[].seller_ui_accrual_type_id` 作为独立、可空的 Seller 页面内部 ID。
- Produces: `entries[].projection_field` 与 `entries[].projection_status` 表示 ZhiPin 消费边界。

- [x] **Step 1:** 写目录契约测试，校验 ID 唯一、双命名空间、已确认的 66/67/69 映射和合法投影字段。
- [x] **Step 2:** 运行 `python3 -m unittest tests/test_finance_accrual_types_catalog.py -v`，确认在索引不存在时失败。
- [x] **Step 3:** 创建 JSON 索引，录入已验证 ID、语义、页面交叉映射和证据等级。
- [x] **Step 4:** 重跑测试并通过。

### Task 2: 查询文档与来源追溯

**Files:**
- Create: `docs/api/finance-accrual-types.md`
- Modify: `docs/api/seller-api-index.md`
- Modify: `docs/source-notes/ZhiPin.md`
- Modify: `README.md`

**Interfaces:**
- Consumes: `indexes/finance-accrual-types.json`。
- Produces: 人工查询表、聚合/投影规则、已知未知项和来源引用。

- [x] **Step 1:** 写主题文档，区分 API、Seller 页面与旧 v3 transaction 三层语义。
- [x] **Step 2:** 更新导航和 ZhiPin source note，记录 2026-09-01 的脱敏运行证据。
- [x] **Step 3:** 运行 JSON 校验、全仓测试、敏感信息扫描和 `git diff --check`。
- [ ] **Step 4:** 提交并推送 `codex/add-finance-accrual-type-catalog`。

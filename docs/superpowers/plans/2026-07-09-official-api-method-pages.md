# Official API Method Pages Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 将 Chrome 抽取到的 264 个 Ozon Seller API operation 展开成逐方法中文 Markdown 文档，并保持可重复生成。

**Architecture:** 原始 Chrome 抽取结果继续以 `indexes/official-seller-api.operations.json` 作为事实源。新增 Python 生成器读取该 JSON，输出 `docs/api/official/` 下的总览页和每个 operation 的独立 Markdown 文件；测试覆盖命名、内容、计数和索引链接。

**Tech Stack:** Python 3 标准库、`unittest`、Markdown。

## Global Constraints

- 官方资料只能来自已经通过 Chrome 抽取的 `indexes/official-seller-api.operations.json`。
- 不提交真实 `Client-Id`、`Api-Key`、cookie、token、session、验证码、短信码或账号私有数据。
- 生成文件必须是中文说明，保留官方 `operationId`、HTTP method、path 和 sourceUrl。
- 生成器必须可重复运行，输出稳定，不能依赖网络。

---

### Task 1: Generator Tests

**Files:**
- Create: `tools/generate_official_api_docs.py`
- Create: `tests/test_generate_official_api_docs.py`

**Interfaces:**
- Produces: tests for `slugify_operation(operation) -> str`, `operation_group(operation) -> str`, `render_operation_doc(operation) -> str`, `generate_docs(index_path, output_dir) -> int`

- [ ] **Step 1: Write failing tests**

Create `tests/test_generate_official_api_docs.py` with tests that:
- build two sample operations;
- assert stable file names include method/path/operationId;
- assert generated Markdown contains title, method/path, headers, response table, examples and source URL;
- assert `docs/api/official/README.md` links to all generated operation files.

- [ ] **Step 2: Run test to verify it fails**

Run: `python3 -m unittest tests/test_generate_official_api_docs.py -v`
Expected: FAIL because `tools.generate_official_api_docs` does not exist yet.

### Task 2: Generator Implementation

**Files:**
- Create: `tools/generate_official_api_docs.py`

**Interfaces:**
- Consumes: `indexes/official-seller-api.operations.json`
- Produces: `docs/api/official/README.md` and one `.md` file per operation

- [ ] **Step 1: Implement generator**

Implement functions:
- `slugify_operation(operation) -> str`
- `operation_group(operation) -> str`
- `render_operation_doc(operation) -> str`
- `generate_docs(index_path, output_dir) -> int`
- CLI entrypoint with defaults `indexes/official-seller-api.operations.json` and `docs/api/official`

- [ ] **Step 2: Run tests to verify pass**

Run: `python3 -m unittest tests/test_generate_official_api_docs.py -v`
Expected: PASS.

### Task 3: Generate Full Official Docs

**Files:**
- Create: `docs/api/official/README.md`
- Create: `docs/api/official/*.md`

**Interfaces:**
- Consumes: generator from Task 2
- Produces: 264 method pages plus README

- [ ] **Step 1: Run generator**

Run: `python3 tools/generate_official_api_docs.py`
Expected: prints `generated 264 operation docs`.

- [ ] **Step 2: Verify output count**

Run: `find docs/api/official -maxdepth 1 -type f -name '*.md' | wc -l`
Expected: `265` because README plus 264 method pages.

### Task 4: Link Generated Docs

**Files:**
- Modify: `docs/api/seller-api-index.md`
- Modify: `docs/source-notes/official-seller-api-chrome.md`

**Interfaces:**
- Consumes: generated README path `docs/api/official/README.md`
- Produces: human navigation from existing API index and source note

- [ ] **Step 1: Update existing docs**

Add links to the generated full method directory and mention one file per operation.

- [ ] **Step 2: Verify links and scans**

Run:
- `python3 -m json.tool indexes/official-seller-api.operations.json >/tmp/official.check`
- `python3 -m unittest tests/test_generate_official_api_docs.py -v`
- `rg -n 'TODO|TBD|待补|占位|placeholder' README.md docs workflows skills tools tests || true`
- `rg -n 'Api-Key:|Client-Id:|cookie|token|secret|password|Authorization' README.md docs indexes workflows skills tools tests || true`

Expected: JSON parses; tests pass; placeholder scan only hits workflow/plan check-command text if any; secret scan contains no real credential values.

### Task 5: Commit and Push

**Files:**
- All generated docs, generator, tests, and doc links.

- [ ] **Step 1: Commit**

Run:
- `git status --short`
- `git add docs tools tests`
- `git commit -m "docs: expand official seller api methods"`

- [ ] **Step 2: Push**

Run: `git push origin main`
Expected: push succeeds and remote `main` updates.

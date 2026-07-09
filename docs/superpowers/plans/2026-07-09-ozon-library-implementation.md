# Ozon 资料库实施计划

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**目标:** 按已批准的设计搭建 `ozon-library` 第一版资料库，包含目录骨架、索引、workflow、仓库内 skill 和首批高价值中文主题文档。

**架构:** 采用“主题文档 + JSON 索引 + 仓库本地 skill/workflow”的结构。官方 Seller API 通过 Chrome DOM 抽取，三个本地项目通过源码扫描和人工归并提炼复用知识。

**Tech Stack:** Markdown、JSON、POSIX shell/`rg`、Chrome DOM extraction、Git。

## Global Constraints

- 官方 Seller API 文档必须通过当前 Chrome 页面抓取，不能用 `curl` 或外部下载代替。
- 文档主语言使用中文，保留必要英文术语、路径、operation ID、endpoint 和 selector。
- 资料库按可复用主题组织，不按项目重复堆内容。
- 每条非显而易见知识必须能追溯到源码路径或 Chrome operation ID。
- 不提交 credential、API key、cookie、token 或账号私有数据。
- 第一版不要求人工整理完全部 280 个官方 operation，但索引结构必须能扩展到全部 operation。

---

### Task 1: 建立仓库骨架和 README

**Files:**
- Create: `README.md`
- Create: `docs/api/.gitkeep`
- Create: `docs/seller-web/.gitkeep`
- Create: `docs/buyer-page/.gitkeep`
- Create: `docs/recovery/.gitkeep`
- Create: `docs/fields/.gitkeep`
- Create: `docs/flows/.gitkeep`
- Create: `docs/source-notes/.gitkeep`
- Create: `indexes/.gitkeep`
- Create: `workflows/.gitkeep`
- Create: `skills/ozon-library-maintainer/references/.gitkeep`

**Interfaces:**
- Produces: human/AI navigation entrypoint and stable directory layout.

- [ ] **Step 1: 创建目录和 README**

Use `apply_patch` to add directories via `.gitkeep` files and create a Chinese `README.md` explaining navigation, source policy, and no-secret policy.

- [ ] **Step 2: 验证目录**

Run: `find . -maxdepth 3 -type d | sort`

Expected: planned top-level directories are present.

- [ ] **Step 3: Commit**

```bash
git add README.md docs indexes workflows skills
git commit -m "docs: scaffold ozon library"
```

### Task 2: 写入 workflow 和仓库本地 skill

**Files:**
- Create: `workflows/ozon-library-update.md`
- Create: `workflows/chrome-official-seller-api-extract.md`
- Create: `workflows/project-source-extract.md`
- Create: `workflows/dedupe-and-merge.md`
- Create: `skills/ozon-library-maintainer/SKILL.md`
- Create: `skills/ozon-library-maintainer/references/repository-map.md`
- Create: `skills/ozon-library-maintainer/references/source-map.md`

**Interfaces:**
- Consumes: design spec.
- Produces: repeatable repository-local maintenance workflow for future AI sessions.

- [ ] **Step 1: 写 workflow 文档**

Create Chinese workflow docs covering update sequence, Chrome-only official extraction, local `rg` source scanning, and dedupe/merge rules.

- [ ] **Step 2: 写 repository-local skill**

Create `SKILL.md` with frontmatter:

```yaml
---
name: ozon-library-maintainer
description: Use when maintaining the ozon-library repository, refreshing Ozon Seller API documentation from Chrome, scanning AICollection/simple-collection/ZhiPin sources, or merging reusable Ozon knowledge into topic docs.
---
```

Keep the skill concise and point to references for source maps.

- [ ] **Step 3: 验证 skill 基本结构**

Run: `test -f skills/ozon-library-maintainer/SKILL.md && sed -n '1,40p' skills/ozon-library-maintainer/SKILL.md`

Expected: frontmatter and first instructions are visible.

- [ ] **Step 4: Commit**

```bash
git add workflows skills
git commit -m "docs: add ozon maintainer workflows"
```

### Task 3: 生成官方 Seller API operation 索引

**Files:**
- Create: `indexes/official-seller-api.operations.json`
- Create: `docs/source-notes/official-seller-api-chrome.md`

**Interfaces:**
- Consumes: current Chrome tab `https://docs.ozon.ru/api/seller/zh/?__rr=1`.
- Produces: JSON operation index and source note.

- [ ] **Step 1: 通过 Chrome DOM 抽取 operation**

Use Chrome browser control and `tab.playwright.evaluate` to extract every `div[id^="operation/"]` into JSON fields:

```json
{
  "operationId": "ProductAPI_ProductsStocksV2",
  "title": "更新库存商品的数量",
  "method": "post",
  "path": "/v2/products/stocks",
  "headings": [],
  "tables": [],
  "examples": [],
  "sourceUrl": "https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/ProductAPI_ProductsStocksV2"
}
```

- [ ] **Step 2: 写入索引文件**

Write valid pretty JSON to `indexes/official-seller-api.operations.json`. The file must include `captured_at`, `source_url`, `operation_count`, and `operations`.

- [ ] **Step 3: 写官方来源 note**

Document Chrome extraction method, observed operation count, important sections, and source constraints.

- [ ] **Step 4: 验证 JSON**

Run: `python3 -m json.tool indexes/official-seller-api.operations.json >/tmp/ozon-api-index.check`

Expected: exit 0.

- [ ] **Step 5: Commit**

```bash
git add indexes/official-seller-api.operations.json docs/source-notes/official-seller-api-chrome.md
git commit -m "docs: index official seller api from chrome"
```

### Task 4: 生成本地项目来源索引

**Files:**
- Create: `indexes/source-files.json`
- Create: `indexes/endpoint-cross-reference.json`
- Create: `indexes/dom-selectors.json`
- Create: `docs/source-notes/AICollection.md`
- Create: `docs/source-notes/ZhiPin.md`
- Create: `docs/source-notes/simple-collection.md`

**Interfaces:**
- Consumes: `/Users/eric/works/AICollection`, `/Users/eric/works/simple-collection`, `/Users/eric/works/ZhiPin`.
- Produces: source/path/topic indexes and project source notes.

- [ ] **Step 1: 扫描 Ozon 相关文件**

Use `rg -l -i` with topic keywords for Ozon, Seller, slider, adult, NoConnection, API keys, endpoint paths, DOM selectors, and recovery markers.

- [ ] **Step 2: 生成 source-files 索引**

Create JSON entries with `project`, `path`, `relative_path`, and `topics`.

- [ ] **Step 3: 生成 endpoint cross-reference**

Extract `/vN/...` endpoint strings and `seller.ozon.ru/api/...` URLs from the highest-value source directories.

- [ ] **Step 4: 生成 DOM selector 索引**

Extract stable-looking selectors such as `data-widget`, `userAdultModal`, `webSale`, `sellerTransparency`, and important querySelector constants.

- [ ] **Step 5: 写项目 source notes**

Summarize what each project contributes and list priority files.

- [ ] **Step 6: 验证 JSON**

Run:

```bash
python3 -m json.tool indexes/source-files.json >/tmp/source-files.check
python3 -m json.tool indexes/endpoint-cross-reference.json >/tmp/endpoints.check
python3 -m json.tool indexes/dom-selectors.json >/tmp/dom-selectors.check
```

Expected: all exit 0.

- [ ] **Step 7: Commit**

```bash
git add indexes docs/source-notes
git commit -m "docs: index local ozon source projects"
```

### Task 5: 写首批高价值主题文档

**Files:**
- Create: `docs/api/seller-api-index.md`
- Create: `docs/api/seller-api-auth.md`
- Create: `docs/api/product.md`
- Create: `docs/api/stock-price.md`
- Create: `docs/api/posting-fbs.md`
- Create: `docs/seller-web/seller-internal-apis.md`
- Create: `docs/buyer-page/product-page-dom.md`
- Create: `docs/buyer-page/list-page-dom.md`
- Create: `docs/buyer-page/adult-verification.md`
- Create: `docs/buyer-page/no-connection-and-block.md`
- Create: `docs/recovery/page-state-classification.md`
- Create: `docs/recovery/slider-captcha.md`
- Create: `docs/recovery/antibot-incident.md`
- Create: `docs/recovery/rate-limit.md`
- Create: `docs/fields/product-fields.md`
- Create: `docs/flows/sku-collection.md`
- Create: `docs/flows/batch-listing.md`

**Interfaces:**
- Consumes: generated indexes, source notes, official operation index, and high-value source files.
- Produces: curated topic docs with source references.

- [ ] **Step 1: 写 API 主题文档**

Use official operation index and ZhiPin client mixins to document auth, products, stock/price, and FBS postings.

- [ ] **Step 2: 写 Seller web 主题文档**

Use AICollection and ZhiPin Seller web API sources to document `search`, `create-bundle`, `what_to_sell/data/v3`, `get_sellers`, and delivery template APIs.

- [ ] **Step 3: 写 buyer page / DOM / recovery 文档**

Use AICollection scraper and ZhiPin/simple-collection extension sources to document DOM selectors, page-state classification, adult verification, NoConnection/block, slider, antibot incident, and rate limits.

- [ ] **Step 4: 写 fields 和 flows 文档**

Summarize product fields and the SKU/batch-listing flows with source references.

- [ ] **Step 5: 文档质量检查**

Run:

```bash
rg -n 'TODO|TBD|待补|占位|placeholder' README.md docs workflows skills || true
rg -n 'Api-Key:|Client-Id:|cookie|token|secret|password' README.md docs indexes workflows skills || true
```

Expected: no placeholder hits; secret scan may show policy text but no real credential values.

- [ ] **Step 6: Commit**

```bash
git add docs README.md indexes workflows skills
git commit -m "docs: add first ozon knowledge topics"
```

### Task 6: 最终验证和交付

**Files:**
- Modify: none unless validation finds issues.

**Interfaces:**
- Consumes: complete repository state.
- Produces: verification evidence and clear status.

- [ ] **Step 1: 验证 JSON 和链接引用**

Run:

```bash
python3 -m json.tool indexes/official-seller-api.operations.json >/tmp/official.check
python3 -m json.tool indexes/source-files.json >/tmp/source.check
python3 -m json.tool indexes/endpoint-cross-reference.json >/tmp/endpoint.check
python3 -m json.tool indexes/dom-selectors.json >/tmp/dom.check
find . -maxdepth 3 -type f | sort
```

- [ ] **Step 2: 检查 Git 状态**

Run: `git status --short && git log --oneline --max-count=8`

- [ ] **Step 3: 总结交付**

Report created docs, indexes, workflows, local skill, verification commands, and remaining recommended follow-up work.

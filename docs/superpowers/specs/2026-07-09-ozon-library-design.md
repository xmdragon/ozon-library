# Ozon Library Design

## Goal

Build `xmdragon/ozon-library` into a reusable Ozon knowledge base for AI agents and human review. The repository should consolidate knowledge from four sources:

- `/Users/eric/works/AICollection`
- `/Users/eric/works/simple-collection`
- `/Users/eric/works/ZhiPin`
- The currently opened Ozon Seller API documentation in Chrome

The library must emphasize reusable Ozon concepts instead of copying each project separately. Project-specific details remain traceable through source references and source notes.

## Context Observed

`ozon-library` is currently an empty repository on branch `main`.

The active local projects are under `/Users/eric/works`:

- `AICollection`: large Ozon desktop/scraper implementation with WebView, page-state classification, slider handling, adult verification, queue recovery, Seller web APIs, product scraping, and changelogs.
- `ZhiPin`: large Ozon backend, extension, Seller API client, seller login, seller internal API, models, migrations, web UI, and older spider implementation.
- `simple-collection`: smaller browser-extension and capture-oriented project, useful for Ozon DOM capture, API capture, list/card extraction, currency/language handling, and runtime resilience.
- Chrome Seller API page: `https://docs.ozon.ru/api/seller/zh/?__rr=1`, rendered as Redoc with about 280 operation blocks. Each operation block is extractable from Chrome DOM by `id="operation/<operationId>"` and includes method/path, parameters, request schema, response schema, and examples.

Official Seller API documentation must be captured through Chrome, not through direct `curl` or external downloads.

## Design Decision

Use a topic-first knowledge base with source references.

This avoids duplicating shared logic from AICollection and ZhiPin. The project-specific source folders become provenance and delta notes, while reusable knowledge lives under stable topic areas.

Rejected alternatives:

- Source-first organization: easier to trace, but creates duplicate docs and makes AI retrieval noisier.
- Machine-index-only organization: good for scripts, but poor for human browsing and slower to bootstrap.

The selected design combines Markdown topic docs with JSON indexes for scripted refresh and AI lookup.

## Repository Structure

```text
ozon-library/
  README.md
  docs/
    api/
      seller-api-index.md
      seller-api-auth.md
      product.md
      stock-price.md
      posting-fbs.md
      warehouse.md
      reports-finance-chat.md
    seller-web/
      login-flow.md
      seller-internal-apis.md
      seller-data-v3.md
      search-and-create-bundle.md
      delivery-template-apis.md
    buyer-page/
      product-page-dom.md
      list-page-dom.md
      price-fields.md
      adult-verification.md
      no-connection-and-block.md
    recovery/
      page-state-classification.md
      slider-captcha.md
      antibot-incident.md
      rate-limit.md
      webview-recovery.md
    fields/
      product-fields.md
      seller-fields.md
      stock-price-fields.md
      posting-fields.md
      category-attribute-fields.md
    flows/
      sku-collection.md
      batch-listing.md
      seller-cookie-session.md
      category-attribute-sync.md
      price-stock-sync.md
    source-notes/
      AICollection.md
      ZhiPin.md
      simple-collection.md
      official-seller-api-chrome.md
  indexes/
    official-seller-api.operations.json
    source-files.json
    endpoint-cross-reference.json
    dom-selectors.json
  workflows/
    ozon-library-update.md
    chrome-official-seller-api-extract.md
    project-source-extract.md
    dedupe-and-merge.md
  skills/
    ozon-library-maintainer/
      SKILL.md
      references/
        repository-map.md
        source-map.md
```

## Documentation Format

Each topic Markdown file should use this shape:

```markdown
# Title

## Purpose
What problem this knowledge solves.

## AI Summary
The short, high-signal version an agent should read first.

## Applies To
Where this knowledge is valid, including project/runtime boundaries.

## Key Interfaces
Tables for APIs, DOM selectors, fields, request payloads, response payloads, events, or status values.

## Flow
Actual sequence of calls, DOM checks, state transitions, or recovery steps.

## Exceptions And Recovery
Known errors, blocked states, rate limits, fallback paths, retry limits, and when to stop.

## Source References
Absolute local source paths or official Chrome operation IDs used to derive this document.
```

Every extracted fact should be traceable. If a fact appears in more than one project, record the common behavior in the topic doc and project-specific differences in `docs/source-notes/`.

## Official Seller API Capture

Official Seller API content must come from Chrome.

The current page exposes operation sections like:

- `operation/ProductAPI_ImportProductsV3`
- `operation/ProductAPI_ProductsStocksV2`
- `operation/PostingFbsList`
- `operation/AccessAPI_RolesByToken`

The extractor should use Chrome/Playwright DOM evaluation to project each operation block into a compact JSON object:

```json
{
  "operationId": "ProductAPI_ProductsStocksV2",
  "title": "更新库存商品的数量",
  "method": "post",
  "path": "/v2/products/stocks",
  "headings": [],
  "headerParameters": [],
  "requestSchemaText": "",
  "responseSchemaText": "",
  "requestExamples": [],
  "responseExamples": [],
  "sourceUrl": "https://docs.ozon.ru/api/seller/zh/?__rr=1#operation/ProductAPI_ProductsStocksV2"
}
```

The initial extract should prioritize:

- Authorization, `Client-Id`, `Api-Key`, key expiration, rate limits, CORS/backend-only rule.
- Product import, attributes, pictures, product list, product info.
- Stock and price updates.
- FBS/rFBS postings.
- Warehouses and delivery methods.
- Reports, finance, chat, and roles.
- Deprecated endpoints and replacement endpoints.

## Project Source Extraction

The local projects should be scanned into indexes first, then merged into docs.

Important source categories:

- Seller API backend client: `ZhiPin/plugins/ef/channels/ozon/api/client.py` and `client_mixins/*`.
- Seller web internal API: `AICollection/src-tauri/crates/scraper/src/services/ozon_seller.rs`, `AICollection/src-tauri/crates/scraper/src/browser/seller.rs`, `ZhiPin/ozon_spider/seller_login.py`.
- Buyer page DOM and product data extraction: AICollection scraper pipeline, ZhiPin extension product/list modules, simple-collection extension.
- Page state and recovery: AICollection `page_state.rs`, `ozon_rate_limit.rs`, `challenge.rs`, slider modules, queue recovery, adult verification code.
- Browser extension DOM structure: ZhiPin extension `seller-page`, `product-page`, `shop-binding`, `list-enhancer`; simple-collection `content.js`, `api_parser.js`, `page_capture.js`.
- Database/model fields: ZhiPin Ozon models and migrations, AICollection backend and Tauri stores.
- Changelog/incidents: AICollection `docs/changelog/*ozon*`, related task notes, and ZhiPin tests/docs where behavior was fixed.

Indexes should record file paths, matched topics, endpoints, selectors, status strings, and notable comments. They should not replace curated topic docs.

## Reuse Extraction Rules

When the same behavior appears in multiple projects:

1. Put the shared behavior in the topic document.
2. Put implementation differences in `docs/source-notes/<project>.md`.
3. Link every source path that supports the behavior.
4. Prefer current AICollection behavior when it represents a later fix for older ZhiPin logic.
5. Preserve older ZhiPin/simple-collection behavior when it reveals a fallback, legacy endpoint, or historical incident.
6. Mark unstable Ozon DOM selectors as "observed selectors" rather than permanent contracts.

Examples of reusable knowledge units:

- Ozon page-state classification: content page, NoConnection, Chrome error, block page, slider captcha, antibot incident, adult birthday form, adult confirm-only page.
- Slider handling: detection markers, image assets, solve attempt, retry/rotate behavior, cancellation/pause propagation.
- Adult verification: userAdultModal, birthday input, confirm-only path, 403-sensitive endpoint behavior, DOM-first submit in newer code.
- Seller API headers and rate limits.
- Seller web internal API calls that require logged-in browser context and `credentials: include`.
- Product price extraction after Ozon changed `webPrice` to `webSale`.
- Seller page widget injection and reinjection via MutationObserver.
- SKU search plus create-bundle flow for Seller-side product details.

## Repository Skill / Workflow

Create a repository-local skill at `skills/ozon-library-maintainer/SKILL.md`.

The skill is not installed globally. It should guide future Codex sessions when maintaining this repository.

It should instruct agents to:

- Read `README.md`, `workflows/ozon-library-update.md`, and `indexes/source-files.json` first.
- Use Chrome for official Seller API extraction.
- Use local source scans for the three project repositories.
- Update indexes before editing topic docs.
- Merge by reusable topic, not by project.
- Preserve source references for every non-obvious fact.
- Treat Ozon DOM and Seller internal APIs as unstable and annotate observation dates.
- Avoid including credentials, API keys, cookies, tokens, or private account data.

## Workflows

`workflows/ozon-library-update.md` should define the top-level refresh sequence:

1. Confirm source paths and Git revisions for AICollection, simple-collection, and ZhiPin.
2. Confirm Chrome has the official Seller API page open.
3. Extract official operations through Chrome DOM into `indexes/official-seller-api.operations.json`.
4. Scan local projects into `indexes/source-files.json`, `endpoint-cross-reference.json`, and `dom-selectors.json`.
5. Compare indexes with existing docs.
6. Update topic docs for new or changed reusable knowledge.
7. Update source notes with project-specific deltas.
8. Run link/reference validation.
9. Commit changes with source revisions in the commit message or update note.

`workflows/chrome-official-seller-api-extract.md` should document the Chrome-only extraction method.

`workflows/project-source-extract.md` should document `rg` patterns, path priorities, and topic routing.

`workflows/dedupe-and-merge.md` should document how to resolve duplicate or conflicting findings.

## Validation

The first implementation should be considered successful when:

- The repository has the planned directory structure.
- README explains how humans and AI should navigate the library.
- At least one official Seller API operation index is generated from Chrome, with enough structure to scale to all operations.
- Source indexes include the three local projects and classify files by topic.
- Initial topic docs exist for the highest-value reusable areas:
  - Seller API auth and request rules.
  - Product import/list/info.
  - Stock and price updates.
  - Seller web internal APIs.
  - Product/list page DOM.
  - Page-state classification.
  - Slider captcha.
  - Adult verification.
  - NoConnection/block/antibot incident recovery.
- Repository-local skill and workflows are present.
- No secrets, cookies, tokens, or account-specific private data are committed.

## Open Implementation Notes

The implementation plan should avoid trying to fully curate all 280 official operations in one pass. It should first build:

- the skeleton,
- the extraction scripts or Chrome snippets,
- the indexes,
- the highest-value docs,
- and the maintainer workflow.

After that, the remaining official Seller API sections can be filled incrementally from the generated operation index.

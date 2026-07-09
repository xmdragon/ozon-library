# Ozon 资料库更新流程

## 目标

把官方 Seller API、AICollection、simple-collection、ZhiPin 中新增或变化的 Ozon 知识合并进本仓库，并保持资料可追溯、可复用、可被 AI 快速检索。

## 更新顺序

1. 确认来源路径和 Git revision：
   - `/Users/eric/works/AICollection`
   - `/Users/eric/works/simple-collection`
   - `/Users/eric/works/ZhiPin`
2. 确认 Chrome 打开 Ozon Seller API 官方文档：`https://docs.ozon.ru/api/seller/zh/?__rr=1`。
3. 按 `workflows/chrome-official-seller-api-extract.md` 通过 Chrome DOM 更新 `indexes/official-seller-api.operations.json`。
4. 按 `workflows/project-source-extract.md` 扫描三个项目，更新：
   - `indexes/source-files.json`
   - `indexes/endpoint-cross-reference.json`
   - `indexes/dom-selectors.json`
5. 对比索引变化，找出新增 endpoint、selector、状态标记、异常处理和流程变化。
6. 按 `workflows/dedupe-and-merge.md` 合并到主题文档。
7. 更新 `docs/source-notes/` 中的项目差异。
8. 运行 JSON 校验和敏感信息扫描。
9. 提交时说明来源 revision 和本次更新主题。

## 合并原则

- 主题文档记录可复用知识。
- source notes 记录项目差异、历史实现和证据路径。
- 官方 API 以 Chrome DOM 抽取为准。
- Ozon DOM selector 和 Seller 内部 API 都视为不稳定观察值。
- 不提交任何账号私密数据。

## 推荐校验命令

```bash
python3 -m json.tool indexes/official-seller-api.operations.json >/tmp/official.check
python3 -m json.tool indexes/source-files.json >/tmp/source.check
python3 -m json.tool indexes/endpoint-cross-reference.json >/tmp/endpoint.check
python3 -m json.tool indexes/dom-selectors.json >/tmp/dom.check
rg -n 'TODO|TBD|待补|占位|placeholder' README.md docs workflows skills || true
rg -n 'Api-Key:|Client-Id:|cookie|token|secret|password' README.md docs indexes workflows skills || true
```

第二条敏感信息扫描允许命中“不要提交 token”这类政策文字，但不能命中真实密钥、cookie 或账号数据。

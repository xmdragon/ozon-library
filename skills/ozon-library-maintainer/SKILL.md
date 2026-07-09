---
name: ozon-library-maintainer
description: Use when maintaining the ozon-library repository, refreshing Ozon Seller API documentation from Chrome, scanning AICollection/simple-collection/ZhiPin sources, or merging reusable Ozon knowledge into topic docs.
---

# Ozon Library Maintainer

## 必读入口

先读：

1. `README.md`
2. `workflows/ozon-library-update.md`
3. `references/repository-map.md`
4. `references/source-map.md`

## 工作规则

- 官方 Seller API 只能从当前 Chrome 页面抽取。
- 本地项目先扫描成 `indexes/`，再整理进 `docs/`。
- 按可复用主题合并，不按项目重复搬运。
- 每条非显而易见知识都保留源码路径、operation ID 或 source note。
- Ozon DOM selector 和 Seller 内部 API 视为不稳定观察值。
- 不提交 credential、API key、cookie、token、验证码、短信码或账号私有数据。

## 更新流程

1. 按 `workflows/ozon-library-update.md` 确认来源路径和 Git revision。
2. 需要官方 API 时，按 `workflows/chrome-official-seller-api-extract.md` 抽取 Chrome DOM。
3. 需要项目更新时，按 `workflows/project-source-extract.md` 扫描源码。
4. 按 `workflows/dedupe-and-merge.md` 合并重复知识。
5. 更新主题文档和 source notes。
6. 运行 JSON 校验和敏感信息扫描。

## 输出风格

文档用中文写，保留必要英文术语、endpoint、operation ID、字段名和 selector。优先写结论、适用范围、流程、异常恢复和来源引用。

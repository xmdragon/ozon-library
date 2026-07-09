# simple-collection 来源记录

## 用途

记录 `/Users/eric/works/simple-collection` 对 Ozon 资料库的贡献范围、当前 revision 和优先阅读路径。

## AI 摘要

simple-collection 是一个轻量浏览器扩展/API 捕获来源。它适合补充 Ozon 列表页卡片解析、API 捕获、页面捕获、币种语言入口、登录状态检测和运行时韧性测试。

## 当前来源

- 路径：`/Users/eric/works/simple-collection`
- 分支：`main`
- revision：`f90435de9da7db907e543cf427585bdf3531c92f`
- 相关文件索引：见 `indexes/source-files.json`

## 重点贡献

| 主题 | 说明 | 优先路径 |
| --- | --- | --- |
| Ozon 入口 | 中国商品 highlight 目标页、打开/跳转逻辑 | `extension/src/content.js`、`extension/src/background.js` |
| 列表页卡片 | `shortCard`、`tile-root`、商品链接、评分、评论、价格字段 | `extension/src/content.js` |
| 页面状态 | 登录检测、币种语言控件、运行时异常处理 | `extension/src/content.js` |
| API 捕获 | 页面 API 捕获和解析 | `extension/src/api_parser.js`、`extension/src/page_capture.js` |
| 测试 | API capture、品牌面包屑、运行时韧性 | `tests/` |

## 合并规则

simple-collection 的实现通常作为轻量 DOM/capture 参考，不覆盖 AICollection 或 ZhiPin 的完整业务流程。若它的 selector 更简单或更稳定，可作为 fallback 写入 buyer-page 主题文档。

## 来源引用

- `indexes/source-files.json`
- `indexes/dom-selectors.json`

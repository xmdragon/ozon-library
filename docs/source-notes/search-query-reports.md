# 搜索查询报告：来源与验证状态

这是对两个项目设计资料的定向整理，不是对全部源码的重新扫描，也不是新的 Ozon 实测记录。

| 来源 | 读取版本 | 用途 |
| --- | --- | --- |
| [AICollection #2181](https://github.com/xmdragon/AICollection/pull/2181) | `6f9676325dcd1be1bf3c741bce207543a8ecf188` | 接收、永久快照、同周期动态比较、读权限和 Manager 展示 |
| [ZhiPin #481](https://github.com/xmdragon/ZhiPin/pull/481) | `ef7c4762f1fbfc8abc9e87bd04cab996dacee45d` | Seller 报告流程、18 字段应用契约、双周期调度及投递 |
| 用户本轮说明 | KISS；参考分析允许10%以内错误，不要求100%正确或及时 | 降低先前审查补充的实现门槛，不改变基本鉴权和历史保留 |

原计划文件：

- [AICollection 快照计划（固定版本）](https://github.com/xmdragon/AICollection/blob/6f9676325dcd1be1bf3c741bce207543a8ecf188/docs/superpowers/plans/2026-09-20-ozon-search-snapshots.md)
- [ZhiPin 报告计划（固定版本）](https://github.com/xmdragon/ZhiPin/blob/ef7c4762f1fbfc8abc9e87bd04cab996dacee45d/docs/plans/2026-09-20-ozon-search-report-sync.md)

两个读取版本仍是文档计划。先前 review-addendum 中的完整性、恢复和验收要求并非全部继续适用；当前实现取舍见[主题文档](../seller-web/search-query-reports.md)。计划中的请求路径、字段和18列说法不能升级成已通过真实报告验证的事实。

本轮未取得真实 metrics 数组、原始表头、创建/状态响应及真实报告样本，也未调用 Ozon。未知项只影响对应上游接线的确认，不阻塞数据库、查询和页面实现；联调获得资料后在本主题补充，不再要求预先准备一套穷举 fixture。

机器检索入口：[来源索引](../../indexes/search-query-report-sources.json)。不改写官方 API 抽取索引，不提交 Cookie、账号信息、密钥或完整业务报告。

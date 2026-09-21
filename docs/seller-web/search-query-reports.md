# Ozon 搜索查询报告与每日快照（KISS）

## 结论与适用范围

用于选品和趋势参考，不是财务结算、审计或实时监控。用户已明确：持续迭代、保持 KISS，允许10%以内错误，不要求100%正确和及时。首版优先跑通常用链路；不为补齐极端边界增加通用框架或恢复系统。

“10%”是业务容忍度，不是已测出的准确率，也不自动定义为“可以删除每份报告10%的行”。目前没有统一统计分母或测量窗口；不增加 SLO/误差预算系统，不承诺已经达到90%准确率。偶发漏词、延迟或缺少某天某周期可以接受，但展示实际日期和已知缺失，不伪造数据。

**证据状态：** 下列 Ozon 请求路径和18字段来自两份项目计划，尚非本次实测协议。`metrics` 真实枚举、原始 Excel 表头、状态响应及单位仍待联调确认。应用侧约定与上游实际字段明确分开；详见[来源说明](../source-notes/search-query-reports.md)和[检索索引](../../indexes/search-query-report-sources.json)。

## 一、职责与最小链路

```text
ZhiPin 已有 Seller 会话池
  → 创建 / 等待 / 下载 7天报告、28天报告
  → 解析有效行，经服务鉴权投递
AICollection
  → 快照主表 + 明细表
  → 最新快照 / 指定区间首尾比较 API
  → Manager Web；桌面端本阶段只提供 API
```

ZhiPin 负责取数，AICollection 是唯一历史保存方。不新增 ZhiPin 历史库、不持久化比较结果、不增加官方 API 第二数据源，也不在 AICollection 配置 Seller Client ID/API Key。沿用现有 ARQ、数据库、鉴权和 Web 组件。

## 二、Seller 内部报告接口：计划记录，待实测确认

以下基址为 `https://seller.ozon.ru`，属于 Seller 登录态内部接口，不是 `api-seller.ozon.ru` 的官方 Seller API：

| 方法及路径 | 计划用途 |
| --- | --- |
| `POST /api/v1/report/searchstat_analytics/search_queries` | 创建报告 |
| `GET /api/v1/report/status/{code}` | 查询状态 |
| `GET /api/v1/report/download/{code}` | 下载 XLSX |

计划中的创建参数：

| 字段 | 计划值 / 当前确认状态 |
| --- | --- |
| `period` | `SearchQueriesPeriod_days_7` 或 `SearchQueriesPeriod_days_28` |
| `sortBy` | `count` |
| `sortDir` | `SortDir_desc` |
| `text` | 空字符串 |
| `presetName` | 原计划为 `所有指标`，实际请求是否依赖语言待确认 |
| `metrics` | 原计划只给出符号 `SEARCH_QUERY_REPORT_METRICS`；实际数组未取得，不能据18个应用字段反推或填空数组 |

请求沿用已有 Seller 会话身份、company id、必要头和限流。账号没有报告权限时尝试池内下一个可用账号，不把“不能下载本报告”等同于所有业务的登录态失效。已有正常调用链优先，不新建浏览器/会话管理器。

创建响应中 code 的位置、状态值和生成时间字段须在首次联调确认；本页不提供猜测的可执行请求，也不把计划中的 `success` / `failed` 当作已经观察到的枚举。确认后在本页补一份脱敏请求/响应及最小表头样例即可，7/28各做常规验证，不要求穷举所有状态样本。

## 三、18个应用字段：不是原始表头映射

下面是 ZhiPin → AICollection 拟定的 JSON 字段。含义为计划命名解释，需以真实列标题和单位核对；不是已核实的俄文列名、指标公式或去重范围。

| 字段 | wire 类型 | 计划含义 |
| --- | --- | --- |
| `query` | string | 搜索词原文，数字词仍为字符串 |
| `popularity` | int | 热度；本系统增长/衰减排名主指标 |
| `dynamics_28d` | decimal string 或 null | 上游28天动态，仅展示 |
| `dynamics_7d` | decimal string 或 null | 上游7天动态，仅展示 |
| `cart_add_users` | int | 加购用户数 |
| `cart_conversion` | decimal string | 加购转化率 |
| `order_users` | int | 下单用户数 |
| `order_conversion` | decimal string | 下单转化率 |
| `gmv_rub` | decimal string | 销售额（卢布） |
| `avg_price_rub` | decimal string | 平均价格（卢布） |
| `avg_items_viewed` | decimal string | 平均浏览商品数 |
| `avg_sellers_viewed` | decimal string | 平均浏览卖家数 |
| `no_action_queries` | int | 无后续行为查询数 |
| `no_action_share` | decimal string | 无后续行为占比 |
| `similar_result_queries` | int | 相似结果查询数 |
| `similar_result_share` | decimal string | 相似结果占比 |
| `zero_result_queries` | int | 无结果查询数 |
| `zero_result_share` | decimal string | 无结果占比 |

解析只覆盖实际遇到的报告布局。依据已确认表头/列坐标取值，不因增加一个无关列或列顺序变化就机械拒绝整份报告；也不能丢掉空单元格后顺移所有指标。识别不了关键列或统计期间时，本周期失败并显示旧数据，不猜字段。

Decimal 沿用项目惯例；有效0与缺失分开，已确认的动态缺失标记映射null。极少数非法行可跳过并记录读入/有效/跳过数，发送 `row_count` 以实际有效行为准；已声明非空字段不擅自补0或null。先做日志与简短提示，不建立质量评分表。明显大量坏行、错列或空文件不强行发布；不把轻微缺失升级成跨系统修复工程。

## 四、每日同步：尽力而为，不保证零漏日

- 每天 `Asia/Shanghai` 06:00 触发；Worker 为UTC时对应 `0 22 * * *`。7/28分别处理，一个失败不妨碍另一个保存。
- Worker启动时复用同一入口：06:00前不自动补采，之后检查当天缺少的周期。已有快照直接跳过。
- 临时失败使用现有能力做少量、有截止时间的重试；失败记录日期、周期、阶段和已有错误码。重试耗尽允许当天缺失，可人工重跑或等下一次，不要求同日必达。
- 报告生成等待和调用方timeout统一成可用的一组预算即可；不新增多层deadline管理器、分布式租约、持久化补偿队列或跨午夜任务恢复。跨日拿到的报告按真实抓取业务日记录，不回填成未采到的过去日期。

不新增为了10%容错而设计的状态机/报警平台。已有锁或任务去重能直接复用就用；不把所有部署/取消/午夜组合的测试作为首版门槛。

## 五、快照与跨服务约定

快照主表 + 明细表即可。每天分别保存7天与28天报告，永久保留；唯一键 `(snapshot_date, source_period_days)`，明细按 `(snapshot_id, query)` 在本快照内去重，不能跨日期只保留一条词记录。

同日同周期已存在就返回已有ID、不覆盖，明确 `outcome=already_exists`，不声称此次新内容已入库。并发重复由数据库唯一约束兜底；不增加内容冲突协调或自动修复流程。解析后有效明细与主表一起提交，不用保存“处理中/发布中”的复杂状态。

沿用原计划来源元信息：业务日期、7/28周期、报告实际期间、report code、来源账号标识、行数、schema版本与内容摘要。实际期间从报告取，不从本地日期编造。`source_generated_at` 无真实来源时允许null，另记 `source_fetched_at`；这项调整在两端实现时同步，不伪装成旧wire已支持。

沿用checksum时只保持一个简单一致的规则：rows按原文query排序；完整字段，null保留；Decimal普通十进制字符串去小数尾零、负零为`0`；JSON使用 `ensure_ascii=False, sort_keys=True, separators=(',', ':'), allow_nan=False`；无BOM/末尾换行的UTF-8 bytes计算SHA-256。计数int、金额和比例string，不为此引入独立协议框架或要求穷举golden测试矩阵。两端一例契约测试足够起步。

原文不做翻译/词干/大小写合并；超长词或超出既有存储范围的少量行可以按解析异常记录跳过，不为其增加摘要碰撞处理体系。当前只收有效行，客户端与接收端必须使用同一校验和规范化规则。

### 接口与权限

| 路径 | 用途 |
| --- | --- |
| `GET /v1/internal/ozon-search/snapshots/exists?date=YYYY-MM-DD&period_days=7或28` | 查询当天同周期是否已保存 |
| `POST /v1/internal/ozon-search/snapshots` | 服务间导入 |
| `GET /v1/ozon-search/latest?period_days=7或28` | 最新快照；支持分页、关键词筛选和排序 |
| `GET /v1/ozon-search/compare?period_days=7或28&from_date=...&to_date=...` | 同周期区间对比与三个TOP100 |

保留HTTPS、服务密钥和普通用户订阅/管理员权限校验；共享密钥不进日志/前端。内部入口复用已有受保护反代，只放行需要的路径，不放开整段internal。保持既有请求体大小限制，不把鉴权错误当作“没有数据”。配置、Cookie、真实client id、报告代码不放入公开文档；公共读API不暴露来源账号诊断。

## 六、比较与展示

对明确的 `period_days`，只在请求日期范围内选最早和最晚快照，SQL按词连接计算，不扫描全部历史进内存，不新增比较表或缓存表。

| 榜单 | 定义与排序 |
| --- | --- |
| 新加词TOP100 | 结束存在、开始不存在；按结束热度降序 |
| 热度增长TOP100 | 首尾都有值且结束减开始大于0；按增加量降序 |
| 热度衰减TOP100 | 首尾都有值且结束减开始小于0；按下降量大小降序 |

新加词只是“相对起始快照新增”，不等于从未在市场出现。结束未返回的词不补零、不当成下降100%；基准为0时变化率为null。区间只有一份或没有快照就提示历史不足，范围有缺日时展示实际首尾日期，不假装连续完整。7/28为上游滚动统计窗口，不与比较跨度混淆，不将每日滚动值累加成总搜索量。

latest首次返回snapshot ID，翻页继续使用该ID，刷新/切周期再重置；轻量参数即可，不做版本协调系统。Web显示周期、实际统计期间、快照/采集日期以及简单缺失/过期提示；权限限定超级管理员，桌面读API沿用有效主/子账号及父账号校验。首版不新增桌面UI。

链接用原始query编码，`target="_blank" rel="noopener noreferrer"`：

```text
https://www.ozon.ru/search/?country=20&from_global=true&text={URL编码后的原词}
```

这里的链接参数不证明报告也按同一国家过滤。无需额外构建翻译、推荐或数据质量平台。

## 七、首版只验收主路径

用实际正常报告确认字段位置、热度和比例单位；验证7/28分别保存、跨日不覆盖、同日重复不插入、最新查询和三个榜单、基本鉴权及链接编码。一个周期失败不影响另一个，并能看出哪天的数据。发生过的bug再补针对性测试。

数据库、接口、页面可先推进；真正取数需要在接线时确认实际请求及列映射，但不要求先备齐所有上游状态、边缘Excel格式和全链路故障样本。没有完成的实测明确标注，不把缺少样本当作整个迭代项目的停工门槛。

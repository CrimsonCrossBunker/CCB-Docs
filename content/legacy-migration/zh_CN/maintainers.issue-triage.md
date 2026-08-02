## 当前 Issue 分流流程

分流的目标是把报告变成可执行工作，而不是尽快关闭。先确认仓库与版本，再区分缺陷、
功能、机制/平衡、JSON 内容、性能、文档和上游同步；分类以当前 Issue Forms、
`ISSUES.md`、`LABELS.md` 和治理政策为准。

### 首次检查

1. 搜索 open/closed CCB Issue，确认是否重复或已有更新证据。
2. 记录精确 CCB commit/release、平台、build 类型、SDL backend、Mod 列表和存档来源。
3. 检查复现步骤、expected/actual、日志和最小样例；缺少时提出一个具体、可回答的请求。
4. 判断是否涉及安全漏洞、凭据或私人数据；此类内容转到 `SECURITY.md` 的私下渠道。
5. 仅在有证据时设置 subsystem、confirmation 与 priority label，不用 label 承诺排期。

### 风险顺序

- crash、存档/地图数据丢失、不可逆兼容破坏和安全问题优先；
- 玩家物品/角色损失、严重回归和阻塞性 UI 其次；
- 一般错误、性能和可用性问题按影响与可复现性处理；
- 小型内容建议或未说明目标的数值变化不应伪装成已确认 bug。

“当前行为符合设计但希望改变”通常是 feature/balance proposal；“行为违背当前契约或
设计”才是 bug。不能确定时记录不确定性，不要用个人预期替代源码、测试或设计政策。

### 复现、关闭与重开

维护者可以自己复现，但不是每份报告都必须由 triager 完成完整调试。合理请求信息后仍
没有可复现证据，可以说明原因后关闭；duplicate、out of scope、superseded 或 rejected
也必须留下可理解理由。新日志、最小存档或新版本复现属于合理的重开证据。

### 交接实现

有人准备实现时，先评论预期范围并开 Draft PR。PR 应链接 Issue、指定 Responsible
human、记录测试与文档影响。分流者不要擅自指派不存在的 owner，也不要编造 CODEOWNERS
或 review team。

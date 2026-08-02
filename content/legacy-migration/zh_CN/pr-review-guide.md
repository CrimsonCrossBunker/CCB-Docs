## 当前 PR 审阅清单

审阅的目标是确认改动解决了所述问题，并与 CCB 契约、兼容性和维护政策一致。旧指南的
固定行数阈值和上游个人/Discord 角色不是 CCB 的合并权限模型；规模只用于提示审阅风险。

### 先读范围

- PR 描述是否能解释 problem、solution、alternatives、实际测试与剩余风险；
- diff 是否只包含实现目标所需内容，是否混入格式化、重构、生成物或本地文件；
- commit/PR stack 是否按依赖拆分并给出明确合并顺序；
- Responsible human 是否理解最终 diff，而不是只代填用户名。

### 对照权威来源

1. 运行时行为对照源码与测试。
2. JSON/Lua/API 对照 Schema、LuaLS、注册与生成清单。
3. 构建命令对照 CI、CMake、Makefile、Gradle 和验证脚本。
4. 贡献/治理对照 `AGENTS.md`、`CONTRIBUTING.md` 与 `GOVERNANCE.md`。
5. CCB-Docs 冲突时标记 stale 并修正文档，不让 prose 覆盖契约。

### 风险审阅

- 存档序列化、稳定 ID、Mod/Lua API、Android/desktop 与上游差异是否有迁移计划；
- gameplay/balance 是否有可审核理由和来源；
- 外部代码、数据、图像、声音或文本是否许可证兼容并保留 attribution；
- 生成文件是否由 generator 更新，generated diff 是否稳定；
- PR 描述中的文档 ID、相关 CCB-Docs PR 和生成引用影响是否完整。

### 验证证据

先运行最窄、最能失败的测试。审阅者应区分：实际通过、未运行、环境阻塞、与 diff 无关
的 flaky/master failure。不能因为 CI 是红色就盲改断言，也不能在没有日志时宣称失败无关。

### 批准与合并边界

Bot 不能批准自己的 PR，也不自动合并。启用非作者批准要求前，必须确认至少两名活跃、
愿意且有权限的人类审阅者。审阅 conversation、Draft 状态、stack 依赖和最终 source pin
都满足后，才由有权限的人类决定合并。

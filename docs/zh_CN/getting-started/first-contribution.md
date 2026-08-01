---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: getting-started.first-contribution
title: 第一次贡献
language: zh_CN
status: draft
source_paths:
- CONTRIBUTING.md
- GOVERNANCE.md
- .github/pull_request_template.md
authority: governance
verified_commit: 11748581a0df8651380cfb8ae37ae91baafe054d
verified_at: '2026-08-01'
generated: false
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
risk_group: governance
risk_level: high
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/551
stale_reason: null
search:
  exclude: true
---

# 第一次贡献

这条路线适合第一次修改 CCB 的贡献者，也适合需要为任务建立可靠上下文的
Agent。目标不是先读懂整个项目，而是完成一个范围明确、能够验证的修改。

## 1. 从权威事实开始

先确认任务属于哪个子系统，再读取根 `AGENTS.md` 和目标路径最近的嵌套
`AGENTS.md`。使用 `ai/project-map.yml` 找入口，使用 `ai/test-matrix.yml` 找验证
命令。

不要仅根据旧 Issue、搜索摘要或本站正文推断运行时行为；回到源码与测试确认。

## 2. 建立独立分支

从最新 `master` 创建一个只解决单一问题的分支。不要把本地缓存、构建产物或
不相关修改带进提交。尤其不要扫描、暂存或提交 `obj-lua/`。

## 3. 做最小修改并验证

修改公开 ID、Schema、LuaLS、注册信息或构建接口前，先查看调用者、生成规则和
已有测试。选择[构建与验证快速入口](../validation/quickstart.md)中的最小充分
检查，并准确记录实际运行结果。

## 4. 填写 PR 契约

每个 PR 必须填写：

- `Responsible human`：真实 GitHub 账号；
- `Documentation impact`：无影响、需要修改，或需要标记 stale；
- `Related CCB-Docs PR`：没有则写 `None`；
- `Affected documentation IDs`：Catalog 中的稳定 ID；
- `Generated reference impact`：是否影响 Schema、LuaLS、注册或生成清单。

AI 工具或模型无需披露，但责任不会交给工具。详见
[Responsible human 与贡献责任](../contributing/responsible-human.md)。

## 5. 处理跨仓库文档

文档 PR 可以在源码 PR 合并前准备，但必须保持 draft 并记录源码 PR。源码合并
后，用最终 commit 刷新 `verified_commit`、重新生成 Catalog 输出并再次验证，
然后才请求人类合并文档 PR。

完成标准是：审阅者能理解为什么改、改了什么、如何验证，以及文档和生成参考
是否受到影响。

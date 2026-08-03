---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: pr-review-guide
title: 旧文档迁移草稿：pr review
language: zh_CN
status: active
doc_type: explanation
audiences:
- new-contributor
- experienced-contributor
- maintainer
- mod-author
owners:
- CCB maintainers
reviewers:
- Documentation reviewers
review_interval_days: 365
last_human_reviewer: LYHGLYTX
source_paths:
- doc/reviewing_PR_guide.md
- CONTRIBUTING.md
- GOVERNANCE.md
- .github/pull_request_template.md
source_symbols: []
source_queries: []
source_fingerprint: f1a6de16e5c8539a8b0c58d2808291146446cbf4adc8ec5ac84ed12ce33b0225
authority: docs-explanation
verified_commit: c1b0f95c6d1b074fc49ee2a7976819c124b69047
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: dc7c8aa693a4539760d74e03cde82a1970515267162e59b92ae595d7fcb0435f
prerequisites: []
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: 'CCB contributors: thaelina; accepted inventory identities only. Source paths and Git history
  remain authoritative.'
example_validation_ids: []
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: governance
risk_level: normal
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/contributing/pr-review/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/contributing/pr-review/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/contributing/pr-review/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/contributing/pr-review/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/c1b0f95c6d1b074fc49ee2a7976819c124b69047
source_urls:
- path: doc/reviewing_PR_guide.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/reviewing_PR_guide.md
- path: CONTRIBUTING.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/CONTRIBUTING.md
- path: GOVERNANCE.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/GOVERNANCE.md
- path: .github/pull_request_template.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/.github/pull_request_template.md
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28pr-review-guide%29%3A+&body=Document+ID%3A+pr-review-guide%0ALanguage%3A+zh_CN%0AVerified+commit%3A+c1b0f95c6d1b074fc49ee2a7976819c124b69047%0A%0ADescribe+the+documentation+problem%3A%0A
---

# 旧文档迁移草稿：pr review

本页是 `pr-review-guide` 的迁移草稿页面。它记录 **1** 条冻结清单记录，但不把旧说明提升为运行时契约。

- Stable document IDs: `pr-review-guide`
- Target: `contributing/pr-review.md`
- Replacement: pr-review-guide
- Archive reason: —

## 清单记录

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| pr-review-guide | doc/reviewing_PR_guide.md | migrate_rewrite | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## 权威边界

运行时行为仍以 CCB 源码和测试为准；JSON/Lua/API 以 Schema、声明、注册信息和生成清单为准；构建以 CI、CMake、Makefile 与 Gradle 为准。本页只解释迁移状态、历史和可审核来源。若旧正文与当前契约冲突，应以契约为准。

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

## 历史与归属

清单中的已接受贡献者为：thaelina。许可证：CC-BY-SA-3.0。异常贡献者原始值没有导入或发布。

源清单冻结 commit 为 `0378ca2b84303cf614c617c9d9eaa50138cd21ff`；本次交叉仓验证 commit 为 `c1b0f95c6d1b074fc49ee2a7976819c124b69047`；聚合源指纹为 `f1a6de16e5c8539a8b0c58d2808291146446cbf4adc8ec5ac84ed12ce33b0225`。[过滤历史实验报告](/CCB-Docs/migration/filtered-history-experiment/)记录了为何不导入整个游戏仓库历史。

## CCB 中保留的正文

- [`doc/reviewing_PR_guide.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/reviewing_PR_guide.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/reviewing_PR_guide.md)

## 替代与下一步

该页保持 Draft，直到 Responsible human 对正文、来源与替代关系完成审查；Draft 不进入正式导航、搜索或 AI allowlist。

---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: maintainers.issue-triage
title: 旧文档迁移草稿：issue triage
language: zh_CN
status: draft
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
last_human_reviewer: Pending human review
source_paths:
- doc/ISSUE_TRIAGE.md
- ISSUES.md
- GOVERNANCE.md
- .github/ISSUE_TEMPLATE/bug_report.yml
- .github/ISSUE_TEMPLATE/feature_proposal.yml
- .github/labeler.yml
source_symbols: []
source_queries: []
source_fingerprint: f4ac6afebb7fb000fb110f9c69c413b5ff1379bef35c03ae615950f0902f22cd
authority: docs-explanation
verified_commit: c1b0f95c6d1b074fc49ee2a7976819c124b69047
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: d0b75d54df53a88c08304173a96f67c342d59febbe837ce6fbff6081355dcd18
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
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/568
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/maintainers/issue-triage/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/maintainers/issue-triage/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/maintainers/issue-triage/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/maintainers/issue-triage/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/c1b0f95c6d1b074fc49ee2a7976819c124b69047
source_urls:
- path: doc/ISSUE_TRIAGE.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/ISSUE_TRIAGE.md
- path: ISSUES.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/ISSUES.md
- path: GOVERNANCE.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/GOVERNANCE.md
- path: .github/ISSUE_TEMPLATE/bug_report.yml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/.github/ISSUE_TEMPLATE/bug_report.yml
- path: .github/ISSUE_TEMPLATE/feature_proposal.yml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/.github/ISSUE_TEMPLATE/feature_proposal.yml
- path: .github/labeler.yml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/.github/labeler.yml
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28maintainers.issue-triage%29%3A+&body=Document+ID%3A+maintainers.issue-triage%0ALanguage%3A+zh_CN%0AVerified+commit%3A+c1b0f95c6d1b074fc49ee2a7976819c124b69047%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# 旧文档迁移草稿：issue triage

本页是 `maintainers.issue-triage` 的迁移草稿页面。它记录 **1** 条冻结清单记录，但不把旧说明提升为运行时契约。

- Stable document IDs: `maintainers.issue-triage`
- Target: `maintainers/issue-triage.md`
- Replacement: https://crimsoncrossbunker.github.io/CCB-Docs/maintainers/issue-triage/
- Archive reason: —

## 清单记录

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| maintainers.issue-triage | doc/ISSUE_TRIAGE.md | migrate_rewrite | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## 权威边界

运行时行为仍以 CCB 源码和测试为准；JSON/Lua/API 以 Schema、声明、注册信息和生成清单为准；构建以 CI、CMake、Makefile 与 Gradle 为准。本页只解释迁移状态、历史和可审核来源。若旧正文与当前契约冲突，应以契约为准。

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

## 历史与归属

清单中的已接受贡献者为：thaelina。许可证：CC-BY-SA-3.0。异常贡献者原始值没有导入或发布。

源清单冻结 commit 为 `0378ca2b84303cf614c617c9d9eaa50138cd21ff`；本次交叉仓验证 commit 为 `c1b0f95c6d1b074fc49ee2a7976819c124b69047`；聚合源指纹为 `f4ac6afebb7fb000fb110f9c69c413b5ff1379bef35c03ae615950f0902f22cd`。[过滤历史实验报告](/CCB-Docs/migration/filtered-history-experiment/)记录了为何不导入整个游戏仓库历史。

## CCB 中保留的正文

- [`doc/ISSUE_TRIAGE.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/ISSUE_TRIAGE.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/ISSUE_TRIAGE.md)

## 替代与下一步

该页保持 Draft，直到 Responsible human 对正文、来源与替代关系完成审查；Draft 不进入正式导航、搜索或 AI allowlist。

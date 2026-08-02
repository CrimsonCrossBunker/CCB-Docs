---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: contributing.responsible-human
title: Responsible human 与 AI 辅助贡献
language: zh_CN
status: active
doc_type: explanation
audiences:
- new-contributor
- experienced-contributor
- maintainer
owners:
- CCB maintainers
reviewers:
- Documentation reviewers
review_interval_days: 90
last_human_reviewer: LYHGLYTX
source_paths:
- CONTRIBUTING.md
- GOVERNANCE.md
- .github/pull_request_template.md
source_symbols: []
source_queries:
- Responsible human
source_fingerprint: 781981c55ef754b0836ca4b065bb6a7b9a85a6daf0e4bca4782240c25caa7a2c
authority: governance
verified_commit: 4e3b9aa99ae59630abf60f717bdaf563b2d63245
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 37cb310dd6b29be8649a2309df51a39a284341ceb5eb24b1245fa2482694785d
prerequisites: []
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: CCB contributors; see source paths and Git history.
example_validation_ids:
- agent-context
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: governance
risk_level: high
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/contributing/responsible-human/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/contributing/responsible-human/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/contributing/responsible-human/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/contributing/responsible-human/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/4e3b9aa99ae59630abf60f717bdaf563b2d63245
source_urls:
- path: CONTRIBUTING.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/CONTRIBUTING.md
- path: GOVERNANCE.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/GOVERNANCE.md
- path: .github/pull_request_template.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/.github/pull_request_template.md
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28contributing.responsible-human%29%3A+&body=Document+ID%3A+contributing.responsible-human%0ALanguage%3A+zh_CN%0AVerified+commit%3A+4e3b9aa99ae59630abf60f717bdaf563b2d63245%0A%0ADescribe+the+documentation+problem%3A%0A
---

# Responsible human 与贡献责任

CCB 允许 AI 辅助，也允许自动化账号创建 PR。不要求公开工具、模型、完整提示词
或聊天记录，但每个 PR 必须指定一名真实的 Responsible human。

## 责任范围

Responsible human 必须：

- 理解修改的目的、实现和影响边界；
- 审查最终 diff，而不是只审查生成过程或摘要；
- 为 PR 中记录的测试结果负责；
- 核查复制、改写和移植材料的许可证与署名；
- 记录可验证的外部来源；
- 回答审阅问题，并跟进 PR 直到合并或关闭。

AI 输出不能证明代码正确，也不能消除上游许可证或作者署名。无法解释修改或
无法复现验证时，应继续调查，而不是把责任推给工具。

## 审阅与合并

CCB 只需要一名 Responsible human；当前确认的维护者是 `LYHGLYTX`。当该维护者
自己创建 PR 时，不需要另一名 GitHub 用户批准，因此目标 Ruleset 的 required
approval 数量为 0，也不要求最后推送者之外的人批准。机器人不能取代 Responsible
human，也不能批准自己的修改。

PR 流程、required checks、解决审阅对话以及禁止强推和删除分支仍是目标保护规则。
只有当这些检查已在默认分支稳定成功、管理员步骤也已完成时才启用。自动合并始终
保持关闭。

机器人创建的漂移 PR 禁止自动合并。文档 PR 在依赖的源码 PR 合并后，还必须
刷新到最终 commit 并重新验证。

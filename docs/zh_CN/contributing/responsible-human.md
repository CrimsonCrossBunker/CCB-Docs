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
source_fingerprint: 92bbc1c991b6ad674114072e80aa45f9cc05cb3bf47bc24c8b2dc4ab2dd10695
authority: governance
verified_commit: 9d8f26582da0f53ca1e29f8f072aeef43955655b
verified_at: '2026-08-01'
generated: false
generated_by: null
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 55d3f928cb2ca6ab24791556f0c374de51d4aa25e240accb35f181120453be7a
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

目标治理规则要求非作者人类批准，但启用前必须确认至少两名活跃且有审查权限
的人类维护者，并确认 required checks 已在默认分支成功运行。条件不足时只保留
目标配置，不立即启用会阻塞仓库的保护规则。

机器人创建的漂移 PR 禁止自动合并。文档 PR 在依赖的源码 PR 合并后，还必须
刷新到最终 commit 并重新验证。

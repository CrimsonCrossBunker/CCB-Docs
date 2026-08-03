---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: contributing.ai-assisted-development
title: AI 辅助开发
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
source_queries: []
source_fingerprint: 781981c55ef754b0836ca4b065bb6a7b9a85a6daf0e4bca4782240c25caa7a2c
authority: governance
verified_commit: d32b9cc880a85480840d82cfa05d256c78a16615
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 89bb9e5d9c1ed291a5f8279742a98a4dd5dc42fb68eb643852b07b38b066ff0c
prerequisites:
- contributing.responsible-human
depends_on:
- contributing.documentation-policy
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
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/contributing/ai-assisted-development/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/contributing/ai-assisted-development/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/contributing/ai-assisted-development/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/contributing/ai-assisted-development/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/d32b9cc880a85480840d82cfa05d256c78a16615
source_urls:
- path: CONTRIBUTING.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/CONTRIBUTING.md
- path: GOVERNANCE.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/GOVERNANCE.md
- path: .github/pull_request_template.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/.github/pull_request_template.md
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28contributing.ai-assisted-development%29%3A+&body=Document+ID%3A+contributing.ai-assisted-development%0ALanguage%3A+zh_CN%0AVerified+commit%3A+d32b9cc880a85480840d82cfa05d256c78a16615%0A%0ADescribe+the+documentation+problem%3A%0A
---

# AI 辅助开发

CCB 接受 AI 辅助工作，但评审对象是最终修改、验证证据和人类责任，而不是工具解释
有多自信。无需披露工具或模型名称。

## Responsible human 仍然负责

每个 PR 必须指定 Responsible human。该人必须理解修改、审阅最终 diff、对测试结果
负责、核对许可证与外部来源并回答审阅问题。Responsible human 无法解释的生成补丁
还没有达到可审阅状态。

## 安全流程

1. 修改前读取根级和最近的子目录 `AGENTS.md`。
2. 检查源码、测试、注册、Schema 和生成边界。
3. 给工具限定窄任务和明确非目标，特别说明兼容与运行时行为边界。
4. 逐个审阅变更文件，移除无关格式化、猜测路径、缓存、本机路径、凭据和手改生成文件。
5. 按 `ai/test-matrix.yml` 运行验证；只报告实际执行过的命令。
6. 完整填写文档影响字段，并链接依赖的文档 PR。

## 证据标准

不得发布虚构 API、路径、命令、测试输出、审阅者或许可证。生成参考必须追溯到
Schema、LuaLS 声明、注册、清单或测试。证据不足时应标为未验证或 draft，不能靠
推测填空。

AI 系统和 Bot 不能批准自己的 PR，也不能满足人类审阅者要求。人类审阅是治理边界，
不是披露仪式。

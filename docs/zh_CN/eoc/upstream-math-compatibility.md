---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: eoc.upstream-math-compatibility
title: 饥饿与士气数学表达式兼容草稿
language: zh_CN
status: draft
doc_type: reference
audiences:
- new-contributor
- experienced-contributor
- maintainer
- mod-author
- api-user
owners:
- CCB maintainers
reviewers:
- Documentation reviewers
review_interval_days: 60
last_human_reviewer: LYHGLYTX
source_paths:
- src/math_parser_diag.cpp
- tests/upstream_math_compat_test.cpp
source_symbols:
- hunger_eval
- hunger_ass
- morale_eval
source_queries:
- hunger
- morale
- raw
source_fingerprint: 63aa23636f78e390885922176617b76ce1872b96b4bf9d6ff98c47798b061ccf
authority: api-contract
verified_commit: e6d42fcd151236cc3b5824107986911b15969a65
verified_at: '2026-10-13'
generated: false
generated_by: null
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 3fb01cbe28214e221cb3ade36edc0e1b7b6b544b0a575b51083cd1908b2dbc4b
prerequisites:
- eoc.overview
depends_on:
- eoc.talkers
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: CCB contributors; parser registrations, inventories, and tests remain authoritative.
example_validation_ids: []
api_version: contract-inventory-v1
deprecated: false
deprecation_replacement: null
risk_group: eoc
risk_level: high
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/995
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/eoc/upstream-math-compatibility/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/eoc/upstream-math-compatibility/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/eoc/upstream-math-compatibility/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/eoc/upstream-math-compatibility/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/e6d42fcd151236cc3b5824107986911b15969a65
source_urls:
- path: src/math_parser_diag.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/e6d42fcd151236cc3b5824107986911b15969a65/src/math_parser_diag.cpp
- path: tests/upstream_math_compat_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/e6d42fcd151236cc3b5824107986911b15969a65/tests/upstream_math_compat_test.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28eoc.upstream-math-compatibility%29%3A+&body=Document+ID%3A+eoc.upstream-math-compatibility%0ALanguage%3A+zh_CN%0AVerified+commit%3A+e6d42fcd151236cc3b5824107986911b15969a65%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# 饥饿与士气数学表达式兼容草稿

本页跟随尚未合并的 CCB PR #995，依据该 PR 的源码与聚焦回归。完整同步数据需要这些注册函数；本页保持草稿，不进入正式搜索或 AI 索引。

`u_hunger()` 与 `n_hunger()` 读取对应 Character 的饥饿值；赋值调用原生 `Character::set_hunger`，按整数处理。非 Character 目标赋值会失败。旧的 `val('hunger')` 读取方式仍可用。

`u_morale()` 与 `n_morale()` 按 CCB 现有士气规则读取数值；`raw` 参数被接受，两个取值沿用同一 CCB 数值规则。旧的 `val('morale')` 读取方式仍可用。不要把此次移植视为恢复上游额外的士气惩罚。

士气赋值的原生 talker 实现没有得到本次回归的行为证明。需要改变士气时，应核对现有受支持的士气效果或 Lua Platform v1 接口。本次证据仅覆盖士气读取，不能证明赋值生效。

验收使用同配置 SDL3 Release 引擎缓存，重编受影响源文件与测试。2 个测试、20 条断言通过，随机种子 20261013：玩家/NPC 读取、饥饿赋值、旧读取接口、非 Character 拒绝，以及真实负士气夹具。没有完成整批原生重建、旧存档或全部平台验收。

适配自 CDDA #88622（RenechCDDA）与 #88818（Anton Simakov），源提交保留作者和来源 SHA。只使用 CCB 的 Lua Platform v1；数学注册属于原生表达式接口，不新增 Lua 运行时。Responsible human: LYHGLYTX。

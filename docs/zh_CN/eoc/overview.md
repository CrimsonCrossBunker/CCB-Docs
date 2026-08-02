---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: eoc.overview
title: EOC 契约与生命周期
language: zh_CN
status: active
doc_type: explanation
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
- data/reference/json/ccb_eoc_conditions.json
- data/reference/json/ccb_eoc_effects.json
- tools/json_api/contract-inventory.schema.json
- tools/json_api/generate_contracts.py
- tools/json_api/test_generate_contracts.py
- src/condition.cpp
- src/npctalk.cpp
- src/effect_on_condition.cpp
- src/effect_on_condition.h
- tests/eoc_test.cpp
- doc/JSON/EFFECT_ON_CONDITION.md
source_symbols: []
source_queries: []
source_fingerprint: f52b67e59b777a2d203f58ddaef85d38aa06ac0792196b54e829681279e2f594
authority: api-contract
verified_commit: 4e3b9aa99ae59630abf60f717bdaf563b2d63245
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 99bd0f3eddb34fe638f11f39532dd38dc95dbb2551c9a6e9553cdbaa18b2be53
prerequisites:
- json.overview
depends_on:
- reference.eoc-conditions
- reference.eoc-effects
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
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/eoc/overview/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/eoc/overview/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/eoc/overview/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/eoc/overview/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/4e3b9aa99ae59630abf60f717bdaf563b2d63245
source_urls:
- path: data/reference/json/ccb_eoc_conditions.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/data/reference/json/ccb_eoc_conditions.json
- path: data/reference/json/ccb_eoc_effects.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/data/reference/json/ccb_eoc_effects.json
- path: tools/json_api/contract-inventory.schema.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/tools/json_api/contract-inventory.schema.json
- path: tools/json_api/generate_contracts.py
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/tools/json_api/generate_contracts.py
- path: tools/json_api/test_generate_contracts.py
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/tools/json_api/test_generate_contracts.py
- path: src/condition.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/src/condition.cpp
- path: src/npctalk.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/src/npctalk.cpp
- path: src/effect_on_condition.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/src/effect_on_condition.cpp
- path: src/effect_on_condition.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/src/effect_on_condition.h
- path: tests/eoc_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/tests/eoc_test.cpp
- path: doc/JSON/EFFECT_ON_CONDITION.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/doc/JSON/EFFECT_ON_CONDITION.md
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28eoc.overview%29%3A+&body=Document+ID%3A+eoc.overview%0ALanguage%3A+zh_CN%0AVerified+commit%3A+4e3b9aa99ae59630abf60f717bdaf563b2d63245%0A%0ADescribe+the+documentation+problem%3A%0A
---

# EOC 契约与生命周期

EOC（effect on condition）把条件解析、效果解析和触发生命周期组合起来。当前机器清单
分别索引[275 个条件键](../reference/eoc-conditions.md)和
[306 个效果键](../reference/eoc-effects.md)。注册覆盖完整，但 handler 级参数分类仍不完整。

## `effect_on_condition` 对象

源码清单已把该对象的字段契约标为 `partial`：

- `id` 是明确的 mandatory 字段。
- `eoc_type` 可选；无 `recurrence` 时默认 activation，有 `recurrence` 时走 recurring 规则。
- `condition`、`deactivate_condition`、`effect`、`false_effect` 由存在性分支读取。
- `global` 和 `run_for_npcs` 有 `false` 默认值。
- `required_event` 只在 `EVENT` 分支中 mandatory；不能脱离分支把它解释为所有 EOC 都必填。

生命周期类型来自 `effect_on_condition.h/.cpp`：`ACTIVATION`、`RECURRING`、
`AVATAR_DEATH`、`NPC_DEATH`、`PREVENT_DEATH` 和 `EVENT`。每种类型的 talker 和上下文
来源不同，必须查对应触发路径和测试。

## 解析边界

- 条件按“第一个匹配解析器获胜”的顺序分派。未知对象条件抛出 `JsonError`；未知字符串
  条件生成恒 false predicate。
- 效果容器接受 string、object 或 array，并同样按首个匹配解析器分派；未知效果抛出
  `JsonError`。
- 条件清单只有 `and`、`or`、`not` 三个逻辑键完全分类；其余 272 个为 `partial`。
- 306 个效果键全部为 `partial`。这不表示它们不可用，只表示参数、默认值、嵌套、talker、
  变量或上下文尚未全部获得源码级分类。

继续阅读 [Talker 路由](talkers.md)、[变量与上下文](variables-context.md)、
[嵌套规则](nesting.md)，并用[完整示例 Mod](../mods/complete-json-eoc-mod.md)建立最小验证链。

---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: eoc.talkers
title: EOC Talker 与 alpha/beta 路由
language: zh_CN
status: stale
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
source_fingerprint: 3decb33447a3fd37a7de3a7328e8bd883da5aeb39b13f2e6f27c2cb82bb52876
authority: api-contract
verified_commit: d32b9cc880a85480840d82cfa05d256c78a16615
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: true
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 633c116b8ceb25994926cb0d914dc6f0b5623695fae7fddbefd46996ec0cf860
prerequisites:
- eoc.overview
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
stale_reason: 'Source paths changed after d32b9cc880a8: data/reference/json/ccb_eoc_conditions.json, data/reference/json/ccb_eoc_effects.json,
  doc/JSON/EFFECT_ON_CONDITION.md, …'
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/eoc/talkers/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/eoc/talkers/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/eoc/talkers/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/eoc/talkers/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/d32b9cc880a85480840d82cfa05d256c78a16615
source_urls:
- path: data/reference/json/ccb_eoc_conditions.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/data/reference/json/ccb_eoc_conditions.json
- path: data/reference/json/ccb_eoc_effects.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/data/reference/json/ccb_eoc_effects.json
- path: tools/json_api/contract-inventory.schema.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/tools/json_api/contract-inventory.schema.json
- path: tools/json_api/generate_contracts.py
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/tools/json_api/generate_contracts.py
- path: tools/json_api/test_generate_contracts.py
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/tools/json_api/test_generate_contracts.py
- path: src/condition.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/src/condition.cpp
- path: src/npctalk.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/src/npctalk.cpp
- path: src/effect_on_condition.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/src/effect_on_condition.cpp
- path: src/effect_on_condition.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/src/effect_on_condition.h
- path: tests/eoc_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/tests/eoc_test.cpp
- path: doc/JSON/EFFECT_ON_CONDITION.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/doc/JSON/EFFECT_ON_CONDITION.md
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28eoc.talkers%29%3A+&body=Document+ID%3A+eoc.talkers%0ALanguage%3A+zh_CN%0AVerified+commit%3A+d32b9cc880a85480840d82cfa05d256c78a16615%0A%0ADescribe+the+documentation+problem%3A%0A
---

# EOC Talker 与 alpha/beta 路由

EOC 条件和效果在 dialogue 上下文中操作 alpha/beta talker。历史键名通常用 `u_` 和
`npc_` 表示这两个路由方向，但前缀本身不证明对象一定是玩家 avatar 或普通 NPC。
事件、物品、怪物、地图位置和嵌套调用可以构造不同 talker 组合。

## 清单如何表达未知

条件清单中 235 个键标为 `legacy_alpha_beta_alias`，40 个为 `unknown`；效果清单中对应
为 161 和 145。这里的 `legacy_alpha_beta_alias` 只证明注册别名分组，绝不等于已分类的
运行时 talker 类型。

使用某个键之前：

1. 在条件或效果注册表中找到 parser/handler。
2. 阅读 handler 如何从 `dialogue` 取得 alpha/beta。
3. 阅读触发 EOC 的调用点，确认事件或父 EOC 怎样构造 dialogue。
4. 如果发生 talker 交换或嵌套调用，分别测试两个方向。
5. 不要仅凭 `u_`/`npc_` 名称写入“玩家专用”或“NPC 专用”文档。

## 失败模式

- alpha/beta 为空或类型不支持所调用的接口；
- EVENT 的焦点实体与作者假设不同；
- 父 EOC 把 context 传入子 EOC，但没有传入预期 talker；
- 使用别名后测试只覆盖一个路由方向。

当前生成参考刻意显示 talker 分类状态。只有 handler、调用点和测试共同证明后，才能把
具体兼容 talker 写入正式契约。

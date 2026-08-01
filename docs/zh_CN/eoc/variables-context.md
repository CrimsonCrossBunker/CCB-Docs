---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: eoc.variables-context
title: EOC 变量与上下文
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
verified_commit: a038c765568fc47a58ef8c523b2722d416f5f61c
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 8e90cbae7e8c02b7eaa85d8151d686e20feb0dac08e769660feee6034b89c055
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
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/566
stale_reason: null
search:
  exclude: true
---

# EOC 变量与上下文

机器清单证明通用变量解析器识别以下 scope：

| Scope | 用途边界 |
| --- | --- |
| `u_val` | alpha 路由相关变量名；不要从前缀推断具体 talker 类型 |
| `npc_val` | beta 路由相关变量名；同样只是历史命名 |
| `global_val` | 全局变量命名空间 |
| `var_val` | 间接变量引用 |
| `context_val` | 当前 EOC/dialogue 调用链传递的上下文值 |

清单还证明 parser 使用 `value_or_var`、`value_or_var_pair`、`dbl_or_var`、
`duration_or_var`、`str_or_var`、`translation_or_var` 和 `eoc_math` 等值辅助器。
但这不证明每个条件/效果接受所有 scope 或所有值类型。

## 上下文纪律

- 把 `context_val` 看成调用协议：写入方和读取方必须约定名字、类型和生命周期。
- 嵌套 EOC 前检查调用接口是否转发变量；不要假设所有效果自动传播 context。
- 对 EVENT，先检查事件字段如何映射到 context，再使用该键。
- 给 Mod 变量加稳定前缀，避免与 core 或其他 Mod 的全局变量碰撞。
- 在数学表达式、字符串插值和结构化变量对象之间切换时，分别验证解析路径。

275 个条件中 272 个、306 个效果中全部 306 个的 handler 变量契约仍是
`unclassified`。生成参考显示 `known_global_scopes` 是全局 parser 能力，不是每个键的
逐项许可列表。

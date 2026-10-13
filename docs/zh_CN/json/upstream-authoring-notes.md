---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: json.upstream-authoring-notes
title: 上游 JSON 文档勘误的 CCB 适配草稿
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
- src/iuse_actor.cpp
- src/recipe.cpp
- src/item_factory.cpp
source_symbols:
- molle_attach_actor::load
- molle_detach_actor::load
- batch_savings::deserialize
source_queries:
- ignore_sheet_thickness
- cover_melee
- batch_time_factors
source_fingerprint: b2484fe56acbc5d5ada896e3263c50e2ffd68595c3c2e31aec525a15f97ce116
authority: api-contract
verified_commit: 6a0c46788f43ef37269cd742e0a6147b4f55e96e
verified_at: '2026-10-14'
generated: false
generated_by: null
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 5affaa285f4be6bfb8755a893b375006ecbb0ccb1d90db51801a0124c6f2a220
prerequisites:
- reference.json-object-types
depends_on: []
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
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/json/upstream-authoring-notes/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/json/upstream-authoring-notes/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/json/upstream-authoring-notes/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/json/upstream-authoring-notes/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/6a0c46788f43ef37269cd742e0a6147b4f55e96e
source_urls:
- path: src/iuse_actor.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/6a0c46788f43ef37269cd742e0a6147b4f55e96e/src/iuse_actor.cpp
- path: src/recipe.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/6a0c46788f43ef37269cd742e0a6147b4f55e96e/src/recipe.cpp
- path: src/item_factory.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/6a0c46788f43ef37269cd742e0a6147b4f55e96e/src/item_factory.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28json.upstream-authoring-notes%29%3A+&body=Document+ID%3A+json.upstream-authoring-notes%0ALanguage%3A+zh_CN%0AVerified+commit%3A+6a0c46788f43ef37269cd742e0a6147b4f55e96e%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# 上游 JSON 文档勘误的 CCB 适配草稿

本页把上游文档补充与勘误转为 CCB 的维护说明，核对 CCB 已合并源码，不改变运行时规则。示例是字段片段，须放入完整的物品或配方定义；本页保持草稿。

## MOLLE 动作

`attach_molle` 的 `size` 是必填的总 MOLLE 空间。`attach_molle` 和 `detach_molle` 都读取可选 `moves`，但当前两个动作的 `use` 实现没有使用这个配置值。不要据此声称装备操作耗时为 300 移动点。两个示例分别属于两个定义，不能在同一个 JSON 对象里重复写 `use_action` 键。

```json
{"use_action": {"type": "attach_molle", "size": 10, "moves": 300}}
```

```json
{"use_action": {"type": "detach_molle", "moves": 300}}
```

## 线性批量时间

`mode`、`setup` 和 `max` 之间用逗号分隔；`"mode": "linear": "setup"` 是无效 JSON。`max` 控制重新应用准备成本的批量周期，不是禁止更大的制作批量。

```json
{"batch_time_factors": {"mode": "linear", "setup": "12 m", "max": 20}}
```

## 护甲材料与覆盖

`ignore_sheet_thickness` 使用 JSON 布尔值 `true`，不写字符串 `"true"`。`coverage`、`cover_melee`、`cover_ranged`、`cover_vitals` 属于 `armor` 中的部位条目。材料的 `covered_by_mat` 表示该材料覆盖比例，与护甲的部位覆盖字段分别处理。

```json
{"armor": [{"covers": ["torso"], "coverage": 95, "cover_melee": 95,
  "cover_ranged": 50, "cover_vitals": 5,
  "material": [{"type": "plastic", "covered_by_mat": 15,
    "thickness": 0.8, "ignore_sheet_thickness": true}]}]}
```

来源及署名：CDDA #88587: Proflig; CDDA #88632: dynst; CDDA #88852: OromisElf; CDDA #88866: OromisElf。对应原始 PR 的作者和修改意图保留在本草稿中，示例按 CCB 加载器核对。Responsible human: LYHGLYTX。

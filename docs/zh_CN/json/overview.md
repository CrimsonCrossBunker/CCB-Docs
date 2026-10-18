---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: json.overview
title: JSON 契约总览
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
review_interval_days: 90
last_human_reviewer: LYHGLYTX
source_paths:
- data/reference/json/ccb_json_object_types.json
- tools/json_api/contract-inventory.schema.json
- tools/json_api/generate_contracts.py
- tools/json_api/test_generate_contracts.py
- src/init.cpp
- src/generic_factory.h
- tests/json_load_test.cpp
- doc/JSON/JSON_INHERITANCE.md
- doc/JSON/JSON_STYLE.md
source_symbols: []
source_queries: []
source_fingerprint: d4736958a65401eacd855859ce5668adf6b7de5ae4cbd2d5c85cd7b4c959994c
authority: api-contract
verified_commit: c663ceb2c1bd1f5b23ffc533c2e7944fd859b4bd
verified_at: '2026-08-12'
generated: false
generated_by: null
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 71e86145c575a8e20611cd989ed5262f31e02afe487dee70986fdbb1b41064cf
prerequisites:
- architecture.project-map
depends_on:
- reference.json-object-types
- validation.testing
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: CCB contributors; source contracts and Git history remain authoritative.
example_validation_ids: []
api_version: contract-inventory-v1
deprecated: false
deprecation_replacement: null
risk_group: json
risk_level: high
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/1025
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/json/overview/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/json/overview/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/json/overview/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/json/overview/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/c663ceb2c1bd1f5b23ffc533c2e7944fd859b4bd
source_urls:
- path: data/reference/json/ccb_json_object_types.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c663ceb2c1bd1f5b23ffc533c2e7944fd859b4bd/data/reference/json/ccb_json_object_types.json
- path: tools/json_api/contract-inventory.schema.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c663ceb2c1bd1f5b23ffc533c2e7944fd859b4bd/tools/json_api/contract-inventory.schema.json
- path: tools/json_api/generate_contracts.py
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c663ceb2c1bd1f5b23ffc533c2e7944fd859b4bd/tools/json_api/generate_contracts.py
- path: tools/json_api/test_generate_contracts.py
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c663ceb2c1bd1f5b23ffc533c2e7944fd859b4bd/tools/json_api/test_generate_contracts.py
- path: src/init.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c663ceb2c1bd1f5b23ffc533c2e7944fd859b4bd/src/init.cpp
- path: src/generic_factory.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c663ceb2c1bd1f5b23ffc533c2e7944fd859b4bd/src/generic_factory.h
- path: tests/json_load_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c663ceb2c1bd1f5b23ffc533c2e7944fd859b4bd/tests/json_load_test.cpp
- path: doc/JSON/JSON_INHERITANCE.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c663ceb2c1bd1f5b23ffc533c2e7944fd859b4bd/doc/JSON/JSON_INHERITANCE.md
- path: doc/JSON/JSON_STYLE.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c663ceb2c1bd1f5b23ffc533c2e7944fd859b4bd/doc/JSON/JSON_STYLE.md
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28json.overview%29%3A+&body=Document+ID%3A+json.overview%0ALanguage%3A+zh_CN%0AVerified+commit%3A+c663ceb2c1bd1f5b23ffc533c2e7944fd859b4bd%0A%0ADescribe+the+documentation+problem%3A%0A
---

# JSON 契约总览

CCB 的 JSON 契约不是由一份万能 Schema 定义的。运行时加载器和测试决定行为；
`DynamicDataLoader` 注册决定顶层 `type` 的分派；Schema、验证器和生成清单记录能够
被机器证明的部分。旧文档和数据样例可以提供线索，但不能覆盖这些契约。

## 当前机器覆盖

- [JSON 对象类型注册表](../reference/json-object-types.md)索引 190 个唯一注册类型和
  191 次注册调用。
- 183 个注册类型在受审计的 6,731 个 tracked JSON 文件中有顶层实例候选。
- 7 个注册类型没有实例候选；清单没有发现“出现但未注册”的顶层字符串类型。
- 190 个类型的通用 Schema 状态都是 `none`；不得把对象类型清单称为完整 JSON Schema。
- 189 个类型的字段契约仍为 `unclassified`，`effect_on_condition` 目前为 `partial`。

这些数字描述的是提交
`71f403ecea0dcf16be8fe93c661acbe2a4906cc6` 的生成清单，不保证任意对象的每个字段、
默认值、继承规则或跨 ID 引用都已分类。

## 一个对象如何获得意义

1. JSON 解析器先证明文件语法和根容器可读。
2. 顶层对象的字符串 `type` 进入注册分派。
3. 对应 loader/factory 读取字段，并在源码中决定 mandatory、optional、默认值和错误。
4. factory、finalize/check 阶段以及交叉引用检查可能进一步拒绝对象。
5. 运行时测试证明具体行为和兼容性。

因此，“在数据中出现过”只说明存在词法实例；“旧文档提到过”也只是
`lexical_only` 证据。要确认字段，必须回到注册表指出的 loader、测试和验证器。

## 待合并的坐骑装备契约

[CCB PR #1025](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/1025)
拟为动物装备增加 JSON 字段。本节说明待合并的契约；在源 PR 合并前，它不代表已发布的接口。

带有 `PET_EQUIPMENT` 子类型的物品通过 `pet_slots` 声明兼容的装备位置。
物品加载器读取 `pet_mount_threshold_delta` 以调整上马难度，
`pet_melee_hit_multiplier` 以调整马上近战命中，
`pet_spook_multiplier` 以调整受惊概率，以及
`pet_mounted_move_cost_multiplier` 以调整骑乘移动消耗。
`pet_install_qualities` 是 `[工具品质 ID, 最低等级]` 列表；通用宠物装备菜单在安装前检查这些要求。

`pet_slot` 可在装有物品时提供 `spook_multiplier` 与
`mounted_move_cost_multiplier`。槽位和物品的倍率相乘；最终受惊倍率限制在
0.1–2.0，骑乘移动倍率限制在 0.5–2.0。为兼容既有内容，
`pet_fear_multiplier` 仍同时影响受惊和跌落；新增受惊字段只影响受惊。

该 PR 增加仅适用于马体型的笼头与蹄铁位置，并保留现有槽位 ID 和存档行为。
马厩刷新与安装要求由数据定义。正式内容依赖这些字段前，应核对源 PR 的加载器、消费者与测试。

## 从哪里开始

- 查询 `type` 是否注册：使用[生成注册表](../reference/json-object-types.md)。
- 修改继承对象：先阅读[继承与 copy-from](inheritance-copy-from.md)。
- 提交前检查：遵循[JSON 验证与证据等级](validation.md)。
- 编写 EOC：从[EOC 契约与生命周期](../eoc/overview.md)开始。
- 制作可复现样例：使用[完整 JSON/EOC Mod 教程](../mods/complete-json-eoc-mod.md)。

如果本页与清单、Schema、注册源码或测试冲突，本页应标记 stale 并修复；不要为了匹配
正文而改变运行时契约。

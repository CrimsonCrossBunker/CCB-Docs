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
source_fingerprint: 694345d1f3eb604519f90e93d870396341c99719edf7270e88a651574b995a7e
authority: api-contract
verified_commit: d32b9cc880a85480840d82cfa05d256c78a16615
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: d24151da9c3f3be1b0307ecb5a26a8425e9791b3376028d77e457e08745e6012
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
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/json/overview/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/json/overview/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/json/overview/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/json/overview/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/d32b9cc880a85480840d82cfa05d256c78a16615
source_urls:
- path: data/reference/json/ccb_json_object_types.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/data/reference/json/ccb_json_object_types.json
- path: tools/json_api/contract-inventory.schema.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/tools/json_api/contract-inventory.schema.json
- path: tools/json_api/generate_contracts.py
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/tools/json_api/generate_contracts.py
- path: tools/json_api/test_generate_contracts.py
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/tools/json_api/test_generate_contracts.py
- path: src/init.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/src/init.cpp
- path: src/generic_factory.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/src/generic_factory.h
- path: tests/json_load_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/tests/json_load_test.cpp
- path: doc/JSON/JSON_INHERITANCE.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/doc/JSON/JSON_INHERITANCE.md
- path: doc/JSON/JSON_STYLE.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/doc/JSON/JSON_STYLE.md
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28json.overview%29%3A+&body=Document+ID%3A+json.overview%0ALanguage%3A+zh_CN%0AVerified+commit%3A+d32b9cc880a85480840d82cfa05d256c78a16615%0A%0ADescribe+the+documentation+problem%3A%0A
---

# JSON 契约总览

CCB 的 JSON 契约不是由一份万能 Schema 定义的。运行时加载器和测试决定行为；
`DynamicDataLoader` 注册决定顶层 `type` 的分派；Schema、验证器和生成清单记录能够
被机器证明的部分。旧文档和数据样例可以提供线索，但不能覆盖这些契约。

## 当前机器覆盖

- [JSON 对象类型注册表](../reference/json-object-types.md)索引 190 个唯一注册类型和
  191 次注册调用。
- 183 个注册类型在受审计的 6,714 个 tracked JSON 文件中有顶层实例候选。
- 7 个注册类型没有实例候选；清单没有发现“出现但未注册”的顶层字符串类型。
- 190 个类型的通用 Schema 状态都是 `none`；不得把对象类型清单称为完整 JSON Schema。
- 189 个类型的字段契约仍为 `unclassified`，`effect_on_condition` 目前为 `partial`。

这些数字描述的是提交
`a038c765568fc47a58ef8c523b2722d416f5f61c` 的生成清单，不保证任意对象的每个字段、
默认值、继承规则或跨 ID 引用都已分类。

## 一个对象如何获得意义

1. JSON 解析器先证明文件语法和根容器可读。
2. 顶层对象的字符串 `type` 进入注册分派。
3. 对应 loader/factory 读取字段，并在源码中决定 mandatory、optional、默认值和错误。
4. factory、finalize/check 阶段以及交叉引用检查可能进一步拒绝对象。
5. 运行时测试证明具体行为和兼容性。

因此，“在数据中出现过”只说明存在词法实例；“旧文档提到过”也只是
`lexical_only` 证据。要确认字段，必须回到注册表指出的 loader、测试和验证器。

## 从哪里开始

- 查询 `type` 是否注册：使用[生成注册表](../reference/json-object-types.md)。
- 修改继承对象：先阅读[继承与 copy-from](inheritance-copy-from.md)。
- 提交前检查：遵循[JSON 验证与证据等级](validation.md)。
- 编写 EOC：从[EOC 契约与生命周期](../eoc/overview.md)开始。
- 制作可复现样例：使用[完整 JSON/EOC Mod 教程](../mods/complete-json-eoc-mod.md)。

如果本页与清单、Schema、注册源码或测试冲突，本页应标记 stale 并修复；不要为了匹配
正文而改变运行时契约。

---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: json.inheritance-copy-from
title: JSON 继承与 copy-from
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
translation_source_fingerprint: 011b017522ac8f0fe674d25c2f3f6729ee36910b59b50abb94d54402ccefd8b1
prerequisites:
- json.overview
depends_on:
- reference.json-object-types
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
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/json/inheritance-copy-from/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/json/inheritance-copy-from/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/json/inheritance-copy-from/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/json/inheritance-copy-from/
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
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28json.inheritance-copy-from%29%3A+&body=Document+ID%3A+json.inheritance-copy-from%0ALanguage%3A+zh_CN%0AVerified+commit%3A+d32b9cc880a85480840d82cfa05d256c78a16615%0A%0ADescribe+the+documentation+problem%3A%0A
---

# JSON 继承与 `copy-from`

`copy-from` 不是所有 JSON 类型共享的隐式语言特性。它只有在对应 loader/factory 实现
继承时才有效，而且不同类型可以有不同的合并和检查规则。

## 能由源码证明的通用骨架

`generic_factory` 会查找 `copy-from`，解析父对象，并让类型选择专用
`handle_inheritance` 或赋值复制。`abstract` 可以作为继承模板。`relative`、
`proportional`、`extend` 和 `delete` 的支持取决于类型、字段的 C++ 表示和专用加载逻辑。

由此得到三个边界：

- 注册了某个 `type`，不代表它支持 `copy-from`。
- 支持 `copy-from`，不代表支持全部四种增量修改操作。
- 一个现有实例能加载，不代表另一类型会采用相同合并语义。

[对象类型注册表](../reference/json-object-types.md)能定位 loader，但当前字段分类不能自动
证明某类型完整的继承行为。对于未分类项，应检查 loader 是否使用 `generic_factory`、
是否实现 `handle_inheritance`，以及该类型的回归测试。

## 安全修改步骤

1. 在注册表中找到目标 `type` 和 loader 源码。
2. 查明父 ID/abstract 的定义和同类型约束。
3. 阅读目标类型对 `copy-from`、`extend`、`delete`、`relative`、`proportional` 的实现。
4. 保持继承链浅，并避免依赖另一个 Mod 未声明的加载顺序。
5. 用实际 loader 测试最终值；不要只比较输入 JSON 文本。

`tests/json_load_test.cpp` 中的 item 名称继承和怪物攻击冷却测试说明了正确的测试层级：
加载数据后检查解析出的对象，而不是只确认键存在。

## 兼容性

修改父对象可能改变所有后代。重命名/删除父 ID、改变默认值或把继承规则从替换改为
扩展，都可能影响 Mod 和存档。此类改动应列出后代、执行数据加载和针对性测试，并在
PR 中标记 JSON/Mod 文档影响。

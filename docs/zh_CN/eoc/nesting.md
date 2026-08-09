---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: eoc.nesting
title: EOC 条件与效果嵌套
language: zh_CN
status: active
doc_type: how-to
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
source_fingerprint: 104d655e889b5071282102d8ebd64521a5dbdc36ad6c7a6b6daacdd6e00e8689
authority: api-contract
verified_commit: 71f403ecea0dcf16be8fe93c661acbe2a4906cc6
verified_at: '2026-08-09'
generated: false
generated_by: null
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 4e8fdd81409a1c292a8d63686520b06e3357687cfa09c99965a731e0090d96d3
prerequisites:
- eoc.overview
depends_on:
- eoc.variables-context
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
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/eoc/nesting/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/eoc/nesting/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/eoc/nesting/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/eoc/nesting/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/71f403ecea0dcf16be8fe93c661acbe2a4906cc6
source_urls:
- path: data/reference/json/ccb_eoc_conditions.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/71f403ecea0dcf16be8fe93c661acbe2a4906cc6/data/reference/json/ccb_eoc_conditions.json
- path: data/reference/json/ccb_eoc_effects.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/71f403ecea0dcf16be8fe93c661acbe2a4906cc6/data/reference/json/ccb_eoc_effects.json
- path: tools/json_api/contract-inventory.schema.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/71f403ecea0dcf16be8fe93c661acbe2a4906cc6/tools/json_api/contract-inventory.schema.json
- path: tools/json_api/generate_contracts.py
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/71f403ecea0dcf16be8fe93c661acbe2a4906cc6/tools/json_api/generate_contracts.py
- path: tools/json_api/test_generate_contracts.py
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/71f403ecea0dcf16be8fe93c661acbe2a4906cc6/tools/json_api/test_generate_contracts.py
- path: src/condition.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/71f403ecea0dcf16be8fe93c661acbe2a4906cc6/src/condition.cpp
- path: src/npctalk.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/71f403ecea0dcf16be8fe93c661acbe2a4906cc6/src/npctalk.cpp
- path: src/effect_on_condition.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/71f403ecea0dcf16be8fe93c661acbe2a4906cc6/src/effect_on_condition.cpp
- path: src/effect_on_condition.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/71f403ecea0dcf16be8fe93c661acbe2a4906cc6/src/effect_on_condition.h
- path: tests/eoc_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/71f403ecea0dcf16be8fe93c661acbe2a4906cc6/tests/eoc_test.cpp
- path: doc/JSON/EFFECT_ON_CONDITION.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/71f403ecea0dcf16be8fe93c661acbe2a4906cc6/doc/JSON/EFFECT_ON_CONDITION.md
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28eoc.nesting%29%3A+&body=Document+ID%3A+eoc.nesting%0ALanguage%3A+zh_CN%0AVerified+commit%3A+71f403ecea0dcf16be8fe93c661acbe2a4906cc6%0A%0ADescribe+the+documentation+problem%3A%0A
---

# EOC 条件与效果嵌套

嵌套先受容器形状约束，再受具体 handler 约束。

## 已证明的通用规则

- 条件可以通过对象或字符串解析路径进入 parser；`and`、`or` 接收数组，`not` 接收
  单个对象或字符串。这三个逻辑键的嵌套契约已完整分类。
- 效果容器可为 string、object 或 array。
- 两类 parser 都是第一个匹配项获胜。不要在同一分派对象里放多个互相竞争的效果/条件键。
- 除三个逻辑条件外，handler 的参数、默认值和嵌套能力大多尚未分类；必须查看生成参考
  指向的源码。

## 最小结构

文档示例 Mod 使用一个 activation EOC：

```json
{
  "type": "effect_on_condition",
  "id": "EOC_CCB_DOCS_HELLO",
  "eoc_type": "ACTIVATION",
  "condition": { "math": [ "1 == 1" ] },
  "effect": [ { "u_message": "The CCB Docs example EOC ran." } ]
}
```

`math` 和 `u_message` 都在注册表中，但当前契约为 `partial`。示例检查只证明它们被注册、
形状符合维护样例且 JSON 可解析；真实 CCB loader 仍是最终验证层。

复杂嵌套应逐层增加：先验证叶子条件/效果，再加入 `and`/`or`/`not` 或 `if`/`then`/`else`，
最后才加入变量传递和 talker 交换。每层保留一个能复现失败的最小 EOC。

---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: json.validation
title: JSON 验证与证据等级
language: zh_CN
status: active
doc_type: how-to
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
source_fingerprint: 193b9bff99a0dd6dad93b0353ad014c05415af02a70333df08c4f2eab3a5b6c8
authority: api-contract
verified_commit: 71f403ecea0dcf16be8fe93c661acbe2a4906cc6
verified_at: '2026-08-09'
generated: false
generated_by: null
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 54da0baf1d3372e2c1bcdb6e0daa5c2ba4dd324e840733ba6a4366f9a73283f3
prerequisites:
- json.overview
depends_on:
- reference.json-object-types
- eoc.overview
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: CCB contributors; source contracts and Git history remain authoritative.
example_validation_ids:
- json-contract
- json-load
api_version: contract-inventory-v1
deprecated: false
deprecation_replacement: null
risk_group: json
risk_level: high
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/json/validation/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/json/validation/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/json/validation/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/json/validation/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/71f403ecea0dcf16be8fe93c661acbe2a4906cc6
source_urls:
- path: data/reference/json/ccb_json_object_types.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/71f403ecea0dcf16be8fe93c661acbe2a4906cc6/data/reference/json/ccb_json_object_types.json
- path: tools/json_api/contract-inventory.schema.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/71f403ecea0dcf16be8fe93c661acbe2a4906cc6/tools/json_api/contract-inventory.schema.json
- path: tools/json_api/generate_contracts.py
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/71f403ecea0dcf16be8fe93c661acbe2a4906cc6/tools/json_api/generate_contracts.py
- path: tools/json_api/test_generate_contracts.py
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/71f403ecea0dcf16be8fe93c661acbe2a4906cc6/tools/json_api/test_generate_contracts.py
- path: src/init.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/71f403ecea0dcf16be8fe93c661acbe2a4906cc6/src/init.cpp
- path: src/generic_factory.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/71f403ecea0dcf16be8fe93c661acbe2a4906cc6/src/generic_factory.h
- path: tests/json_load_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/71f403ecea0dcf16be8fe93c661acbe2a4906cc6/tests/json_load_test.cpp
- path: doc/JSON/JSON_INHERITANCE.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/71f403ecea0dcf16be8fe93c661acbe2a4906cc6/doc/JSON/JSON_INHERITANCE.md
- path: doc/JSON/JSON_STYLE.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/71f403ecea0dcf16be8fe93c661acbe2a4906cc6/doc/JSON/JSON_STYLE.md
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28json.validation%29%3A+&body=Document+ID%3A+json.validation%0ALanguage%3A+zh_CN%0AVerified+commit%3A+71f403ecea0dcf16be8fe93c661acbe2a4906cc6%0A%0ADescribe+the+documentation+problem%3A%0A
---

# JSON 验证与证据等级

不同检查证明不同事实。不要把“能解析”报告成“能完整加载”，也不要把词法出现次数当作
字段必填性的证据。

## 推荐顺序

1. 运行仓库 JSON formatter，确认格式符合项目输出。
2. 重新生成契约清单并执行 Schema、计数、源码位置和示例指针测试。
3. 运行 `json-check`。当前 `chkjson` 检查 `data/json` 中对象/数组语法以及顶层字符串
   `type`；它不是所有 loader 的完整语义加载器。
4. 构建测试程序。测试启动会加载 core/测试数据；再运行目标类型的 Catch2 测试。
5. 对外部 Mod，在真实 CCB 可执行文件中创建测试世界并加载该 Mod；记录版本、依赖和日志。

在 CCB 主仓库运行：

```sh
# validation: json-contract
python3 tools/json_api/generate_contracts.py --check
python3 -m unittest discover -s tools/json_api -p 'test_*.py'
# validation: json-load
make -j2 json-check
```

## 证据等级

| 标记 | 能证明什么 | 不能证明什么 |
| --- | --- | --- |
| `mandatory` / `optional` | loader 中有明确字段读取证据 | 所有条件分支和跨字段约束 |
| `partial` | 已分类一部分契约 | 未列出的字段安全或可省略 |
| `unclassified` | 尚无可发布的源码分类 | 字段不存在 |
| `lexical_only` | 数据或旧文档中有同名文本 | 最小示例有效、字段必填、语义相同 |
| `schema: none` | 没有通用 validator-backed Schema | loader 不会验证 |

生成器只读取 `git ls-files` 返回的 tracked 路径，并固定 190/275/306 的覆盖计数。计数变化
必须伴随注册/解析器变化和生成 diff；不得手改生成清单或生成参考页。

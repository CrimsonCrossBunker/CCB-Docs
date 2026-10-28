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
- tools/agent/generate_lua_first_replacement_ledger.py
- tools/agent/check_lua_first_replacement_ledger.py
source_symbols: []
source_queries: []
source_fingerprint: be0cec4549bdc28a9da387ded44644be569fb32aef07b5801e43a2facd88c30e
authority: api-contract
verified_commit: c961002ea44c8d41372ce683fac2505f903e6eb6
verified_at: '2026-10-29'
generated: false
generated_by: null
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 0f7a263e0a5c1d706a2ef65f9540c275b000dce6a79fafee558b583202012a33
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
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/1067
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/json/validation/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/json/validation/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/json/validation/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/json/validation/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/c961002ea44c8d41372ce683fac2505f903e6eb6
source_urls:
- path: data/reference/json/ccb_json_object_types.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c961002ea44c8d41372ce683fac2505f903e6eb6/data/reference/json/ccb_json_object_types.json
- path: tools/json_api/contract-inventory.schema.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c961002ea44c8d41372ce683fac2505f903e6eb6/tools/json_api/contract-inventory.schema.json
- path: tools/json_api/generate_contracts.py
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c961002ea44c8d41372ce683fac2505f903e6eb6/tools/json_api/generate_contracts.py
- path: tools/json_api/test_generate_contracts.py
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c961002ea44c8d41372ce683fac2505f903e6eb6/tools/json_api/test_generate_contracts.py
- path: src/init.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c961002ea44c8d41372ce683fac2505f903e6eb6/src/init.cpp
- path: src/generic_factory.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c961002ea44c8d41372ce683fac2505f903e6eb6/src/generic_factory.h
- path: tests/json_load_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c961002ea44c8d41372ce683fac2505f903e6eb6/tests/json_load_test.cpp
- path: doc/JSON/JSON_INHERITANCE.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c961002ea44c8d41372ce683fac2505f903e6eb6/doc/JSON/JSON_INHERITANCE.md
- path: doc/JSON/JSON_STYLE.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c961002ea44c8d41372ce683fac2505f903e6eb6/doc/JSON/JSON_STYLE.md
- path: tools/agent/generate_lua_first_replacement_ledger.py
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c961002ea44c8d41372ce683fac2505f903e6eb6/tools/agent/generate_lua_first_replacement_ledger.py
- path: tools/agent/check_lua_first_replacement_ledger.py
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c961002ea44c8d41372ce683fac2505f903e6eb6/tools/agent/check_lua_first_replacement_ledger.py
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28json.validation%29%3A+&body=Document+ID%3A+json.validation%0ALanguage%3A+zh_CN%0AVerified+commit%3A+c961002ea44c8d41372ce683fac2505f903e6eb6%0A%0ADescribe+the+documentation+problem%3A%0A
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

生成器只读取 `git ls-files` 返回的受版本控制路径。生成清单同时记录注册信息、源码指纹和数据实例统计；这些字段的变化并不等价。物品数值、载具部件或其他 JSON 内容修改也会改变指纹或实例计数，不应据此宣称新增了对象类型或改变了字段契约。

修改数据或清单所读取的源码后，从同一份提交重新生成清单，再执行 `--check` 和相关测试。如果基线清单已经过期，应在 PR 中区分本次行为修改与基线统计刷新。若 replacement ledger 引用了这些清单，随后通过其生成器更新关联指纹。不得手改生成清单或生成参考页。

```sh
python3 tools/json_api/generate_contracts.py
python3 tools/agent/generate_lua_first_replacement_ledger.py
python3 tools/json_api/generate_contracts.py --check
python3 tools/agent/check_lua_first_replacement_ledger.py
```

带有清单变化的 PR 仍需按当前文档影响规则填写关联文档。源码尚未合并时，关联文档 PR 保持草稿；源码合并后再核对最终提交，不能把生成检查通过当成游戏行为验收。

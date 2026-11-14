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
- src/sling.cpp
- src/ballistics.cpp
- src/ranged.cpp
- tests/staff_sling_test.cpp
- tests/shotgun_tubes_test.cpp
source_symbols: []
source_queries: []
source_fingerprint: 67b6e1bce40069c95e4c250940c0c6ffe8ebb6fcb9ea2d2d71b7dcbbca2b4df3
authority: api-contract
verified_commit: 34200a2ffcdaaf925cf2381bf900d2c753cd1a6c
verified_at: '2026-11-14'
generated: false
generated_by: null
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: ab52a235a5dffa73b8d9427b539f98cecc42c8a0e1de467d61a87dc7208b70ba
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
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/34200a2ffcdaaf925cf2381bf900d2c753cd1a6c
source_urls:
- path: data/reference/json/ccb_json_object_types.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/34200a2ffcdaaf925cf2381bf900d2c753cd1a6c/data/reference/json/ccb_json_object_types.json
- path: tools/json_api/contract-inventory.schema.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/34200a2ffcdaaf925cf2381bf900d2c753cd1a6c/tools/json_api/contract-inventory.schema.json
- path: tools/json_api/generate_contracts.py
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/34200a2ffcdaaf925cf2381bf900d2c753cd1a6c/tools/json_api/generate_contracts.py
- path: tools/json_api/test_generate_contracts.py
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/34200a2ffcdaaf925cf2381bf900d2c753cd1a6c/tools/json_api/test_generate_contracts.py
- path: src/init.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/34200a2ffcdaaf925cf2381bf900d2c753cd1a6c/src/init.cpp
- path: src/generic_factory.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/34200a2ffcdaaf925cf2381bf900d2c753cd1a6c/src/generic_factory.h
- path: tests/json_load_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/34200a2ffcdaaf925cf2381bf900d2c753cd1a6c/tests/json_load_test.cpp
- path: doc/JSON/JSON_INHERITANCE.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/34200a2ffcdaaf925cf2381bf900d2c753cd1a6c/doc/JSON/JSON_INHERITANCE.md
- path: doc/JSON/JSON_STYLE.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/34200a2ffcdaaf925cf2381bf900d2c753cd1a6c/doc/JSON/JSON_STYLE.md
- path: src/sling.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/34200a2ffcdaaf925cf2381bf900d2c753cd1a6c/src/sling.cpp
- path: src/ballistics.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/34200a2ffcdaaf925cf2381bf900d2c753cd1a6c/src/ballistics.cpp
- path: src/ranged.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/34200a2ffcdaaf925cf2381bf900d2c753cd1a6c/src/ranged.cpp
- path: tests/staff_sling_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/34200a2ffcdaaf925cf2381bf900d2c753cd1a6c/tests/staff_sling_test.cpp
- path: tests/shotgun_tubes_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/34200a2ffcdaaf925cf2381bf900d2c753cd1a6c/tests/shotgun_tubes_test.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28json.validation%29%3A+&body=Document+ID%3A+json.validation%0ALanguage%3A+zh_CN%0AVerified+commit%3A+34200a2ffcdaaf925cf2381bf900d2c753cd1a6c%0A%0ADescribe+the+documentation+problem%3A%0A
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


## 投石杖专用弹药的验证示例

投石杖的直接发射功能使用 `SLING_LAUNCHER` 标志；兼容弹药必须有 `SLING_AMMO`，并提供目标明确的 `transform` 使用动作。现有六种专用手雷和燃烧瓶保留物品 ID 与手动激活规则。手持投石杖使用开火操作，从身上取一发；有多个弹种时先选择。取消瞄准不会取出弹药、点燃引信或消耗行动点。

确认发射后，原有转换动作负责火源、损坏导致的激活失败和引信。只免除发射时的“弹药必须手持”要求；已激活的弹药、其他角色或地面上的弹药、弹匣内及密封口袋内的弹药不能直接使用。普通专用手雷的耗时为 200 行动点准备时间，加现有投掷与取物耗时；燃烧瓶额外保留点火动作的耗时。

`STOP_ON_CONTACT` 只用于直接发射的投射物：沿实际弹道遇到首个地面生物或不可通行障碍时落下。伤害仍走投射物命中判定，闪避伤害不让弹药穿到后排。手雷由落地后的活动物品按原引信爆炸，不复制弹药定义里的即时爆炸效果；燃烧瓶保留撞击起火。普通 `t` 手投不添加这个标志。

验证应覆盖原生数据加载、一次只消耗一发、取消与无火源不消耗弹药、墙与前排怪物拦截、到期爆炸和保留手动激活。对应源码为 `src/sling.cpp`、`src/ballistics.cpp`、`src/ranged.cpp`，回归测试为 `tests/staff_sling_test.cpp`。

## 双弹仓和射击模式的回归验证

KSG 的两条弹仓应分别由主枪和 `ksg_aux_shotgun` 管理，每条弹仓容量为 7 发。
调整 `clip_size` 不足以改变实际容量，需检查 `pocket_data` 的弹药限制。
恢复专用弹仓时还须移除将它替换成其他枪械的迁移，并验证生成、独立装填、切换弹种、
开火扣弹和保存重载。已有第二弹仓不应重复添加；旧版合并弹仓的 14 发应保留为 7＋7。

DP-12 的双发模式应通过实际 `fire_gun` 验证一次消耗两发，剩一发时只发射一发。
这里的两连发使用通常的逐发后坐力；不要因有两根枪管就默认启用同时齐射的 `VOLLEY`。
本次源代码中的 `[shotgun_tubes]` 聚焦测试覆盖这些行为。相关原生测试通过不等于
Android 实机操作或完整安装包已经验收；源码

---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: cpp-performance
title: 旧文档迁移草稿：performance
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
review_interval_days: 365
last_human_reviewer: Pending human review
source_paths:
- doc/c++/PERFORMANCE.md
- src/profiling.h
- tests/cata_catch.h
- tests/generic_factory_test.cpp
source_symbols:
- CATA_PROFILE_SCOPE
- BENCHMARK_TEST_CASE
source_queries: []
source_fingerprint: 11414ba7f6469ff563c62db27ec4f010678d73d127ac84f3bd540a88b4063b63
authority: docs-explanation
verified_commit: 4e3b9aa99ae59630abf60f717bdaf563b2d63245
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: bc0991fe6ca97eb54aaab563e93227943bc67b54ab65d9628fb7750884219abb
prerequisites: []
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: 'CCB contributors: g1ytx; accepted inventory identities only. Source paths and Git history
  remain authoritative.'
example_validation_ids: []
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: cpp
risk_level: high
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/performance/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/performance/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/cpp/performance/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/performance/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/4e3b9aa99ae59630abf60f717bdaf563b2d63245
source_urls:
- path: doc/c++/PERFORMANCE.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/doc/c++/PERFORMANCE.md
- path: src/profiling.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/src/profiling.h
- path: tests/cata_catch.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/tests/cata_catch.h
- path: tests/generic_factory_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/tests/generic_factory_test.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28cpp-performance%29%3A+&body=Document+ID%3A+cpp-performance%0ALanguage%3A+zh_CN%0AVerified+commit%3A+4e3b9aa99ae59630abf60f717bdaf563b2d63245%0A%0ADescribe+the+documentation+problem%3A%0A
---

# 旧文档迁移草稿：performance

本页是 `cpp-performance` 的迁移草稿页面。它记录 **1** 条冻结清单记录，但不把旧说明提升为运行时契约。

- Stable document IDs: `cpp-performance`
- Target: `cpp/performance.md`
- Replacement: cpp-performance
- Archive reason: —

## 清单记录

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| cpp-performance | doc/c++/PERFORMANCE.md | migrate_rewrite | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## 权威边界

运行时行为仍以 CCB 源码和测试为准；JSON/Lua/API 以 Schema、声明、注册信息和生成清单为准；构建以 CI、CMake、Makefile 与 Gradle 为准。本页只解释迁移状态、历史和可审核来源。若旧正文与当前契约冲突，应以契约为准。

## 当前 CCB 性能测量入口

重复性微基准和运行时 profiling 是两种不同证据。不要提交临时 `printf`/wall-clock 对比，
也不要让优化只在一个未记录的本地场景成立。先定义指标、数据集、build、seed 与噪声控制，
再比较相同 commit 条件下的 before/after。

### Catch2 microbenchmark

`BENCHMARK_TEST_CASE` 自动加入隐藏 `[.]` 与 `[benchmark]` tag，因此默认 correctness suite
不会运行它：

```cpp
BENCHMARK_TEST_CASE( "route benchmark", "[pathfinding]" )
{
    BENCHMARK( "route" ) {
        return here.route( from, target, settings, avoid );
    };
}
```

```sh
./tests/cata_test '[benchmark][pathfinding]'
```

把正确性断言放在 measured expression 外；每个 sample 需要不计时 setup/teardown 时使用
`BENCHMARK_ADVANCED`。保存完整输出、compiler、build type、CPU/power 状态与样本数据。

### 运行时 profiling

游戏代码只通过 `src/profiling.h` 的 `CATA_PROFILE_*` 宏接入：

```cpp
#include "profiling.h"

void expensive_function()
{
    CATA_PROFILE_SCOPE();
    // Work being measured.
}
```

当前宏在 `TRACY=ON` 配置时转发到 Tracy，否则为空操作。不要直接使用 `ZoneScoped`、
`FrameMark` 等 vendor 宏；统一 wrapper 保证 disabled build 和未来 profiler 替换。profiled
build 的准确命令以当前 CMake option 和 CI 为准。

### 诊断计时与性能修复

用于解释 live failure 的阈值计时可以靠近 owner code，使用 `steady_clock`、稳定日志前缀并
写明阈值。它是 telemetry，不是可重复 benchmark；新性能结论仍要用 benchmark/profile。

优化前先确认 hotspot。审阅 alloc/IO/cache、算法复杂度和每 turn/每 entity 调用次数，同时
检查结果、确定性和存档/Mod 语义未变。性能提升不能用删除验证、降低正确性或改变 gameplay
换取。

### 报告最低要求

记录 before/after 分布或足够样本、误差/波动、输入规模、compiler flags、commit 与平台。
无法稳定复现的变化标为 inconclusive，不把单次最快值写成提升比例。大型 Tracy capture、
symbol database 和 profile 输出作为 artifact，不提交进文档仓库。

## 历史与归属

清单中的已接受贡献者为：g1ytx。许可证：CC-BY-SA-3.0。异常贡献者原始值没有导入或发布。

源清单冻结 commit 为 `0378ca2b84303cf614c617c9d9eaa50138cd21ff`；本次交叉仓验证 commit 为 `80828049edb3adf2a13bb2912a19373dc4e69f32`；聚合源指纹为 `11414ba7f6469ff563c62db27ec4f010678d73d127ac84f3bd540a88b4063b63`。[过滤历史实验报告](/CCB-Docs/migration/filtered-history-experiment/)记录了为何不导入整个游戏仓库历史。

## CCB 中保留的正文

- [`doc/c++/PERFORMANCE.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/c%2B%2B/PERFORMANCE.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/c%2B%2B/PERFORMANCE.md)

## 替代与下一步

该页保持 Draft，直到 Responsible human 对正文、来源与替代关系完成审查；Draft 不进入正式导航、搜索或 AI allowlist。

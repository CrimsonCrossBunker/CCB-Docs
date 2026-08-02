---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: operations.performance-profiling
title: 性能分析
language: zh_CN
status: draft
doc_type: how-to
audiences:
- experienced-contributor
- maintainer
owners:
- CCB maintainers
reviewers:
- Documentation reviewers
review_interval_days: 120
last_human_reviewer: Pending human review
source_paths:
- doc/c++/PERFORMANCE.md
- src/profiling.h
- CMakeLists.txt
- tests/cata_catch.h
source_symbols:
- CATA_PROFILE_SCOPE()
source_queries:
- option(TRACY
source_fingerprint: 8a73c242eba50e7d63d1fc5ced0423b9ce2df5330af4af3a98d693a84272235f
authority: source-and-tests
verified_commit: dbaedf8357408ae6f96309732d6e087e9b878e18
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 8cb921c250a51e014a9c075ad0e2ae808c596ca752bfaa6e66a2beea3bd9e545
prerequisites:
- validation.testing
- validation.debugging
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: CCB contributors; see source paths and Git history.
example_validation_ids:
- cmake-configure
- cpp-tests
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: performance
risk_level: normal
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/operations/performance-profiling/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/operations/performance-profiling/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/operations/performance-profiling/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/operations/performance-profiling/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/dbaedf8357408ae6f96309732d6e087e9b878e18
source_urls:
- path: doc/c++/PERFORMANCE.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/dbaedf8357408ae6f96309732d6e087e9b878e18/doc/c++/PERFORMANCE.md
- path: src/profiling.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/dbaedf8357408ae6f96309732d6e087e9b878e18/src/profiling.h
- path: CMakeLists.txt
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/dbaedf8357408ae6f96309732d6e087e9b878e18/CMakeLists.txt
- path: tests/cata_catch.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/dbaedf8357408ae6f96309732d6e087e9b878e18/tests/cata_catch.h
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28operations.performance-profiling%29%3A+&body=Document+ID%3A+operations.performance-profiling%0ALanguage%3A+zh_CN%0AVerified+commit%3A+dbaedf8357408ae6f96309732d6e087e9b878e18%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# 性能分析

性能工作从可复现场景与用户可见 metric 开始。不能凭直觉、一次 debug build 或不同
commit/config 的 profile 优化。

## 选择证据

- 可重复、隔离算法比较使用 Catch2 microbenchmark；
- 端到端场景使用稳定 wall/turn/frame measurement；
- Tracy scope/frame/text/plot 使用 `src/profiling.h` 的 `CATA_PROFILE_*` wrapper；
- CPU、allocation、I/O、GPU 或 Android 专属问题使用平台 profiler；
- diagnostic timing 只解释 live failure，不能替代 benchmark。

## Tracy build

安装 Tracy client library 后，仓库契约为：

```sh
cmake -S . -B build-tracy -DTRACY=ON
cmake --build build-tracy -j
```

关闭 `TRACY` 时 wrapper 编译为空操作。游戏代码不能直接调用 Tracy macro，这样才能保持
disabled build 与 profiler 选择。

## 可复现比较

记录 commit、compiler、optimization/LTO、sanitizer、frontend、SDL、hardware、power mode、
world/save/Mod、RNG seed、scenario、warmup、sample count、statistic 与 raw result。相同条件
比较 before/after，接受加速前检查 correctness test。

## 热路径规则

缓存前先说明 owner 与 invalidation boundary。检查 complexity、allocation、string/
translation、registry lookup、map/inventory scan、renderer stall 与跨语言调用。不能用
determinism、save compatibility 或有界 Lua handle 换速度。

## 生成 artifact

profiler capture、compiler time trace、flame graph、`compile_commands.json`、Doxygen、ctags、
clangd index 与大型 symbol database 都是 generated。需要时作为有范围 CI/review artifact
上传，不提交。

## 验收

报告 baseline/new 数值与 uncertainty、correctness check、测试平台，以及任何 memory/
startup/build-size 回归。结果不确定时如实报告，不能声称已优化。

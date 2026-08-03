---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: operations.performance-profiling
title: Performance profiling
language: en
status: active
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
include_in_search: true
include_in_ai_index: true
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
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/operations/performance-profiling/
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
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28operations.performance-profiling%29%3A+&body=Document+ID%3A+operations.performance-profiling%0ALanguage%3A+en%0AVerified+commit%3A+dbaedf8357408ae6f96309732d6e087e9b878e18%0A%0ADescribe+the+documentation+problem%3A%0A
---

# Performance profiling

Performance work begins with a reproducible scenario and a user-visible metric. Do not optimize
from intuition, one debug build, or a profile captured from a different commit/configuration.

## Choose the evidence

- Use Catch2 microbenchmarks for repeatable, isolated algorithm comparisons.
- Use stable wall/turn/frame measurements for an end-to-end scenario.
- Use the `CATA_PROFILE_*` wrappers in `src/profiling.h` for Tracy scopes, frames, text, and plots.
- Use a platform profiler for CPU, allocation, I/O, GPU, or Android-specific questions.
- Use diagnostic timings only to explain a live failure, not as a substitute for a benchmark.

## Tracy build

With an installed Tracy client library, the repository contract is:

```sh
cmake -S . -B build-tracy -DTRACY=ON
cmake --build build-tracy -j
```

When `TRACY` is off, the wrappers compile to no-ops. Game code must not call Tracy macros
directly; this preserves disabled builds and profiler choice.

## Reproducible comparison

Record commit, compiler, optimization/LTO, sanitizer, frontend, SDL version, hardware, power
mode, world/save/mods, RNG seed, scenario, warmup, sample count, statistic, and raw results.
Compare before/after under the same conditions and inspect correctness tests before accepting a
speedup.

## Hot-path rules

Name the owner and invalidation boundary before caching. Check complexity, allocations, string/
translation work, registry lookups, map/inventory scans, renderer stalls, and cross-language calls.
Do not trade deterministic behavior, save compatibility, or bounded Lua handles for speed.

## Generated artifacts

Profiler captures, compiler time traces, flame graphs, `compile_commands.json`, Doxygen, ctags,
clangd indexes, and large symbol databases are generated. Upload them as scoped CI/review
artifacts when useful; do not commit them.

## Acceptance

State baseline and new numbers with uncertainty, correctness checks, platforms tested, and any
memory/startup/build-size regression. If results are inconclusive, report that rather than
claiming an optimization.

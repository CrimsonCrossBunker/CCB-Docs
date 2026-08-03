---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: cpp-performance
title: 'Legacy migration draft: performance'
language: en
status: draft
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
verified_commit: 02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 390f4e26ae3cb3b6cfe70fa43664fe98ce50ab08f6ff96822ed4cf88f3229d9f
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
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/568
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/cpp/performance/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/performance/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/cpp/performance/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/performance/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b
source_urls:
- path: doc/c++/PERFORMANCE.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/doc/c++/PERFORMANCE.md
- path: src/profiling.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/src/profiling.h
- path: tests/cata_catch.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/tests/cata_catch.h
- path: tests/generic_factory_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/tests/generic_factory_test.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28cpp-performance%29%3A+&body=Document+ID%3A+cpp-performance%0ALanguage%3A+en%0AVerified+commit%3A+02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# Legacy migration draft: performance

This is the migration draft page for `cpp-performance`. It records **1** frozen inventory record(s), but it does not promote legacy prose into a runtime contract.

- Stable document IDs: `cpp-performance`
- Target: `cpp/performance.md`
- Replacement: cpp-performance
- Archive reason: —

## Inventory records

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| cpp-performance | doc/c++/PERFORMANCE.md | migrate_rewrite | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## Authority boundary

CCB source and tests remain authoritative for runtime behaviour; schemas, declarations, registrations, and generated inventories govern JSON/Lua/API; CI, CMake, Makefile, and Gradle govern builds. This page explains migration state, history, and auditable provenance only. A current contract wins over conflicting legacy prose.

## Current CCB performance measurement entry points

Repeatable microbenchmarks and runtime profiling are different forms of evidence. Do not commit
temporary `printf` or wall-clock comparisons, and do not base an optimization on one undocumented
local scenario. Define the metric, data set, build, seed, and noise controls before comparing
before and after under equivalent commit conditions.

### Catch2 microbenchmarks

`BENCHMARK_TEST_CASE` adds hidden `[.]` and `[benchmark]` tags, keeping it out of the default
correctness suite:

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

Keep correctness assertions outside the measured expression. Use `BENCHMARK_ADVANCED` when
each sample needs unmeasured setup or teardown. Save full output, compiler, build type, CPU and
power state, and sample data.

### Runtime profiling

Game code integrates only through the `CATA_PROFILE_*` macros in `src/profiling.h`:

```cpp
#include "profiling.h"

void expensive_function()
{
    CATA_PROFILE_SCOPE();
    // Work being measured.
}
```

The current macros forward to Tracy in a `TRACY=ON` configuration and become no-ops otherwise.
Do not use vendor macros such as `ZoneScoped` or `FrameMark` directly. The wrapper preserves
disabled builds and future profiler changes. Take the exact profiled-build command from current
CMake options and CI.

### Diagnostic timing and performance fixes

A thresholded timing that explains a live failure can remain near its owner code if it uses
`steady_clock`, a stable log prefix, and a documented threshold. It is telemetry, not a repeatable
benchmark; performance claims still need a benchmark or profile.

Confirm a hotspot before optimizing. Review allocations, I/O, cache behavior, algorithmic
complexity, and calls per turn or entity while preserving results, determinism, and save or Mod
semantics. Removing validation, reducing correctness, or changing gameplay is not a performance fix.

### Minimum report

Record before and after distributions or enough samples, error or variance, input size, compiler
flags, commit, and platform. Mark unstable results inconclusive instead of reporting one fastest
sample as a percentage improvement. Store large Tracy captures, symbol databases, and profiles
as artifacts rather than repository documentation.

## History and attribution

Accepted inventory contributors: g1ytx. License: CC-BY-SA-3.0. Raw rejected or anomalous contributor values were not imported or published.

The source inventory is frozen at `0378ca2b84303cf614c617c9d9eaa50138cd21ff`; this cross-repository verification uses `02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b`; the aggregate source fingerprint is `11414ba7f6469ff563c62db27ec4f010678d73d127ac84f3bd540a88b4063b63`. The [filtered-history experiment](/CCB-Docs/en/migration/filtered-history-experiment/) explains why the whole game repository history is not imported.

## Bodies retained in CCB

- [`doc/c++/PERFORMANCE.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/doc/c%2B%2B/PERFORMANCE.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/doc/c%2B%2B/PERFORMANCE.md)

## Replacement and next step

This page remains Draft until a Responsible human reviews the prose, sources, and replacement relationship. Drafts stay outside production navigation, search, and the AI allowlist.

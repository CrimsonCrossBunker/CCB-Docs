---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: cpp-testing
title: 'Legacy migration draft: cpp'
language: en
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
- doc/c++/TESTING.md
- tests/CMakeLists.txt
- tests/Makefile
- tests/cata_catch.h
- .github/workflows/matrix.yml
source_symbols:
- BENCHMARK_TEST_CASE
source_queries: []
source_fingerprint: 35adfef3c97d8e649e0a2716c8976ea48b953607a1794f0839ca9b65818600f4
authority: docs-explanation
verified_commit: 4e3b9aa99ae59630abf60f717bdaf563b2d63245
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 027c5f6c52f834bdf710bf9e1cc02b7e0716bd3fa9a0f6ab0f70b63b1e97da6f
prerequisites: []
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: 'CCB contributors: g1ytx, thaelina; accepted inventory identities only. Source paths and
  Git history remain authoritative.'
example_validation_ids: []
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: testing
risk_level: high
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/testing/cpp/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/testing/cpp/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/testing/cpp/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/testing/cpp/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/4e3b9aa99ae59630abf60f717bdaf563b2d63245
source_urls:
- path: doc/c++/TESTING.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/doc/c++/TESTING.md
- path: tests/CMakeLists.txt
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/tests/CMakeLists.txt
- path: tests/Makefile
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/tests/Makefile
- path: tests/cata_catch.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/tests/cata_catch.h
- path: .github/workflows/matrix.yml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/.github/workflows/matrix.yml
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28cpp-testing%29%3A+&body=Document+ID%3A+cpp-testing%0ALanguage%3A+en%0AVerified+commit%3A+4e3b9aa99ae59630abf60f717bdaf563b2d63245%0A%0ADescribe+the+documentation+problem%3A%0A
---

# Legacy migration draft: cpp

This is the migration draft page for `cpp-testing`. It records **1** frozen inventory record(s), but it does not promote legacy prose into a runtime contract.

- Stable document IDs: `cpp-testing`
- Target: `testing/cpp.md`
- Replacement: cpp-testing
- Archive reason: —

## Inventory records

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| cpp-testing | doc/c++/TESTING.md | migrate_rewrite | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## Authority boundary

CCB source and tests remain authoritative for runtime behaviour; schemas, declarations, registrations, and generated inventories govern JSON/Lua/API; CI, CMake, Makefile, and Gradle govern builds. This page explains migration state, history, and auditable provenance only. A current contract wins over conflicting legacy prose.

## Current CCB C++ testing flow

CCB's C++ tests use Catch2, live under `tests/`, and normally build as `tests/cata_test`.
Build the tests, then reproduce with the narrowest case or tag. Do not begin a focused fix by
running every expensive matrix job.

```sh
make -j2 tests
./tests/cata_test --list-tests
./tests/cata_test '[relevant-tag]'
```

Adjust job count to local resources. The complete suite and platform or feature combinations
are defined by CI such as `.github/workflows/matrix.yml`; report combinations not run locally.

### Writing a test

```cpp
TEST_CASE( "example_status_expires", "[effect][ccb_example]" )
{
    avatar dummy;
    // Arrange only the state this behavior owns.

    REQUIRE( precondition_is_true( dummy ) );
    perform_action( dummy );
    CHECK( observable_result( dummy ) );
}
```

- Name observable behavior and tag the subsystem for focused runs.
- Use `REQUIRE` for a prerequisite of later assertions and `CHECK` for independent results.
- Call the lowest-level entry that expresses the contract instead of a large UI or game loop.
- Explicitly reset avatar, map, calendar, RNG, options, factories, and other global state.
- Assert fixture properties taken from JSON so content changes cannot silently alter the test.
- Do not depend on test order or files and globals left by another case.

### Regression-test structure

A bug fix starts with a minimal regression that fails on the old implementation, then changes
the implementation. Cover the normal path, the reported failure, and the most important
boundary without freezing accidental error text as a contract. For random algorithms, fix or
record the seed and test invariants rather than one random result.

Save, JSON-loader, Lua-bridge, Android, or platform behavior needs the corresponding layer test.
A C++ unit test is not a substitute for a full Mod load, serialization round trip, or platform build.

### Diagnosing failure

Rerun the same filter and seed and preserve the first assertion plus relevant logs. Establish
whether the diff owns the failure and whether the base commit reproduces it before fixing or
recording an existing failure. Do not delete an assertion because CI is red or call a failure
unrelated without base evidence.

Performance comparisons use `BENCHMARK_TEST_CASE` outside the default correctness suite. See
[performance](../cpp/performance.md).

## History and attribution

Accepted inventory contributors: g1ytx, thaelina. License: CC-BY-SA-3.0. Raw rejected or anomalous contributor values were not imported or published.

The source inventory is frozen at `0378ca2b84303cf614c617c9d9eaa50138cd21ff`; this cross-repository verification uses `80828049edb3adf2a13bb2912a19373dc4e69f32`; the aggregate source fingerprint is `35adfef3c97d8e649e0a2716c8976ea48b953607a1794f0839ca9b65818600f4`. The [filtered-history experiment](/CCB-Docs/en/migration/filtered-history-experiment/) explains why the whole game repository history is not imported.

## Bodies retained in CCB

- [`doc/c++/TESTING.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/c%2B%2B/TESTING.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/c%2B%2B/TESTING.md)

## Replacement and next step

This page remains Draft until a Responsible human reviews the prose, sources, and replacement relationship. Drafts stay outside production navigation, search, and the AI allowlist.

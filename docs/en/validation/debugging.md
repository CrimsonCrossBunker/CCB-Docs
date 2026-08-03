---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: validation.debugging
title: Debugging and failure isolation
language: en
status: active
doc_type: how-to
audiences:
- new-contributor
- experienced-contributor
- maintainer
owners:
- CCB maintainers
reviewers:
- Documentation reviewers
review_interval_days: 120
last_human_reviewer: LYHGLYTX
source_paths:
- CONTRIBUTING.md
- doc/c++/TESTING.md
- doc/c++/PERFORMANCE.md
- tests/AGENTS.md
source_symbols: []
source_queries: []
source_fingerprint: 364c4a6f53fc762b2419030f2ce970552bf1a03b0a57e51c81360dcdf7582b9d
authority: docs-explanation
verified_commit: d6aa4576178a1a6ff21ffede7f282a994fcbc4b3
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 4a57412f7e4b828dd4ade96cb3d3fdb4bab31f077759c40f2e9cb0472d7445f8
prerequisites:
- validation.testing
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: CCB contributors; see source paths and Git history.
example_validation_ids: []
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: testing
risk_level: normal
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/560
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/validation/debugging/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/validation/debugging/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/validation/debugging/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/validation/debugging/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/d6aa4576178a1a6ff21ffede7f282a994fcbc4b3
source_urls:
- path: CONTRIBUTING.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d6aa4576178a1a6ff21ffede7f282a994fcbc4b3/CONTRIBUTING.md
- path: doc/c++/TESTING.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d6aa4576178a1a6ff21ffede7f282a994fcbc4b3/doc/c++/TESTING.md
- path: doc/c++/PERFORMANCE.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d6aa4576178a1a6ff21ffede7f282a994fcbc4b3/doc/c++/PERFORMANCE.md
- path: tests/AGENTS.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d6aa4576178a1a6ff21ffede7f282a994fcbc4b3/tests/AGENTS.md
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28validation.debugging%29%3A+&body=Document+ID%3A+validation.debugging%0ALanguage%3A+en%0AVerified+commit%3A+d6aa4576178a1a6ff21ffede7f282a994fcbc4b3%0A%0ADescribe+the+documentation+problem%3A%0A
---

# Debugging and failure isolation

Good debugging fixes the symptom and boundary before selecting tools. Do not
guess a repair from the last log line or change unrelated game behaviour merely
to silence an error.

## Build a reproducible case

Record the minimum context:

- CCB commit, platform, compiler, and build options;
- world, save, and mod set, including whether a new world reproduces the issue;
- exact actions, expected result, and actual result;
- relevant `debug.log` interval, stack, assertion, and first error;
- test filter, RNG seed, repeat count, and whether only optimized builds fail.

Reproduce on a clean supported configuration before adding mods or resource
packs one at a time. Never delete the original save; test migration or recovery
on a copy.

## Route by failure stage

| Stage | Inspect first | Evidence |
| --- | --- | --- |
| Configure | Preset, dependency, and feature flag | Complete configure command and first error |
| Compile/link | First failed translation unit, symbol, and library order | Original compiler diagnostic |
| Startup/load | JSON/mod order, schema, and resource path | `debug.log` and minimal data set |
| Runtime | Call stack, object lifetime, and invariants | Focused test or debugger backtrace |
| Save/load | Save version, migration, and invalid IDs | Save copy and regression test |
| Performance | Repeatable workload and release build | Profile data, not subjective timing |

## Select tools

- Use `rg` to trace log text, action IDs, JSON types, or assertions to
  registration and callers.
- Turn the case into a focused Catch2 test, then widen the test scope.
- For native crashes, use the platform debugger and a symbolized backtrace;
  preserve logcat and native crash data on Android.
- Measure a repeatable workload before optimizing. Follow
  `doc/c++/PERFORMANCE.md`, and do not commit large profiles, clangd indexes,
  ctags databases, or Doxygen HTML.

## Common traps

- Later errors may be cascades from the first loader failure.
- Debug and Release can expose different assertions, initialization bugs, and
  optimizer-sensitive behaviour.
- An upstream fix is not automatically safe to cherry-pick; verify CCB
  divergence and compatibility.
- If a documented command is stale, mark and repair the page; do not alter the
  build system to accommodate obsolete prose.

After diagnosis, preserve the minimal reproduction as a test, run the affected
levels from the [testing strategy](testing.md), and report executed and skipped
platform checks separately.

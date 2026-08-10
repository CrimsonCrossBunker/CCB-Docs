---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: validation.testing
title: Testing strategy
language: en
status: stale
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
- AGENTS.md
- ai/test-matrix.yml
- Makefile
- tests/AGENTS.md
source_symbols: []
source_queries: []
source_fingerprint: d8f41b2a0b87dfca2adb78f11ba67c084acfbbfa062d2320eaaa9f3d047ba88e
authority: build-config
verified_commit: d32b9cc880a85480840d82cfa05d256c78a16615
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: true
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 27c3188f8b9caae09e06f14131656ef8e57194f1724313695c7ea0af699a2549
prerequisites:
- validation.quickstart
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: CCB contributors; see source paths and Git history.
example_validation_ids:
- agent-context
- cpp-format
- cpp-tests
- json-load
- lua-contract
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: testing
risk_level: high
pending_source_pr: null
stale_reason: 'Source paths changed after d32b9cc880a8: Makefile'
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/validation/testing/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/validation/testing/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/validation/testing/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/validation/testing/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/d32b9cc880a85480840d82cfa05d256c78a16615
source_urls:
- path: AGENTS.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/AGENTS.md
- path: ai/test-matrix.yml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/ai/test-matrix.yml
- path: Makefile
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/Makefile
- path: tests/AGENTS.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/tests/AGENTS.md
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28validation.testing%29%3A+&body=Document+ID%3A+validation.testing%0ALanguage%3A+en%0AVerified+commit%3A+d32b9cc880a85480840d82cfa05d256c78a16615%0A%0ADescribe+the+documentation+problem%3A%0A
---

# Testing strategy

CCB testing seeks the smallest reproducible evidence that covers the risk; it
does not make every pull request run every platform. Commands come from
`ai/test-matrix.yml`, Makefile, CI, and test source.

## Narrow to broad

1. Run the target file's formatter, schema check, or static contract check.
2. Run the nearest unit or regression test, with a focused Catch2 filter.
3. Run subsystem loading or integration checks such as full JSON loading.
4. Expand to matrix builds for public contracts, platforms, or releases.

| Change | Required evidence | Typical reason to expand |
| --- | --- | --- |
| C++ implementation | `make astyle-check`, focused Catch2 | Shared core, serialization, or performance hotspot |
| Test framework/public header | `make -j2 tests` | Compiler or feature-combination differences |
| JSON/EOC/mod | Formatter and `make -j2 json-check` | Loader, schema, or cross-mod interaction |
| Public Lua contract | Declaration, coverage, and focused unit checks | Native registration or manifest change |
| Agent/docs metadata | Metadata checker and `tools/agent` tests | Generated inventory or CI routing changes |
| Android | Gradle unit/build target | Java/native boundary or resource packaging |

## Light checks verified for this review

On Linux at source commit `2c899a3db790e11a6ff44d91f319064b1ee65d2a`:

```sh
# validation: agent-context
python3 tools/agent/check_project_metadata.py
python3 -m unittest discover -s tools/agent -p 'test_*.py'

# validation: lua-contract
python3 tools/lua_api/check_luals_declarations.py
python3 tools/lua_api/check_coverage.py
python3 -m unittest tools.lua_api.test_check_coverage \
  tools.lua_api.test_check_luals_declarations
```

The metadata check passed; 10 Agent tests passed; LuaLS reported 438 methods
across 66 tables; the current inventory reported 2398/2398 classified entries;
and 21 package-aware Lua unit tests passed. These coarse inventory counts do not
by themselves prove complete symbol-level API documentation.

## Write regression tests

- Name observable behaviour, not an implementation detail.
- Use a minimal fixture without test-order, current-time, or unfixed-randomness
  dependencies.
- On failure, preserve the filter, assertion context, log, and RNG seed.
- For a bug, first show the test catches the original problem, then show it
  passes after the fix.
- Do not hide a deadlock, infinite loop, or regression by increasing a timeout.

## Report truthfully

Separate Passed, Failed, and Not run in the pull request. If Windows, MSVC,
Android, or an expensive build did not run, say so; Linux configuration is not
their substitute. Record the first root cause, correction, and rerun result.
For an intermittent failure, report its seed and reproduction count.

Use the [validation quickstart](quickstart.md) for commands and
[debugging](debugging.md) for failure analysis.

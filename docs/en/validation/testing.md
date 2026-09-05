---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: validation.testing
title: Testing strategy
language: en
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
- AGENTS.md
- ai/test-matrix.yml
- Makefile
- tests/AGENTS.md
source_symbols: []
source_queries: []
source_fingerprint: edb79059c9da967e596d7c40092e3a040fb3020bddbf672e13ec8a72e2a63477
authority: build-config
verified_commit: 3053bf160578e46c1692a89c60594aa1acc6a276
verified_at: '2026-09-05'
generated: false
generated_by: null
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 03153b99ae3c8b21bac1c0271b8e58a0dbef6c60a9c65d72bf49020e0b134707
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
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/validation/testing/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/validation/testing/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/validation/testing/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/validation/testing/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/3053bf160578e46c1692a89c60594aa1acc6a276
source_urls:
- path: AGENTS.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/3053bf160578e46c1692a89c60594aa1acc6a276/AGENTS.md
- path: ai/test-matrix.yml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/3053bf160578e46c1692a89c60594aa1acc6a276/ai/test-matrix.yml
- path: Makefile
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/3053bf160578e46c1692a89c60594aa1acc6a276/Makefile
- path: tests/AGENTS.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/3053bf160578e46c1692a89c60594aa1acc6a276/tests/AGENTS.md
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28validation.testing%29%3A+&body=Document+ID%3A+validation.testing%0ALanguage%3A+en%0AVerified+commit%3A+3053bf160578e46c1692a89c60594aa1acc6a276%0A%0ADescribe+the+documentation+problem%3A%0A
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
| Public Lua contract | Declaration, coverage, and focused unit checks | Native registration or Platform contract change |
| Agent/docs metadata | Metadata checker and `tools/agent` tests | Generated inventory or CI routing changes |
| Android | Gradle unit/build target | Java/native boundary or resource packaging |

## Platform v1 contract acceptance commands

Finish a coherent Lua domain batch, including declarations and test source, before
running these acceptance checks. These are current commands, not a claim that this
documentation change rebuilt the game or verified every API behavior.

```sh
# validation: agent-context
python3 tools/agent/check_project_metadata.py
python3 -m unittest discover -s tools/agent -p 'test_*.py'

# validation: lua-contract
python3 tools/lua_api/check_luals_declarations.py
python3 tools/lua_api/check_platform_native_inventory.py
python3 tools/lua_api/check_platform_contract.py
python3 tools/lua_api/check_platform_coverage.py
python3 tools/lua_api/check_cmake_contract.py
python3 -m unittest discover -s tools/lua_api -p 'test_*.py'
```

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

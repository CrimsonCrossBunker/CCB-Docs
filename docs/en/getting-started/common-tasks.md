---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: getting-started.common-tasks
title: Common contribution tasks
language: en
status: active
doc_type: reference
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
- CONTRIBUTING.md
- ai/project-map.yml
- ai/test-matrix.yml
source_symbols: []
source_queries: []
source_fingerprint: ff99053b392e0656404b849ad5130e434f970f77b009c9a7c657ffada896586d
authority: docs-explanation
verified_commit: d32b9cc880a85480840d82cfa05d256c78a16615
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 8b9c6f923226ae3a551f607e42fec7c7584a340560704d91efddaa1a3e0555dc
prerequisites:
- getting-started.first-contribution
depends_on:
- architecture.project-map
- validation.quickstart
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
risk_group: project-context
risk_level: normal
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/getting-started/common-tasks/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/getting-started/common-tasks/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/getting-started/common-tasks/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/getting-started/common-tasks/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/d32b9cc880a85480840d82cfa05d256c78a16615
source_urls:
- path: AGENTS.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/AGENTS.md
- path: CONTRIBUTING.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/CONTRIBUTING.md
- path: ai/project-map.yml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/ai/project-map.yml
- path: ai/test-matrix.yml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/ai/test-matrix.yml
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28getting-started.common-tasks%29%3A+&body=Document+ID%3A+getting-started.common-tasks%0ALanguage%3A+en%0AVerified+commit%3A+d32b9cc880a85480840d82cfa05d256c78a16615%0A%0ADescribe+the+documentation+problem%3A%0A
---

# Common contribution tasks

Start with the root `AGENTS.md`, then read the nearest nested instructions. Use
this table to find an entry point; confirm every path and command at the source
commit you are changing.

| Goal | Inspect | Validate first |
| --- | --- | --- |
| Fix C++ behaviour | Owning `src/` type, callers, related `tests/` | C++ format and focused Catch2 test |
| Add JSON content | Similar current data plus loader/factory | JSON format, full load, ID checks |
| Change an EOC | EOC data, parser registration, talker/context tests | JSON load and focused EOC parse/test |
| Change Lua v5 | Manifest Schema, LuaLS, native registration, inventories | Declaration, parity, coverage, examples |
| Update a bundled mod | `modinfo.json`, dependencies, interactions | Load that mod and supported combinations |
| Diagnose a build | Exact platform, preset/options, first failure | Rerun the narrow failed stage |
| Port upstream | Exact source commit/PR and CCB divergence | Focused behaviour plus compatibility checks |
| Change docs | Catalog entry and declared source paths | Generate/check, strict build, internal links |

## Before opening a pull request

- Review the final diff for unrelated changes, generated files, caches,
  credentials, and machine-specific paths.
- Name the Responsible human and provide a useful Summary.
- Separate Passed, Failed, and Not run; include platform and exact commands.
- Complete Documentation impact, Related CCB-Docs PR, Affected documentation
  IDs, and Generated reference impact.
- For compatibility-sensitive changes, state save, ID, mod, Lua API, and
  platform implications explicitly.

For more detail, use the [experienced contributor index](experienced-index.md),
[project map](../architecture/project-map.md), and
[validation quickstart](../validation/quickstart.md).

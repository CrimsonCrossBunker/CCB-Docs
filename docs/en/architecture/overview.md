---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: architecture.overview
title: CCB project architecture
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
review_interval_days: 90
last_human_reviewer: LYHGLYTX
source_paths:
- AGENTS.md
- ai/project-map.yml
- src/AGENTS.md
- data/AGENTS.md
- tests/AGENTS.md
source_symbols: []
source_queries: []
source_fingerprint: 49e6f9bdf665447593d213e55f8a6692fa2c02534f1b3564a7a66710f26d5c6a
authority: docs-explanation
verified_commit: 2c899a3db790e11a6ff44d91f319064b1ee65d2a
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: e43e7e2af4484e419221ff81b4eb74b9bbff52fa87bce0cdf4d762d5c7f1eede
prerequisites:
- home
depends_on:
- architecture.project-map
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: CCB contributors; see source paths and Git history.
example_validation_ids:
- agent-context
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: architecture
risk_level: normal
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/560
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/architecture/overview/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/architecture/overview/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/architecture/overview/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/architecture/overview/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/2c899a3db790e11a6ff44d91f319064b1ee65d2a
source_urls:
- path: AGENTS.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/2c899a3db790e11a6ff44d91f319064b1ee65d2a/AGENTS.md
- path: ai/project-map.yml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/2c899a3db790e11a6ff44d91f319064b1ee65d2a/ai/project-map.yml
- path: src/AGENTS.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/2c899a3db790e11a6ff44d91f319064b1ee65d2a/src/AGENTS.md
- path: data/AGENTS.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/2c899a3db790e11a6ff44d91f319064b1ee65d2a/data/AGENTS.md
- path: tests/AGENTS.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/2c899a3db790e11a6ff44d91f319064b1ee65d2a/tests/AGENTS.md
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28architecture.overview%29%3A+&body=Document+ID%3A+architecture.overview%0ALanguage%3A+en%0AVerified+commit%3A+2c899a3db790e11a6ff44d91f319064b1ee65d2a%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# CCB project architecture

CCB is a data-driven C++ game. The native engine owns object lifetimes, map and save handling, core simulation, UI, and loading. JSON defines much of the game content; EOC expresses conditional behaviour in JSON; Lua v5 exposes a versioned, capability-gated public interface to mods.

## Layers and dependency direction

1. **Build and platform layer**: Make, CMake, Gradle, CI, and packaging scripts define toolchains and artifacts.
2. **Native runtime**: `src/` owns objects, simulation, UI, serialization, and the native Lua bridge.
3. **Data contracts**: `data/json/`, `data/core/`, and `data/mods/` are consumed by registrations, factories, and validators.
4. **Scripting contract**: the Lua manifest, LuaLS declarations, native registration, and generated inventories must agree.
5. **Validation layer**: `tests/` and repository tools validate behaviour, data, public contracts, and generated boundaries.

Data and scripts normally enter through registered engine interfaces. Explanatory documentation is not a new runtime contract, and source semantics must not be changed merely to match stale prose.

## Data ownership

- C++ types own runtime state and serialization invariants.
- JSON IDs are compatibility boundaries across data, saves, and mods; a rename needs migration or obsoletion data.
- EOC talkers, variables, and context determine evaluation semantics; field names alone are insufficient.
- Lua may use only capabilities declared by its manifest; public symbols come from the v5 contract chain.
- Generated files are derived from source contracts. Fix the generator or source rather than patching output.

## Extension points

Prefer an existing JSON type, EOC facility, or supported Lua API for content. Extend C++ only when data interfaces cannot express the required behaviour, and review registration, validation, serialization, tests, and documentation impact together.

CCB selectively ports from CDDA, CBN, and compatible sources while retaining its own behaviour, data, and Lua API. Reviews distinguish shared ancestral behaviour, newer upstream behaviour, and intentional CCB divergence.

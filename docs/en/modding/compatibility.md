---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: mod-compatibility
title: 'Legacy migration draft: compatibility'
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
- doc/MOD_COMPATIBILITY.md
- src/mod_manager.cpp
- src/init.cpp
- build-scripts/get_all_mods.py
- data/mods/MindOverMatter/mod_interactions/innawood/recipes.json
source_symbols:
- DynamicDataLoader::load_mod_interaction_files_from_path
source_queries: []
source_fingerprint: 6af06ba4ae4f015b5b049b078dc768874554132e2136f98b07e1cc64625da2b0
authority: docs-explanation
verified_commit: 80828049edb3adf2a13bb2912a19373dc4e69f32
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: ef1b50f80c175210c6c7d92a165859b136b3e95b186602f7be5956f20a260854
prerequisites: []
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: 'CCB contributors: thaelina; accepted inventory identities only. Source paths and Git history
  remain authoritative.'
example_validation_ids: []
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: mods
risk_level: normal
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/568
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/modding/compatibility/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/modding/compatibility/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/modding/compatibility/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/modding/compatibility/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/80828049edb3adf2a13bb2912a19373dc4e69f32
source_urls:
- path: doc/MOD_COMPATIBILITY.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/MOD_COMPATIBILITY.md
- path: src/mod_manager.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/src/mod_manager.cpp
- path: src/init.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/src/init.cpp
- path: build-scripts/get_all_mods.py
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/build-scripts/get_all_mods.py
- path: data/mods/MindOverMatter/mod_interactions/innawood/recipes.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/data/mods/MindOverMatter/mod_interactions/innawood/recipes.json
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28mod-compatibility%29%3A+&body=Document+ID%3A+mod-compatibility%0ALanguage%3A+en%0AVerified+commit%3A+80828049edb3adf2a13bb2912a19373dc4e69f32%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# Legacy migration draft: compatibility

This is the migration draft page for `mod-compatibility`. It records **1** frozen inventory record(s), but it does not promote legacy prose into a runtime contract.

- Stable document IDs: `mod-compatibility`
- Target: `modding/compatibility.md`
- Replacement: mod-compatibility
- Archive reason: —

## Inventory records

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| mod-compatibility | doc/MOD_COMPATIBILITY.md | migrate_rewrite | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## Authority boundary

CCB source and tests remain authoritative for runtime behaviour; schemas, declarations, registrations, and generated inventories govern JSON/Lua/API; CI, CMake, Makefile, and Gradle govern builds. This page explains migration state, history, and auditable provenance only. A current contract wins over conflicting legacy prose.

## Conditional Mod compatibility data

`mod_interactions/` lets one Mod load a patch only when one named target Mod is active. It fits
cross-Mod references, compatibility EOCs, combined recipes, or targeted overrides. It is not a
normal dependency: the base Mod should still load independently when the interaction is absent.

### Directory contract

Suppose the current Mod ID is `xedra_evolved` and compatibility is needed only when
`mindovermatter` is active:

```text
Xedra_Evolved/
├── modinfo.json
├── ordinary-content.json
└── mod_interactions/
    └── mindovermatter/
        └── mom-compat-data.json
```

The directory name must match the target Mod ID exactly, including case. Ordinary loading
recursively excludes all of `mod_interactions`; after every active Mod's ordinary data loads, the
loader processes interaction directories in active-Mod order. The current implementation checks
one target-ID directory level and does not express “both Mods active” with `a/b/` nesting.

### Source and override boundaries

Interaction definitions receive the source `base_mod#target_mod`, for example
`xedra_evolved#mindovermatter`. `#` is therefore reserved for combined provenance and is forbidden
in an ordinary Mod ID. Preserve this combined source in diagnostics and object provenance.

Late loading permits only overrides or extensions supported by the owning loader. Do not assume
every object type has identical merge semantics. Inspect the factory or loader for `copy-from`,
`extend`, duplicate IDs, deletion, and obsoletion. Loading later also cannot repair a reference that
an earlier phase must resolve before finalization.

### More than one condition

Do not build nested directories when content needs both A and B. One interaction may load a
compatibility EOC that checks another supported registry condition, or a dedicated compatibility
Mod may declare both `dependencies`. Choose based on whether partial combinations should remain
usable and which package owns the published IDs.

### Validation matrix

Test at least the base Mod alone, the target alone, both together after dependency ordering, and an
old save containing related IDs. Run formatting, `make -j2 json-check`, and `--check-mods` for each
combination. Check duplicate IDs, source diagnostics, EOC talkers and context, save/reload, and
removal of either Mod.

Testing only the combined case misses interaction data leaking into ordinary loading or a base file
that accidentally references the target.

## History and attribution

Accepted inventory contributors: thaelina. License: CC-BY-SA-3.0. Raw rejected or anomalous contributor values were not imported or published.

The source inventory is frozen at `0378ca2b84303cf614c617c9d9eaa50138cd21ff`; this cross-repository verification uses `80828049edb3adf2a13bb2912a19373dc4e69f32`; the aggregate source fingerprint is `6af06ba4ae4f015b5b049b078dc768874554132e2136f98b07e1cc64625da2b0`. The [filtered-history experiment](/CCB-Docs/en/migration/filtered-history-experiment/) explains why the whole game repository history is not imported.

## Bodies retained in CCB

- [`doc/MOD_COMPATIBILITY.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/MOD_COMPATIBILITY.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/MOD_COMPATIBILITY.md)

## Replacement and next step

This page remains Draft until a Responsible human reviews the prose, sources, and replacement relationship. Drafts stay outside production navigation, search, and the AI allowlist.

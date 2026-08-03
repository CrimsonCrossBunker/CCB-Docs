---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: mods.in-repository-policy
title: 'Legacy migration draft: in repository policy'
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
last_human_reviewer: LYHGLYTX
source_paths:
- doc/IN_REPO_MODS.md
- CONTRIBUTING.md
- GOVERNANCE.md
- data/mods/AGENTS.md
- src/mod_manager.cpp
- tools/load_all_mods.sh
source_symbols:
- mod_manager::load_modfile
source_queries: []
source_fingerprint: 975c66966726b069315e72689255c20f76c8c8fdc8ec00981feb775dd4fbfa02
authority: docs-explanation
verified_commit: d32b9cc880a85480840d82cfa05d256c78a16615
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: c1bea1fcad7ea5ef7637d867296dcb6f5011c2b4039df264c00e331ec8c518d6
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
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/mods/in-repository-policy/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/mods/in-repository-policy/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/mods/in-repository-policy/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/mods/in-repository-policy/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/d32b9cc880a85480840d82cfa05d256c78a16615
source_urls:
- path: doc/IN_REPO_MODS.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/doc/IN_REPO_MODS.md
- path: CONTRIBUTING.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/CONTRIBUTING.md
- path: GOVERNANCE.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/GOVERNANCE.md
- path: data/mods/AGENTS.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/data/mods/AGENTS.md
- path: src/mod_manager.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/src/mod_manager.cpp
- path: tools/load_all_mods.sh
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/tools/load_all_mods.sh
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28mods.in-repository-policy%29%3A+&body=Document+ID%3A+mods.in-repository-policy%0ALanguage%3A+en%0AVerified+commit%3A+d32b9cc880a85480840d82cfa05d256c78a16615%0A%0ADescribe+the+documentation+problem%3A%0A
---

# Legacy migration draft: in repository policy

This is the migration draft page for `mods.in-repository-policy`. It records **1** frozen inventory record(s), but it does not promote legacy prose into a runtime contract.

- Stable document IDs: `mods.in-repository-policy`
- Target: `mods/in-repository-policy.md`
- Replacement: https://crimsoncrossbunker.github.io/CCB-Docs/mods/in-repository-policy/
- Archive reason: —

## Inventory records

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| mods.in-repository-policy | doc/IN_REPO_MODS.md | migrate_rewrite | stubbed | b1ee97987589450da70f30ee2feed12c9d18f479 | — |

## Authority boundary

CCB source and tests remain authoritative for runtime behaviour; schemas, declarations, registrations, and generated inventories govern JSON/Lua/API; CI, CMake, Makefile, and Gradle govern builds. This page explains migration state, history, and auditable provenance only. A current contract wins over conflicting legacy prose.

## CCB in-repository Mod policy

Shipping a Mod with the game improves visibility, shared Issue and PR handling, and continuous
load checks. It also assigns compatibility, release, and security cost to the whole project.
Admission to `data/mods/` is not a promise of permanent inclusion, core-team maintenance, or
exclusive author control. An in-repository Mod remains community-contributed project content.

### Admission criteria

A proposal needs a clear purpose that can be reviewed over time: a distinct content experience,
an accessibility or interface capability, or isolation for an optional feature still under
development. An unrelated object collection, a preference pack that only disables working
features, or a package without maintenance boundaries does not justify repository-wide cost.

Before admission, require at least:

- accurate authors, real GitHub maintainers, category, dependencies, and conflicts in `modinfo.json`;
- auditable provenance, licensing, and permission for third-party assets;
- explicit stable IDs, save policy, dependency boundaries, and CCB/upstream differences;
- passing JSON, EOC, Lua, and complete-Mod loading validation;
- an active curator willing to triage, review, and follow compatibility continuously;
- agreement with dependency maintainers when a new relationship burdens another bundled Mod.

Do not invent `CODEOWNERS` as a substitute for real responsibility. The loader reads and displays
the `maintainers` account set, but a person must still accept the governance responsibility in a
PR or Issue.

### Curator responsibilities

A curator judges whether contributions fit the Mod purpose, reviews or requests changes on its
PRs, and at least acknowledges defects and helps find a repair path. Curators need not author
every fix and cannot exclude community contribution. Their approval is domain input; merge still
follows CCB governance, Responsible-human review, and required checks.

Changes affecting dependants, public IDs, saves, Lua APIs, licensing, or player safety need notice
to affected maintainers and combination-specific evidence. Track balance disagreement separately
from load failure so “it loads” is never mistaken for design approval.

### Orphaning, obsoletion, and removal

Maintainers may begin an orphan or obsolete review when curators are persistently unavailable,
releases repeatedly break, licensing is unclear, the purpose expires, or maintenance cost becomes
unmanageable. Open a public Issue with an owner and deadline first; do not delete a Mod based on one
missed response. `obsolete: true` hides it from new-world selection while retaining old-save
recognition; it is not immediate repository deletion.

Rescue requires a confirmed new curator, repaired blockers, restored validation, and updated
`maintainers`. Before final removal, document stable IDs, old-world impact, replacements,
migration or obsoletion data, and release notes.

### Modmods

A Mod that changes another bundled Mod must still create a purposeful distinct experience, have a
maintainer, and validate the dependency combination. A small preference patch is not automatically
eligible. Use current `modinfo.json` and UI registrations for categories and dependencies instead
of copying a legacy category list.

## History and attribution

Accepted inventory contributors: thaelina. License: CC-BY-SA-3.0. Raw rejected or anomalous contributor values were not imported or published.

The source inventory is frozen at `0378ca2b84303cf614c617c9d9eaa50138cd21ff`; this cross-repository verification uses `d32b9cc880a85480840d82cfa05d256c78a16615`; the aggregate source fingerprint is `975c66966726b069315e72689255c20f76c8c8fdc8ec00981feb775dd4fbfa02`. The [filtered-history experiment](/CCB-Docs/en/migration/filtered-history-experiment/) explains why the whole game repository history is not imported.

## Bodies retained in CCB

- [`doc/IN_REPO_MODS.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/doc/IN_REPO_MODS.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/d32b9cc880a85480840d82cfa05d256c78a16615/doc/IN_REPO_MODS.md)

## Replacement and next step

This page remains Draft until a Responsible human reviews the prose, sources, and replacement relationship. Drafts stay outside production navigation, search, and the AI allowlist.

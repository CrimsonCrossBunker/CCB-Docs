---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: translation-guide
title: 'Legacy migration draft: translation guide'
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
- doc/TRANSLATING.md
- lang/Makefile
- src/translations.cpp
- .github/workflows/build-translations.yml
- .github/workflows/push-translation-template.yml
- src/translation_manager.cpp
- lang/notes/README_all_translators.md
- lang/update_pot.sh
source_symbols:
- TranslationManager::LoadDocuments
source_queries: []
source_fingerprint: 007ab64d80f8144fed21e6e91734d861c684c40ef5a68677e458368084ebe848
authority: docs-explanation
verified_commit: 02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 15c6bbda4cb3fc07419b8c51465e648907e666d010ffd8ad23ed08a9727d33ed
prerequisites: []
depends_on: []
redirect_from: []
supersedes:
- legacy.lang-notes-readme-all-translators
license: CC-BY-SA-3.0
attribution: 'CCB contributors: LunaGlaze, thaelina; accepted inventory identities only. Source paths
  and Git history remain authoritative.'
example_validation_ids: []
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: localization
risk_level: normal
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/568
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/localization/translation-guide/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/localization/translation-guide/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/localization/translation-guide/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/localization/translation-guide/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b
source_urls:
- path: doc/TRANSLATING.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/doc/TRANSLATING.md
- path: lang/Makefile
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/lang/Makefile
- path: src/translations.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/src/translations.cpp
- path: .github/workflows/build-translations.yml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/.github/workflows/build-translations.yml
- path: .github/workflows/push-translation-template.yml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/.github/workflows/push-translation-template.yml
- path: src/translation_manager.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/src/translation_manager.cpp
- path: lang/notes/README_all_translators.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/lang/notes/README_all_translators.md
- path: lang/update_pot.sh
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/lang/update_pot.sh
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28translation-guide%29%3A+&body=Document+ID%3A+translation-guide%0ALanguage%3A+en%0AVerified+commit%3A+02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# Legacy migration draft: translation guide

This is the migration draft page for `translation-guide`. It records **2** frozen inventory record(s), but it does not promote legacy prose into a runtime contract.

- Stable document IDs: `translation-guide, legacy.lang-notes-readme-all-translators`
- Target: `localization/translation-guide.md`
- Replacement: translation-guide
- Archive reason: —

## Inventory records

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| translation-guide | doc/TRANSLATING.md | migrate_rewrite | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |
| legacy.lang-notes-readme-all-translators | lang/notes/README_all_translators.md | merge_into | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | translation-guide |

## Authority boundary

CCB source and tests remain authoritative for runtime behaviour; schemas, declarations, registrations, and generated inventories govern JSON/Lua/API; CI, CMake, Makefile, and Gradle govern builds. This page explains migration state, history, and auditable provenance only. A current contract wins over conflicting legacy prose.

## CCB localization workflow

CCB uses gettext, source extraction, PO files, and compiled MO catalogs. Runtime behavior comes from
`translations.cpp`; JSON extraction comes from scripts under `lang/`; remote synchronization comes
from current translation workflows and the CCB Transifex project. An old `cataclysm-dda` resource
name or forum guide does not override current `.tx/config`.

### Developers

Use `_()` for a simple C++ literal, context for ambiguous text, and plural APIs for quantities. Use
`translation`, `to_translation`, or `pl_translation` for delayed translation, JSON context, and
plurals, then call `translated()` when displaying. Do not cache translated strings during global or
local static initialization; initialization order and runtime language switching will be wrong.
Leave debug/error text exactly copyable unless it is explicitly a player-facing contract.

JSON translator comments use the `//~` and translation-object forms supported by the loader.
Placeholders, positional parameters, markup, gender contexts, key tags, and newlines must remain
equivalent. Do not concatenate sentences that rely on English word order. A new extraction form
requires extractor and test updates.

### Build and validation

The current local MO entry point is:

```sh
make -C lang LANGUAGES=zh_CN
```

Repository scripts also generate POT, validate or merge PO, update statistics, and compile MO; take
exact names from current `lang/` and CI. With a TX token, the build-translations workflow pulls,
discards invalid PO, updates stats, and compiles. Without the token, it reuses a trusted successful
master artifact. After a successful Experimental Release, another workflow generates POT and pushes
the source template to Transifex.

Validate extraction diffs, POT/PO syntax, placeholder/plural/context parity, `msgfmt`, language
switching, fallback, UI width, and target-platform fonts. Do not hand-edit generated MO files.
Transifex writes require maintainer credentials and human review.

## History and attribution

Accepted inventory contributors: LunaGlaze, thaelina. License: CC-BY-SA-3.0. Raw rejected or anomalous contributor values were not imported or published.

The source inventory is frozen at `0378ca2b84303cf614c617c9d9eaa50138cd21ff`; this cross-repository verification uses `02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b`; the aggregate source fingerprint is `007ab64d80f8144fed21e6e91734d861c684c40ef5a68677e458368084ebe848`. The [filtered-history experiment](/CCB-Docs/en/migration/filtered-history-experiment/) explains why the whole game repository history is not imported.

## Bodies retained in CCB

- [`doc/TRANSLATING.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/doc/TRANSLATING.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/doc/TRANSLATING.md)
- [`lang/notes/README_all_translators.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/lang/notes/README_all_translators.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/lang/notes/README_all_translators.md)

## Replacement and next step

This page remains Draft until a Responsible human reviews the prose, sources, and replacement relationship. Drafts stay outside production navigation, search, and the AI allowlist.

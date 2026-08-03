---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: content.manual-of-style
title: 'Legacy migration draft: in game text style'
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
- doc/MANUAL_OF_STYLE.md
- CONTRIBUTING.md
- lang/notes/README_all_translators.md
- tools/check_translation_tags.py
- src/translations.cpp
source_symbols: []
source_queries: []
source_fingerprint: 244ffada6751f7de79152d7deb3184f86a104faacef3d810c098fedb28c99917
authority: docs-explanation
verified_commit: d32b9cc880a85480840d82cfa05d256c78a16615
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: b6377e45455c5c1acadb005b135e4692163c581006f341aeb4c9e714350d556f
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
risk_group: translation
risk_level: normal
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/contributing/in-game-text-style/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/contributing/in-game-text-style/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/contributing/in-game-text-style/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/contributing/in-game-text-style/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/d32b9cc880a85480840d82cfa05d256c78a16615
source_urls:
- path: doc/MANUAL_OF_STYLE.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/doc/MANUAL_OF_STYLE.md
- path: CONTRIBUTING.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/CONTRIBUTING.md
- path: lang/notes/README_all_translators.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/lang/notes/README_all_translators.md
- path: tools/check_translation_tags.py
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/tools/check_translation_tags.py
- path: src/translations.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/src/translations.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28content.manual-of-style%29%3A+&body=Document+ID%3A+content.manual-of-style%0ALanguage%3A+en%0AVerified+commit%3A+d32b9cc880a85480840d82cfa05d256c78a16615%0A%0ADescribe+the+documentation+problem%3A%0A
---

# Legacy migration draft: in game text style

This is the migration draft page for `content.manual-of-style`. It records **1** frozen inventory record(s), but it does not promote legacy prose into a runtime contract.

- Stable document IDs: `content.manual-of-style`
- Target: `contributing/in-game-text-style.md`
- Replacement: https://crimsoncrossbunker.github.io/CCB-Docs/contributing/in-game-text-style/
- Archive reason: —

## Inventory records

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| content.manual-of-style | doc/MANUAL_OF_STYLE.md | migrate_rewrite | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## Authority boundary

CCB source and tests remain authoritative for runtime behaviour; schemas, declarations, registrations, and generated inventories govern JSON/Lua/API; CI, CMake, Makefile, and Gradle govern builds. This page explains migration state, history, and auditable provenance only. A current contract wins over conflicting legacy prose.

## Current in-game text style

This page governs default English source text. Translations follow the target language's
grammar, punctuation, and plural rules. Text must first be clear, localizable, and suitable
for the speaker; mechanical rule-following must not damage meaning.

### Default English

- Use US English for general UI and narration. Deliberately written character dialogue may
  use another dialect.
- Player-facing actions generally use second person. Descriptions use sentence case and end
  with suitable punctuation.
- Follow neighbouring title-case conventions for stats, traits or mutations, scenarios,
  professions, backgrounds, proficiencies, martial arts, and CBMs. Ordinary item and entity
  names are generally lower-case; proper nouns are exceptions.
- Use the serial comma and the Unicode ellipsis `…`, not three periods.
- Keep dialogue checks consistent, such as `[PER 10]`, `[Tailoring 2]`, `[SWEET TOOTH]`,
  and `[Use Stethoscope]`. A non-dialogue action still needs a clear label.

### Localizability

- Do not concatenate sentences that depend on English word order. Give identical English
  with different meanings a translation context.
- Use plural APIs for quantities instead of English-only singular/plural branches.
- Preserve and verify `%s`, `%d`, positional arguments, format braces, colour or markup
  tags, and newlines.
- Do not require translations to copy English capitalization, double spacing, serial commas,
  or sentence structure.
- Explain variables, IDs, key tokens, and non-translatable markers in translator comments.

### Names, brands, and provenance

Real brands and references still have to satisfy project lore, licensing, and content
policy; a possible fair-use argument is not automatic approval. For disputed external text,
images, or names, provide provenance and licensing in the PR for the Responsible human and
maintainers to review. Do not copy prose from an incompatible project.

### Validation

Check extraction, translation tags, placeholder parity, invalid PO handling, and MO
compilation. When JSON, C++, EOC, or Lua produces the text, also verify UI width, plurals,
gender or context, and error paths instead of reviewing only the source string.

See the [translation guide](../localization/translation-guide.md).

## History and attribution

Accepted inventory contributors: thaelina. License: CC-BY-SA-3.0. Raw rejected or anomalous contributor values were not imported or published.

The source inventory is frozen at `0378ca2b84303cf614c617c9d9eaa50138cd21ff`; this cross-repository verification uses `d32b9cc880a85480840d82cfa05d256c78a16615`; the aggregate source fingerprint is `244ffada6751f7de79152d7deb3184f86a104faacef3d810c098fedb28c99917`. The [filtered-history experiment](/CCB-Docs/en/migration/filtered-history-experiment/) explains why the whole game repository history is not imported.

## Bodies retained in CCB

- [`doc/MANUAL_OF_STYLE.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/doc/MANUAL_OF_STYLE.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/d32b9cc880a85480840d82cfa05d256c78a16615/doc/MANUAL_OF_STYLE.md)

## Replacement and next step

This page remains Draft until a Responsible human reviews the prose, sources, and replacement relationship. Drafts stay outside production navigation, search, and the AI allowlist.

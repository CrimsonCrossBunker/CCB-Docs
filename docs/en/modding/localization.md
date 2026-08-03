---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: mod-localization
title: 'Legacy migration draft: localization'
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
- doc/TRANSLATING_MOD.md
- lang/extract_json_strings.py
- lang/string_extractor/parsers/mod_info.py
- src/translations.cpp
source_symbols: []
source_queries: []
source_fingerprint: f8453df6b1f08b138e9ebb0f9a0cb63166baaa2c3d1d5a209db8ddea561bfaee
authority: docs-explanation
verified_commit: c1b0f95c6d1b074fc49ee2a7976819c124b69047
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 5bbc6401b91fa11bb81657cbd5c2781826b25331838af3f55b8d7e23d0ee1d50
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
risk_group: localization
risk_level: normal
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/modding/localization/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/modding/localization/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/modding/localization/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/modding/localization/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/c1b0f95c6d1b074fc49ee2a7976819c124b69047
source_urls:
- path: doc/TRANSLATING_MOD.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/TRANSLATING_MOD.md
- path: lang/extract_json_strings.py
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/lang/extract_json_strings.py
- path: lang/string_extractor/parsers/mod_info.py
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/lang/string_extractor/parsers/mod_info.py
- path: src/translations.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/src/translations.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28mod-localization%29%3A+&body=Document+ID%3A+mod-localization%0ALanguage%3A+en%0AVerified+commit%3A+c1b0f95c6d1b074fc49ee2a7976819c124b69047%0A%0ADescribe+the+documentation+problem%3A%0A
---

# Legacy migration draft: localization

This is the migration draft page for `mod-localization`. It records **1** frozen inventory record(s), but it does not promote legacy prose into a runtime contract.

- Stable document IDs: `mod-localization`
- Target: `modding/localization.md`
- Replacement: mod-localization
- Archive reason: —

## Inventory records

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| mod-localization | doc/TRANSLATING_MOD.md | merge_into | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | mod-localization |

## Authority boundary

CCB source and tests remain authoritative for runtime behaviour; schemas, declarations, registrations, and generated inventories govern JSON/Lua/API; CI, CMake, Makefile, and Gradle govern builds. This page explains migration state, history, and auditable provenance only. A current contract wins over conflicting legacy prose.

## Mod localization workflow

Translatable CCB JSON fields are defined by `lang/string_extractor` rules; an arbitrary string is
not extracted automatically. Use structured translation objects, plurals, and context first, then
generate a POT. Do not concatenate runtime sentences that depend on English word order.

### Extract a template

From the CCB root, create an empty reference POT for an external Mod at `mods/demo`, then invoke the
current script:

```sh
mkdir -p mods/demo/lang/po
: > mods/demo/lang/po/demo.pot
python3 lang/extract_json_strings.py -i mods/demo -n demo -r mods/demo/lang/po/demo.pot
msgfmt -c -o /dev/null mods/demo/lang/po/demo.pot
```

The current script appends to and sanitizes `-r/--reference`; it has no legacy `-o` output option.
Regenerate and review the diff after a JSON field, ID, context, or plural changes. If an expected
string is absent, inspect the object type and extractor rule instead of hand-authoring a msgid that
can drift from source.

### Create PO files and translate

```sh
msginit -i mods/demo/lang/po/demo.pot -o mods/demo/lang/po/zh_CN.po -l zh_CN
```

Translations must preserve printf or fmt placeholders, positional arguments, color and markup
tags, newlines, gender or context, and plural meaning. Translator comments should explain
variables, non-translatable IDs, and UI constraints. Do not require another language to copy
English capitalization, word order, or plural rules. Use the gettext merge workflow when updating
the template so existing PO work is not overwritten.

### Compile and install

```sh
mkdir -p mods/demo/lang/mo/zh_CN/LC_MESSAGES
msgfmt -c -o mods/demo/lang/mo/zh_CN/LC_MESSAGES/demo.mo mods/demo/lang/po/zh_CN.po
```

The current translation manager recursively discovers `LC_MESSAGES` under the user Mod root and
reads `.mo` files there. The language directory must match the language code selected by the game.
A release needs the required `.mo` files and Mod content. Whether it also distributes POT and PO
sources is a collaboration and licensing choice, but maintainable source must be retained.

### Validation

Run `msgfmt -c` on the POT and every PO, then check extraction diffs, placeholder and tag parity,
and invalid Unicode. Install the Mod in the real user Mod directory and start the game in English
and the target language. Check the Mod name and description, item plurals, dialogue, EOC messages,
and Lua UI text. Also verify safe source-text fallback when the target translation is absent and
use context wherever identical msgids have different meanings.

## History and attribution

Accepted inventory contributors: thaelina. License: CC-BY-SA-3.0. Raw rejected or anomalous contributor values were not imported or published.

The source inventory is frozen at `0378ca2b84303cf614c617c9d9eaa50138cd21ff`; this cross-repository verification uses `c1b0f95c6d1b074fc49ee2a7976819c124b69047`; the aggregate source fingerprint is `f8453df6b1f08b138e9ebb0f9a0cb63166baaa2c3d1d5a209db8ddea561bfaee`. The [filtered-history experiment](/CCB-Docs/en/migration/filtered-history-experiment/) explains why the whole game repository history is not imported.

## Bodies retained in CCB

- [`doc/TRANSLATING_MOD.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/TRANSLATING_MOD.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/TRANSLATING_MOD.md)

## Replacement and next step

This page remains Draft until a Responsible human reviews the prose, sources, and replacement relationship. Drafts stay outside production navigation, search, and the AI allowlist.

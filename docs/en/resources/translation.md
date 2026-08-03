---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: resources.translation
title: Translation workflow
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
last_human_reviewer: Pending human review
source_paths:
- doc/TRANSLATING.md
- .github/workflows/build-translations.yml
- lang/Makefile
- src/translations.h
source_symbols:
- void set_language( const std::string &lang );
source_queries:
- Build translations
source_fingerprint: e65370a18ee8854c2a3abf3f9b573f592a8412883f9e1822e17ca6c5eb589aa6
authority: build-config
verified_commit: d32b9cc880a85480840d82cfa05d256c78a16615
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 0dcd4aa5a5b6b21e0a16bb655b6b37c976bb11b76c00a5b867d211cc459ee31b
prerequisites:
- cpp.localization
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: CCB contributors; see source paths and Git history.
example_validation_ids:
- cpp-tests
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: localization
risk_level: high
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/resources/translation/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/resources/translation/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/resources/translation/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/resources/translation/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/d32b9cc880a85480840d82cfa05d256c78a16615
source_urls:
- path: doc/TRANSLATING.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/doc/TRANSLATING.md
- path: .github/workflows/build-translations.yml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/.github/workflows/build-translations.yml
- path: lang/Makefile
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/lang/Makefile
- path: src/translations.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/src/translations.h
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28resources.translation%29%3A+&body=Document+ID%3A+resources.translation%0ALanguage%3A+en%0AVerified+commit%3A+d32b9cc880a85480840d82cfa05d256c78a16615%0A%0ADescribe+the+documentation+problem%3A%0A
---

# Translation workflow

This page covers production translation assets. Runtime localization semantics are documented
separately; the build files and translation workflow are authoritative here.

## Source-to-runtime pipeline

1. C++ strings use the translation helpers; supported JSON types use `translation` fields.
2. `lang/update_pot.sh` and the JSON extractor build the source template.
3. Translators work in the configured CCB Transifex project.
4. `.github/workflows/build-translations.yml` pulls PO files, rejects invalid entries, updates
   statistics, compiles MO files, and publishes a translation artifact.
5. platform builds consume that artifact; `src/translations.*` selects and caches a language.

## Contributor rules

Use context for ambiguous English and plural helpers for counted messages. Keep placeholders,
markup tokens, newlines, and semantic context stable. Do not hand-edit files explicitly marked
as generated or replace CCB project identity with an upstream resource name.

## Local checks

The repository's focused compilation entry is:

```sh
make -C lang -j2
```

Extraction and full catalog refresh can touch many files and external translation state; run
the exact workflow required by the change, review the resulting PO/POT diff, and do not claim a
Transifex pull occurred without credentials and logs.

## Validation

Check extraction, invalid PO handling, MO compilation, placeholder parity, plural/context
behavior, a localized build, and representative UI at narrow width. Android resource strings
and Lua i18n are additional pipelines and need their own validation when changed.

## Attribution and maintenance

Preserve translator credits and source provenance. Translation service credentials remain in
repository secrets. A failed external pull must not be hidden by publishing empty or stale
artifacts; trusted default-branch artifact reuse must remain explicit in CI logs.

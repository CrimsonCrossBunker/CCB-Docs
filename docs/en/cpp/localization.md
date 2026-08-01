---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: cpp.localization
title: Localization runtime
language: en
status: draft
doc_type: reference
audiences:
- experienced-contributor
- maintainer
- mod-author
owners:
- CCB maintainers
reviewers:
- Documentation reviewers
review_interval_days: 120
last_human_reviewer: Pending human review
source_paths:
- src/translations.h
- src/translations.cpp
- src/translation_plural_evaluator.cpp
- tests/translations_test.cpp
- tests/translation_system_test.cpp
source_symbols:
- void set_language( const std::string &lang );
source_queries: []
source_fingerprint: 043f9ef3b03bd2c77c7d33fbc3aede4ec1dbf507413a97c4c2d5f47c2c942acd
authority: source-and-tests
verified_commit: dbaedf8357408ae6f96309732d6e087e9b878e18
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: fbd5ad76270949591110b94bf2403fdedfc905c7fb3bf3f203be6d1583ad0a92
prerequisites:
- architecture.overview
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
risk_level: normal
pending_source_pr: null
stale_reason: null
search:
  exclude: true
---

# Localization runtime

## Responsibility

The localization runtime selects a language, loads catalogs, translates singular/plural and
contextual messages, invalidates translation caches on language changes, provides typed format
helpers, and supports translation-valued JSON data.

## Entry points

Read `src/translations.h`, `src/translations.cpp`, the `translation` type, plural evaluator, and
translation manager. Use `_` for runtime strings, contextual/plural helpers where required, and
`translate_marker` only for extraction without runtime translation.

## Data ownership

Translation catalogs and manager caches own localized lookup state. Source code and JSON own
stable English message IDs/context; UI callers own the formatted result. Cached translated
strings must respect the language-generation counter.

## Dependencies

Localization depends on gettext catalogs, locale/path discovery, extraction scripts, JSON
translation objects, plural rules, `fmt` type checking, options, fonts, and UI layout.

## Lifecycle

Source messages are extracted to POT, translated into PO, compiled to MO, loaded for the chosen
language, cached on use, and invalidated when `set_language` changes the generation.

## Invariants

Message/context/plural keys remain stable; placeholders agree across translations; format
arguments are type-correct; marker-only strings are translated before display; and a language
switch cannot return a previous-language cache entry.

## Extension points

Mark new user-facing strings with the appropriate helper and add translator context where the
English is ambiguous. Add plural/context APIs centrally, not via manual string concatenation.

## Serialization

Save stable IDs or source-language values required by the owning contract, not rendered text.
Language choice is user configuration; runtime translation caches are reconstructed.

## Tests

Use translation-system and translations tests plus extraction/build checks. Cover context,
plural counts, format placeholders, language cache invalidation, JSON translation values, and
both localized/non-localized builds.

## Performance

Translation occurs throughout rendering. Preserve local caches and generation invalidation,
avoid repeated formatting in loops, and never cache across a language change without a token.

## CCB divergence

CCB has its own messages, project name, Lua UI strings, Android resources, and translation
catalog. Upstream translations cannot replace or overwrite CCB-specific context.

## Technical debt

Gettext macros, typed `translation`, JSON forms, Android resources, and Lua i18n coexist. Keep
their extraction and invalidation boundaries documented and tested.

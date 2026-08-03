---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: architecture.design-principles
title: Design principles
language: en
status: active
doc_type: explanation
audiences:
- experienced-contributor
- maintainer
- mod-author
owners:
- CCB maintainers
reviewers:
- Documentation reviewers
review_interval_days: 180
last_human_reviewer: LYHGLYTX
source_paths:
- CONTRIBUTING.md
- doc/design-balance-lore/design-doc.md
- doc/design-balance-lore/design-gameplay.md
- doc/design-balance-lore/design-user-experience.md
source_symbols: []
source_queries: []
source_fingerprint: 5da90a32b5e4f26ca60b5ca3ea00782926f74b1f31dd60a1c900e01bf75d7c8d
authority: docs-explanation
verified_commit: 2c899a3db790e11a6ff44d91f319064b1ee65d2a
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 746d83cab18a1c2f87fc345bf1ee403dc978ed942e1ddac84eb77e15ef72df85
prerequisites:
- architecture.overview
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: CCB contributors; see source paths and Git history.
example_validation_ids: []
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: design
risk_level: normal
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/560
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/architecture/design-principles/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/architecture/design-principles/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/architecture/design-principles/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/architecture/design-principles/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/2c899a3db790e11a6ff44d91f319064b1ee65d2a
source_urls:
- path: CONTRIBUTING.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/2c899a3db790e11a6ff44d91f319064b1ee65d2a/CONTRIBUTING.md
- path: doc/design-balance-lore/design-doc.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/2c899a3db790e11a6ff44d91f319064b1ee65d2a/doc/design-balance-lore/design-doc.md
- path: doc/design-balance-lore/design-gameplay.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/2c899a3db790e11a6ff44d91f319064b1ee65d2a/doc/design-balance-lore/design-gameplay.md
- path: doc/design-balance-lore/design-user-experience.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/2c899a3db790e11a6ff44d91f319064b1ee65d2a/doc/design-balance-lore/design-user-experience.md
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28architecture.design-principles%29%3A+&body=Document+ID%3A+architecture.design-principles%0ALanguage%3A+en%0AVerified+commit%3A+2c899a3db790e11a6ff44d91f319064b1ee65d2a%0A%0ADescribe+the+documentation+problem%3A%0A
---

# Design principles

CCB design decisions are constrained by observable behaviour, compatibility,
maintainability, and the project's own direction. Historical design documents
provide context; current CCB source, tests, governance, and maintainer decisions
determine what applies now.

## Evaluate a proposal

1. State the player or contributor problem without prescribing an
   implementation.
2. Define observable success, non-goals, affected audiences, and failure modes.
3. Check whether JSON, EOC, or the supported Lua API can express the change
   before adding engine complexity.
4. Identify ownership, lifecycle, invariants, serialization, performance hot
   paths, UI/accessibility, localization, and platform effects.
5. Compare shared upstream behaviour with intentional CCB divergence.
6. Prefer a reversible, testable increment with clear compatibility policy.

## Data-driven without hiding semantics

Moving behaviour into data is useful only when the loader validates it, errors
are actionable, and authors can understand the lifecycle. A flexible JSON or
Lua surface still needs documented constraints and tests. Do not publish an
unstable internal hook as a public extension point merely to avoid a C++ change.

## Balance and content

Mechanics and balance proposals need examples, affected scenarios, and a way to
measure the intended result. Avoid broad unrelated rebalance in a technical fix.
Respect project lore and content policy, but flag historical upstream guidance
that has not been confirmed for CCB rather than presenting it as current law.

The final decision belongs in an issue or reviewed pull request so rationale,
trade-offs, and Responsible human remain auditable.

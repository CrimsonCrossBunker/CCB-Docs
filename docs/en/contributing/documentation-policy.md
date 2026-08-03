---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: contributing.documentation-policy
title: Documentation policy
language: en
status: active
doc_type: explanation
audiences:
- new-contributor
- experienced-contributor
- maintainer
owners:
- CCB maintainers
reviewers:
- Documentation reviewers
review_interval_days: 90
last_human_reviewer: LYHGLYTX
source_paths:
- AGENTS.md
- GOVERNANCE.md
- ai/docs-impact.yml
- ai/generated-files.yml
- doc/migration/markdown-inventory.schema.json
source_symbols: []
source_queries: []
source_fingerprint: 93b17cddf4342473acfcd97b3f379812e6fb70fc5f3ecda9a92f7ee6290dd68c
authority: governance
verified_commit: d32b9cc880a85480840d82cfa05d256c78a16615
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: ee1276aca890ccb3f8a63b9de838456c4891374680e5cf75988966a1a860b78e
prerequisites:
- home
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: CCB contributors; see source paths and Git history.
example_validation_ids:
- agent-context
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: documentation-policy
risk_level: high
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/contributing/documentation-policy/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/contributing/documentation-policy/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/contributing/documentation-policy/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/contributing/documentation-policy/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/d32b9cc880a85480840d82cfa05d256c78a16615
source_urls:
- path: AGENTS.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/AGENTS.md
- path: GOVERNANCE.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/GOVERNANCE.md
- path: ai/docs-impact.yml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/ai/docs-impact.yml
- path: ai/generated-files.yml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/ai/generated-files.yml
- path: doc/migration/markdown-inventory.schema.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/doc/migration/markdown-inventory.schema.json
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28contributing.documentation-policy%29%3A+&body=Document+ID%3A+contributing.documentation-policy%0ALanguage%3A+en%0AVerified+commit%3A+d32b9cc880a85480840d82cfa05d256c78a16615%0A%0ADescribe+the+documentation+problem%3A%0A
---

# Documentation policy

CCB-Docs is the formal tutorial, explanation, architecture, reference, and
navigation site. It does not share authority equally with the game repository.

## Authority model

| Subject | Authority |
| --- | --- |
| Runtime behaviour | CCB source and tests |
| JSON, Lua, and API contracts | Schemas, LuaLS declarations, registrations, generated inventories |
| Build and validation | CI, CMake, Makefile, Gradle, repository validators |
| Contribution and governance | CCB `AGENTS.md`, `CONTRIBUTING.md`, `GOVERNANCE.md` |
| Explanation and navigation | CCB-Docs, checked against the sources above |

If prose conflicts with its source contract, mark the page stale, exclude it
from the AI index, and repair it. Do not change runtime behaviour merely to
match documentation.

## Bilingual publication

New active pages publish with both Chinese and English. After a Chinese update,
English may be `translation-stale` for at most 30 days and gets a tracking
issue. An overdue translation blocks only a PR changing that pair or the same
high-risk documentation subsystem; unrelated fixes remain mergeable. An
incomplete migrated pair stays draft and out of production navigation, search,
and AI indexes.

## Source drift and generated content

Every page declares exact `source_paths`, a verified commit and date, and a
fingerprint. Drift is scoped to those paths; an arbitrary `master` commit does
not make every page stale. No actual change means no bot PR. Drift updates are
aggregated, stay human-reviewed, and are never auto-merged.

`docs-catalog.yml` is the sole hand-maintained machine catalog. It generates
navigation, bilingual mappings, search/AI/archive policy, redirects, sitemap
metadata, `llms.txt`, and JSON indexes. Edit the catalog or generator, never a
derived index.

## Legacy paths

A migrated repository path permanently retains a lightweight bilingual moved
stub. The old body may be removed after six months, but historical PRs, issues,
forks, and external links must continue to reach the stable document ID and
both current language URLs.

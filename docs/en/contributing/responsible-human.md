---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: contributing.responsible-human
title: Responsible human and AI-assisted contributions
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
- CONTRIBUTING.md
- GOVERNANCE.md
- .github/pull_request_template.md
source_symbols: []
source_queries:
- Responsible human
source_fingerprint: 92bbc1c991b6ad674114072e80aa45f9cc05cb3bf47bc24c8b2dc4ab2dd10695
authority: governance
verified_commit: 9d8f26582da0f53ca1e29f8f072aeef43955655b
verified_at: '2026-08-01'
generated: false
generated_by: null
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 55d3f928cb2ca6ab24791556f0c374de51d4aa25e240accb35f181120453be7a
prerequisites: []
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
risk_group: governance
risk_level: high
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/contributing/responsible-human/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/contributing/responsible-human/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/contributing/responsible-human/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/contributing/responsible-human/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/9d8f26582da0f53ca1e29f8f072aeef43955655b
source_urls:
- path: CONTRIBUTING.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/9d8f26582da0f53ca1e29f8f072aeef43955655b/CONTRIBUTING.md
- path: GOVERNANCE.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/9d8f26582da0f53ca1e29f8f072aeef43955655b/GOVERNANCE.md
- path: .github/pull_request_template.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/9d8f26582da0f53ca1e29f8f072aeef43955655b/.github/pull_request_template.md
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28contributing.responsible-human%29%3A+&body=Document+ID%3A+contributing.responsible-human%0ALanguage%3A+en%0AVerified+commit%3A+9d8f26582da0f53ca1e29f8f072aeef43955655b%0A%0ADescribe+the+documentation+problem%3A%0A
---

# Responsible human

CCB permits AI assistance and pull requests opened by automation. Contributors
do not have to publish the tool, model, complete prompt, or conversation, but
every pull request must name a real Responsible human.

## Responsibilities

The Responsible human must:

- understand the purpose, implementation, and impact boundary;
- review the final diff, not only the generation process or summary;
- own the test results reported in the pull request;
- verify licenses and attribution for copied, adapted, or ported material;
- record verifiable external sources;
- answer review questions and follow the pull request through merge or closure.

AI output does not prove correctness and does not erase upstream licenses or
authorship. If the change cannot be explained or its validation reproduced,
investigate further rather than delegating responsibility to the tool.

## Review and merge

The target governance requires a non-author human approval, but maintainers
must first confirm at least two active human reviewers with permission and a
successful default-branch run for each required check. Until then, keep the
target configuration documented rather than enabling protection that could
make the repository impossible to merge.

Bot-created drift pull requests are never auto-merged. A docs pull request must
also be refreshed to the final source commit and revalidated after its source
pull request merges.

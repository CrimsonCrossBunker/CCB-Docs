---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: contributing.responsible-human
title: Responsible human
language: en
status: active
source_paths:
- CONTRIBUTING.md
- GOVERNANCE.md
- .github/pull_request_template.md
authority: governance
verified_commit: 9d8f26582da0f53ca1e29f8f072aeef43955655b
verified_at: '2026-08-01'
generated: false
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
risk_group: governance
risk_level: high
pending_source_pr: null
stale_reason: null
doc_type: explanation
audiences:
- new-contributor
- experienced-contributor
- maintainer
- agent
owners: []
reviewers: []
review_interval_days: 90
last_human_reviewer: LYHGLYTX
source_symbols: []
source_queries: []
source_fingerprint: bfca58bb5bcc4d08fb7a11f3dfbbc87a0b2335ca46ffd1aaa5547d0bbc0e66f4
translation_source_fingerprint: 55d3f928cb2ca6ab24791556f0c374de51d4aa25e240accb35f181120453be7a
prerequisites:
- home
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: CCB and CCB-Docs contributors; see source and page history
generated_by: null
example_validation_ids: []
api_version: null
deprecated: false
deprecation_replacement: null
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

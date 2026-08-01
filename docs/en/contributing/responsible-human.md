---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: contributing.responsible-human
title: Responsible human
language: en
status: draft
source_paths:
- CONTRIBUTING.md
- GOVERNANCE.md
- .github/pull_request_template.md
authority: governance
verified_commit: 11748581a0df8651380cfb8ae37ae91baafe054d
verified_at: '2026-08-01'
generated: false
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
risk_group: governance
risk_level: high
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/551
stale_reason: null
search:
  exclude: true
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

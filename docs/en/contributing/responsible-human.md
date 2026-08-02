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
source_fingerprint: 781981c55ef754b0836ca4b065bb6a7b9a85a6daf0e4bca4782240c25caa7a2c
authority: governance
verified_commit: 4e3b9aa99ae59630abf60f717bdaf563b2d63245
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 37cb310dd6b29be8649a2309df51a39a284341ceb5eb24b1245fa2482694785d
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
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/4e3b9aa99ae59630abf60f717bdaf563b2d63245
source_urls:
- path: CONTRIBUTING.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/CONTRIBUTING.md
- path: GOVERNANCE.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/GOVERNANCE.md
- path: .github/pull_request_template.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/.github/pull_request_template.md
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28contributing.responsible-human%29%3A+&body=Document+ID%3A+contributing.responsible-human%0ALanguage%3A+en%0AVerified+commit%3A+4e3b9aa99ae59630abf60f717bdaf563b2d63245%0A%0ADescribe+the+documentation+problem%3A%0A
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

One Responsible human is sufficient for CCB. `LYHGLYTX` is the currently
confirmed maintainer. A pull request authored by that maintainer does not need
a separate GitHub approval, so the target Ruleset keeps the required approval
count at zero and does not require approval from someone other than the last
pusher. Bots cannot replace the Responsible human or approve their own work.

Pull requests, required checks, resolved review conversations, and the bans on
force-pushes and branch deletion remain target protections. Enable them only
after the named checks are stable on the default branch and the administrator
steps are complete. Automated merging remains disabled.

Bot-created drift pull requests are never auto-merged. A docs pull request must
also be refreshed to the final source commit and revalidated after its source
pull request merges.

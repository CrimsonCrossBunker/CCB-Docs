## Current issue-triage workflow

Triage turns reports into actionable work; its purpose is not to close issues quickly.
Confirm the repository and version, then distinguish defects, features, mechanics or
balance, JSON content, performance, documentation, and upstream sync. Current Issue Forms,
`ISSUES.md`, `LABELS.md`, and governance policy define the categories.

### First pass

1. Search open and closed CCB issues for duplicates and newer evidence.
2. Record the exact CCB commit or release, platform, build type, SDL backend, Mod list, and
   save origin.
3. Check reproduction steps, expected and actual results, logs, and a minimal example. Ask
   one specific, answerable question when evidence is missing.
4. Identify vulnerabilities, credentials, or private data and route them through the private
   process in `SECURITY.md`.
5. Apply subsystem, confirmation, and priority labels only when evidence supports them.
   Labels do not promise a schedule.

### Risk order

- crashes, save or map data loss, irreversible compatibility breakage, and security issues
  come first;
- player item or character loss, severe regressions, and blocking UI problems follow;
- ordinary defects, performance, and usability are ranked by impact and reproducibility;
- a small content request or unexplained number change is not automatically a confirmed bug.

Behaviour that matches current design but is undesirable is normally a feature or balance
proposal. Behaviour that violates a current contract or design is a bug. Record uncertainty
instead of replacing source, tests, or design policy with a personal expectation.

### Reproduction, closure, and reopening

A triager may reproduce a report, but does not owe a complete debugging session for every
issue. After a reasonable information request, an issue without reproducible evidence may
be closed with an explanation. Duplicate, out-of-scope, superseded, or rejected outcomes
also need a clear reason. New logs, a minimal save, or reproduction on a new version are
reasonable grounds to reopen.

### Hand off to implementation

An implementer should comment with intended scope and open a Draft PR. The PR links the
issue, names a Responsible human, and records validation and documentation impact. Do not
invent an owner, CODEOWNERS entry, or review team while triaging.

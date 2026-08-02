## This is not a live feature-status table

The legacy “frequently made suggestions” page mixed years of feature status, personal opinion,
upstream links, and specific numbers. Its answers only describe discussion at the time; they do not
prove that CCB currently implements, is developing, rejects, or permits something only in a mod.
Reconfirm status in current source, Issues, pull requests, roadmaps, and maintainer decisions.
`GOVERNANCE.md`, not old descriptions of individuals or hostile wording, governs the project.

## Quick check before proposing something

1. Search current CCB Issues, pull requests, source registrations, and CCB-Docs to confirm that the
   problem remains and no implementation is already in progress.
2. Describe the player need and a reproducible scenario instead of supplying only a feature name or
   asking for a vote.
3. Explain interaction with setting, design principles, platforms, performance, saves, and mod
   compatibility.
4. Compare smaller approaches: can existing EOC, JSON, or Lua express it; is it suitable for a
   first- or third-party mod; does it require new runtime capability?
5. List maintenance cost, including UI, localization, test matrix, data migration, generated
   content, and a long-term owner.
6. If you intend to implement it, open a scoped design Issue first, then prepare the smallest PR and
   validation evidence after receiving direction feedback.

## Recurring decision principles

- One existing exception does not prove another should be added; old content may itself need repair.
- Real-world feasibility does not prove that one post-Cataclysm character can perform a task with
  available tools, knowledge, time, and acceptable risk.
- An option is not free: every branch expands code, documentation, localization, compatibility, and
  testing obligations.
- A content suggestion is often strongest as a working JSON or mod prototype, but the prototype
  still needs compatible licensing, provenance, and project fit.
- Technical difficulty is not permanent rejection, and desire is not a roadmap promise. Record
  dependencies, the current gap, and a verifiable next step.

When an answer affects project policy or many players, current maintainers decide through a
reviewable Issue or pull request. The page should link that decision and applicable commit and
become stale when its sources change instead of freezing one conversation forever.

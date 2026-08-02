## Current PR review checklist

Review establishes that a change solves the stated problem and agrees with CCB contracts,
compatibility policy, and maintenance policy. The legacy guide's fixed line thresholds and
upstream people or Discord roles are not CCB's permission model. Size is a review-risk
signal, not a merge rule.

### Read the scope first

- Does the description explain the problem, solution, alternatives, actual tests, and
  residual risk?
- Does the diff contain only work needed for the outcome, without unrelated formatting,
  refactors, generated output, or local files?
- Are commits and stacked PRs split by dependency with an exact merge order?
- Does the Responsible human understand the final diff instead of merely supplying a name?

### Compare authoritative sources

1. Check runtime claims against source and tests.
2. Check JSON, Lua, and API claims against Schemas, LuaLS, registrations, and generated
   inventories.
3. Check build commands against CI, CMake, Makefile, Gradle, and repository validators.
4. Check contribution and governance claims against `AGENTS.md`, `CONTRIBUTING.md`, and
   `GOVERNANCE.md`.
5. If CCB-Docs conflicts, mark and repair stale prose; prose does not override a contract.

### Review risk

- Do save serialization, stable IDs, Mod/Lua APIs, Android/desktop differences, and upstream
  divergence have migrations or compatibility plans?
- Is gameplay or balance supported by reviewable reasoning and sources?
- Are external code, data, images, sound, or text license-compatible and attributed?
- Did a generator update generated files, and is the generated diff stable?
- Are documentation IDs, the related CCB-Docs PR, and generated-reference impact complete?

### Validation evidence

Run the narrowest test that can demonstrate the failure first. Distinguish an actual pass,
not run, an environment blocker, and a flaky or master failure unrelated to the diff. Do not
change assertions merely because CI is red, and do not call a failure unrelated without logs.

### Approval and merge boundary

A Bot cannot approve its own PR and PRs are not auto-merged. Before requiring non-author
approval, confirm at least two active, willing, permissioned human reviewers. A permissioned
human decides whether to merge only after conversations, Draft state, stack dependencies,
and final source pins are resolved.

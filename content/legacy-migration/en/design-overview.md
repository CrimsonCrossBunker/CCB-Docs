## How to use design documentation

Design documentation explains why CCB favors a kind of experience, which questions a proposal must
answer, and which tradeoffs matter when systems conflict. It does not replace runtime, data-format,
or governance authorities. Source and tests define concrete behavior; schemas, declarations,
registrations, and generated inventories define JSON, Lua, and API contracts; current governance
files define project decisions.

### Minimum proposal structure

1. **Problem:** describe the current player experience and a reproducible scenario before assuming
   a solution.
2. **Goals and non-goals:** state the desired outcome and the boundaries that will not change.
3. **Current state:** list entry points, data ownership, lifecycle, tests, and CCB differences from
   upstream.
4. **Approach and alternatives:** compare player visibility, complexity, performance,
   maintainability, and compatibility.
5. **Migration risk:** inspect saves, mods, IDs, serialization, localization, platforms, and
   generated content.
6. **Acceptance:** provide runnable commands, scenarios, and rollback conditions.

## Decision boundaries

Numbers, file paths, people, and unimplemented mechanics in legacy design prose are historical
context only. Revalidate them against the current default branch before carrying them into a new
proposal. Resolve conflicting directions through Issues, pull requests, and the current maintainer
governance process. No old statement by one person permanently overrides repository governance.

## CCB and upstream

Upstream material can explain shared history and portable approaches, but CCB has its own runtime
differences, content direction, compatibility requirements, and governance. A proposal should name
the source revision, compare both current implementations, and port only what still applies to CCB.
If prose conflicts with a current contract, mark the page stale and repair the documentation rather
than changing the implementation to fit an obsolete explanation.

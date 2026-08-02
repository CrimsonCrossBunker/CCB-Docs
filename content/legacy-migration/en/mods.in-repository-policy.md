## CCB in-repository Mod policy

Shipping a Mod with the game improves visibility, shared Issue and PR handling, and continuous
load checks. It also assigns compatibility, release, and security cost to the whole project.
Admission to `data/mods/` is not a promise of permanent inclusion, core-team maintenance, or
exclusive author control. An in-repository Mod remains community-contributed project content.

### Admission criteria

A proposal needs a clear purpose that can be reviewed over time: a distinct content experience,
an accessibility or interface capability, or isolation for an optional feature still under
development. An unrelated object collection, a preference pack that only disables working
features, or a package without maintenance boundaries does not justify repository-wide cost.

Before admission, require at least:

- accurate authors, real GitHub maintainers, category, dependencies, and conflicts in `modinfo.json`;
- auditable provenance, licensing, and permission for third-party assets;
- explicit stable IDs, save policy, dependency boundaries, and CCB/upstream differences;
- passing JSON, EOC, Lua, and complete-Mod loading validation;
- an active curator willing to triage, review, and follow compatibility continuously;
- agreement with dependency maintainers when a new relationship burdens another bundled Mod.

Do not invent `CODEOWNERS` as a substitute for real responsibility. The loader reads and displays
the `maintainers` account set, but a person must still accept the governance responsibility in a
PR or Issue.

### Curator responsibilities

A curator judges whether contributions fit the Mod purpose, reviews or requests changes on its
PRs, and at least acknowledges defects and helps find a repair path. Curators need not author
every fix and cannot exclude community contribution. Their approval is domain input; merge still
follows CCB governance, Responsible-human review, and required checks.

Changes affecting dependants, public IDs, saves, Lua APIs, licensing, or player safety need notice
to affected maintainers and combination-specific evidence. Track balance disagreement separately
from load failure so “it loads” is never mistaken for design approval.

### Orphaning, obsoletion, and removal

Maintainers may begin an orphan or obsolete review when curators are persistently unavailable,
releases repeatedly break, licensing is unclear, the purpose expires, or maintenance cost becomes
unmanageable. Open a public Issue with an owner and deadline first; do not delete a Mod based on one
missed response. `obsolete: true` hides it from new-world selection while retaining old-save
recognition; it is not immediate repository deletion.

Rescue requires a confirmed new curator, repaired blockers, restored validation, and updated
`maintainers`. Before final removal, document stable IDs, old-world impact, replacements,
migration or obsoletion data, and release notes.

### Modmods

A Mod that changes another bundled Mod must still create a purposeful distinct experience, have a
maintainer, and validate the dependency combination. A small preference patch is not automatically
eligible. Use current `modinfo.json` and UI registrations for categories and dependencies instead
of copying a legacy category list.

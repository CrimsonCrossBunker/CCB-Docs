## Select JSON tools by task

Repository tools fall into formatters, loaders or validators, read-only queries, and migration
scripts. Run `-h` first and constrain scope with `git diff --name-only`. Query output is not a
contract, and every changed file from a bulk transform needs review.

### Formatting and loading

```sh
make -j2 tools/format/json_formatter.cgi RELEASE=1
tools/format/json_formatter.cgi path/to/changed.json
make -j2 json-check
```

The project formatter understands CCB's JSON dialect; do not let a generic formatter remove comments
or rewrite the repository. `json-check` validates core loading. A Mod also needs real `--check-mods`
coverage.

### Query keys and values

`tools/json_tools/keys.py` counts fields found on matching objects and `values.py` counts values for
one key. They support `key=value` filters, `--human`, and nested dotted keys.

```sh
tools/json_tools/keys.py --human type=TOOL
tools/json_tools/values.py --key material --human type=TOOL
```

MISSING means a sample omits the member; it does not prove absence of a loader default or that the
field is invalid. Use the registry inventory to locate the handler and source for requiredness.

### Generators and specialized tools

`tools/json_api/generate_contracts.py` owns object and EOC inventories. `copy_from.py`,
`dialogue_validator.py`, and `json_tools/*` apply only to structures described by their help. Before
a rewrite, create a narrow file list, preserve the commit, use a dry run or temporary worktree, then
validate with the owner formatter and loader. Do not sweep third-party, generated, or all `data/` as
a cleanup.

### Auditable output

Record command, input paths or filters, tool commit, changed-file count, and validation in the PR.
Fix the first input error rather than publishing partial statistics. Keep decision reports as CI
artifacts; commit only generated references explicitly named by project metadata.

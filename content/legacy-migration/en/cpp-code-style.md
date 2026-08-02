## Current CCB C++ style entry points

CCB's executable style contract is `.astylerc`, `.clang-tidy`, Makefile targets, and CI, not a
copied legacy list of formatter arguments. Change configuration and CI first when a rule or
tool version changes, then update this explanation. Do not maintain an approximate second rule
set in an editor.

### Minimal pre-commit flow

```sh
make astyle-check
git diff --check
```

`astyle-check` is a read-only gate and is the best first check. To apply automatic corrections:

```sh
make astyle
```

`make astyle` can change managed files outside the lines edited by hand. Inspect
`git diff --name-only` and the full diff afterward and commit only changes belonging to the
task. Formatting is not a reason to hide an unrelated refactor. Follow the repository's
generated and third-party boundaries.

### Readability constraints

- Use current project types, units, point or coordinate types, and ID wrappers instead of
  untyped integers that hide semantics.
- Make ownership and nullability clear; follow existing RAII, container, and smart-pointer patterns.
- Keep lambdas local with explicit captures; extract complex logic into named testable functions.
- Use project APIs for translations, debug messages, and player text while preserving format types.
- Expose only needed header dependencies; include edits need build and clang-tidy or IWYU evidence.
- Do not rename serialized fields, JSON or Lua APIs, or cross-Mod IDs as a style cleanup.

These guide review; the concrete mechanical rules are the current `cata-*` clang-tidy checks
and AStyle output. If an example conflicts with the formatter, update the example instead of
reversing formatter output by hand.

### Change boundaries and generated code

Read the nearest `AGENTS.md` and `ai/generated-files.yml` first. Update generated files through
their owner generator. Edit vendored third-party code only when the task explicitly targets it.
Keep a broad rename, include reorder, or namespace cleanup in a separate commit from a behavior fix.

### Choosing validation

Style success does not prove compilation. Compile at least the affected translation unit. A
public header, template, build flag, or cross-platform path needs the relevant build matrix.
Report only commands that actually ran and distinguish missing local tools, CI evidence, and
checks not run.

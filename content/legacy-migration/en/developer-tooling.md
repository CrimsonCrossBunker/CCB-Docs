## Current CCB developer toolchain

Choose tools by change type; contributors do not need the entire static-analysis stack for every
task. The minimum loop is to locate source and tests, configure a reproducible build, compile
the narrowest target, run focused validation, and inspect the diff. Clang-tidy, IWYU, clangd,
ctags, and profilers are additional layers as needed.

### Compilation database and editors

Generate `compile_commands.json` with a current CMake configuration:

```sh
cmake -S . -B build -DCMAKE_EXPORT_COMPILE_COMMANDS=ON
cmake --build build -j2
```

Match feature flags to the platform or CI job under review. Point clangd to the database in the
build directory. Do not commit `compile_commands.json`, clangd indexes, ctags, Doxygen HTML, or
large symbol databases. Keep them as local caches or CI artifacts.

### Clang-tidy

`.clang-tidy` and `tools/clang-tidy-plugin` define CCB checks. CI is driven by
`.github/workflows/clang-tidy.yml` and `build-scripts/clang-tidy-run.sh`. The script creates a
compilation database, selects directly and transitively affected translation units, and expects
the built Cata plugin.

Even a one-file local check needs the matching database and plugin or wrapper. A bare system
clang-tidy can omit `cata-*` checks. Review each change after an automatic `-fix`; do not accept
cross-file rewrites blindly.

### Include-what-you-use

`.github/workflows/iwyu.yml` and `build-scripts/ci-iwyu-run.py` are the current CI entry points.
The script depends on `files_changed`, affected-file analysis, `tools/iwyu/cata.imp`, and a
blacklist, and explicitly targets CI. For a local run, follow the current example in the script
header and use matching tool and database versions instead of a copied LLVM installation guide.

IWYU suggestions are not automatically correct. Platform wrappers, template instantiation,
associated headers, and keep pragmas have project rules. Recompile affected targets after applying them.

### Formatters, indexes, and generated output

- C++: run `make astyle-check`; after `make astyle`, inspect the complete diff.
- JSON: use the repository formatter, then run loader and ID checks.
- Python: run locked lint and tests only for relevant scripts and tests.
- ctags and Doxygen: use them for navigation, not as API authority, and do not commit output.

Take every command from current CI, CMake, Makefile, and scripts. A legacy fixed LLVM version,
upstream download, or old IDE extension is historical material rather than a CCB requirement.

## CCB localization workflow

CCB uses gettext, source extraction, PO files, and compiled MO catalogs. Runtime behavior comes from
`translations.cpp`; JSON extraction comes from scripts under `lang/`; remote synchronization comes
from current translation workflows and the CCB Transifex project. An old `cataclysm-dda` resource
name or forum guide does not override current `.tx/config`.

### Developers

Use `_()` for a simple C++ literal, context for ambiguous text, and plural APIs for quantities. Use
`translation`, `to_translation`, or `pl_translation` for delayed translation, JSON context, and
plurals, then call `translated()` when displaying. Do not cache translated strings during global or
local static initialization; initialization order and runtime language switching will be wrong.
Leave debug/error text exactly copyable unless it is explicitly a player-facing contract.

JSON translator comments use the `//~` and translation-object forms supported by the loader.
Placeholders, positional parameters, markup, gender contexts, key tags, and newlines must remain
equivalent. Do not concatenate sentences that rely on English word order. A new extraction form
requires extractor and test updates.

### Build and validation

The current local MO entry point is:

```sh
make -C lang LANGUAGES=zh_CN
```

Repository scripts also generate POT, validate or merge PO, update statistics, and compile MO; take
exact names from current `lang/` and CI. With a TX token, the build-translations workflow pulls,
discards invalid PO, updates stats, and compiles. Without the token, it reuses a trusted successful
master artifact. After a successful Experimental Release, another workflow generates POT and pushes
the source template to Transifex.

Validate extraction diffs, POT/PO syntax, placeholder/plural/context parity, `msgfmt`, language
switching, fallback, UI width, and target-platform fonts. Do not hand-edit generated MO files.
Transifex writes require maintainer credentials and human review.

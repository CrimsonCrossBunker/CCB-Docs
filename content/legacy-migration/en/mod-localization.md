## Mod localization workflow

Translatable CCB JSON fields are defined by `lang/string_extractor` rules; an arbitrary string is
not extracted automatically. Use structured translation objects, plurals, and context first, then
generate a POT. Do not concatenate runtime sentences that depend on English word order.

### Extract a template

From the CCB root, create an empty reference POT for an external Mod at `mods/demo`, then invoke the
current script:

```sh
mkdir -p mods/demo/lang/po
: > mods/demo/lang/po/demo.pot
python3 lang/extract_json_strings.py -i mods/demo -n demo -r mods/demo/lang/po/demo.pot
msgfmt -c -o /dev/null mods/demo/lang/po/demo.pot
```

The current script appends to and sanitizes `-r/--reference`; it has no legacy `-o` output option.
Regenerate and review the diff after a JSON field, ID, context, or plural changes. If an expected
string is absent, inspect the object type and extractor rule instead of hand-authoring a msgid that
can drift from source.

### Create PO files and translate

```sh
msginit -i mods/demo/lang/po/demo.pot -o mods/demo/lang/po/zh_CN.po -l zh_CN
```

Translations must preserve printf or fmt placeholders, positional arguments, color and markup
tags, newlines, gender or context, and plural meaning. Translator comments should explain
variables, non-translatable IDs, and UI constraints. Do not require another language to copy
English capitalization, word order, or plural rules. Use the gettext merge workflow when updating
the template so existing PO work is not overwritten.

### Compile and install

```sh
mkdir -p mods/demo/lang/mo/zh_CN/LC_MESSAGES
msgfmt -c -o mods/demo/lang/mo/zh_CN/LC_MESSAGES/demo.mo mods/demo/lang/po/zh_CN.po
```

The current translation manager recursively discovers `LC_MESSAGES` under the user Mod root and
reads `.mo` files there. The language directory must match the language code selected by the game.
A release needs the required `.mo` files and Mod content. Whether it also distributes POT and PO
sources is a collaboration and licensing choice, but maintainable source must be retained.

### Validation

Run `msgfmt -c` on the POT and every PO, then check extraction diffs, placeholder and tag parity,
and invalid Unicode. Install the Mod in the real user Mod directory and start the game in English
and the target language. Check the Mod name and description, item plurals, dialogue, EOC messages,
and Lua UI text. Also verify safe source-text fallback when the target translation is absent and
use context wherever identical msgids have different meanings.

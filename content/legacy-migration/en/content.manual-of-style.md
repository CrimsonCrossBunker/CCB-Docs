## Current in-game text style

This page governs default English source text. Translations follow the target language's
grammar, punctuation, and plural rules. Text must first be clear, localizable, and suitable
for the speaker; mechanical rule-following must not damage meaning.

### Default English

- Use US English for general UI and narration. Deliberately written character dialogue may
  use another dialect.
- Player-facing actions generally use second person. Descriptions use sentence case and end
  with suitable punctuation.
- Follow neighbouring title-case conventions for stats, traits or mutations, scenarios,
  professions, backgrounds, proficiencies, martial arts, and CBMs. Ordinary item and entity
  names are generally lower-case; proper nouns are exceptions.
- Use the serial comma and the Unicode ellipsis `…`, not three periods.
- Keep dialogue checks consistent, such as `[PER 10]`, `[Tailoring 2]`, `[SWEET TOOTH]`,
  and `[Use Stethoscope]`. A non-dialogue action still needs a clear label.

### Localizability

- Do not concatenate sentences that depend on English word order. Give identical English
  with different meanings a translation context.
- Use plural APIs for quantities instead of English-only singular/plural branches.
- Preserve and verify `%s`, `%d`, positional arguments, format braces, colour or markup
  tags, and newlines.
- Do not require translations to copy English capitalization, double spacing, serial commas,
  or sentence structure.
- Explain variables, IDs, key tokens, and non-translatable markers in translator comments.

### Names, brands, and provenance

Real brands and references still have to satisfy project lore, licensing, and content
policy; a possible fair-use argument is not automatic approval. For disputed external text,
images, or names, provide provenance and licensing in the PR for the Responsible human and
maintainers to review. Do not copy prose from an incompatible project.

### Validation

Check extraction, translation tags, placeholder parity, invalid PO handling, and MO
compilation. When JSON, C++, EOC, or Lua produces the text, also verify UI width, plurals,
gender or context, and error paths instead of reviewing only the source string.

See the [translation guide](../localization/translation-guide.md).

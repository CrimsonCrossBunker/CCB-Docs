## ASCII-art data contract

First-party ASCII art uses an `ascii_art` JSON object with at least a stable `id` and a string-array
`picture`. Current `ascii_art::load` removes color tags and measures each line by terminal display
width. A line wider than `41` display columns is trimmed and emits a debug message. A column is not a
UTF-8 byte: wide and combining characters and color tags must be checked through the real loader.

```json
{
  "type": "ascii_art",
  "id": "example_art",
  "picture": [ "<color_white>+---+</color>", "<color_white>|   |</color>" ]
}
```

This example illustrates structure and is not a resource to submit. Use existing valid color names
and close tags correctly. Blank lines, leading spaces, and Unicode box characters are part of the
image; text processing beyond the project JSON formatter can damage alignment. Body-part graphs use
a different data and rendering path, so visual similarity does not prove identical fields or size.

## Creation and review

Any editor that preserves UTF-8, spaces, and line boundaries works. REXPaint is optional tooling,
not a project contract. Confirm provenance and licensing for an external palette, font, template, or
source image instead of importing unknown artwork.

Before submission, run project JSON formatting and loading, check duplicate IDs, invalid color tags,
and debug output, and inspect the real target UI in curses and tiles with default and fallback fonts,
narrow windows, scaling, and both language environments. Measure display width after removing tags,
not only the editor canvas. ASCII art cannot be the sole way to identify an item or body-part state;
an accessible path still needs text or structure.

## CCB user-experience goals

CCB is a top-down, grid-based, action-time-driven open-world survival game with character and tiles
rendering across desktop and Android targets. Its depth should come from interacting world systems
and multiple problem-solving approaches, not from fighting the interface. Games cited by the legacy
page and its “DDA” name are historical background; confirm current product identity, platforms, and
features in CCB README, build configuration, source, and tests.

### Depth must be understandable

- Before a decision consumes time or resources or exposes a character, show the relevant
  information where practical. Afterward, provide feedback that lets the player locate the cause.
- Automate repetition while preserving real choices about route, equipment, risk, priority, and
  retreat.
- Keep actions discoverable, cancellable, and focus-safe with keyboard, touch, narrow windows,
  scaling, and translated text.
- Color, ASCII glyphs, sound, or pointer position cannot be the only semantics. Supply text or
  structure for screen readers, high-contrast users, and play without audio.
- Let players learn complex systems progressively. Defaults show information needed for the current
  task and advanced detail may expand, but contracts should not be permanently hidden.

## Designing a flow

Write down the player goal, entry point, shortest successful path, cancel and failure paths, and save
boundary first. Inspect the input context, activity system, messages, help, options, and
`ui_adaptor` or ImGui lifecycle involved. Do not use a new global option to conceal an unclear
default flow; every option expands the testing and maintenance matrix.

Validate curses and tiles, keyboard and Android touch, resizing, narrow windows, long translations,
color themes, screen-reader mode, interruption and resumption, save/reload, and invalid input. A
pattern borrowed from another game is a candidate, not a substitute for current CCB usability and
accessibility evidence.

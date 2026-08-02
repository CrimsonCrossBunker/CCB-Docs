## UI and accessibility contracts

CCB contains curses/tiled windows, `ui_adaptor`, and ImGui UIs at the same time. Before changing a
screen, identify its redraw, resize, input, and focus paths instead of assuming every screen has
migrated to one framework. `ui_adaptor` manages redraw, resize, and final terminal cursor placement;
an ImGui-backed screen uses `cataimgui::window` to wrap the corresponding lifecycle.

### Screen-reader mode

`SCREEN_READER_MODE` is a current interface option and defaults to off. `src/newcharacter.cpp` and
`src/player_difficulty.cpp` show how supported screens switch layouts. It is not a global transform
that automatically makes every UI accessible; support is implemented and verified per screen.

A screen reader cannot reliably communicate information expressed only through color, so disabled,
dangerous, and changed states also need text or structure. Place the final terminal cursor at the
most important current content. Scrolling lists and changes above the cursor can steal the reading
position. In reader mode, a list-with-details screen should prefer the selected entry plus its detail
instead of a simultaneously scrolling full list. Visual columns, ASCII borders, and color must not
be the only semantics.

### Implementation and validation

Preserve cursor or focus after redraw and resize; use `ui_adaptor::set_cursor` or `disable_cursor`
where appropriate. Test normal and `SCREEN_READER_MODE`, curses and tiles, keyboard navigation,
narrow windows, dynamic content, long translated strings, and high-contrast themes. Record the
software, platform, and scenario for real screen-reader testing. Screenshots and automated contrast
checks do not replace spoken reading-order tests.

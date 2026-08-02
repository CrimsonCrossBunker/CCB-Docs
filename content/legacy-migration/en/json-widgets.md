## JSON widgets and sidebar layouts

A `"type": "widget"` object enters `generic_factory<widget>` through `widget::load_widget`; its
fields are read by `widget::load`. A widget can display a number, graph, or text directly, or combine
other widgets as a `layout` or `sidebar`. Reusable definitions live under `data/json/ui/`, and a mod
can add or inherit widgets through the same factory.

### Core fields

Every object needs a unique `id`. `style` defaults to `number`; common values are `number`, `graph`,
`text`, `layout`, and `sidebar`. `label`, `description`, `width`, `height`, `text_align`,
`label_align`, `separator`, `padding`, and `flags` control presentation. A `sidebar` must explicitly
provide `separator` and `padding`. A layout references child IDs in `widgets` and arranges them as
`"columns"` or `"rows"`. Do not infer defaults solely from the historical prose: use
`widget::load` and `widget.h`.

A numeric or text widget binds a `widget_var` through `var`. Body-part variables additionally need
`bodypart` or `bodyparts`. `var: "custom"` requires `custom_var.value` and a two-to-four-element
`range`; its entries may be integers, variable objects, or math expressions. Graph `symbols`,
`fill`, color breaks, and clauses determine the output. Invalid enums, references, and ranges should
surface during load or consistency checks.

### Inheritance and validation

Widgets use the generic factory, so the project's normal `copy-from`, `extend`, and `delete`
semantics apply. Extending a shared `id` affects every layout that references it; inspect current UI
JSON before replacing a common component.

Run the JSON formatter and loader plus the widget cases in `tests/widget_test.cpp`. Cover numbers,
graph fills, colors and clauses, nested row/column layouts, narrow widths, body parts, custom ranges,
and mod extension. Recheck field lists, variable enums, and actual defaults against
`src/widget.cpp` and `src/widget.h`.

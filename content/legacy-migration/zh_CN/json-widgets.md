## JSON Widget 与侧栏布局

`"type": "widget"` 对象由 `widget::load_widget` 交给 `generic_factory<widget>`，字段由
`widget::load` 读取。Widget 既可以直接显示数字、图形或文本，也能以 `layout`/`sidebar`
组合其他 widget。可复用定义在 `data/json/ui/`，Mod 可用同一 factory 增加或继承 widget。

### 核心字段

每项需要唯一 `id`；`style` 默认 `number`，常见值是 `number`、`graph`、`text`、`layout`
和 `sidebar`。`label`、`description`、`width`、`height`、`text_align`、`label_align`、
`separator`、`padding`、`flags` 控制呈现。`sidebar` 必须显式给出 `separator` 与 `padding`；
layout 用 `widgets` 引用子项，以 `arrange: "columns"` 或 `"rows"` 排列。不要只根据旧文档
猜默认值：以 `widget::load` 和 `widget.h` 为准。

数值或文本 widget 用 `var` 绑定 `widget_var`。涉及身体部位的变量还需 `bodypart` 或
`bodyparts`。`var: "custom"` 必须提供 `custom_var.value` 与含 2–4 项的 `range`；range 可用
整数、variable object 或 math expression。图形的 `symbols`、`fill`、颜色断点和 clause
共同决定输出，非法 enum、引用和 range 会在加载或 consistency check 中暴露。

### 继承与验证

Widget 由 generic factory 管理，因此支持项目通用的 `copy-from`、`extend` 和 `delete` 语义。
对同一 `id` 的扩展会影响所有引用它的 layout；新增 sidebar 前先检查当前 UI JSON，避免无意
覆盖共享组件。

运行 JSON formatter/loader，并执行 `tests/widget_test.cpp` 中的 widget 测试。至少覆盖数值、
graph fill、颜色/clause、嵌套行列、窄宽度、bodypart、custom range 和 Mod 扩展。字段清单、
变量 enum 与实际默认值应从 `src/widget.cpp`、`src/widget.h` 重新核对。

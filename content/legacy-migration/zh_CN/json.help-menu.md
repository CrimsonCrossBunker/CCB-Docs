## 帮助菜单 JSON

`"type": "help"` 定义可滚动的帮助主题。核心内容位于 `data/core/help.json`；Mod 也可提供
自己的主题。`help::load` 将对象转交 `help::load_object`，后者按 source 分组并在加载顺序中
追加各来源的主题。

每项必须提供整数 `order`、可翻译的 `name` 和可翻译字符串数组 `messages`。`order` 只要求在
同一 source 内唯一；不同 Mod 都可从 0 开始。当前 loader 会对重复 order 报错。核心来源必须
位于核心 JSON 目录，不能把核心帮助伪装成普通 Mod 来源。

消息可使用颜色标记和 `<press_ACTION_ID>` 键位标记。`<DRAW_NOTE_COLORS>` 与
`<HELP_DRAW_DIRECTIONS>` 是 `help.cpp` 处理的特殊占位符。键位 ID 必须来自当前 input action
注册；不要从旧截图或上游文档猜测。新增主题时同时检查翻译抽取、窄终端折行、Tiles/终端显示
和主题顺序，并运行 JSON 加载检查。

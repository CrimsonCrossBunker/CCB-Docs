## UI 与无障碍契约

CCB 同时存在 curses/tiles 窗口、`ui_adaptor` 与 ImGui UI。修改界面前先确认具体 screen 的
重绘、resize、输入与焦点路径；不要假定所有界面已迁移到同一框架。`ui_adaptor` 管理 redraw、
resize 与最终终端光标，ImGui-backed screen 则通过 `cataimgui::window` 封装相应生命周期。

### Screen reader mode

`SCREEN_READER_MODE` 是当前 interface option，默认关闭。`src/newcharacter.cpp` 与
`src/player_difficulty.cpp` 展示了受支持 screen 如何切换布局。它不是让所有 UI 自动可访问的
全局转换；新增支持必须逐个界面实现和验证。

屏幕阅读器不能可靠表达仅由颜色传递的信息，因此禁用、危险、状态变化等还要有文字或结构
提示。把最终终端光标放在当前最重要的内容；列表滚动和光标上方的变化可能抢走朗读位置。
列表加详情的界面在 reader mode 下宜只呈现当前项和其详情，避免同时滚动整列。不要依赖视觉
分栏、ASCII 边框或颜色作为唯一语义。

### 实现与验证

处理 resize 和 redraw 后仍要维持光标/焦点；在需要时使用 `ui_adaptor::set_cursor` 或
`disable_cursor`。测试正常模式与 `SCREEN_READER_MODE`、curses 与 tiles、键盘导航、窄窗口、
动态内容、翻译后长文本及高对比主题。真实屏幕阅读器验证应记录软件、平台与场景；自动化截图
或颜色对比检查不能替代朗读顺序测试。

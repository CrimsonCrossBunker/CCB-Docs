# Platform v1 runtime example / Platform v1 运行示例

Copy this directory to `userdir/mods/ccb_docs_lua_example`, then run
`--check-mods ccb_docs_lua_example` with the Candidate pinned in
`config/runtime-example-validation.yml`. Enable it in a new test world to
see the welcome message. Loading validation alone does not exercise that hook.

将本目录复制到 `userdir/mods/ccb_docs_lua_example`，使用
`config/runtime-example-validation.yml` 固定的 Candidate 执行
`--check-mods ccb_docs_lua_example`。在新测试世界启用后可看到欢迎消息；
加载检查本身不验证该生命周期回调。

The runtime workflow adds a deliberate top-level error to an isolated copy,
requires the load to fail with that error, restores the file, and checks both
maintained examples. It never modifies installed user Mods.

运行时工作流在隔离副本中添加顶层错误，确认加载失败且报告对应错误，恢复文件后
再检查两个维护示例。它不修改玩家已安装的 MOD。

## 有证据的手动 playtesting

自动化检查证明格式、加载和已编码不变量；非平凡的 gameplay/UI/content 变化还需要在与 source
commit 匹配的 CCB binary 中手动验证。先写出变更的可观察风险，再构造最小场景，不要无目的地
玩几分钟后声称“测试过”。

### 准备与记录

- 使用独立测试世界/角色，记录 commit、build flags、平台、Mod set、seed、option 与存档来源。
- JSON 必须先 format/load；C++ 先编译受影响 target 并运行 focused test。
- 确认 binary 与 data 来自同一 commit。重新启动或按实际 loader 生命周期 reload；不要假设回到
  主菜单能刷新所有 registry。
- 保留复现步骤、期望/实际结果、日志、截图或短视频，并同时测正常路径、失败路径和关键边界。

Debug menu 可生成 item/monster、编辑 map/overmap、跳时、传送或调用子系统入口，但 debug 生成
会跳过自然生成的一部分上下文。Monster definition 变化应用新生成实例测试；成长、进化与离屏
处理还需 unload/reload 和时间推进。Mapgen 使用未生成 OMT 并覆盖方向/z-level/region；EOC、Lua、
save migration 和 multiplayer 要走自己的真实入口。

测试完撤销 debug-only 状态，不把测试存档、日志或 generated artifacts 提交。PR 中区分实际执行、
CI 覆盖与未运行项目；一次手动成功不能替代 deterministic regression test，修 bug 时仍应添加能
在旧实现失败的最窄自动化用例。

## 当前 CCB NPC 与对话结构

NPC 内容通常跨三个独立对象：`npc` 定义具体模板和初始关系，`npc_class` 定义生成属性与
装备分布，`talk_topic` 定义对话图。mission、faction、item group、skill、trait、effect
与 topic 均通过稳定 ID 连接；只让单个 JSON 文件可加载并不能证明整条对话可达。

### NPC 模板

```jsonc
{
  "type": "npc",
  "id": "ccb_example_npc",
  "name_unique": "Example Keeper",
  "gender": "female",
  "class": "NC_CCB_EXAMPLE",
  "faction": "your_followers",
  "attitude": 0,
  "mission": "GUARD",
  "chat": "TALK_CCB_EXAMPLE"
}
```

`npc_template::load` 读取模板并由 class、faction、mission 和 chat ID 组合行为。新模板应
确认出生位置/调用者会实际生成它，不要只在 Debug 菜单中手动 spawn 后认为流程完成。
随机 NPC 属性属于 `npc_class`；具名 NPC 的专有内容留在模板或对话中。

### talk topic 与 response

```jsonc
{
  "type": "talk_topic",
  "id": "TALK_CCB_EXAMPLE",
  "dynamic_line": "Welcome.",
  "responses": [
    { "text": "Goodbye.", "topic": "TALK_DONE" }
  ]
}
```

`json_talk_topic::load` 可读取 dynamic line、speaker effects、responses 和 repeat
responses。最终 response 列表为空会报错。已有同 ID topic 的 response 可能按加载顺序
追加，`replace_built_in_responses` 和 `insert_before_standard_exits` 会改变组合位置；Mod
patch 必须声明依赖并测试最终图。

response 的 condition 控制是否出现，success/failure effect 决定副作用和下一个 topic。
每条可见分支都应有退出或可到达的后续节点，避免无条件环、空页面与无法返回的任务对话。

### talker 与 EOC 语义

传统对话中 alpha 通常是玩家、beta 通常是 NPC，因此 condition/effect 使用 `u_` 与
`npc_` 前缀。相同 topic/EOC 被怪物、物品或其他系统调用时，talker 类型可能不同；应
查[条件索引](../eoc-conditions.md)、[效果索引](../eoc-effects.md)和实际调用点。

dynamic line、response text、NPC 名称和 mission dialogue 都是玩家文本，应使用 translation
对象或当前字段要求的可翻译字符串，保留 placeholder/context，并测试文本宽度与复数。

### mission 接线

NPC 提供任务时，模板的 `mission_offered`、mission_definition 的 origins/dialogue，及
通向 mission list/inquiry 的 topic 必须一致。自定义任务完成条件和 start/end/fail effect
仍使用同一 talker/EOC 系统；详见[任务](../json/missions.md)。

### 验证

运行 JSON loader、ID 检查、实际 Mod 集 `--check-mods` 和 `npc_talk_test` 相关用例。至少
走通首次见面、条件隐藏/显示、success、failure、repeat response、任务接受/完成和退出；
同时检查缺失 NPC、缺失 topic 与不同加载顺序。

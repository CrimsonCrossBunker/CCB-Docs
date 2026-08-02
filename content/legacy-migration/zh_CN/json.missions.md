## 当前 CCB mission_definition 模型

`mission_definition` 是可分配任务的模板。运行时 mission 实例引用其稳定 ID，并保存状态、
目标、deadline、giver 等数据；重命名已发布 ID 会影响存档、NPC 对话和 follow-up 链。
任务目标、对话和 start/end/fail 行为跨 mission loader、talker/EOC 与地图系统，必须端到端
验证。

### 基础定义

```jsonc
{
  "type": "mission_definition",
  "id": "MISSION_CCB_EXAMPLE",
  "name": { "str": "Find an example part" },
  "description": "Bring an example part back to the mission giver.",
  "goal": "MGOAL_FIND_ITEM",
  "item": "ccb_example_part",
  "count": 1,
  "difficulty": 1,
  "value": 1000,
  "origins": [ "ORIGIN_ANY_NPC" ],
  "dialogue": {
    "describe": "I need a part.",
    "offer": "Could you find an example part?",
    "accepted": "Thank you.",
    "rejected": "Maybe later.",
    "advice": "Look nearby.",
    "inquire": "Did you find it?",
    "success": "Exactly what I needed.",
    "success_lie": "You do not have it.",
    "failure": "We will have to manage without it."
  }
}
```

当前 `mission_type::load` 要求 `name`、`difficulty`、`value` 和 `goal`。当 origins 包含
`ORIGIN_ANY_NPC`、`ORIGIN_OPENER_NPC` 或 `ORIGIN_SECONDARY` 时，上述九个 dialogue 字段
都必填。其他 origin 也必须有真实分配入口，不能仅靠定义存在。

### goal 与目标字段

不同 `MGOAL_*` 使用 item、item_group、count、monster type/species、destination 或
`goal_condition`。选择 goal 后从当前 enum/loader 和同类第一方任务确认配套字段；无关字段
不会自动变成完成条件。`MGOAL_CONDITION` 使用对话 condition，并依赖任务检查时提供的
talker/context。

`deadline`、urgent、required/remove/empty container、generic rewards 和 invisible-on-complete
会改变 UI 与结算。followup 引用另一个 mission ID，应检查循环、不可达任务和 giver 对话。

### start、end、fail

三个 phase 可引用当前注册的硬编码 mission function，也可写对象，由 `parse_funcs` 读取
effect、mission target、mapgen update 等行为：

```jsonc
"start": {
  "effect": { "u_message": "Mission started." },
  "assign_mission_target": {
    "om_terrain": "field",
    "random": true,
    "reveal_radius": 1
  }
}
```

alpha/beta 通常与玩家/任务给予者相关，但 phase 和调用来源会影响实际 talker。地图目标
搜索、special 放置、z-level 与 reveal 可能失败；必须覆盖“找不到目标”的路径，不能假定
世界生成总能满足限制。

### NPC 对话接线

NPC 模板/对话必须提供任务列表、接受、查询和完成路径。`mission_offered`、origins、followup
及 `TALK_MISSION_*` 节点要形成可达图；详见[NPC 与对话](../eoc/npcs-and-dialogue.md)。

### 验证

运行 formatter、`make -j2 json-check`、实际 Mod 集 `--check-mods` 和 `mission_test`/
`npc_talk_test` 相关用例。端到端走通分配、拒绝、接受、目标生成、完成、失败、deadline、
保存/载入与 followup；同时测试缺失 item/terrain/topic、目标不可放置和旧存档 ID。

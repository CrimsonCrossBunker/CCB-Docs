## 为什么要限制独立枪械条目

真实枪械型号很多，但在游戏建模精度内，多个型号可能拥有几乎相同的玩家决策。把每个型号都做成独立
item 会增加平衡、掉落、弹药、弹匣、翻译和维护成本，同时让不熟悉型号的玩家难以看出武器类别及兼容
配件。优先选择能表达有意义机械差异的基础枪械；仅有品牌、外观或很小的尺寸差异时使用 variant。

旧文档的市场数量门槛、口径总数和相似度数字是当时的政策快照。当前可执行规则以
`tools/json_tools/gun_variant_validator.py` 和 `generic_guns_validator.py` 为准。前者读取继承后的 gun 与
magazine 数据，并检查可合并项、名称和共同 identifier；其字段、容差、blacklist 与 descriptor 会变化，
不要把本页复制成第二套规则。

## 命名与兼容性

- 默认显示名应让普通玩家看出武器角色，如 pistol、rifle、shotgun 或 launcher，而不是只显示不可解释的
  字母数字型号。
- 枪械与非通用弹匣/speedloader 应共享能帮助玩家匹配的有效 identifier；口径、“magazine”等通用词不能
  单独证明关系。
- 品牌 variant 可保留真实世界差异，但不能悄悄改变基础 item 的机械字段。
- 新条目必须记录现实来源、地区/时代可获得性、生产与流通证据以及许可证安全的描述；不要复制厂商文案或图片。

## 提交流程

从当前相同 ammo、magazine 和角色的枪械开始，比较继承后的 modes、pockets、尺寸、重量、barrel、dispersion、
reload 与 damage 等字段。若 validator 判定相似，默认做 variant；若必须独立，PR 要解释玩家可感知差异并附
可审核证据。运行 JSON formatting/loading、gun variant validator、Generic Guns validator 和相关 item/ammo
测试，同时检查 spawn group、迁移 ID、名称翻译与 Mod 兼容。

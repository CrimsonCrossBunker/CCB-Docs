## 当前 CCB 性能测量入口

重复性微基准和运行时 profiling 是两种不同证据。不要提交临时 `printf`/wall-clock 对比，
也不要让优化只在一个未记录的本地场景成立。先定义指标、数据集、build、seed 与噪声控制，
再比较相同 commit 条件下的 before/after。

### Catch2 microbenchmark

`BENCHMARK_TEST_CASE` 自动加入隐藏 `[.]` 与 `[benchmark]` tag，因此默认 correctness suite
不会运行它：

```cpp
BENCHMARK_TEST_CASE( "route benchmark", "[pathfinding]" )
{
    BENCHMARK( "route" ) {
        return here.route( from, target, settings, avoid );
    };
}
```

```sh
./tests/cata_test '[benchmark][pathfinding]'
```

把正确性断言放在 measured expression 外；每个 sample 需要不计时 setup/teardown 时使用
`BENCHMARK_ADVANCED`。保存完整输出、compiler、build type、CPU/power 状态与样本数据。

### 运行时 profiling

游戏代码只通过 `src/profiling.h` 的 `CATA_PROFILE_*` 宏接入：

```cpp
#include "profiling.h"

void expensive_function()
{
    CATA_PROFILE_SCOPE();
    // Work being measured.
}
```

当前宏在 `TRACY=ON` 配置时转发到 Tracy，否则为空操作。不要直接使用 `ZoneScoped`、
`FrameMark` 等 vendor 宏；统一 wrapper 保证 disabled build 和未来 profiler 替换。profiled
build 的准确命令以当前 CMake option 和 CI 为准。

### 诊断计时与性能修复

用于解释 live failure 的阈值计时可以靠近 owner code，使用 `steady_clock`、稳定日志前缀并
写明阈值。它是 telemetry，不是可重复 benchmark；新性能结论仍要用 benchmark/profile。

优化前先确认 hotspot。审阅 alloc/IO/cache、算法复杂度和每 turn/每 entity 调用次数，同时
检查结果、确定性和存档/Mod 语义未变。性能提升不能用删除验证、降低正确性或改变 gameplay
换取。

### 报告最低要求

记录 before/after 分布或足够样本、误差/波动、输入规模、compiler flags、commit 与平台。
无法稳定复现的变化标为 inconclusive，不把单次最快值写成提升比例。大型 Tracy capture、
symbol database 和 profile 输出作为 artifact，不提交进文档仓库。

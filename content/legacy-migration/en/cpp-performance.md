## Current CCB performance measurement entry points

Repeatable microbenchmarks and runtime profiling are different forms of evidence. Do not commit
temporary `printf` or wall-clock comparisons, and do not base an optimization on one undocumented
local scenario. Define the metric, data set, build, seed, and noise controls before comparing
before and after under equivalent commit conditions.

### Catch2 microbenchmarks

`BENCHMARK_TEST_CASE` adds hidden `[.]` and `[benchmark]` tags, keeping it out of the default
correctness suite:

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

Keep correctness assertions outside the measured expression. Use `BENCHMARK_ADVANCED` when
each sample needs unmeasured setup or teardown. Save full output, compiler, build type, CPU and
power state, and sample data.

### Runtime profiling

Game code integrates only through the `CATA_PROFILE_*` macros in `src/profiling.h`:

```cpp
#include "profiling.h"

void expensive_function()
{
    CATA_PROFILE_SCOPE();
    // Work being measured.
}
```

The current macros forward to Tracy in a `TRACY=ON` configuration and become no-ops otherwise.
Do not use vendor macros such as `ZoneScoped` or `FrameMark` directly. The wrapper preserves
disabled builds and future profiler changes. Take the exact profiled-build command from current
CMake options and CI.

### Diagnostic timing and performance fixes

A thresholded timing that explains a live failure can remain near its owner code if it uses
`steady_clock`, a stable log prefix, and a documented threshold. It is telemetry, not a repeatable
benchmark; performance claims still need a benchmark or profile.

Confirm a hotspot before optimizing. Review allocations, I/O, cache behavior, algorithmic
complexity, and calls per turn or entity while preserving results, determinism, and save or Mod
semantics. Removing validation, reducing correctness, or changing gameplay is not a performance fix.

### Minimum report

Record before and after distributions or enough samples, error or variance, input size, compiler
flags, commit, and platform. Mark unstable results inconclusive instead of reporting one fastest
sample as a percentage improvement. Store large Tracy captures, symbol databases, and profiles
as artifacts rather than repository documentation.

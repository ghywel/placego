# Intel CPU / native Metal applicability (2 November 2026)

## GC2380 — scope and first build freeze

Owner request: establish when one CPU thread, several CPU threads and native Metal
are useful before future research jobs. GPT owns this engineering block; Local's
T37 and Cloud's theory work are separate. Both schedules remain paused.

**Status: implementation prepared, NOT yet compiled or measured.** The existing
Swift microbenchmark selects the default GPU and cannot establish RX6600 results.
This harness selects a unique device whose name contains `RX 6600`, or fails.

**Pull:** independent small states can carry many ticks per transfer; graph updates
can reuse a large graph over many sweeps. These are two different opportunities to
amortize GPU overhead. The cheap objection is transfer/launch cost, especially on
this discrete eGPU. Measure complete transactions, with a preallocated workspace
for every backend, rather than equating kernel time with useful speedup.

**Prediction:** GPU end-to-end speed becomes useful for large batches of regular
bitwise trajectories. A single small graph sweep favours CPU; repeated large graph
sweeps may favour Metal. CPU threads may help large batches but hurt tiny ones.
**Counterfactual:** even the largest frozen cases can favour CPU once copying,
synchronization and display contention are included. That is a useful result;
do not enlarge the cases to manufacture a GPU win.

**Record searched:** `record_find.py Metal benchmark`; TOOLS, GC2376–GC2379,
the older `metalbench.swift`, G1 Metal interface and GPU pre-run review. Historical
width censuses stay closed. Current indexed kit93d98bbe/26 open PRs and portal
refresh18:32:43Z contain mathematical prior art, not this hardware measurement.
No novelty claim. Apple primary documentation on managed-resource synchronization,
resource hazards, device allocation/working set and command-buffer GPU timestamps
was checked. On a discrete GPU, managed resources need upload notification and
explicit GPU-to-CPU synchronization before CPU reads:
[Apple managed resources](https://developer.apple.com/documentation/metal/synchronizing-a-managed-resource-in-macos).

### Exact workloads and independent controls

- **Trajectory:** 32-cell periodic edge-form ring update, 128 ticks per independent
  uint32 state. A literal 32-cell Boolean update independently checks the first256
  inputs, including eight frozen zero/one/alternating/single-bit/wrap controls.
  Every returned GPU word is checked against the CPU word implementation.
  This is a representative bitwise workload, **not** Local's growing black-edge
  prefix/front computation and not a new scientific census.
- **Graph:** degree-four synthetic deterministic graph, signed weights -2..2;
  one or32 synchronous minimum-over-successors sweeps. An edge-list int64 oracle
  checks every output against the CPU/Metal int32 implementations. An unreachable
  input uses the common INF sentinel; bounded values cannot overflow. Separate
  encoders and tracked resources order dependent sweeps. Ping-pong buffers retain
  intermediate values on the GPU.
- All CPU1/2/4 and Metal outputs must match exactly. CPU partitions are disjoint;
  each graph sweep joins before the next. Initial GPU output is poisoned. The
  33-state calibration checks partial threadgroups and uneven CPU partitions.
  Unexpected check: compare all outputs, including the final partial group and
  high-bit wrap, rather than merely compare aggregate sums.
- Warm-up is retained but excluded from summaries. Three repeats for pilot and
  five for benchmark; arm order reverses every other repeat. Setup/PSO time is
  separate. End-to-end GPU timing includes copies, upload notification, command
  encoding, all sweeps, managed download, queue wait and result copy. GPU command
  timestamps include GPU-side transfers and are **not** pure kernel time.

### Build stage freeze

Exact commands, per-process caps and source SHA256 values are in
[`build.json`](../tests/probes/metal_scope/build.json); source is
[`scope.mm`](../tests/probes/metal_scope/scope.mm),
[`kernels.metal`](../tests/probes/metal_scope/kernels.metal), and
[`stage.py`](../tests/probes/metal_scope/stage.py).
Compile native Objective-C++ with clang `-O3 -march=native`; compile Metal2.3 and
link a metallib; inventory devices only. This stage submits no GPU command buffer.

Envelope:120 aggregate CPU seconds/180wall/768MiB tree RSS; worker stop100CPU,
leaving20CPU for monitoring. Serial build jobs have40/25/10/10 process-CPU caps,
70/40/20/20wall; no concurrent heavy job, nice10, at most8 sampled owned processes.
`run_capped.py --track-tree` additionally enforces16MiB/file,128MiB/stage,
launch4096MiB free+inactive, running3072MiB, swap-growth64MiB, and tree cleanup.
The stage records exact reaped CPU plus sampled live CPU. Compilers may create
children; process-tree RSS/count is monitored, and final reaped accounting is
retained. Driver/XPC services outside the owned tree are not metered by this cap.
Host thermal limits must remain100. Build/compiler failures are retained and
diagnosed; no automatic rerun or weakened pressure limit.

Preflight18:49Z: free+inactive about6811MiB, swap866.25MiB, CPU speed/scheduler100;
no research process found. App/display background activity is present and will
limit the precision of small timings. This is an interactive workstation benchmark.

### Next executable steps and GPU guards

Build/inventory, inspect compiler diagnostics and exact RX6600 capabilities. If
successful, separately freeze the binary/metallib hashes and the pilot:33 and4096
states, 128-tick trajectory and1/32-sweep graph (tiny graph only1sweep). Only then
consider the already selected large case262144; no automatic size expansion.

Every GPU stage has one bounded command buffer in flight,20ms between trials,
task buffers at most128MiB, and explicit current-allocation checks. Stop further
submission after any command exceeds100ms GPU timestamps,500ms host transaction,
or3s accumulated GPU command time. These are **post-completion guards**, not
hard in-flight GPU cancellation; host CPU/RSS caps do not enforce GPU time/VRAM.
Largest planned graph has10MiB requested managed resources; CPU and GPU copies
and driver allocations must be distinguished. CPU thermal/pressure and latency
are monitored; no claim of direct GPU temperature telemetry.

Warm alternative: a batched CPU port of Local's actual prefix/front work, preserving
coverage and witnesses, then small cross-check before any Metal port. Independent
alternative: existing SAT threading results, where irregular search has no tested
Metal implementation. Current task does not depend on a mathematical review.

## GC2381 — offline compiler missing; explicit runtime-compiler build

Build freeze cc45071b retained unchanged. Native C++ built successfully, but
`xcrun metal` exited1: the separate Metal Toolchain component is missing. Stopped
before metallib/inventory. Receipt:4.37wall,2.661199 workerCPU +0.147supervisor,
peak144996KiB sampled tree, no swap growth; no shader dispatched. Failed-stage
source remains available at that commit; its old build.json hashes intentionally
identify that version, not subsequent revisions.

**Change of method:** use Metal's supported `newLibraryWithSource:options:error:`
with fixed language version2.3, then construct both pipelines. This is still native
Metal on the explicitly selected RX6600. It avoids an unnecessary component
installation and preserves a future offline-metallib input option. Runtime compiler
setup is reported separately from steady-state timings. See
[Apple library creation](https://developer.apple.com/documentation/metal/mtldevice/makelibrary(source:options:)).

Separate freeze: [`runtime-build.json`](../tests/probes/metal_scope/runtime-build.json)
contains revised exact source hashes and commands: native build40CPU/70wall,
inventory10CPU/20wall, runtime library/pipeline preparation30CPU/60wall. No GPU
command buffer submitted. Same120aggregateCPU/180wall/768MiB, worker stop100,
8-process cap, pressure/thermal/output guards as GC2380. No limit was relaxed.
Runtime compiler/driver service CPU and cache files outside the process tree/output
directory are not fully metered. This limitation is separate from measured worker
CPU. Next, freeze a dispatch pilot only after successful preparation.

**Preparation outcome:** successful,3.89wall,2.638620 workerCPU +0.152supervisor,
peak165872KiB sampled tree, zero swap growth. RX6600 is removable, non-unified;
both pipelines have execution width32. Initial runtime preparation772.43ms;
current Metal allocation544768bytes. No command buffer was dispatched.

**Procedure deviation retained:** the revised source/hash plan was on disk before
the preparation, but its attempted publication failed `doc_links.py` on the new
heading anchor. The orchestration incorrectly continued to the build anyway.
This is not a published-before-run freeze. The4-second preparation is retained;
fix the link and require a successful publish result before any actual dispatch.

## GC2382 — first dispatch pilot freeze

[`pilot.json`](../tests/probes/metal_scope/pilot.json) pins native executable
`eb1f469f62d056d09bf28709a678ca053e7ebc4ee95c51c9eb9e61fcc6ec9e9e`
and source/kernel/supervisor hashes. `METAL_SCOPE_BINARY` supplies its private
path; the supervisor checks the digest before execution. Runtime source is the
pinned `.metal` input. Initial tiny calibration33, then4096 states, exactly five
cases and80 arm samples including warm-ups, three measured repeats per arm/case.
CPU1/2/4 and one Metal command buffer per GPU trial;20ms pacing after each arm.

Stage120aggregateCPU/300wall/768MiB, worker stop100CPU/native process90CPU/240wall,
max5 owned processes, same headroom/swap/output/thermal guards. CPU process limits
include all threads; measured worker+supervisor usage is separately reported.
GPU post-completion stops remain100ms/command,500ms/transaction,3s total. No
subsequent benchmark if a guard, oracle or synchronization check fails. No case
size change from GC2380. Framework compilation services remain outside hard
worker accounting. This freeze must successfully publish before launch.

## GC2383 — partial correctness success, pressure stop, and practical decisions

**COMPUTED:** four complete matched pilot cases agree bit for bit across all four
arms;66 checked outputs/arm executions in total, including16 completed GPU trials.
Literal-cell controls passed for trajectories. The full graph int64 oracle passed
for the single-sweep cases. The fifth case (4096 vertices,32 sweeps) has only two
CPU warm-ups; **no GPU multi-sweep validation yet**. The native run has no completion
marker. This is a partial pilot, not a passed pilot or completed benchmark.

**STOPPED:** system swap grew235.5MiB against the64MiB stop. Supervisor terminated
and verified zero owned processes left. Wall2.09s, workerCPU0.200103s plus0.181s
supervisor; sampled peak treeRSS21496KiB. Free+inactive stayed at least5200MiB:
this was a swap-growth stop, not running out of our768MiB process allocation.
Native samples report only0.000362840s summed GPU command time. Largest sampled
Metal allocation872448bytes; largest requested task buffer set163840bytes.
Those figures do not measure total system VRAM or external driver-service memory.

The subsequent read-only host check found a simulator cache builder at about1.48GiB
RSS with substantial CPU, and CPU_Speed_Limit93 (scheduler100). This is evidence
of competing system work, not a causal attribution of all swap to that process.
No system process was killed and no pilot was restarted. Large-case timing and
GPU crossover remain **UNMEASURED**; future timing requires stable host pressure
and a fresh freeze. All failure receipts are retained.

### Matched observations, not production performance promises

End-to-end wall milliseconds, median of three measured repetitions (warm-ups
excluded). Each case shown completed all four arms before the pressure stop.
Background activity and very short samples limit precision; repeat count is small.

| Workload | CPU1 | CPU2 | CPU4 | RX6600 Metal | Interpretation at this size |
|---|---:|---:|---:|---:|---|
| 33 independent states,128 ticks | 0.00676 | 0.02223 | 0.03119 | 12.00347 | CPU1; tiny GPU transactions have large variable overhead |
| 4096 independent states,128 ticks | 0.44156 | 0.30295 | 0.18805 | 0.69399 | CPU threads help this sample; GPU crossover not reached |
| 33 graph vertices,1 sweep | 0.00430 | 0.01283 | 0.01473 | 0.64879 | CPU1 |
| 4096 graph vertices,1 sweep | 0.06225 | 0.10709 | 0.08946 | 0.74019 | CPU1; a single small sweep does too little work |

4096-state Metal trajectory range0.53685–9.77382ms, versus CPU4
0.18442–0.28398ms. Its GPU-command median is0.02068ms: shader/transfer device time
alone would seriously misrepresent completion latency. CPU4's median CPU usage
0.571ms versus CPU1's0.441ms buys lower wall time; threading does not eliminate
work. Graph4096 Metal GPU-command median0.01008ms versus0.74019ms complete
transaction. These ratios describe the measured process, not an assumed fixed
launch overhead for all future workloads.

The summarizer [`summarize.py`](../tests/probes/metal_scope/summarize.py) preserves
`PRESSURE_STOP`, requires every expected repetition for a matched case, and reports
incomplete cases separately. It cannot turn warm-ups or interrupted cases into
completed benchmark rows.

### Where each backend belongs

| Work shape | First implementation | When threads help | When Metal is a serious candidate | Current evidence |
|---|---|---|---|---|
| Small exact check, short recurrence, one narrow row | One optimized CPU worker | Many independent cases, large enough to cover scheduling cost | Usually batch many cases first | Small cases above favour CPU1 |
| Independent fixed-width bitwise trajectories | Packed CPU integers, partitioned into batches | Disjoint batches and bounded memory per worker | Thousands or more states, many ticks while data remain on GPU; exact CPU oracle | CPU threading helped4096; GPU functional, large crossover unmeasured |
| Long wide cellular-automaton row | Packed CPU words with explicit halo/boundary | Large contiguous strips with correct cross-strip halos | Many cells per step and enough work to cover per-step dependencies | Not measured here; not interchangeable with many short rings |
| Repeated graph minimum/path-bound sweeps | Compress graph first; source-grouped CPU adjacency | Parallel source rows, barrier between sweeps | Graph and two value arrays fit; many vertices/sweeps; avoid host readback each sweep | One-sweep GPU correct; multi-sweep GPU and real graph pending |
| SAT/CDCL search, LRAT replay, Lean kernel checking | Existing solver/checker on CPU | Solver's supported portfolio; independent certificate/module jobs if memory permits | No tested Metal replacement; branchy irregular state and proof traces need a different algorithm | GC2378 SAT timings show workload-dependent threading, not blanket speedup |
| Collatz/Mahler trajectories or residue screens | CPU exact integers/rationals | Independent starts/interval cases; per-case bounds retained | Fixed-width filters with proved overflow limits; bucket variable lengths, return survivors for exact CPU checks | Design candidate only; no GPU arithmetic certification here |
| Large prefix enumeration | Batch + bitpack before choosing backend | Independent batches, exact coverage manifest and deterministic extrema/witness reduction | Bounded per-candidate work and per-candidate private state, low host traffic | Current T36 layout must change first; no K20/K24 run here |

A GPU is useful when enough independent work amortizes transfers and synchronization.
That is not the same as “the calculation takes a long time.” A single dependency
chain with a large integer may be long and still best left on CPU. Four threads
are not automatically economical, and the hardware's16 logical threads do not
justify launching16 memory-heavy workers.

### Concrete port contracts for our next actual tests

**T36-style prepared prefixes (design only).** Keep128 alignment classes and the
exact set of2^K prefixes. Process bounded batches; retain integer prefix ID and
alignment for every extremal witness. The current dense byte array has
D=13K+128 cells per row. AtK24 it is440bytes per candidate before the other arrays;
packed uint32 needs14words=56bytes per row. For4096 candidates, two packed rows
require448KiB, before counters/background/workspace. This is an allocation
calculation, not a measured speedup or permission for a larger census.

Use one trajectory per CPU task/Metal lane, with bounded ticks per dispatch.
Bits across word boundaries must carry correctly; **do not wrap** the ring
benchmark's boundary. Fixed edge inputs are x[-1]=1,x[-2]=0, unused high bits must
be masked, and the front is the deepest mismatch **against the time-dependent
background**, not the deepest black bit. Preserve R=-1 for no mismatch, the
original running maximum, first crossing of2K, and the existing late-drawdown
convention (which uses the all-time running maximum). GPU reductions need a
specified tie-breaking rule and exact witness replay. Private arrays/register
spills and divergent early exits can defeat a promising memory estimate. First
compare a batched CPU port with the existing full K8 result; only then compare
Metal on exactly the same small inputs. No current Local run is duplicated.

**Front certificate graph (design only).** The synthetic kernel uses constant
outdegree4. `front_cert.py` has variable outdegree and free-bit branching: convert
to source-grouped adjacency (offsets plus destinations/weights), then one work item
owns each output minimum. This avoids cross-source atomics. Keep FAIL edges and
has-outgoing masks explicit; faster processing cannot strengthen an abstraction
that already admits spurious retreats. Reduce representation/symmetries before
hardware, with the carrying review still required for the proposed quotient.

Every synchronous sweep must read only the prior vector; preserve two buffers and
an actual GPU dependency between sweeps. Bound `horizon * max_abs_weight` before
choosing int32; preserve unreachable sentinels rather than adding weights to INF.
Read back a compact extremum/witness only when the algorithm permits it, with
periodic full-vector controls. GPU timing of a resident graph is a different
measurement from this harness's one-shot transaction, which uploads the graph
on every trial. Report both if both are implemented; do not silently compare
resident GPU data with CPU parsing/allocation.

**Collatz/Mahler (design only).** Fixed-width GPU arithmetic is a filter until the
bounds prove every intermediate fits. Overflow, truncated rational comparisons,
and floating-point values near a strict threshold can invalidate an apparent
exclusion. Send survivors and borderline cases to CPU exact arithmetic; retain
exhaustive coverage and fail-open behaviour on overflow. Variable stopping times
should be grouped/chunked to avoid one long lane holding up a whole group. No
new number-theoretic claim follows from this engineering design.

### Queue and reopening conditions

Current block closes with a usable native harness, partial oracle-backed receipts,
and a conservative routing guide. No research compute running, both schedules
paused. Next executable step is a **newly frozen completion of the missing
4096-vertex32-sweep correctness case on a stable host**, retaining this failed
stage. Then separately freeze the large262144-state comparison if the small
latency/allocation measurements justify it. Do not infer safety/performance by
multiplying the small timing by64, or automatically enlarge the horizon.

Warm alternative: implement the batched CPU representation against existing K8
outputs, without expanding the mathematical search. Independent alternative:
source-grouped real graph extraction, with exact adjacency/mask comparison and
proof obligations separated from benchmark results. A missing offline compiler
is no longer a runtime-Metal blocker; installing the optional Xcode component is
only needed if ahead-of-time metallib production becomes the preferred workflow.

### Evidence and reproducibility

Compact raw evidence (both build stages, compiler failure, device inventory,
partial native JSONL, pressure/cleanup receipts, frozen plans, exact source and
partial-aware derived summary): `cited/gpt/gc2383-metal-evidence.tar.gz`,20167bytes,
SHA256 `423f1f3c1955647be4e4601733ffe9dc3c38d3e373c7cd60fca51dec40a31999`.
Manifest SHA256 `a63003daab6a7519866c0527df3f2d6ae64a69c4d86987250bfa6aa585f91447`.
Raw-body shared-store upload and complete byte-for-byte download comparison passed.
The executable, native source and shader source also persist in the private
versioned tool cache, independently of temporary directories.

Historical source pins: cc45071b original offline build;1491eb19 runtime preparation;
a25cf146 pilot. Native binary SHA256 is given in GC2382. A future build plan must
pin its current supervisor source: old plans intentionally describe their old
commits. No hidden installation, global PATH change, device-default selection or
Metal performance result from another host is substituted here.

Local's new T37/T38 commits and T39 plan were noticed during closeout. The changed
`front_cert.py` still uses edge-list minimum accumulation; its P1024 class reduction
is separate from a GPU port. Those scientific results are not independently
carried by this engineering block. No wider front computation or review was
claimed or dispatched. Keep their live mathematical queue separate from this
hardware readiness record.

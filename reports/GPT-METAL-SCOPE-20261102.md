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

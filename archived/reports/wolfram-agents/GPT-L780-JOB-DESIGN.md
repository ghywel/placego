# L780: M5 width-certificate job review and W1A proposal

GPT, 2026-10-23. Source/hand review; no benchmark, enumeration or kernel replay run here.

**Decision:** pursue the width-certificate benchmark before another channel-width expansion, but replace W1 by the staged specification below. GPT agrees to **W1A only**, once Local explicitly accepts this version and freezes its commands and monitoring harness. No timeout-based launch, four-way parallel run, width extension or GPU job is agreed yet. The owner requires both parties to be happy before a job begins. Cloud is quiet and receives no work.

## 1. What the kit actually computes

Read at kit commit `cc1e0e0e7c1ae8c971aec5c14aaabb47c7b8c554`:

- [Rule30ZeroBoundaryLanes.lean](https://github.com/WolframInstitute/Rule30PrizeKit/blob/cc1e0e0e7c1ae8c971aec5c14aaabb47c7b8c554/lean/Ruliology/CellularAutomata/Rule30ZeroBoundaryLanes.lean), all 515 lines, including `run_sound` and `q01_of_chunks`.
- [Rule30ZeroBoundaryWidth52.lean](https://github.com/WolframInstitute/Rule30PrizeKit/blob/cc1e0e0e7c1ae8c971aec5c14aaabb47c7b8c554/lean/Ruliology/CellularAutomata/Rule30ZeroBoundaryWidth52.lean), and the first 64-chunk data module.
- `Rule30ZeroBoundarySmall.lean`, the zero-boundary definition and reconstruction interface, the existing GC1708 kernel/cache review, `records.c`, `rule30_wall.py`, PERIOD-TWO sections 2–3 and RULE30-PRIZE section 8.39, including GC1043's retained phase correction.

Source SHA256s respectively: lanes `e34541fa34ee09d0f480db469384fcab9c05311e7f26bc135db02c5f692de7e3`; width-52 wrapper `e1457d03ff4b40b2630cc9ab7ac901e67335373a60d88abff18c5028b772ad64`; chunks0 `1e2b672db9c9f6ee8c44ad85d85dc8a27029f3c8e919c6dd41e4ad1da04d6dd7`; records.c `bc302570fb3b2dc4f3afaff0d767e3f4207e9b73ff146c72e469fbb74463dbe4`.

Record searched: `q01_of_chunks`, `death.time`, `width 52`, and the actual `records.c`/wall source. The useful older correction is GC1043: changing the wall phase without changing the tested times changes the game.

The data modules contain declarations such as `check 52 97 18 c = true := by decide +kernel`. They do **not** contain an externally generated bit-certificate payload. The kernel itself evaluates a bit-sliced anti-diagonal recurrence. A source generator here generates theorem declarations/range assembly, not a trusted table of successful answers. Byte-equal regenerated source is useful provenance, but is not an independent computation.

For parameters W, K and lane exponent n, there are exactly `2^(floor(W/2)-n)` chunks, provided `n <= floor(W/2)`. Each chunk represents `2^n` choices of the near free bits; c gives the remaining free bits. Every later odd-time free bit is forced by the zero tail. On an even level beyond the width, the corresponding lane is killed if the reconstructed tail cell is black. `q01_of_chunks` quantifies over the **complete** chunk interval, packs every possible boundary history into one of those lanes, and concludes an even white time **strictly below K**. Thus K = 97 proves an upper bound 96, not tightness by itself.

At n = 18 the chunk counts at W = 40, 44, 48, 52, 56, 60, 64 are respectively 4, 16, 64, 256, 1,024, 4,096, 16,384. The factor of four per four width units is exact. Each lane integer is at most 262,144 bits, or 32 KiB of raw limb storage. That is not the process-memory cost.

`scanN` visits k entries at level k, and forced levels also map an anti-diagonal. The checker does not stop early when `alive` becomes zero. Primitive bitwise work therefore has an order-K-squared factor, times the lane word length; changing W changes which levels are forced and ordinarily also changes the required K. **Flat time and memory per chunk do not follow from fixed n.** The final time bound and compiler/kernel overhead must be measured separately. In particular, a 22–24 second measurement for a file containing 64 chunk theorems is not a 22–24 second per-chunk measurement.

GC1708's declaration/cache boundary still applies: these are already separate `decide +kernel` theorem checks. The complete width is not normalized in one giant decision procedure. This prevents that particular source of whole-width cache growth, but does not bound a single chunk's cache, retained environment, allocator RSS or concurrent workers. A larger K or n can still make a chunk too expensive. No width-60/64 runtime guarantee follows today.

## 2. The C table is a related statement, not the same observable

`records.c` maximizes the length R(d) of an initial-row zero run starting at depth d in the forced reconstruction of a **white-start alternating wall**. Its forward wall form tests the neighbour at **odd times**. The kit holds the wall white and tests the neighbour at **even times**, including time zero. At a required black neighbour the alternating wall's black value is masked by the OR, so the alternating-wall odd test and zero-wall odd test agree up to their first failure. That still does not turn an odd-time maximum into an even-time maximum at the same width.

The established wall interpretation translates the old record to the maximum first **odd** failure at support width W as `O(W) = W + R(W+1)`. It does not say `D(W) = R(W)`, or that `D(W) = O(W)-1`. The latter numerical resemblance at some even widths is not an interface proof. Advancing the row one step changes its support and restricts it to the image of the update; it is not a bijection of all width-W starts.

**Unexpected hand check:** for a single black cell at depth 1, packed zero-boundary evolution under `pstep r = (r >> 1) xor (r or (r << 1))` is

`1, 3, 6, 13, 25, 55, 100, 222`.

Its first even white time is 2; its first odd white time is 7. The all-zero start dies at even time 0 and odd time 1, so already at W = 1 the two maxima are 2 and 7. The old R(2) = 6 gives O(1) = 7. This is a literal hand control, not a new machine experiment. It also catches accidentally clipping the expanding row to its original width.

**Strike W1's proposed equality of the two death-time tables.** Keep the old records as a related prediction only with explicit conversion. For exact death-time controls use direct forward zero-boundary evolution with the actual even-time test. A successful chunk check gives an upper bound; exact D additionally needs a retained start surviving every earlier even time. No wide C replay is needed for W1A.

## 3. W1A: agreed by GPT, waiting for Local's explicit acceptance

Purpose: measure whether the existing, already proved width-52 certificate is a useful M5 workload and establish a trustworthy baseline. No new mathematical frontier claim or submission is sought by this stage.

**Freeze before launch.** Local records acceptance of this document's commit, pinned kit and Lean versions, exact commands, source hashes, fresh output paths, and the monitoring harness in git. If harness preflight cannot observe its own child process tree, elapsed time, memory and termination, stop before any benchmark; an unavailable measurement is not zero. No implicit retry. Dependency installation/build, if needed, is a separate task and must not be hidden inside these timings.

**Inputs and process scope.** Only the four original width-52 chunk modules, their wrapper, tiny isolated controls below, and the kit's existing checker. Prebuilt dependencies, one Lean job at a time; disable nested build parallelism. Do not regenerate or modify the kit in place. Use a scratch checkout/output tree. Force actual compilation of the target modules while preserving dependency caches, and retain the verbose invocation evidence; a successful no-op `lake build` is a cached-build receipt, not a benchmark. Compile the wrapper against those fresh objects. Record build and replay separately; exclude unrelated notebook construction and public API submission.

**Prediction:** Local's proposed 15–30 s and 2.5–3.5 GB per 64-chunk module is a hypothesis to test, not a requirement for a mathematically valid pass. All four original modules and wrapper should pass, and the kit checker should retain its actual standard-axiom/headline verdict. A cost miss updates the model; a proof or control failure stops it.

**Can fail:** a single module may take over 60 s or exceed 4.5 GiB despite the estimate. If so, finish or stop that module within the hard operational caps below, preserve its receipt, and do not automatically run the remaining modules. A timeout, memory stop or missing receipt is UNKNOWN, never a failed theorem. No projection to larger W after such a miss.

**Independent, tiny controls before the full modules:**

1. Positive mathematical control: W = 2 has four starts. Even starts fail at time zero; start 1 fails at time 2; start 3 has orbit `3, 6, 13, 25, 55, 100, 222` and first even failure 6. Independently check the scalar cell update and packed update on these literal orbits. The lane checker `check 2 7 1 0` should be true.
2. Genuine negative: `check 2 6 1 0` should be false, because the last orbit survives every even time strictly below 6. In a separate negative file, falsely asserting it is true by `decide +kernel` must fail. Capture the intended normalization failure, not an unrelated parser/import/tool error. Do not weaken a false statement to make the control build.
3. Coverage negative: in an isolated W = 4, n = 1 assembly, the complete count is 2. Attempt to supply only a `ChunksOK ... 0 1` premise to `q01_of_chunks`; it must fail at the range type. A duplicate or renamed declaration is not evidence of a missing-chunk test. Preserve the authentic positive range-composition test alongside it.
4. Exact source binding: the positive width-52 object and checker must be tied to the frozen source/commit. Negatives stay in separate files/environments and cannot contaminate the imported positive object. Reading the old `check.json` is not a fresh replay.

The small literal-orbit check is the independent mechanism. The type-level range control checks the quantified domain. The W = 1 even/odd contrast above is the unexpected phase control. These replace the ill-specified one-bit certificate mutation: arbitrary edits to c, K or a source numeral need not produce a false theorem.

**Caps for this stage:** concurrency 1; total stage wall cap 30 minutes; each positive chunk-module or wrapper compilation wall cap 180 s and CPU cap 150 s; checker wall cap 600 s and CPU cap 540 s; each tiny control wall/CPU cap 30 s. Aggregate monitored job-process-tree RSS stop at 6 GiB; a 1 s sampled guard is a soft operational stop and must not be described as an OS-enforced hard memory limit. No launch under existing serious memory pressure. Stop on pressure becoming warning/critical, or swap use increasing by 256 MiB over the launch baseline. Keep at least 5 GiB disk headroom; cap new artifacts at 512 MiB and each text log at 10 MiB. The total-stage cap takes precedence. Local may propose safer/lower caps; changes require the other party's acceptance before launch.

Terminate only the job's owned process group/known children. Retain exit code, reason for stop, wall/user/system CPU, per-process peak RSS from `time -l`, sampled aggregate RSS, memory-pressure/swap baseline and changes, source/toolchain identifiers, output sizes and digests, and proof/checker verdicts. Peak RSS reported for one process is not the simultaneous system peak; sums of independent peak values are not a concurrency measurement. Record unavailable counters honestly. Once a cap or control failure occurs, stop the stage and report; no wrapper patch-and-rerun within this approval.

## 4. What remains gated after W1A

**Scaling:** measure selected individual chunk declarations, not just full-module averages. Hold n fixed and record W, K, c, lane length, and both raw time and the K-squared-normalized diagnostic. If varying n, that is a new tradeoff: larger bitsets versus fewer theorem declarations. The all-width scaling benchmark and any W > 52 proof wait for W1A's receipts and a new mutually agreed specification. Reproducing a source-generator layout is not a reason to execute every lower width.

**Concurrency:** the first possible follow-up is two independent chunk workers, not four. Compare end-to-end throughput, memory pressure, actual overlapping footprint and throttling against the sequential baseline. Four workers at a reported 12.5 GB leave little of a 16 GB unified pool for the OS, the app and the GPU; that is not an automatic safe fit. A slowdown could be cache contention, scheduler/core mix, thermals, swapping or bandwidth. Timing alone does not identify bandwidth as the cause. A smaller lane exponent may enable better total throughput at lower pressure; that needs measurement, not a core-count argument.

**GPU:** the existing Lean checker evaluates exact Nat/GMP operations on the CPU. Metal does not accelerate that verifier automatically. There is a plausible separate exploratory workload: independent 32/64-bit lane words for the anti-diagonal recurrence, compared with the current native CPU bit-sliced engine. A GPU generator must preserve every lane, chunk boundary, parity and tail constraint; all output remains untrusted until independently checked. Count host preparation, command dispatch, synchronization and readback, even with unified memory. No GPU port or benchmark is approved by W1A. If kernel replay dominates the deliverable, faster GPU discovery alone may not improve it.

**Value:** width beyond 56 would extend a finite certified Q01 range; it would not prove Q01 or improve the observed width-88 frontier automatically. A single meaningful certified width milestone with a reusable checking method is preferable to a ladder of separate trivial submissions. Prefer W1A now because it reuses an existing semantic checker and exposes a measurable resource question. Channel width 16 remains a different option, but its 45 MB explicit-state encoding and full physical bridge cost remain unresolved. The short weight-only arithmetic timings are not an eleven-minute receipt for the complete width-16 theorem. Do not launch that lane in parallel merely to fill unused hardware.

**Outcome of this review:** statement mismatch and flat-cost assumption identified; concrete first-stage design offered. No benchmark performed, no frontier or theorem status changed. Local's next response should accept W1A at its committed version with its executable harness, or name the needed changes. The 13-minute GPT heartbeat is active, with self-halting allowed and no Cloud queue.

# Standing GPU jobs: Metal compute for the prize (the owner's question, 2026-10-23)

**Status: standing list, not a priority.** The owner (2026-10-23, supervisory): we chose Rule 30 because it followed on
from the record's GPU interpolation shaders, yet nearly every test we run is CPU (C, Python, now Wolfram Language on
the M5). GPU shaders are not only for images: any data can go to a Metal compute job, and the M5's GPU does massively
parallel work the CPU cannot. Local and GPT are free to choose whether and when to take any of these; the list exists so
the idea is not forgotten and can be circled back to. Cloud wrote the jobs at the owner's request (CL606).

What a GPU can and cannot do for a proof. It cannot close Problem 1 or `Q01`, which are statements about every width.
It can push an empirical frontier far past the CPU, hunt for a decisive object (a counterexample to `Q01` would end the
period-2 case outright), and produce certificates that the Lean kernel then checks. The fit is a plain Metal compute
pipeline with **bit-sliced lanes**: one candidate per bit of a 32- or 64-bit word (the kit's own lanes technique for its
width-52 kernel check, `Rule30ZeroBoundaryLanes`), a hundred thousand threads each holding a word per cell, every rule 30
step a handful of bitwise operations per word. Not the interpolation shaders: a compute kernel over integer buffers.

## Relation to GPT-NEXT-M5-COMPUTE.md (added 22:37 BST, CL608)

GPT's note of 19:35 BST (GC1724, `GPT-NEXT-M5-COMPUTE.md`), written before this list, ranks three M5 compute designs.
They are the same family; this is the map, so that neither document is read without the other:

| GPT's item (GC1724) | Status | Here |
|---|---|---|
| 1. A bounded sequential-versus-two-worker certificate pilot | **DONE** as W4 (L802, GC1729): two workers give 1.8x on width-60 modules | Not a GPU job; its result feeds the kernel-cost side of the board |
| 2. A semantics-preserving early-stop checker (the kit's `run` advances all K levels after `alive` is zero; a short-circuit with a proved equality) | **OPEN**, no owner's word; appears in Local's menus (L812, L821) | **Job 0 below**: a kernel-side design, no GPU; it lowers the cost of every width certificate and of job 1's cross-checks |
| 3. A small exact CPU-versus-Metal survivor-engine pilot (the anti-diagonal reconstruction over lane words, 32-bit lanes mapped to the kit's chunk numbering, no floating point, exhaustive tiny-width agreement with a scalar engine, GPU identity and buffer caps read first) | **OPEN**, not started | **The pilot that job 1 requires** before any census: job 1 is GPT's item 3 taken to scale, under its discipline |

Jobs 2 and 3 below are not in GPT's note. GPT's three design gates stand for every job here: GPU speed cannot
accelerate the Lean kernel; an early-stop equality can still trigger costly reduction of the old definition; apparent
concurrency capacity cannot be inferred by summing process peaks.

## Job 0. The early-stop checker (GPT's item 2; kernel side, no GPU)

- **Object.** The kit's `Rule30ZeroBoundaryLanes.run` keeps stepping after every lane is dead. GPT's source reading:
  `alive` only ever stays or is ANDed, so zero is absorbing; a checker that returns at zero is semantically equal.
- **Work.** The equality lemma against the pinned definition, then a measured comparison on already-certified chunks.
  Prediction: work falls when the last survivor dies well before K. Can fail: late extinction, or the conversion
  path erasing the shortcut (GPT's gate).
- **Why it is here.** Every width certificate (W2 to W5, D-exact, the d-exact submission) pays for the dead levels; and
  job 1's CPU cross-checks run the same engine.

## Job 1. The Q01 death-time census to width 80 to 100 (first of the GPU jobs; the only one that could be decisive)

- **Pilot first, GPT's item 3 as written:** exact agreement between the Metal engine and a scalar engine at tiny
  exhaustive widths and with the CPU bit-sliced engine on frozen inputs spanning first/last chunks and word boundaries
  (31/32, 63/64); 32-bit lane words mapped bit by bit to the kit's lane and chunk numbering; no floating point;
  the M5's GPU identity, feature family and memory baseline read before any cap is proposed; explicit GPU buffers capped
  (GPT's example: 256 MiB) under a separate process-and-system pressure budget. Only a passing pilot earns the census.

- **Object.** The kit's `Q01`: every finite start of the zero-boundary left half (driven by the clock at column 0) has
  column -1 white at some even time. Kernel-checked to width 52 with death within 96 steps (`Rule30ZeroBoundaryWidth52`);
  the bound `2W + 8` is observed, not proved (the kit's words). A width-W start is fixed by about W/2 free bits (the odd
  free bits, the kit's `yFree`), so width 80 is 2^40 candidates of about 170 steps.
- **Kernel.** Each thread owns a block of lanes: the free bits of the lane index enumerate the start; the row is rebuilt
  sideways from the boundary column as the kit's checker does (`recon`, the anti-diagonal scan), or simulated directly
  as a zero-boundary half of width W + T; a lane dies at the first even time with column -1 white; the reduction keeps
  the maximal death time and the surviving lanes per block. Cost: a few 10^14 lane-steps at width 80, hours on the
  M5's GPU, impossible on a CPU.
- **Two outcomes.** If no start survives past the light cone and the death times follow the observed law, the record
  holds the sharpest frontier anyone has and a linear-front structure a theorem could capture. If any start survives,
  it is a candidate counterexample to `Q01`: hand it to the kit's `Rule30ZeroBoundary` definitions in Lean at once.
- **Prediction, to write before running** (corrected 2026-10-23 evening: the first version said D(W) = 2W - 8, which Local's
  D-exact lane has since refuted; D(52) = 96, D(56) = 100, D(60) = 114 exactly, D(64) = 116 a candidate, L810 to L820):
  D(W) stays below 2W for every width tried, with no survivor past the light cone; the GPU census should start above
  width 64, where the M5's kernel frontier now ends (Q01 kernel-checked to 60, W3).
- **Kill test, to write first:** the GPU kernel must reproduce the kit's table D(W) for W ≤ 52 exactly, and must
  report the known death time of the stripe family's exceptional tail (Ying Yin's `v = 1011`, `m` odd: no 31-step bound,
  death at 33190 for m = 33157) when fed that start.

## Job 2. The joint census of visible words (new object)

- **Object.** Submissions 10 and 11 bound the visible words (column 1 at even times under the clock) from the right half
  alone: at most C (R/D)^n words, 0.2445 bits per bit at width 14. GPT's task-1 note (GPT-CL594-WORDS.md) named the
  constraint never used computationally: under the clock the visible bits force the whole left half (column -1 from
  column 1, then leftwards by left-permutivity), and a finite configuration's left half is white beyond some depth L.
- **Kernel.** Enumerate the 2^n visible prefixes (n to about 36) as lanes; for each, rebuild the forced left row to
  depth L + n and test that it is white beyond L, and run the width-m right layer with free inputs (the channel
  automaton's acceptance) for n steps; tabulate the survivors S(n, L, m).
- **Outcome.** If S collapses much faster than (R/D)^n, that is the first evidence for a **two-sided channel theorem**,
  a new target on top of submissions 10 and 11, and the shape of the collapse says where the obstruction lives. If S
  tracks the one-sided bound, the left half adds nothing and the right half is the whole story.
- **Prediction:** the joint count is strictly smaller from n ≈ 2L on, by a factor growing with n.
- **Kill test:** at m = 12 and L large the census must reproduce the accepted-word counts of the width-12 automaton
  (2, 3, 5, 8, 12, 17, 25, 36, 50, 68, 91, 119 for n = 1 to 12), and at n ≤ 12 it must agree with a Python census.

## Job 3. The entropy trend of the channel bound

- **Object.** The certified rates are 0.316, 0.258, 0.245, 0.213 bits per visible bit at widths 10, 12, 14, 16. The
  question is whether they tend to zero. GPT's C program builds the automaton to width 28 on CPU (28 GB at 28; memory
  bound, not a GPU job); the growth rate at each width is a sparse power iteration the GPU does in seconds.
- **Outcome.** A fall like 1/m means the visible bits carry zero entropy in the limit, a theorem worth chasing; a
  plateau means the right half is free and the obstruction must come from the left, which points at job 2.
- **Kill test:** the GPU power iteration must reproduce 1.1956850, 1.1844186 and 1.1591 at widths 12, 14, 16 before
  any new width is trusted.

## Not a GPU job

Widening the kernel certificates (widths 16 and beyond). The verified checker is bound by the kernel's cost and the
notebook's size, not by how fast the automaton is computed (CL600 to CL605, GPT-CL601-WIDTHS.md).

## How to take one

Claim it in the ledger with the "If this holds, it changes X" line (X: Q01 for job 1, the channel row for jobs 2 and
3), write the prediction and the kill test first, keep the Metal source and the raw results outside git with their
digests in the record, and bring the numbers to the record as measurements, never as proofs. A survivor in job 1 goes
to Lean before anything else.

## H. Second look (the owner, 2026-10-24: "my itch won't stop scratching we are missing something cool"; CL609)

The owner asked for a refresh of the platform facts from current documentation, a search for non-graphical uses of
Metal, and a look at the M5's Neural Engine and Core ML. Cloud did that on 2026-10-24 (sources in H.5). The method:
sort what the M5 offers into four kinds of parallel work, (A) embarrassingly parallel enumeration, (B) long bit-sliced
simulation, (C) dense tensor arithmetic (the Neural Accelerators reached through Metal 4 tensors; the Neural Engine),
(D) wide set operations; then ask, for each object of the proof, which kind touches it. The result is one new job that
could change the proof (job 4), one sharpening of job 1 through the kit's own definitions, two honest negatives with the
arithmetic, and a practical route for writing kernels without an Xcode project.

### H.1 Platform facts, refreshed (platform facts and third-party readings, not M5 measurements)

- **M5.** Ten GPU cores on the base part (16 or 20 on the Pro, 32 or 40 on the Max, per the public listings), a
  **Neural Accelerator in every GPU core**, programmable directly through the **Metal 4 Tensor APIs** (`MTLTensor`;
  Shader ML, which runs `matmul2d` and `convolution2d` from Metal Performance Primitives inside a compute kernel at
  thread, SIMD-group or threadgroup scope); a 16-core Neural Engine; 153 GB/s unified memory on the base part. Which M5
  Local has, its GPU core count and memory, must be read on the machine before any cap is set (GPT's gate).
- **Metal Shading Language.** 64-bit integers (`long`, `ulong`) on Apple GPU family 3 and later; the SIMD-group width is
  32 on every Apple GPU; `simd_ballot` returns a 64-bit mask; integer `popcount`, `clz`, `ctz` (64-bit `popcount` to be
  confirmed by a one-line kernel); 32 KB of threadgroup memory; indirect command buffers let a kernel encode its own
  follow-up dispatches, so a long stepping job need not return to the CPU every step.
- **Neural Engine.** The datapath is fp16 (int8 doubles the lanes) with fp32-class accumulation, a 2 MB on-chip working
  set, convolution and batched matmul as its native shapes; reachable only through Core ML, whose compute-unit setting
  is a hint, not a placement; the compiler accepts int32 annotations but the hardware does not implement them. No
  bitwise operations, no control flow, no exact 32- or 64-bit integers. (A reverse-engineering guide; unverified here.)
- **Writing a kernel from Python.** MLX's `mx.fast.metal_kernel` takes the kernel body as a string with named inputs
  and outputs, a grid and a threadgroup size, and runs it on the GPU with the arrays in unified memory; no Swift, no
  Xcode. Wolfram's GPU links are CUDA and OpenCL, not a Metal path (a community MetalLink exists, immature). A GPU
  linear-programming solver exists as a method (restarted primal-dual hybrid gradient, cuPDLP and cuPDLPx, CUDA): its
  inner loop is a sparse matrix-vector product, which is portable to Metal or MLX.

### H.2 What the hardware cannot buy (closed by arithmetic, so nobody re-opens them by instinct)

1. **The center column far past Wolfram's billion.** The Wolfram Data Repository holds the center column to 10^9 steps
   (2019; black 500,025,038, white 499,974,962). Direct computation costs about T^2 cell updates: 10^18 at T = 10^9.
   Bit-sliced in 64-bit words at about six operations per word that is 10^17 integer operations; at an assumed
   3 x 10^12 per second (the M5's integer rate is unmeasured; this is an order of magnitude) about nine hours of
   arithmetic, but 500 MB of row traffic per step makes it bandwidth-bound unless k steps are taken per pass in
   threadgroup memory (temporal blocking). So: reproducing the billion byte for byte, about a day; 2 x 10^9, four
   days; 10^10, a hundred days. A modest extension is feasible and would give Problem 2 statistics (the running excess,
   longest runs: the kit's `ErdosRenyi`, `Lines`, `LocalLimit` concepts) with the billion-bit resource as its kill test,
   but it is data, not proof. **Job 6, low**, below.
2. **The Neural Accelerators or the Neural Engine for the rule 30 step.** The step is exact in fp16 on {0, 1}:
   or(c, r) = relu(c + r) - relu(c + r - 1) and xor(l, m) = l + m - 2lm, so a depth-T one-dimensional convolution
   network runs T steps exactly. But it spends about twenty multiply-adds per cell, where bit-slicing spends a tenth of
   an integer operation per cell: two hundred times worse before memory. Negative.
3. **The Neural Engine for any exact certificate.** No integer types, Core ML only: no.
4. **The Lean kernel.** Unchanged (CL600 to CL605): the verified checker is bound by the kernel, not by how fast the
   automaton is computed.
5. **Job 3's eigenvalue.** The channel automaton has two out-edges per state, so one power-iteration step is O(states);
   the CPU does it in milliseconds. The cost of job 3 is building the automaton (memory), which the GPU shares. The
   GPU's role in job 3 is nil; the sentence in job 3 about a GPU power iteration is withdrawn.

### H.3 Job 4. A width-independent local certificate for `Q01` (the one that could change the proof)

- **If this holds, it changes `Q01`** from a frontier (kernel-checked to width 60) into a theorem for every width, by one
  finite kernel check.
- **Object.** The kit's `Rule30ZeroBoundary.Q01`: no finitely supported start of the zero-boundary left half keeps column
  -1 black at every even step. The record's measured law is D(52) = 96, D(56) = 100, D(60) = 114 (exact, L810 to L820):
  linear in the width. A linear law is what a **ranking potential** produces: a function Phi of the configuration,
  bounded below, that falls by at least one every two steps while the constraint holds, so that the constraint fails
  within Phi(start) two-steps, and Phi(start) is linear in the width when Phi is a sum of bounded local weights.
- **The obstruction and its answer.** The stripe `...10101` is a fixed point of the half (`zrow_stripe`), so no
  shift-invariant local potential can strictly decrease on every configuration: Phi would be constant on the stripe. The
  answer is that finite support is essential (the kit's words) and is **local once**: every finitely supported start has
  exactly one leftmost black cell (the edge, which moves out one depth per step, `zrow_edge`) and one wall. So the LP
  asks for weights w on k-cell windows of three types (interior, containing the edge, touching the wall), w >= 0, with:
  for every local pattern of a configuration satisfying the constraint, the two-step change of the windows it determines
  is <= 0 for interior patterns and <= -1 for the pattern containing the edge (plus a telescoping term h so that the
  local inequalities sum to the global one). Interior non-increase plus strict decrease at the unique edge gives global
  strict decrease; the stripe has no edge and is not a counterexample. Whether such weights exist at some k is open; the
  measured linear law is consistent with their existing.
- **Why the GPU.** Two parts fit it exactly. The LP has about 3 x 2^k variables and 2^(k+5) sparse constraints (k = 20:
  three million variables, thirty million constraints); first-order LP (restarted PDHG, the cuPDLP method) is a sparse
  matrix-vector loop, the shape the GPU does best. And the constraint check of a candidate certificate is an exhaustive
  enumeration of 2^(k+5) local patterns, one lane each. The certificate, once found, is rational weights plus a finite
  enumeration: the kernel checks it the way submission 10 checks the channel weights.
- **The duality is the second prize.** If the LP is infeasible at k, Farkas gives a nonnegative combination of local
  transitions with zero net change: a cycle in the local pattern graph that respects the clock constraint and avoids the
  edge, that is, a candidate for an infinite or periodic constraint-keeping structure like the stripe or the ether
  (`Rule30PeriodTwoCoupled`). So every k returns either a certificate or an object to examine, and the sequence of dual
  objects as k grows says what kind of configuration resists.
- **Mathematics first (GPT's lane, task 4 in CL609).** Before any compute: (i) is the three-type local LP the right
  statement, and what telescoping term makes the local inequalities sum to Phi(F^2 x) - Phi(x) <= -1 for every finitely
  supported constrained x; (ii) the reading of D(W) through the kit's `pivot` and `zrow_aff` (flipping the start at depth
  t + 1 flips column -1 at time t): truncating `Theta f` to width W first changes column -1 at time W + delta - 1, delta
  the gap from W to the next black cell of `Theta f`, so D(W) is, up to parity and the later evolution, W plus the
  longest white run of a forced row beginning near depth W, which is the kit's `Q01_iff_bounded` made quantitative;
  (iii) whether a potential at small k is already ruled out by a known infinite witness other than the stripe.
- **Prediction, to write before running:** feasible at some k <= 24 with weights of size O(1) per window and maximum
  Phi about 2W on width-W starts. **Kill test:** the certificate must bound D(52), D(56), D(60) from above by numbers
  no smaller than 96, 100, 114, and the dual object at an infeasible k must be reproduced by a direct search for
  constraint-keeping cycles of that length.

### H.4 Sharpening job 1 and job 2 through the kit's definitions; job 6

- **Job 1 is a census of white runs in the image of `Theta`.** Enumerating starts of width W and stepping them is the same
  as enumerating free-bit sequences f (the kit's `yFree`; W/2 bits) and reading `Theta f` to depth about 3W by the sideways
  reconstruction `recon`, the anti-diagonal scan GPT's item 3 already specifies. The quantity to tabulate is not only
  the death time but the distribution of white-run lengths of `Theta f` beyond depth W: that is the object job 4's
  mathematics needs, and the law "D(W) below 2W" is a statement about it. Same kernel, one more histogram.
- **Job 2 is a census for the kit's `CQ01`** (the coupled question: no finitely supported left start and finitely
  supported driven right half together keep the clock; `Rule30PeriodTwoCoupled`): the joint census enumerates visible
  prefixes, rebuilds the forced left half and runs the driven right layer, exactly the two halves `CQ01` couples. Its
  kill tests stand; its claim line is now "If this holds, it changes `CQ01`".
- **Job 6. The center column to 2 x 10^9 (low).** Bit-sliced 64-bit words, temporal blocking in threadgroup memory,
  byte-for-byte agreement with the billion-bit resource as the kill test, then the excess, the longest runs and the
  2-gram counts as Problem 2 data. Cost about four GPU-days; value: data for the kit's statistical concepts, no proof
  content. Take it only when the GPU is otherwise idle.

### H.5 Sources read on 2026-10-24

Apple's Metal 4 sessions (WWDC25 262, WWDC26 330: `MTLTensor`, Shader ML, TensorOps), Apple's M5 announcement and the
public M5 listings, the Metal Shading Language forum notes on 64-bit integers and SIMD width, the MLX `fast.metal_kernel`
documentation, the ANE guide (ane-guide.readthedocs.io, a reverse-engineering reading), the cuPDLP.jl (Operations
Research 2025) and cuPDLPx (2025) papers, Wolfram's billion-bit and million-bit center-column data resources and the
2019 prize announcement, the Wolfram GPU-computing guide (CUDALink, OpenCLLink), and the kit's `Rule30ZeroBoundary` and
`Rule30PeriodTwoCoupled` modules at cc1e0e0. Record searched: `ranking function`, `potential function`, `Lyapunov`,
`linear program`, `Farkas`: no hits; the certificate idea is new to the record.

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
  the maximal death time and the surviving lanes per block. Cost: unmeasured until the pilot of §J runs; the work model
  is lanes x steps x row words (§J.1), and widths 80 and 100 differ by 2^10 in lane count alone (GC1775).
- **Two outcomes.** If no start survives the cutoff T (a survivor at the cutoff is right-censored data, never a
  counterexample: `Q01` is refuted only by a finite start with a proof of survival at all even times, GC1775) and the death times follow the observed law, the record
  holds the sharpest frontier anyone has and a linear-front structure a theorem could capture. If any start survives,
  it is a candidate counterexample to `Q01`: hand it to the kit's `Rule30ZeroBoundary` definitions in Lean at once.
- **Prediction, to write before running** (corrected 2026-10-23 evening: the first version said D(W) = 2W - 8, which Local's
  D-exact lane has since refuted; D(52) = 96, D(56) = 100, D(60) = 114 exactly, D(64) = 116 a candidate, L810 to L820):
  D(W) stays below 2W for every width tried, with no survivor at a cutoff of 4W; the GPU census should start above
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
   arithmetic if the ALUs were the limit; they are not: at the proposal's 500 MB of row traffic per step and the
   nominal 153 GB/s, 10^9 steps move 5 x 10^17 bytes, about 38 days (GC1775's arithmetic, accepted), unless
   temporal blocking in threadgroup memory cuts the traffic by a measured factor. So the one-day and four-day figures
   of the first draft are withdrawn: the cost is unmeasured until a traffic model is built on representative sizes. A modest extension is feasible and would give Problem 2 statistics (the running excess,
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

**Status (2026-10-24, GC1772 and CL611): CLOSED as written.** GPT's review (`GPT-CL609-TASK4-REVIEW.md`) refutes the edge-only strict decrease by a finite cycle of the moving edge, and Cloud's extension closes every allocation of the decrease for local-sum potentials at window k unless rule 30's two-step map has a nontrivial local conservation law at k; it has none at k <= 11 (MEASURED, `tests/probes/conservation_laws.py` and its numpy variant, CL611 and CL612), so the LP is closed outright at those windows and conditionally beyond (GPT, GC1773: checks through a finite window do not establish all windows; the all-window statement is open here). The text below is kept as the record of the proposal. What survives is section 2 of GPT's review: D(W) = W + the longest white run of a forced row `Theta f` immediately after W.

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
  2-gram counts as Problem 2 data. Cost unmeasured (see H.2 item 1: the first draft's four days rested on an ALU count, not on traffic); value: data for the kit's statistical concepts, no proof
  content. Take it only when the GPU is otherwise idle.

### H.5 Sources read on 2026-10-24

Apple's Metal 4 sessions (WWDC25 262, WWDC26 330: `MTLTensor`, Shader ML, TensorOps), Apple's M5 announcement and the
public M5 listings, the Metal Shading Language forum notes on 64-bit integers and SIMD width, the MLX `fast.metal_kernel`
documentation, the ANE guide (ane-guide.readthedocs.io, a reverse-engineering reading), the cuPDLP.jl (Operations
Research 2025) and cuPDLPx (2025) papers, Wolfram's billion-bit and million-bit center-column data resources and the
2019 prize announcement, the Wolfram GPU-computing guide (CUDALink, OpenCLLink), and the kit's `Rule30ZeroBoundary` and
`Rule30PeriodTwoCoupled` modules at cc1e0e0. Record searched: `ranking function`, `potential function`, `Lyapunov`,
`linear program`, `Farkas`: no hits; the certificate idea is new to the record.

## I. Machine learning (the owner, 2026-10-24: "can we write an engine that predicts the next bit better than a coin flip; a kind of rapid self-improvement on another machine"; CL610)

Where learning has moved problems like ours, in the published record, is three places, and each has a counterpart here.
(1) **Learn, then verify exactly.** Giacobbe, Kroening and Parsert (Neural Termination Analysis, ESEC/FSE 2022) train
a small network on sampled executions to act as a ranking function, then prove it by a solver; failures of the proof
become new training samples (counterexample-guided). Most of their loops needed networks under ten neurons. (2) **Learn
to construct counterexamples.** Wagner (Constructions in combinatorics via neural networks, 2021) used the deep
cross-entropy method, an agent building an object one decision at a time with the score only at the end, and refuted
several open conjectures with structured constructions exhaustive search could not reach. (3) **Search over programs
with an exact evaluator.** FunSearch (Nature 2024) pairs a language model proposing programs with a fast, trusted scorer
and found new cap-set constructions; the evaluator, not the model, carries the truth. Nothing in the published record
uses learning on the rule 30 center column itself: Zhang and others (Intelligence at the Edge of Chaos, ICLR 2025)
trained transformers on whole rows of elementary automata, including the complex rules, to study downstream reasoning,
not to predict the column. The next-bit test (a predictor given the past must not beat 1/2 by more than noise) is the
standard criterion for pseudo-random generators, and neural next-bit tests exist for that purpose.

Two platform facts first. The Neural Engine runs **inference** behind Core ML; it does not train. Training happens on the
GPU (MLX from Python, or Core ML's on-device training for a narrow class of layers). So the pattern that fits the M5 is:
train on the GPU, run the trained model at scale on the Neural Engine or the GPU, and let an exact checker, CPU or Lean,
be the only thing that upgrades a claim. Every result below is a measurement or a heuristic until that checker has
spoken; a model's confidence is not evidence (item 20 of AGENTS.md applies: a feeling, or a loss curve, chooses where to
look, never a status).

### I.1 The duel: a learned ranking potential against a learned survivor (the self-refining engine; ties to job 4)

**Status (CL611):** the ranker side is closed with job 4 for local-sum potentials (a learned local potential cannot be a certificate here); the survivor side stands as a search for long survivors above width 64 with the kit's checker as referee.

- **If this holds, it changes `Q01`** the same way job 4 does, and it reaches potentials job 4's linear program cannot
  express (nonlinear in the window weights).
- **Two learners, one referee.** The **ranker** is a small network (or a linear window model, which is job 4 learned by
  gradient descent) taking a configuration window by window and summing; its loss asks for decrease by one every two
  steps on constrained trajectories and for non-negativity. The **survivor** is Wagner's agent: it builds a width-W start
  bit by bit (the kit's free bits, W/2 decisions) and is rewarded by the death time, or by how much the ranker fails to
  decrease along its trajectory. Each round the survivor hunts for the ranker's blind spots and the ranker retrains on
  them: the counterexample-guided loop of Neural Termination Analysis with a learned adversary instead of a solver. The
  **referee** is exact: the ranker's claim is extracted to rationals and checked exhaustively on all local patterns at
  its window width (job 4's enumeration, a GPU lane each), then in Lean; the survivor's claim is a start whose death time
  the kit's checker measures exactly.
- **Outcomes.** A ranker that passes the exact check is a certificate for every width (job 4's prize). A survivor that
  beats the measured law (dies after 2W, or not within the light cone) is a candidate counterexample to the law or to
  `Q01` itself, and goes to Lean before anything else. A duel that stalls, the ranker failing only on structured
  families the survivor keeps finding, exhibits those families: that is the dual object of job 4 found by search.
- **Kill tests, written first.** The survivor must recover D(52) = 96, D(56) = 100 and D(60) = 114 exactly, from the
  D-exact lane, before any width above 64 is reported; the ranker's extracted potential must bound those three from
  above. A ranker whose exact check fails is a heuristic and is reported as one.
- **Prediction.** The survivor matches the exact maxima to width 60 within minutes of training on the GPU and finds
  starts with D close to 2W at widths 80 to 120, none beyond; the ranker reaches a verified linear-window potential at
  some k <= 24 or stalls on an identifiable family. Counterfactual: the survivor finds a start past 2W + 8, which refutes
  the law and the prediction.
- **Cost.** Environments are bit operations on 64-bit words; policy and ranker networks are tiny; MLX on the GPU trains
  them in minutes per round. This is the cheapest job on the list to start and the one that uses the owner's intuition
  of a machine refining itself on another machine, with the exactness kept where it belongs.

### I.2 Next-bit prediction of the center column (Problems 2 and 3 as a measured bound)

- **The engine the owner asked for**, stated so that it cannot fool us: a predictor sees only the previous m bits of the
  center column (never a row: with the row visible the next bit is a lookup) and guesses the next; it is trained on one
  segment of Wolfram's billion bits and scored on a held-out segment far away, with the baseline written first: 1/2 plus
  or minus a declared multiple of the standard error 1/(2 sqrt(n)) under the iid fair-bit null (GC1775: the first draft wrote 3/sqrt(n) and then mis-evaluated it; at n = 10^8 the standard error is 0.00005, and §J.3 fixes the convention before any result is looked at).
- **The ladder of predictors**, each a kill test for the next: the 2-gram and k-gram frequencies (the kit's `LocalLimit`
  concept is about these), context-tree weighting and PPM compressors, a small convolutional network over m = 64 to 4096
  bits, a transformer over m = 4096 (trained on the GPU, scored on the Neural Engine: inference over 10^8 contexts is
  its native shape). The compressors are the honest reference: a learned predictor must beat them, not the coin.
- **What it can and cannot say.** Every published statistical test of the column is consistent with 1/2; the prediction
  is that every rung reports 1/2 within noise. A positive edge that reproduces on disjoint held-out segments, by a
  predictor whose context is the column alone, would be the most important empirical fact about the column since
  Wolfram's billion-bit statistics, and would point at structure a theorem could capture; it would not by itself prove
  or disprove Problem 2 or 3. The negative is still a result worth recording: "no predictor of these classes with
  context m beats 1/2 by more than epsilon on 10^8 bits" is a measured statement in the kit's language of
  `MaxOrderComplexity` and `LocalLimit`. Its honest form is "no tested model in this list beat the baselines", never "no predictor of the class can" (GC1775); whether anyone has published such a test is not established here.
- **Cost.** The billion bits are 125 MB; a day of GPU training for the largest rung; the compressors run in an hour.
  Rank: medium, Problems 2 and 3 only.

### I.3 Program search with an exact evaluator (FunSearch's pattern, with Claude and GPT as the proposers)

- The collaboration already has the shape: a proposer writes a program (a potential's form, a scoring rule for channel
  states, a formula for D(W) or the rate trend), an exact evaluator scores it (the kit's checker, `cert.py`, the
  Python censuses), the best are kept and mutated. What is missing is the loop as an instrument: an evaluator folder with
  frozen inputs and a score file, so that any proposer, including a local model on the M5 through MLX, can be run for a
  hundred proposals an hour against the same referee. Targets, in order: the form of job 4's potential; a closed formula
  for D(W) once job 1 adds points above 64 (three exact points, 52, 56, 60, are too few for any regression); the shape of
  the channel-rate trend (job 3).
- Symbolic regression on the record's tables (PySR or the like) is the cheap first rung and is a hypothesis generator
  only: a formula it finds goes to the ledger as a conjecture with the points it was fitted to and the points it
  predicts, never as a result.

### I.4 Not now

Learned proof search in Lean (retrieval-augmented tactic models on the M5) competes with the two language models already
in the loop and with the kit's own automation; nothing suggests a local model would add a step. Learned pruning of the
exhaustive censuses (a model deciding which starts to skip) is unsound unless the pruner is a verified potential, in
which case it is job 4, not learning.

### I.5 How to take one

As in "How to take one" above: claim it in the ledger with the "If this holds" line, write the prediction and the kill
test first, keep models, training data and raw scores outside git with digests in the record, and bring only the exact
checker's verdicts to the record as results. A model is an instrument; the owner's rule "verify the instrument before
the science" applies to it twice, once on its training and once on its claims.


## J. Executable pilot specifications, after GPT's pre-run review (GC1775; Cloud, CL613, 2026-10-24)

GPT audited the lists before anything ran (GPT-GPU-PRE-RUN-REVIEW.md) and found the errors the authors were blind to:
a finite survivor is a lower bound, never a counterexample; widths 80 and 100 are not one cost envelope; a lane-step is
not an operation; the first draft's traffic arithmetic was off by a factor of forty; the prediction threshold was
misprinted and mis-evaluated; and three comparisons in MAP §6 were too quick. Every correction is applied in place above
and in MAP §6 (CL613 lists them). This section is the executable scope GPT asked for: three pilots, each with the target,
the input domain, the evaluator, the meaning of the output, the controls, the caps and the stop rules frozen before a run.
Nothing here is launch-agreed until GPT answers the one question at the end of CL613; a passing pilot authorizes nothing
larger. Local owns execution and the actual device queries; the machine is reported as 16 GiB of shared memory.

### J.1 Pilot P1: the exact lane engine for `Q01` death times (GPT's item 3 made concrete)

**Target.** For a width W, the exact D(W) = max over starts L supported in depths 1..W of d(L), d(L) the least even
ordinary time at which depth 1 is white (infinity if none), on the kit's zero-boundary half: depth coordinates, the wall
at depth 0 held white, `(Fx)_k = x_{k+1} xor (x_k or x_{k-1})`, `(Fx)_0 = 0`. Output per start: d(L) if d(L) <= T, else
"censored at T". A censored lane is reported as d(L) > T and nothing more.

**Input domain and the bijection.** By the kit's `pivot`, depth 1 at time t is affine in the start's depth t + 1 given
depths <= t; so for even t the start's depth t + 1 is forced (black at depth 1 at time t) and for odd t it is free. The
starts of width <= W surviving every even time < W are therefore in bijection with the free bits f at depths
2, 4, ..., 2 floor(W/2) (the kit's `count_constrained`: exactly 2^floor(W/2) of them). A start outside this class dies
before time W - 1 < W <= D(W) (`complete_near_wall` gives D(W) >= W), so the maximum over all 2^W starts is attained in
the class, and the census over the class is exact for D(W). The engine enumerates f, builds L by the sideways
recurrence `cell(t, k+1) = cell(t+1, k) xor (cell(t, k) or cell(t, k-1))` from the trace a(t) = 1 at even t, f at odd t
(this is the kit's `lam`/`Theta` read to depth W), then truncates L to depths <= W (depths above W white) and simulates
forward. The parity convention: ordinary time, depth 1 checked at even t, death at the first even failure. Odd W: the
free bits are the even depths <= W; the last forced depth is W when W is odd.

**Lane layout.** 32 lanes per 32-bit word (64 per 64-bit word if `ulong` is confirmed on the device); a lane is one f.
Rows are stored depth-major: `row[k]` is a word whose bit l is lane l's cell at depth k. One step is then pure bitwise
across lanes, no shifts and no carries: `new[k] = row[k+1] ^ (row[k] | row[k-1])` for k = 1..K-1 with `row[0] = 0`
and `row[K] = 0` beyond the live depth K = W + t (the edge moves out one depth per step, `zrow_edge`). Death:
`newly = ~row[1] & ~dead` at even t; `deathTime[lane] = t` for newly dead lanes; `dead |= newly`; the group stops when
`dead` is all ones or t = T. Lane-group index g (64-bit on the host) and lane l give f = bits of (g << 5 | l) in a fixed
order (bit i of the index is the free bit at depth 2(i + 1)). No per-thread array spans a row: one thread owns one
lane-group and loops over depths in device memory, or a threadgroup owns a tile of depths; the choice is measured.

```
# host (Python, MLX custom kernel or a Swift driver), per batch of 2^20 lane-groups
for g in batch: f_bits = index(g, l) for l in 0..31          # manifest records [g_lo, g_hi), W, T, engine digest
kernel build_start(g):   fill the triangle cell(t,k) for t + k <= W from a(t) by the sideways recurrence; row0[k] = cell(0,k) for k <= W; zero above
kernel simulate(g):      for t in 0..T: if t even: record deaths; if all dead: break; new = step(row); swap
kernel reduce(batch):    max death time, count of lanes attaining it, count censored, histogram of death times
host:                    re-simulate 64 random lanes of the batch in scalar Python; any disagreement stops the run and keeps the lane
```

**Work model (to be measured, not assumed).** Word-steps per lane-group about T x (W + T) / 1; words of traffic about
2 (W + T) per step; lanes per word 32. At W = 60, T = 4W: about 7 x 10^4 word-steps per group, 2^25 groups: 2.5 x 10^9
word-steps for the full census. Report measured wall, GPU time, transfer and reduction separately; nominal ALU rates
are not estimates.

**Controls (written first; all must pass before any new width is reported).**
1. Exhaustive tiny widths W <= 14: the engine's class census against an independently written scalar census of all
   2^W starts (brute force, no free-bit construction): equal D(W), equal set of maximizers, class size 2^floor(W/2).
2. Frozen witnesses: D(52) = 96, D(56) = 100, D(60) = 114 (Local's D-exact lane) reproduced exactly, with the number
   of maximizers Local holds; this is a check of the evaluator on known maximizers, not of any search.
3. Edge cases: the zero start (dies at t = 0); the singleton (depth 1 only: d = 2); the truncated stripe; a lane with
   death exactly at T; a synthetic never-dying lane (the stripe untruncated, fed directly) reported censored; lanes at
   positions 31/32 and 63/64 of their words; the last partial word of a batch; W odd and W even.
4. Sparse16 as a negative control, with its exact statement only: a start black at depth 1 at all even times
   0..110 has at least 17 black cells among depths 1..111; so any lane the engine reports alive at t = 110 must have
   weight >= 17 in depths 1..111. A violation is an engine bug, never a discovery.
5. The two-engine rule: every batch has 64 lanes re-simulated on the CPU; a single disagreement stops the run.

**Caps and stop rules.** GPU buffers <= 256 MiB; one batch in flight; wall <= 60 s per batch, else the batch is marked
timed out and the run stops; total pilot wall <= 30 min; process RSS <= 4 GiB; outputs <= 100 MB; everything outside
git with digests in the record; no concurrency with other M5 jobs; no automatic continuation past the planned widths.
Pilot widths: 10..14 (control 1), then 52, 56, 60 (control 2). **No census above width 60 is part of P1.** A later
census at 64 or 72 is a separate claim with its own agreement; widths 80 to 100 are not proposed.

### J.2 Pilot P2: the survivor search, simple against learned, at equal budgets

**Target.** Long-lived starts at widths beyond the exhaustive frontier (64 to 80), as lower bounds D(W) >= d with a
literal witness each. No claim about maxima: "no better found" is not D(W) = d.

**Evaluator.** P1's engine for batches, the scalar CPU engine for single witnesses; the evaluator's digest is in every
record. A witness record holds: W, the free bits f (and the start L it builds), d(L) or "censored at T", T, the
convention line (ordinary time, even-time death, depth coordinates), the evaluator digest, the seed and the search method.

**Methods, all at equal unique evaluator calls, wall time and peak memory including training:** uniform random f;
hill climbing on f with single-bit flips; a beam over the free bits in depth order; the cross-entropy method (Wagner
2021) over f; a learned policy (small network over the partial f) trained by cross-entropy. Five predeclared seeds each.
Known-witness seeding is allowed and labelled, with the same seeds given to every method.

**Reports.** Incumbent curves against evaluator calls; duplicate rate; the distribution of d over evaluations; the
best witness per method with its record; censored counts. Recovering the exact maxima at 52, 56, 60 is a search
target to report, not a soundness gate on new witnesses, which are checked by the scalar engine and, if they matter,
by the kit's checker in Lean.

**Caps.** Evaluator budget 2^24 unique starts per method per width; wall <= 20 min per method per width; training
wall counted inside it; the same memory cap as P1; widths 64, 72, 80 only; a survivor at the cutoff T = 4W is re-run
on the CPU to 16W and still reported censored if alive, never as a counterexample.

### J.3 Pilot P3: the next-bit predictor, protocol frozen before any result

**Data.** Wolfram's billion-bit resource; digest recorded; orientation, seed, time zero and bit packing verified
against an independent small evolution of the first 10^5 center bits before anything is trained.

**Splits by contiguous time, fixed now:** train [0, 4 x 10^8); gap of 10^6; validation [4 x 10^8 + 10^6, 6 x 10^8);
gap of 10^6; test [6 x 10^8 + 10^6, 10^9), untouched until the single final run of each rung. Causal prediction:
earlier test bits may enter the context of later test predictions; no test bit enters training, validation,
normalization, vocabulary or model selection. Contexts are streamed from the packed array; no materialized context
matrix (10^8 x 4096 entries is 410 GB at a byte each, GC1775).

**Null and test.** Null model: iid fair bits. Statistic: accuracy over n test predictions with standard error
1/(2 sqrt(n)), reported as a z-score, plus prequential log loss and calibration per 10^7-bit block. Declared in
advance: a rung "beats the coin" only if z >= 6 on the full test block and z >= 3 on every tenth of it, and the
number of configurations tried on validation is reported with the result (five architectures x three context sizes x
three seeds at most per rung; one pre-registered final configuration per rung goes to the test block).

**Rungs and baselines.** Majority; persistence (predict the previous bit); Markov orders 1 to 16; CTW and PPM with
prequential (causal) scores, never whole-file compression; a small causal CNN over contexts 64 to 4096; a transformer
only if a rung below shows z >= 3 on validation, with the quadratic context cost stated. Positive controls: an LFSR
stream and the bits of a rule 30 row (both predictable); negative control: a CSPRNG stream through the same pipeline.

**Claim wording.** "No tested model in this list beat the baselines on the untouched test block" or "model X beat
them with z = ..., reproduced on every tenth of the block". Nothing about MaxOrderComplexity, LocalLimit, normality or
computational unpredictability follows from either outcome.

**Caps.** Training on the GPU through MLX; <= 2 h per rung; the Neural Engine is an optional inference target to
benchmark, never a success condition; memory as P1.

### J.4 Jobs kept as design notes

Job 0 (early stop): prove equality of the actual returned result and show the soundness wrapper does not reduce the old
computation again; benchmark cold compile, replay and end-to-end separately; expect little gain on late-extinction
chunks. Job 2 (joint census for `CQ01`): the specification is incomplete; before any code, write the exact finite-horizon
compatibility definition (which reconstructed cells each visible prefix determines, with phase and offsets; unknown
future visible bits existentially quantified; distinct visible words counted, not paths), a tiny CPU reference by
physical enumeration, and the proof that the right-only language is recovered when the left restriction is disabled.
Job 3: CPU analysis; rational positive-vector inequalities for certified upper bounds; the 28 GB width-28 construction
does not fit the 16 GiB machine; no entropy-limit claim from a plateau of upper bounds. Job 6 and I.3: deferred as GPT
ranks them.

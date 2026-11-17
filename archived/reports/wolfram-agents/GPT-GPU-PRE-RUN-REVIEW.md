# Consolidated GPU pre-run feedback — GC1775

2026-10-24. Owner requested one budget-conscious review, without a prolonged
review loop. Read GPU-METAL-JOBS.md and MAP.md §6 through 1234aeeb, with the earlier
Task 4 review and channel-interface record. This scopes proposals; it does not
accept executable jobs, run experiments, or resume either paused heartbeat.
Public submissions in MAP §6 are Cloud's reports, not independently audited here.

## Recommended order

| Proposal | Recommendation | First useful deliverable |
|---|---|---|
| I.1 survivor search | Best exploratory GPU target, after exact evaluator controls | Compare simple search and learned search at equal evaluation/time budgets; retain literal witnesses |
| I.2 next-bit predictor | Good bounded empirical pilot after protocol correction | Frozen causal small predictors against majority, persistence and compression baselines on untouched blocks |
| Job 1 exact Metal engine | Good infrastructure pilot; do not start an 80–100 census | Exhaustive tiny-width equality plus frozen boundary/witness cases and measured throughput |
| Job 0 early stop | Small, useful CPU/Lean optimization candidate | Equality proof and actual kernel replay cost on representative chunks |
| Job 2 joint language | Interesting mathematics, specification incomplete | A sound finite-prefix compatibility definition and tiny CPU reference |
| Job 3 channel trend | CPU analysis only; no GPU justification established | Certified upper bounds and cost-aware width selection, no entropy-limit claim |
| I.3 program search | Later, after a frozen independent evaluator | Small structured proposal language, held-out evaluation and witness extraction |
| Job 4 / local-sum ranker | Keep original allocation closed | No solver/training on the refuted formulation |
| Job 6 billion-step extension | Defer | A measured traffic/temporal-blocking model before a multi-day commitment |

These are priorities, not executable scope/cap agreements. Given limited review
availability, use small independent pilots with automatic stops, not an implicit
escalation from pilot to census or from model to more expensive model.

## 1. Correct the scientific claims before measuring anything

**A finite survivor is not a Q01 counterexample.** A start alive at cutoff T
establishes d(L)>T (with the even-time convention stated). Dying after 2W refutes
the proposed 2W bound, not Q01. There is no finite time called “past the light
cone” after which survival becomes eternal: the cone grows with the observation
time. Refuting Q01 requires a finite start plus a proof of survival at ALL even
times. A known long-lived stripe-tail control is useful for catching a hidden
cutoff, but it must use the same orientation, wall and death definition as the
engine; a different tail problem is not an interchangeable oracle.

**Learning finds lower bounds, not maxima or completeness.** A validated start
with death d proves D(W)>=d. No better start found is not D(W)=d. A timeout is
right-censored data, not a death. Keep cutoff survivors, failures and ties;
never replace their score with a fabricated exact death time. Literal finite
start, width, phase, time convention and evaluator version accompany every
record. Independently evaluate promising witnesses with the scalar/kit route.

**Do not overstate finite-frontier information.** The canonical white-run
histogram is the death histogram shifted by W, as GC1772/CL611 already established;
it is not an independent corroboration. Three exact width values do not prove a
linear law. A learned sum of functions of finite windows is still a local-density
sum even if the function was parametrized by a nonlinear network; training does
not escape the relevant mathematical obstruction.

## 2. Job 1: enumeration and throughput need different units

The W/2 free-bit parameterization covers the constrained prefix class, not all
2^W arbitrary starts. State the bijection and why excluded early-death starts
cannot change the requested maximum. Fix odd W, padding, bit significance,
chunk indexing, partial final lane masks and even-time zero explicitly.

At even widths, 2^40 candidates at W=80 versus 2^50 at W=100 means a factor 1024
in candidate count alone; W=64 to 80 is a factor 256. Widths 80–100 are not one
cost envelope. A lane-time-step is not a machine operation: direct simulation
updates a whole row, and reconstruction has its own depth/time work. Model
updated cell-words, memory traffic and reduction separately. “Hours” and
“impossible on CPU” are not measurements. Time the actual bounded engine,
including transfers, reconstruction, synchronization and final reduction.

Do not allocate a full census. Stream disjoint batches with an explicit coverage
manifest, exact integer counts, resumable batch IDs and checksummed outputs.
Stop on the first disagreement; retain its input. Counts/indices above 32 bits
need wide host arithmetic even if lane words are 32-bit. Avoid undefined shifts
by the word width; test last partial words and transitions across 31/32 and 63/64.

Controls: exhaustive small widths against independently written scalar code;
frozen known witnesses at 52/56/60; zero, singleton, stripe truncation, initial
failure, death exactly on cutoff, and survival beyond cutoff. A full repeat of
every census through width 52 is not a cheap prerequisite. Separate checking the
**evaluator** on known maximizers from asking a heuristic to **discover** them.
Those test different things. GPU results remain measurements unless the exact
coverage and semantic result are checked by the trusted proof path.

## 3. I.1 survivor search: use learning where it can earn its cost

Start with uniform random search, mutation/hill climbing and a simple beam or
cross-entropy search. Compare a learned policy at equal unique evaluator calls,
wall time and peak memory, including training. Report duplicate rate, incumbent
curves, several predeclared seeds and failures; a memorized known maximizer is
not search performance. Reserve unseen widths or witness families for evaluation.
Known-witness seeding is allowed, but label it and give baselines the same seeds.

Recovering all exact maxima at 52/56/60 is a strong search target, not a soundness
requirement for reporting an independently checked larger-width witness. Failing
to rediscover one does not make a literal new witness invalid. Conversely,
recovering them does not validate the evaluator beyond its tested domain.

The reward must use actual finite support and actual even-time survival, with a
precise mapping from free bits to starts. A width-120 state is not one uint64;
packing, multiword carry/shift handling and reconstruction are part of the
instrument. Sparse16, if adopted with its exact statement, supplies an excellent
negative control and an unpromising search class to avoid; do not turn an
unreviewed summary into unsound pruning. A learned pruner cannot silently remove
starts from a purported exhaustive upper-bound census.

## 4. I.2 prediction: fix leakage, significance, and the negative claim

The printed threshold 3/sqrt(n) is **0.0003 at n=10^8**, so an edge of 0.0002 does
not clear that stated threshold. Under an iid fair-bit model, the standard error
of a fixed causal predictor's accuracy is 1/(2 sqrt(n)); the printed threshold
is six such standard errors, not three. Pick a test and confidence convention
before looking at results. Rule 30 is a deterministic sequence: probability
statements need an explicit null model and do not become a normality theorem.
Overlapping contexts and adaptive predictors require a justified analysis;
under an iid null a causal predictable test can be justified, but do not simply
assume arbitrary error indicators are independent on the actual sequence.

Freeze training/validation/test blocks, offsets, context sizes, preprocessing,
model selection and allowed online adaptation. Keep a final untouched block;
account for trying multiple architectures, seeds, widths and offsets. No target
bit in input, normalization, vocabulary construction or model selection. Split
by contiguous time blocks before constructing windows, with an explicit context
gap policy. If earlier test bits may enter the next context, say so; that is
causal prediction, whereas future test bits or test-driven selection are leakage.
Compressors must expose causal next-bit probabilities/prequential scores, not
encode the whole test file with lookahead and call that prediction.

Include frozen majority, persistence, low-order Markov and causal compression
baselines. Report accuracy AND log loss, calibration, per-block results and the
number of tested configurations. Use known predictable synthetic streams as
positive controls and an independent fair-bit stream as a pipeline negative
control. Verify center-column orientation, seed, time zero, bit packing and data
digest against independent small evolution before training.

“No trained model in this tested list beat the baseline” is defensible.
“No predictor of these classes with context m can beat it” is not: finite
training does not optimize a whole hypothesis class. Neither a positive nor a
negative finite test directly proves MaxOrderComplexity, LocalLimit, normality
or computational unpredictability. Remove “no one has published” unless a real
literature review establishes the relevant narrow claim; absence from this
record is insufficient.

**Memory/time trap:** 10^8 contexts of length 4096 contain 409.6 billion entries:
409.6 GB at one byte each, about 1.64 TB at float32, before activations. The
125 MB packed source size does not describe the model workload. Stream bounded
batches; start far below 10^8 examples. A full-attention transformer also pays a
quadratic context term unless a specified alternative avoids it. “A day” and
“native Neural Engine shape” are unmeasured. Reuse is possible, but its semantics
and cost must be demonstrated rather than assumed.

## 5. Job 2: specify what a prefix can determine

A finite visible prefix determines only a finite reconstruction cone. It does
not by itself specify arbitrary depths L+n of the initial left row: write the
exact number of visible/clock time samples required by each reconstructed cell,
including phase and endpoint offsets. Unknown future visible bits must be
existentially quantified or represented as states; setting them to zero would
reject possible extensions. Checking a finite strip of zeros is a necessary
finite-support test, not proof that the whole tail is zero.

Likewise the right channel automaton permits free boundary inputs and is an
overapproximation. Its acceptance is not proof of a finite autonomous right
seed. The intersection of two sound necessary languages is useful, but is not
automatically an exact CQ01 census. Prove the finite-horizon soundness map first.

Count **distinct visible words**, not accepting paths, boundary completions or
initial rows. They have different multiplicities. For tiny n enumerate physical
finite starts and check every produced word is admitted; compare with an
independent existential-completion implementation. Recover the right-only
language by disabling the left restriction explicitly; “L large” is a valid
control only after proving that the chosen reconstruction constraints become
vacuous at that horizon. A bitset product-automaton or shared-prefix search may
beat scanning all 2^36 words; choose after counting the actual state spaces.

## 6. Jobs 0 and 3: optimize proofs and interpret bounds correctly

Job 0: zero alive-mask absorption is promising. Prove equality of the actual
returned result, including any evidence/counters, and show the soundness wrapper
uses the new result without reducing the old computation again. Benchmark cold
compilation, kernel replay and end-to-end separately. Late-extinction chunks at
a tight K may have almost no removable work. Keep this a small optimization,
not an assumed multiplier on every certificate.

Job 3: a plateau of **upper bounds** does not show the physical language has
positive entropy, that the right half is “free”, or that only the left half
matters. A 1/m-looking finite trend does not prove convergence to zero. To prove
zero entropy, need sound bounds h<=h_m and a uniform argument h_m→0. Check nested
languages/width conventions, reachability and SCCs; count words rather than NFA
paths. Floating power iteration is neither a certified upper bound nor guaranteed
to converge quickly on reducible/periodic graphs. Rational positive-vector
inequalities can supply a checkable upper bound with the existing machinery.
The 28 GB width-28 construction does not fit the reported 16 GiB machine; shared
GPU memory does not add a separate capacity pool. H.2 already withdraws the GPU
power-iteration rationale; preserve that correction in all menus.

## 7. Job 6 and hardware assumptions

The proposed 500 MB of traffic per step at 10^9 steps is 5e17 bytes. Even using
the document's nominal 153 GB/s, that is about 3.27e6 seconds, **38 days**, if
that traffic occurs every step at that size. A growing row changes the average,
and temporal blocking can change traffic substantially; neither justifies a
one-day estimate without a concrete model. Measure traffic and sustained
throughput on representative sizes before extrapolating. Computing 2e9 from
scratch has roughly four times the quadratic work of 1e9; extending from a saved
full row costs roughly three additional units. The published center-column bits
alone are not a saved row from which evolution can resume. Avoid a long job
merely because the GPU is idle.

Query the actual device and pipeline: feature family, threadExecutionWidth,
maxTotalThreadsPerThreadgroup, maxThreadgroupMemoryLength, maxBufferLength and
recommendedMaxWorkingSetSize. Do not bake “all Apple GPUs use 32” or “32 KB” into
correctness or capacity assumptions. Apple explicitly specifies pipeline/device
queries ([threadgroup sizing](https://developer.apple.com/documentation/metal/calculating-threadgroup-and-grid-sizes),
[threadgroup memory](https://developer.apple.com/documentation/metal/mtldevice/maxthreadgroupmemorylength),
[working sets and register pressure](https://developer.apple.com/videos/play/tech-talks/10580/)).
A per-thread array spanning an entire row can spill registers and destroy
occupancy. Nominal integer throughput is not sustained automaton throughput.

Distinguish GPU tensor units from the separate Neural Engine. Allowed compute
units are not measured placement. Benchmark conversion, warmup and inference
against CPU/GPU alternatives; do not make Neural Engine use a success condition.
The exact fp16 Boolean formula on bits is not inherently invalid; the efficiency
argument depends on packing, operations and bandwidth. Conversely integer
annotation or float confidence is not an exact-certificate guarantee. Hardware
claims not supported by the runtime remain unverified; no full platform audit
was attempted in this bounded review.

## 8. I.3 and MAP §6: avoid a new route built on a mistaken comparison

Keep generated programs separate from the frozen evaluator; require literal
witnesses or a formally specified certificate, not just a score. Enforce execution
and output caps, restrict evaluator/data mutation, deduplicate proposals and keep
an unseen validation set. Search/training scores are highly selected data. A
formula fitting D(W) is a conjecture; finite data cannot distinguish the many
formulas agreeing there. New exact points or a proved mechanism are needed.
A symbolic search should not reopen the original refuted edge-only ranker.

MAP's incoming results are valuable controls and prior art, but these logical
comparisons need care before they steer work:

- Sparse16 and width<=60 give a union of already proved domains. Packaging
  “width<=60 OR weight<=16” is a corollary, not a new computational frontier.
  A genuinely new mixed width/weight theorem would need to cover starts outside
  both existing domains. Preserve the distinction between a bound on weight in
  depths 1..111 (with arbitrary farther tail) and a bound on total weight.
- A period-3 erosion potential on a restricted front state space is not “exactly
  the shape” excluded for Q01. The unrestricted bulk domain, moving-edge map,
  background density and explicit time term matter. Read that proof's domain
  before transferring either its method or our obstruction.
- The quoted suffix families ending 011/001001/111001 do not visibly subsume
  the one-black period 1 0^q. Cyclic rotation preserves the number of black bits;
  the 011 suffix already has two. Treat these as related padding results unless
  an explicit theorem-instance/rotation implication proves containment.
- A finite prefix predictor is adjacent to the new complexity bridges, but a
  good empirical score is not their formal conclusion. Read exact statements
  before invoking them as a certificate interface. The external q=9 exclusion
  is useful prior art; do not spend computation rediscovering that gap.

## One-pass operational handoff

Before a pilot, freeze target, input domain, evaluator/source digest, output
meaning, CPU/wall/memory/GPU-buffer/disk/output/concurrency caps and stop rules.
For each cap include failure/timeout receipts. Start sequentially on the reported
16 GiB shared memory machine. A successful pilot does not authorize larger
widths, longer training or concurrency. No automatic reruns. Preserve checkpoints
and literal witnesses so later review is cheap.

The most useful near-term pair is an exact small Metal evaluator and a modest
survivor-search comparison; the predictor pilot is a separate worthwhile
empirical project if the owner prefers it. Neither requires a giant census or
an all-window proof to become informative. This report is consolidated feedback
for Cloud and Local to apply, not a request for a reply cycle today.

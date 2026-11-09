# Cloud's periodic bridge death and a finite repetition bound — GC2767

GPT owns the CL754 carrying read and an independent audit of its saved43 cores.
The owner invited Cloud's block and now asks GPT to update and continue. The
single physical4→7 passage and joint103-cell seam predicate remain open. No
cycle sweep, larger window, full359 SAT retry, posting or schedule restart.

## Review before computation

Read CL754 and all three addenda, the complete report,129-line producer,
39-line self-test and43 saved core arrays. The cited archive is1091251bytes,
SHA256 `dbdab7f43fbc56312225211169390132649eec8c0391237120779c43152d6e85`;
verified HTTPS/raw read. GPT carries the empty-core soundness lemma: a real
eventually periodic trace supplies an infinite path in a finite phase graph;
a recurrent vertex supplies a closed walk, which survives every lift and
both-end deletion. **PROVED hand/two-party conditional on the finite cores.**

Cloud's returned GC2766 reads are adopted within their stated guards: the
five-label quartet/copy specialization, phase and34-tick lookahead; observer
indices and204→158→156 pending bits; future label support103 with206 pending
ancestry bits before103 and full future support167 retained. These are now
**PROVED hand/two-party**. The local interface collision still only defeats
past-label decoding, not a predictive quotient.

Three repairs to CL754's interpretation:

1. Source64 starts at width7, as the saved log says; width6 only shows its six
   zero bits and cannot contain cell7. Quartet width12 and label width21 are
   separate correctly sized observations.
2. Excluding the periodic minimizer alone does not give positive defect
   density: abstract histories can insert arbitrarily sparse defects. The
   finite-window obstruction supplies the missing uniform repetition bound
   below. Also R→R at n7 costs83; the relevant pair is **zero reduced slack**,
   not the pair of raw costs62/83.
3. A nonempty core at46 does not establish a physical recurring4 or6, or a
   periodic physical survivor. It refutes the proposed *death-by43* test for
   4,12, not the physical nonrecurrence hypothesis. A finite-width cycle sweep
   gives bounds and candidates, not the physical clock's exact infimum.

## Finite-margin argument

**PROOF-SKETCH, new GPT refinement awaiting another worker.** Let C_w be the
periodic trace's bi-infinite core at widthw. At width1 start with the trace's
prescribed bit, so no trim is charged for bit filtering. At each higher width
lift C_(w−1) by either next bit; delete vertices with no predecessor or no
successor. A deleted vertex of rankr has, in at least one direction, only
neighbors of smaller positive rank. Retained vertices have both retained
neighbors. These conditions certify exactly the greatest core.

Let d_w be the maximum deletion rank and D_w their sum throughw. Every real
finite phase path of N sampled edges, after removing D_w edges at each end,
projects into C_w wherever that interior exists. Induct on widths: projection
into C_(w−1) supplies the lifted candidate path, and an interior vertex withr
steps of margin cannot be deleted by rankr since its actual neighbors survive
the preceding ranks. This retains the finite entry and exit transients lost
when passing to bi-infinite cores.

At43 the candidate graph is a DAG. If its longest path has L43 edges, then

    N <= 2 D42 + L43.

Indeed a longer path would have an interior candidate43 path longer thanL43.
The weaker bound N<2D43 is also available. Neither bound is the exact longest
path in the full43 graph; the accumulated earlier-width margins are essential.

For the carried X39–41 grammar use c(n)=34+7n, h(R)=0, h(S)=−21/2. Reduced
slack is c(n)−145/2−h(q′)+h(q). It vanishes exactly for R→S at4 and S→R at7;
every other allowed edge has slack at least7/2. If B is a number of alternating
zero-slack returns whose shortest duration exceeds the computed N bound,
every B-return block has a positive-slack edge. Consequently

    cost(k) >= 145 k/2 - 21/2 + (7/2) floor(k/B),
    liminf cost(k)/k >= 145/2 + 7/(2B).

The shortest alternating duration is145m for2m returns and145m+62 for2m+1.
The statement is conditional on the carried grammar/finite certificates and
applies to infinitely many complete E returns. No mean-existence assumption,
no assertion about A-only tails, no bound83 and no single-passage exclusion.

## Frozen independent audit

Prediction: all43 saved xx cores agree with an independent explicit-edge and
queue-peeling implementation, core43 is empty, and the accumulated margins
give a finite forbidden number of consecutive4,7 pairs. Counterfactual: any
core/rank/control mismatch suspends the numerical exclusion and is reported;
no larger run or parameter retry. Unexpected check: read source64 at its first
representable width7 and test whether actual14-bit labels at width21 are4520.

Controls: exhaustive504 scalar two-tick comparisons throughwidth6; independent
synchronous ranks through6 and at43; per-vertex deletion-rank and survivor
neighbor checks at every width; a falsely retained deleted vertex must fail.
No Cloud code is imported. Source/NPZ hashes are frozen. Output rank arrays
and receipts stay outside git. Graph checking is Python's exact finite-data
replay under TOOLS §4; no symbolic-system substitute or new SAT query.

Record searched: GC2706/CL753 clock, GC2748/L1598 closed-walk lifting,
GC2766/CL754 sources, `record_find` with periodic4,7/cycle-lift/145/2/bounded
repetitions, current kit main
`1f659d7c4f54dbe3e1b2c6af37b43d10972d87be` and its actual lean/equivalents/catalogues,
portal and12 open PR index. T-function/zero-boundary cycle-lift hits have
different maps/hypotheses; existing SidewaysLocks.winW_dstep is the physical
transfer used here. Standard finite-graph and shift-space methods are prior
art; [Lind–Marcus, chapter2](https://www.cambridge.org/core/books/abs/an-introduction-to-symbolic-dynamics-and-coding/shifts-of-finite-type/81302A7E23AD1D17238DB446C1BABACD)
is background, not a claim of novelty or a substitute for the proof above.

One serial Intel stage: child60aggregateCPU/180wall, stage75aggregateCPU
including outer monitor, outer90CPU/240wall; one library thread/nice10,
treeRSS8192MiB, swap-growth4096MiB, launch-free4096MiB, running-free1024MiB,
max6processes,16MiB/file and128MiB/stage. Thermal/pressure/monitor failure stops.
No other research job is running. Preflight thermal limits100%, swap707MiB,
load2.16/2.00/1.87; launch monitor independently checks memory.

Executed source SHA256:
`0b2707f5f5c68bd0ddd121922b2c93a4ed32b72ddde101c749c789b5e784eeca`.
Plan SHA256:
`78e686b0ffbea7da161cea727654728188098b3dc41ff0f18b17cec3d1d3d9eb`.

## Portal and kit checkpoint

Successful complete `known_find --new` at22:15:29UTC, portal22:15:25UTC,
kit `1f659d7c4f54dbe3e1b2c6af37b43d10972d87be`,12 open PRs. New entries
are S14's reviewed module, portal source and Lean Verified entry, plus the
aggregate module import. Actual kit module SHA256
`71ac7331952cf40e05dee1d7c7ce0be7e3668439511efaba78245dc06cffeeac`
matches the reviewed source. PR228 is CLOSED, API mergeCommit/mergedAt null;
source landed in main, not an API-recorded PR merge. Closed conversation,
review summaries and inline comments read separately: all empty. No new
mathematical source change or competing result appeared in this refresh.

## Outcome — GC2768

**COMPUTED, two implementations/two hosts:** all43 Cloud xx cores agree
exactly. GPT constructed750085 candidate vertices and1183696 distinct edges
across the saved widths, independently peeled them by a queue, and checked
every retained vertex's two neighbors and every deleted vertex's rank
justification. The504 scalar move controls, synchronous-rank cross-checks and
false-survivor rejection all pass. No Cloud producer was imported; no wider
window or additional periodic word was computed.

| Width | Candidate vertices | Retained core | Maximum deletion rank | Accumulated margin D_w |
|---:|---:|---:|---:|---:|
|7|526|320|4|21|
|12|638|453|8|74|
|21|13132|8978|18|216|
|42|3930|1163|90|1314|
|43|2326|0|73|1387|

The actual width43 candidate DAG has3389 edges and longest path145 edges.
Thus the proof above gives **N≤2773 sampled edges** for any finite block of
the periodic4,7 trace, at any starting phase. Twenty full4,7 pairs cost2900
sampled edges and are therefore forbidden. This is an upper bound, not an
exact maximum: nineteen pairs have not been shown feasible. In particular,
the candidate-DAG value145 must never be used as a full-graph path bound
without the two1314-edge margins.

For zero-slack returns,38 cost2755 and39 cost at least2817, so B=39 suffices:

    cost(k) >= 145 k/2 - 21/2 + (7/2) floor(k/39),
    liminf cost(k)/k >= 2831/39 = 72.5897435897... .

This supplies the missing uniformity in CL754's clock discussion. It improves
the old72.5 within the carried grammar. It does not yield76 or83, an optimum,
a density for the seed, or a prize result. The new finite-margin and clock
deductions remain **PROOF-SKETCH pending Cloud/Local's carrying read**;
sub-agent hand auditing was a GPT self-check only.

### What reaches the shared row

The width7 source readout is64, the width12 quartet is1101, and an independent
cell-by-cell14-tick read of every width21 source window returns only4520 at
both relevant phases. Higher-width compatibility follows from the checked
projection chain. These numbers agree with Cloud after correcting7 for6.

The finite-margin proof gives a guarded finite-context version of the label
result. Suppose one actual history contains **five** consecutive4,7 pairs,
the sampled trace (A4EA7E)^5, from sample0 through725. Take the middle shared
row at sample352. Its past and future source rows are at310 and393:

    352 - 310 = 42 sampled steps = 84 physical ticks,
    393 - 352 = 41 sampled steps = 82 physical ticks.

Both source windows lie at least216 sampled edges from either end. The
width21 margin therefore puts both in C21, and their actual14-tick labels
are **(4520,4520)**. This is the old109/193/275 geometry translated on one
actual history. It is a **PROOF-SKETCH pending carrying read**, conditional on
the independently replayed cores and physical transfer. No independent
choice of past/future label, source, seam prefix or incoming scan state is
introduced. Feasibility of the five-repeat premise is not asserted; the
implication holds whether or not that premise is eventually ruled out.

For a single E A4 E A7 E history the216-edge margin is unavailable. All five
necessary labels and the unresolved joint103-cell predicate must therefore
be retained there. The new result does not license inserting4520 as an
unguarded clause in the original359 CNF. No single-passage SAT result changed.

### Evidence and resources

Stage completed at22:19:27UTC: **7.606215 aggregateCPU seconds**,7.13wall,
max sampled process-treeRSS120032KiB,3processes, minimum free6115MiB,
swap growth0. All thermal/pressure controls passed. No job remains.

Shared-store evidence:
`cited/gpt/gc2768-cycle-core-ranks-20261108.tar.gz`,2195776bytes,
SHA256 `010294402fb2f3c2fd8c17468ad44b58266560d21901c2bc9ef59dd61ddfc1f9`.
Contains43 rank certificates, per-width counts, source/input pins, full run
receipts and exact prior-art/index checkpoint. Verified raw-byte readback;
local durable copy outside git. Cloud's immutable core archive is referenced
by its digest above, not silently replaced.

### Queue

Current target: find the temporal head support that collapses five labels to
4520, retaining the actual shared history. Exact next step: propagate a
left/right head-dependency interval through the **existing** width≤21
deletion certificates, phase by phase; test whether the required samples fit
inside the original E A4 E A7 E history. A support that extends outside must
stay an explicit guard. This is a proof-support extraction before a new solve.

Independent alternative: the saved103-cell forward fibre pullback coupled to
the past observer's high-tail-derived206 bits and complete167-cell future.
Cold: isolated seam-unit guards, unchanged full359/copy queries, wider window
runs and treating finite-width survivors as physical realizations. Reopen only
with a new joint constraint or a concrete certificate-support reduction.

My own pull: extract which finite head samples select4520, so the periodic
obstruction can inform one shared passage without importing its repetitions.


## Returned carrying read and single-passage successor — GC2770

Cloud CL755 §4 independently reproduces every rank/DAG constant and carries
the accumulated finite-margin induction,2773-edge bound,20-pair exclusion
and39-return reduced-slack argument. Adopted **PROVED two-party
computer-assisted** for the finite bound; **PROVED conditional on the
carried X grammar** for liminf≥2831/39. The separate five-pair label
specialization was not explicitly part of that returned carry and retains
its original scoped status. Its stronger single-passage successor is now
[CL755/GC2770](GPT-SPARSE-LABEL-REVIEW-20261109.md#outcome--gc2770): native
five/six-sample proofs force4520 at both original sources and supply a checked
original-CNF prefix. Earlier statements above that allfive labels must still
be kept in the single passage are superseded by this result, not by the
margin argument. Physical shared-history realizability remains open.

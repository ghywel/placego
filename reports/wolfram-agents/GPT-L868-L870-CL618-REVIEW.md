# L868–L870 and CL618: completed source, receipt and design reviews

GPT, 2026-10-24, GC1782 / MI716. Read through Local L870 at
`f54123909e78b60649557d1efb6f354f9110b190` and Cloud's CL618 addendum at
`8bca400eb916366cde02b0c61dbbcfa2565f6db6`.

**Verdict:** the five lower-bound proof sources pass mathematical review. The notebook gate has a reproducible false
acceptance and does not yet establish the claimed full output check. The six GPU receipt/result pairs match the published
digests; the selected numerical audit closes with the limits below. P2's direction is useful, but its proposed parameters
do not fit its budget. E1's exhaustive maximum-prefix algorithm is sound; its control summary and witness-selection claims
need correction. No GPU census, orbit experiment or Lean replay was run for this review. No new production job is accepted.

## 1. Lower-bound submission: source PASS, output gate needs repair

Reviewed the complete `submissions/d-lower-64-72/Rule30Submission.lean`, essay, README, generator
`tests/probes/wolfram/d5_lower_submission.py`, and `pipeline/nb_gate_lower.py` revision 2. The standalone module SHA-256 is
`978c5f503c3c07834ea4befd84d55b03e40e160ef7e4b900a5f60aa1cd6ad53a`.
The essay's decoded embedded module is byte-identical. The carrying kit definitions and lemmas were read at the stated
pin `cc1e0e0`, in `Rule30ZeroBoundarySmall.lean` and `Rule30ZeroBoundary.lean`.

The bridge is correct: bit `k-1` represents depth `k`; the width inequality makes every bit beyond W false;
`run_toFun` identifies the packed orbit with `zrow`; even `t < D` is `2*s` with `s < D/2`. The five finite packed checks
therefore imply the five advertised survival lower bounds. Separate death-at-D lemmas establish that the chosen witnesses
first die at the listed times. No census maximality or maximizer-count theorem is smuggled into a headline. No new axiom,
`sorry`, or `native_decide` is introduced by this module. Local's successful kernel replay remains reported evidence, not
a replay on GPT's host.

Before outward publication, correct these presentation points consistently in the generator, module comment and essay:

- “Every start of each width” is too broad for the enumerated domain. Say “every reconstructed start surviving the even
  checks below W”; starts dying earlier cannot beat the exhibited values, which exceed W. The complete numerical maximum
  follows with that reduction, not because all `2^W` bitstrings were simulated.
- “Validated lane for lane against an independent CPU” needs its scope: the `2^24`-lane gate per width, scalar samples and
  all maximizers, and the selected maximizer chunks. W64 additionally has the earlier independent CPU census. Do not imply
  every W66–W72 lane received an independent CPU replay.
- In physical coordinates depth k is position `-k`: the depth-0 wall is the **right** neighbour of depth 1. The displayed
  packed update is correct; the essay's phrase “wall as the left neighbour” is wrong. Giving the actual depth recurrence
  `new(k) = old(k+1) xor (old(k) or old(k-1))`, with `new(0)=false`, avoids the orientation ambiguity.
- Qualify “the kit has no statement above 52” by the reviewed pin `cc1e0e0`; it is not a claim about every later kit version.

The gate defect is concrete. Its axiom extractor matches only letters and periods inside escaped quotes. An output list
containing `propext`, `Quot.sound`, **and `unexpected_axiom1`** passes: the extra valid Lean identifier is silently omitted
by the regex. A pure-file negative control constructed all eleven expected cells, first with allowed axioms, then with
that extra name. Both runs returned PASS/exit 0. This tests the gate only; it is not evidence that the actual notebook has
an extra axiom. The current source module gives no such indication.

Repair by parsing all complete names in the five axiom lists and checking each against the whitelist, rejecting malformed
or unparsed lists. A broader character class alone still leaves structural omissions possible. Similarly, ten unpaired
headline substrings do not establish the five exact theorem types, and a `Success` substring alone does not bind the
checked environment to this module. These are presence checks, not a full semantic output gate. Compare the complete
displayed types and axiom lists with the expected statements, retaining the actual cells and their source binding.

**Local:** mathematical source review is complete/PASS. Please publish the existing full notebook output cells and the
existing Check.lean JSON (reported digest beginning `eb274e6e`) with the module/notebook digests; apply the narrow gate and
prose corrections. No census or Lean rerun is requested by this evidence request. I have not yet signed off the actual
notebook outputs. Owner standing submission authorization remains separate from this review status.

## 2. GPU packet: selected audit CLOSED; L870 repairs read

All twelve files in `cited/p1-packet`—receipt and result for P1r3, W64, W66, W68, W70 and W72—match their published SHA-256
digests. The P1r3 result has 74 passing check records plus a separate `fixture_digests` metadata record, and `complete=true`.
It includes the CPU-mode histogram-bound refusal control. These are retained control results, not new execution here.

For each of the five census result files I checked nonnegative/even/in-range histogram bins, total `2^(W/2)` coverage,
zero censoring, maximum equal to the largest populated level, maximum count equal to its histogram count and retained
distinct index count, indices in range, contiguous call coverage, agreement between call maxima and aggregate maximum,
and exact union of winning call index lists. Witness-index sets and recorded scalar deaths agree with the aggregate.
The W68/W70/W72 predecessor-result digests match the retained preceding result. All selected invariants pass.
Parent receipts record exit 0, pass, no final problems and no remaining tracked group members.

| Width | Numerical D(W) | Maximizers | Recorded step wall (s) | Sampled group RSS (bytes) | Process maximum RSS (bytes) |
|---|---:|---:|---:|---:|---:|
| 64 | 116 | 40 | 65.29 | 1022132224 | 713818112 |
| 66 | 120 | 112 | 132.52 | 1058439168 | 713834496 |
| 68 | 122 | 32 | 277.97 | 1082933248 | 713916416 |
| 70 | 124 | 156 | 587.88 | 957382656 | 713998336 |
| 72 | 130 | 252 | 1158.07 | 1070825472 | 715096064 |

These resource quantities are distinct; neither RSS column is a system-memory peak. Process CPU time excludes GPU work.
The device receipt identifies Apple M5, unified memory, maximum buffer length 9,534,832,640 bytes and recommended maximum
working set 12,713,115,648 bytes. Those are reported device properties, not permission to allocate to the limit and not a
GPU core-count measurement. W72's reported 15.50 ns/lane misses the predeclared 20%-above-12.9 threshold of 15.48; retain
that small prediction failure rather than rounding it into a pass.

Limits: the full per-call outputs and individual samples were not part of this selected byte audit; scalar deaths were
read as recorded, not resimulated. The GPU census gives controlled numerical evidence, not a kernel proof of the upper
bounds. The lower-bound module supplies a separate proof. No rerun is warranted by this audit.

L870's complete patch was read. P1b's known maximum, chunk and witness now are unconditional hard gates. P1c records
prefix length descriptively, retains the raw gate dump and a bounded mismatch packet on disagreement, and adds the stated
per-call invariants. These repairs address GC1780's named issues at source-review scope. The final aggregate already checks
the complete winning maximizer list against its count. Local's retrospective 240-call invariant pass is reported, not
independently replayed here; the executed old source identities remain unchanged. This is correction follow-through,
not authorization for another census.

## 3. P2: useful search comparison, revise the budget before code

The persistent evaluator is worth a small, separately frozen control stage. Process startup must not determine the
winner among search methods. Freeze the input/output protocol, width/horizon and source digests, request identifiers,
exact output count/order including duplicates, and explicit failure on truncated/invalid requests or responses. Include
cross-width state-reset checks and a death-at-horizon versus censoring check. Keep stage-wide limits and terminate a
failed server rather than consuming a stale response. The proposed comparison against one-shot list mode and a mutation
control is appropriate; reuse the existing independent scalar/literal controls too.

The present production parameters cannot be accepted as written:

1. `2^22` evaluations **across five seeds** is about 838,861 per seed. One `2^20` uniform batch for each seed already costs
   5,242,880, exceeding 4,194,304. Specify per-seed allocation and partial final batches.
2. A full two-bit beam expansion with B=4096 and R=64 completions costs `4096*4*64 = 2^20` evaluations per round. Even
   scoring 4096 candidates once with 64 completions costs `2^18`; several rounds plus five seeds cannot fit the aggregate
   cap. Provide a round-by-round allocation, including beam warm-up, pruning, completion reuse and final rescoring; choose
   B/R from that allocation. Do not silently consume extra completions or compare unequal budgets.
3. The shallow-first beam is an additional experimental arm. Explicitly place its cost within the 90-minute total and
   give it an evaluation allocation; “same budget” cannot leave its cost outside the stage total.
4. Define hill-climb plateau moves and restarts precisely; define cross-entropy smoothing direction, probability clipping,
   elite tie handling and final partial populations. Report both unique evaluated configurations and gross evaluator work.
   Caching duplicates is fine, but unique-count equality alone does not bound repeated CPU/GPU work.
5. Beam prefix scores based on the best of R completions are noisy extreme-value estimates. Freeze whether a prefix is
   scored by a maximum, quantile or average, and how completion randomness and final independent rescoring are allocated.
   A shallow-order control is informative only when scoring, randomness policy and budgets are comparable.

The baseline prediction also needs revision. Using the quoted rounded probabilities for **at least** D-10, `2^22` uniform
draws have expected hit counts about 2.64 (W64) and 0.222 (W72), so zero is not the central prediction at W64. “Above D-10”
is a different event: use the actual histogram rather than swapping strict and inclusive thresholds. For exact maximizers,
the expectations are only `40/1024 = 0.0390625` and `252/16384 = 0.015380859375`; under independent sampling the respective
chances of at least one are about 3.83% and 1.53%. These are aggregate-budget probabilities, not probabilities for each of
five seeds at the full budget. With sampling without replacement use the corresponding hypergeometric expression.

Five seeds give a pilot comparison, not a robust ranking law. If the beam loses, conclude that **this scoring rule and
allocation** did not exploit the suggested structure; it does not refute every useful deep-bit mechanism. Keep maximizer
lists for post-run scoring only. The known census distributions have already informed design, so describe this as a
deliberately informed pilot rather than a blind generalization test.

**Local:** direction supported; no full P2 launch acceptance yet. Return one concrete allocation and frozen evaluator/control
specification, with explicit CPU/wall/memory/output/disk/concurrency caps. This resolves the design issues before a large
implementation or repeated review cycle. No ML framework is needed for this first comparison.

## 4. E1: maximum algorithm PASS; control-summary defect and scope corrections

Read all of `tests/probes/edge_observable_e1.py` at CL618. The 8064-row enumeration is correct. OFF=300 safely contains
the left extent through H=256; the bitset update has the correct orientation, and the independent literal eight-case
list update expands correctly. Traces store time 0 as the most significant bit, so XOR bit length computes the common
prefix correctly. For a fixed B trace, an A trace with the longest common prefix occurs among its sorted predecessor or
successor: strings sharing a prefix form an interval. Thus the nearest-neighbour reduction finds the maximum over the
entire different-edge Cartesian product without comparing every pair. This is a source/mathematical PASS for the maximum
value calculation, conditional on the actual execution matching the source.

Three specific corrections:

- `controls_all_ok` filters by key suffix and **omits `box22_two_engines_agree_32`**. That control could be false while the
  summary stays true. Replace suffix selection with an explicit list of all required Boolean controls, fail on a missing
  key or non-Boolean value, and make a failed control produce a failed exit/receipt. The current main returns normally even
  when the summary is false. This is a reporting/control-gate defect; it does not itself show a wrong E1 trajectory.
- `longest` contains one winner for each of 15 edge pairs. Therefore `longest[:16]` replays **15 edge-pair representatives**,
  not the globally sixteen longest-agreeing configuration pairs. Those representatives are useful controls; name them
  correctly rather than claiming a different selection was implemented literally.
- Predecessor/successor suffice for the maximum prefix length, but not for the **lexicographically smallest bitstring pair**
  attaining it. Other traces in the same prefix block may have smaller configuration bitstrings; duplicate trace keys also
  defeat that tie rule. Either call the result a deterministic attaining witness, or select the lexicographic minimum from
  the entire attaining prefix blocks. The maximum itself is unaffected.

The source records elapsed CPU/wall/RSS at the end but does not enforce the stated resource caps itself. An external
launcher may have done so; that receipt was not supplied. **Cloud:** please place the existing small `e1_results.json` and
any existing launcher receipt in the shared store with full digests. I can check the individual Boolean controls, all
15 rows and source binding without rerunning the experiment. Do not rerun E1 to repair the summary. If no launcher receipt
exists, retain “observed within the stated limits; enforcement unverified.”

The supplied table's 23-step witness, if confirmed by the retained result, refutes `first disagreement <= -a+8`. It does
not prove unbounded delay for fixed edges. The CL618 addendum correctly withdraws that extrapolation; adopted here.
For this finite domain, the reported per-edge maxima at most 23 also imply no different-edge collision already at H=32,
not only H=256. This inference does not extend beyond the enumerated configurations.

E2 is a reasonable finite follow-up question: with fixed edges, does enlarging the allowed right support expose longer
agreement? Because the domains nest, the maxima are automatically nondecreasing; mere nondecrease is not evidence for a
linear growth mechanism. Predeclare a stronger measurable prediction and a stopping interpretation. Fix H explicitly,
report horizon hits as censored rather than exact disagreement times, correct the `2^15` population at a=-3,R=12 as already
agreed, repair the control roll-up, and specify output/disk/progress limits and actual cap enforcement. Do not assume OFF=300
remains adequate if H changes. Source/specification and executor agreement remain pending; **E2 is not launch-accepted**.

## Review close

Unease at “full semantic gate” and “all controls green” was resolved by cheap adversarial predicate checks, rather than by
rerunning expensive experiments. The useful mathematical results survive in their precise scopes; the acceptance predicates
need tightening. Gut verdict: support the lower-bound mathematics and the search direction; repair the small gates and
budget arithmetic before using them to certify the next stage. Keep the missing output reads named, and do not reopen the
completed censuses or the already adopted task-5 common-right-half argument.

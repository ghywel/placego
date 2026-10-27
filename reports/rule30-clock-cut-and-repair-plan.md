# Natural clock: cut the supply, then test a genuine repair

GC1938 / MI857 / DQ-023, 27 October 2026. **Design recommendation, not a
launched experiment or an accepted executable.** The owner requested a portal
check and a decision about the next path before resuming work.

## Question → response → challenge → better question

**Question.** Can the staircase's natural clock survive by handing support
from one configuration to another?

**Response.** GC1937 shows that a local handover is possible. The new external
submission [c137e0](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261027-c137e0)
also supplies an exact natural eternal clock with an infinite, spatially
7-periodic left half and a finite right half. The infinite left side is an
essential qualification: this is not a finite-seed counterexample.

**Challenge.** Simply cutting that left side at increasing distances and
measuring longer clocks would rediscover a hand theorem. Suppose two rows
agree at every site strictly greater than r and differ at r. Rule 30 makes
them agree strictly beyond r+1 next time and differ at r+1: at that cell only
the left input differs, and XOR preserves the difference. Induction puts the
rightmost discrepancy at r+t. If r=-d<0, the centre first differs at time d.
Thus a finite truncation of this clock, with its right side unchanged, misses
its first beat exactly when the nearest removed black cell's discrepancy
reaches the centre. This is ordinary left-permutivity, not a new theorem.
Arbitrarily long finite agreement is already guaranteed by taking deeper cuts.

**Better question.** With the truncated left half held fixed, can a small
change in the actual right starting row repair that first missed beat,
without spoiling a single earlier beat? If so, what is the next unavoidable
failure, and does the same repair work for a second cut?

This isolates a repair rather than inferring one from two pictures that look
similar. It is an explanatory intervention test, not a new D(W) census or a
promised proof strategy. Existing CQ01/J and E(L,B) work already describes the
general compatibility problem; the proposed novelty is not that formulation.

## Answer the cheap part before searching

Let the required centre be c(t)=1 at even times and 0 at odd times. Evolve the
left half with this candidate boundary, only as a diagnostic. Until the true
centre first deviates, its actual left half must equal this diagnostic, by
induction on the update rule. Call its adjacent value l(t).

- At an even time t, continuation requires l(t)=1 regardless of the right
  neighbour. If l(t)=0, **every right starting row** fails by time t+1 unless
  it has already failed earlier. No right-side edit can rescue that beat while
  preserving the previous centre history.
- At an odd time t, continuation requires r(t)=NOT l(t). A repair is locally
  possible, but an actual finite right row must generate that value and every
  other required value. The neighbours are not independently selectable.

Define H as the first t+1 with even t and diagnostic l(t)=0, if found.
It is an upper bound on uninterrupted alternation for every right completion
of this fixed left row. If H equals the unchanged-right failure time d, close
that case before doing a right-side search. If H>d, the interval (d,H] is the
available repair window. If no H is found by the fixed cap, record censoring;
never call H infinite. This is the existing black-tick/white-tock split.

## Proposed small Intel stage

Freeze source and supervisor in git and obtain the ordinary independent
design read before launch. No M5 stage is justified yet.

**Reference.** Use exactly c137e0's `Witness.alt_left_periodic_right_finite`:
`etherL 3 1`, centre 1, and `config 3 1 6 wsA`, with
`wsA = 0110001101000`. The kit's `etherTable` and `config` definitions fix all
coordinates. At time zero, left depth d>=1 is black iff d modulo 7 is 0, 1,
or 2. The right row at positions 1..19 is `0000110110001101000`, then zeros.
Use a sufficiently padded piece of the infinite reference only as a
finite-horizon oracle; never periodically wrap a finite test row.

**Six distinct left truncations.** Keep depths through
L=14,15,16,21,22,23 and set greater depths white. Their hand-predicted
unchanged-right first failures are d=15,16,21,22,23,28 respectively. These are
distinct rows; cuts through consecutive white cells would duplicate a row.

**Candidate interventions.** For each case with diagnostic H>d, compare the
unchanged right row with every one- or two-cell flip among positions 1..19.
There are 1+19+171=191 right rows per left case, at most 1,146 cases. No
random choice, adaptive widening, best-only reporting, or new cut lengths.
Every candidate then evolves by genuine full-line Rule 30, with the centre
unclamped, until its first missed beat or time 256 inclusive.

**Prediction P.** At least one eligible cut admits a one- or two-cell right
edit with first failure strictly later than d. This is a tentative hypothesis:
the white-phase freedom motivates it but does not imply realizability.
Retain all early failures as well as repairs. If P fails, close this particular
repair family; do not infer that natural relays in general are impossible.

**Counterfactual.** Right edits repair a black-phase left mismatch while
preserving every earlier centre tick. This must fail by the hand argument;
one reported success invalidates the implementation or phase convention.

**Controls.** Independent scalar truth-table and packed implementations must
agree on all first-failure labels, with explicit zero padding/light-cone
margins. The uncut reference matches its declared clock through the horizon.
All six unchanged-right cases match the exact d values above; every computed
H must be at least d, and no genuine candidate may continue past a computed H. Each reported
repair has the identical left initial row and centre start, the declared
right edit only, and no earlier missed beat. Retain the exact local histories
through the first failure and through every left0/centre0 handover.

**Unexpected check.** Test each successful edit on the other already-declared
cut depths, using the same complete table. Does it transfer, or does it only
repair one arrival phase? Report both; do not choose the transfer rule after
seeing outcomes or enlarge the domain. Also retain the duplicate-cut control
as an instrument check, without treating it as another experimental case.

**Limits.** One process, one CPU thread; stage-wide wall 180 s, summed CPU
120 s, process RSS 256 MiB, output plus scratch 10 MiB, no GPU/network inside
the run. Stop on any control failure, cap, system pressure warning or less
than 2 GiB available headroom; retain partial evidence and the actual
enforcement receipt. These are proposed limits, not claims of enforcement.
No automatic rerun. Legacy startup checks must be reported separately:
the earlier merge check was capped/incomplete, not a pass.

**Interpretation.** A repair is finite, causal evidence of a real handover.
The carrying result would be the explicit explanation of the repaired beat
and the next failure, not a longer record. If every outcome is explained
entirely by the existing local identities and no reusable constraint emerges,
stop numerical widening and return to inquisition. A new M5 stage would need
a different, precise prediction about the remaining compatibility cost.

## The new trap is relevant, but it does not supply the answer

[230bc7](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261027-230bc7)
proves an invariant set of 829 right windows, entered from the empty driven
right row at physical time 293. Thereafter black events at white-clock
observations have successive gaps 3 or 5. Under an actual continuing clock,
these would be left0 handovers spaced 6 or 10 physical ticks. This constrains
their timing; it does not prove their finite-left compatibility.

Do not replace the controlled reference above by this empty-right trap
silently. They are different cases. The trap's `Q01Gap` is still open.
Its eight-column reconstruction transform fails its own spacing premise on
the next application, as the source proves. A small repeated-picture argument
therefore cannot simply be iterated. The kit also supplies a period-31
3/5-gap control with 17 consecutive white reconstructed initial cells,
refuting a naive uniform gap bound of 16. Those are prior results, not new tests.

Record searched: `record_find.py 'handover|replacement|relay'`, DQ-023/L997,
PERIOD-TWO sections 2/4, G239's controlled 3/5-gap loops and the CQ01/J and
E(L,B) entries. The same gap alphabet and finite-prefix limitations already
occur in our work. New external input is the certified trap and the exact
half-infinite control, not a claim to have discovered a new encoding.

Reasoned verdict: keep the natural-clock question; prefer this small
cut-and-repair diagnostic over a longer lifetime census. Gut: warm, with a
specific falsifiable intervention and an analytic stop before unnecessary
search. No experiment or heartbeat was started in this review.


## GC1939 execution freeze — owner restart, 27 October 2026

The owner now explicitly requests this Intel test and re-arms both schedules;
self-halting is no longer authorized. This instruction authorizes execution
without waiting for a routine launch permission round. Local's independent
source/design read remains pending and is not claimed by the two-engine check.
Source: `tests/probes/wolfram/clock_cut_repair_intel.py`; existing supervisor:
`tests/probes/wolfram/run_capped.py`. Exact declared domain and prediction above
are unchanged. The source first guards all eight truth-table entries and the
external ether coordinates; both engines compare every retained local window,
not just failure times. Radius288 covers time256 and the recorded radius4.

Operational limits: one computational worker/thread, no numerical subprocesses,
GPU or network. The supervisor and transient OS monitoring helpers are additional
processes. Worker CPU limit110s; supervisor CPU limit10s. Worker plus completed
helper CPU is also sampled with a110s stop. The120s sum is the allocation budget,
not an atomic process-tree kernel limit. Wall180s, group RSS256MiB, file8MiB,
aggregate artifacts10MiB are the existing supervisor's limits; RSS, disk, pressure
and wall are sampled and may overshoot between samples. Headroom uses the declared
free+inactive proxy, at least2048MiB throughout and4096MiB at launch, not a claim of
exact available RAM. Swap growth cap256MiB. The probe separately checks actual OS
memory-pressure level at launch and at most one second between case boundaries,
refusing anything except normal. Parsing/monitor failure stops the stage. Retain
the full receipt and report observed supervisor/helper CPU separately. No automatic
rerun; an incomplete run is not a passed experiment. Legacy startup remains wall
PASS / merge capped-incomplete from the prior checked session; this does not claim
both startup checks pass. Current exact controls are independent of those scripts.

Record searched: `record_find.py 'cut.*repair|rightmost.*discrepancy'`, including
the existing rightmost-damage result G105 and the GC1938 hand filter. No novelty
claim for the propagation/deadline identities. Gut: warm about an actual intervention,
with unease that the small right-edit family may be too rigid; prediction P stays
falsifiable and its failure will be retained.

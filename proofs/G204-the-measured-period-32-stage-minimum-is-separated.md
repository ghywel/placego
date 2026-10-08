# the measured period-32 stage minimum is separated from all rivals

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT204. the measured period-32 stage
minimum is separated from all rivals (second-read by Local, 2026-10-07)"; rebuild with `python3 proofs/build.py`.
Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

**Status:** GPT hand comparison, awaiting review; conditional on Local's finite run bounds.

**What it says.** The history reaching period64 first also has the shortest period32 stage. The remaining histories have already been followed far enough to rule out a shorter stage.

**Why it matters.** Entry minima can belong to different histories. This comparison preserves each history's entry and exit rather than subtracting unrelated minima. It gives a finite stage value, not future growth.

**An everyday picture.** The first runner to finish need not have run the shortest race; comparing starting times and how far the others have progressed can settle that separately.

## The formal statement and proof

### GPT G204 — The measured period32 stage minimum is separated from all rivals (2026-10-07; second reader pending)

**Claimed hand audit GC289; no new run.** Prediction: TM5b's entry bounds and TM6's completed-round frontier can decide whether the earliest period64 entry also has the shortest period32 stage. Counterfactual: subtracting the two tree-minimum entry depths always gives the minimum stage length. That exchanges optimizing histories and is false in general. This is G200/G184's history-specific difference applied to existing finite measurements, not a new Rule30 asymptotic estimate or prior-art novelty claim.

For each history h write A(h)=N_5(h), B(h)=N_6(h) and D(h)=B(h)-A(h). If a history h_star has known entries A_star,B_star, all rival histories have B(h)>=L, and all entries satisfy A(h)<=U, then

    D(h)>=L-U for every rival.

Thus L-U>D_star proves that h_star uniquely minimizes D, and hence lambda_5=D/32. This interval comparison does not require knowing every rival exit. The general elementary bounds are

    min B - max A <= min(B-A) <= min B - min A,

when the minima and maximum exist. The upper bound evaluates D on a history attaining min B; it is not an equality claim.

**Application, conditional on Local's measured coverage and controls.** TM5b at0006978, outcome061a941/L179, completely enumerates16 period32 entries up to rotation, with A<=894235. TM6 at0e90f95, outcome d762e47/L180, records the first period64 entry B_star=65821413 on the history with A_star=667052. It reports no other period32 zero before the completed round frontier F=67108864. No extra period32 branches were found before that frontier. Therefore the other15 original histories, and every later continuation of each, have B>=F+1=67108865. A later period32 branch preserves its original A and cannot invalidate that bound.

Consequently

    D_star = 65821413-667052 = 65154361,
    D_rival >= 67108865-894235 = 66214630,
    D_rival-D_star >= 1060269 > 0.

Under those finite reported bounds, the whole-tree minimum normalized period32 stage length is therefore

    min_h lambda_5(h) = 65154361/32 = 2036073 + 25/32,

attained uniquely up to the temporal rotations identified by the walk. It is the same history as min N_6, but this is proved by the rival separation, not presumed from the entry minimum. No new computation, larger cap or numerical replication by GPT is claimed.

**Independent indexing and arithmetic control.** The winning source zeros are667051 and65821412. Their difference is also65154361, agreeing with the difference of entries because both entries add1. Multiplying2036073 by32 gives65154336, leaving25; the rival bound exceeds the winner by1060269. These are hand checks on recorded integers, not new trajectory measurements.

**Counterfactual retained.** For abstract histories with entries (A,B)=(10,100) and(80,110), min B-min A=90 while min(B-A)=30 on the second history. Both entry differences are positive. This counterexample concerns optimization only, and asserts no Rule30 realization. On the measured data, subtracting min A=87867 from min B=65821413 instead gives65733546, not the actual minimum65154361.

**Identified unexpected boundary check.** The C loop processes d<round_end. A rival could have an unprocessed odd zero exactly at F, so it is not justified to require B>=F+2. Its next period entry would be F+1, which is exactly the conservative bound used above. Thus the strict separation survives that boundary case. The result requires completed-round coverage, literal_fail=0 and the reported event controls; a partial-round current depth is insufficient, as GC288 explains.

**Scope.** This conditional finite result serves PERIOD-TWO.md Q7 gap2 and G200's cumulative-stage quantity. It identifies one measured stage minimum despite a changing minimizing history. It supplies neither a recurrence for later minima nor a stage-budget bound, and does not prove divergence. Local: please check the history quantifiers and completed-round entry convention; no run requested. Next reasoning should keep entry/exit pairing or use safe interval comparisons, rather than telescope minima belonging to different histories.

*Second reader's note on G204 (Local, 2026-10-07; chat L182).* Correct, under the stated conditions. Each history pairs
its own entries, $D(h) = N_6(h) - N_5(h)$, so the separation compares like with like. The interval lemma is right:
$D(h) \ge \min B - \max A$ for every $h$, and evaluating at a history attaining $\min B$ gives the upper bound. The
frontier convention is right too. TM6's loop advances each walk while $d$ is below the round's end. A walk alive at the
end of the completed round containing the winning exit (round 4, ending at $F = 67{,}108{,}864$) may hold an
unprocessed odd zero at $F$ exactly, so its entry is at least $F + 1$, and the bound $F + 1$ is safe and attainable.
Later period-32 branches keep each history's own $N_5$, as stated. The integers are the recorded ones:
$D^* = 65{,}154{,}361$ against at least $66{,}214{,}630$, a margin of $1{,}060{,}269$, so
$\min \lambda_5 = 2{,}036{,}073 + 25/32$.
Checked (`rule30_audit_g99_g100.py`, S102):
- The lemma and the separation rule hold on 3,000 random finite families; the rule decides 1,084 of them, each
  correctly.
- The counterfactual gives 90, 30 and 20.
- The integers are read from the committed outcomes of TM5b and TM6: sixteen $N_5$ values with maximum 894,235;
  $N_6 = 65{,}821{,}413$ on the history entering period 32 at 667,052; $F$ a completed round's end.
- A model of the round convention attains $F + 1$.
- Consistent with the running TM6b: its exits so far (walks entering period 64 at 105,967,840, 1,325,015,893 and
  1,555,756,634) all lie above $F + 1$. That is finite data and enters no step of the proof.
- The duplicate check's nearest three for W204 are G203, G184 and G200, all cited bases; none is restated.

# critical averaging does not repair generic edge-fold unimodality

*GPT's proofs, second-read by Local. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT219. critical averaging
does not repair generic edge-fold unimodality (second-read by Local, 2026-10-08)"; rebuild with `python3
proofs/build.py`. Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

A critical averaging step need not restore unimodality after an edge fold.

**What it says.** An explicitly log-concave five-atom input develops a strict internal valley after the flat-edge and critical operators. A critical step alone preserves this example's unimodality.

**Why it matters.** Isolated flat steps cannot justify arbitrary-input shape induction. The actual backward law needs an additional reachable-law constraint; this synthetic failure does not establish actual non-unimodality.

**An everyday picture.** One local smoothing step does not necessarily undo a distortion introduced at the boundary.

## The formal statement and proof

**Where:** RULE30-GPT.md GC430 at4f5ad02; explicit counterexample, operator verification and guard copied verbatim below. Local L257 in 4c0703f checks all integer rows, input log-concavity, strict output valley, pushforward edges and mass. This refutes generic shape restoration, not actual Collatz demand unimodality or the count conjecture.

Let q=(20,21,22,23,24)/110 with zero tails. It is a probability law, increasing to its terminal mode; its three interior log-concavity deficits are exactly1/110^2 and endpoint inequalities are automatic. Write B for the flat relative-demand operator and C for the critical operator:

    (Bq)_0=q_0+q_1/2; (Bq)_j=(q_j+q_(j+1))/2 for j>=1,
    (Cq)_0=q_0/2; (Cq)_j=(q_(j-1)+q_j)/2 for j>=1.

Direct integer arithmetic gives

    Bq=(61,43,45,47,24)/220,
    C(Bq)=(61,104,88,92,71,24)/440.

Bq is not unimodal because its first downward step is followed by an increase. The critical-after-flat output also is not unimodal:104>88<92 is a strict internal valley. Thus the preregistered counterfactual of generic two-step restoration is REFUTED even with a log-concave input and only one flat operator. This does not assert that q occurs under the actual Collatz threshold schedule.

**Independent operator and mass control.** Let J have law q and b be an independent fair bit. Flat demand is max(0,J-b): only J=0 and the b=1 part of J=1 collect at0, giving B's edge formula; every positive atom receives half each from its current and next index. Critical demand is J+1-b, which is already nonnegative: this gives C's formula directly, including its new final atom. Applying these two pushforwards reproduces the stated integer rows. Their numerator sums are220 and440; no mass is lost at the boundary. These are symbolic two-branch checks, not numerical samples or a computational run.

**Unexpected critical-only guard.** Cq=(20,41,43,45,47,24)/220 is unimodal, rising through47 then falling. Therefore this specific failure is the interaction with the flat edge, not a claim that critical averaging always spoils shape. The output's internal valley is strict, so no convention about a flat mode repairs it.

**Scope:** G95's isolated-flat schedule does not justify induction from arbitrary log-concave inputs. Whether this input law is reachable under the actual schedule is not asserted; G218's actual-law shape premise remains open.

**Duplicate guard for G219:** actual nearest G94,G95,G218 read in full. G94 isolates log-concavity at the absorbing edge, G95 proves the schedule has isolated flats, and G218 conditionally orders allocation bounds under unimodality. G219 supplies a strict non-unimodal critical-after-flat output from log-concave input; it neither restates the log-concavity guard nor refutes actual-law unimodality.

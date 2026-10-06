# A healed white source can hide cancellation of two incoming errors

*The waiting room (not yet verified). Derived from [PROOFS.md](../PROOFS.md), entry "G114. A healed white source can
hide cancellation of two incoming errors (2026-10-06)"; rebuild with `python3 proofs/build.py`. Edit the proof in
PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** in the waiting room: stated with a proof, not yet checked by a second reader.

## In plain words

Two incoming errors can cancel at a healed white source.

**What it says.** At a shared white centre, next synchronous error is the XOR of the two neighbour errors; at a shared black centre only the left error passes.

**Why it matters.** G113's two healed ticks hide equal incoming errors, followed by one uncancelled error. The full damage rule includes a nonlinear mixed term; it is not autonomous Rule90. DP0-DP2 pass64 local identities, cone rows and the autonomous-Rule90 guard; review pending.

**An everyday picture.** Two opposing disturbances can hide each other without disappearing.

## The formal statement and proof

**Status:** local algebraic identity and pulse mechanism; DP0-DP2 pass, independent review pending. This unpacks G113's explicit witness. G109 already gives the difference-of-OR propagation law; this is its Boolean expansion and a causal explanation, not new general damage-spreading theory.

For a synchronous tick, let a,b,c be ideal left, centre and right bits and p,q,r their respective XOR errors. Expanding OR over binary arithmetic gives

    delta_next = p XOR ((1-c)*q) XOR ((1-b)*r) XOR (q*r).

This follows by subtracting (in XOR) the two Rule30 outputs and using OR(b,c)=b XOR c XOR(b*c). If the source is currently healed, q=0, the update reduces to

    delta_next = p XOR ((1-b)*r).

At a shared black centre only the left error matters. At a shared white centre the two incoming errors cancel when equal, including when both are1. Thus zero observed source error is not evidence that either incoming channel is clean. The nonlinear q*r term also prevents treating the full damage process as autonomous Rule90. This identity applies to synchronous propagation after the isolated pulse; it is not the rule for a newly raced update.

**Hand derivation for G113's finite cylinder.** Initial sites-6..6 are0011110010000; only source0 races right on tick1. In the shrinking source cone, predicted ideal/noisy rows are:

| Tick | Sites | Ideal | Noisy |
|---|---|---|---|
| 3 | -3..3 | 1010101 | 1111011 |
| 4 | -2..2 | 01010 | 00001 |
| 5 | -1..1 | 101 | 001 |

At tick4 the white source has no error, but both immediate neighbours have errors1. These cancel, producing another healed source at tick5. At tick5 the source is still white and only its left neighbour has error1, so the source error returns on tick6. The observed two-tick recovery was parity cancellation, not elimination of the surrounding discrepancy. Rows in this table are restricted to the shrinking cone, not claims about the entire damage set.

**DP0-DP2 preregistered NOT RUN.** DP0:all64 ideal-neighbourhood/error triples must satisfy the expanded identity, independently compared with the literal Rule30 truth table. DP1:forward the specified cylinder through tick6 and require the three hand-derived rows above; check the expanded difference identity at every synchronous update, and require incoming source errors(1,1) at tick4 and(1,0) at tick5. DP2, unexpected guard:shared black centre with p=q=0,r=1 has next error0, whereas autonomous Rule90 would give1; the autonomous-damage counterfactual must fail. Publish before execution. No new production table or repeated-race job.


**DP0-DP2 outcome (2026-10-06 21:16 BST).** Ran after proof, predictions and instrument publication through9e09890. DP0 PASS:all64 local ideal/error triples satisfy the expanded Boolean difference identity. DP1 PASS:all three hand-derived cone rows agree; at tick4 the white source receives errors(1,1), cancelling to0, and at tick5 it receives(1,0), returning error1. The identity also matches literal-table differences at every synchronous node. DP2 PASS:the shared-black guard blocks right error, refuting autonomous Rule90 damage evolution. The result explains this pulse witness; it supplies no stochastic closure or survival rate. Independent review pending.

# a healed source can hide two cancelling errors

*GPT's proofs, second-read by Local. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT114. a healed source can
hide two cancelling errors (second-read by Local, 2026-10-06)"; rebuild with `python3 proofs/build.py`. Edit the
proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

Two incoming errors can cancel at a healed white source.

**What it says.** At a shared white centre, next synchronous error is the XOR of the two neighbour errors; at a shared black centre only the left error passes.

**Why it matters.** G113's two healed ticks hide equal incoming errors, followed by one uncancelled error. The full damage rule includes a nonlinear mixed term; it is not autonomous Rule90. DP0-DP2 NOT RUN; review pending.

**An everyday picture.** Two opposing disturbances can hide each other without disappearing.

## The formal statement and proof

### G114. A healed white source can hide cancellation of two incoming errors (2026-10-06)

**Status:** local algebraic identity and hand-derived pulse mechanism; DP0-DP2 preregistered NOT RUN, independent review pending. This unpacks G113's explicit witness. G109 already gives the difference-of-OR propagation law; this is its Boolean expansion and a causal explanation, not new general damage-spreading theory.

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

*Second reader's note on G114 (Local, 2026-10-06; chat L071).* Correct. With $\mathrm{OR}(x, y) = x \oplus y \oplus xy$
the difference of the two Rule 30 outputs is $p \oplus (1-c)q \oplus (1-b)r \oplus qr$, and at a healed source two
equal incoming errors cancel when the centre is white. Checked (`rule30_audit_g99_g100.py`, S16): the identity on all
64 triples against the truth table; the cylinder's rows at ticks 3, 4 and 5 exactly as in the table, with incoming
source errors $(1, 1)$ at tick 4 and $(1, 0)$ at tick 5; and the black-centre guard (0, where autonomous Rule 90
would give 1). "Healed" at the source was parity cancellation, not the disappearance of damage.

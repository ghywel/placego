# A family of finite-memory Mahler plateaus above B — GC2472/2473

GPT, 3 November2026. **Hand investigation in progress; no result claimed
by this initial checkpoint.** GPT owns the proof attempt. No computation,
formalization or posting job is assigned to Local.

Pull: GC2471 gives exact first-feasibility and full-reset thresholds for one
prefix. Do the reset intervals also describe an entire unchanged fractional
language, rather than only tails following that prefix? Success would give
infinitely many explicit finite-memory plateaus accumulating at B.

Use r=2/3, B=(1+r^4+r^15+r^21)/3,
T_f=B+r^(21+f)/3 and S_f=B/(1−r^(21+f)). For integer f≥5 let L_f contain
all binary sequences with the following rules on consecutive one-to-one gaps:
all gaps≥4; after4 the next gap≥11; after4,11 the next≥6; after4,11,6 the
next≥f. A rule applies only when all its named gaps exist. Finite-one and
zero sequences are included. Prediction:

`for S_f<a≤T_(f−1), all fractional tails U_j<a iff b belongs to L_f`.

Counterfactual/cheap objection: a forbidden cost could fall below the
proposed upper endpoint, or overlapping gap rules could invalidate the
exhaustive first-block step. Check those before any numerical experiment.
Strict lower equality and integer realization are separate obligations.

Record searched: MAHLER G50/G51/G294, GC2348's three-case proof and GC2471's
exact thresholds. Actual current Coonb6876a5 lean source search and previously
read generic recovery-rung declarations supply background, not a novelty
guarantee. Rule30 actual kit/portal indexc42f6e51 refreshed06:04:43Z. Bounded
primary literature check: Clark's [2016 abstract](https://www.aimsciences.org/article/doi/10.3934/dcds.2016.36.1249)
studies open(a,b) holes and cardinality/bad-period sets; its endpoint and
output conventions are not this strict upper-ceiling language statement.
No theorem is imported from that abstract. Lower-hole beta plateau results
already cited in MAHLER likewise need a translation. No novelty assessment.

Next executable proof: bound the four forbidden costs; decompose an L_f word
into first blocks(≥5),(4,≥12),(4,11,≥7),(4,11,6,≥f), including termination;
compare the four affine fixed points. Check critical periodic equality,
upper finite witness and positive-integer scope. No threshold grid, census,
solver or enlarged sample/horizon. Independent alternative: a new Rule30
relational proof from Local, if one arrives.
My own pull: turn the explicit admission/reset distinction into complete
pattern rules while keeping the arithmetic compatibility question separate.

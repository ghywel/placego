# Dyadic stage budgets stitch without a logarithmic loss

*The waiting room (not yet verified). Derived from [PROOFS.md](../PROOFS.md), entry "G165. Dyadic stage budgets
stitch without a logarithmic loss (2026-10-07)"; rebuild with `python3 proofs/build.py`. Edit the proof in PROOFS.md
and this summary in [summaries.md](summaries.md), never this file.*

**Status:** in the waiting room: stated with a proof, not yet checked by a second reader.

## In plain words

If each stage with an unchanged dyadic period has a uniform interval budget proportional to that period, those budgets add geometrically across doublings. Phase changes and birth restarts then cost only a constant times the final period. The stage budget and sublinear period growth remain assumptions; a branch that keeps its period gives no fresh allowance.

## The formal statement and proof

**Conditional reduction.** Follow one infinite admissible rooted diagonal history. At node k let p_k be the least common temporal period of its adjacent pair, with the root (0,1) at k=0. Use gamma with 1<=gamma<3. Suppose there is one finite constant C>=0 for this history such that, on every maximal constant-period stage q, one full-line reference path has debt at most C*q on every finite subinterval of that stage. Different stages may use different reference arrival phases, but C and gamma must stay uniform along this history.

Then, for a prefix of M edges, every full-line interval and every starting time has debt at most2*(C+1)*p_M. The same bound transfers to normalized birth-clamped absolute timing:

    T_birth(M) <= gamma*M+2*(C+1)*p_M.

It also covers every global temporal phase of this same history. Thus p_M=o(M), together with the assumed stage budget, would supply G2's below-3 sufficient settling bound on this history. To cover every admissible left side, both assumptions must hold separately on every history; history-dependent constants are allowed as in G2. No stage budget or period-growth estimate is proved here.

**Exact stage structure.** The predecessor B commutes with temporal shifts. If a child pair has period q', its predecessor has a period dividing q'. G157's reset/integration rule supplies child common period at most q, or2q at an odd zero-driver integration, when the parent's least period is q. Since rooted periods are dyadic, the child's least period is therefore q or2q, never smaller. A doubling can occur only on a zero-driver edge; that edge has full-line reset cost0. Every edge whose source pair has period q uses a driver with period dividing q, including that final zero edge. Consequently all clock maps within a stage share common period q. Genuine even-parity branches preserve q; they do not start a new period stage.

**Proof of the budget.** Fix any finite interval within the M-edge prefix and split it at period changes. For its part in a q-stage, G164 upgrades the assumed reference all-interval debt C*q to an arbitrary-start debt at most(C+1)*q-1. Each stage is contiguous, so the interval visits each q at most once. The distinct q are powers of2 bounded by p_M. Their sum is at most2*p_M-1. Sum the interval inequalities at their actual arrival times to obtain elapsed <=gamma*(interval length)+2*(C+1)*p_M. This holds for every starting time, so G9's restart identity applies on the finite prefix, giving the stated birth bound. Phase conjugacy preserves the same inequalities. No separate phase sum, per-birth penalty or per-branch allowance occurs. Square.

**Equivalent period-growth checkpoint.** Every infinite rooted history has unbounded p_k: otherwise its path would be infinite in G7's finite rooted tree. Let N_j be the first node of least period2^j, for j>=1. The exact stage structure gives p_k=2^j for N_j<=k<N_(j+1). Hence p_k=o(k) if and only if2^j/N_j tends to0. Necessity evaluates at k=N_j; sufficiency bounds p_k/k by2^j/N_j throughout that stage. This is a reformulation, not an estimate for N_j. A large finite doubling delay does not prove the limiting condition.

**Identified unexpected check: branching is not doubling.** The known split at diagonal53208 has period16 children, as G2.3, G158 and the independent FBR16 replay establish. It is not the first period32 node N_5 and earns no new stage allowance. The known initial stage entries3,8,29,400 do not locate N_5. Nor may one add C*q after every genuine branch at fixed q: the assumed all-interval budget must already cover the selected continuation within that entire stage. The elementary sum1+2+4+8+16=31 checks the strict bound below2*16, but certifies no actual stage debt.

**Scope.** Direct use of G2, G7, G157/G158, G164's interval transfer and G9's birth theorem; elementary geometric summation, with no novelty or new computation claim. G164 is pending independent review at this writing. The hard obligations remain uniform one-reference-path stage debt and superlinear doubling-entry positions on every admissible history. Word-only branch counting, finite doubling records and repeated-strip rates supply neither obligation. No prize conclusion is asserted.

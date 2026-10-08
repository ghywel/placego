# dyadic stage budgets stitch without a logarithmic loss

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT165. dyadic stage budgets stitch
without a logarithmic loss (second-read by Local, 2026-10-07)"; rebuild with `python3 proofs/build.py`. Edit the
proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

If each stretch with a fixed period has a budget in proportion to that period, the budgets add up to a constant
times the last period.

**What it says.** Along an edge history the period stays the same for a stretch, then doubles. If every such stretch
keeps its timing debt within a fixed multiple of its period, the totals add up like 1 + 2 + 4 + ..., less than twice
the last, so the whole history stays within a constant times its final period, phases and restarts included. A real
fork that keeps the period earns no extra allowance.

**Why it matters.** It reduces the settling question to two named assumptions: the budget for each stretch, and
periods that grow more slowly than the depth. Neither is proved.

**An everyday picture.** Bills that double every month never add up to more than twice the latest one.

## The formal statement and proof

### G165. Dyadic stage budgets stitch without a logarithmic loss (2026-10-07)

**Conditional reduction.** Follow one infinite admissible rooted diagonal history. At node k let p_k be the least common temporal period of its adjacent pair, with the root (0,1) at k=0. Use gamma with 1<=gamma<3. Suppose there is one finite constant C>=0 for this history such that, on every maximal constant-period stage q, one full-line reference path has debt at most C*q on every finite subinterval of that stage. Different stages may use different reference arrival phases, but C and gamma must stay uniform along this history.

Then, for a prefix of M edges, every full-line interval and every starting time has debt at most2*(C+1)*p_M. The same bound transfers to normalized birth-clamped absolute timing:

    T_birth(M) <= gamma*M+2*(C+1)*p_M.

It also covers every global temporal phase of this same history. Thus p_M=o(M), together with the assumed stage budget, would supply G2's below-3 sufficient settling bound on this history. To cover every admissible left side, both assumptions must hold separately on every history; history-dependent constants are allowed as in G2. No stage budget or period-growth estimate is proved here.

**Exact stage structure.** The predecessor B commutes with temporal shifts. If a child pair has period q', its predecessor has a period dividing q'. G157's reset/integration rule supplies child common period at most q, or2q at an odd zero-driver integration, when the parent's least period is q. Since rooted periods are dyadic, the child's least period is therefore q or2q, never smaller. A doubling can occur only on a zero-driver edge; that edge has full-line reset cost0. Every edge whose source pair has period q uses a driver with period dividing q, including that final zero edge. Consequently all clock maps within a stage share common period q. Genuine even-parity branches preserve q; they do not start a new period stage.

**Proof of the budget.** Fix any finite interval within the M-edge prefix and split it at period changes. For its part in a q-stage, G164 upgrades the assumed reference all-interval debt C*q to an arbitrary-start debt at most(C+1)*q-1. Each stage is contiguous, so the interval visits each q at most once. The distinct q are powers of2 bounded by p_M. Their sum is at most2*p_M-1. Sum the interval inequalities at their actual arrival times to obtain elapsed <=gamma*(interval length)+2*(C+1)*p_M. This holds for every starting time, so G9's restart identity applies on the finite prefix, giving the stated birth bound. Phase conjugacy preserves the same inequalities. No separate phase sum, per-birth penalty or per-branch allowance occurs. Square.

**Equivalent period-growth checkpoint.** Every infinite rooted history has unbounded p_k: otherwise its path would be infinite in G7's finite rooted tree. Let N_j be the first node of least period2^j, for j>=1. The exact stage structure gives p_k=2^j for N_j<=k<N_(j+1). Hence p_k=o(k) if and only if2^j/N_j tends to0. Necessity evaluates at k=N_j; sufficiency bounds p_k/k by2^j/N_j throughout that stage. This is a reformulation, not an estimate for N_j. A large finite doubling delay does not prove the limiting condition.

**Identified unexpected check: branching is not doubling.** The known split at diagonal53208 has period16 children, as G2.3, G158 and the independent FBR16 replay establish. It is not the first period32 node N_5 and earns no new stage allowance. The known initial stage entries3,8,29,400 do not locate N_5. Nor may one add C*q after every genuine branch at fixed q: the assumed all-interval budget must already cover the selected continuation within that entire stage. The elementary sum1+2+4+8+16=31 checks the strict bound below2*16, but certifies no actual stage debt.

**Scope.** Direct use of G2, G7, G157/G158, G164's interval transfer and G9's birth theorem; elementary geometric summation, with no novelty or new computation claim. G164 was independently verified by Local L122 during this publication; its review and controls are preserved. The hard obligations remain uniform one-reference-path stage debt and superlinear doubling-entry positions on every admissible history. Word-only branch counting, finite doubling records and repeated-strip rates supply neither obligation. No prize conclusion is asserted.

*Second reader's note on G165 (Local, 2026-10-07; chat L123).* Correct as a conditional reduction. The stage structure
holds: since $B$ commutes with shifts, the parent's least period divides the child's, so with G157's reset and
integration rule a child has period $q$ or $2q$ and never less. Doubling happens only on an odd-parity zero-driver edge,
which costs 0, and an even-parity branch keeps $q$. The budget sum holds: within a stage G164 turns the assumed $Cq$
into an arbitrary-start $(C + 1)q - 1$. An interval meets each dyadic stage at most once, and the powers of two up to
$p_M$ sum to less than $2p_M$. The period-growth reformulation is right in both directions. Checked
(`rule30_audit_g99_g100.py`, S59) along the known $Q = 16$ representative path to its first genuine branch (53,208
nodes). The period never decreases and changes only at odd-parity zero drivers, by doubling. Every node's driver has
least period dividing its stage period. The stage entries are $N_1, \ldots, N_4 = 3, 8, 29, 400$ with no period-32 node,
and the branch keeps period 16. Both hypotheses, the uniform stage budget and $2^j/N_j \to 0$, remain unproved, as G165
says.

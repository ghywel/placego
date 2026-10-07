# complete branch blocks and partial interval costs

*GPT's proofs, second-read by Local. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT167. complete branch blocks
and partial interval costs (second-read by Local, 2026-10-07)"; rebuild with `python3 proofs/build.py`. Edit the
proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

A free step pays for a whole branch block, but not for every part of it.

**What it says.** At a real fork the branch step costs nothing, and with the three resets after it (G162) it makes a
block whose total stays within the allowance for periods up to 8. A shorter stretch inside the block can still run
over: by 11 in one period-8 case, and by 2 at the known period-16 fork, where every whole block pays.

**Why it matters.** Paying for whole blocks is not enough; the bound must hold on every stretch, and the steps
between blocks are still open.

**An everyday picture.** A bank account that comes out even once the salary lands can still go overdrawn in the week
before payday.

## The formal statement and proof

### GPT G167 — complete branch blocks and partial interval costs (RULE30-GPT.md G167; awaiting second reader, 2026-10-07)

**Bounded symbolic result, independent review requested.** Include G162's zero-driver branch edge(a,0)->(0,c), then the three nonzero-driver edges whose elapsed cost is either ell+2 or ell+m+2. Here r is gated, ell and m are the first two constant-run lengths of c, and ell+m<=q. The zero-driver edge costs0. At slope5/2 the total doubled reward of this four-edge block is therefore one of

    2*ell-16, 2*(ell+m)-16.

The worst endpoint reward is at most2q-16. Thus every such block at dyadic q<=8 has nonpositive endpoint reward. This is an ambient gated statement, not a rootedness assertion. At larger periods the upper bound can be positive. G162's pulse attaining family makes the larger reward2q-16 sharp. G159's seven-depth separation ensures these four-edge blocks around distinct genuine branches do not overlap, but supplies no bound on the remaining edges.

**Exact partial-prefix audit.** On the fast sibling c(r)=1, the four reset delays are0,1,1,ell. Its prefix doubled rewards, after0 through4 edges, are

    0, -5, -8, -11, 2*ell-16.

On the slow sibling c(r)=0, the delays are0,ell+1,1,m. The rewards are

    0, -5, 2*ell-8, 2*ell-11, 2*(ell+m)-16.

These follow directly from G162's literal reset arithmetic, including the m=1/ell=1 endpoint cases. Consequently the largest reward of a prefix anchored before the free zero edge is the maximum of0,2*ell-8,2*(ell+m)-16 across the two siblings. It is at most max(0,2q-10), since a nonconstant c has ell<=q-1. This says nothing about an interval that begins after the free edge.

**Known rooted control, not a new run.** G162's six allowed phases at the recorded q16 split have(ell,m)=(5,1),(1,4),(4,2),(2,3),(3,1),(1,5). Hence every whole four-edge branch block there has doubled reward at most-4, while the largest branch-anchored prefix reward across phases and siblings is2 (debt1). This is arithmetic on the existing table, not a continuation search or a uniform q16 theorem. No actual birth-clamped settling estimate is imported.

**Identified unexpected check/counterfactual: endpoint payment does not pay arbitrary intervals.** At q8 choose the valid G162 gated pulse family with ell=7,m=1. The slow sibling's whole four-edge reward is0, but its two-edge prefix reward is6 (debt3). If an interval starts immediately after the free edge, its very next reset costs8 and has reward11 (debt5.5). These are actual compatible local blocks from G162, unlike the generic clock schedules of G163's addendum; rooted membership is not claimed. They refute treating nonpositive block endpoints as a certificate for every prefix or subinterval.

**What moves and what remains.** The free zero edge is an exact part of the local branch charge and should not be discarded when charging complete branch blocks. Negative complete blocks can be recognized without charging a fresh period budget per branch. However interior endpoint effects and the intervening nonbranch edges still need control, especially at larger q. Removing blocks does not create a new compatible history, so no bound may be applied to the compressed word sequence without a separate argument. G165's uniform all-interval stage obligation remains unproved. This is a symbolic corollary of G162 and G159, not a new general amortized theorem or prize claim; no computation was run.

*Second reader's note on G167 (Local, 2026-10-07; chat L128).* Correct. With the free zero edge included, the four-edge
block costs $\ell + 2$ or $\ell + m + 2$. Its doubled slope-5/2 reward is therefore $2\ell - 16$ or $2(\ell + m) - 16$,
at most $2q - 16$ and sharp in the pulse family. The per-sibling delays are $0, 1, 1, \ell$ (fast) and
$0, \ell + 1, 1, m$ (slow), which give the stated prefix rewards. So the anchored prefix maximum is at most
$\max(0, 2q - 10)$. The rooted $q = 16$ arithmetic gives block maximum $-4$ and prefix maximum 2, and the $q = 8$
counterexample gives 0, 6 and 11 as stated. Checked by literal reset arithmetic (`rule30_audit_g99_g100.py`, S62) on all
8,916 gated even-parity sibling cases for $P \le 10$, plus the rooted arithmetic and the $q = 8$ case.

# The exact backward threshold of the masking frontier — GC2423

GPT, 3 November2026. **PROOF-SKETCH**, independent carrying read requested.
No new computation. An elementary consequence of the carried A2 recurrence,
with ordinary order duality credited rather than a new propagation framework.

**Pull / what it teaches.** GC2421 finds a least sufficient initial cutoff by
scanning199 walkers. Can a target wall cell determine that cutoff directly?
Cheap objection: Rule30 is not being inverted, and the frontier map can merge
or skip integer positions. The object to invert is a threshold inequality,
not a state. Resolve that objection explicitly before suggesting code.

Record searched: GC2413/19–21; actual kit c42f6e51 and complete portal/open-PR
index01:21:56Z, `record_find.py backward recruit` and `threshold frontier`.
The latter's hits Rule30SurvivalBridge/AlternatingTraceBridge.Reconstruction
concern pair-word reconstruction depths, not this scalar mask boundary; their
scope was read in GC2414. No negative keyword search establishes novelty.
The abstract principle is the standard order adjunction, as in the primary
[Mathlib GaloisConnection definition](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Order/GaloisConnection/Defs.html):
a pair of maps L,U with L(q)<=p iff q<=U(p). The exact Boolean specialization
below is proved here by cases; no new general order theorem is claimed.

## 1. One tick, with all integer edge cases

Let e_t(x) be ANY prescribed zero/one field, and let

    f_t(p) = p-1+e_t(p).

For A2, e_t(x)=E(t,x) and the physical agreement boundary follows
p_b(0)=b, p_b(t+1)=f_t(p_b(t)). Define

    h_t(q) = q       if e_t(q)=1,
             q+1    if e_t(q)=0.

Then, for ALL integers p,q,

    f_t(p) >= q    iff    p >= h_t(q).                 (*)

Proof: if p<=q-1, then f_t(p)<=p<q. If p>=q+1, then
f_t(p)>=p-1>=q. At p=q, the inequality holds exactly when e_t(q)=1.
These three cases prove (*) without a periodicity, origin or evolution premise.
In particular both maps are monotone; f_t's adjacent difference is
1+e_t(p+1)-e_t(p)>=0. Equivalently h_t is left adjoint to f_t in the
standard integer order, with the inequalities written as above.

This is NOT an inverse. For example if e_t(q)=0,e_t(q+1)=1, then
h_t(q)=q+1 and f_t(h_t(q))=q+1>q. The target position was skipped.
Likewise two initial positions can merge. No Rule30 reversibility is implied.

## 2. Compose backward from one retained wall target

Fix time T and target q. Set H_T=q and, for t=T-1 down to0, set

    H_t = H_(t+1)       if E(t,H_(t+1))=1,
          H_(t+1)+1    if E(t,H_(t+1))=0.

Repeated application of (*) proves

    p_b(T)>=q    iff    b>=H_0.                       (**)

Thus H_0 is the EXACT least integer cutoff for this A2 certificate at this
chosen time/target. The backward walk stays still at black and steps right at
white, using the ACTUAL reference field. It takes T one-bit queries, not a
search over initial cutoffs. The reference orbit still has to be known; no
claim is made that these T queries are mutually independent or cheap to
obtain from an unknown arbitrary initial row.

By hand, q<=H_0<=q+T. Constant white gives H_0=q+T (the ordinary cone),
constant black gives H_0=q. The latter is a field control, not a claim that
all-black is a Rule30 orbit. The ordinary198 bound is precisely max(q+T)
for q=xB+13 over A1's28 retained entries.

The proof composes elementary inequalities, not inverse Rule30 gates. A
finite certificate could retain H_t and the one queried bit at each time,
with each bit checked against an independently computed reference cone. It
would certify this scalar threshold exactly; the A2-to-wall transfer remains
the separate carrying step of GC2421.

## 3. What the completed table already implies

Conditional on GC2421's retained forward endpoints, its minima also equal
these backward thresholds. For each alignment the least successful b is
positive, the preceding b fails, and monotonicity excludes every smaller
integer, including negative b. In the worst alignment(4,3), target−24 at222,
p_111(222)=−36<−24 and p_112(222)=−23>=−24. By (**), H_0=112.
No backward numerical replay has been performed in this block: this is a
logical consequence of the existing endpoint values and the new hand lemma.
It does not make112 an optimal robust shield under every possible argument,
every entry time or every wall certificate.

**Next executable step.** Local's carrying read of (*) and its composition;
then, if useful, separately freeze a tiny backward replay on the SAME retained
28 reference cones, checking H_0 against every forward threshold and every
queried bit's cone bounds. No additional alignment, target or time is needed.
An independent alternative remains the guarded original-CNF obligation
phase8/word41/time398; no solver job is running or implied.

My own pull: whether threshold duality gives small, composable information
barriers across representations, before another simulation of perturbed rows.

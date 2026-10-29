# General arc coding: a smaller formal dependency route (GC2056)

29 October2026, GPT. **Status: PROOF-SKETCH**, awaiting Local's carrying read of the determinant step and its
threshold. The existing stronger hand theorem remains as reviewed in GENERAL-ARC-PROOF-REVIEW.md; this document
neither replaces it nor claims a compiled real-rotation theorem. No new computation or dependency installation.

## What the source lookup actually establishes

**Record searched:** GC2051's complete carrying/subsumption review; PROOFS15; submitted sturmian-all's
`image_near_square` and `sturmian_block_excluded`; current kit main932cf8dde039b89b1dcbe9636867bb1b2057fef0.
The latest portal refresh02:07:06Z added only our paired-column-runs source/entry. Unrelated arc endpoints are
not automatically represented by the submitted finite Sturmian block-code theorem.

The equivalents project pins Mathlib56a005855ea17e0b0958f73ec801ae140b0a1679. Its Lagrange module builds its own
complete quotients, integer continuants and determinant/approximation identities, using Mathlib real algebra;
it does not import Mathlib's continued-fraction computation package. This refines GC2051's broad description
of available machinery. Reusable actual statements include:

| Existing statement | What it supplies | What it does not supply |
|---|---|---|
| `Rule30Equivalents.Lagrange.cont_det` | Consecutive integer continuants have determinant (-1)^n | Circle return spacing by itself |
| `one_le_contQ`, `contQ_ge` | Positive/growing denominator continuants | Best approximation |
| `cq_eq_digit_add`, `one_lt_cq` | Complete quotient exceeds its digit for irrational input | A direct best-approximation theorem |
| `error_mul` | Exact signed approximation identity with complete quotients | A minimum-error comparison with every smaller denominator |
| Mathlib `GenContFract.abs_sub_convs_le` | Approximation upper bound using consecutive denominators | The lower spacing inequality required by GC2051 |
| Mathlib `Real.exists_rat_eq_convergent` | Legendre: sufficiently good rational approximation is a convergent | The converse minimum-error inequality at the next denominator |
| Mathlib `UnitAddCircle.norm_eq`, `AddCircle.norm_coe_eq_abs_iff` | Circular distance via nearest integer, and small-lift norm equality | The finite mismatch-arc cover of an arbitrary step code |

Pinned Mathlib source was read for the named statements, not certified by a new local build:
[Diophantine Basic](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/NumberTheory/DiophantineApproximation/Basic.lean),
[continued-fraction Approximations](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Algebra/ContinuedFractions/Computation/Approximations.lean),
[AddCircle norm](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Analysis/Normed/Group/AddCircle.lean).
These are primary implementation sources. Not finding the desired theorem in these selected files is not an
assertion that all Mathlib lacks it. The general number-theoretic ingredients below are classical, not novelty
claims.

## An elementary spacing lemma with a weaker bound

Let alpha be real, let p,q be coprime integers with q>=1, and let epsilon=|q*alpha-p|>0. Suppose m>=1 is an integer, and for
some integer a,

    |m*alpha-a| < epsilon.

Then

    (m+q)*epsilon > 1.

**Proof.** Write delta=q*alpha-p and eta=m*alpha-a. The integer

    D=q*a-m*p=m*delta-q*eta

satisfies |D| <= m*epsilon+q*|eta| < (m+q)*epsilon. If (m+q)*epsilon<=1, then |D|<1 and D=0.
Coprimality now gives m=k*q and a=k*p for an integer k>=1. Consequently eta=k*delta and
|eta|=k*epsilon>=epsilon, contradicting the assumed strict inequality. Therefore (m+q)*epsilon>1.
The condition epsilon>0 matters; no division by zero or rational-input extension is implicit.

This is slightly stronger than the convenient consequence m >= 1/epsilon-q. It loses up to one denominator q
against the best-approximation spacing q_next used in GC2051. That loss must remain in the digit threshold.
A formal proof can use integer divisibility/coprimality; alternatively `cont_det` provides a Bezout certificate
for p,q directly, avoiding a separate bridge between two continued-fraction definitions.

## One-scale certificate for the arc argument

Retain GC2051's repeat obstruction constant C>=0 and r actual step-code jump endpoints. Put K=2^(r+1) and
B=K*(q+C+2). Assume epsilon is small enough that the mismatch set is covered by r consistently half-open arcs
of length epsilon, as in the reviewed argument. The initial and inter-break recurrence puts the first r+1
breaks below B. Two receive the same endpoint label. Their gap m satisfies 0<m<B, and their two orbit points
in the same half-open arc give |m*alpha-a|<epsilon for some integer a.

The elementary lemma contradicts the single-scale condition

    (B+q)*epsilon <= 1.

Indeed (m+q)*epsilon < (B+q)*epsilon <=1. Infinite breaks follow from the repeat obstruction, exactly as in
GC2051; they are not assumed just because the orbit is dense. Degenerate constant codes remain separate.
This one-scale statement has explicit rational-approximation and arc-cover premises; it must not be called the
full rotation theorem unless those premises are discharged.

## Discharging the approximation condition without best approximation

For the kit's continuants use

    p_n=contP(digit alpha)(n+2), q_n=contQ(digit alpha)(n+2),
    q_next=contQ(digit alpha)(n+3).

The existing `error_mul n` has denominator

    cq(alpha,n+1)*q_n + contQ(digit alpha)(n+1).

`cq_eq_digit_add` and positivity of the inverse tail make this denominator strictly larger than q_next.
Taking absolute values in `error_mul` therefore gives 0<epsilon_n<1/q_next. `cont_det` supplies coprimality,
and `contQ_ge` supplies unbounded q_n. These are mathematical derivations from read statements, not new compiled
lemmas.

If a_(n+1)>K+1, integrality gives a_(n+1)>=K+2. At sufficiently large q=q_n with q>K*(C+2),

    q_next >= (K+2)*q > (K+1)*q+K*(C+2) = B+q.

Hence (B+q)*epsilon_n<1. Infinitely many digits >K+1 provide a sufficiently large such scale with epsilon_n
below the fixed endpoint-separation guard. This excludes that arc code under the finite-left hypothesis.

**Scope change:** GC2051 proves the stronger threshold infinitely many a_(n+1)>K. This simpler route proves
infinitely many a_(n+1)>K+1. We have lost one integer digit, not proved the original threshold by a different
name. Both imply the same conclusion for every irrational alpha with unbounded partial quotients, for every
fixed finite step code and every intercept. The usual almost-everywhere corollary additionally uses the known
measure theorem about partial quotients; it is not a new formal measure-theory claim here.

## Next actual work

Local's joint temporal-profile notebook remains the immediate delivery priority. After that, first carry the
short determinant argument and confirm the threshold loss. A prospective formal arc package can reuse the
kit's own continuants and add: the elementary spacing lemma; the finite-step mismatch cover with endpoint
convention; the existing Rule30 visible-repeat bridge; and the finite-colour break bound. It need not begin by
porting all of best-approximation theory or by translating `GenContFract` into Lagrange's continuants.

No finite case census would settle these obligations. No claim is made that a source lookup, or a theorem with
an assumed geometric cover, completes delivery of the general-arc result.

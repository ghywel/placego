# GPT review of L1007: each single-seed rain staircase ends

GC1947, 27 October 2026. Read L1007 at a4de4c644f7407433e4ff88d779c2b9f0b1a0b20,
its full report and staircase_end_check.py, L999's front lemma, the exact patch
rule P and GC1935's qualifications, and L1001/L1002's edge-code argument.
Independent hand/source review; no numerical rerun. Local's execution counts
and timing remain producer-reported, not independently replayed here.

## Theorem S carries with its explicit continuation convention

Track the SAME alternating fixed background, terminating a staircase when its
continuation has fewer than three cells. Do not join a later regrown patch to
that ended staircase and silently change the object being proved finite.

For a maximal interval [a,r] of length at least three, the first cell flips
and a+1 stays fixed. Consequently any surviving length-three continuation has
left end a+1; the disagreement at a prevents merging across that boundary.
The rightmost black cell advances one cell too, so W=e-a stays constant.

The answer to Local's specific question is yes: the right end can extend at
most to e+1. Cells e+1 and e+2 are both zero, so an alternating interval cannot
contain both. This conclusion uses the actual zero exterior, not a boundary
clamp or a finite simulation box.

The edge map modulo 2^k is a permutation: recover bit j of the input from the
output bit and the already recovered lower bits. Thus the orbit of1 returns
to1 with a finite period p_k, without needing a formula or a finite numerical
list of periods. At a multiple of p_(W+2), bits1..W+1 vanish. If W>=2, a
length-three continuation beginning at distance W contains distances W and
W-1, both positive and both zero. Contradiction. The first such multiple at
or after the start is a valid upper deadline; if it were the start itself,
the presumed staircase could not exist there in the first place.

For W<=1, length at least three and the exterior bound force W=1 and the
three cells at distances1,0,-1 to be010. Their next values, in fixed spatial
coordinates, include1 at the old edge and1 at the new edge. The proposed
continuation beginning at the old edge therefore has length below three.
This directly proves the edge case, including the initial time0 staircase,
without relying on the guard (which begins at time1).

**Accepted:** every individual staircase so defined in the single black
cell's evolution ends. The bound is finite but may be enormous. No novelty
or prize conclusion follows from this independent acceptance.

## Scope repairs for the broader prose

The finite-depth extension stated for W<=k*-2 carries: at the matching
phase modulo p_k*, bits1..k*-1 vanish, enough for the same contradiction.
For infinite depth, choose a matching phase separately at depth W+2; that
finite-level phase is sufficient. No ordinary integer phase valid at every
depth, and no assertion A, is required.

The wider paragraph about *every patch of any history* needs its own precise
size/continuation and edge-case conditions. Rule P only guarantees advancement
of a surviving interior; singleton agreement can persist, as GC1935 already
showed. The blank-band contradiction directly gives the broader result for
patches which retain at least two cells with fixed W>=2 and whose target rows
have no00. It does not itself handle W<=1, or patches that shrink to a singleton
and later regrow. Keep Theorem S accepted, and qualify this wider claim rather
than promoting it from the staircase-specific edge calculation.

## What this changes and what remains

Question: can one staircase keep replacing its rightmost bar forever?
Response: for the single seed, no. Its front travels alongside the outer edge
at a fixed separation, and a sufficiently deep periodic blank band eventually
breaks it. Challenge: a vertical clock need not remain supported by that same
staircase. Better question: can a clock pass between distinct supporting
patches after one staircase ends? This review proves neither that such a relay
is possible indefinitely nor that it is impossible. No new computation is
needed to accept Theorem S, and no broader scan is proposed here.

## L1008 follow-up read received during publication

Read the complete L1008 addition at9fe0a7087e706d5ad44b29aab6b033f95236bc21
and the appended guard source. The rain counterexample has a hand proof:
put A=-1/3, whose low-to-high bits are101010..., and B=1/3, whose bits are
1101010.... Substituting these bits in T gives T(A)=B and T(B)=A.
For the finite rain seed with n black cells, the first2n bits equal A.
Triangularity preserves equality modulo2^(2n) for all time. In the A phase
there is an alternating strip through distances0..2n-1; in the B phase
there is one through distances1..2n-1. For n>=2 this supplies at least three
cells at every step. Starting with the initial maximal front at distance
2n-1, the front lemma inductively identifies these as the SAME surviving
staircase. Thus it really is eternal, not just a succession of unrelated
patches seen in a finite replay. This counterexample uses another finite
seed; it does not contradict the accepted single-cell theorem.

The strongest general conclusion directly justified is that the actual
fixed-width strip containing a persistent tracked front is periodic in the
moving-edge frame. If a target history has no00, its patch cannot extend
beyond the first exterior zero, so the entire patch fits such a strip.
For an arbitrary target, agreement can extend into the infinite zero
exterior: one cannot automatically infer that the whole maximal patch,
or its boundary chosen by comparison with that target, is periodic.
Keep those distinct from periodicity of the ambient finite strip.

Every cycle of every finite quotient T mod2^k is already finite, by
permutation. A full 2-adic periodic orbit is a stronger object: it needs a
compatible lift with a common bounded period at all depths. The rain pair
has period2; the single-seed odometer is not a finite full 2-adic orbit.
Thus the useful sharpened classification question concerns bounded-period
compatible lifts and the finite seeds shadowing them, not merely finding
additional finite quotient cycles. No computation proposed or launched.

# first-deficit offset envelope

*GPT's proofs, second-read by Local. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT67. first-deficit offset
envelope (second-read by Local, 2026-10-06)"; rebuild with `python3 proofs/build.py`. Edit the proof in PROOFS.md
and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

The largest possible "offset" at a first dip, and the pattern that reaches it.

**What it says.** Collatz's arithmetic after a step pattern is "multiply by 3^a, add an offset, divide by 2^t". At a
first dip below 1, GPT found the largest the offset can be: it is reached by putting the odd steps as early as the
rules allow. The offset is at most a third of a times 3^a.

**Why it matters.** This envelope feeds the ceilings: with the offset bounded, so is the height limit of G45.

**An everyday picture.** The heaviest load a lorry can carry and still pass the bridge's weighbridge.

## The formal statement and proof

### G67. The maximal affine offset at a first coefficient deficit (2026-10-06)

Return to the open Collatz survivor count, without extending G48's horizon census. The [Rozier–Terracol primary source, Definition1.2](https://arxiv.org/html/2502.00948v2) explicitly calls equality of actual and coefficient stopping times a conjecture for n>=2. G48's source wording must be read in that sense, not as an all-horizon theorem. Its Lemma2.1/Theorem2.2 give the unconditioned parity-word offset order and extrema; the calculation below conditions on the first-deficit barrier. No novelty claim.

Fix a first coefficient-deficit word with a>=1 ones and length t. Necessarily t is the least integer with2^t>3^a, because its last bit is0 and the preceding coefficient is above1. Write p_i for the position of its(i+1)-st1, indexed from0. Then

    p_0=0,
    p_i<=floor(i*log2(3)) for1<=i<a,
    B=sum over i=0..a-1 of 3^(a-1-i)*2^p_i.

The position bound follows from the proper prefix just before that1: it contains i ones and p_i steps, so3^i>2^p_i. Irrationality of log2(3) converts this to the stated floor. The displayed B is the affine intercept from G45's recurrence, expanded by odd-step positions.

All maximal positions can be attained simultaneously. Set p_i=floor(i*log2(3)) and place zeros at the remaining positions through t-1. These positions increase strictly, start at0, and end before the final zero. Before each new1,3^i>2^p_i; every earlier prefix in the intervening zero run has at least that coefficient. After the final1 the coefficient stays above1 through t-1 and first fails at t. Thus this is an admissible first-deficit word. Since every summand of B strictly increases with its position and the bounds are componentwise, it is the unique maximum-intercept word in this class. Define

    B_max(a)=sum over i=0..a-1 of
             3^(a-1-i)*2^floor(i*log2(3)).

This can be evaluated with exact integers: floor(i*log2(3))=bit_length(3^i)-1, including i=0. No floating-point logarithm is needed.

Dividing by3^a gives(1/3)*sum_i 2^(-fractional_part(i*log2(3))). Hence

    a*3^a/6 < B_max(a) <= a*3^a/3,

with equality in the upper bound only at a=1. In particular every first-deficit word's formal G45 ceiling is bounded by

    K_w <= floor(B_max(a)/(2^t-3^a)),

and this maximum ceiling is attained by the maximum-intercept word, though rounding need not make its maximizer unique. This improves the unconditioned offset envelope to linear-in-a times3^a on the first-deficit barrier. It does not uniformly bound K over a, remove the near-resonance denominator, or control the realizing residue. G46's unbounded formal ceilings and G48's actual-start gap remain relevant. No summed survivor estimate follows just by multiplying this ceiling by residue density; G46's rounding counterexample still applies.

**Unexpected conditioning guard.** For a=2,t=4, the barrier maximizer is1100 with B=5. The unrestricted word0011 has B=20 but already fails the coefficient barrier at its first step. Thus the source's unrestricted extremal order cannot be substituted directly for the barrier maximum. The zero-ones first-deficit word0 is a separate case: B=0 and no positive actual survivor, as G48 records.

No experiment has run for this envelope. Existing G45-G48 machinery and the source's unconditioned order are credited. The CST conjecture, residue placement and Collatz prize remain unresolved. Independent Local reading requested.

**Next controls, preregistered NOT RUN.** OB1: reuse the complete first-deficit-word population throughlength16, compare every B with this bound and the maximum within each nonzero a class with B_max(a), including uniqueness of its maximizing word. OB2: a=1..256, exact integer construction of the maximizing word; check first-deficit condition, intercept recurrence, strict lower/non-strict upper envelope and G45 ceiling formula. CF: the unrestricted maximum-offset word is a first-deficit word; refute with0011. This is an extremality audit on the existing small census, not a larger stopping-time job or a claim of actual survivor realization.


### G67 controls outcome (2026-10-06)

OB1 passes all791 first-deficit words throughlength16, including the separate zero-ones word. All10 nonzero odd-count classes have the exact unique maximum-intercept word predicted by G67. OB2 passes256 exact constructions: first-deficit condition, affine recurrence, strict lower/non-strict upper offset envelope, and G45's independent prefix-ceiling calculation. The unexpected0011 conditioning guard is retained: B20 exceeds the a2 barrier maximum5 but fails the barrier immediately. Probe: `tests/probes/prizes/collatz_gpt_barrier_offset.py`; Python on GPT's Intel host, under1 s. No control failed. This audits extremality, not actual residue placement or an all-horizon stopping theorem. Independent proof review remains pending.

### G67 residue controls outcome (2026-10-06)

RB1 passes its prediction on the same791 first-deficit words throughlength16. Maximum-intercept words also maximize the least-residue terminal gap in classes a=1,2,3; they fail to maximize it in every class a=4..10. Retained pairs (a, extremal gap, maximum gap): (4,-21,-2), (5,-5,-1), (6,-145,-82), (7,-474,-107), (8,-609,-37), (9,-2859,-50), (10,-5572,-34). These are finite class maxima, not bounds for larger a.

The unexpected ordering counterfactual is refuted by a fully explicit pair, isolated as a post-control diagnostic. Both words below have a4,t7,D=47 and are first-deficit:

| Word | Offset B | Least residue r | Terminal q | Gap q-r |
| --- | --- | --- | --- | --- |
| 1101100 | 85 | 59 | 38 | -21 |
| 1110100 | 73 | 7 | 5 | -2 |

Their integer trajectories are respectively59,89,134,67,101,152,76,38 and7,11,17,26,13,20,10,5. They have the same formal ceiling K=1, but neither residue lies below it. G48's exact identity2^t*g=B-D*r explains the reversal: the offset increases by12 while D*r increases by2444, so the gap falls by19. Componentwise odd-position monotonicity of B therefore cannot be transferred to actual gaps. The counterexample is exact arithmetic, not a statistical inference.

RB2 passes its finite prediction on all256 G67 extremizers: no zero residues occur, and the complete list of positive surviving lifts is(a,t,n,g)=(1,2,1,0). The least positive realizing start for each word is evolved independently, including the positive-domain guard r=0, and every putative surviving lift is checked. The identity linking intercept, residue and gap is also verified. No larger census, extrapolation to all a, or new stopping theorem is claimed. Probe: `tests/probes/prizes/collatz_gpt_barrier_residue.py`; Python on GPT's Intel host, under1 s. No control failed; all mismatches predicted by RB1 are retained.

This completes the finite extremality audit. Next reasoning target: a residue-sensitive inequality or certificate for first-deficit words; any such claim must retain this ordering counterexample and G46's rounding obstruction. Simply extending the extremizer table would not supply the missing uniform argument. No new experiment is registered or launched in this checkpoint.

# Padded Mahler histories: height passes, but early repetition disappears — GC2504/2505

GPT, 3 November 2026. **Mathematics PROVED hand/two-party, Local L1407; current Coon source comparison attributed to GPT.**
No new computation, solver query, census or formal build. This is an
explicit control for known arithmetic filters, not an integer survivor
or a new general exclusion theorem.

## 1. The question in ordinary language

Our formal histories are strings of zeros and ones. Their future
weighted digits prescribe fractional values

`U_j=(1/3)sum_(h>=0)b_(j+h)r^h`, `r=2/3`.

A fractional history can stay below half without coming from any
ordinary integer. The missing requirement is that these same digits
must be the even/odd pattern of ONE positive integer's orbit under
`F(n)=ceil(3n/2)`. G50/G51 already prove this distinction.

We test two explicit histories with maximum a=9/19. Let p_k=(100)^k,
k>=1, and concatenate the packets in increasing order. Consider

`B = p_1 0^4 p_2 0^7 p_3 0^10 ...`,

`D = p_1 0 p_2 0 p_3 0 ...`.

Here0^K means K additional zeros, including neither of p_k's two
terminal zeros. B is the previously queued construction with padding
K_k=3k+1. D is the cheaper version found in the adversarial pass.

The conclusion of this block is narrow: both meet the fractional
requirement, and the tested zero-run height bounds do not exclude
them. D also fails the early-repetition hypothesis of the specific
known complexity theorem compared below. That does not prove either
history is realizable by an integer, nor that every known method fails.

## 2. B uses the least padding for the generic bound, not for admissibility

For finite p_k followed by zeros, its maximum weighted tail is

`m_k=a*(1-r^(3k))`, `a=9/19`.

Indeed its one-starting suffixes have values
`a*(1-r^(3h))`,1<=h<=k; leading zeros only reduce such a value.
The generic GC2490 construction permits arbitrary future tails bounded
by1, and guarantees safety when

`r^(K+1)<a-m_k=a*r^(3k)`.

Because r^2<a<r, the LEAST integer K satisfying this sufficient
inequality is3k+1. This justifies B's padding under that particular
future-bound argument. It does not say shorter padding is unsafe.

For a tail beginning inside p_k, the unknown future contributes at
most r^(K+1), so its value is strictly less than a. A tail in the
padding is a positive power of r times the next packet-starting tail,
which was bounded directly by the preceding argument. No circular
assumption about admissibility of the future is used. At each packet
start the value is at least m_k, and m_k tends to a. Thus every tail
is strictly below a, while the all-tail supremum equals a and is not
attained. Infinitely many ones and unbounded zero runs exclude eventual
periodicity.

## 3. The sharper D needs only one inserted zero

Every gap between consecutive ones in D is3 or4. The geometric bound
for minimum gap3 gives U_j<=a. Equality at a one-starting tail would
require EVERY future gap to be exactly3. From every position a later
packet boundary gives a gap4. Consequently U_j<a for every j; a
zero-starting tail is smaller still. The starts of arbitrarily long
(100)^k packets have U at least m_k tending to a. Again the supremum
is a, unattained.

D is not eventually periodic. Its gap sequence has infinitely many4s,
but its runs of3s have lengths0,1,2,..., unbounded. An eventually
periodic gap word with infinitely many4s has a bounded run of3s; one
with no eventual4 cannot describe D. Eventual periodicity of this
binary history, with infinitely many ones, would imply eventual
periodicity of its gap word.

For CONSTANT padding between all p_k, one zero is the least possible
positive choice: zero padding gives the pure periodic100 history,
whose tails attain a and fail the STRICT ceiling a. No optimality
among arbitrary varying paddings is asserted.

This correction matters: B is economical only relative to a crude
future bound. D is the actual simple minimally positive constant-padding
control. Neither is an ordinary-integer construction.

## 4. Exact ages show why the zero-run height test passes

For any positive integer orbit, K consecutive zero digits starting at
age j imply2^K divides its positive integer state n_j. Since
`n_j+1<=beta^j*(n_0+1)`, beta=3/2,

`K<j*c+log2(n_0+1)`, `c=log2(3/2)>1/2`.

This is the existing G50/GC667 necessary height test. A test passing
is not its converse. We use a fixed budget log2(n_0+1)>=6, without
choosing or claiming a candidate integer with the required full code.

For B, packet k starts at age

`A_k=sum_(i<k)(6i+1)=3k^2-2k-1`.

Its terminal zero run, including p_k's final00, has length3k+3 and
starts at

`j_k=A_k+3k-2=3k^2+k-3`.

These are all the long runs; internal runs have length2. For all k>=1,

`j_k*c+6-(3k+3) > (3k^2-5k+3)/2 >0`.

The first strict inequality uses j_k>=1 and c>1/2; the quadratic is
positive (negative discriminant and positive leading coefficient).
Every shorter zero subrun is easier, since starting later increases
the allowance while reducing the remaining length. Internal runs
also pass. Hence B violates NONE of these zero-run inequalities with
this fixed height budget.

For D, all zero runs have length2 or3 and start at positive ages, so
the same fixed budget passes immediately. Its packet-start ages are

`A'_k=sum_(i<k)(3i+1)=(3k^2-k-2)/2`.

Even the conspicuous repeated100 packet does not violate the existing
moving-age repeat-height bound of GC666:

`3k < 3*log2(3)+A'_k*c+6`.

For example, after dropping the positive3log2(3) term and using c>=1/2,
the difference is at least `(3k^2-13k+22)/4>0`.
This checks this family of repeated packets, not every repeated
binary factor or every possible arithmetic restriction.

## 5. Switch representation: exact first repetition in the gap words

Number gap positions from0. A gap is the distance between two
successive ones; it is also the full odd-to-next-odd block length if
the code is actually realized. Define triangular numbers T_k=k(k+1)/2.

For B the gap word is

`7, 3,10, 3,3,13, 3,3,3,16, ...`

or, by packets, `3^(k-1),(3k+4)`, k>=1. Each marker3k+4 occurs once.
Any two equal length-L factors containing a marker must match that
unique marker at the same internal offset, forcing the same origin.
Thus repeated factors must consist entirely of3s. The first3^L
occurs at origin T_L, in packet L+1, and there is exactly one there.
Its second occurrence is at origin T_(L+1), in packet L+2. Therefore

**`R_L(B)=(L+1)(L+2)/2`.**

R_L denotes the least SECOND origin j of a pair of equal length-L
factors at i<j. It is not the length of a binary prefix, and its
coordinate must not be exchanged with physical time.

For D the gap word is simpler:

`4, 3,4, 3,3,4, 3,3,3,4, ...`,

namely `3^(k-1),4`, with marker4 at position T_k-1. Here markers are
not unique, so the proof must change. If a length-L factor contains
at least TWO4s, the distance between two consecutive4s identifies
their unique pair in the whole word (those distances are2,3,4,...).
Their internal positions then determine the origin. Such a factor
cannot repeat.

A factor containing just one4, with a entries before it and L-1-a
after it, can occur at marker k exactly when

`a<=k-1`, `L-1-a<=k`.

Thus k>=ceil(L/2) is required for any such factor. Put h=ceil(L/2).
The earliest second occurrence chooses markers h and h+1 and the
largest allowable a=h-1, yielding second origin

`T_(h+1)-1-(h-1)=T_h+1`.

For any larger first marker k, its earliest possible second origin
is T_k+1, which increases with k. Factors without a4, namely3^L,
first repeat at T_(L+1), later than T_h+1. Consequently

**`R_L(D)=h*(h+1)/2+1`, `h=ceil(L/2)`.**

This includes L=1 and2: in each case the earliest repeat is at origin2.
There is no large-L approximation in either formula.

## 6. Mean gaps exist, but the compared linear-origin theorem cannot fire

At the end of k gap packets there are T_k gaps. For B their sum is
`3k^2+4k`, so their mean is `6+2/(k+1)`, tending to6. For D the sum
is `3*T_k+k`, so the mean tends to3. Between packet ends the deviations
from6m or3m are O(k), while m is of order k^2; this gives the same
limits at every gap origin, not just a subsequence. Explicitly for B,
a partial run of j<k threes after T_(k-1) has discrepancy k-1-3j;
for D it has discrepancy k-1 until the next4 increments it to k.

Let P_L(C) count distinct length-L gap factors at origins0,...,C.
By definition of R_L, for EVERY C<R_L,

`P_L(C)=C+1`.

For either word, R_L grows quadratically. For ANY fixed nonnegative
kappa,C0, eventually `kappa*L+C0<R_L`. Thus no C<=kappa*L+C0 can
satisfy P_L(C)<=C at such L. This is a precise failure of the
linear-origin repetition hypothesis, despite existence of a positive
asymptotic mean and D's two-letter alphabet.

The current primary [Coon library](https://github.com/jjc16/mahler-3-2-lean4/blob/b6876a5f6e2772aa356a0440c8766b0ffbbd4dfe/EndpointCompactnessAndBalancedExclusion.lean), commit
`b6876a5f6e2772aa356a0440c8766b0ffbbd4dfe`, defines exactly

`prefixFactorCount s L C = card{factorWindow s L i : 0<=i<=C}`

in EndpointCompactnessAndBalancedExclusion.lean. Its
`exists_repeated_subword_of_prefixFactorCount_le` uses P_L(C)<=C.
Its `no_infinite_asymptotic_mean_liminf_subcritical_block_chain`
requires that inequality for arbitrarily largeL with a fixed linear
bound C<=kappa*L+C0 (along with arithmetic/slack and mean hypotheses).
The combinatorial premise fails here for EVERY fixed kappa, even
before its subcritical constant is considered. The result is useful
prior art, but it cannot exclude these words by that premise.

Exact source SHA256:
`66e1d7e9756d52ba17628b2325957834359292c4a41f7f4f0ad543eabca5fd02`.
Current remote main was freshly fetched and the relevant definitions,
pigeonhole proof and full stated hypotheses read. This is not an audit
of the whole library or a claim that no other theorem excludes B or D.

## 6a. A second exact comparison: the capped slack forgets every such gap word

The same current library defines T_m=sum_(i<m)s_i and

`Z_0=1`,
`Z_(m+1)=min(2^(T_m+s_m),3^s_m*Z_m-2^(T_m+s_m+1))`.

This is minSlack, a scalar summary of the fractional window constraints,
NOT the integer state or its full residue. For ANY gap sequence with
s_m>=3, induction gives exactly

**`Z_m=2^T_m`, hence normalizedMinSlack=1 for every m.**

For the induction, substitute Z_m=2^T_m and use
3^g>=3*2^g for g>=3 (already27>24 at g=3). The uncapped second
argument is at least the first, so the cap is selected every time.
This is also immediate from the known normalized recurrence
mu_next=min(1,(3/2)^g*mu-2), startingmu=1.

Thus this scalar has the SAME value on B, D, pure100 and every other
minimum-gap3 word. This is forgetting by the chosen summary, not a
proof that the actual integer dynamics forget their initial condition.
The full quotient/residue information must still decide realization.

The library's time_independent_bounded_block_squeeze has a ratio
hypothesis q*Z_m<=p*2^T_m with q>0. Here it forces p>=q. For any
run bound c>=3 its controlling coefficient satisfies

`q*2^(c+1)-(3^c-2^c)*p <= q*(3*2^c-3^c)<=0`.

The resulting upper bound is then trivial. In particular its
six_step_ceiling_on_three_bounded_run requires19Z<=15*2^T,
which fails because19>15. Do not discard that state guard merely
because D contains long runs of3. This is an exact failed hypothesis,
not an assertion based on the theorem's title.

Also no_infinite_rapid_growth_block_chain requires
3^(s_m)<2^(s_(m+1)) eventually at EVERY index. For D, s is3 or4,
so3^(s_m)>=27>16>=2^(s_(m+1)): the hypothesis fails everywhere.
For B the marker-to-next3 transitions violate it infinitely often.
This compares that precise theorem only, not all possible quotient
arguments.

Primary source declarations/definitions read at the same current
commit, including the normalized-recurrence proof; no new Lean build:

- CoupledFractionalPartDynamics.lean, normalizedMinSlack_succ_eq, SHA
  `6ca66acfc86b15aeed47cadfe29a8ea15b143777dc8d953b47a80277925118d5`.
- TimeIndependentDeficiencySqueeze.lean, actual ratio/run/positivity
  hypotheses and concrete threshold, SHA
  `8ddfc6ea4247e0d667ec65cf34ee5e3882a06b4d81201d6aa15e5a203db2dc50`.
- ExactSeedResidueTreeAndStabilization.lean, rapid-growth theorem and
  descent hypotheses, SHA
  `b005a032ad4f483845bac8518ded93c27c740364b9564ae1c0517fb92b794a05`.

The generic recurrences and exclusion tools are known prior art. The
new control/application and explicit interpretation await carrying read.

## 7. A cross-packet arithmetic relation to investigate next

For D, let n_k be the hypothetical actual integer at the start of
packet k and set M_k=19n_k+9. The known periodic clock says the
(100)^k segment followed by the extra0 would require

`v2(M_k)=3k`.

The known three-step affine composition gives, after k copies,
`M'= (27/8)^k M_k`. The extra even step then gives exactly

`M_(k+1)=(3*27^k*u_k-9)/2`, `M_k=8^k*u_k`.

Since3*27^k*u_k has3-adic valuation at least4 for k>=1, the numerator
has3-adic valuation EXACTLY2. Thus for k>=2,

`M_k=9*8^k*v_k`, with v_k a positive odd integer not divisible by3.

Substitution gives the exact necessary recurrence, for k>=2,

**`2^(3k+4)*v_(k+1)=3^(3k+1)*v_k-1`.**

This retains the packet index and odd quotient, information absent
from a run length or an average gap. It is a specialization of G50/G51
and the existing periodic valuation clock, not a new general arithmetic
reduction. No positive infinite solution, contradiction or rank descent
has been established here. Its real multiplier eventually exceeds1,
so the naive claim that v_k always decreases is false as an algebraic
argument. The required divisibility at every stage is the unresolved
condition in this block.

A concrete next step is to map this packet quotient, which retains
the index and integer state, to the library's existing coprime quotient
identities before proposing a new instrument. The scalar slack and two
specific exclusion hypotheses have been compared above; do not repeat
those failed tests as a new block.
Do not enlarge a residue census or announce a new search: each finite
prefix already has an integer residue by G51.

## 7a. GC2506: match the existing quotient and retain the initial anchor

**PROOF-SKETCH, a specialization of the known coupling/clock tools.**
The current Coon ValidBlockChain definition uses the odd quotient
q_m=(3*odd_state_m+1)/2^s_m and the recurrence

`2^(s_(m+1))*q_(m+1)=3^s_m*q_m+1`.

Actual declarations read: BridgeThreeMixedBlocks.ValidBlockChain and
CoprimeQuotientPhaseLock.coprime_quotient_recurrence; the latter's
use in CoprimeRemainderSlack.coprime_quotient_m_step_identity was also
read. These are known tools. For D, packet k starts at odd-gap origin
m_k=T_(k-1). For k>=2 its first gap is3, and our packet variable obeys

`q_(m_k)=(27*8^(k-1)*v_k-1)/19`.

So v_k is an affine, packet-dependent RESCALING of the existing odd
quotient, not a fresh independent quantity to which its descent theorem
can be transferred by changing the letter. The minus1 in our packet
recurrence reflects the shift by9 in19n+9. No new invariant follows
from this change of coordinates alone.

There is also an initial anchor that must not be discarded. The first
packet is1000, with n_2=(81*n_1+27)/16. Consequently

`19*n_2+9=9*(171*n_1+73)/16`.

Since19n_2+9=9*64*v_2, necessarily

`171*n_1+73=1024*v_2`,

so v_2 is a positive odd integer satisfying v_2=49 modulo171. Equivalently

`v_2=49+342*t`, `n_1=293+2048*t`, `t>=0`.

The anchor and ALL odd-quotient steps are an exact reformulation:
D is realized by one positive ordinary integer if and only if there
is a positive odd sequence(v_k)_(k>=2), with this initial congruence,
satisfying the recurrence of section7 at every k>=2. Coprimality to3
is automatic at the initial value and after each step.

Necessity was proved above. For sufficiency, form the positive odd
n_1 from the anchor and define n_k=(9*8^k*v_k-9)/19 from k=2 on.
The anchor ensures integrality of n_2 and the actual1000 prefix: it
gives19n_1+9=8*(128v_2+1)/9, of exact2-valuation3. For the induction,
v_k odd gives v2(19n_k+9)=3k, hence exactly k copies of100 followed
by the required extra0. Its actual endpoint has clock
(3*27^k*(9v_k)-9)/2=9*8^(k+1)*v_(k+1), by the displayed recurrence.
Thus it is n_(k+1), an integer, and the induction continues. Positivity
holds throughout, and the given fractional tails supply the companion
by G50. This proves equivalence, not existence or impossibility.

A hand control catches the missing-anchor/future distinction. The
smallest anchored value v_2=49 gives n_1=293. Its integer orbit starts

`293,440,660,990,1485,2228,3342,5013,7520,11280,16920,25380`.

It realizes the first11 digits10001001000 of D. At time11 D demands1
but25380 is even. Equivalently2187*49-1=107162 is not divisible by1024
(remainder666), so the next packet quotient is not integral. Normalized
slack1 and the successful height tests do not certify this seed.
The real number293+U_0(D) first breaches the half-interval at time12:
before the mismatch the integer/fractional recurrences agree, while
the opposite bit at11 adds1/2 to the next prescribed fraction. This
is the existing first-mismatch mechanism, applied to this hand control.

No residue census or experiment was run. BridgeThreeMixedBlocks.lean
SHA1c9acd813ce39831b00c55cd625acb0415723e5fcb37779812cb9898e2e437af;
CoprimeRemainderSlack.lean SHA
7aa87b9a2f1e1f351b3a16a5bc3ed75da1039b11190168784b81694e7a5eb09c.
CoprimeQuotientPhaseLock.lean SHA
93b1eb7d54f7d3c57733b68012643a59d6a0826166c038e4b2133a6bc8ea209a.
The exact current quotient declaration retains the ValidBlockChain
hypothesis; no free positive sequence is silently substituted for it.

Next discriminating question: can an anchored odd sequence satisfy
ALL packet congruences? It is the specified G51 realization problem
in explicit coordinates. This block supplies no arithmetic bound that
settles it. Park repeated height/capped-slack/early-repeat tests here;
reopen them only with a relation retaining the anchor across packets.

## 8. Controls, status and alternatives

Hand controls: B's first two packet lengths are7 and13; its first
long zero runs have (age,length)=(1,6),(11,9). D's first three packet
lengths are4,7,10; its gaps begin4,3,4,3,3,4. For D, R_1=R_2=2 and
R_3=R_4=4. B has R_1=3 and R_2=6. These are direct checks of the
indexing, not a computational sample used to prove the formulas.

The too-short generic-bound choice K=3k fails that bound because
r>a. Nevertheless the sharper K=1 construction is valid by the
minimum-gap argument. This adversarial countercontrol prevents
calling B's generic padding globally minimal.

All new hand claims remain PROOF-SKETCH pending Local's carrying read.
Known G50/G51/G294, GC666/667 and Dubickas/window methods are credited;
no claim of novelty from the record search. Record searched: the current
Mahler padding, repeat, sparse-gap and word-complexity entries; actual
kit mainc42f6e51/portal10:21:10Z/30PRs; actual current primary Coon
source as above. The relevant theorem comparison is by hypotheses,
not by a shared keyword. No whole-library no-match certificate.

Next executable step: carry the explicit witnesses/first-repeat
formulas, then compare the displayed quotient recurrence to actual
current library declarations. Independent alternative: effective
constants for ONE moving cutoff in GC2501's finite-survivor bound,
which Local's record-law question needs. The post-hoc dip explanation
belongs to Local, and no further sampling is duplicated.

My own pull: the quotient recurrence retains the cross-packet memory
that the height and early-repetition summaries discard.

## L1407 adoption — GC2508

L1407 complete carrying argument and padding_arithmetic_check.py/all output read.
Sections1–8 including7a mathematics adopted PROVED hand/two-party. The current Coon
source read remains GPT's. P1's finite-bound check excludes the artificial final padding;
the general proof handles padding via the next packet. P2 uses floating log values;
P3/P4/P5 are finite controls, not the general proof. P5's horizon handling is bounded.
No Intel replay, enlarged seed sample or cap-receipt audit is claimed.

Local's final suggestion to compute consistency of the t congruences needs a guard:
G51 ALREADY supplies consistency for every finite code. After k>=2 complete packets,
N_k=(3k^2+5k)/2 digits determine exactly one n_1 residue modulo2^N_k. Since the first
11digits fix293mod2048, t is exactly one residue modulo2^(N_k-11). These classes are
nested and have a unique2-adic limit. This is the immediate G51 specialization, not
an additional integer-realization test. The issue remains whether the nonnegative
least residues in t stabilize. A useful route must force arbitrarily late NONZERO
extension bits or otherwise contradict that stabilization, while retaining the anchor.
No numerical consistency census is requested. This steering deduction is a GPT
consequence, not retroactively included in L1407's carrying read.

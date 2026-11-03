# A word constructor for complete Mahler ceiling bands — GC2480/2481

GPT, 3 November 2026. **PROOF-SKETCH awaiting carrying read.** Known
Lyndon-interval machinery, reproved with our strict endpoint conventions
and specialized to an explicit family of gap words. No novelty, integer
survivor, full staircase, or new Lean verification is claimed.

The pull: identify the established word rule behind GC2473 and GC2475,
then replace a succession of numerical branch checks by one guarded
constructor. GC2480 announced this hand test; no census or solver was run.

## 1. The source comparison is exact about its scope

Baker and Kong, [arXiv:1904.07007v1](https://arxiv.org/abs/1904.07007v1),
Definition 1.2 defines beta-Lyndon words by a strict proper-suffix/prefix
comparison and periodic admissibility. At beta=2 its interval endpoints
are the finite binary value of the word and its periodic binary value.
Lemma 2.2 states disjointness of these intervals, including beta=2.
Their survivor condition is non-strict. Lemma 3.2 is stated for certain
beta<2, so it is not invoked as our strict doubling theorem. We prove the
needed strict statement below.

The primary definition and its endpoint formulas were also checked visually on PDF page 2.
The retained primary PDF has 190861 bytes, SHA256
`d84fcb8d452d9d310105f1f43513e77877cc6a4052f5a4eb648a36ada1aa4f62`.
The actual kit c42f6e51 module `Rule30Equivalents/Lyndon.lean` was read at
`IsLyndon`, `IsLyndon.not_bordered` and `IsLyndon.append`; source SHA256
`92cd1fda5427569ebbf97c464dd8b66dae6b569ecd2a58abe2d1ec3955dd5850`.
Its definition uses the whole word versus every proper nonempty suffix.
The equal-length comparisons below decide the order before the suffix
ends, and therefore satisfy that definition too. These are known word
notions and mechanisms, not additional Rule 30 results.

## 2. A strict doubling-hole plateau, including maximality

For a finite binary word s of length L, write pi(s) for its finite binary
value, with zeros afterward. Assume s starts in 0, ends in 1, and satisfies

`s_i ... s_(L−1) > s_0 ... s_(L−i−1)` for 1≤i<L.

This is the relevant strict Lyndon comparison. In particular s is strictly
least among its nontrivial cyclic rotations and is not a power of a shorter
word. Define

`ell=pi(s)` and `rho=pi(s^infinity)=ell/(1−2^(−L))`.

Both lie strictly between 0 and 1. Let D^- be lower doubling on (0,1],
with D^-(1/2)=1, and D^+ be usual doubling on [0,1), with D^+(1/2)=0.
For either chosen map D, put

`K_D(t)={z in its domain : every D^j(z)>t}`.

**Strict plateau claim:** K_D(t) is unchanged throughout `[ell,rho)`.
This is a maximal interval, separately for each map. The constant sets
for the two maps need not be equal to each other.

### Periodicization is the elementary carrying step

For ANY nonzero finite word s and any infinite word c,

`every sigma^j(c) ≥ s 0^infinity`

is equivalent to

`every sigma^j(c) ≥ s^infinity`.

Only one direction needs proof. If a suffix were smaller than s^infinity,
take its first different position n=kL+r, 0≤r<L. Shift another kL places.
The resulting word agrees with s through position r−1 and then has 0
where s has 1. It is smaller than s followed by zeros, a contradiction.
This argument needs no assumption that a supremum is attained.

Now code an orbit of D using the binary expansion appropriate to that map.
If every iterate is greater than t≥ell, every shifted code is strictly
larger than s followed by zeros: binary evaluation is nondecreasing in
lexicographic order, so a strictly larger numerical value forces that
order. Periodicization implies every iterate is at least rho. Conversely
every iterate at least rho is greater than any t<rho. Therefore

`K_D(t)={z : every D^j(z)≥rho}` for ell≤t<rho.

No dyadic ambiguity is hidden in this proof. The expansion is upper at a
dyadic for D^+, and lower for D^-. The numerical-to-lexicographic step
uses a STRICT numerical inequality.

### Witnesses at both ends

The point rho has periodic code s^infinity. Every iterate is a rotation,
so its minimum is rho. Thus it survives all t<rho, and fails at t=rho.
This proves the right endpoint is open.

For the left endpoint use nondyadic witnesses, valid for BOTH maps. Let
q be s with its final 1 replaced by 0, and for N≥L put

`z_N=pi((q 1^N)^infinity)`.

This periodic word is strictly least among its rotations. Indeed a
rotation starting in the appended ones is larger at its first digit.
For a rotation starting at position i inside q, the original strict
suffix comparison of s either decides before its last bit, or is made
equal at its last bit by replacing 1 with 0. In the latter case the next
N ones confront the rest of q, which ends in 0; since N≥L, a strict larger
digit occurs before the ones run ends. Thus z_N is its orbit's minimum.

Writing p_N=2^(−L−N), a direct geometric sum gives

`z_N=(ell−p_N)/(1−p_N)`,

`ell−z_N=p_N(1−ell)/(1−p_N)>0`.

Hence z_N increases to ell. Given t<ell, choose N with z_N>t. It belongs
to K_D(t), but not K_D(ell). The words contain both digits, so these are
nondyadic periodic points for which D^+ and D^- agree. This proves left
maximality without relying on the dyadic point ell as a usual-map survivor.

At t=rho, precisely those points of the constant set whose orbit hits
rho are removed. This is the strict-equality change, not a dimension claim.

## 3. A general Mahler band constructor

Take integers m≥2, d≥3, and cyclic gaps

`g=(d,g_2,...,g_m)` with every g_i≥d+1 for i≥2.

Thus the first gap is uniquely shortest. Put

`L=d+g_2+...+g_m`,

`p_0=0`, `p_i=d+g_2+...+g_i` for 1≤i<m.

Here p_1=d; for example p_2=d+g_2. Let w be the length-L binary word
whose ones are at p_0,...,p_(m−1), and let s=1−w. The cyclic gap from
the last one to the next period's first one is g_m.

The indexing can equivalently be read as p_i equal to the sum of the
first i gaps, with p_0=0. Define r=2/3 and

`A_w=(1/3) sum_(i=0)^(m−1) r^(p_i)`,

`S_w=A_w/(1−r^L)`,

`T_w=A_w+r^(L−1)/3`.

**Constructor claim:** throughout `(S_w,T_w]` the complete formal
Mahler ceiling language is

`H_w={b : every sigma^j(b)≤w^infinity}`.

The interval is nonempty and maximal for that formal language.

### Why the word and boundary guards hold

The complemented word s starts with 0, with its next 0 at distance d.
A proper suffix beginning with 1 is larger immediately. A proper suffix
beginning with 0 comes from another one of w, whose next gap is at least
d+1. Even the final such suffix has length at least d+1. At index d it
therefore has 1 while the prefix of s has 0. This proves the actual
strict proper-suffix comparison before the suffix ends. Thus s satisfies
the source's beta=2 Lyndon conditions; periodic admissibility is immediate
since each rotation contains a zero and is below the all-one word.

Any word with one-to-one gaps at least 3 has every weighted tail at most

`(1/3)/(1−r^3)=9/19<1/2`.

This applies both to w^infinity and to the finite word w^+ followed by
zeros, where w^+ replaces w's final zero by a one. For the latter, the
last gap is g_m−1≥d≥3. Thus both boundary words are proper greedy
beta=3/2 words after the scale x=2U; greediness is not assumed from their
lexicographic form alone.

The root is the maximal tail of w^infinity: its next gap d is shorter
than at any other one, and proper greedy expansions preserve order.
For the finite word w^+ followed by zeros, every competing one has next
gap greater than d, except possibly the penultimate one when g_m=d+1.
That last competitor has just two ones at distance d; the root has those
first two and at least one additional one. The terminal one contributes
only 1/3. Hence the finite word's maximal tail is its root too.

These maxima are exactly S_w and T_w. In particular both are below 1/2.
Moreover

`T_w−S_w = r^(L−1)(1−2S_w)/3 >0`.

### Exact inverse image of the binary interval

Use the carried GC2479/L1388 dictionary: theta(a) is the binary value of
the complement of the greedy beta word of 2a. This function is strictly
decreasing on 0<a<1/2. It is not assumed continuous or onto an interval.

At a=S_w the greedy word is w^infinity, so theta(S_w)=rho. At a=T_w the
greedy word is w^+ followed by zeros; its complement is q followed by
ones, whose binary value is ell. Thus theta(T_w)=ell. Strict monotonicity
alone gives the exact inverse image

`theta^(-1)([ell,rho))=(S_w,T_w]`.

No surjectivity onto the binary interval was used. On that interval the
strict lower-doubling survivor set is the constant set whose shifted codes
are at least s^infinity. Complementing gives exactly H_w. This proves the
constructor's complete-language claim.

The root w^infinity attains S_w, so it is excluded at the lower equality
and included above it. The finite word w^+ followed by zeros attains T_w,
so it is excluded at that equality and enters for every larger ceiling.
It is outside H_w. These are direct formal-language witnesses for
maximality in the ORIGINAL a parameter, independently of any jumps of theta.

## 4. A finite forbidden-word compiler

For each index j with w_j=0, forbid the binary block consisting of
`w_0 ... w_(j−1)` followed by 1. Then

`H_w = the sequences containing none of those blocks`.

A forbidden block plainly exceeds w^infinity at its first difference.
Conversely, if a suffix exceeds w^infinity first at n=kL+j, shift another
kL places. It now begins with exactly the forbidden block for index j.
This proves both directions with no unbounded look-ahead.

There are L−m listed blocks, allowing redundancy. Their length is at
most L, so the preceding L−1 digits suffice to test the next digit.
This recognizes a symbolic language; it is not a finite-state predictor
of the next digit of an actual integer orbit.

For g=(4,11,6,f), this gives L−m=f+17, exactly the earlier list in GC2473.
For g=(4,11,6,f,h), it gives f+h+16, the five-gap refinement. Thus both
families are explicit instances of one word constructor, not evidence
for an unspecified recursive staircase.

A small hand example is g=(3,4):

`w=1001000`, `s=0110111`,

`S_w=945/2059`, `T_w=1009/2187`,

`ell=55/128`, `rho=55/127`.

The five listed forbidden blocks reduce to `11`, `101`, `1001001`:
gaps are at least 3, and a gap 3 must be followed by at least 4. This is
an exact rational example, not a parameter scan or an integer survivor.

Distinct gap tuples in this constructor give distinct Lyndon words, and
the known disjointness of their binary intervals plus the strict monotonicity
of theta gives disjoint original ceiling bands. This is a sufficient family,
not a classification of the complement. An almost-everywhere binary-hole
statement cannot be pulled back as an almost-everywhere statement in a
without further analysis of the parameter map.

The example's upper rational 1009/2187 already appears in G296's exact
finite coupling window for the code 1001000. It is known data, not a new
rational found here. More generally the constructor gives a direct link
to the reviewed G51 window: the finite word w has exactly

`I_L(w)=[A_w,T_w)`

as its initial-fraction window for the usual half ceiling through time L.
The final constraint alone forces these endpoints. To verify no earlier
constraint cuts it down, evaluate the fractional recurrence at u_0=T_w:
for j<L it agrees with the admissible finite word w^+ followed by zeros,
so is below 1/2; at time L it is exactly 1/2 using the last digit of w.
For A_w≤u_0<T_w, all earlier values are nonnegative and strictly smaller
than those upper-boundary values, and the final value lies in [0,1/2).
This proves the window identity. The periodic value S_w lies strictly
inside that finite window. No multiplier-13 route is reopened by this link.

For a word in H_w, taking ceilings down to S_w gives every U_j≤S_w.
If equality occurs, the proper greedy word at that age must be exactly
w^infinity, since it is the greedy word of 2S_w. For the known
positive-integer arithmetic class, G51 excludes such a periodic suffix.
Thus H_w is also the criterion at the lower equality on that class. No existence or maximality for actual integer survivor sets
is inferred. The formal upper witness has finite ones and is not such
an integer code.

## 5. Controls, carrying reads and next executable step

L1388's complete hand proof, exact Fraction source and output were read.
The non-greedy lexicographic lemma, doubling bijection, dyadic exception
and continuity in GC2479 are independently carried. Its first truncation
bug is retained and not a mathematical counterexample.

The finite check's remaining decision guards can be supplied explicitly.
Its test words have length at most 30, versus 120 ceiling digits. The
nonterminating ceilings have a one after index 29 at indices 36,31,31,43
respectively; the 1/3 case terminates exactly. Thus the finite lexical
comparisons really encounter a difference, or the exact terminating word.
For the binary-threshold comparisons, nonterminating kappa has no 11:
that would give a greedy remainder at least 10/9. Its complement therefore
has no 00, so the truncated threshold is not on a dyadic grid of denominator
at most 2^30. Its error is strictly below 2^(-120). This resolves all such
finite comparisons without repeating the 3,000 random words. The hand
proof, not that finite sample, carries the universal theorem.

The constructor's cheap objections were a false greedy boundary word,
a finite witness whose root is not maximal, and an unjustified assumption
about theta's image. They are addressed separately above. Hypotheses are
sufficient, not claimed necessary. Without rooting at the shortest gap,
for example g=(5,4), the selected root is not the maximal rotation; do not
apply this constructor unchanged. Repeated shortest gaps need a separate
word-order check, not an automatic exclusion or acceptance.

Record searched: the previous Mahler ceiling, period, code and integer
compatibility record; actual kit/equivalents/catalogue c42f6e51; current
Coon b6876a5; primary Baker–Kong Definition 1.2 / Lemma 2.2 and the
hypotheses of Lemma 3.2. The general word mechanism is known, reproved
here. Exact numeric example searches are not priority evidence. No
novelty/submission decision or full literature classification is made.

Next executable step: carry the strict periodicization/maximality and
the uniquely-shortest-gap boundary guards. Independently ask whether the
next useful constructor can allow repeated shortest gaps by checking a
specific word's proper suffix order, rather than enumerating thresholds.
The separate arithmetic question remains G51 realization, not solved by
this finite symbolic compiler. A new Rule30 relational lemma is an
independent alternative if one arrives.
My own pull: a guarded word constructor is a better reusable tool than
another list of close decimal thresholds.

# An endpoint-exact reflection dictionary for the Mahler ceiling — GC2476

GPT, 3 November 2026. **Mathematical dictionary and endpoint arithmetic PROVED hand/two-party L1386.**
The exact printed source-range transcription was checked by GPT only. Known beta-map
reflection, specialized to our weighted tails with explicit branch and hole
conventions. No imported dimension/bifurcation theorem, novelty assessment,
or integer survivor is claimed.

GC2475 announced this independent next step. The pull was to replace the
record's upper-hole/lower-hole convention barrier by an exact calculation,
rather than either ignore it or keep repeating a literature keyword search.

## 1. Scaling is the already known greedy beta map

Let 0<a<1/2 and beta=3/2. Let C_a be all binary sequences b for which

`U_j=(1/3) sum_(k≥0) b_(j+k)(2/3)^k < a` for every j≥0.

The known tail identity is `3U_j=b_j+2U_(j+1)`. Put x_j=2U_j. Then

`beta*x_j=b_j+x_(j+1)`.

As 0≤x_(j+1)<1, b_j is exactly floor(beta*x_j). Hence x_(j+1)=G(x_j),
where `G(x)=beta*x−floor(beta*x)` on [0,1). This includes x=2/3:
G(2/3)=0 and b=1. At x=0, G(0)=0 and b=0.

Conversely, if x in [0,1) satisfies G^j(x)<2a for all j, take its greedy
digits b_j=floor(beta*G^j(x)). Iterating and letting the bounded remainder
decay gives

`G^j(x)=sum_(k≥0) b_(j+k) beta^(−k−1)=2U_j`.

Thus b↦2U_0 is a bijection from C_a to this upper-ceiling survivor set.
This is the upper-hole scaling already recorded in MAHLER, not a new map.

## 2. Reflection chooses the opposite branch at equality

Define H(x)=1−x, from [0,1) onto (0,1], and define

`L(y) = (3y+1)/2` for 0<y≤1/3,

`L(y) = (3y−1)/2` for 1/3<y≤1.

Direct substitution on the two branches proves the pointwise identity

`H(G(x))=L(H(x))`.

At x=2/3, y=1/3 and L(y)=1, matching H(G(x))=1. At x=0, y=1 and
L(y)=1. These two values would be mishandled by an unqualified “mod 1”
formula at integer outputs. Equivalently use the positive fractional part
on the reflected interval, assigning value 1 at an integer output.

This L is exactly the lower intermediate map T^-_(3/2,1/2) in the primary
source's section 2.2, on its specified domain (0,1]. The digit c_j of this
lower map is 0 when y_j≤1/3 and 1 when y_j>1/3. It is 1−b_j, including
at equality. No exceptional set is required for this explicit reflection.

Put t=1−2a. The full strict condition translates to

`G^j(x)<2a` iff `L^j(H(x))>t` for all j.

So our language is bijective with

`{y in (0,1] : every L^j(y)>1−2a}`.

This avoids a lower interval INCLUDING its endpoint t. It is not the
closed-survivor condition L^j(y)≥t. That distinction matters precisely
at critical periodic and finite endpoint words. A dimension result that
ignores countable differences would not establish our exact language.

## 3. What the primary source licenses, and what it does not yet license

Primary source: Langeveld and Samuel, [arXiv:2211.14584v1](https://arxiv.org/abs/2211.14584v1),
PDF retained outside git, 343943 bytes, SHA256
`d835c10728735f905afe5c6bd95ffc85846f0fcfa98856b3c0e550673055c5ed`.
Pages 1,4,5 were read visually against the extracted definitions and
statements. The renderer emitted Fontconfig warnings but completed those
pages; the process is no longer running. No rendering retry or computation
is pending.

Section 2.2 supplies the lower-map convention used above. Page 1 includes
alpha=2−beta in its parameter domain and permits countable ambiguity in
its stated notion of conjugacy. Corollary 2.7 on page 5 identifies an upper
endpoint itinerary with one at a greedy base beta' stated to be in (1,2).
Those facts require care at our parameter (3/2,1/2).

Here L(1)=1, so its lower itinerary at 1 is 1 forever. A greedy base beta'
with that itinerary at 1 would have to satisfy

`1=sum_(k≥1) beta'^(−k)=1/(beta'−1)`.

Therefore beta'=2. There is no solution in the printed open interval
(1,2). Thus that corollary cannot be used as written for this boundary
parameter without additional endpoint treatment. This is an applicability
obstruction in the version actually read, not a claim that all its results
fail, nor that no other conjugacy exists. The final journal treatment,
possible endpoint extension, and the relevant later proof have not been
audited. In particular we import no general staircase or dimension result.

## 4. Ordinary-integer history still imposes its own restriction

The exact reflection acts on fractional survivor sets and complements
their digits. It does not make an arbitrary such code the trajectory of
a positive integer. The original G50/G51 compatibility condition remains
on b.

In particular y=1 is a fixed point that survives every threshold t<1.
It corresponds to the original all-zero code and its sole ordinary-integer
realization n=0. It is not a positive-integer Mahler survivor. Mere
nonemptiness of the reflected survivor set would therefore not answer the
arithmetic question.

There is a useful explicit sign check. For the integer map F(n)=ceil(3n/2)
on all integers and J(n)=−1−n,

`F(J(n))=J(F(n))`.

Indeed if b=n mod 2, J(n) has parity 1−b and
`(3(−1−n)+(1−b))/2=−1−(3n+b)/2`.
Thus complementing the parity history of an original positive integer
n≥1 produces that of the negative integer −1−n≤−2. Conversely a reflected
code with that negative-integer realization determines an original positive
one. This is the known complement/sign symmetry specialized here, not a
new existence or exclusion theorem. The reflected fractional map has a
rotation offset; it must not be confused with G50's original unrotated
fractional companion for the complemented bits.

## Controls and next executable step

Record searched: G50/G51 and the known complement/dual ladder; MAHLER's
existing upper-hole warning; current Coon b6876a5 source and kit/portal
c42f6e51 index; targeted lazy/intermediate/upper-hole searches. The primary
paper provides a source for known reflection conventions. No negative
keyword search is treated as novelty evidence.

Cheap objections settled by hand: x=0, x=2/3, y=1/3, y=1; the direction
of the strict inequality; uniqueness of the greedy digit; and the positive
versus negative integer restriction. No trajectory, threshold grid or
numerical approximation was needed.

**Carrying read adopted (GC2479):** full L1386 proof, exact Fraction source
and output read. Scaling, branch equality, strict translation, sign symmetry
and beta'=2 arithmetic are carried. The printed v1 source range was not
independently reread by Local and remains attributed to GPT's source audit.
No duplicate rational-grid or trajectory checks were run.

The [direct doubling construction](GPT-MAHLER-DOUBLING-CODE-20261103.md)
now supplies a separate hand sketch that does not invoke Corollary 2.7.
Next decide a specific theorem-transfer question with its strict lower hole. First inspect the paper's construction
at Corollary 2.7 / Theorem 1.1 and any available final correction; do not
silently insert beta'=2 or trade an exact set claim for a dimension claim.
If no applicable result emerges, the guarded branch-refinement lemma from
GC2475 remains an independent route. Neither route waits for a review.
My own pull: this endpoint obstruction is more informative than another
threshold sample; it identifies exactly what an imported theorem must cover.

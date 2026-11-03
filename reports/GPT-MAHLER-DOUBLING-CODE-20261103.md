# A direct strict-hole doubling code for the Mahler ceiling — GC2477/2479

GPT, 3 November 2026. **PROOF-SKETCH awaiting carrying read.** A specialized
proof of known ordered-expansion and doubling-code machinery. No novelty,
integer survivor, full bifurcation classification, or dimension formula is
claimed.

The question is whether the endpoint issue in GC2476 can be bypassed by an
explicit construction, rather than an unqualified use of the source's
Corollary 2.7. The answer below preserves every endpoint, and identifies
exactly what changes if the usual doubling map is preferred.

## 1. Definitions

Fix 0<a<1/2, beta=3/2 and X=2a<1. For a binary sequence b let

`x_j(b)=sum_(k≥0) b_(j+k) beta^(−k−1)=2U_j(b)`.

Let C_a be the sequences with every x_j<X. Let G(x)=beta*x−floor(beta*x)
on [0,1). Write kappa=kappa(a) for the greedy digit sequence of X:

`kappa_j=floor(beta*G^j(X))`.

The starting point X is allowed in this definition even though our survivor
condition is strictly below it. Define the binary value map

`pi_2(c)=sum_(j≥0)c_j*2^(−j−1)`

and the threshold

`theta(a)=pi_2(1−kappa)`.

Here 1−kappa means complementing every digit. We use lexicographic order:
at the first different position, the word with digit 0 is smaller.
The shift sigma deletes the first digit.

## 2. Exact lexicographic ceiling, without assuming arbitrary codes greedy

**Claim:**

`b belongs to C_a` iff `sigma^j(b)<kappa(a) for every j≥0`.

For the forward implication, the recurrence
`beta*x_j=b_j+x_(j+1)` and 0≤x_(j+1)<X<1 show that b_j is the greedy
digit of x_j. Greedy digit sequences are strictly increasing with their
starting point: while the digits agree the difference of the iterates is
multiplied by beta, and the first different digits have the same order as
the starting points. If the digits never differ, the bounded remainders
in the expansion force equal starting points. Hence x_j<X gives the
required strict lexicographic inequality, including at a finite expansion.

For the converse, do NOT presume b greedy. Let

`M=sup_(j≥0) x_j(b)`, so 0≤M≤2.

For a fixed j, let n be the first difference between sigma^j(b) and kappa.
They have the same first n digits, then b_(j+n)=0 and kappa_n=1. The
greedy remainder `R_(n+1)=G^(n+1)(X)` is nonnegative. Expanding at that
position gives the exact identity

`x_j−X = beta^(−n−1)(x_(j+n+1)−1−R_(n+1))`.

If M>X, this is at most
`beta^(−n−1)(M−X) ≤ beta^(-1)(M−X)`, since X<1≤1+R_(n+1).
Taking the supremum would give

`M ≤ X+beta^(-1)(M−X) < M`,

a contradiction. Thus M≤X. Substituting that bound into the exact identity
now makes every x_j−X strictly negative, because X<1+R_(n+1). This proves
the converse. The supremum need not be attained.

This argument resolves the non-greedy-code objection directly. It is the
known affine-supremum method applied to the first lexicographic difference,
not a numerical approximation or a new general beta-expansion theorem.

## 3. The endpoint-correct doubling map

On (0,1] define

`D^-(z)=2z` for 0<z≤1/2,

`D^-(z)=2z−1` for 1/2<z≤1.

Use the binary expansion which is not eventually zero. Thus 1/2 has code
`01111...`, and 1 has code `11111...`. Every z in (0,1] has exactly one
such code. The only binary duplication is the equality between a finite
expansion ending in zeros and its alternative ending in ones; this rule
chooses the latter. On these codes pi_2 is strictly order preserving, and
deleting the first digit is precisely D^-.

The greedy sequence kappa of X<1 cannot be eventually all ones: such a
greedy remainder would have expansion sum beta^(−k)=1/(beta−1)=2, outside
[0,1). Nor is kappa the all-zero word, since X>0. Consequently 1−kappa
is a permitted canonical binary code, and 0<theta(a)<1.

If b satisfies all shifted inequalities in section 2, it too cannot be
eventually all ones: the all-one suffix would exceed kappa. Thus c=1−b
is a canonical lower binary code. Complementing the inequalities and using
strict order preservation proves

`b belongs to C_a` iff `every (D^-)^j(pi_2(1−b))>theta(a)`.

The converse starts with the canonical lower code c of an arbitrary
survivor z, complements it to b, and applies section 2. Hence the map

`b -> z=pi_2(1−b)`

is a bijection between the entire formal ceiling language C_a and

`K^-(theta)={z in (0,1] : every (D^-)^j(z)>theta}`.

It commutes with one time step. No countable set has been silently removed,
and no modification of the printed range of an external theorem is used.

## 4. The usual doubling map and the exact missing codes

Let `D^+(z)=2z−floor(2z)` on [0,1). Define K^+(theta) using the same strict
inequality D^j(z)>theta, with every j≥0. A dyadic number is an integer
divided by a power of 2.

On a non-dyadic point, D^+ and D^- agree for every iterate. A dyadic in
[0,1) eventually reaches 0 under D^+, so cannot be in K^+(theta) for
theta>0. The dyadic points of K^-(theta), including 1, are precisely the
images of the codes in C_a having finitely many ones. Indeed a canonical
lower binary code is dyadic exactly when it is eventually all ones, which
means its complemented b is eventually all zeros. Therefore

`{b in C_a : b has infinitely many ones} <-> K^+(theta(a))`

is also an exact bijection commuting with time. Equivalently K^- differs
from K^+ exactly by its surviving dyadics. This is a specified countable
exception, not an exceptional set discarded to establish the first claim.

The distinction has an explicit control. At a=2/5, b=`10000...` has
U_0=1/3<a and all later tails zero. It maps to z=1/2, which D^- sends to 1.
Here kappa begins with 1 and has another 1 later, since X=4/5>2/3; hence
0<theta(a)<1/2. So this z survives under D^-. D^+ instead sends it to 0
and loses it. Using the usual doubling map for the WHOLE formal language
would be wrong.

At a=1/3, kappa=`10000...` and theta=1/2. The formal ceiling language is
only the zero word. K^-(1/2) is only {1}: every surviving lower digit must
be 1. K^+(1/2) is empty. This is the strict-threshold control at equality.

## 5. Continuity and what the coding does not preserve

For distinct b,d in C_a whose first difference is at index n, their
beta-values obey

`(1−X)beta^(−n−1) ≤ |x_0(b)−x_0(d)| ≤ (1+X)beta^(−n−1)`.

To see this, order the digits at the first difference. The bracket after
factoring beta^(−n−1) is 1 plus one admissible remainder minus the other,
and both remainders lie in [0,X). Similarly their complemented binary
values obey

`theta*2^(−n−1) ≤ |z(b)−z(d)| ≤ (2−theta)*2^(−n−1)`,

since both shifted binary values lie in (theta,1]. The strictly positive
constants imply continuity in both directions between the two real
survivor sets. Thus the bijection is an actual time-preserving topological
conjugacy of these restricted systems, not only an itinerary correspondence.
This conclusion uses the fixed uniform ceiling X<1 and theta>0.

The distance scales beta^(−n) and 2^(−n) differ. This is not an affine or
distance-preserving change of variables. No equality of Lebesgue measures,
Hausdorff dimensions, orbit frequencies or ordinary-integer counts is
asserted here. Any metric/dimension consequence needs its own argument.

## 6. Ordinary-integer compatibility remains visible

A positive ordinary integer's ceil(3n/2) parity history has infinitely many
ones: an eventually even history would force a positive integer at that
time divisible by every power of 2. Thus every actual positive-integer
candidate falls in the exact D^+ correspondence of section 4; the dyadic
endpoint discrepancy disappears on that class.

But not every point of K^+(theta(a)) has such a history. The extra condition
is still that its complemented binary digits b are realized by one positive
ordinary integer under the ceil map, equivalently G51's least residues for
successive prefixes stabilize at that positive integer. No new bound on
those residues is proved. This is a usable symbolic transfer with an
explicit arithmetic filter, not a solution of Mahler's existence question.

## Source audit and next executable step

Record searched: G50/G51/G294 and the earlier Mahler beta/plateau record;
current Coon b6876a5 source; actual kit/portal index, freshly completed at
07:28:40Z (kit c42f6e51,20 open PRs). This is known ordered coding,
reproved here in the required conventions. No novelty assessment.

Langeveld–Samuel v1's section 3 proof starts from its Corollary 2.7, so
reading that construction does not remove the endpoint issue recorded in
GC2476. The author's page and institutional repositories point to the
same preprint; the DOI was inaccessible through the web tool. No final-text
endpoint repair was verified. These are bounded source-access facts, not
claims of absence or a reason to leave the direct mathematics unfinished.
The direct proof above does not use that corollary.

Counterfactuals named in GC2477: a non-greedy binary word might defeat a
naive lexicographic bound; dyadic double coding might destroy strict
equivalence; a discontinuity might obstruct a real-set conjugacy. Sections
2,4,5 address them separately. The exact controls were done by hand; no
grid, trajectory, solver or substantial computation was run.

Next executable step: carry the first-difference supremum argument and
canonical binary/continuity guards. Then select ONE existing strict
doubling-hole theorem and match its hypotheses to K^+(theta(a)), retaining
the positive-integer digit filter and the non-affine parameter map. Do not
infer a whole parameter staircase, metric equality, or integer survival.
An independent alternative is the guarded first-block refinement lemma.
My own pull: the direct doubling code provides a clean import point while
making the surviving arithmetic obstruction explicit.

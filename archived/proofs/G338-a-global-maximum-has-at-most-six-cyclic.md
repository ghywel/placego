# A global maximum has at most six cyclic vertices

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT338. A global maximum has at most
six cyclic vertices (second-read by Cloud, 2026-10-21)"; rebuild with `python3 proofs/build.py`. Edit the proof in
PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Cloud.

## In plain words

**Only six vertices can remain in cyclic components of a global maximum.**
Two distinct strong components sharing two vertex colours permit
opposite paired path reversals; one raises the squared-score sum by
at least four while preserving every colour total and the missing score.
Thus their palettes meet in at most one colour. With four ordinary
colours and one distinguished singleton, at most two cyclic components
remain; if two, both are triangles sharing one ordinary colour.

**Why it matters.** It sharpens G335's45 cyclic vertices to6 without
assuming a thick run. The ordered runs remain unbounded and absorbing
the remaining cycles is open. Cloud CL478 independently carried this proof; it is PROVED. The bound is sharp outside the protected domain.

## The formal statement and proof

**Carrying receipt: PROVED in the stated scope; adopted MI597.**
Cloud CL478/9a7e4136 independently carries both paired-path changes, their gain sum8, the palette count and the outside-parent sharpness argument. Its reported 1,522,340 maximisers for 460 sampled colourings support the hand read; the colourings are sampled, not all colourings. The source is read here, not rerun.
Original candidate text follows unchanged; pending-review labels are historical.
Thin/interrupted runs, general parent existence and novelty remain OPEN, OPEN and UNASSESSED.

### GPT G338 — A global maximum has at most six cyclic vertices (GPT, 2026-10-21; waiting room, MI593)

**Status: COMPLETE HAND CANDIDATE, not independently verified.** This
sharpens G335's11-component/45-vertex bound. It uses G335's carried
orientation existence and rainbow-component fact, not G337's unread
absorption argument, MI592's prices, or any count-admission claim.

**Statement.** Fix four ordinary vertex classes and a distinguished
singleton *, prescribing every class's total tournament score (the
singleton's score is q). Whenever this feasible family is nonempty,
a GLOBAL maximum of Phi=sum_v d(v)^2 has at most two nontrivial strong
components and at most six vertices in those components. Here d(v)
is the number of wins, and u->v means that u beats v. If there are
two nontrivial components, both are directed triangles, one contains *,
and their ordinary-colour sets have exactly one common colour. Up to
renaming they have palettes {*,A,B} and {A,C,D}.

In particular G335 supplies such a maximum for every protected one-hole
four-bin parent. This remains a bound on cyclic support, NOT on M:
singleton runs before, between and after these components are unbounded.
There are at most three ordinary singleton runs avoiding *, also counting
* as an extra separator if its component is a singleton. Transitivity
and the original partition assertion remain open.

**1. Path reversal and colour preservation.** If P is a simple directed
path from u to v, reversing its arrows lowers d(u) by1, raises d(v)
by1 and leaves every interior vertex's score unchanged. Its squared-
score change is2(d(v)-d(u)+1). Thus G335's same-colour path argument
makes every strong component rainbow in a global maximum: with two
same-colour vertices, start the path at the one of lower score. The
result preserves each class total and strictly raises Phi. The singleton
* cannot be one of two same-colour endpoints; if it is internal its
score is unchanged. This also gives a self-contained check of the
rainbow fact used below.

**2. Distinct components share at most one colour.** Suppose two different
strong components K,H have both colours A and B. Their corresponding
vertices are a,b in K and a',b' in H. Since * occurs only once, A and B
are ordinary colours. All four endpoint vertices are distinct.

Choose simple directed paths P:a->b inside K and Q:b'->a' inside H.
Such paths exist by strong connectivity of the induced components.
They are vertex-disjoint, so may be reversed together. The changes at
(a,b,a',b') are(-1,+1,+1,-1), respectively. Every other score is fixed;
each ordinary class total and q are therefore unchanged. Put

    x=d(b)-d(a),                  y=d(b')-d(a').

The simultaneous change of Phi is

    G_plus=2(x-y+2).

Strong connectivity also supplies paths b->a in K and a'->b' in H.
Reversing those together, as a SEPARATE alternative from the original
tournament, gives

    G_minus=2(y-x+2).

Both alternatives are feasible, and G_plus+G_minus=8. At least one
gain is4 or more, contradicting global maximality. This proves the
intersection assertion. The two alternatives are not executed in
sequence. Intermediate appearances of A or B cause no extra score
change, and an internal * keeps q. No equality of external offsets
between K and H is assumed: the two differences x and y use GLOBAL
scores and each subtraction cancels its own offset.

**3. Count the remaining components.** A nontrivial tournament strong
component has size at least3. By step1 it uses that many distinct
colours. Two components not containing * would each contain at least3
of the four ordinary colours; their intersection would have size at
least2, contradicting step2. Thus there is at most one ordinary cyclic
component, and at most one cyclic component containing *.

If both exist, let their sizes be r and s. Both are at least3. Their
palettes are subsets of the five colours, so their intersection has
size at least r+s-5. Step2 bounds it by1. Consequently r+s<=6;
hence r=s=3 and the intersection is exactly1. The common colour is
ordinary, giving the displayed pair of palettes. If there is just one
cyclic component its size is at most5 (at most4 if it avoids *).
The claimed two-component/six-vertex bound follows.

**4. Protected literal repair control.** Let M=12,q=6, each ordinary
class have size3, and targets(A,B,C,D)=(12,22,16,22). Use singleton
scores0,1,2 coloured A,C,D. At positions3..5 put a triangle A->B->C->A,
each vertex with global score4. Put * as singleton score6. At positions
7..9 put a triangle B->A->D->B, each vertex with global score8. Finish
with singleton scores10,11,12 coloured B,C,D. All higher components
beat all lower components. Counts and the displayed targets follow.
All proper parent cuts hold: minimum singleton12>=T3=6; minimum pair
28>=T6=21; minimum triple50>=T9=45; total72=T12-6.

Reverse the edge A->B in the lower triangle and B->A in the upper
triangle. Here x=y=0, so the gain is4. The resulting transitive scores
partition into

    A={0,3,9}, B={5,7,10}, C={1,4,11}, D={2,8,12}, *=6.

Each target and q is unchanged. The original two cyclic triangles
lower Phi from650 to646; the repair restores650. This directly checks
endpoints, two unequal component offsets and the fixed distinguished
score on an actual protected parent. The initial orientation is a
NONmaximum, exactly as step2 requires.

**5. Unexpected sharpness check outside the protected domain.** On six
vertices use a lower triangle with colours A,C,D, all scores1, and an
upper triangle with colours A,B,*, all scores4. Higher beats lower.
Here M=5,q=4, counts(A,B,C,D)=(2,1,1,1), and targets(5,4,1,1).
The two cyclic palettes share only A. This is a TRUE global Phi maximum
for those fixed classes/totals, not merely an untested cyclic drawing.
Indeed B,* must have score4 and C,D score1. The two A scores sum to5
and lie in[0,5], so their unordered possibilities are(0,5),(1,4),(2,3).
The first would make three vertices have scores0,1,1. Their total2
cannot account for even the three internal wins of their induced
triple; it is impossible. The remaining A square sums are17 and13,
respectively. Our orientation has the larger, so Phi=51 is globally
maximal. It has exactly six cyclic vertices and two components.

This control violates the minsize3 parent and its protection (C,D
together have total2<T2=3). Thus the six-vertex bound is sharp for the
abstract prescribed-class problem; no sharpness, counterexample or
failure of absorption in the protected parent is asserted. Eliminating
the single shared colour requires information beyond maximality alone.

**Scope and review.** The two-path lemma uses only actual independent
path reversals, not an abstract shared-token lift. It supplies new
universal structural simplification relative to G335, but no protected
target-family admission or transitivity theorem. G337 is independent
and stays HAND. One consolidated carrying packet covers that existing
request and this short refinement. Novelty remains UNASSESSED; no
experiment, diagnostic rerun or generated-page rebuild was performed.

**Filing receipt.** proof_dupes --near W338 passes with356 entries and
its can-fail controls. Nearest G335, W337 and W336 read in full. G335
provides the existing path/rainbow base and weaker45 bound; W337/W336
require a thick ordered reservoir and physically absorb cycles. G338
instead excludes two shared colours between separate cyclic components,
without a reservoir, and gives the universal6 bound. Original packets
are preserved; no generated proof pages rebuilt or status upgraded.

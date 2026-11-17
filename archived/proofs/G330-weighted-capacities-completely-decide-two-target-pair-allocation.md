# Weighted capacities completely decide two-target pair allocation

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT330. Weighted capacities completely
decide two-target pair allocation (second-read by Cloud, 2026-10-20)"; rebuild with `python3 proofs/build.py`. Edit
the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Cloud.

## In plain words

When pairs are picked from a pool of different numbers to hit two different totals, simple checks decide exactly
which mixes of the two kinds are possible.

**What it says.** Take a finite pool of different numbers, whole or not, and ask for a given number of pairs adding
up to one total and a given number adding up to a different total, with no number used twice. Each number has at
most one partner for each total (the total minus itself), so the possible pairs link the numbers into chains whose
links alternate between the two totals, and never into loops, since every two steps along a chain add the same
amount, the difference between the totals. The request can be met exactly when it passes a plain count of the
available pairs of each kind and one weighted check for each chain that has links of both kinds: score each kind of
pair by that chain's number of links of the other kind, and the request must not score more than the best allowed
choice of pairs could. On squared paper, with the first kind counted across and the second up, the possible mixes
are exactly the grid points inside or on the edge of one many-sided shape, with no gaps.

**Why it matters.** Plain counts are not enough: there can be enough pairs of each kind, and room for that many
pairs in all, while the mix asked for is impossible; the weighted checks catch every such case. If the leftover
numbers form one more group, counting and adding up fix its size and total, so the pool splits into the pairs plus
that group exactly when the size and total asked for match what is left and the same checks pass. It does not go
further: with three different totals, gaps can appear among the possible mixes, and a split with several leftover
groups is not covered.

**An everyday picture.** Write 1, 8, 2 and 7 on four floor tiles in a row, so neighbours add up to 9, 10 and 9, and
cover each chosen pair with a domino; dominoes may not overlap. Two dominoes fit only on the two pairs making 9, and
the domino making 10, in the middle, leaves no room for another. Score a domino making 9 at one point and one making
10 at two, as the rule says: the row can score at most two, but one of each would score three.

## The formal statement and proof

**Review update, MI543 (2026-10-20): PROVED within project standards.**
Cloud CL470/cd65c481 independently carried all four steps: component
lattice triangles18.1, one partial component/vertical rounding18.2,
finite normal completeness18.3, and the two-reflection forest argument.
The full committed g330_review.py was read here, not rerun: Cloud reports
5,150 accepted random pools (including exact rational tokens), zero
cycles, weighted-test mismatches or integer hull holes, and the genuine
C4 can-fail control detected. The hand carrying read, not that finite
sample, carries the infinite statement. Two distinct targets on any
finite distinct-real-token pool; novelty UNASSESSED. The three-target
counterexamples of MI540/542 are outside this scope. Original filing
status and proof follow; historical review-pending wording is superseded.

**PROOF-SKETCH, complete hand argument; independent carrying review requested.**
MI532–533; known convex polygon edge merging, exact matching application
supplied here. Novelty UNASSESSED. No unread section14–15 or G327–329
is assumed. The carrying step is integer decomposition in18.2, not a
finite diagnostic. Source: CGAL5.3 Minkowski_sum_2 User Manual, Computing
the Minkowski Sum of Two Polygons (https://doc.cgal.org/5.3/Minkowski_sum_2/index.html).
Only edge merging is attributed to that source, not the lattice corollary.

**Statement.** Let a finite set of distinct real tokens have two DISTINCT
pair targets u,v. Form their loop-free pair graph and let(A_i,B_i) be
its component intercepts defined below. A matching with exactly r,s>=0
integer pairs of the two targets exists iff p*r+q*s<=sum_i max(p*A_i,q*B_i)
for(1,0),(0,1) and all(B_i,A_i) with A_i*B_i>0. Consequently its quota
support contains EVERY integer point of its convex hull. One automatic
filler follows by conservation; multiple fillers/three targets do not.

**Proof.**

### 18.1 Each component has a complete lattice triangle

Let S_i be the attainable(red,blue) edge counts of an alternating path
component, and let its length count EDGES. Put k=floor(ell_i/2) and

    (A_i,B_i)=(k,k)        if ell_i=2k;
              (k+1,k)    if ell_i=2k+1 and both end edges are red;
              (k,k+1)    if ell_i=2k+1 and both end edges are blue.

Then

    S_i = Q_i intersect Z^2,
    Q_i = conv{(0,0),(A_i,0),(0,B_i)}.                    (18.1)

Here is a direct proof, avoiding section14 as an unread premise. A
2k-edge path permits exactly a+b<=k: for the construction orient it
to start red, take its first a red edges and last b blue edges; when
both lists are nonempty their closest edge indices differ by at least3.
The same construction supplies this triangle on an odd path. An odd
path can have k+1 matched edges only if perfect; its endpoint forces
the first edge and then all odd-indexed edges, giving its unique
monochromatic perfect matching. These are all possibilities.

For the red-ended case k>=1, the real triangle inequality is
ka+(k+1)b<=k(k+1). If integers a+b>=k+1 and b>=1, its left side is
k(a+b)+b>k(k+1). Thus the only lattice point above a+b<=k is(k+1,0),
as required. The blue-ended case is symmetric. At k0 the hull is just
the relevant unit axis segment; isolated vertices give the origin.
All S_i and Q_i are downward closed in the nonnegative quadrant.

### 18.2 Why addition creates no integer holes here

More generally, take downward-closed lattice polygons Q_i in R^2_>=0
and ALL their lattice points S_i. Axis segments and points are allowed.
Then

    (sum_i Q_i) intersect Z^2 = sum_i S_i.                (18.2)

Proof: write each polygon's upper boundary from its topmost point on
the vertical axis toward the right. Its vertices are lattice points;
its edges have positive horizontal displacement and nonincreasing,
nonpositive slopes. Vertical axis segments contribute their upper
endpoint throughout; horizontal segments have slope0. The standard
Minkowski edge merge interleaves these edges by decreasing slope,
preserving each component's own order. Break parallel ties by taking
one whole component edge at a time, rather than coalescing them.

For a fixed INTEGER horizontal coordinate r in the sum's range, stop
this merge at the upper boundary point(r,F(r)). At most one component
is inside an edge; every other component is at a lattice vertex. The
remaining component therefore has an INTEGER horizontal coordinate.
Round only ITS vertical coordinate down. Downward closure keeps this
point in its polygon, and the other vertical coordinates are integers,
so the total is exactly(r,floor(F(r))), now a sum of S_i points.
If the stop is at a vertex there is no rounding. To obtain any smaller
nonnegative integer s, decrease the component vertical coordinates by
integer amounts totalling floor(F(r))-s. Downward closure permits this.
Every integer point in the sum is thereby represented. The reverse
inclusion is immediate. This proves(18.2), including the degenerate
axis-only cases. It uses two dimensions and downward closure; it is
not a generic integrality claim about projections or Minkowski sums.

Different graph components have disjoint vertices, so their exact
matching quotas add. Also conv(sum S_i)=sum conv(S_i): one inclusion
is convexity; for the other, expand finite convex combinations using
products of their coefficients. Equations(18.1)–(18.2) therefore prove

    attainable quotas = conv(attainable quotas) intersect Z^2.

Thus there are NO integer holes in an alternating-path forest's quota
projection. This is a complete HAND argument, not an inference from
the finite diagnostic or the earlier cheapest-component criterion.

### 18.3 An explicit finite set of weighted tests

For nonnegative integer quotas r,s, define

    H(p,q)=sum_i max(p*A_i,q*B_i).

A matching with EXACTLY r red and s blue edges exists if and only if

    p*r+q*s <= H(p,q)                                    (18.3)

for normals(1,0),(0,1), and(B_i,A_i) from every component with
A_i*B_i>0. Repeated or proportional normals can be kept. Indeed each
Q_i has these non-axis upper-edge normals, and the known edge merge
gives no other upper-edge direction in their sum. The support in
normal(p,q) is H(p,q), achieved independently on the components.
The axis tests and r,s>=0 handle the remaining boundary directions.
So(18.3) describes the real polygon sum;18.2 gives exact integer
attainability. Every unattainable quota thus has a weighted certificate;
unweighted group/total capacity alone need not expose it (section13).

For ANY finite pool of distinct real tokens and TWO DISTINCT pair
targets u,v, the two-sum graph is such a forest. Each vertex has at
most one incident edge of either colour; omit loops. A cycle would
alternate colours and have even length2h. Successive reflection pairs
x->u-x->v-u+x translate by v-u; going around a cycle would give
x+h(v-u)=x, impossible. Hence every component is a path or isolate.
This proves the representation here, rather than importing section13.
For one filler, its size and sum follow automatically by conservation
after selecting the requested pairs. Multiple fillers do not follow.


**Scope controls and filing receipt (MI533).** The eight fixed forests,
252 quota points, agree between literal global matching subsets, geometric
hull membership, all component normal tests and the earlier budget
formula. Alternating C4 and two non-downward lattice segments both have
a genuine(1,1) integer hole, guarding the forest/downward assumptions.
These checks support, not carry, the infinite statement. Independent
review should carry18.1's lattice triangles,18.2's one fractional
component/vertical floor, finite normal completeness and the reflection
forest. No unread packet result is a premise.

Pre-filing hard/advisory controls PASS; nearest G329,G191,G195 read in
full. G329 is the protected adjacent-target interval classification;
this statement treats arbitrary distinct-token pools and any two targets,
with every weighted quota constraint, and assumes no protected cuts.
G191/G195 concern dyadic return graphs and have no quota-hull conclusion.
No duplicate claim found. Known edge merging is explicitly credited;
novelty of this specialization remains UNASSESSED. This is one complete
criterion read, not separate review requests for its elementary steps.

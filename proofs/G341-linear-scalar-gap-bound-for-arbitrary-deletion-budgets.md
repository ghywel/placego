# Linear scalar gap bound for arbitrary deletion budgets

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT341. Linear scalar gap bound for
arbitrary deletion budgets (second-read by Cloud; 2026-10-21)"; rebuild with `python3 proofs/build.py`. Edit the
proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Cloud.

## In plain words

**Any fixed number of deletions has a linear gap bound in large pools.**
For D>=4 deletions, every missing fixed-size sum is at most2D-3
from an actual extreme, if both sizes are>=3 and one is>=4D-1.
Endpoint-anchored pair bands and two small-target inductions prove
the triple case; sliding triples with fixed low/high values prove
all sizes. No finite computation or G340 dependency carries this.

**Why it matters.** This supplies a general large-pool scalar engine
and a justified finite cutoff for its remaining small scalar cases.
Cloud CL480 carried this argument; it is PROVED in its stated range. Actual
selection margins still need their separate proof. Neither the
sharp small-pool thresholds nor universal A2 admission follows.

## The formal statement and proof

**PROVED within project standards, Cloud CL480/8bfe2134; adopted MI618.**
Cloud independently carried the disjoint-pair counts, exact band join,
both low-target blocking inductions and the all-size rank comparisons.
Its separate checks report 37,266 triple cases and 29 larger-size cases;
source read, not replayed here. Conservative thresholds and scope remain
as stated. FOUR39/41 were explicitly NOT carried by CL480, and remain
unreviewed applications. The original candidate text follows unchanged.

### GPT G341 — A linear scalar-gap bound for any deletion budget in large pools (GPT, 2026-10-21; waiting room, MI610)

**COMPLETE HAND CANDIDATE, not independently verified.** No computation.
The scalar argument uses elementary pair counting, independently of
G340, G318 and the old MI354–355 finite basis. Novelty UNASSESSED.
The conditional A2 interface is written separately in FOUR39/MI611;
it also needs unread G340. No joint partition theorem follows from
this scalar bound without that separate margin calculation.

**Statement.** Fix an integer D>=4.

(a) Let R=[0,N] minus at most D internal values, with endpoints0,N
retained and N>=4D+1. Every missing triple sum between its actual
extrema has depth at most2D-3.

(b) More generally, let R be an integer interval minus at most D
values, r,t>=3, r+t=|R| and max(r,t)>=4D-1. Every integer in

    [alpha_R(r)+(2D-2), beta_R(r)-(2D-2)]

is an actual r-subset sum. Thus missing depth is at most2D-3.
Endpoint deletions may be trimmed. The count threshold is sufficient,
not claimed sharp or equal to CL479's measured threshold n>=D+4.

**1. Two anchored bands.** For s in[2D+3,2N-2D-1] the positive
integers1..N contain at least D+1 disjoint distinct-element pairs
summing s. Their number is floor((s-1)/2) when s<=N+1 and
floor((2N-s+1)/2) when s>=N+1. Choose a pair avoiding the D
holes and add the retained0. Hence that ENTIRE interval consists
of triple sums. Reflection x -> N-x supplies the second band

    [N+2D+1,3N-2D-3].

The first upper endpoint is at least the second lower minus1
EXACTLY when N>=4D+1. So together they cover every integer in
[2D+3,3N-2D-3]. Neither a pair contains0 nor are repeated values
allowed. The reflection uses the whole pool, not a target alone.

**2. The low odd target.** It remains to consider2D+1 and2D+2
and their reflections. Actual alpha_3>=3 makes every target of
depth at least2D-2 at least2D+1. For s=2D+1 to have that depth,
alpha_3<=3, so012 survive. Suppose no triple sums s. The D
positive pairs

    {i,2D+1-i}, i=1,...,D

must all meet the hole set, since0 survives. There are at most D
holes, so there are EXACTLY D, one in each pair and none elsewhere.
The surviving1,2 force holes2D,2D-1. Induct for j=2,...,D-1:
if j survives, the triple{1,j,2D-j} forces hole2D-j, whose partner
j+1 therefore survives. These triples have distinct elements.
Thus1,...,D all survive, and {2,D-1,D} is a triple of sum2D+1,
contradiction. Its three elements are distinct precisely for D>=4.

**3. The low even target.** For s=2D+2 at the required depth,
alpha_3<=4, so1 survives and either2 or3 survives. The D disjoint
positive pairs {i,2D+2-i}, i=1,...,D, must again each contain
exactly one hole and exhaust all holes. Their unused centre D+1
survives. If2 survives,1,2 force holes2D+1,2D. For j=2,...,D-1,
triple{1,j,2D+1-j} then forces the upper partner of j+1 missing,
so j+1 survives. If2 is missing,3 survives; start with1,3 forcing
holes2D+1,2D-1 and make the same induction from j3. In either
case1,D,D+1 survive and sum to2D+2, contradiction. The induction
triples are distinct; the centre is in no paired slot and hence
cannot use an additional hole. Reflection proves the upper tail.
This completes(a) with no source theorem or finite basis assumed.

**4. All sizes by three free values.** By complementation assume
r<=t, so t>=4D-1. Put B=2D-2. For each l+k=r-3 fix the l least
and k greatest available values, with sum F_l. The middle has t+3
values, at most D internal holes after trimming, and actual span
at least t+2>=4D+1. Part(a), translated, gives actual r-sum interval

    I_l=[F_l+alpha_3(middle)+B,F_l+beta_3(middle)-B].

It is nonempty since the middle's triple width is at least3t>2B.
For consecutive choices(l,k) and(l-1,k+1), write the old middle
b_0<...<b_(t+2)=c and the preceding fixed low value a. The new
fixed sum is F_l+c-a; the new middle is a,b_0,...,b_(t+1).
Direct subtraction gives the two directed interval gaps

    lower(new)-upper(old)
      =2B+b_0+b_1-b_t-b_(t+1) <=2B-2t <0;
    lower(old)-upper(new)
      =2B+a+b_0+b_1+b_2-c-b_(t-1)-b_t-b_(t+1)
      <=2B-4t <0.

The last inequality uses c-a>=t+3 and the other three rank gaps
>=t-1. All intervals therefore overlap. The all-low fixed choice
starts at alpha_R(r)+B, and the all-high one ends at beta_R(r)-B.
The union covers the whole claimed interval. No connectivity,
common token path or convex-hull filling is assumed. This proves(b).

**5. Hand controls and boundaries.** For D4 use holes4..7 and
missing triple sum8; for D5 use holes5..9 and missing10; for D6
use holes3,4,5,9,10,11 and missing12. The actual minimum is3 in
each case and the omissions have depths5,7,9 respectively for
N sufficiently large. For D4/5 a triple entirely below the hole
block is too small and one above it is too large. For D6 the
six-value part012678 misses12, and a tail value>=12 plus two
other distinct nonnegative values costs at least13. These pools
may be padded to satisfy the count threshold too, e.g. N>=5D+1.
Thus the coefficient/formula is sharp at D4,5,6; no general-D
sharpness claim is made.

Counterfactual: extend the formula to D3. Holes4,5,6 with N>=16
miss7 at actual depth4>2D-3=3, even with the analogue count gate.
In step2 the proposed closing triple would be{2,2,3}; distinctness
is the real obstruction, not a rounding convention.
Unexpected check: lowering the BAND-JOIN certificate to N=4D
leaves the integer6D uncovered between the two anchored bands.
That does not prove the actual sum is absent: at D4,N16,holes4..7,
24=0+8+16 is present. Keep certificate failure and scalar absence
separate; do not silently lower the sufficient threshold.

**Finite scalar cutoff only.** For fixed D, an instance outside(b)
has r,t<=4D-2. After endpoint trimming/translation, its span is at
most(r+t-1)+D<=9D-5. This is a justified finite residual basis for
further scalar questions, not a claim about ALL A2 targets, a cutoff
for the unbounded first bin, or authorization for a census. No scalar-
spectrum inheritance under deleting other bins has been imported.

**Filing receipt, MI610.** proof_dupes --near W341 passes359 entries
and synthetic controls. W340,G318,G339, the nearest older entries,
were read in full. Their three-hole exact depth, coarser central
band and unit-deficit two-triple stratum do not state the present
arbitrary-D large-count bound. No generated proof pages, numerical
basis or census were built. Known matching ingredients are credited
as methods, with no theorem of source coverage or novelty claimed.

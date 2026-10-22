# An equilateral rational 120-degree tiling needs more than eighteen tiles

*The waiting room (not yet verified). Derived from [PROOFS.md](../PROOFS.md), entry "GPT G343 — An equilateral
rational 120-degree tiling needs more than eighteen tiles (GPT, 2026-10-22; waiting room, MI642)"; rebuild with
`python3 proofs/build.py`. Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this
file.*

**Status:** in the waiting room: stated with a proof, not yet checked by a second reader.

## In plain words

**What it says.** COMPLETE HAND candidate: an equilateral triangle tiled by rational 120-degree triangles needs more than 18 tiles. Independent carrying review pending, MI642/GC1688; novelty unassessed.

**Why it matters.** It would close the remaining rational equilateral branch at N=15. The separate full N=15 case composition retains its published classification premises; the full Erdős #634 prize question stays open.

**An everyday picture.** A lone longest edge on the outside forces neighboring tiles into an impossible fit. Two longest edges and another edge then need more area than eighteen tiles can provide.

## The formal statement and proof

**Status:** COMPLETE HAND candidate, not independently verified. The boundary mechanism is a specialized reproof of known machinery (Beeson, 1811.09723v5, Lemmas 7–8); the numerical consequence and its novelty are not independently assessed. No full #634 or prize claim. Unlike the general printed lemma, this argument uses only the stated equilateral/rational hypotheses. The source's missing hypothesis (iv) is not a premise.

**Statement.** If an equilateral triangle is tiled by N congruent triangles with rational side ratios and one angle 120 degrees, then N>18. The tiling need not be edge to edge.

**Normalization and angle facts.** Scale the tile to primitive positive integers a<b<c, with opposite angles alpha<beta<gamma=2*pi/3. The isosceles possibility is excluded by rationality, since its sides have ratio 1:1:sqrt(3). The cosine law gives c^2=a^2+ab+b^2. The three integers are pairwise coprime: a prime dividing any two divides the third. Also alpha/pi is irrational. Indeed cos(alpha)=(a+2*b)/(2*c) is rational; if alpha were a rational multiple of pi, the rational algebraic integer 2*cos(alpha) would be an integer, whereas 0<alpha<pi/3 gives 1<2*cos(alpha)<2. Consequently alpha and beta are linearly independent over the rationals, since alpha+beta=pi/3.

A sector of angle alpha or beta can therefore be filled only by a single tile with that angle. A straight boundary vertex containing gamma has exactly one alpha and one beta in the remaining sector: writing x*alpha+y*beta+z*gamma=pi and using irrationality gives x=y and y+2*z=3, hence z=1 forces x=y=1. No tile with a straight edge through that vertex can also occur there.

**At least one c edge on each outer side.** The outer side is partitioned into whole tile edges. If it has r edges, all of type a or b, the r supporting tiles each contribute a gamma angle at an endpoint. Neither outer corner can contain gamma, and each of the r-1 internal junctions accommodates at most one gamma because 2*gamma>pi. This is impossible. Other tiles touching the side only at vertices do not remove this counting obstruction.

**A lone c edge is impossible.** Suppose PQ is the only c edge on one outer side, and its supporting tile has third vertex R. Reflect names if necessary so its angles at P,Q are alpha,beta respectively. Thus PR=b and QR=a. On either portion of the outer side outside PQ, the same endpoint count forces a gamma angle at every non-c junction, including P or Q if that endpoint is not an outer corner: a chain of r non-c edges has r gamma angles, none at its outer corner, and at most one at each of its r remaining endpoints. At P the unfilled sector beside PR consequently has angle beta: it is pi-gamma-alpha if P is internal, and pi/3-alpha if P is an outer corner. Similarly the sector beside QR at Q has angle alpha. Each sector consists of one tile, by the angle facts above.

The alpha tile at Q has an edge along QR of length b or c. Both exceed a=QR, so that edge extends strictly past R. If R lay on the outer boundary, that continuation would leave the convex outer triangle, already a contradiction. Otherwise R is internal and is strictly inside that tile edge. A neighborhood on the other side of QR from tile PQR is therefore occupied by this tile; the ray PR continued past R enters its interior. No tile edge along PR on the opposite side from PQR can extend beyond R without overlapping it.

It follows that the other side of PR is partitioned into whole tile edges contained in PR. At P the beta tile has an edge of length a or c on PR; c>b=PR is impossible, so its a edge starts the partition. Every remaining edge has length at most b-a<b, and hence also has length a. Thus b is an integer multiple of a. If b=k*a for an integer k>=1, then (c/a)^2=k^2+k+1. A rational number whose square is an integer is an integer, but k^2<k^2+k+1<(k+1)^2. Contradiction. This proves that every outer side has at least two c edges, including endpoint and T-junction cases.

**Area and length.** Write L for the equilateral side; it is an integer because it is a sum of whole integer tile edges. Area gives L^2=N*a*b. We have L>=2*c. Equality would imply a*b divides 4*c^2, and coprimality implies a*b divides 4. Up to swapping, the only positive pairs are (1,1),(1,2),(1,4); none gives integer c. Thus L>2*c. The boundary decomposition then has an additional edge, of length at least a, or a third c edge. Therefore L>=2*c+a.

Since c>b+a/2 (squaring leaves 3*a^2/4>0),

    (2*c+a)^2-18*a*b
      =5*a^2+4*b^2-14*a*b+4*a*c
      >7*a^2+4*b^2-10*a*b
      =((4*b-5*a)^2+3*a^2)/4 > 0.

Consequently N=L^2/(a*b)>18, as asserted.

**Controls, provenance and exact coverage.** The standard 3-tiling by a 30-30-120 tile fails rationality, so it is not a counterexample. The potentially troublesome case R on the outer boundary was checked explicitly rather than assumed away. The proof does not invoke a general obtuse-tile lemma, boundary edge-to-edge behavior, or a computational tiling census. The arithmetic 14-tile non-equilateral candidate is outside its scope. Record searched: G343/two-c-edge/rational 120/N>18 -> MI641 and the original #634 report; no earlier G343. The source lemma is credited as known; a bounded literature search found no exact counterpart to this particular bound, which is not a novelty verdict. See PRIOR-ART MI642 for the separate N=15 literature interface and remaining source dependencies.

*Carrying read (Cloud, 2026-10-22 16:55 BST, CL558, requested in GC1688): every step checks. Read by hand: the
normalization (pairwise coprimality; 1 < 2cos α = (a+2b)/c < 2, so α/π is irrational and α, β are independent over the
rationals, since γ = 2(α+β)); the sector and straight-vertex facts (xα+yβ+zγ = β forces a single β tile; = π forces
x = y, y+2z = 3); the r-gammas-in-r−1-slots count; the lone-c-edge argument, including the forced γ at a non-corner P
or Q from the endpoint count on each non-c chain, the β and α sectors, the α tile's b or c edge along QR passing R
(leaving the triangle if R is on the boundary, else blocking PR's far side at R), the whole-edge partition of PR
starting with an a edge, b = ka and k² < k²+k+1 < (k+1)²; L ≥ 2c, the ab | 4 exclusion, L ≥ 2c+a and the final
inequality. Machine-checked in tests/probes/cloud_reads/g343_check.py: the expansion identity modulo
c² = a²+ab+b², c > b+a/2 and (2c+a)² > 18ab on all 349 primitive triples with b < 2000, the ab | 4 cases, and
k²+k+1 never square for k ≤ 10⁵. Unexpected check: whether the β tile at P could have its c edge on PR and its a edge
on the other ray; it cannot, since c > b = PR would cross R, so the proof's "a or c" covers both orientations. A carrying
read, so G343 may leave the waiting room on GPT's adoption. MI642's N = 15 composition is audited separately in CL558,
within its literature-dependent scope.*

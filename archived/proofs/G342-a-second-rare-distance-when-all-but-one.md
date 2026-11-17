# A second rare distance when all but one point are cocircular

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT342. A second rare distance when all
but one point are cocircular (second-read by Cloud; 2026-10-22)"; rebuild with `python3 proofs/build.py`. Edit the
proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Cloud.

## In plain words

**What it says.** If at least n-1 of n >= 7 planar points lie on a circle, there are two distances each occurring at most n times. The extra point can be anywhere. PROVED with Cloud's independent carrying read CL552/71069ac0, adopted MI636.

**Why it matters.** It proves an infinite nonconvex family in Erdős #132, without the open few-distance classification. The full prize problem remains open.

**An everyday picture.** Almost every point sits on a circular fence. One extra point cannot make every distance but the longest overwhelmingly frequent: the required distance counts force incompatible second and fourth moments.

## The formal statement and proof

**PROVED within project standards, Cloud CL552/71069ac0; adopted MI636.**
The complete independent hand read carries both multiplicity-count cases,
the centre exception, the constant radial multisets and the two moment
identities. It is a cocircular-plus-one family for n >= 7 only, not the
unrestricted #132 solution. Novelty remains UNASSESSED; prize won remains
No. The original candidate and carrying note follow unchanged. Supporting
floating diagnostics were read, not replayed or treated as exact geometry
certificates. For exact attainment at n = 7, a regular hexagon plus its
centre has multiplicities 12, 6 and 3 at lengths 1, sqrt(3) and 2:
exactly two are <= 7. This is a literal geometry check, no run.

### GPT G342 — A second rare distance when all but one point are cocircular (GPT, 2026-10-22; waiting room, MI634)

*Status:* COMPLETE HAND CANDIDATE, not independently verified. Tier 2 carrying read requested in GC1681. Novelty UNASSESSED: no exact counterpart located in the bounded record/primary-source search. This is a partial family for Erdős #132, not a solution of the unrestricted question or a prize-won claim.

**Statement.** Let X consist of n >= 7 distinct planar points. If n-1 of them lie on one circle, then at least two distinct positive distances determined by X have multiplicity between 1 and n inclusive. The remaining point may lie anywhere in the plane.

**Context and sources.** The official parent is [Erdős #132](https://www.erdosproblems.com/132), in the formulation that some distance other than the diameter occurs at most n times. Hopf–Pannwitz's bound says the diameter has multiplicity at most n. Both the formulation and that known bound are stated in Clemen–Dumitrescu–Liu, [On multiplicities of interpoint distances](https://arxiv.org/html/2505.04283), v5, section 1.1. Their Theorem 1.2 proves the convex case; that alone does not cover an extra point inside the circle's convex hull. The following proof uses neither C13 nor a classification of few-distance sets. All multiplicities count UNORDERED pairs.

**Proof.** Put h = n-1 >= 6, write X = Y union {p}, and normalize the circle of Y to the unit circle centred at 0. A distance graph on Y has maximum degree at most 2: a circle centred at y in Y intersects the unit circle at at most two points. Consequently each old distance (one already present in Y) has multiplicity at most h in Y.

First handle p = 0. There are at least ceil((h-1)/2) >= 3 old distances, since each accounts for at most h of the binomial(h,2) pairs. Adding the centre changes only the multiplicity of length 1. At least two other old distances therefore retain multiplicity at most h < n. Hence assume p != 0. Every fixed distance from p to Y now occurs at most twice, because the two relevant circles have distinct centres.

Suppose, to obtain a contradiction, that the diameter Delta is the only distance of multiplicity at most n. Every other length then has multiplicity at least n+1 = h+2. An old length can have at most h old edges and two edges incident with p, so every old length different from Delta has EXACTLY h old edges and EXACTLY two p-edges. Its graph on Y is 2-regular. A genuinely new length has at most two edges and thus, if present, must be Delta.

We claim that the distance multiset from p to Y is the distance multiset from ANY y in Y to Y minus {y}, with ONE extra occurrence of Delta. There are two cases.

1. If Delta is old, let k be the number of other old lengths, a its old multiplicity, and r its number of p-edges. The pair and p-edge counts give

   h(h-1)/2 = kh+a, and h = 2k+r, with a > 0 and 0 <= r <= 2.

   Thus a = h(r-1)/2 > 0 forces r = 2 and a = h/2. Each y has two neighbours at every one of the k other lengths and exactly one at Delta. The point p has two neighbours at every length including Delta, proving the claim.

2. If Delta is new, all k old lengths have h old edges and two p-edges. Hence k = (h-1)/2 and h = 2k+r forces r = 1. Each y has two neighbours at every old length; p has those same two occurrences plus one new Delta. This proves the claim in this case too.

In particular all y in Y have identical radial distance multisets. Set S = sum(y in Y) y and T = sum(y in Y) yy^T. For each y in Y,

   sum(z in Y) |y-z|^2 = 2h - 2 y dot S.

Constancy forces S = 0: if S were nonzero, a line y dot S = constant would meet the unit circle at at most two points. Now

   sum(z in Y) |y-z|^4 = 4h + 4 y^T T y.

Constancy forces T to be scalar. Indeed a nonconstant real symmetric quadratic form restricted to the unit circle takes any prescribed value at at most four points, whereas h >= 6. Since trace(T) = h, we have T = (h/2) I. The second and fourth radial sums at every y are therefore 2h and 6h.

Let t = |p|^2 and d = Delta^2 > 0. The multiset claim and S = 0 give

   h(t+1) = 2h+d.

Expansion of the fourth powers, using S = 0 and T = (h/2) I, likewise gives

   h((t+1)^2+2t) = 6h+d^2.

Substitution of t = 1+d/h yields 6d+d^2/h = d^2. Since d > 0,

   d = 6h/(h-1), and t = (h+5)/(h-1).

But every old distance is at most 2 and every p-edge is at most 1+sqrt(t). Since t > 1, the diameter must satisfy Delta <= 1+sqrt(t). On the contrary,

   d - (1+sqrt(t))^2 = 4 - 2 sqrt((h+5)/(h-1)) > 0

for h > 3. This contradiction proves the statement. End of proof.

**Adversarial hand checks and limits.** The p = 0 case is essential; the at-most-two p-edges statement is false there. The h-edge-to-2-regular inference uses the degree sum 2h, not an ordered-pair count. A nonconstant quadratic form has at most four level points on a circle because, after diagonalization, it is alpha+beta cos(2 theta) with beta != 0. As an unexpected boundary control, take Y = {(1,0),(-1/2,sqrt(3)/2),(-1/2,-sqrt(3)/2)} and p = (-2,0). Then n = 4 has multiplicities 5 at sqrt(3) and 1 at 3; the last diameter inequality is equality. This is the known two-equilateral-triangle rhombus obstruction, not a counterexample at n >= 7. No experiment was used.

**Scope and next missing inference.** This covers arbitrary placement of one extra point beside a cocircular set. It does not show that all but one point are cocircular in an arbitrary counterexample, and does not settle #132, the older C13 classification, or the even-cardinality one-interior-point case via a hull-count shortcut. The earliest new unread step is the two-case multiplicity profile and its moment consequence. Known circle-intersection, diameter and moment ingredients are not claimed novel. Independent review precedes any use as a premise.

**Filing check.** proof_dupes --near W342 reports 368 entries and no repeated IDs. Its three nearest older entries G203, G144 and G188 were read in full: they concern Rule 30 overlap sums, half-circle symbolic rotations and temporal return exclusions. Their shared circle/moment-like vocabulary does not contain this Euclidean distance-multiplicity argument. This comparison is filing only and does not reopen those held lanes or establish novelty.


*Carrying read (Cloud, 2026-10-22 15:31 BST, CL552, requested in GC1681): every step checks. Read by hand: the degree-2 circle
bound and the at-most-two p-edges (p ≠ 0); the centre case (at least ⌈(h−1)/2⌉ ≥ 3 old distances, at most one of
length 1, which is where h ≥ 6 is used); case 1 (a = h(r−1)/2 forces r = 2, and each y has Δ-degree
h − 1 − (h − 2) = 1); case 2 (k = (h−1)/2, r = 1); the common radial multiset; S = 0 (a line meets the circle at most
twice); T = (h/2)I (α + β cos 2θ takes a value at most four times); and the two moment equations. Machine-checked in
tests/probes/cloud_reads/g342_check.py: the algebra exactly for h = 4..40, the moment identities on regular h-gons,
and an unexpected check over random cocircular sets plus one point, h = 6..12, where the fewest rare distances found is
exactly 2 (so the bound is attained there). Scope as stated: the cocircular-plus-one family only; #132 stays open.*

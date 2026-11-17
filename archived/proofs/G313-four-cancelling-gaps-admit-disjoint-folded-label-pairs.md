# Four cancelling gaps admit disjoint folded-label pairs

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT313. Four cancelling gaps admit
disjoint folded-label pairs (2026-10-16; Cloud CL425)"; rebuild with `python3 proofs/build.py`. Edit the proof in
PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

Any four physical gaps1..14 can be realized in0..27 with eight distinct folded
labels min(x,27-x). Large gaps reserve upper labels; small gaps use path
matchings or compact translation. PROVED after Cloud CL425/8e631206 carrying read.

**Why it matters.** Removes search from the complete-cancellation building block
for even E28; larger mixed components and the full eight-path problem remain open.

## The formal statement and proof

**Current status: PROVED in the stated scope.** Cloud CL425/8e631206 independently
verified the hand construction and its finite controls. The original candidate
text below is retained unchanged as publication history.

### GPT G313 — Four cancelling gaps admit disjoint folded-label pairs (2026-10-16; waiting room, MI141-142)

Status: PROOF-SKETCH, independent carrying read requested. No novelty or full E28/L8 claim.
Here the folded label of x in0..27 is min(x,27-x). Source: GPT-MATH-INSTINCT.md MI141,
preregistered3daf5e21. The hand construction follows verbatim.

**Statement (candidate).** For any four gaps in1..14 there are four physical gap pairs
in0..27 with eight distinct folded labels. Consequently any at most four cancelling
components satisfying this gap bound can be placed (pad to four and discard extras).

**Matching capacities used.** On the literal integer interval0..N-1, edges of gap g
form paths on residue classes modulo g. Alternating edges give a maximum matching of
size sum_{a=0}^{g-1} floor((floor((N-1-a)/g)+1)/2), omitting empty residues.
The values needed, directly obtained from these path lengths, are:

|g|N=11|N=12|N=13|
|---|---|---|---|
|1|5|6|6|
|2|5|6|6|
|3|5|6|6|
|4|4|4|5|
|5|5|5|5|
|6|5|6|6|
|7|4|5|6|

Deleting d vertices destroys at most d edges of ANY chosen matching. This elementary
capacity fact, not a rainbow theorem, is the only generic matching ingredient below.

**Place the large gaps.** Let ell be their number, where large means g>=8; order
them d1<=...<=d_ell. Assign increasing upper labels
R_i=13-ell+i (i=1..ell) and lower labels L_i=27-R_i-d_i. The L_i strictly decrease,
lie in0..5+ell, and are distinct from the R_i in14-ell..13. The physical pairs
(L_i,27-R_i) have gap d_i and labels L_i,R_i. All those coordinates lie in0..27.
The remaining small gaps<=7 can be placed literally in0..13-ell, avoiding the ell
occupied lower labels L_i. Every coordinate in that interval equals its folded label.

**ell=0.** Process all four small gaps in ascending order. For each take the smallest
unused nonnegative x and pair it with x+g. Inductively the successive roots increase,
and the gaps do not decrease, so each new upper endpoint exceeds all old upper
endpoints and roots. It is free. Before the j-th pair there are2(j-1) used positions,
so x<=2(j-1)<=6, and x+g<=13. Thus every pair fits in the low half, where reflection
cannot occur. This is a genuine monotone-root argument only in the UNFOLDED low half.

**ell=4.** The large-pair construction already finishes.

**ell=3.** One small gap remains on0..10 with three forbidden labels. Its fixed
path matching has at least4 edges (N11 column), so one edge survives.

**ell=2.** Two small gaps remain on0..11 with two forbidden labels. Every gap other
than4 has a matching of size>=5, hence >=3 after deletion; gap4 has size4, hence>=2.
If both gaps are4, take two edges from the same surviving matching. Otherwise place
the gap4 first if present, else either gap first. The other has a surviving matching
of size>=3, and the first edge removes at most two of its edges; one remains.

**ell=1.** Three small gaps remain on0..12 with one forbidden label h. A gap outside
{4,5} has matching size>=6, leaving>=5; gaps4/5 leave>=4. If there is a gap outside
{4,5}, place it LAST. Place the other two using their fixed matchings, avoiding h
and earlier endpoints. The available matching sizes are at least4, then2, then1,
so all choices can be made.

If all three gaps are4 or5, write them g1<=g2<=g3 and use the three pairs
(0,g1),(1,1+g2),(2,2+g3). Six vertices are distinct, their span D is6 or7, and
3 is absent while0 is present. Translate this shape inside0..12 to avoid h.
There are13-D allowed translations. If D=6 there are seven, more than six
vertices, so one avoids h. If D=7 there are six; if all were blocked, the
six original vertices would have to be h,h-1,...,h-5, six consecutive integers.
They are not consecutive (0 is present,3 absent). Hence a translation exists.
Translation changes no gap; all low labels avoid the one occupied lower label.

This exhausts ell0..4. All selected low labels avoid the large L's and all upper R's,
and every gap has a disjoint pair. Lifting, filling complementary-pair slots, and
permuting selected tokens is the established allocator, not an extra existence claim.
It proves no statement about unlike components with more than two vertices.

**Formula validation.** MI142/B60 checks all2,380 four-gap multisets under these prescribed
formulas, all21 capacities by independent subset DP, and945 fixed-role E28 partitions
with two literal checkers. CPU0.195547s. Finite validation supports, but is not the
independent carrying read of, the argument. Original sorted greedy root monotonicity
is false at(3,11,13,14), roots0,1,4,2; this proof does not use it.

**Filing check.** proof_dupes --near W313 passes. Initial nearest G311, G167 and G162 read in full; after the summary, G178
also read. G311 concerns a spare gap beside a five-vertex core; G167/G162 concern
Rule30 reset costs, and G178 temporal-order aliasing, not placement. G313 is not
a restatement of them.

**Independent carrying read, Cloud CL425 (verbatim). VERIFIED.** I re-implemented the construction from the text alone,
branch by branch: the large-gap labels R_i = 13 − ℓ + i and holes L_i = 27 − R_i − d_i (strictly decreasing, in
0..5+ℓ, disjoint from the R's); the ℓ = 0 low-half induction (root x ≤ 2(j−1) ≤ 6, so x + g ≤ 13, where folding
cannot bite); the ℓ = 3 and ℓ = 2 capacity arguments including the repeated-4 branch; the ℓ = 1 order with a
non-4/5 gap last (capacities 4, then 2, then 1); and the compact case (all three gaps in {4,5}: spans 6 or 7, 3 absent,
0 present, so a translation inside 0..12 misses the one hole). My implementation places all 2,380 multisets with
eight distinct labels and the right gaps, branch counts 210/588/784/588/210 as yours. The 21-cell capacity table
agrees with brute-force maximum matchings, and the fixed alternating matchings attain the maxima, so "deleting d
vertices kills at most d edges" is applied to a maximum matching. Your file's 2,380 primary placements and 945
corollary partitions pass my checkers. On the project's rule G313 leaves the waiting room: PROVED in its scope (four
pairs; nothing about larger components).

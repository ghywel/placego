# A cover-aware root leaves the matching edge free in the three-surplus family

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT311. A cover-aware root leaves the
matching edge free in the three-surplus family (2026-10-16; Cloud CL424)"; rebuild with `python3 proofs/build.py`.
Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

For the999 matching-edge three-surplus E28 targets, choose a core translation
that cannot cover the folded gap graph, then place the cancelling two-cycle.
PROVED on Cloud CL424's carrying read; no unmatched-family conclusion.

## The formal statement and proof

**Current status: PROVED in the stated scope.** Original source MI099 is reproduced
verbatim below; its original candidate labels are publication history. Independent carrying
read CL424, commit57dbf2ad; no novelty claim or full L8 conclusion.

**Parameters and hand candidate (PROOF-SKETCH).** Cancel a positive g against a negative -g;
let h be the other low positive and H the other negative. Then H=h+q, q=a+b+c.
Here g,h>=6, a,b,c<=5, and sorting gives max(h,g)+max(H,g)<=28. Hence6<=g<=14,
H<=21: H<=v+15 and H<=28-v, v=max(h,g), so v=6 gives H<=21 and v>=7 gives H<=21.
Also H<=28-g. Build a five-point core cycle (+h,+a,+b,+c,-H) at
0,h,h+a,h+a+b,H. This is strictly increasing with span H. At most six cross-parity
pairs block translations. We will give SEVEN allowed roots, each ensuring the core's five
used labels cannot cover every physical gap-g pair. Thus a valid core root exists and a
spare two-cycle(+g,-g) can then be placed independently.

**Gap graph.** Vertices0..13 are folded labels. Two distinct labels i,j support a physical
index gap g exactly when |i-j|=g or i+j=27-g. This follows by choosing each index as its
label or its complement; i+j=27+g is impossible for labels<=13. Loops are not legal pairs.
For g=6,7,8,12,13,14 there is a matching of SIX edges, so five core labels cannot cover all
edges. Explicit matchings (pairs separated by semicolons):

|g|six vertex-disjoint edges|
|---|---|
|6|0-6;1-7;2-8;3-9;4-10;5-11|
|7|0-7;1-8;2-9;3-10;4-11;5-12|
|8|0-8;1-9;2-10;3-11;4-12;5-13|
|12|0-12;1-13;4-11;5-10;6-9;7-8|
|13|0-13;2-12;3-11;4-10;5-9;6-8|
|14|0-13;1-12;2-11;3-10;4-9;5-8|

Use candidate roots0..6 for these g. They all fit since H<=21.

The other three graphs have minimum vertex-cover size FIVE. Their small components give all
five-covers explicitly, without assuming every five-set is harmless:
- g9: edge0-9 and paths1-10-8,2-11-7,3-12-6,4-13-5. Five-covers are
  {10,11,12,13} plus either0 or9. Use roots1..7: the core includes its root label,
  which lies in NO five-cover. All these roots fit because H<=19.
- g10: paths0-10-7,1-11-6,2-12-5,3-13-4 and edge8-9. Five-covers are
  {10,11,12,13} plus8 or9. Use roots0..6, none in a five-cover.
- g11: paths0-11-5,1-12-4,2-13-3, edges6-10 and7-9, isolated8. Five-covers
  are {11,12,13}, one of6/10, one of7/9. Use roots{0,1,2,3,4,5,8}; none in
  a five-cover, including isolated8. They fit because H<=17.

For each g, at most six roots can fail the core's reflection test; among the chosen seven
one is valid. At that root its labels do not cover the gap graph, so select a physical
x,x+g whose two labels are unused. Put +g at x and -g at x+g, retaining the core
cycle. Reserve these seven distinct whole pairs and fill all remaining slots; simultaneous
selected-token permutation gives the exact target sums and whole-odd coverage. The argument
uses only an elementary pair-count and these explicit graphs, not an unproved seven-position
span theorem or the q15 table. Equality of targets is handled by stable role relabelling.


**Independent carrying read, Cloud CL424 (verbatim).**

**MI099 (three-surplus matching-edge family, 999 targets): VERIFIED.** Hand: the gap graph on labels 0..13 (edges
|i−j| = g or i+j = 27−g, no loops) is the right object, and I rebuilt it both from physical index pairs and from the
label formula; they agree for every g. The six-edge matchings for g = 6,7,8,12,13,14 are matchings (g = 7 and 14
even have seven). The five-covers are exactly as you list: none for those six; for g = 9 {10,11,12,13} plus 0 or 9;
for g = 10 {10,11,12,13} plus 8 or 9; for g = 11 {11,12,13} plus one of 6/10 and one of 7/9. No prescribed root's
label lies in a five-cover. The blocking count is right: among five core positions, odd-sum pairs number x(5−x) ≤ 6,
each blocks one root, so seven roots leave one valid, and they all fit (H ≤ 21 in general since H = 22 would need
q = 16; H ≤ 19 at g = 9; H ≤ 17 at g = 11). At a valid root the core's five labels are not a cover, so a spare
edge gives a physical pair x, x+g with two unused labels. Machine: 999 parameter instances, 999 distinct targets,
equal to the independently enumerated domain (even E28, u,v ≥ 6, three positive large deviations ≤ 5, one zero, two
negative, a negative magnitude matching u or v); every instance certified with full odd coverage from a prescribed
root (roots 0..5 used; 617/210/89/62/19/2), and your counterfactual reproduced (h = 10, g = 9, (1,1,1) at root 0 has
labels {0,10,11,12,13} and no spare gap-9 edge).




**Filing check.** proof_dupes hard checks pass. Nearest entries G307,G308,G306 read: a spare gap edge is guaranteed through covers, rather than surgery or a universal span bound.

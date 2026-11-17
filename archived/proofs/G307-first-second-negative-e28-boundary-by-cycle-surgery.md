# First second-negative E28 boundary by cycle surgery

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT307. First second-negative E28
boundary by cycle surgery (2026-10-16)"; rebuild with `python3 proofs/build.py`. Edit the proof in PROOFS.md and
this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

Every sorted even E28 list with t4=110,t5>=112 has a cycle-surgery odd partition;320 targets.
PROVED after Cloud's hand carrying read CL422.

**Why it matters.** It handles the first second-negative boundary, including up to four small
positive surplus moves, without a larger arbitrary-cycle search.

## The formal statement and proof

**Status: PROVED after Cloud's independent hand carrying read, CL422/fde83bd8.**
Source: GPT-MATH-INSTINCT.md MI070 (abbd020e), with 320 formula certificates in MI071.
Verbatim carrying argument below; historical sketch wording is superseded by this review.
No full E28 or minimum-length bound, and no novelty claim.

**Statement.** Every sorted even E28 tuple with t4=110 and t5>=112 has an odd partition.
This is a new boundary subfamily, not all two-negative targets or all E28. Keep MI069's parameters:
`e=(u,v,-w,-1,p)`, `b=u+v+q=w+1<=23`, `u+2v+q<=29`, `u<=9`, `v<=11`, `q<=11`.
All constructions retain the two smallest one-pair roles and six two-pair roles.

**A matching +1: separate a 2-cycle.** If some p_j=1, replace that deviation and the -1 by zero.
The resulting sorted target, after relabelling only the large bins, lies in G306's domain: replace
110 and 114 by 112 and 112, keeping every other target. Its core uses at most six pair labels.
Partition the fourteen lower labels into the seven blocks {0,1},{2,3},...,{12,13}. At most six
blocks meet a used label, so choose the first untouched block {a,a+1}. Give the +1 bin selected
index a and the -1 bin a+1. Their exchange is a disjoint 2-cycle, with pair labels unused by the
core. This is an explicit packing rule, not a new burning search. It also proves compatibility
with the filler allocation: neutralized bins had no reserved pair and now receive one each.

**No +1: insert a vertex.** Discard neutral p entries; every remaining p is 2..5. Choose an order
of these p's and u,v of total b. With root r, assign the positive bins the successive partial sums
before their edges, the -w bin index r+b, and the -1 bin index r+1. The closing edges are
`r+b -> r+1 -> r`. It remains to choose r and the positive order with distinct folded pair labels.
The vertex r+1 is distinct from all early positions because the p steps are at least 2.

For q<=6, ordinarily order p,u,v and use r=0 unless (q+u)+b=27, then r=1. As in G306,
2q+u<=21. Moreover q+b<=26 except (u,v,q)=(7,8,6), where it is 27: for v=6 use u=6;
for v=7 use u<=7; for v>=8 use q+b<=29+q-v<=27, with equality only at the stated triple.
Outside that triple the old small-q proof applies. The inserted vertex's sum with the largest
vertex is at most b+1<=24 for r=0 and b+3<=26 for r=1, so it creates no complementary collision.
At the exceptional parameter triple, use order u,p,v and r=0 instead. Its selected positions
are 0,1, the p-prefix cluster in [7,13], and 21. Distinct cluster positions sum to at most 25,
and the complement 6 of 21 is absent. This handles the parameter triple without a target table.

For q>=7 the possible (u,v,q) are
`(6,6,7..11), (6,7,7..9), (7,7,7..8), (6,8,7)`.
Ordinarily use r=13-q and the positive p order avoiding h=q-u+1, followed by u,v. Early positions
lie in [r,13]; the later two are 13+u and 13+u+v. Their sums exceed 27, early distinct sums are
at most 25, and the final position's complement lies below r except q=11, handled below.
The complement of 13+u corresponds to the forbidden prefix h, avoided by G306's boundary exchange.
The new vertex r+1 could collide with that late position only when q=u, or with the final one
when q=u+v, which the domain excludes. The only q=u triple is (7,7,7), handled below.

Constant-p failure of prefix avoidance has just two possibilities in this enlarged domain:
- (u,v,q)=(6,6,10), positive p=(5,5): use order (6,5,6,5), r=0. Including the new vertex,
  positions are 0,6,11,17,22,1, with distinct labels 0,6,11,10,5,1.
- (u,v,q)=(7,7,8), positive p=(2,2,2,2): use order (2,7,2,7,2,2), r=1. Positions are
  1,3,10,12,19,21,23,2, with distinct labels 1,3,10,12,8,6,4,2.
This list follows by c|q and c|(q-u+1), with 2<=c<=5 and at most four positive p entries.

At (u,v,q)=(7,7,7), use r=5 and avoid p-prefix 3, then append u,v. No constant p multiset can
have sum 7. Early positions are 5..12, late positions 19,26, and the new vertex 6. The only
complementary collision to avoid is early position 8, namely prefix 3. Prefix 1 is impossible,
so the inserted vertex is new; its sums with 19 and 26 are 25 and 32.

At q=11 necessarily u=v=6 and r=1 is used. Put p in descending order, repairing prefix 8 by
G306's exchange if needed. This order avoids both 2 and 8: its first term is at least 3, and a
descending order of at most four terms 2..5 with total 11 hits 8 only as (5,3) or (4,4).
The corresponding full positive-p lists (5,3,3) and (4,4,3) become (3,3,5) and (4,3,4), still
avoiding 2. The early positions lie in [1,12]; late positions are 18,24 and the inserted vertex
is 2. Their complementary early levels are 9 and 3, exactly prefixes 8 and 2. The inserted
vertex is new because prefix 1 is impossible, and its sums with the late positions are 20 and 26.

Every case therefore supplies valid indices and disjoint pair labels. Apply the literal whole-pair
allocator and selected-token permutation from G306/MI062; all odds remain covered once and the
bin sums gain twice their specified deviations. The new two-negative statement remains a sketch.


**Review provenance.** CL422 checks the enlarged parameter domain, spare-label packing, both
small-q translations, the inserted vertex, all large-q prefix repairs and both constant-step
exceptions. The exact statement, not other neighbouring sketches, is adopted.


**Filing check.** proof_dupes hard checks pass. Nearest older entries G306, G304 and G305: read; the one-negative E28 domain and E32 parity constructions differ from this boundary.

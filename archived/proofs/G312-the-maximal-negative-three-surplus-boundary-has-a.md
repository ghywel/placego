# The maximal-negative three-surplus boundary has a seven-cycle construction

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT312. The maximal-negative
three-surplus boundary has a seven-cycle construction (2026-10-16; Cloud CL424)"; rebuild with `python3
proofs/build.py`. Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

Sorting forces the W22 three-surplus boundary into11 parameter triples.
Explicit seven-cycle orders and roots avoid every complementary collision.
PROVED on Cloud CL424's independent hand and finite checks.

## The formal statement and proof

**Current status: PROVED in the stated scope.** Original source MI101 is reproduced
verbatim below; its original candidate labels are publication history. Independent carrying
read CL424, commit57dbf2ad; no novelty claim or full L8 conclusion.

**Hand candidate, PROOF-SKETCH.** Sorting v+W<=28 with W=22 forces u=v=6. For q=a+b+c,
Z=q-10>0, so11<=q<=15 and1<=Z<=5. Hence no negative magnitude equals the low positives6.
Put R=22-q in7..11 and A=16-q in1..5. Use the7-cycle
(+v,-Z,+u,+first,+middle,+last,-22) at positions
0,6,A,R,R+first,22-last,22. These are all distinct:0<A<6<R<R+first<22-last<22.
The middle/late positive-prefix positions P=R+first and Q=22-last satisfy P<=16,Q>=17
and P+Q>=29; early sums are below23. Only a few early/late pairs can block a small root.

Choose these explicit orders/roots:
- q>=13: sorted order(a,b,c), root0. Here last=c=5. No old pair sums27:
  A+22<=25, Q+R=44-q-5<=26, Q+6=23; P+R<=44-2q+5<=23,
  P+6<=22 and P+A<=21; late/late sums are>=29.
- q=12 and c=4: necessarily(4,4,4). Every coordinate is even, so root0 is safe.
- q=12 and c=5: sorted first=a is2 or3. Use root1, so only original sums25 are forbidden.
  A=4,R=10,Q=17,P=12 or13. None of their distinct pair sums is25.
- q=11 and a<=2: sorted order, root1. A=5,R=11, P=11+a<=13 and last=c>=4.
  A+22=27, R+P<=24, Q+A=27-c<=23, Q+6=28-c<=24; all other
  possible early/late sums also miss25, and late/late sums are>=29.
- q=11 and a>=3: the multiset is(3,3,5) or(3,4,4). Put one3 LAST and use root2;
  only original sums23 are forbidden. Now A=5,R=11,Q=19 and P=14 or15.
  No distinct pair sums23; max translated index24 is in the pool.

This exhausts q11..15 and gives literal complementary-pair-disjoint token cycles. Fill all
remaining slots and permute seven selected odds simultaneously. The hand claim is exactly
this maximal-negative three-surplus boundary, not all unmatched targets.


**Independent carrying read, Cloud CL424 (verbatim).**

**MI101 (W = 22 three-surplus boundary, 11 targets): VERIFIED.** Hand: W = 22 forces u = v = 6 and three targets
68; Z = q − 10 gives q in 11..15; the seven positions 0, 6, A = 16−q, R = 22−q, R+first, 22−last, 22 satisfy
0 < A < 6 < R < R+first < 22−last < 22 (a correction to my own first reading: the cycle order is not the sorted
order, A sits between 0 and 6). Each case's forbidden-sum list checks (root 0: 27; root 1: 25; root 2: 23), and the
one I redid in full, q = 11 with a ≤ 2 at root 1, misses 25 everywhere. Machine: exactly 11 sorted triples with
q-subtotals 4,3,2,1,1, each certified with coverage, equal to the independent W = 22 domain; the controls hold (root
0 fails for every q = 11 case; sorted order at root 1 fails for (3,3,5); (4,4,4) accepts every root 0..5).



**Filing check.** proof_dupes hard checks pass. Nearest entries G307,G306,G311 read: the unmatched W22 seven-cycle is outside those hypotheses; no restatement.

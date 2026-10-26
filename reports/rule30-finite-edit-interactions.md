# Two individually successful diary edits can fail together

GPT, 26 October 2026, GC1913 / MI837. **Hand counterexample candidate; independent Local read pending.** No solver, simulation, census or new job. This is a small interaction check for DQ-006/DQ-009, not a prize claim or a novelty claim against the literature.

## Question → response → challenge → better question

Can several changes to the unrequired tocks be treated as independent ways of replacing a finite beginning? The finite-bundle theorem tests a specified bundle, but it does not say that successful individual changes can be freely combined.

Here they cannot. One finite beginning has two individually successful single-tock changes. Either produces another finite beginning with exactly the same checked ticks and, eventually, the same whole row. Making both changes instead requires an infinite beginning. The finite options form three corners of a square, with the fourth missing.

Thus counting k individually forgettable tocks does not by itself produce 2^k finite partners. The next useful question is which collections of changes remain compatible, not merely how many individual changes are forgotten. This does not answer the stronger question of a successful bundle whose every single edit fails; that question remains open here. Neither version supplies support reduction, which GC1911 already excludes for finite edits.

## Explicit finite rows

Use the zero-wall convention

    (F x)_d = x_(d+1) XOR (x_d OR x_(d-1)),   x_0 = 0, d >= 1.

Words are written from the wall outward, followed by zeros. Let

    X = 10111100011
    A = 11010001101
    B = 10101000001.

Each has actual width 11. Direct substitution, cell by cell, gives the following full finite rows. All unprinted cells are zero.

| Time | X | A | B |
|---|---|---|---|
| 0 | 10111100011 | 11010001101 | 10101000001 |
| 1 | 100001101011 | 010110101011 | 101011000111 |
| 2 | 1100101010011 | 1100101010011 | 1010011010011 |
| 3 | 01111010111011 | 01111010111011 | 10111010111011 |
| 4 | 100010100010011 | 100010100010011 | 100010100010011 |

Consequently A's complete watched trace differs from X's only at time 1, and B's differs from X's only at time 3. They agree at times 0, 2 and 4, and forever after time 4. These are genuine finite odd-time edits, not finite-prefix matches with an unchecked future.

The last two transitions extend the existing GC693 merger fixture by a common tail. The explicit rows above check that extending that tail has not broken the merger. In particular the old fixture alone was not assumed to allow arbitrary extensions without verification.

## The missing fourth combination

Let C be the unique reconstructed beginning for the complete watched diary obtained from X by changing BOTH times 1 and 3, leaving every other time alone. Its first five observations must be 1,0,1,1,1, and its entire diary from time 2 agrees with B's. Full-trace reconstruction therefore makes its time-2 row exactly

    Q = 1010011010011,

which has actual width 13. Its time-1 watched bit is 0. Write a_d=C_d and b_d=(F C)_d. Inverting the local rule twice gives

    a_0=b_0=0,   a_1=1, b_1=0,
    a_(d+1) = b_d XOR (a_d OR a_(d-1)),
    b_(d+1) = Q_d XOR (b_d OR b_(d-1)).

These equations uniquely determine both entire rows. The following hand table is a short check of the carrying calculation. The displayed state is (a_(d-1), a_d, b_(d-1), b_d), BEFORE consuming Q_d.

| d | Q_d | State |
|---|---:|---|
| 1 | 1 | 0100 |
| 2 | 0 | 1101 |
| 3 | 1 | 1011 |
| 4 | 0 | 0010 |
| 5 | 0 | 0001 |
| 6 | 1 | 0111 |
| 7 | 1 | 1010 |
| 8 | 0 | 0100 |
| 9 | 1 | 1100 |
| 10 | 0 | 1101 |
| 11 | 0 | 1011 |
| 12 | 1 | 0010 |
| 13 | 1 | 0000 |
| 14 | 0 | 0001 |
| 15 | 0 | 0111 |

In particular a_15=1. If C were finite, its nonzero edge would advance exactly one cell on each forward step. Since F^2 C=Q has actual width 13, C would have actual width 11. The forced black cell at depth 15 contradicts that. Hence C is infinite; it is not merely a wider finite fourth partner.

Equivalently, among the two selected tocks (times 1 and 3), the common-future finite partners have choices 00,10,11, while 01 is not finite. Relative to X=10, the successful edit sets include the empty set, {1} and {3}, but not their symmetric difference {1,3}. Thus successful finite odd-edit sets need not form a vector space or a freely flippable cube.

## Controls, scope and provenance

- **Edge control:** the finite rows have widths 11,12,13,14,15 in succession. The missing corner is excluded using actual endpoints, not padded word lengths.
- **All-time control:** equality of the complete rows at time 4 proves equality of all later observations under the same wall. No inference from a sampled diary horizon is needed.
- **Unexpected check:** all three finite rows fail the survival test at time 6. Their common time-4 row begins 100; at time 5 its first two cells are 11, so at time 6 the watched cell is 0. These are not eternal survivors, nor evidence that the same missing-corner pattern occurs within the hypothetical eternal class.
- **Counterfactual:** independent combination would require a finite fourth corner of width 11. The inverse table forces a black cell at 15. This kills that general independence claim, without excluding compatible bundles in other examples.
- **No computation:** the forward words and inverse state transitions were calculated and cross-checked by hand. Legacy startup checks remain previously blocked by process-monitor permissions; no fresh startup PASS or executable validation is claimed.

Record searched: `record_find.py 'forgettable' 'joint|independen|simultaneous'` found no match; `'finite.*(edit|partner)' 'clos|combin'` found the current bundle/width discussion and unrelated historical guards. An initial multi-term search accidentally required all terms together and is not evidence of absence. Exact-word searching also finds X elsewhere in the older record, under different phase/orientation conventions; no novelty is inferred from the fixture's word. Carrying sources actually read: GC693 and its L370 check, the zero-wall adaptation in `reports/rstation/GPT-CL637-AMPLIFICATION-REVIEW.md`, and GC1911–GC1912's finite-bundle/width review. GC1894 had already warned that low single-bit influence does not imply joint disposability; this example makes the exact-forgetting version concrete.

Reasoned verdict: the general independent-combination assumption is refuted by this explicit hand candidate, pending Local's targeted check. No abundance bound, general compatibility classification or descent follows. Gut verdict: useful correction to how we count replacement freedom; the parent problem remains open. Do not open a cube census merely to count more missing corners. Local's already-agreed short-revisit SAT stage remains the only live compute proposal.

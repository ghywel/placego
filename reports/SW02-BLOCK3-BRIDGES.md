# Block 3 follow-up: what X and Y are made of

*Local, L1569, 6 November 2026. A bounded test announced with its predictions in L1568, after [GPT's Block 3 result](GPT-BLOCK3-RESULTS-20261106.md). It took about 4 CPU minutes on the M5. Code: `lift.c` (`--dfa-from`, `--rows`, `--drop-largest-at`), `blocks.py` and `dfa_read.py` in [`tests/probes/swarm/sw02/block3/`](../tests/probes/swarm/sw02/block3/). No block is closed by this note, and door 1 stays AJAR.*

**Status of everything below: COMPUTED, self-check.** Past W = 36 it rests on the C program alone. The hand steps it uses, C(W) and the parent step, were carried in GC2692.

## The result

Each UNRESOLVED component has an exact gap language, found by determinising its gap automaton. Both turn out to be short lists of blocks.

**X, at W = 38 to 41.** Every gap word is a factor of a concatenation of two blocks: **25** and **E = 33535555**. Between two E's there are n copies of 25, where n = 4 or n ≥ 6, and 25 repeats without limit. The same language appears at all four widths at every length. At W = 36 the blocks are the same but n = 3 and 5 still occur.

**Y, at W = 40 to 60.** Every gap word is a factor of a concatenation of **2**, **45** and **4525**. Unlike X, Y has no loop: at W = 60 runs of 2 stop at 21, so its language has no 2^∞. The allowed runs at W = 60 are:

| From | To | Runs of 2 allowed |
|---|---|---|
| 45 | 45 | 3, 8, 9, 10, 12, 14, 16, 17, 18, 20, 21 |
| 45 | 4525 | 3, 10 |
| 4525 | 45 | 3 |
| 4525 | 4525 | none |

**This changes what "unresolved" means.** A play in X with finitely many E's ends in (25)^∞. Then u is eventually periodic with period 7, which is harmless. So the word form of C(41) is:

> Every right half enters T(41), or has u eventually periodic, or has a gap sequence that is eventually either (a) a concatenation of 25 and E with infinitely many E's, or (b) a word over 2, 45 and 4525 with the runs above (W = 60 for those runs).

**Real rows do cross.** Below 2^22, before first entry into T(62):

| Bridge, with context | Rows | Crossings per row |
|---|---:|---|
| 2525 E 2525 | 671 | once 668, twice 3 |
| 2222 45 2222 or 2222 4525 2222 | 16,087 | once 14,042, twice 1,955, three times 81, four times 9 |

R = 2,135,555 reads (25)⁶ E (25)³³ E (25)³⁰⁷, then leaves. R = 993,136 reads 2¹¹ 45 2¹⁰ 45 2⁸ 45 2¹² 45 2⁹ 45, then enters the gate's gaps. So the bridges are not artefacts of free inputs, which answers half of GPT's question: a bridge has a real realisation, at least finitely often. Whether any real row crosses infinitely often is the open part. These early crossings sit in finite histories, so they do not by themselves show that E stays on a bi-infinite path at larger W.

**Y's lineage does not die by W = 60,** the program's width limit. It stays one UNRESOLVED component with gaps [2,4,5] at 5,458,619 windows, growing only about 1.11 a column. A second UNRESOLVED child appeared at W = 47 and became LOCKED at W = 54, with gcd 79, then vanished at 55. The 16-gap count fell from 85 to 69 at W = 47 and stays 69 through 60. Longer words still move: chained pairs 45 2ⁿ 45 2ᵐ 45 fell from 34 of 64 at W = 39 to 25 at W = 60, with the n tested changing at W = 47, while the minimal automaton grows to 6,696 states. So a plateau at length 16 does not show a settled language.

## Predictions from L1568 and the prereg

| # | Prediction | Result |
|---|---|---|
| B1 (0.7) | X's recurrent blocks at W = 38 are 25 and E only | **HELD** |
| B2 (0.65) | Y's are 2, 45, 4525 only, at least three 2s between excursions | **HELD from W = 40; MISSED at W = 39,** where gap 3 remains. My reading "one loop, 2" was wrong: Y has no such loop |
| B3 (0.7) | Least separation does not grow from W = 38 to 41 | **HELD:** 4 for X, 3 for Y. Y's stays 3 through W = 60 |
| B4 (0.55) | Crossings exist; no row crosses more than three times | **Half:** crossings HELD; the bound MISSED (9 rows cross Y's bridges four times) |
| B5 (0.6) | No descendant of Y is UNRESOLVED by W = 56 | **MISSED** |
| B6 (0.7) | Y's 16-gap words below 85 at W = 48 | **HELD:** 69 |

B5's counterfactual occurred: Y's lineage is unresolved at W = 56 with its 16-gap count flat from 48 to 56. I wrote that this would make the obstruction two parts, and it does at these widths, but the longer words above do not support calling Y settled.

## Controls

- The automata's 16-gap words equal the Intel run's word files exactly, at W = 40 and 41, for both X and Y (a different algorithm on a different host).
- At W = 34 their counts by length equal `lift`'s own recursion for both components, through length 16.
- W = 41 gives 21,103,162 windows and W = 42 gives Y 510,780, both as in GC2696.
- The row run reproduced gate 4,057,307, family 107,736, lock-7 29,260, lock-7b 1, none 0.

## Limits

- Automaton states are named by a 128-bit hash of the window set, so a collision is possible in principle; no replay excludes it.
- Separation sets were read to n = 400. The claim that X's n has no upper limit rests on the 25 cycle in the minimal automaton.
- The crossing census counts only the patterns above, only before first entry.
- E and 45 are words in column 1. I have not shown that either is a moving object, so "defect" and "glider" are not claims here.
- Y past W = 41 was lifted alone. By the parent step that is exact for Y's descendants, but no second host has replayed it.
- Nothing here excludes any word class for CQ01. Corollary F needs near-squares anchored at the start, and Theorem A‴ bounds repeats only close to the time they end, so neither reaches these tails as they stand.

## The questions this leaves

1. **X:** can a right half cross E infinitely often? Each periodic cycle word, such as ((25)⁶E)^∞, either dies at a finite depth or is a true periodic right half. A column-word tree can test one cycle at a time without growing the window, though the period here is 152 ticks, beyond PE-1's search as written.
2. **Y:** what generates its run lengths? They look less like a loop with a bridge than like the reading of something deeper.
3. **Both:** which left-side statement rules out a finite left half with free bits in these languages? These are the exact analogues of `Q01Gap`, for two explicit word classes.

**Evidence:** `cited/local/block3-bridges-20261106.tar.gz`, 1,410,257 bytes, SHA256 `ba78c5fa0d097eb77b607d0abbcd87f316855b18eafa7c201a1037d0086b6147`.

**Record searched:** as L1568, plus `record_find` on Corollary F and near-square, `PROOFS.md` §11, the Corollary F addendum in PRIOR-ART, the C.6 glider note, the kit's `PeriodicPoints` entry, and the `rule30-open` catalogue and tree on glider, defect, bridge and excursion. Its ether-defect entries concern defects on the ether tail, a different object, and were read by title only. No source found states these words.

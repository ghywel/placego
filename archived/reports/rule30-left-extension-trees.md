# Legal-past trees of the late-dying short words (L1036)

Local, 27 October 2026. This answers GC1991's request for a local explanation of why `01000101` loses all its pasts
at age 33. It reads only the committed, certified phase-0 list `tests/probes/lexicon/rule30_local_mfw44.txt`. There is
no cellular-automaton evolution, solver run or sampling. The probe is
[`tests/probes/wolfram/left_extension_tree.py`](../tests/probes/wolfram/left_extension_tree.py).

## Method

GC1991's recursion (carried in L1036) gives d(w) = 1 + max(d(0w), d(1w)) for w in L. So d(w) − 1 is the height of the
tree of legal pasts u, those with uw in L. The phase-0 list contains every minimal forbidden word up to length 44:
- its exact language (L590, L623, L640) gives the existence side;
- each listed word has a cake_lpr-verified absence certificate, which gives the exclusion side.

So while |uw| ≤ 44, the list alone decides membership, and the probe asserts that bound.

## Prediction, written before the run

H_train: the deepest pasts of 01000101 are a gap-3 train (1000)^k after a short head, ending on train-exit words.
Counterfactual: the deepest pasts have no common periodic background.

## Result

The tree heights reproduce the record's anchors from the list alone:

| Word | d | Branch count by depth |
|---|---:|---|
| 10001001 | 17 | 1,1,2,1,2,2,2,2,2,2,3,4,2,2,2,2,1 |
| 0010001 | 32 | 1,2,2,2,3,4,3,4,5,6,5,6,7,8,6,8,9,8,7,8,8,6,6,5,3,2,2,2,2,2,2,1 |
| 1000101 | 34 | the row below with one forced 0 in front (GC1991's lemma) |
| 01000101 | 33 | 1,2,2,2,2,3,4,3,4,5,6,4,5,6,5,5,6,7,6,5,5,4,2,3,3,2,2,2,2,2,2,2,1 |

The tree is never wider than 9. Every dead branch, in all four trees, ends on one of twelve certified words.

**H_train holds only for 10001001.** Its deepest past is the gap-3 train (1000)^4, killed by
0100010001000100010001001; this agrees with GC1983.

**It fails for the three late words.** Their deepest past is not periodic. Written as gaps (the runs of 0 between
successive 1s), it is a chain of blocks 4·3^k·1. For 01000101 the gaps read 4,3,1 | 4,3,3,1 | 4,3,1 | 4,3,1, and
the word itself supplies the last block. **All three deaths, at 32, 33 and 34, end at the same head:**

    z = 001000010001        (the gap pair 4,3 after at least two 0s)

z is in L, since it begins the deepest legal past. Both of its one-symbol pasts are certified forbidden
(`1001000010001` and `0001000010001`), so d(z) = 1: z occurs only at age 0. In gap terms, after age 0 a gap pair 4,3
must follow a gap of 1. z is a factor of none of the three words. It is reached only through their forced pasts,
and their deadlines differ by the length of the forced path to z.

## The dead branches of 01000101

The table lists the depth at which each branch ends, then the past u, then the certified words that kill both of
u's one-symbol extensions.

```text
 1: 1|01000101  gaps [1, 3, 1]  killed by ['0101000101', '11']
 2: 10|01000101  gaps [2, 3, 1]  killed by ['010010001', '11']
 5: 10100|01000101  gaps [1, 3, 3, 1]  killed by ['010100010001', '11']
 6: 001000|01000101  gaps [4, 3, 1]  killed by ['0001000010001', '1001000010001']
 6: 100100|01000101  gaps [2, 3, 3, 1]  killed by ['010010001', '11']
 8: 10101000|01000101  gaps [1, 1, 4, 3, 1]  killed by ['0101010000', '11']
 9: 100101000|01000101  gaps [2, 1, 4, 3, 1]  killed by ['0100101', '11']
 9: 101000100|01000101  gaps [1, 3, 3, 3, 1]  killed by ['010100010001', '11']
10: 0010000100|01000101  gaps [4, 3, 3, 1]  killed by ['0001000010001', '1001000010001']
10: 1001000100|01000101  gaps [2, 3, 3, 3, 1]  killed by ['010010001', '11']
11: 10000101000|01000101  gaps [4, 1, 4, 3, 1]  killed by ['010000101000010001', '11']
12: 101000101000|01000101  gaps [1, 3, 1, 4, 3, 1]  killed by ['0101000101', '11']
12: 101010000100|01000101  gaps [1, 1, 4, 3, 3, 1]  killed by ['0101010000', '11']
13: 1001000101000|01000101  gaps [2, 3, 1, 4, 3, 1]  killed by ['010010001', '11']
13: 1001010000100|01000101  gaps [2, 1, 4, 3, 3, 1]  killed by ['0100101', '11']
13: 1010001000100|01000101  gaps [1, 3, 3, 3, 3, 1]  killed by ['010100010001', '11']
15: 100001010000100|01000101  gaps [4, 1, 4, 3, 3, 1]  killed by ['010000101000010001', '11']
16: 1010001000101000|01000101  gaps [1, 3, 3, 1, 4, 3, 1]  killed by ['010100010001', '11']
16: 1010001010000100|01000101  gaps [1, 3, 1, 4, 3, 3, 1]  killed by ['0101000101', '11']
17: 00100001000101000|01000101  gaps [4, 3, 1, 4, 3, 1]  killed by ['0001000010001', '1001000010001']
17: 10010001000101000|01000101  gaps [2, 3, 3, 1, 4, 3, 1]  killed by ['010010001', '11']
17: 10010001010000100|01000101  gaps [2, 3, 1, 4, 3, 3, 1]  killed by ['010010001', '11']
17: 10100010001000100|01000101  gaps [1, 3, 3, 3, 3, 3, 1]  killed by ['010100010001', '11']
18: 100100010001000100|01000101  gaps [2, 3, 3, 3, 3, 3, 1]  killed by ['010010001', '11']
19: 1000100010001000100|01000101  gaps [3, 3, 3, 3, 3, 3, 1]  killed by ['0100010001000100010001000101', '11']
20: 10100010001000101000|01000101  gaps [1, 3, 3, 3, 1, 4, 3, 1]  killed by ['010100010001', '11']
20: 10100010001010000100|01000101  gaps [1, 3, 3, 1, 4, 3, 3, 1]  killed by ['010100010001', '11']
21: 001000010001000101000|01000101  gaps [4, 3, 3, 1, 4, 3, 1]  killed by ['0001000010001', '1001000010001']
21: 001000010001010000100|01000101  gaps [4, 3, 1, 4, 3, 3, 1]  killed by ['0001000010001', '1001000010001']
23: 10101000010001000101000|01000101  gaps [1, 1, 4, 3, 3, 1, 4, 3, 1]  killed by ['0101010000', '11']
24: 100101000010001000101000|01000101  gaps [2, 1, 4, 3, 3, 1, 4, 3, 1]  killed by ['0100101', '11']
24: 101000100010001000101000|01000101  gaps [1, 3, 3, 3, 3, 1, 4, 3, 1]  killed by ['010100010001', '11']
26: 10000101000010001000101000|01000101  gaps [4, 1, 4, 3, 3, 1, 4, 3, 1]  killed by ['010000101000010001', '11']
27: 101000101000010001000101000|01000101  gaps [1, 3, 1, 4, 3, 3, 1, 4, 3, 1]  killed by ['0101000101', '11']
28: 1001000101000010001000101000|01000101  gaps [2, 3, 1, 4, 3, 3, 1, 4, 3, 1]  killed by ['010010001', '11']
31: 1010001000101000010001000101000|01000101  gaps [1, 3, 3, 1, 4, 3, 3, 1, 4, 3, 1]  killed by ['010100010001', '11']
32: 00100001000101000010001000101000|01000101  gaps [4, 3, 1, 4, 3, 3, 1, 4, 3, 1]  killed by ['0001000010001', '1001000010001']
```

## What this does and does not show

- **The mechanism of 33, relative to the certified list.** Every legal past of 01000101 dies on one of 8 certified
  words. The longest pasts run through 4·3^k·1 blocks and reach the age-0-only head z. This is an exact finite
  account. It is not a hand proof of the 8 words' absence, which rests on their certificates.
- **Relocation, GC1991's question.** One obstruction, z, ends three different words' pasts without being a factor
  of any of them. A later death therefore needs a word whose forced past to an age-0-only head is longer. By the
  factor law, wrapping an old word cannot supply that.
- **Scope.** The list decides only while |uw| ≤ 44. The length-20 control (d = 43, so |uw| = 62) is out of reach
  here, and no claim is made about it. The gap and block reading is descriptive: no general block grammar, and no
  bound or growth law for deaths, is claimed.

# Late deaths end on two start-only heads (L1042)

Local, 27 October 2026. This is my own question, continued at the owner's request. Are late deaths long forced
chains of the reset-to-reset map ([L1040](rule30-reset-tracks.md)) that end on a configuration that can occur only
at the start?

The record frames why it matters. By 8.86's death criterion, deaths at arbitrarily late times would refute soficity
of the visible language.

**Evidence and status.**
- *Data:* the committed certified phase-0 list, exact while |uw| ≤ 44, through
  [`late_death_heads.py`](../tests/probes/wolfram/late_death_heads.py).
- *A three-valued exhaustive search:* [`run_of_threes.py`](../tests/probes/wolfram/run_of_threes.py), about three
  minutes.
- *Status:* finite and exact, but single-party. Nothing here is a hand proof except the short arguments marked.

## Prediction, written before the run

H1: every decidable late death (d ≥ 17) among L-words of length 6 to 12 ends its deepest past on at most 3 terminal
heads, z among them.

H2: in gap form, the deepest pasts are made of blocks (4,3^k,1) and runs of 3-gaps.

Counterfactual: more than 5 heads, or no block structure.

## Result

**Scope.**
- 70 words of length 6 to 12 have a decidable late death (d from 17 to 34).
- 272 words have pasts that run past the certified length 44: survivors, or later deaths. They are not covered, and
  neither is the length-20 control (d = 43).

**H1 holds, in its strongest form: exactly two heads.**

| Terminal head | Gaps | Deepest pasts ending there | Families |
|---|---|---:|---|
| z = 001000010001 | (4,3) after at least two 0s | 65 | the 32/33/34 words and their extensions |
| h2 = 100010001000100010001001 | (3,3,3,3,3,2) | 5 | the d = 17 family of 10001001 |

**H2 holds.**
- The z family's deepest pasts read 4,3,1 | 4,3,3,1 | 4,3,1 | 4,3,1 ….
- The h2 family's are 3-runs: for 10001001, the past is (1000)^4.

## Why each head can occur only at age 0

A visible 1 at age ≥ 1 is made by a reset (GC1992). So any gap word that follows a 1 at age ≥ 1 must lie in Λ, the
post-reset gap language of L1040.

- **h2.** After a reset, five 3-gaps are followed only by 1, 3 or 4. Six are followed only by 4, so seven never occur.
  This comes from an exact depth-first search over tails, `run_of_threes.py`.

  Hence (3,3,3,3,3,2) is not in Λ. If h2 began at age j ≥ 1, its first 1 would be reset-made, which is impossible. So
  h2 occurs only with its first 1 at age 0, the initial cell, which no reset made. The certified killers agree exactly:
  - 0100010001000100010001001 is (3^5,2);
  - 0100010001000100010001000101 is (3^6,1);
  - 010001000100010001000100010001 is (3^7).
- **z.** If z = 00·1 0000 1 000 1 occurs at age j ≥ 1, there are two cases:
  - an earlier 1 exists, and then the gap word (g,4,3) with g ≥ 2 must be in Λ. It is not: (2,4,3), (3,4,3) and
    (4,4,3) are minimal forbidden words of Λ (L1041);
  - there is no earlier 1, and then the pre-reset row must begin 0110. Lemma A excludes that after time 0 (L1037 and
    GC1996, computer-assisted).

**So both heads are pinned to age 0 by the same principle.** Their first post-initial 1s would have to follow a gap
pattern that no reset can produce.

## The mechanism of a late death, in one paragraph

For w ∈ L with finite d, a legal word uw with |u| = d − 1 exists, and every longer past dies. Here, within the
decidable range, every deepest uw starts with z or h2. Read forward, w occurs late only as the far end of a long legal
continuation of one of two start-only heads. It cannot occur late in any history that has forgotten its start. The
death time is the length of the longest such continuation:
- 34 for the z family's best word;
- 17 for the h2 family's.

**Why the chains are long.** The (4,3^k,1) blocks keep the history inside the reset tracks, and the tails carry the
memory of the head forward. **Why they end.** No block chain can be extended past the head: going backward, every
branch reaches a Λ-forbidden gap word or the head.

## What this does not show, and the next question

- No general statement about words beyond the certified range, or about lengths above 12.
- No bound on deaths: a family with unbounded d would refute soficity (8.86), and none is exhibited.
- Not every start-only word is a terminal head. The certified list implies many start-only words; only these two end
  late deaths in this range.

**The next question: are there heads whose legal continuations are unboundedly long and still distinguishable?**
- That would be words that occur ever later but only after a fixed start-only head.
- The 3-run counter is bounded at six, and z's block chains reached 34. A longer death needs a head whose memory
  survives longer in the tails.
- The track lemma says where that memory lives: in the four tail bits each reset reads, refreshed from the light cone.

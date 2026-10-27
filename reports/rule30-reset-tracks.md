# The reset tracks: what happens beside the wall between two visible 1s (L1040)

Local, 27 October 2026. This is my own question, at the owner's request. Every visible 1 after age 0 comes from a
reset: a row beginning 000 (GC1992). What happens between one reset and the next?

**Conventions.** These are the record's:
- a *row* is cells 1, 2, … at an even time, beside the wall x(t,0) = t mod 2;
- two(X) is the row two updates later;
- a reset row is written 000abcd…, and a, b, c, d are its *tail bits*;
- gaps count the zeros between successive visible 1s.

**Status.**
- Sections 1 and 2 are hand proofs: PROOF-SKETCH, single-party, awaiting GPT's read.
- Section 3 is a measurement, with its prediction written first.
- Every statement is also checked exhaustively by
  [`tests/probes/wolfram/reset_tracks.py`](../tests/probes/wolfram/reset_tracks.py): finite truth tables, no
  solver.
- Record search: "latch", "next gap", "reset row", and the renewal and gap-block entries (GC502/503/504, G.GPT239,
  G.GPT250). The pair restrictions in section 2 are known from the record. The four-bit gap function and the
  tracks, I could not find stated. No novelty is claimed.

## 1. The track lemma

**Lemma (tracks).** After a reset row 000abcd…, the next gap is decided by a, b, c, d alone. The rows before the next
reset begin with a fixed track:

| Tail bits a b c d | Next gap | First cells of the rows until the next reset |
|---|---:|---|
| 0 0 and (c OR d) = 1 | 1 | 100 → 000 |
| 1 1 and (c OR d) = 1 | 2 | 111 → 010 → 000 |
| 0 1 * *, or 0 0 0 0 | 3 | 10b → 001 → 010 → 000 |
| 1 0 * *, or 1 1 0 0 | 4 | 111 → 011 → 001 → 010 → 000 |

So every gap is 1 to 4. The row just before every reset that follows a reset begins **100 or 010, never 01100**.

**Proof.** Let y be the odd-time row after R = 000abcd…. Then y = (0, 0, a, a OR b, a XOR (b OR c), …), and
P1 = two(R) begins

    1,  a,  a OR b,  NOT a AND (b OR c),  (a OR b) XOR (y5 OR y6).

By Lemma B (L1037), the next row begins 000 iff the current one begins 010, 01100, or 100 with (x4, x5) ≠ 00.

- **Gap 1** means P1 begins 100 with (P1_4, P1_5) ≠ 00. That is a = b = 0, which makes P1_4 = c and P1_5 = c OR d.
  So gap 1 ⇔ a = b = 0 and (c OR d) = 1.
- **When P1_1 = 1** (always), P2 is not a reset row. Two one-row identities give P2's first cells:
  - for X beginning 1, the next row begins 0, NOT(y2 OR y3), …;
  - for X beginning 0, the next row's second cell is NOT x2 AND (x3 OR x4).
- **a = 1.** P1 = 1 1 1 0 p5 …, so P2 = 0 1 (NOT p5) 1 ….
  - P2 is pre-reset iff it begins 010, iff p5 = 1. (01100 is impossible, since P2_4 = 1.)
  - p5 = NOT(y5 OR y6), with y5 = NOT(b OR c) and y6 = b XOR (c OR d). This is c OR d when b = 1, and 0 when b = 0.
  - So gap 2 ⇔ a = b = 1 and (c OR d) = 1, with track 111 → 010.
  - Otherwise p5 = 0, and P2 begins 0111. Its successor begins 001, and the row after that begins 010, a pre-reset
    row; the identity is the one used in L1038. This is gap 4, with track 111 → 011 → 001 → 010.
- **a = 0, not gap 1.** Then b = 1, or a = b = c = d = 0.
  - P1 = 1 0 b (b OR c) ….
  - P2's second cell is NOT(y2 OR y3) = NOT(NOT b OR (b OR c)) = 0. Its third cell is 1 in both sub-cases, so P2
    begins 001 and is neither a reset nor a pre-reset row.
  - Its successor begins 010, a pre-reset row (the 001 → 010 identity of L1038). This is gap 3. ∎

## 2. Corollary: which gap pairs can follow a reset

**After a gap of 1 the next gap is never 2.** Gap 2 would need c = 0 (from below), and so d = 1. But then the next
reset row's second tail bit is 0.

*Detail.* P1 = 1 0 0 c (c OR d) …. Its successor R2 has first tail bit NOT c, and its second tail bit is
NOT(y5 OR y6) with y5 = 1, so it is 0. Gap 2 needs tail bits 11.

**After a gap of 2 the next gap is 2 or 4.**
- The pre-reset row is 0 1 0 1 …: its fourth cell is the fourth cell of P2 = 0 1 0 1 above.
- For a pre-reset row 010x…, the next reset's first tail bit is x OR NOT(x5 OR x6), here x = 1 (Lemma E's formula).
  So that bit is 1.
- By the track lemma, a first tail bit of 1 means gap 2 or gap 4.

**Check.** Exhaustively, every other ordered pair occurs. So the pairs impossible right after a reset are exactly
(1,2), (2,1) and (2,3). This matches the record:
- the no-(1,2) proof of GC503/504;
- the certified words 0100101 and 010010001, which say "(2,1) and (2,3) cannot be preceded".

Here they follow uniformly from the tracks. That is a reproof of known facts (PRIOR-ART), not a new result.

## 3. How far ahead the tail is read (a measurement)

Let D(k) be the least L such that the first L tail bits of any reset row decide its next k gaps. The prediction,
written first, was **D(k) = 4k**: each gap reads four fresh bits.

| k | D(k) | Distinct k-gap sequences after a reset |
|---:|---:|---:|
| 1 | 4 | 4 |
| 2 | 14 | 13 |
| 3 | 20 | 33 |
| 4 | 28 | 77 |

These are exact. They come from a depth-first search over tail bits, with each leaf decided by three-valued simulation, run once (k ≤ 4, a few minutes). The committed probe covers sections 1 and 2 only.

**The prediction is refuted at k = 2.**
- The first gap reads only four bits.
- The next reset's four deciding bits depend on the first reset's tail bits 3…7, 3…10, 2…12 and 2…14 for gaps 1, 2,
  3 and 4. That is up to the light-cone edge 4 + 2(g+1).
- So shielding holds for one gap only. Later gaps read as far right as causality allows, at least in the worst case.

The sequence counts grow by ratios 3.25, 2.54 and 2.33. This is a raw count of post-reset gap words, not the
record's entropy ceiling, and no rate is claimed.

## What this changes, and the next questions

- **A general reading of the z mechanism (L1037, GC1996).** After any reset, the row before the next 1 begins 100 or
  010. A pre-reset row 01100 therefore occurs only before the first visible 1 at age ≥ 1. With Lemma A, a row 0110
  occurs only at time 0. A *transient-only* configuration is one that cannot recur once the track regime has
  started. z is such a configuration, seen through its forced future.
- **The open question I would take next.** The track lemma makes the visible process a *reset-to-reset map* on tails:
  the gap is N(first four bits), then the tail is updated by a light-cone map. Late deaths, such as 32 to 34 via z
  or 43 for the length-20 control, are long forced chains of this map that end on a transient-only configuration.
  Can the forced chains be described by the gap pairs and triples that cannot follow a reset (section 2, and the 31
  impossible triples found here)? That would give the delayed-obstruction family GC1991 asked for. Not attempted
  here.

# Theorem A′ (a block recurs only if it is no longer than the edge is far)

*Windows, zero runs and the left band. Derived from [PROOFS.md](../PROOFS.md), entry "7. Theorem A′ (a block recurs
only if it is no longer than the edge is far)"; rebuild with `python3 proofs/build.py`. Edit the proof in PROOFS.md
and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved.

## In plain words

A pattern can only repeat if it is shorter than the distance to the edge.

**What it says.** If two neighbouring columns show the same block of n values twice, at times a and a′, then n is at
most the edge's distance at the later time, L + a′. The reason: a block of n values is a fingerprint of the n − 1
squares beside the columns, so seeing it twice means that stretch of the row looked the same both times. But the
seed's edge moves outward one square per tick, so the later row has a black square out where the earlier row was
white, and a block long enough to reach it would see the difference.

**Why it matters.** Repeats are the raw material of periodicity, and this caps them using only the seed's size. It
depends on the room growing (the owner's point): in a closed box, such as Rule 30 on a ring, every pattern must
eventually come back and then repeat for ever (C6), like light between perfect mirrors. A finite seed escapes that
only because the region it disturbs keeps widening. How fast the room grows matters too (the owner's follow-up).
Rule 30's edges move out one square per tick, the fastest anything can travel. News from the edge therefore always
arrives, but ever later, while news from the centre heading left, at about a quarter of that speed (C4), never
catches the edge.

**An everyday picture.** Two photographs of a growing town, taken years apart, can match only through a frame too
narrow to include the new outskirts.

## The formal statement and proof

*Where:* RULE30-PRIZE.md, "8.58 The window principle: Theorem A′, and what the Collatz twin shows is missing (2026-10-05)". *Bears on:* the window principle: a block recurs only if it is no longer than the edge is far. *Status:* proved.

**Theorem A′ (a block recurs only if it is no longer than the edge is far).** Take a nonzero configuration whose
leftmost black cell at time 0 is $L \ge 0$ cells to the left of column $i$. If the pair of columns $(i, i+1)$
shows the same block of $n$ consecutive values starting at times $a$ and $a' > a$, then

```math
n \le L + a' .
```

*Proof.* Rule 30 read from right to left gives each cell from the cell to its right one step later and two cells
of its own time. So the two columns at times $t$ to $t + k$ fix the $k$ cells to their left at time $t$. Equal
blocks of length $n$ therefore make the rows at times $a$ and $a'$ agree at the $n - 1$ cells left of column
$i$. The later row has its leftmost black cell $L + a'$ cells out, and the earlier row is white there. If
$L + a' \le n - 1$ the rows disagree inside the range where they must agree. $\square$

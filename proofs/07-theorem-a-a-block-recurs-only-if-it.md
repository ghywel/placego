# Theorem A′ (a block recurs only if it is no longer than the edge is far)

*Windows, zero runs and the left band. Derived from [PROOFS.md](../PROOFS.md), entry "7. Theorem A′ (a block recurs
only if it is no longer than the edge is far)"; rebuild with `python3 proofs/build.py`. Edit the proof in PROOFS.md
and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved.

## In plain words

A pattern can only repeat if it is shorter than the distance to the edge.

**What it says.** If two neighbouring columns show the same block of n values twice, at times a and a′, then n is at
most the edge's distance plus a′.

**Why it matters.** Repeats are the raw material of periodicity. This caps how long any repeat can be, using only
how far away the seed's edge is.

**An everyday picture.** An echo can only repeat what has had time to travel back from the wall.

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

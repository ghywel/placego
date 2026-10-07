# The shrink theorem for white triangles

*Short proofs restated from the running text. Derived from [PROOFS.md](../PROOFS.md), entry "C.3 The shrink theorem
for white triangles (RULE30-PRIZE.md §8.18; 2026-10-05)"; rebuild with `python3 proofs/build.py`. Edit the proof in
PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved.

## In plain words

A run of white squares shrinks by exactly one square at each end per tick, so Rule 30's white triangles are perfect.

**What it says.** A run of two or more white squares with black on both sides becomes, one tick later, the same run
with one square trimmed from each end. So every white triangle in Rule 30 is an exact isosceles triangle (its two
sloping sides equal), fixed by the row, place and width where it is born.

**Why it matters.** The white triangles are the most visible structure in Rule 30, and this makes them exactly
predictable once born. The gaps in the record's "ladder", its measurements of the longest white run the left half
can be held to, are the bases of such triangles. It was also checked on a million runs; Rule 110, a neighbouring
rule of the same kind, breaks it.

**An everyday picture.** The triangles on the shell of the *Conus textile* snail; or a sheet of ice melting evenly
in from both edges.

## The formal statement and proof

*Where:* §8.18; checked on 1,005,083 runs by `rule30_triangles.py` (0 exceptions; Rule 110 breaks it). *Bears on:* the
triangle census (§8.68); the zero runs of the ladder are the bases of such triangles. *Status:* proved.

**Theorem.** In Rule 30 a maximal run of $n \ge 2$ white cells $[a, b]$, bounded by black cells, becomes exactly the run
$[a + 1, b - 1]$ one step later. So every white triangle is an exact isosceles triangle, fixed by its birth row,
column and width.

*Proof.* $x'(a) = x(a-1) \oplus (x(a) \vee x(a+1)) = 1 \oplus (0 \vee 0) = 1$ since $x(a-1) = 1$ and $n \ge 2$;
$x'(b) = x(b-1) \oplus (x(b) \vee x(b+1)) = 0 \oplus (0 \vee 1) = 1$; every cell strictly inside has three white
parents and $000 \to 0$; and $x'(a+1), \ldots, x'(b-1)$ are bounded by the two black cells just produced. $\square$

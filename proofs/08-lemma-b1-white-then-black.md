# Lemma B1 (white, then black)

*Windows, zero runs and the left band. Derived from [PROOFS.md](../PROOFS.md), entry "8. Lemma B1 (white, then
black)"; rebuild with `python3 proofs/build.py`. Edit the proof in PROOFS.md and this summary in
[summaries.md](summaries.md), never this file.*

**Status:** proved.

## In plain words

In the band near the edge, two neighbouring diagonals can never both fall silent for ever.

**What it says.** Near the left edge the pattern runs along diagonals, and the outermost diagonal, the edge itself,
is black at every tick. If one diagonal turns white for ever, the one two steps further in becomes a latch (C2):
once lit it stays lit, so it ends up black for ever. And two neighbouring diagonals cannot both be white for ever:
their darkness would pass back, diagonal by diagonal, all the way to the edge, which is never dark.

**Why it matters.** It gives the edge band a rigid structure, which later results use to find black squares where a
counterexample would need white ones. The proof separates a lamp switched off locally, which is allowed, from a
power cut, which would have to reach back to the supply (the owner's distinction).

**An everyday picture.** Lamps fed in a chain from a power station that never fails: any single lamp can be switched
off, but two neighbours dark for good would mean the power had failed all the way back to the station, and it never
does.

## The formal statement and proof

*Where:* RULE30-PRIZE.md, "8.59 The window principle meets the band of stripes: a repeat is a white run, and the left side is never white for long (2026-10-05)". *Bears on:* the left band: an eventually white diagonal is preceded by an eventually black one. *Status:* proved.

**Lemma B1 (white, then black).** If diagonal $j$ is eventually white, diagonal $j + 2$ is eventually black. No two
adjacent diagonals are both eventually white. A diagonal other than 0 and 1 is eventually black only if the one two
before it is eventually white.

*Proof.* Once $D_j \equiv 0$, $D_{j+2}(t+1) = D_{j+1}(t) \lor D_{j+2}(t)$, which never falls, so $D_{j+2}$ is eventually
constant, and it is 1 unless $D_{j+1} \equiv D_{j+2} \equiv 0$ as well. If $D_j \equiv D_{j+1} \equiv 0$ then
$D_{j+1}(t+1) = D_{j-1}(t) \oplus (D_j \lor D_{j+1}) = D_{j-1}(t)$ forces $D_{j-1} \equiv 0$, and so on down to
$D_0 \equiv 0$, which is false ($D_0 \equiv 1$). That proves the first two claims. For the third: if $D_k \equiv 1$
then $D_k(t+1) = D_{k-2}(t) \oplus 1$ forces $D_{k-2} \equiv 0$. $\square$

*Machine-checked (Local, 2026-10-10 04:45 BST).* tests/probes/lean/LemmaB1.lean (Lean 4, Mathlib). It holds for any
configuration with a leftmost black cell e. Diagonal j at time t is the cell e - t + j.
- `no_adjacent_white` is part (1), for j >= 0.
- `white_then_black` is part (2), for j >= 0.
- `black_needs_white` is part (3).
- The tools are the diagonal recurrence (`D_succ`), the edge's D_0 = 1 (`D0`), and descent through adjacent white
  pairs (`down`).
- The axioms are propext and Quot.sound, plus Classical.choice in part (2).

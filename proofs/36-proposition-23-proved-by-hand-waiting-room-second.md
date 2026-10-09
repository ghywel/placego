# Proposition 23 (proved by hand; waiting room, second reader wanted): the triangles on the single cell's right edge are a ruler sequence

*Siblings, Jen and the squeeze. Derived from [PROOFS.md](../PROOFS.md), entry "36. Proposition 23 (proved by hand;
waiting room, second reader wanted): the triangles on the single cell's right edge are a ruler sequence"; rebuild
with `python3 proofs/build.py`. Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never
this file.*

**Status:** waiting room, second reader wanted.

## In plain words

At every second step a white triangle touches Rule 30's right edge, and its size depends only on how many times 2 divides the step number.

**What it says.** The owner noticed that the triangles along the right edge start at evenly spaced points and differ only in size. The proof reads the edge's diagonals, each of which repeats with a period that is a power of two. At an even step, the diagonals whose period divides the step are white, as at the start. The first one whose period does not divide it has just been flipped to black. So the triangle's width is fixed by the highest power of 2 dividing the step: 2, 3, 5, 6, 8, 14, 15, 23, and so on.

**Why it matters.** It is exact order inside the side of the pattern that looks chaotic: a ruler sequence, nested like the supertiles of a hierarchical tiling. It explains why the widest triangles of the whole pattern sit on the edge at steps like 32,768 and 65,536. Cloud proved it by hand; it waits for a second reader.

## The formal statement and proof

*Status:* waiting room, second reader wanted. Not a prize claim. Not found in the record or in a short search; the
periods it uses are Rowland's and OEIS A094605, and the widest edge triangles were seen in §8.68.
*Provenance:* Cloud, 2026-10-09 (08:43 BST), from the owner's observation that the rightmost triangles touch the
pyramid's right edge at linearly spaced points and differ only in size. Checked by the exploratory probe
`tests/probes/lexicon/rule30_cloud_edge_triangles.py` (no prediction pushed first).

In the single cell's history let $D_j(t) = x_t(t - j)$ be the $j$-th right diagonal, so $D_0$ is the edge. By §8.27,
every $D_j$ is purely periodic, with a period $p_j$ that is a power of 2 ($p_0 = 1$): $D_j$ is the running XOR of
$g_j = D_{j-1} \lor D_{j-2}$ from $D_j(0) = 0$, and if $q_j$ is the period of $g_j$ then $p_j = q_j$ when one period
of $g_j$ holds an even number of 1s and $p_j = 2q_j$ when it holds an odd number. The periods are OEIS A094605:
$1, 2, 2, 4, 8, 8, 16, 32, 32, 64, \dots$

**Proposition 23.** For $t \ge 1$ let $L(t)$ be the number of white cells at time $t$ that run leftwards from
cell $t - 1$, just inside the black edge cell $t$. Then
```math
L(t) = \min\{\, j \ge 1 : p_j \nmid t \,\} - 1 .
```
So $L(t) = 0$ for odd $t$, and for $t = 2^v m$ with $m$ odd, $L(t) = w(v) = \min\{j \ge 1 : p_j > 2^v\} - 1$,
which depends only on $v$. At every even $t$ this run is the top row of a white triangle, one cell inside the edge.
So one triangle touches the right edge every two steps, and its width is a ruler sequence:
$w = 2, 3, 5, 6, 8, 14, 15, 23, 24, 26, 28, \dots$ for $v = 1, 2, 3, \dots$

**Proof.** Let $j$ be the least index $\ge 1$ with $p_j \nmid t$; it exists because the periods are unbounded
(§8.27). For $1 \le i < j$, $p_i \mid t$, so $D_i(t) = D_i(0) = 0$: cells $t - 1, \dots, t - j + 1$ are white. Now
$q_j$ divides the least common multiple of the periods of $D_{j-1}$ and $D_{j-2}$ (the white side $D_{-1}$ has
period 1), and both divide $t$, so $q_j \mid t$. As $p_j \nmid t$, $p_j \ne q_j$, so $p_j = 2q_j$, one period of
$g_j$ holds an odd number of 1s, and $D_j(s + q_j) = D_j(s) \oplus 1$ for every $s$. Since $q_j \mid t$ and
$2q_j \nmid t$, $t \equiv q_j \pmod{2q_j}$, so $D_j(t) = D_j(q_j) = D_j(0) \oplus 1 = 1$: cell $t - j$ is black.
Hence $L(t) = j - 1$. Each $p_i$ is a power of 2, so $p_i \mid t$ exactly when $p_i \le 2^v$, which gives the form
in $v$. For odd $t$, $p_1 = 2 \nmid t$, so $L(t) = 0$. For even $t$, $p_1 = p_2 = 2$ divide $t$, so $L(t) \ge 2$. The
run is a triangle's top row: the row above, $t - 1$, is black at cell $t - 2$ ($D_1(t-1) = 1$), so the run is not
the shrunken continuation of a white run above it. ∎

*Remarks.* The widest triangles of the whole cone sit on the edge at the times $m \cdot 2^k$ (§8.68); this is why,
and their width is $w(v_2(t))$ exactly. The layers $[L(t) \ge k]$ are periodic with doubling periods, the nesting of
a hierarchical tiling (§8.72). *Computer check:* for every even $t < 2^{24}$ the width depends only on $v_2(t)$ and
equals the formula wherever the periods are known ($v \le 21$); a direct simulation agrees at every $t < 4096$.

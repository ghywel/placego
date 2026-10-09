# Proposition 22 (proved by hand, second-read): a row that turns faster than light is periodic, and every window turns leftwards

*Siblings, Jen and the squeeze. Derived from [PROOFS.md](../PROOFS.md), entry "35. Proposition 22 (proved by hand,
second-read): a row that turns faster than light is periodic, and every window turns leftwards"; rebuild with
`python3 proofs/build.py`. Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this
file.*

**Status:** second-read by Local (L375, 2026-10-09); promoted from the waiting room by Local (L375).

## In plain words

A Rule 30 row whose pattern slides faster than light is always a repeating ring. If it slides left, every short stretch of cells is the start of exactly one such row.

**What it says.** Some rows just slide: one step of the rule, or a few, gives the same row moved over. If the slide is faster than one cell per step, the rule cannot have made the row from its neighbours alone, so each cell is forced by a fixed stretch of cells beside it. That pins the row down and makes it repeat. Sliding left, Rule 30's exact passing-on of its left neighbour means nothing is lost, so every stretch of |s| + p cells grows into one sliding row. Sliding right, information is lost through the OR, and such rows are rare.

**Why it matters.** GPT's all-S ring is one of these rows: it turns 14 cells each step. A census of every sliding row up to 28-cell stretches finds it is the only one with a period-two column at all, so sliding rows give no new mixed S/L witnesses. Cloud proved it by hand; it waits for a second reader.

## The formal statement and proof

*Status:* second-read by Local (L375, 2026-10-09); promoted from the waiting room by Local (L375). Waiting-room heading: "35. Proposition 22 (proved by hand; waiting room, second reader wanted): a row that turns faster than light is periodic, and every window turns leftwards". Elementary; Boyle and Lee (arXiv:math/0607178, Remark 2.1) describe
the same kind of count for permutive directions, so it is not claimed new. Not a prize claim.
*Provenance:* Cloud, 2026-10-09 (08:12 BST), from the owner's questions after CL071 (which surfaces carry a ring's
history; "a unit vector in a space-time picture is a velocity"). Part (b) was noticed in a disclosed smoke test of
`tests/probes/lexicon/rule30_cloud_turning_rings.py` before it was proved, and checked in the full run, whose
predictions were pushed in dedbe55.

Write $F$ for Rule 30, $F(x)(i) = x(i-1) \oplus (x(i) \lor x(i+1))$, and $\sigma$ for the shift,
$(\sigma^s x)(i) = x(i - s)$, so $s > 0$ moves a pattern right. Call $x \in \{0,1\}^{\mathbb{Z}}$ a *turning row*
with vector $(s, p)$ if $F^p x = \sigma^s x$: its space-time is constant along $(s, p)$.

**Proposition 22.** Let $p \ge 1$ and $|s| > p$.
(a) Every turning row with vector $(s, p)$ is spatially periodic, and there are finitely many. They are exactly the
periodic points of a map $T$ on the $2^{|s| + p}$ words of $|s| + p$ cells, and the least period of the row is the
length of its window's cycle.
(b) If $s < -p$, $T$ is a bijection, so there are exactly $2^{|s| + p}$ turning rows with vector $(s, p)$: every
word of $|s| + p$ cells extends to exactly one row that moves left $|s|$ cells every $p$ steps.

**Proof.** (a) $F^p(x)(i)$ depends only on $x(i-p), \dots, x(i+p)$; write it $G(x(i-p), \dots, x(i+p))$. Suppose
$s > p$. The relation says $x(i - s) = G(x(i-p), \dots, x(i+p))$, and the cell $i - s$ lies outside that window.
Putting $m = i - s$, $x(m) = G(x(m+s-p), \dots, x(m+s+p))$. So the window $W_m = x(m+1), \dots, x(m+s+p)$ fixes
$x(m)$, hence $W_{m-1} = T(W_m)$ for a map $T$ on words of $s + p$ cells. For every $j \ge 0$, $W_m = T^j(W_{m+j})$
lies in the image of $T^j$. On a finite set these images decrease to the set of periodic points of $T$, on which $T$
is a bijection. So every $W_m$ is $T$-periodic, $(W_m)$ is periodic in $m$, and so is $x$, with least period the
length of $W_0$'s cycle (each window fixes the row). Conversely, a $T$-cycle read off cell by cell gives a row
satisfying the relation at every site. If $s < -p$ the same argument runs rightwards, with $x(n)$ fixed by the
$|s| + p$ cells to its left.
(b) Rule 30 is left-permutive, and so is $F^p$: $F^p(x)(i) = x(i-p) \oplus H(x(i-p+1), \dots, x(i+p))$. Put
$j = -s > p$. Moving right, $T$ drops the window's leftmost cell $x(n-j-p)$ and appends
$x(n) = x(n-j-p) \oplus H(x(n-j-p+1), \dots, x(n-j+p))$. Every argument of $H$ is still in the new window, because
$n - j + p \le n - 1$. So the dropped cell is recovered from the new window, $T$ is injective, and on a finite set it
is a bijection. Every word is periodic, and (a) gives the count. ∎

*Remarks.* Part (a) uses only that the rule has radius one. For $s > p$, $T$ drops the rightmost cell, which Rule 30
reads through the OR, and $T$ is not injective: the census finds such rows about as rare as a random map's cycles
(from 4 times more at $p = 1$ to as many at $p = 3$). GC686's all-S ring (CL071: $F x = \sigma^{14} x$ on its own ring
of 84 cells, which is also $\sigma^{-70}$) is a turning row of both kinds.
*Computer check* (`rule30_cloud_turning_rings.py`, `turning_rings.c`). For $p \le 3$ and $|s| + p \le 28$, every
row found satisfies its relation directly. On every ring of period up to 20 the census agrees with brute force over
all rings. For every $s < -p$ all $2^{|s|+p}$ words are periodic.
*Corollary, by composition with GPT's results (conditional on GC687's exhaustive certificate).* A turning row with
$s \ne 0$ whose columns 0 and 1 are the all-S pair (the wall $0101\ldots$ and $110100$ repeated, in marker form) is
a rotation of GC686's ring. Reason: columns 0 and 1 have period 6, so every column to the left does (GC704's
propagation); column $i + s$ is column $i$ delayed by $p$ steps, so every column has period 6. GC688 then fixes the
entrance, GC687 the right half and L372's decoding the left half. The census agrees: in its whole range the only
turning row with an alternating column at all is GC686's ring.

*Independent reading (Local L375, 2026-10-09).* Verified by hand. (a) With $m = i - s$ and $s > p$, the window $x(m+s-p), \dots, x(m+s+p)$ lies inside $W_m = x(m+1), \dots, x(m+s+p)$ because $s - p \ge 1$, so $W_{m-1} = T(W_m)$; $W_m$ lies in every image $T^j$, hence among $T$'s periodic points, where $T$ is a bijection, so the windows cycle both ways and the row is periodic with least period the cycle length. (b) $F^p$ stays left-permutive under composition, and with $j = -s > p$ the arguments of $H$ end at $n - j + p \le n - 1$, inside the new window, so the dropped cell is recovered and $T$ is injective. The corollary's step "column $i + s$ is column $i$ delayed by $p$" reads $x_{t+p}(i) = x_t(i - s)$ correctly, and it carries period 6 from the left columns to every column. Near-entry check first (`proof_dupes.py --near 35`): entries 25, 05 and 07, a pulse-weight proposition and Theorems A and A′; none is restated. The census and GC687 were not replayed here.


*Correction to the corollary's wording (Cloud, 2026-10-09, at GPT's request in GC725).* The corollary assumes
$|s| > p$ as well as $s \ne 0$: its reason uses part (a)'s spatial period. GPT's GC727 (hand proof, read by Cloud in
CL073) extends part (a) to every $s \ne p$: for $s < p$, $x(m) = x(m + p - s) \oplus H(x(m+1), \dots, x(m+2p))$
fixes each cell from cells strictly to its right. With it, the corollary holds for every direction except
$s = p$.

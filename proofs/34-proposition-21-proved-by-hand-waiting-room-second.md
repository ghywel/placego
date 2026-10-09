# Proposition 21 (proved by hand; waiting room, second reader wanted): a seed sharing the single cell's centre column begins its left half exactly where its right half alone fails

*The waiting room (not yet verified). Derived from [PROOFS.md](../PROOFS.md), entry "34. Proposition 21 (proved by
hand; waiting room, second reader wanted): a seed sharing the single cell's centre column begins its left half
exactly where its right half alone fails"; rebuild with `python3 proofs/build.py`. Edit the proof in PROOFS.md and
this summary in [summaries.md](summaries.md), never this file.*

**Status:** in the waiting room: stated with a proof, not yet checked by a second reader.

## In plain words

A finite seed that shares the single cell's centre column must start its left half exactly where its right half, on its own, would first break that column.

**What it says.** Rule 30 pushes any difference on the left rightward at exactly one cell per step. So a black cell added deep on the left reaches the centre at a time equal to its depth, and changes the column there. A left half can only help if it arrives at the very moment the right half would go wrong. With a white or a fringe right half nothing ever goes wrong, so the left half must be white.

**Why it matters.** It turns the open half of Proposition 20 into two finite searches. Run them up to right halves of 28 cells, and left halves 500 deep, and they find nothing outside the fringe family. Whether the family is complete for all sizes is still open. Cloud proved it by hand; it waits for a second reader.

## The formal statement and proof

*Provenance:* Cloud, 2026-10-09 (05:48 BST), pushing on Proposition 20's open converse at the owner's request.
Stated as Lemma U1 in `tests/probes/lexicon/rule30_cloud_fringe_uniqueness.py`, whose predictions were pushed in
8327e7c before its full run, and checked there on every right half of up to 16 cells.

**Proposition 21.** For a right half $R = x_0(1..w)$ let $\tau(R)$ be the first time the centre column of
$(\text{white}, 1, R)$ differs from the single cell's, with $\tau(R) = \infty$ if it never does. Let $X = (L, 1, R)$
be a finite seed whose centre column is the single cell's. Then either $L$ is white and $\tau(R) = \infty$, or the
shallowest black of $L$ is at depth exactly $\tau(R) < \infty$. In particular, (a) the single cell is the only
finite seed with a white right half and this column, and (b) a seed with this column whose right half is a fringe
$S_r$ (Proposition 20) has a white left half.

**Proof.** Put $Y = (\text{white}, 1, R)$. If $L$ is white then $X = Y$, and $\tau(R) = \infty$. Otherwise let $b$
be the depth of the shallowest black of $L$. The rows $X$ and $Y$ differ only at cells $\le -b$, and the rightmost
difference is at $-b$. Rule 30 is left-permutive: if two rows agree at every cell $> i$ and differ at $i$, the next
rows agree at every cell $> i + 1$ and differ at $i + 1$, because $x'(i+1) = x(i) \oplus (x(i+1) \lor x(i+2))$ and
the inputs of the OR agree. So at time $t$ the rightmost difference is exactly at $-b + t$, and the centre columns
of $X$ and $Y$ agree for $t < b$ and differ at $t = b$. As $X$ has the single cell's column, $Y$'s column agrees with
it before $b$ and differs at $b$, so $\tau(R) = b$. For (a), $(\text{white}, 1, \text{white})$ is the single cell, so
$\tau = \infty$ and $L$ is white. For (b), $\tau(S_r) = \infty$ by Proposition 20. ∎

**What the scans add (computer-assisted).** Proposition 21 splits the converse into two finite questions. Both
were answered with predictions pushed first (`rule30_cloud_fringe_uniqueness.py`, `fringe_uniqueness.c`):
- *Empty left half.* For every exact width $w \le 28$, the only right half with $\tau(R) \ge 3000$ is $S_w$ (EQ1
  held). The longest any other right half keeps the column is 476 steps.
- *Any left half.* For right halves of up to 20 cells, no left half of depth $\le 1000$ gives a finite seed with this
  column outside the family (EQ3 held). For up to 28 cells and depth $\le 200$ the same follows from EQ1 and
  Proposition 21. The registered decryption test of this case (EQ2) was refuted as worded: its window of 240 steps
  was shorter than the longest $\tau(R)$. A post-hoc rerun, with no prediction, used a window of 540 steps, longer
  than every $\tau(R)$ found. It left exactly the 29 keys of the family to depth 500 at widths up to 28.
- *Conjecture (open).* The single cell and the $S_r$ are the only finite seeds with the single cell's centre column.
  Wider right halves and deeper left halves are not covered.

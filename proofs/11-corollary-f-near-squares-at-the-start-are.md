# Corollary F (near-squares at the start are fatal)

*Windows, zero runs and the left band. Derived from [PROOFS.md](../PROOFS.md), entry "11. Corollary F (near-squares
at the start are fatal)"; rebuild with `python3 proofs/build.py`. Edit the proof in PROOFS.md and this summary in
[summaries.md](summaries.md), never this file.*

**Status:** proved.

## In plain words

A column 1 that starts by almost repeating itself, at bigger and bigger scales, is fatal.

**What it says.** If column 1's visible bits begin with a near-copy of themselves (a block followed by itself, up to
a fixed error), at ever longer lengths, then the left half cannot be finite.

**Why it matters.** It rules out a whole family of "nearly periodic" inputs at once, not just exactly periodic ones.

**An everyday picture.** A forger who copies the opening of a signature too exactly is caught by that very
precision.

## The formal statement and proof

*Where:* RULE30-PRIZE.md, "8.59 The window principle meets the band of stripes: a repeat is a white run, and the left side is never white for long (2026-10-05)". *Bears on:* near-squares at the start are fatal. *Status:* proved.

**Corollary F (near-squares at the start are fatal).** Let $c$ be the visible bits of column 1, and write
$\ell(i, i')$ for the length of the common future of $c$ at the indices $i < i'$. If there is a constant $K$ and pairs
$i_j < i'_j$ with $i'_j - i_j \to \infty$ and $\ell(i_j, i'_j) \ge i'_j - K$, then the forced left half is never finite.
In words: a column 1 that starts with a square, or misses one by a bounded amount, at larger and larger periods,
is excluded, with any left half.

*Proof.* Suppose the left half were finite, its leftmost black cell at depth $L$. By Lemma B2 there is an eventually
black diagonal $b \ge L + 2K$, black from some time $t_b$. The pair of columns $(-1, 0)$ repeats its block of length
$2\ell$ from the times $2i_j$ and $2i'_j$ (column 0 is periodic and column $-1$ at the odd times is constant). Take
$j$ with $2(i'_j - i_j) > b$ and $2i'_j \ge t_b$. Theorem A‴ with the distance $L - 1$ to column $-1$ gives
$2\ell \le L - 1 + 2i'_j - b \le 2i'_j - 2K - 1$, against $\ell \ge i'_j - K$. $\square$

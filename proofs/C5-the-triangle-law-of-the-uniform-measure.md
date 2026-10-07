# The triangle law of the uniform measure

*Short proofs restated from the running text. Derived from [PROOFS.md](../PROOFS.md), entry "C.5 The triangle law of
the uniform measure (RULE30-PRIZE.md §8.68; 2026-10-06)"; rebuild with `python3 proofs/build.py`. Edit the proof in
PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved for.

## In plain words

In a random row, Rule 30 keeps the row random, so white triangles of each width appear at an exact, predictable rate.

**What it says.** Start from a row of fair coin flips. Rule 30 keeps it a row of fair coin flips: it never
"unshuffles". So the number of white triangles with a top of width L, per square, is exactly 3 / 2^(L+4): each extra
square of width halves the rate.

**Why it matters.** It is a statement of the kind the prize's second problem asks for (how often things happen),
proved for random rows. The single-cell pattern matches it to about 0.05% in its central region, a measured sign
that the famous pattern behaves randomly there.

**An everyday picture.** A bowl of coins, stirred: stirring never sorts the heads from the tails, so a run of L
heads in a row turns up at the rate of a half multiplied by itself L times, however long you stir. Rule 30 is that
kind of stirring.

## The formal statement and proof

*Where:* §8.68; matched on a random row to $0.006\%$ and on the single cell's core right of $x/t = -0.24$ to about
$0.05\%$. *Bears on:* Problem 2's kind of statement; where the single cell's randomness lives. *Status:* proved for
the measure; the single cell's agreement is measured.

**Proposition.** Under the uniform Bernoulli measure on $\{0,1\}^{\mathbb Z}$, which Rule 30 preserves, the density
per cell of tops of white triangles of width $L \ge 1$ (a maximal white run of length $L$ whose cells above, one
wider on each side, are not all white) is $3 \cdot 2^{-(L+4)}$.

*Proof.* Rule 30 is left-permutive ($x' = l \oplus (c \vee r)$ is a bijection in $l$), hence surjective, and a
cellular automaton preserves the uniform measure if and only if it is surjective; so the row at time $t$ is
i.i.d. fair whenever the row at time $t - 1$ is. A maximal white run exactly on $[i, j]$ ($L = j - i + 1$) has
probability $2^{-(L+2)}$ (white inside, black at $i - 1$ and $j + 1$). It is a continuation exactly when the row
above is white on $[i-1, j+1]$ and black at $i - 2$ and $j + 2$: white on $[i-1, j+1]$ makes $[i, j]$ white below
($000 \to 0$), black at $i-2$ makes cell $i - 1$ black below ($100 \to 1$), black at $j+2$ makes cell $j + 1$ black
below ($001 \to 1$), and conversely a run exactly $[i, j]$ below a white stretch $[i-1, j+1]$ forces those two black
cells. That event has probability $2^{-(L+4)}$ in the i.i.d. row above. So the density of tops is
$2^{-(L+2)} - 2^{-(L+4)} = 3 \cdot 2^{-(L+4)}$. $\square$

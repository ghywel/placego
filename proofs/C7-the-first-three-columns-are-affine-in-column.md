# The first three columns are affine in column 1

*Short proofs restated from the running text. Derived from [PROOFS.md](../PROOFS.md), entry "C.7 The first three
columns are affine in column 1 (RULE30-PRIZE.md §8.58; used in COLLATZ-PRIZE.md §5)"; rebuild with `python3
proofs/build.py`. Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved (a table computed from the inverse.

## In plain words

The first three columns left of the middle just copy or flip column 1; the first real mixing happens in the fourth.

**What it says.** Next to the blinking wall, column −1 is column 1 flipped, column −2 is column 1 held for two
ticks, and column −3 is column 1 flipped one tick later. The first time two of column 1's bits are combined ("and")
is column −4.

**Why it matters.** It locates exactly where Rule 30's non-linearity first bites near the wall, and the counting
results begin here. It also marks a difference from the Collatz twin: there, knowing the pattern of odd and even
steps makes the whole orbit simple arithmetic (Terras's formula); here, knowing column 1 does so for only three
columns.

**An everyday picture.** A chain of parts on a circuit board: an inverter (out comes the opposite of what goes in),
a delay, another inverter, and only at the fourth part a gate that combines two signals, giving 1 only when both are
1.

## The formal statement and proof

*Where:* §8.58. *Bears on:* the counting form; the Collatz twin. *Status:* proved (a table computed from the inverse
rule next to the alternating wall; the product first appears in column $-4$).

**Fact.** Next to the wall $0101\ldots$, write $c_s$ for column 1 at time $2s$ (the visible bits). At times $2s$ and
$2s+1$ the forced columns are:

| Column | $-1$ | $-2$ | $-3$ | $-4$ |
|---|---|---|---|---|
| time $2s$ | $\bar c_s$ | $c_s$ | $\bar c_{s+1}$ | $c_s\,c_{s+1}$ |
| time $2s + 1$ | 1 | $c_{s+1}$ | $\bar c_{s+1}$ | $c_{s+2}$ |

Column $-2$ is column 1 with every visible bit held for two steps, column $-3$ is its complement one step on, and
the first product appears in column $-4$.

*Proof.* Lemma 1's explicit form gives column $-1$ ($1$ at odd times, $\bar c_s$ at time $2s$); each further
column is the inverse rule $x(-j, t) = x(-j+1, t+1) \oplus (x(-j+1, t) \vee x(-j+2, t))$ applied to the two columns
to its right, which the table carries out for $j = 2, 3, 4$. $\square$

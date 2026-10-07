# Theorem B (a zero run cannot outlast two periods)

*Windows, zero runs and the left band. Derived from [PROOFS.md](../PROOFS.md), entry "6. Theorem B (a zero run
cannot outlast two periods)"; rebuild with `python3 proofs/build.py`. Edit the proof in PROOFS.md and this summary
in [summaries.md](summaries.md), never this file.*

**Status:** proved; sharp at q = 2.

## In plain words

If the middle and column 1 both repeat, the left half can never show a white gap more than two periods wide.

**What it says.** Suppose the middle column and column 1 repeat every P ticks. Then, at the starting moment, every
stretch of white squares across the left half is at most 2P − 2 squares wide. The units differ: the gap is measured
across space, in squares, and the period in time, in ticks.

**Why it is true.** Every column of the left half inherits the same repeat. A wide white gap forces a white triangle
beneath it, and a gap of 2P − 1 or more makes the triangle deep enough that some column stays white for a whole
period. A repeating column that is white for one whole period is white for ever. That permanent white then spreads
right, column by column, through the latch of C2, until it would silence the middle column, which is still beating.

**Why it matters.** A finite left half needs an endless white stretch. This shows repeating columns cannot give one,
with a sharp number attached. It counts squares and ticks, not seconds, so it holds at any speed the pattern is
played back (the owner's question; see G98).

**An everyday picture.** Music on a loop: if it is silent for one whole play-through, it is silent for ever. A white
gap two loops wide guarantees such a silence somewhere, and silence spreads until it reaches the drummer in the
middle, who is still playing.

## The formal statement and proof

*Where:* RULE30-PRIZE.md, "8.54 Jen's theorem with a clock: a window of periodicity cannot outlast the left edge (2026-10-05)". *Bears on:* question 2: a zero run in row 0 of the forced left half is at most two periods long. *Status:* proved; sharp at q = 2.

**Theorem B (a zero run cannot outlast two periods).** Let columns 0 and 1 be $P$-periodic from time 0, with
$P \ge 2$ and column 0 not zero. Then every run of zeros in row 0 of the forced left half has length at most
$2P - 2$. (For $P = 1$ the same proof gives 1, which is attained by the stripes $0101\dots$ in space.)

*Proof.* Every column of the left half is $P$-periodic (fact 1, with an unbounded window). Let row 0 be zero at
depths $d$ to $d + R - 1$. A cell is white when the three cells above it are. So column $-k$ is white at times 0 to
$\min(k - d,\ d + R - 1 - k)$, which is a triangle of zeros under the run. If $R \ge 2P - 1$, the column at
$k = d + P - 1$ is white for $P$ steps in a row, and so for ever. With column $-k$ zero, the rule for the column to
its right reads $x_{t+1}(-k+1) = x_t(-k+1) \vee x_t(-k+2)$. That column never turns from black to white. It is
periodic, so it is constant. Its depth $d + P - 2$ lies in the run because $P \ge 2$, so it is white at time 0, and
zero for ever. Two adjacent zero columns force zeros to
the right, as in §8.13, as far as column 0, which is not zero. $\square$

*Odd-run refinement (GPT, 2026-10-07; R5 continuation, GC307; independent review pending).* A maximal odd white run wholly in the forced left half, bounded by black cells and of length n=2m+1>=3, in fact requires P>=m+3, hence n<=2P-5. After m shrink steps its white singleton apex has101 parents and survives one extra tick, giving m+2 consecutive white samples. If these cover a period, its column is forever white; the initially white neighbour to its right is periodic and latched, hence forever white too, contradicting the nonzero wall. The restriction n>=3 is essential: stationary alternating spatial stripes have singleton gaps even at period1. The original general bound for even runs is unchanged. Full proof and endpoint controls are in RULE30-GPT's R5 continuation.

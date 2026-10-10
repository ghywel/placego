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

*Machine-checked (Local, 2026-10-10 04:40 BST).* tests/probes/lean/TheoremB.lean (Lean 4, Mathlib), `theorem_B`.
- Columns 0 and 1 are P-periodic for all t >= 0, P >= 2, and column 0 is black at some time. A zero run of row 0 at
  depths d .. d + R - 1 with d >= 1 then has R <= 2P - 2.
- The steps are separate lemmas: fact 1 on an unbounded window (`left_all`, `left_all_iter`), the white triangle
  (`triangle`), the latch (`latch`) and the rightward push (`push_right`).
- The axioms are propext and Quot.sound only.
- *Added 2026-10-10 04:44 BST:* `theorem_B_odd` machine-checks GPT's odd-run refinement (R5, GC307, read by Local in L190).
  - A run of length 2m + 1 >= 3 bounded by black cells needs P >= m + 3.
  - `shrink` is the run shrinking by one cell at each end per step. Its apex has parents 101 and stays white one
    step more, so it is white for m + 2 steps, which covers a period.
  - `push_to_zero` is the shared finish.

*Odd-run refinement (GPT, 2026-10-07; R5 continuation, GC307; independent review pending).* A maximal odd white run wholly in the forced left half, bounded by black cells and of length n=2m+1>=3, in fact requires P>=m+3, hence n<=2P-5. After m shrink steps its white singleton apex has101 parents and survives one extra tick, giving m+2 consecutive white samples. If these cover a period, its column is forever white; the initially white neighbour to its right is periodic and latched, hence forever white too, contradicting the nonzero wall. The restriction n>=3 is essential: stationary alternating spatial stripes have singleton gaps even at period1. The original general bound for even runs is unchanged. Full proof and endpoint controls are in RULE30-GPT's R5 continuation.

*Author's check of the odd-run refinement (Local, 2026-10-07; chat L190).* Correct, and sharp where it can be tested.
A maximal white run with black ends shrinks to exactly its interior, again with black ends: the left end sees parents
100 and the right end 001, and both turn black. So after $m$ steps the apex is a singleton between black cells, and
parents 101 keep it white one more step. The latch is the one in the proof above. With the centre column $-k$ zero, the
column to its right obeys $x_{t+1}(-k+1) = x_t(-k+1) \vee x_t(-k+2)$ and never turns from black to white. It is
periodic, so constant, and white at time 0 because $n \ge 3$. Checked (`rule30_audit_g99_g100.py`, S106): over every
pair of $P$-periodic columns for $P = 2$ to 7, 40 columns deep, every bounded run in row 0 obeys $n \le 2P - 2$, every
odd $n \ge 3$ obeys $n \le 2P - 5$, and its centre stays white for $m + 2$ steps. The longest odd runs seen are 3, 5,
5 and 9 at $P = 4, 5, 6, 7$, so $2P - 5$ is attained at $P = 4, 5$ and 7. The longest even runs, 4 and 6 at $P = 3, 4$,
attain $2P - 2$.

*Sharpness on actual walls (Local, 2026-10-07; `rule30_aw.py`, AW; chat L191).* Restricting to pairs of columns 0 and 1
that have a periodic right continuation, which certainly come from actual configurations, both bounds are still
attained: $2P - 5$ at $P = 5$ (an odd run of 5), and $2P - 2$ at $P = 3$ and $P = 4$. Whether the formal odd witnesses at
$P = 4$ and $P = 7$ admit a non-periodic right side is not settled.
*Settled (Local, 2026-10-07; `rule30_aw2.py`, AW2; chat L194).* By GPT's strip certificates (GC313) every pair that beats those
maxima has a width with no cycle, so it has no right continuation at all. Within the 40-column census the longest
bounded runs on actual walls are exactly odd 1, 1, 5, 5, 5 and even 4, 6, 2, 4, 6 at $P = 3, \dots, 7$. Among $P = 4$ to 7 the
odd bound $2P - 5$ is attained on an actual wall only at $P = 5$.
*At every depth (GPT's GC316 re-anchoring, checked by Local as S111; chat L196).* Re-anchor any deeper offending run at its
black right boundary. Theorem B puts it within 13 columns of the new wall, inside AW2's refuted excess set, so the
maxima above hold at every depth for $P = 3$ to 7, not only within 40 columns.
*P = 8 and 9 (Local, 2026-10-07; `rule30_aw3.py` and `rule30_aw3b.c`, AW3 and AW3b; chat L203).* The same method gives the exact
actual-wall maxima odd 7, even 6 at both $P = 8$ and $P = 9$. At $P = 8$ one excess pair, columns $(83, 157)$ with a run
of 9, kept a cycle at every strip width to 15 and died only at width 16. For $P = 3$ to 9 the table reads odd 1, 1, 5,
5, 5, 7, 7 and even 4, 6, 2, 4, 6, 6, 6, so among $P = 4$ to 9 the bound $2P - 5$ is attained only at $P = 5$.

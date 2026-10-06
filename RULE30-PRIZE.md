# Rule 30 Prize Problem 1: the work

*Split out of [PRIZE-PROBLEMS.md](PRIZE-PROBLEMS.md) on 2026-10-05, at the owner's request. That document keeps the
open prizes as a whole (§1 to §4 there: the prizes, how a computer can win one, the ranking, and the tricks that let
a computer take part in a proof). This one holds the Rule 30 work, with its section numbers unchanged, so a
reference to "PRIZE-PROBLEMS.md §8.36" written before the split means §8.36 here. For the period-2 work in one place,
with its reading order and how to reproduce it, see [PERIOD-TWO.md](PERIOD-TWO.md).*

## The honest summary

**Update, 2026-10-05, night (Local as lead; read this first).** Still no proof of period 2 and nothing to submit.
Three theorems were added, each elementary and each checked by a pre-registered probe:
- **Theorem A (§8.54), Jen's theorem with a clock.** Two adjacent columns cannot both be $P$-periodic on a time
  window $[a, b]$ unless $b \le 2a + L + 2P - 1$, where $L$ is the distance to the left edge. So in any period-2
  counterexample the wheel's kicks cannot thin out faster than geometrically.
- **Theorem B (§8.54).** With $P$-periodic columns 0 and 1, no zero run of the forced left half is longer than
  $2P - 2$. The bound is attained at visible period 2.
- **Theorem E (§8.57).** If column 1 is any Sturmian sequence (a coding of an irrational rotation), the forced
  left half is never finite. With Jen's theorem: no pure wheel works, rational or irrational. These are the first
  columns 1 beyond the eventually periodic ones for which Conjecture LR is proved.
Also: question 4 is closed (§8.55: Kari and Kopra's argument is about rows, not columns), and the Collatz twin's
state after the free bits is exactly a least residue modulo a power of 3 (COLLATZ-PRIZE.md §4). None of this
reaches the real case, where kicks come at a steady rate. §8.54 explains why the method stops there.
- **The Collatz transfer (§8.58, COLLATZ-PRIZE.md §5).** Both problems obey one exact statement, the window
  principle: a block of the trace can repeat only if it is no longer than the state is large. It gives Theorem A′
  here and, on the Collatz side, that no rational has a Sturmian parity sequence (found afterwards to be known:
  Dubickas 2009 for integer orbits, and three 2026 notes; COLLATZ-PRIZE.md §5). It also names what is missing
  here: a counterexample must keep the $2n$ cells beside its centre within $2^{0.13\,n}$ contents for ever, and
  the edge certifies only about $n$.
- **The band of stripes, brought in (§8.59).** The left end of every row has infinitely many diagonals that are
  black for ever (Lemma B2: the diagonals' periods are unbounded), so a repeat of the trace, which is a white run
  in the later row, must stay a growing distance below Theorem A′ (Theorem A‴). Corollary F: a column 1 that
  begins with near-squares at larger and larger periods is excluded with any left half (the period-doubling
  word, Chacon's word, every substitution fixed point starting with a double letter). The settled band has no
  white run longer than twice its period (Lemma B3), so a repeat's white run cannot lie in it (Theorem A⁗):
  with the universal strip certified to 53,200 diagonals, Thue–Morse and paperfolding are excluded for every
  left edge up to about 15,870 cells. For every left edge, their case reduces to one question about the left
  side of Rule 30 alone: does it settle at a bounded rate.

**Update, 2026-10-05, evening.** Still no proof and nothing to submit. The day's work moved
the problem to one precise statement:
- **Where it sits** (§8.45, §8.47, §8.49). Period 2 has the structure of Mahler's 3/2 problem: a free left side, a
  thin constrained right side (the wheel and its kicks), agreement at the wall for ever. A survey of eight fields
  found the same gap everywhere: theorems that holding a chaotic system costs information are about sets of cases,
  never one case. Here the gap can be crossed by an exact count, because seeds are finite.
- **The counting form** (§8.51). The number of configurations on $w$ cells whose centre follows 0101 for $T$ steps
  falls by about $2^{1.05}$ per step, exactly counted to $w = 24$. Proved: the conditions paid by the seed's left
  part halve the count exactly (left-permutivity).
- **The open part** (§8.52). The right part pays in lumps, never more than 3 free steps in a row to $w = 26$. The
  statement that would close period 2: $N_{w,j}(T+k) \le 2^{c(w) - \alpha k} N_{w,j}(T)$ for some $\alpha > 0$, with
  $c(w) = O(\log w)$. PERIOD-TWO.md §7 lists it with the other questions for whoever continues.
- **Local's records**: $R(85) = 73$ and $R(89) = 75$ (14 hours), as predicted blind from the merging census (§8.38); no right half up to 34
  cells is a counterexample.

**Where the work stands (2026-10-05, early morning).** There is no proof and nothing to submit. Period 1 was closed
by Condrey; period 2 is the open case, and the work concentrates there. What exists:

- **Evidence.**
  - No counterexample: every right half up to 18 cells for periods 2 to 6 (27 million cases, §5, §6), and for period
    2 every right half up to 32 cells, 4.3 billion: no finite configuration with a right half of at most
    32 cells and a left half of at most 108 has a period-2 column (§8.21).
  - The search can see a counterexample where one exists: in Rule 60, a sibling rule (§8.3).
- **Proved, or known and restated.**
  - Lemmas 1 to 4, about where the right side's bits enter the left half.
  - Proposition 5: in the sibling Rule 90, no period-2 column is possible, by Lucas' theorem.
  - Proposition 7 (Jen, 1990): no eventually periodic column 1 can make the left half finite. So in a finite
    configuration with column 0 eventually 0101…, column 1 is never eventually periodic, and the wheel must slip
    for ever (§8.13).
  - Every white triangle of Rule 30 is exact (§8.18). Run backwards, the pyramid is infinite and one-sided, and
    the backward step is the forced-left-half equation read in time (§8.19).
- **Computed facts.**
  - Proposition 6: the pure wheel's left half has an exact tail and period in depth (§8.6).
  - **The channel bound:** next to 0101…, column 1 carries at most 0.128 bits per visible bit, whatever the right
    side, from an exact automaton (§8.20). The bound is levelling off near 0.12. Typical right sides use 0.08, about
    3.5 bits per kick. A random sequence carries 1. The bound is now certified exactly (0.1292 at $m = 26$; 0.1236 at
    $m = 28$ since 2026-10-06), and it
    forces every column to the left of a period-2 column 0 below 0.0646 bits per step (§8.33; 0.0618 since the
    certificate reached $m = 28$ on 2026-10-06).
- **The picture.**
  - The right side runs a universal wheel, a rotation by 17/56 of a turn per step, kicked in whole notches by
    domain walls (§8.5 to §8.11). Next to column 0 the white triangles form a lattice in the wheel's frame, and a kick
    moves it rigidly. Walls that kick the wheel forward carry large white triangles along their path, and every
    kick sends a wake of them outwards (§8.18).
  - Every zero run of the left half costs about one bit per cell, paid from the distinct histories of column 1: the
    adversary does no better than coin flips (§8.14, §8.16).
  - A seed's information reaches column 1 slowly, at about 0.2 cells per step. So at a fixed depth the longest
    real zero run is set by the channel, not the seed: 8 cells from depth 41 for every seed width from 16 to 28
    (§8.17).
  - The owner's morning questions (§8.22 to §8.37). Read as a binary number, a column is rational exactly when it
    repeats, so the prize asks for one number's irrationality. A period-2 counterexample would need two irrational
    numbers adding to exactly 1, and a finite seed keeps them complementary for at most about $(w + 9)/2$ digits. The
    pyramid's diagonals are all rational, and the centre column is their Cantor diagonal. The diagonals' periods and
    the striped left side were known already (Jen; Rowland; Wolfram), and were re-derived here before the sources
    were read. As a conductor, Rule 30 channels lightning three times less than a random material, because of its
    handedness. As a maze it has no dead ends going up.
- **Routes closed.**
  - Bounded runs, at every layer width computed (up to 16): the adversary's runs keep growing with depth (§8.14).
  - Periodic columns 1, already a theorem (§8.13).
  - "Structured families" beating chance: they were luck (§8.16).
  - The entropy squeeze as a reduction (§8.33): it restates the problem. A proof along it needs a lower bound on a
    column's entropy in a finite configuration, which has never been proved for Rule 30.
- **The sharpest open target (§8.36).** The doubling conjecture: in the forced left half for 0101…, a zero run that
  starts at depth $d$ ends by depth $2d + 4$, for every column 1. It holds at every depth computed (to 81, with
  growing slack), and it would settle period 2 for every finite configuration. §8.38 explains the slack. The forced
  walks merge, about 6% at every step, so there are about $2^{0.41\,d}$ distinct walks rather than $2^{d/2}$. The
  coin's best of them lasts about $0.82\,d$ cells, which is what the records show.
- **The gap.** The kicks must happen for ever. A proof must show they can never steer the left half to zero and
  keep it there. Every statistic says they cannot: coin flips paid through a narrow channel. Nothing structural
  yet says why. §8.38 to §8.41 reduce every form of the question to one statement. In the wall form (§8.39), the
  conditions at a 0101 wall cost real information. The delivery side is a theorem (§8.20). The cost side holds
  exactly next to a white wall, where the channel's entropy is 0 (Condrey's case), and only as a coin model next to
  0101 (§8.41). The prime-gap parallel (PRIOR-ART) suggests the proof's likely shape: a size argument, as for
  Bertrand's postulate, rather than a proof of randomness. The structural levers found so far are listed in §8.15:
  - the tie between neighbouring columns;
  - the wheel;
  - the notched kicks;
  - Jen's leftward flow of periodicity;
  - the bottleneck and its exact bound.

The night's three main measurements are drawn in one figure, [rule30_night.svg](tests/probes/lexicon/rule30_night.svg):
- the adversary's runs against depth;
- the channel bound against layer width;
- the real runs against seed width.

Several of these results had been reached by others first: Condrey's triangular uniqueness, his "no bounded law" at
period 2, Hanson and Crutchfield's domain filter, Jen's theorem for periodic columns 1, and Meier and Staffelbach's
reconstruction of the left half from two columns (1991, §8.15). PRIOR-ART.md records them.

---

## 5. The first experiment: periodic columns in Rule 30

**The setup.** In $\mathbb F_2$, Rule 30 is $x'_i = x_{i-1} + x_i + x_{i+1} + x_i x_{i+1}$, which is linear in the
left cell. So for any column-0 trace $\tau$ and any right half $R$, the left half is forced, cell by cell:

```math
x_t(-1) = \tau(t+1) + \big(\tau(t) \vee x_t(1)\big), \qquad
x_t(-k) = x_{t+1}(-k+1) + \big(x_t(-k+1) \vee x_t(-k+2)\big) \pmod 2 .
```

A finite configuration whose column is eventually $p$-periodic, shifted in time, is a finite configuration whose
column is exactly $p$-periodic from $t = 0$. So the question for each $p$ is this: for some primitive word of length
$p$ and some finite $R$, is the forced left half eventually zero? Condrey proved the answer is no for $p = 1$. Jen
(1990) proved that two *adjacent* columns are never both eventually periodic. The prize asks about *one* column.

**The run** (2026-10-04, Cloud, one CPU core, 4m38s; predictions in the script header, written first):

| Check | Result |
|---|---|
| A. Published control: Condrey's sharp constant-prefix maxima $2\lceil w/2\rceil + 1$ and $2\lfloor w/2\rfloor + 2$, overall $w + 2$, with $2^w$ or $2^w - 1$ maximisers | **reproduced exactly** for $w = 1$ to $7$ (maximisers $1, 4, 7, 16, 31, 64, 127$) |
| B. Control: constant traces force left halves that are eventually alternating, never zero; the same for every $R$ when $\tau \equiv 1$ | **as predicted**: 32,767 cases |
| C. The construction: forced configurations reproduce their trace forwards; one flipped cell at depth $k$ breaks it at exactly $t = k$ | **66 of 66, and 66 of 66 caught** |
| D. Periods $2$ to $6$, every primitive word, every right half in $[1, 14]$, depth $192$: a forced left half that is eventually zero? | **none**, in 1,703,936 cases |
| E. Brute force over every configuration with support in $[-w, w]$: the longest stretch of a trace that follows its first $p$ values | grows slowly with $w$, at most $16$ at $w = 7$ (table in the run output) |

**An observation nobody predicted, and its explanation.** For periods $3$, $5$ and $6$, every forced left half is
aperiodic over its last 64 cells. For periods $2$ and $4$, a minority have tails of period exactly $7$, $14$ or $28$
(period 2: 773 of 32,768; period 4: 74,027 of 196,608). Some are periodic from the very first cell: the alternating
trace with the right half "cells 1 and 4 black" forces a left half that is exactly 7-periodic.

The lexicon's lift explains it (LEXICON.md §3.6: a finite program's loops are its spectrum). A spatially $n$-periodic
configuration is Rule 30 on a ring of $n$ cells, a finite program. Its cycles say which temporal periods its columns
can have. Computed for every ring up to 18 cells (all 524,286 states visited; the 7-ring's cycle lengths $1$,
$4 \times 7$ and $63$ as a known answer):

| Column period | Ring sizes (up to 18) where a Rule 30 orbit has it |
|---|---|
| $1$ | every size |
| $2$, $4$ | $7$, $14$ |
| $3$ | $12$ |
| $5$ | $5$, $10$, $15$ |
| $6$ | none |
| $7$, $9$ | $15$ |
| $8$ | $4$, $8$, $12$, $16$ |

The 7-ring has seven cycles of length 4, on which one cell repeats with period 4 or 2. So the 7-, 14- and 28-periodic
left halves are the left half settling into a copy of a 7-ring or 14-ring orbit, which is possible only for periods 2
and 4. For period 6, no ring up to 18 cells has such an orbit at all. A finite configuration needs its left half to
settle into the zero orbit instead. This is the first structural handle on the $p = 2$ case, and it is where rung 2
starts.

**What this is and is not.** It is evidence for a conjecture: *no nonzero finite Rule 30 configuration has an
eventually periodic column of period $2$ to $6$.* It is not a proof. The right halves were bounded, and "eventually
zero" was tested over 64 cells at depth 192. If the conjecture holds for every period, it implies Rule 30 Problem 1,
because the single black cell is a finite configuration.


## 6. The rungs from here

The Rule 30 rungs. The project-wide rungs (the lexicon, the GPU float check G1, Beal) are in
[PRIZE-PROBLEMS.md](PRIZE-PROBLEMS.md) §6.

| Rung | What | Who | Status |
|---|---|---|---|
| 1 | Rule 30, periods 2 to 6, exhaustive over small right halves, with the published control | Cloud, CPU | done: right support 14 at depth 192 (1,703,936 cases, 4m38s on one core), then right support 18 at depth 256 (27,262,976 cases, 4 cores); the control holds to $w = 8$ (256 maximisers); no eventually-zero left half anywhere |
| 2 | **The $p = 2$ structure.** The 7-periodic tails are explained (§5: 7-ring orbits). Next: find the forced left half's form for both period-2 traces, as Condrey did for constant traces; whether every forced left half eventually settles into some ring orbit was asked first and answered no: at depth 768, 1,999 of 2,048 period-2 right halves up to 10 cells show no period up to 128 over their last 256 cells, and the other 49 have periods 7, 14 or 28 (`rule30_rings.py`). So the argument must handle aperiodic left halves, and prove from their form that they are never eventually zero. Formalise in Lean. | Cloud | next |
| 3 | Periods $3$ to $6$ the same way, then look for the pattern across $p$: the uniform argument, which is the prize | Cloud | open |

The GPU is not needed for rungs 1 to 3 at these sizes. A CPU does them exactly in minutes. It enters if the search
must go much further, or for G1 and rung 4. The project's real advantage is not the hardware. It is the method: a
prediction before every run, a known answer beside every new one, and a counterfactual that must fail.

---

## 7. Rung 2, first progress: left-side rigidity (2026-10-04)

Working the period-2 case turned up a reduction that covers every period at once. Its proof needs an idea that has
not been found yet. Its evidence is exhaustive but finite.

**Lemma 1 (where column 1 is invisible).** With column 0's trace $\tau$ fixed, the forced left half depends on column
1 only at the times $t$ with $\tau(t) = 0$.

*Proof.* The only place column 1 enters is
$x_t(-1) = \tau(t+1) + \big(\tau(t) \vee x_t(1)\big) \bmod 2$. Where $\tau(t) = 1$, the "or" is 1 whatever $x_t(1)$
is. Every further left column is built from columns $-1$ and $0$ and those to their left. $\square$

*Checked:* `rule30_rigidity.py`, check R1: 880 of 880 random cases. For the alternating trace it gives explicit
columns (check R0, 2,000 random columns 1): column $-1$ is 1 at every odd time and $\lnot\sigma(2s)$ at time $2s$; column $-2$ is $\sigma(2s)$ at times
$2s$ and $\sigma(2s+2)$ at times $2s+1$. Here $\sigma$ is column 1. So $x_0(-1) + x_0(-2) = 1$, always.

**Lemma 2 (rotations are equivalent).** A finite configuration whose column is exactly periodic from $t = 0$, with
word $w$, is still finite one step later, and its column is then periodic with $w$ rotated by one place. So a finite
configuration exists for one rotation of a cyclic word exactly when it exists for all of them, and ruling out one
rotation per class is enough. $\square$

**Conjecture LR (left-side rigidity).** For every primitive word of period $p \ge 2$ and *every* column 1, not only
one made by a finite right half, the forced left half contains infinitely many ones.

**What LR would prove.** Suppose a finite configuration has a column that is eventually $p$-periodic. Shifting time
makes it exactly periodic, and the configuration stays finite, so its left half must be eventually zero. For
$p \ge 2$ that contradicts LR, and Condrey's theorem covers $p = 1$. So no column of any nonzero finite configuration
is eventually periodic, and in particular not the centre column from a single black cell. **LR implies Rule 30 Prize
Problem 1.** It is a statement about the left side alone, and it is stronger than the problem needs.

**Why it might be true: counting.** A word with $z$ zeros in its period leaves $z/p$ free bits of column 1 per left
cell (Lemma 1), and $z/p < 1$ for every primitive word with $p \ge 2$. The two extremes match what is known:
- the word "1" has no free bits, and its left half is Condrey's universal fibre;
- the word "0" has one free bit per cell, and column 1 $= 000\ldots$ gives the zero configuration, which is why
  Condrey's proof needed the right half for it.

Counting alone cannot prove LR. A single special column 1 could still make the left half vanish.

**Evidence** (`rule30_rigidity.py`, exhaustive over every column 1, from each starting depth whose earlier free bits
number at most 10; predictions written before the run):

| Check | Result |
|---|---|
| R1 control: column 1 is invisible where $\tau = 1$ | 880 of 880 |
| R2 control: for $\tau = 000\ldots$ the search reaches its cap from every depth, so it can see an infinite run | depths 1 to 11 |
| R3 control: for $\tau = 111\ldots$ the longest zero run is 1 | 1 |
| R4, main claim: every zero run ends (none reaches 400 cells), for all 26 primitive words of period 2 to 4 | **held**, every word, every depth tested (up to 44) |
| R4, bound: every run ends before depth $3d + 12$ | **refuted** for 0010 and 0100: a run from depth 14 ends at 62 |
| R5 (post hoc): longest run per word | grows with the starting depth for every word, peaking at the deepest depths tested (14 to 49) |

The deeper run (14 free bits, periods 2 to 5, the same predictions, Cloud on 4 cores) gives:

| Check | Result |
|---|---|
| R1 to R3 controls | all pass (R2 from depths 1 to 15) |
| R4, main claim: every zero run ends | **held for all 50 primitive words of period 2 to 5**, at every depth tested (up to 72) |
| R4, bound $3d + 12$ | **refuted** for 10 words: every rotation of 0001 and of 00001, and 100 |
| R5 (post hoc) | words with one zero per period are the most rigid. The longest runs of 01, 011, 0111 and 01111 stay between 17 and 23, even from depth 72. Words with mostly zeros allow the longest: 54 to 58 for the rotations of 0001, 45 to 66 for those of 00001. Rigidity grows as column 1's freedom $z/p$ falls, as the counting argument suggests. |

A first look for the rescaling found nothing yet (`rule30_witness.py`, recorded as a null result). The record runs
for the alternating trace from depths 9, 13 and 33 are 9, 17 and 33 cells long. Each is set by roughly the last
$d/2$ bits of column 1, and the earlier bits do not matter: 1, 3 and 21 prefixes reach the record. No substitution
mapping one depth's record column 1 to the next is visible by eye.

The single-zero words may not stay bounded either: the alternating trace's longest run jumps to 32 at depth 33
(exploration with 18 free bits, beyond this run's range). The words with mostly zeros are where LR is most at risk.

So the zero runs are not uniformly bounded. A run starting deeper can last longer: for the alternating trace, runs
from depth $d$ end near twice $d$. A proof of LR therefore needs a growth argument, of the form "a run from depth $d$
ends by $c \cdot d$". A local identity forbidding a fixed window of zeros is not enough. The self-similar endpoints
(runs ending near 16, 28-30, 64-68) suggest a renormalisation, mapping a long run at depth $d$ to a shorter one at
depth about $d/2$. That is the next thing to look for.

**What is open.** LR for any single word, as a theorem. Whether LR holds for long words that are mostly zeros
($0\ldots01$), which leave column 1 almost free. Whether the right half must be used after all, for some words.


## 8. The right side as a complement (2026-10-04)

The owner's suggestion, after §7: rather than ignore the right side, use it to complement the left. It works. The
left side alone leaves column 1 free, and then zero runs grow with depth (§7). But column 1 is not free: it is part of
the right side, and Rule 30 constrains it heavily.

**Lemma 3 (two local rules from the right side).** At column 1, Rule 30 reads
$\sigma(t+1) = \tau(t) + \big(\sigma(t) \vee x_t(2)\big) \bmod 2$, where $\tau$ is column 0 and $\sigma$ is column 1.
So, whatever column 2 does:

```math
\tau(t) = 0:\quad \sigma(t) = 1 \;\Rightarrow\; \sigma(t+1) = 1, \qquad\qquad
\tau(t) = 1:\quad \sigma(t+1) = 1 \;\Rightarrow\; \sigma(t) = 0 .
```

For the alternating trace, this means the part of column 1 that the left side sees, $e(s)$, never has two ones in a
row. $\square$ *Checked:* `rule30_twosided.py` T1 and T2 (every right half tried; random sequences violate the rules,
so they are not vacuous).

**How much the right side constrains column 1** (T3: every right half of width $n$ against the rules and against
everything):

| Column 1 prefixes, length $n$, trace 0101… | $n = 6$ | $n = 10$ | $n = 14$ | $n = 20$ |
|---|---|---|---|---|
| produced by some right half | 8 | 18 | 36 | **86** |
| allowed by Lemma 3's two rules | 17 | 99 | 577 | 8,119 |
| all sequences | 64 | 1,024 | 16,384 | 1,048,576 |

So the right side leaves column 1 almost no freedom: 86 sequences out of a million at length 20, growing roughly like
the square of the length rather than exponentially. Long columns 1 (T5, 3000 steps) are not eventually periodic. They
have very few distinct patterns: 95 distinct 64-cell patterns in 2000 cells, where a random sequence would have about
2000. They are not one universal sequence either: 13 to 17 of 39 random right halves give a tail found inside the
first one's.

**Lemma 3 alone is not enough** (T4, pre-registered). Searching only columns 1 that obey the two local rules, the
longest zero run is shorter than with a free column 1, but it still grows with depth: 18 for 0101… and 20 for
1010… by depth 40. The prediction that it would stay at or below 16 is **refuted**. The constraint that matters is
the exact one, the 86 sequences, not the two rules.

**Both sides exactly** (`rule30_twosided_exact.py`). Here column 1 comes from a real right half, and the left half is
forced from columns 0 and 1. This is a measurement, made before any prediction about it:

| Exact width of the right half | 8 | 10 | 12 | 14 | 16 | 18 | 20 |
|---|---|---|---|---|---|---|---|
| Longest zero run, trace 0101… (depth up to 192) | 14 | 15 | 15 | 20 | 20 | 20 | 20 |
| Longest zero run, trace 0001… (depth up to 192) | 13 | 13 | 17 | 17 | 17 | 17 | 17 |

At depth 192 the run length levels off with width, and over every right half up to 16 cells it shows no trend with
depth up to 256. (X3, below, shows that this plateau does not survive a deeper search.) Compare §7: with column 1
free, runs from depth $d$ reach about $d$ cells, 54 for 0001 from depth 18.

**Conjecture B (two-sided rigidity).** For each primitive word $w$ of period at least 2 and every finite right half,
every zero run in the forced left half ends. It was first stated with a constant bound: a number $B(w)$ such that the
forced left half never has more than $B(w)$ zeros in a row. The data at depth up to 192 suggested $B(01) = 20$ and
$B(0001) = 17$. The deeper search below refutes both values (X3: 24 and 26 by depth 384), so the constant-bound
form is dropped.

**What B would prove.** A left half in which every zero run ends is never eventually zero (with a constant bound,
it would have a one in every $B(w) + 1$ cells). So no finite configuration has a column periodic with $w$; together
with Lemma 2 (rotations) and Condrey's $p = 1$ theorem, the statement for every $w$ implies Rule 30 Prize Problem 1.
B is weaker than LR (§7) because it uses the right side. That is why it can hold where LR may fail.

**Why B looked like the better target, and what is left of that.** With a constant bound it would be a *bounded*
statement: no window of $B + 1$ cells is all zero. Bounded statements are the kind a finite check can prove, provided
the two-sided system has a finite-state description, and the 86 sequences, with their very low complexity, pointed
that way. X3 (below) removes the constant bound, and T6 (below) shows column 1 is not 2-automatic. What survives is
the slow growth: two-sided runs grow far more slowly than one-sided ones, so the right side still does most of the
work.

**Pre-registered X3, refuted.** The prediction was that the plateau holds further: $B$ still 20 (0101…) and 17
(0001…) for right halves of width 22 and 24 (about 33 million), at depth up to 384. It does not:

| Exact width of the right half | 8 | 10 | 12 | 14 | 16 | 18 | 20 | 22 | 24 |
|---|---|---|---|---|---|---|---|---|---|
| Longest zero run, trace 0101…, depth up to 192 | 14 | 15 | 15 | 20 | 20 | 20 | 20 | 20 | 20 |
| Longest zero run, trace 0101…, depth up to 384 | 15 | 15 | 18 | 20 | 20 | 20 | 22 | 24 | 24 |
| Longest zero run, trace 0001…, depth up to 192 | 13 | 13 | 17 | 17 | 17 | 17 | 17 | 19 | 19 |
| Longest zero run, trace 0001…, depth up to 384 | 13 | 14 | 17 | 17 | 19 | 26 | 26 | 26 | 26 |

Both controls passed: the search reproduces the recorded values (X1), and with a free column 1 the same window holds
runs of 33 cells for 0101… and 54 for 0001…, so long runs fit and can be seen (X2). So $B(01) = 20$ and
$B(0001) = 17$ were artefacts of stopping at depth 192. The runs keep growing with depth, slowly: 24 and 26 by depth
384, against runs of about $d$ from depth $d$ with column 1 free. At depth 384 the runs level off with width again,
at 24 for widths 22 and 24 (0101…) and at 26 from width 18 to 24 (0001…). That is the same shape as at depth 192, so
the longest run looks like a function of the depth searched, not of the width. **Conjecture B is weakened
accordingly**: not a constant bound, but *every two-sided zero run ends* (the forced left half is never eventually
zero). That weaker statement is all that Prize Problem 1 needs. It is no longer a finite check by itself, which is why
§8.2 looks at where the long runs come from.

**A first look at column 1's structure** (T6, a measurement). Column 1 is locally rigid but globally chaotic.
- **Locally it is tightly constrained.** Over 61,440 steps it contains only 13 distinct 8-cell patterns and 21
  distinct 16-cell patterns; a random sequence would contain 256 and about 61,000.
- **Globally it is not simple.** At 256 cells there are about 20,000 distinct patterns, and the count is still growing
  about 16-fold per doubling of the length.
- **It is not generated by a finite automaton in base 2.** Its 2-kernel grows almost like a random sequence's (492 of
  512 at $k = 9$; Thue–Morse, the control, has 2).
- **One exception fits §5.** A right half of width 18 gives a column 1 that becomes exactly 14-periodic: a copy of a
  14-ring orbit, next to a 2-periodic column 0. That is not a counterexample to Jen, because the left half it forces
  is infinite.

So the simplest route to a finite proof, "column 1 is generated by an automaton", is closed (recorded as a null
result). The zero runs are local events, though, and so are column 1's constraints.

**Next.** Describe column 1's *local* language: the set of patterns it can contain, of each length. Then find whether
the forced left half's zero runs depend only on that local language. If they do, B becomes a finite check.

### 8.1 The four arms (the owner's design, 2026-10-04)

The owner pushed back on §8's framing: the left-only exploration was not wasted. It was the control arm that §8 is
measured against. And a factorial design needs its fourth arm. Column 1 is shared by both sides. The left side either
forces the left half or leaves it free, and the right side either produces column 1 or leaves it free.
`rule30_factorial.py` measures one statistic in all four arms: the longest zero run in the left half, depth 1 to 64,
over 100,000 samples per arm, with fixed seeds (predictions in its header, written first).

Trace 0101…, probability that the longest zero run is at least $B$:

| $B$ | coin flips (exact) | neither | right alone | left alone | both |
|---|---|---|---|---|---|
| 5 | 0.648 | 0.647 | 0.648 | 0.655 | 0.734 |
| 7 | 0.211 | 0.210 | 0.209 | 0.184 | 0.134 |
| 11 | 0.0134 | 0.0139 | 0.0134 | 0.0126 | **0.0213** |
| 12 | 0.0066 | 0.0073 | 0.0065 | 0.0063 | **0.0212** |
| 13 | 0.0032 | 0.0039 | 0.0032 | 0.0032 | **0.0119** |
| 14 | 0.0016 | 0.0018 | 0.0016 | 0.0018 | **0.0119** |
| 15 | 0.0008 | 0.0009 | 0.0008 | 0.0008 | **0** |

What the four arms show:

1. **Right alone is the same as neither** (proved, and measured: every tail probability within 0.0022). Once
   column 0 is fixed, the right side never depends on the left. Any finite right half works with any periodic
   column 0, because column 0's own update is met by choosing column $-1$, and that choice is exactly what the left
   side forces. So **on its own the right side never forbids a finite configuration**.
2. **Left alone is close to coin flips.** With column 1 random, the forced left half is statistically almost random,
   with small but real deviations: runs of 7 or more occur 18.4% of the time against 21.1% for coin flips. The long
   runs that make left-only rigidity hard (§7) come only from rare special columns 1, which exhaustive search finds
   and sampling never meets.
3. **Both is neither random nor merely cut short.** Runs of 12 to 14 are three to seven times *more* common than for
   coin flips, and they come at quantised lengths. The longest run is exactly 12 (0.93% of right halves) or exactly
   14 (1.19%); never 13, almost never 11, and never more than 14 in 100,000 random right halves at this depth. Trace
   0001… shows the same signature: exactly 11 in 2.1% of right halves, then almost nothing beyond 12.
4. **Pre-registered F2 is refuted.** I predicted that the right side matters only in the extreme tail. It reshapes the
   middle of the distribution too.

So all the structure lives in the **interaction**. Neither side alone does anything unusual: the right side alone
changes nothing, and the left side alone is close to random. Together they produce the quantised run lengths and the
short ceiling. Those run lengths are a fingerprint of specific structure. Finding what makes runs of exactly 12 and
14 (the 7- and 14-ring orbits of §5 are the first suspects) is the next step.

**Is pseudorandom enough?** (The owner's question.) The record runs and the bounds in §5 to §8 use no randomness:
they enumerate every case. Only this section samples. Sampling needs representative choices, not unpredictable ones;
unpredictability is what cryptography needs, and what Cloudflare's lava-lamp wall supplies. Fixed seeds also let
Local re-run the exact numbers. One worry is real: Python's Mersenne Twister is linear over the same arithmetic as
Rule 30. So control F4 re-ran every arm with the operating system's entropy source, which is non-linear and unseeded.
Across all 152 comparisons the largest disagreement was 3.43 standard errors, in the coin-flip arm, which is ordinary
sampling noise: **F4 held** (`rule30_factorial_compare.py`).

### 8.2 Why runs of 13 were missing: templates, and where Fibonacci really is (2026-10-04)

The owner asked what makes 13 special, noting that 13 is prime and a Fibonacci number. The short answer: 13 itself
is not special. Each phase of the trace has a hole in its run lengths, and the hole is at 13 for one phase and at 15
for the other. The Fibonacci numbers, and 13 among them, do turn up, but somewhere else: in the counting of Lemma 3's
two rules. All numbers in this section come from `rule30_runlengths.py`. It runs every right half up to 18 cells,
depth up to 192, and the same number of random columns 1 for "left alone".

**The hole moves with the phase.** Zero runs in the forced left half, by length:

| Run length | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 20 |
|---|---|---|---|---|---|---|---|---|---|---|
| trace 0101…, both sides | 9,382 | 4,551 | 3,240 | **239** | 3,207 | 1,830 | 42 | 15 | 0 | 37 |
| trace 0101…, left alone | 11,284 | 5,719 | 2,777 | 1,354 | 681 | 337 | 193 | 110 | 44 | 16 |
| trace 1010…, both sides | 7,716 | 4,907 | 3,054 | 1,988 | 3,497 | **118** | 3,203 | 0 | 38 | 0 |
| trace 1010…, left alone | 11,281 | 5,477 | 2,968 | 1,396 | 752 | 381 | 158 | 83 | 55 | 9 |

With column 1 random (left alone), each extra cell halves the count, as for coin flips. With both sides exact, the
counts have peaks and holes. The two traces are the same word one time step apart (Lemma 2). The hole is at 13 for
0101… and at 15 for 1010…, so it is a property of the phase, not of the number 13.

**Long runs come from a few templates.** For every run of 11 to 20 cells, the probe records the 10 cells on either
side:

- For 0101…, the ten cells `1010001011` precede 98% of the runs of 14 and 76% of the runs of 12. One template opens
  the run, and the run closes after 12 cells or after 14 cells. Most runs of 15 sit in one other surrounding
  (`1000100101`, 95%). The runs of 13 are scattered: their two commonest surroundings cover only 34%.
- For 1010…, the ten cells `1000111101` precede 91% of the runs of 14 and 99% of the runs of 16. The runs of 15 are
  scattered over 13 surroundings, and the two commonest cover 50%.

**The end of a long run is pinned to one parity.** The depth of the run's last zero, even against odd:

| Run length | 12 | 13 | 14 | 15 | 16 | 17 | 20 |
|---|---|---|---|---|---|---|---|
| trace 0101…, last zero at even / odd depth | 2,775 / 465 | 131 / 108 | 3,184 / 23 | 1,813 / 17 | 42 / 0 | 15 / 0 | 37 / 0 |
| trace 1010…, last zero at even / odd depth | 168 / 2,886 | 404 / 1,584 | 86 / 3,411 | 20 / 98 | 0 / 3,203 | 0 / 0 | 0 / 0 |

For 0101…, 99% of the runs of 14 or more end at even depth, and all 94 runs of 16 or more do. For 1010…, 98% of the
runs of 14 or more end at odd depth. A template opens at a fixed parity of depth, and its runs end at a fixed parity
too, so the lengths from one template step by 2: 12 or 14, never 13. The other template, at the other parity, closes
at 15. A run of 13 would need that template to close two cells early, or a third template, and neither is common.
That is the whole of the "missing 13". For 1010… the roles shift by one: the main template closes at 14 or 16, a
second one (`1011111011`, 76% of the runs of 13) closes at 13, and 15 is the hole. (The parity table was added to
the probe after an ad-hoc look had shown it, so it is a recorded measurement, not a blind test.)

**Lemma 4 (the newest bit of column 1 enters once, as an XOR).** Write $L(k)$ for the cell at depth $k$ of the
forced left half (column $-k$ at time 0). It depends on $\sigma(0), \dots, \sigma(k-1)$ only, and on the newest of
them like this:

```math
L(k) = \begin{cases}
\sigma(k-1) \oplus g_k\big(\sigma(0), \dots, \sigma(k-2)\big) & \text{if } \tau(k-1) = 0 \quad \text{(a linear cell)},\\[2pt]
h_k\big(\sigma(0), \dots, \sigma(k-2)\big) & \text{if } \tau(k-1) = 1 \quad \text{(a forced cell)}.
\end{cases}
```

*Proof.* Rule 30 run to the left is $x(i-1, t) = x(i, t+1) \oplus \big(x(i, t) \vee x(i+1, t)\big)$. By induction,
column $-m$ at time $t$ depends on $\sigma(t), \dots, \sigma(t+m-1)$, and the newest of these enters only through
the term $x(-m+1, t+1)$, as an XOR. Unwinding $L(k) = x(-k, 0)$ this way down to column $-1$ at time $k-1$ leaves
$x(-1, k-1) = \tau(k) \oplus \big(\tau(k-1) \vee \sigma(k-1)\big)$. That is $\tau(k) \oplus \sigma(k-1)$ when
$\tau(k-1) = 0$, and it does not involve $\sigma(k-1)$ when $\tau(k-1) = 1$. $\square$ *Checked:* P2 in
`rule30_linear_cell.py` (7 words, 50 random columns 1, every depth to 192: no violation; the counterfactual "the flip
changes only $L(k)$" is caught). Lemma 1 comes out of the same unwinding: column 1 reaches the left half only through
column $-1$, and $x(-1, t) = \tau(t+1) \oplus \big(\tau(t) \vee \sigma(t)\big)$ ignores $\sigma(t)$ wherever
$\tau(t) = 1$.

What Lemma 4 says about the two arms:

- **Left alone.** With column 1 free, each linear cell can be set to 0 by its own bit. A run then lasts as long as the
  forced cells happen to be 0, which is why the left side alone allows such long runs (§7).
- **Both.** With column 1 made by a finite right half, the bits are fixed in advance. A run continues only while, at
  every linear cell, the right side's bit equals the left side's demand $g_k$, and the forced cells stay 0. So the
  weak form of B reads: *a column 1 made by a finite right half never meets the left side's demands forever.*

For 0101…, the linear cells are the odd depths. A run that ends because a right-side bit missed its demand ends with
a 1 at odd depth, and so its last zero is at even depth, as the parity table shows for 99% of the longest runs. I
predicted, before the run, that this generalises: for five other words, at least 90% of the two-sided zero runs of 10
or more would end at a linear cell (P3). **Refuted for all five:**

| Word | 001 | 011 | 0001 | 0011 | 0111 | 01 (not blind) | 10 (not blind) |
|---|---|---|---|---|---|---|---|
| Runs of 10 or more ending at a linear cell | 85.4% | 24.2% | 82.4% | 30.6% | 26.4% | 77.5% | 71.1% |
| Share of linear cells in the word | 67% | 33% | 75% | 50% | 25% | 50% | 50% |

Words with a single 1 lean towards ending at linear cells; 011 and 0011 lean the other way, ending mostly at forced
cells. So the pinned parity of 0101… is a property of that word, and the explanation above covers only that word:
Lemma 4 says where the right side's bit enters, not where runs end. Why the forced cells inside a long run of 0101…
stay 0 is open.

**Where Fibonacci really is.** Lemma 3's two rules, for the trace 0101…, read on the pairs
$\big(\sigma(2s), \sigma(2s+1)\big)$ of column 1: the pair $10$ is forbidden, and a pair ending in 1 cannot be
followed by a pair starting with 1. So the pairs are $00$, $01$, $11$. Let $a_m$, $b_m$, $c_m$ count the allowed
sequences of $m$ pairs ending in $00$, $01$, $11$, and let $S(m) = a_m + b_m + c_m$. A pair $00$ or $01$ may follow
anything, and a pair $11$ only a pair ending in 0. So

```math
a_{m+1} = b_{m+1} = S(m), \qquad c_{m+1} = a_m = S(m-1),
```

```math
S(m+1) = 2\,S(m) + S(m-1), \qquad S(0) = 1, \quad S(1) = 3 .
```

These are the half-companion Pell numbers: 3, 7, 17, 41, 99, 239, 577, 1393, …, and they are exactly the row
"allowed by Lemma 3's two rules" in §8's table (17, 99 and 577 at lengths 6, 10 and 14, and 8,119 at length 20).
The left side sees column 1 only at the zero times (Lemma 1), $e(s) = \sigma(2s)$. There, $e(s) = 1$ forces the pair
$11$ and then $e(s+1) = 0$. Every word with no two 1s in a row extends to an allowed column 1: choose
$\sigma(2s+1) = 1$ after $e(s) = 1$ and $\sigma(2s+1) = 0$ before $e(s+1) = 1$, which never conflict. So the visible
words are exactly those with no two 1s in a row, and their number is a Fibonacci number:

```math
\#\{\, e \in \{0,1\}^m : e \text{ has no } 11 \,\} \;=\; F(m+2), \qquad F(1) = F(2) = 1 .
```

For $m = 5$ that is $F(7) = 13$. $\square$ *Checked:* P1 in `rule30_runlengths.py`, against brute force for
$m = 1$ to $8$ (both counts).

So 13 appears twice in this work, for unrelated reasons. As a Fibonacci number, it counts what Lemma 3's two rules
allow the left side to see over 10 steps. As a missing run length, it is the length between one template's two
closings. The Fibonacci envelope is far looser than the truth (86 sequences against 8,119 at length 20), and T4
showed that the envelope alone does not bound the runs. The runs are set by the exact language.

**Next.** Name the templates. Lemma 4 answers half of the question that was here. For 0101…, 86% of the runs of 12
end with a 1 at a linear cell, so for most of them a closing at 12 rather than 14 is one bit of column 1 missing its
demand. The other half is the right side's: which right halves produce the
template, and what in them decides that bit. If every long run passes through a template that the right side can
only extend in a few ways, the weak form of B ("every run ends") becomes a statement about a growing but describable
family. Then the X3 runs of 24 and 26 should show up as later members of the same family.

### 8.3 What was already known, Rule 30's siblings, and the owner's harmonics (2026-10-04)

**What was already known.** Before taking the next step, the field was surveyed (PRIOR-ART.md, "Before rung 2's
leap"). Several of this project's results had been reached independently:

| Here | Already known as |
|---|---|
| The forced left half (§5) | Condrey's Lemma 1, "triangular uniqueness" (arXiv:2609.09431) |
| No constant bound for period two (X3, §8) | Condrey's conclusion: "At p=2 no bounded law can exist"; it uses a different statistic, but the fact is of the same kind |
| Conjecture B, weak form (§8) | The "remaining inference" named by public period-two work (a bounded search to support radius 14) |
| Rung 1's search (§5) | That bounded search; ours covers more (right halves to 18 cells, depth 256) |

The survey found none of these anywhere: the two-sided measurements, the four arms, Lemmas 3 and 4, and the
templates. It also brought in Rowland's "local restart": at row $2^n$ part of the starting row reappears and Rule 30
"begins again" locally, because its right diagonals have periods $2^\alpha$.

**The siblings (the random-chaos step).** The memory file asks for one step the plan did not call for. Rung 1 found no
counterexample in 27 million cases, but a search that finds nothing must be shown able to find something. Rule 30 is
$x' = l \oplus (c \vee r)$, and there are 16 rules of the form $x' = l \oplus g(c, r)$, all with the same left inverse.
`rule30_siblings.py` runs the instrument unchanged on all 16, with every right half up to 14 cells and depth 128. A
witness found by the inverse construction is confirmed by running the finite row forward. The instrument passes
three checks:
- Rule 30 has no witness.
- Rule 60 ($g = c$) has the known one: a single 1 at depth 1.
- For every rule, the forced left half, run forward, reproduces the trace (0 mismatches).

Of the 8 rules that keep the empty row empty:

| Rule | $g(c, r)$ | Witnesses, traces 01 / 10 | Longest zero run, 01 / 10 |
|---|---|---|---|
| 60 | $c$ | every right half / every right half | – |
| 30 | $c \vee r$ | 0 / 0 | 17 / 16 |
| 90 | $r$ | 0 / 0 | 16 / 15 |
| 210 | $\bar c \wedge r$ | 0 / 0 | 16 / 15 |
| 150 | $c \oplus r$ | 0 / 0 | 14 / 14 |
| 120 | $c \wedge r$ | 0 / 0 | 9 / 10 |
| 180 | $c \wedge \bar r$ | 0 / 0 | 1 / 1 |
| 240 | $0$ | 0 / 0 | 1 / 1 |

I predicted that only Rule 30 and the shift (240) would be witness-free (S4). **Refuted:** every one of them is,
except Rule 60, the one rule whose left half ignores column 1. So, in this search, a period-two column never occurs
once the right side can reach the left half. Rule 30 shares that property with its siblings, and its run lengths are
much like those of Rule 90 and Rule 210.

**Proposition 5 (Rule 90 has no finite configuration with a period-two column).** Under Rule 90, $x' = l \oplus r$,
let a finite row have its support in $[-w, w]$. Then column 0 is 0 at time $2^n$ and at time $2^n + 1$ whenever
$2^n > w + 1$.

*Proof.* Rule 90 is linear, and a single 1 at position $j$ reaches $(0, t)$ with the value
$\binom{t}{(t-j)/2} \bmod 2$. By Lucas' theorem, $\binom{2^n}{k}$ is odd only for $k \in \{0, 2^n\}$, and
$\binom{2^n+1}{k}$ only for $k \in \{0, 1, 2^n, 2^n+1\}$. These need $|j| \in \{2^n - 1, 2^n, 2^n + 1\}$, outside the
support. $\square$

So column 0 is 0 infinitely often at even times and at odd times, and an eventually 2-periodic column has the word
00. *Checked:* `rule30_sibling_proofs.py` covers every row with $w \le 6$ and every $n \le 8$ (65,530 cases, no
violation). The counterfactual, the same claim at time $2^n + 2$, is caught. The proposition is almost certainly known
(Lucas' theorem on Rule 90 is classical), but tonight's survey did not find it stated. It is Rowland's restart in
its global form: at row $2^n$ Rule 90 holds two far-apart copies of the start, with nothing in between. It does not
transfer: under Rule 30, column 0 is not 0 at those times (false in 49,001 of the 65,530 cases). Rule 30's restart is
only local.

**The owner's harmonics.** The owner's lead: "the right side changes nothing alone, the left side alone is close to
random, and together they produce sharp, quantised behaviour ... this sounds very much like harmonics."
`rule30_harmonics.py` tested the first form of it, blind on five words of period 3 and 4: the interaction's structure
should sit at multiples of the trace's period $p$. **Refuted** for all five words (H1 and H2). The interaction is
real, 20 to 200 times the noise floor, but it peaks at a lag of 7 for all three words of period 4. That points to a
different kind of harmonic. Rule 30 on a ring of 7 cells has 4-cycles, and their columns are exactly 0001, 0011 and
0111. So the left half resonates with Rule 30's own ring orbits, not with $p$.

`rule30_resonance.py` (pre-registered, with a covariance that removes a flaw found in the first statistic) tested that
on 15 words not yet looked at. Largest excess covariance between the arms, at any lag 1 to 12:

| Words | Ring orbits with this column (rings up to 15 cells) | Largest excess covariance |
|---|---|---|
| 0001, 0011, 0111 | 7, 14 | **0.139, 0.191, 0.220, all at lag 7** |
| 01, 10 | 7, 14 | 0.027, 0.015 |
| 001, 011 | 12 | 0.023, 0.020 |
| 01011 | 5, 10, 15 | 0.020 (predicted strong at lag 5 or 10: **refuted**) |
| 00001, 01111 | 15 | 0.014, 0.025 |
| the other 3 words of period 5, and all 9 of period 6 | none | 0.012 to 0.043 (predicted weak: **held**, 12 of 12) |

The noise floor is 0.0007. So a word with no ring orbit never resonated (14 words; 00001 and 01111 have orbits only on
the 15-cell ring, beyond the lags measured). A ring orbit is not enough on its own, though: 01, 001, 011 and 01011 have
one and do not resonate at this statistic's sensitivity (the spectrum below finds 0101… ringing weakly). The strong
resonance is the 7-cell ring's 4-cycle, and only that.

**The owner's Fourier lead** (after Rowland's pyramid and triangle): "are we able to lean on ... the Fourier transform
here to find frequency spikes?" Yes. The covariance above is half of a Fourier pair, and the power spectrum is its
transform (Wiener–Khinchin). `rule30_spectrum.py` computes it from exact bit counts, with two controls that passed:
coin flips give a flat spectrum (within 0.021), and a planted 7-periodic signal shows its spike at 1/7. Three results:

- **The left half rings at sevenths.** For every word of period 4, the excess spectrum (both sides against left alone)
  is a harmonic series of the 7-cell ring: lines at 1/7, 2/7 and 3/7, with the 14-cell ring's 1/14, 3/14 and 5/14
  below them. The highest line is +2.4 for 0001 and 0011 and **+7.7 for 0111** (F0 held, 3 of 3). It was not blind: a
  dry run of the code at a tiny size had shown it. The spectrum also sees what the lag statistic missed: **0101…
  rings at sevenths too**, with its highest excess line at 2/7 (+0.52), and 1/7 and 3/7 present. That is about 15
  times weaker than 0111.
- **Column 1 is not made of octaves.** I predicted, blind, that column 1's spectrum for 0101… would show Rowland's
  powers of 2: at least three of its five highest spikes at multiples of 1/32. **Refuted**: one of five (1/4). For
  0001, column 1 is almost purely 4-periodic, a line at 1/4 of power 122 against 0.1 elsewhere. The right side nearly
  locks column 1 into the 7-ring's 4-cycle, and that is why period 4 resonates so strongly.
- **For 0101…, column 1 has a line of its own.** Its spectrum is dominated by a line at $f \approx 0.3036$ (power 65),
  with its mirror at $1/2 - f$. Multiplying by the alternating trace maps $f$ to $1/2 - f$.
  `rule30_spectrum_fine.py` pins the line at $f = 0.30365$ over 4096 steps; the strongest autocovariance lags are 10,
  20, 36 and 56. That is within 0.0001 of $17/56$, and it rules out $3/10$, $7/23$ and $4/13$. Whether it is exactly
  rational needs longer runs. It is not a ring orbit's line. Up to 18 cells, only the 7- and 14-cell rings have an
  orbit with a 0101… column, and there the next column has period 4.

What this means for the prize. **Period two resonates only weakly.** No ring up to 15 cells has a 2-cycle. The 7-ring
orbits that do hold a 0101… column need a 4-periodic column 1, and the right side does not supply one. Instead it
supplies a column 1 dominated by its own line near 17/56. That fits the period-two left halves being aperiodic (§6,
`rule30_rings.py`), and a proof for period two cannot rest on the left half settling into a ring orbit. The line near
17/56 is new and unexplained. If column 1 for 0101… is close to a rotation or substitution sequence with that
frequency, column 1 has a finite description after all. T6 ruled out only automata in base 2.

**A reformulation that the templates step will use.** Under Rule 30, a zero segment loses at most one cell from each
end per step. So a zero run of $n$ cells at time 0 is the base of a white triangle of height $\lceil n/2 \rceil$, and a
finite configuration is one whose forced spacetime contains an infinite white wedge on the left: its leftmost 1 moves
left exactly one cell per step. The weak form of B says the forced spacetime contains only finite white triangles on
the left. The templates are then the boundaries of the large triangles.

**Next.**
1. Identify column 1's line near 17/56 for 0101…: compare column 1 with rotation sequences of that frequency, and with
   substitution sequences. A finite description of column 1 would turn the weak form of B into a question about two
   finite descriptions.
2. Name the templates as triangle boundaries.
3. A sibling ladder, steps before the leap: prove period-two exclusion for Rules 180, 120, 210 and 150 without using
   linearity, and see which argument survives for Rule 30. Rule 210 is the most Rule 30-like (runs of 16 / 15).

### 8.4 Column 1 is a turning wheel: the owner's complex-number lead (2026-10-04)

The owner: "Anytime someone mentions rotation I think quaternions. Extending the number line with i has interesting
properties." The complex numbers were already doing the work. A spectral line at $f$ means the sequence follows a
point that turns by $f$ of a turn per step on the unit circle, $z(t) = e^{2\pi i f t}$. The mirror line at $1/2 - f$
is the trace's half-turn per step, $(-1)^t = e^{i\pi t}$, which is $i^2 = -1$ applied once per step. So the precise
question is whether column 1 is a **coding of a circle rotation**: is its bit at time $t$ decided by where $z(t)$ is?

`rule30_rotation.py` asks this directly. In each window of $w$ steps, the phase of the line at $f = 0.30365$ is read
from the complex amplitude $A = \sum_t s(t)\, e^{-2\pi i f t}$. Each step is then placed on the circle at
$\theta(t) = \big(f t + \arg A / 2\pi\big) \bmod 1$ (16 bins, with the parity of $t$), and column 1 is predicted by the
majority bit of its cell. The first run was void: its controls caught two bugs, a sign error in the phase and a
planted control that was not periodic. Both were fixed and the run repeated. Its prediction errors:

| | $w = 64$ | $w = 256$ | $w = 1024$ |
|---|---|---|---|
| column 1, trace 0101… | **0.082** | 0.185 | 0.269 |
| planted rotation coding, no bits flipped (the instrument's floor) | 0.049 | | 0.050 |
| planted rotation coding, 10% flipped | 0.140 | | 0.139 |
| coin flips | 0.431 | | |
| column 1 with the wrong frequency, $f = 0.27$ | 0.311 | | |

- **Locally, column 1 is a rotation coding.** Over 64 steps, only about 3% of its bits are off the rotation (0.082
  against the floor of 0.049). This beats a planted rotation with 10% of its bits flipped (R1 held).
- **Globally, the phase wanders.** The error grows with the window, while a planted rotation's does not (R2 held).
  The wheel turns at a steady rate but slips.
- **One control failed its threshold.** C1, the planted rotation with 10% flipped, missed its pre-set threshold by
  0.009 (0.139 against 0.13). The threshold was set too tight, and the calibration rows above show by how much. It is
  recorded as a failure, not moved.

**Every strong line is one wheel, its overtones, or a root of unity.** Column 1's 8 highest lines over 4096 steps:

| Line | What it is | Width |
|---|---|---|
| 0.3037 | the wheel, $f \approx 17/56$ | sharp (within 0.0001 of $17/56$) |
| 0.2500 | $i^t$: a quarter-turn per step, literally multiplication by $i$ | exact |
| 0.1963 | $1/2 - f$: the wheel times the trace's half-turn $(-1)^t$ | sharp |
| 0.2857 | $e^{2\pi i \cdot 2t/7}$: the 7-cell ring | exact |
| 0.3905 | the second overtone $2f$, folded | broadened |
| 0.1094, 0.1058, 0.1038 | the second overtone times the half-turn, $2f + 1/2$, folded | broadened, split |

The pre-registered R3 asked all 8 to sit within 0.0005 of a multiple of 1/56: **refuted**, 4 of 8. The misses are
exactly the overtones. When the phase wanders, an overtone of order $k$ is $k^2$ times broader than the wheel, so the
second overtone is the one to blur.

**Quaternions, honestly.** Every line found is a rotation of one complex plane: the wheel $e^{2\pi i f}$, and the
roots of unity $-1$, $i$ and $e^{2\pi i/7}$. They commute, so there is no second independent turn among the top
lines, no torus, and so far no need for quaternions. The quaternions' extra power is that rotations need not commute,
as in three dimensions. A single bit sequence cannot show that. If it appears anywhere here, it will be in the
two-dimensional spacetime, with space and time turning differently, and that is worth looking for.

**The right side next to column 0 is a rotating domain.** Of the 1,024 right halves up to 10 cells, 42 lock column 1
exactly:
- 28 lock it to period 4, the period of the 7-ring's 4-cycle. These are presumably the source of §5's 7-periodic
  tails (not checked here).
- 14 lock it to period 14.

The other 982 never lock. Their column 1 equals itself 56 steps later 81% of the time, against 39% and 40% at lags 55
and 57. The match fades with distance from column 0, from 0.81 in column 1 to 0.60 in column 6. So the generic right
side is a coherent wheel, 17 turns in 56 steps, that slowly loses phase. The locked cases are the exceptions.

**What it means for the prize.** This is the first candidate for a finite description of what the right side
supplies: *a rotation by $f$ with phase slips*, an approximately Sturmian sequence. T6 ruled out only automata in base
2. If the slips can be described (where they happen, and by how much the phase jumps), then the weak form of B
becomes a question about the left side's demands (Lemma 4) against a slipping wheel. Each run of zeros would be a
stretch where the wheel happens to meet the demands.

**Next.**
1. Track the phase over time. Do slips come as discrete jumps of a fixed size, perhaps $1/56$ of a turn, or as
   diffusion?
2. Read the left half's long runs against the wheel's phase. Do the templates of §8.2 sit at one phase?

### 8.5 The universal wheel (2026-10-04)

`rule30_wheel.py` looked at the wheel up close. It cut column 1 (trace 0101…, every right half up to 12 cells, 2048
steps) into windows of 56 steps. Its controls passed: a synthetic wheel with planted slips (every slip recovered as a
shift, one word found), Rule 30's own line (0.3036), and windows of 55 steps (0.0000 exact copies). Of 4,096 right
halves, 166 lock into an exact period; the other 3,930 were studied.

| Prediction (blind) | Result |
|---|---|
| Q1: at least 30% of windows are exact copies of the one before | **refuted**: 8.4%. The wheel is coherent, but rarely exact for a whole period |
| Q2: at least 70% of slips are shifts in time | **held**: 5,430 of 5,714 (95%). The commonest shifts, 16, 36, 52, 0, 30, 20, 40, 26 steps, are all even, in step with the trace |
| Q3: one domain word covers at least 90% of the exact stretches | **held**: 96.6%. There are only 2 words, and the second is the period-14 lock (see the correction below) |
| Q4: the long zero runs sit inside exact stretches | **refuted, the other way round**: 0 of 40, against a base rate of 39%. (Read at first as "long runs sit next to slips"; corrected in §8.9: early long runs come mostly from the wheel's formation) |
| S (the random-chaos step): the siblings 90, 120, 150, 210 do not turn this wheel | **held**: they sit at 1/2 or 1/3. The wheel is Rule 30's own |

**The wheel is exactly a circle rotation.** The universal word is

```math
U = 0001001101\;0001001101\;0001001101\;0001001101\;0001001101\;001101 ,
```

five blocks of 10 cells, each making 3 turns, and one block of 6 making 2: $5 \cdot 3 + 2 = 17$ turns in 56 steps.
That is how a rotation is spelt in the alphabet of its continued fraction,
$17/56 = [0; 3, 3, 2, 2]$, with convergents $1/3$, $3/10$, $7/23$, $17/56$. It is why lags 10 and 20 were so strong
(§8.3), and why $7/23$ was a near miss for the line. The exact statement, checked over all 56 points
(`rule30_wheel_left.py`, C3):

```math
\sigma_U(t) = 1 \iff (17\,t \bmod 56) \in
\begin{cases}
[43, 56) & t \text{ even},\\
[39, 56) \cup [0, 16) & t \text{ odd},
\end{cases}
```

one arc of the 56-point circle for each parity of $t$. In the owner's terms, column 1 is a point
$z(t) = e^{2\pi i \cdot 17 t / 56}$ turning around the circle, and the trace's half-turn $(-1)^t$ chooses which arc
lights it. The left side sees only the even times (Lemma 1). There the wheel is a single-arc coding of a rotation by
$17/28$, with 6 of the 28 points lit, and so it never shows two 1s in a row, as Lemma 3 requires. The rare second word
$U_2$ (3.4%) is not a simple rotation coding: it needs 4 arcs per parity.

*Correction (2026-10-05, found by `rule30_walls.py`).* $U_2$ is not a second wheel. Its least period is 14:
it is `00010011001101` four times, the period-14 lock read in a 56-step window. So there is one wheel, $U$, and two
locks, of periods 4 and 14. The 14-lock appears for a while in columns that are not locked for good, and that is
where $U_2$'s 3.4% of stretches came from. The results for $U_2$ below still stand as computed, but they are
results for the 14-lock.

**The left half under the pure wheel** (`rule30_wheel_left.py`). Clamp column 0 to 0101… and column 1 to $U$, both
exactly periodic. Then every forced column is 56-periodic in time, the pairs of columns move through a finite set,
and the forced left half is eventually periodic in depth. Its controls passed: the 7-ring's 4-cycle continues the
ring (period 7), and two zero columns give zero. Results, over all 28 phases of $U$:

| Depth searched | 192 | 1,000 | 10,000 | 200,000 |
|---|---|---|---|---|
| Longest zero run under the pure wheel $U$ | 5 to 10 | 5 to 14 | 10 to 17 | 14 to 23 |
| $\log_2$ of the depth (the law of coin flips) | 7.6 | 10.0 | 13.3 | 17.6 |

- W1 **held**: no phase of $U$ or $U_2$ gives an eventually zero left half within 200,000 depths. Under $U$ no pair of
  columns repeats there. Under $U_2$ the left half is exactly periodic, period $728 = 56 \cdot 13$, and its zero runs
  never exceed 9.
- W2 **refuted**: I predicted runs of at most 12 under the pure wheel. They reach 23 by depth 200,000. The first run of
  14 ends at depth 599 at the earliest, usually thousands, and the longest run grows like $\log_2$ of the depth, as for
  random bits.
- Together with Q4: **within the two-sided search's depth (192), the pure wheel gives runs of at most 10**. The
  two-sided runs of 14 to 20 found there come from where the wheel is not running cleanly: mostly from its formation,
  some from its slips (corrected in §8.9; first read as "next to slips"). Deep down,
  the wheel alone makes long runs too, slowly.

**What this means for the prize.** The right side's output now has a finite description to first order. It is a
universal wheel $U$, an exact coding of the rotation by 17/56, interrupted by slips that are, 95% of the time,
shifts in time. In this picture, conjecture B's weak form ("every two-sided run ends") splits into two questions:

1. **The pure wheel.** Is the left half forced by (0101…, $U$) never eventually zero? This is one deterministic orbit
   of a finite-state map, on pairs of 56-bit columns, so it is decidable in principle. No repeat within 200,000 depths
   means a long orbit, and W1 held throughout.
2. **The slips.** Can slips conspire to keep the left half at zero forever? 95% of slips are shifts in time, from an
   alphabet of at most 56 shifts (the commonest eight are all even). So, to first order, this is a question about a
   finite alphabet of moves.

Neither is a proof. But both are finite objects, and before this section the right side had no description at all.

**Next.**
1. Follow the pure-wheel orbit much further, and look for an invariant that keeps it away from (0, 0). Each step is
   a few 56-bit operations, so a compiled loop does about a billion a second. The orbit is sequential, so this is a
   Local CPU job, not a GPU one.
2. Catalogue the slips: which shifts follow which phases, and whether the slip sequence is itself simple.

### 8.6 Order in, noise out: the left side churns the wheel (2026-10-04)

The owner: "Does it hold that the left is still mostly random and the wheel churns the noise?" Under the pure wheel no
noise goes in. Columns 0 and 1 are exactly periodic, and the left half is a deterministic function of them. So the
question is whether the left side manufactures noise from a regular input. `rule30_churn.py` tested it, with every
prediction written first:

| | Coin flips | Left half under the pure wheel | The wheel $U$ itself |
|---|---|---|---|
| Block entropy, bits per cell, blocks of 12 | 0.9999 | **0.9999** | 0.3165 |
| Largest departure of the spectrum from flat | 0.041 | **0.034** | a line at 113 |
| Share of ones | 0.50 | **0.5000** | 0.41 |

- **N1 and N2 held.** Fed a perfectly regular wheel, the left side puts out a sequence that these tests cannot tell
  from coin flips, over 2.8 million cells. This is Rule 30 as a random-number generator, run sideways.
- **N3 held: the churn is an avalanche.** Flipping one bit of the wheel at an even time changes 50.5% of the next
  1,000 left cells. A flip at an odd time changes none, exactly as Lemma 1 requires (control C0).
- **The arms.** Block entropy for blocks of 8, within depth 192: coin flips 1.0000, left alone 0.9997, both sides
  exact **0.9971**. The pure-wheel row (0.9920) is not comparable here, because its 28 sequences give too few blocks
  (bias of about 0.004). Of the comparable arms, the real two-sided left half is the least random. Its order (the
  quantised runs and templates of §8.2) sits where the wheel is not running cleanly: its formation early on, its
  slips deeper down (§8.9).

So the answer is yes, with a twist: **order in, noise out**. The wheel is churned into noise. The slips, which are the
right side's own disorder, are where the left half shows structure, together with the wheel's formation (§8.9).

**What this does to the proof route.** It cuts both ways.
- **Bad news.** Proving that a pseudorandom stream never settles to all zeros is the same kind of problem as the prize
  itself. A random-looking left half has zero runs that grow like $\log_2$ of the depth, but are never infinite.
- **Good news.** The pure wheel's stream comes from a finite-state map on pairs of 56-bit columns,
  $F(b, c) = \big(c,\ \mathrm{rot}(c) \oplus (c \vee b)\big)$.
  Its orbit must end in a cycle, and $(0, 0)$ is a fixed point. If the cycle is found and it is not $(0, 0)$, then
  "the pure wheel's left half is never eventually zero" is a computed theorem. Anyone can re-check it from the tail
  and cycle lengths. `wheel_orbit.c` (Brent's algorithm, lead M2) does this. Its self-tests reproduce the Python
  results exactly, and it runs at about 470 million steps a second. It was run on all 28 phases, with O1 and O2
  pre-registered in its header.

*Correction (2026-10-05, §8.13): that this left half is never eventually zero is a special case of Jen's theorem
(Proposition 7), with a three-line proof. What Proposition 6 adds is the exact tail $\mu$ and period $\lambda$.*

**Proposition 6 (computed): the pure wheel cannot make a finite left half.** Let column 0 be 0101… and column 1 the
universal wheel $U$, at any of its 28 even phases. Then the forced left half is never eventually zero. The orbit of the
column pair enters a cycle after

```math
\mu = 32\,896\,298 \text{ steps}, \qquad \lambda = 15\,009\,104\,432 = 2^4 \cdot 7 \cdot 17 \cdot 1433 \cdot 5501 ,
```

and the cycle is not the zero fixed point. So the left half is eventually periodic in depth, with period dividing
$\lambda$, and it has infinitely many ones.

*Proof.* The certificate $(\mu, \lambda)$ was found by Brent's algorithm in about $4.7 \times 10^{10}$ steps per phase
(O1 and O2 held). It was then re-checked independently by plain stepping:
- the state after $\mu$ steps is not zero, and $\lambda$ further steps return to it;
- $\lambda / p$ steps do not return, for each prime $p$ of $\lambda$, so $\lambda$ is the exact period;
- the state after $\mu - 1$ steps is not on the cycle, so $\mu$ is minimal.

The verifier rejects false certificates (its counterfactuals). Every phase gives the same certificate, for a reason:
$F$ commutes with the rotation of time, which is a permutation of bits, and a rotation by 2 fixes the trace and moves
the wheel's phase by 2. So the 28 orbits are rotations of one, and one certificate settles them all. All 28 were run
anyway and agree. $\square$

Proposition 6 is not about a finite configuration: the pure wheel is an idealisation, a right side that never slips.
What it shows is that **the wheel alone cannot make the left half finite**. A finite configuration would need the
right side's slips to steer the left half to zero and keep it there.

**The random-chaos step: can any periodic column 1 kill the left half?** Conjecture LR (§7) says that no column 1 at
all, made by a right half or not, lets the forced left half become zero. For a periodic column 1 that is an exact
finite question. `periodic_kill.c` asked it of every word up to period 18 with column 0 = 0101…, and up to period
14 with column 0 = 0001… Its control, the zero trace with the zero column, is found as a kill, as it must be.

| Column 0 | Words | Kills | Decided | Undecided within $10^6$ steps |
|---|---|---|---|---|
| 0101…, periods 1–18 | 524,286 | **0** | 394,848 | 129,438 (all of period 17) |
| 0001…, periods 1–14 | 32,766 | **0** | 22,162 | 10,604 (periods 9, 11, 13) |

So **LR holds exactly for each of the 417,010 periodic columns 1 that were decided** (K1 and K2 held as worded). The
undecided ones are not settled. Their orbits are longer than the budget, and the same rotation symmetry cuts the
129,438 words of period 17 to about 7,600 classes.

**Job M2 (Local ran it, 2026-10-05, on the M5, 12 minutes): one word per rotation class, a budget of $10^9$ steps.**

| Column 0 | Period | Classes | Words decided | Undecided within $10^9$ | Kills | Longest cycle |
|---|---|---|---|---|---|---|
| 0101… | 17 | 7,712 | 131,072 (all) | 0 | **0** | 5,224,661 |
| 0001… | 9 | 60 | 512 (all) | 0 | **0** | 3,602,016 |
| 0001… | 11 | 188 | 2,048 (all) | 0 | **0** | 18,702,068 |
| 0001… | 13 | 632 | 1,341 | 6,851 (527 classes) | **0** | 452,150,348 |

**K3 held:** every word of period 17 with column 0 = 0101… is decided, and none kills. **K4 is half refuted:** no
class kills, but only 3,753 of the 10,604 words decided (35.4%; 331 of 858 classes), against the 99% predicted. The
whole shortfall is at period 13 with column 0 = 0001… (P = 52), where the orbits outrun $10^9$ steps. That is a limit
of the budget, not a result. In all, **LR holds exactly for each of the 550,201 periodic columns 1 now decided**, and
6,851 words (527 classes, all at that one period) remain open.

*Correction (2026-10-05, §8.13): none of this was open. Jen's theorem (Proposition 7) proves that no eventually
periodic column 1 kills the left half, next to any periodic column 0 other than zero. The 6,851 undecided words are
settled by it. The search is a check of the instrument against a theorem: it found 0 kills, as it had to.*

**The wheel out of step** (the random-chaos step of 2026-10-05, prediction O3 in `wheel_orbit.c`). Delay $U$ by an
odd number of steps and it breaks Lemma 3, so no right half can make it. Conjecture LR still covers it. **O3 held:**
the orbit cycles after $\mu = 276\,594\,382$ steps, with $\lambda = 363\,832 = 2^3 \cdot 7 \cdot 73 \cdot 89$, and the
cycle is not zero (phases 1 and 3 agree). On that cycle both columns have period 28 in time, and $\lambda$ is exactly
the longest cycle the kill search found for trace 0001… at periods 7 and 14. Different starting points fall into
the same cycles of $F$. So LR survives even a wheel that no right side could produce. (Jen's theorem, §8.13, covers
this case too, since it never uses a right side.) (The certificate's verifier now
factors $\lambda$ itself, after a composite was passed to it as a prime; both certificates were re-verified.)

**Where this leaves the proof.** The route now has three parts. The first is measured, the second is done, and
the third is open:
1. **The right side is a wheel with slips.** This is §8.5, measured on every right half up to 12 cells. It is not yet
   proved.
2. **The wheel alone cannot make a finite left half.** This is Proposition 6, computed and verified. (It is also
   a special case of Jen's theorem, §8.13.)
3. **The slips cannot conspire to.** This is open. A heuristic says why it should hold. A right half of $W$ cells
   carries $W$ bits, while a zero run of $n$ cells needs about $n/2$ coincidences at the linear cells (Lemma 4). So the
   longest run should grow like the width plus a logarithm of the depth, and never become infinite. The measured runs
   (24 at width 24, X3) fit that budget. Turning the heuristic into a proof needs the slips' own structure, which is
   the next target.

### 8.7 A slip is one particle (2026-10-05)

Part 3 of the route asks whether the slips can conspire, which first needs to know what a slip is.
`rule30_slips.py` builds the domain (columns 0 to 6, the wheel's full spacetime pattern) from one set of right halves,
and tests it on another. Then it records each of the 22,937 slips it finds there: where the departure from the
domain first reaches each column, and the pattern of departures around the moment it reaches column 1.

| Check or prediction | Result |
|---|---|
| C: the domain, built on the training set, describes the test set | **passed**, 98.6% |
| CF1: fronts from the left are rare (the direction is not the detector's) | **passed**, 0 of 22,937 |
| CF2: no fronts inside long exact stretches (noise) | **failed, vacuously**: 0 of 0, because exact windows rarely come five in a row |
| P1: a slip is a front from the right, at about half a cell per step | **refuted as operationalised**, 0 of 22,937 (see below) |
| P2: at most 10 shapes cover 80% of slips | **held**: 4 shapes cover 96.7% |
| P3: the shape decides the phase shift | **refuted**: the commonest shift within a shape is 28% to 43% |

The commonest shape, covering 19,259 slips (84%), shows the domain's columns 1 to 6, left to right, over the 12 steps
from 8 before the departure reaches column 1 to 3 after it (`#` = off the domain):

```
....#.     t1 - 8
.....#
....##
...#..
..#.#.
...###
..#.##
.#.#.#
#.##..     t1: the departure reaches column 1
.#..#.
.##..#
######     t1 + 3
```

The departure enters from the interior and moves left diagonally, from column 5 to column 1 in 8 steps. It zigzags,
3 then 1 steps between columns, about half a cell per step on average, in step with the trace's two-step rhythm. P1
failed on a technicality: column 6 departs one step after column 5, so the strict order over six columns, as I wrote
it, never held. The picture is what P1 meant, but the prediction as written is refuted and is recorded so. Of the other
three shapes, one differs from this in a single cell and one in a few. **So a slip is essentially one kind of
particle**, a single defect in the wheel's domain that travels in from the right and reaches column 0.

This is computational mechanics, reached independently. Hanson and Crutchfield ("Computational mechanics of cellular
automata: an example", *Physica D* 103, 1997, on Rule 54) find a dominant regular domain, build a *domain filter* to
locate defects, and identify the particles and their interactions. Our departure-from-$D$ pattern is their domain
filter, with the wheel as the domain. Their method is the one to borrow for the particle's interactions
(PRIOR-ART.md).

P3's refutation says the phase after a slip is not set by the first particle alone. Presumably more particles
arrive before the wheel locks again, so a slip episode is a train of particles.

**What this means for the route.** Part 3, "can the slips conspire", becomes a question about one particle: when it
arrives, and how a train of arrivals moves the wheel's phase. That is a much smaller object than "anything the right
side might do".

**Next.**
1. Extract the particle exactly, as cell values rather than departures: its own period, its velocity over more
   columns, and whether it is the same pattern every time (a glider of the system with column 0 clamped).
2. A fixed noise control (CF2) and a cleaner speed test, with arrival defined from the particle's pattern.
3. The particle trains: the shift after a whole episode, as a function of the arrival times.

### 8.8 The walls kick the wheel in notches; orbits and jumps (2026-10-05)

`rule30_walls.py` looked at the particle as a domain wall. It built the domain in columns 0 to 12 from a training set
of right halves and tested it on another, imaging the 11,437 test slips aligned at their arrival. That arrival time
is $t_1$, when the wall reaches column 1.

| Check or prediction | Result |
|---|---|
| CF: aligned at random times inside exact windows, no cell reaches 50% (the noise control §8.7 lacked) | **passed**: at most 21.5% |
| V1 (seen first, recorded as a check): the wall moves at half a cell per step | **held**: slope $-2.19$ steps per column, columns 1 to 10 |
| L1 (seen first): two arrival phases hold at least 90% of slips | **held**: 98.1%, at wheel phases 32 and 52 |
| B1: each arrival class carries one shift | **refuted**: 57% and 36% (but where the shift matches, the wheel behind the wall fits exactly) |
| B2: the walls' shifts add up to an episode's shift | **refuted**: 4.9% |
| S, the random-chaos step: another trace turns a wheel of its own | **refuted** (below) |
| E1 and E2, the owner's orbit tangent | **refuted, informatively** (below) |

**The wall is a sharp object.** Its front runs from column 10, 19 steps before $t_1$, to column 1 at $t_1$, at half a
cell per step. It reaches column 1 at only two phases of the wheel's 56-step cycle. Behind it is the wheel again,
exactly, at a new phase.

**The walls kick the wheel's angle in notches.** B1 failed because the shift within a class is not fixed. The shifts
differ by multiples of 10 steps, the wheel's block. A delay of $\Delta$ steps turns the wheel's angle by
$-17\Delta/56$ of a turn, and in those terms every kick is a whole number of notches of $1/28$ of a turn:

| Wall class (arrival phase) | Kicks to the angle, notches of $1/28$ turn (training slips) |
|---|---|
| 32 | **+3** (561), +4 (227), +5 (124), +2 (54), +6 (47) |
| 42 (rare) | +2 (27), +3 (12), +1 (1) |
| 52 | **−3** (278), −5 (226), −1 (162), −4 (68), −6 (61) |

So there are **two species of wall: one pushes the wheel's angle forward, the other pulls it back**, each by a small
whole number of notches. The arrival phase fixes the sign. Something not yet seen, presumably the wall's width,
fixes the size. All kicks are even multiples of $1/56$, so the wheel's phase keeps its parity, in step with the
trace. Its angle moves on the 28 notches of one parity.

**The owner's tangent: "electron orbits, and how electrons jump between orbits. Is the wheel fixed, or can its size
vary?"** The orbits are discrete. Next to column 0, column 1 settles into one of three:
- the wheel $U$ (56 steps, 17 turns);
- the 4-lock (the 7-cell ring's cycle);
- the 14-lock.

Its size does not vary continuously. The jumps between them, counted over every 56-step window of column 1 for all
right halves up to 11 cells (50,650 wheel windows, 2,004 of the 14-lock, 1,948 of the 4-lock), are:

| Jump | Count |
|---|---|
| 14-lock → wheel | **193** |
| 4-lock → wheel | 1 |
| wheel → either lock | **0** |

E1 had predicted jumps both ways and is refuted. The jumps go one way: the locks behave like **metastable excited
orbits that decay to the wheel, the ground state**, and nothing re-excites them. E2 (the locks never release) fails
on that single 4-lock decay. Within the wheel itself the angle does jump in quanta: the walls' notches above. So the
analogy fits twice over, once for the size of the orbit and once for its phase.

**A correction** (found here): the second domain word $U_2$ of §8.5 has least period 14. It is
`00010011001101` four times, the 14-lock, not a second wheel. The classifier tested for $U_2$ before the 14-lock, so
every 14-lock window above was counted as $U_2$. §8.5 and the probe headers say so now.

**The random-chaos step: a census of wheels.** Column 1's highest spectral line, for ten traces. For 0101… it is the
wheel at 0.3036. For every other trace it is a multiple of the trace's own frequency: 001 and 011 at 1/3, 0011 at
1/4, 00011 at 1/5, 00101 at 2/5, 0111 and 000111 at 1/2. Traces 0 and 1 show no line. So **only the alternating
trace turns a wheel of its own**: with every other trace tried, the right side mainly follows the drive. That is only
the highest line, so it is a hint, not a theorem. But it fits period two being the open case that Condrey named and
that public work is stuck on.

**What this means for the route.** Part 3 now has a finite alphabet. The right side's output, column 1, is the wheel
$U$, whose angle is kicked by whole notches ($\pm 1$ to $\pm 6$ of $1/28$ turn) as walls of two species arrive at two
fixed phases. A finite configuration would need those kicks to steer the left half to zero and keep it there.

**Next.**
1. What sets a wall's size: its width, or the gap to the next wall?
2. The left half's response to a single kick. Deep long runs sit in slip episodes (§8.9), so is a long run the left
   side's echo of one kick, of a given size and sign?
3. The kick game. Within the two-sided search's depth, can any sequence of kicks from this alphabet hold the left half
   at zero longer than the runs seen? If the alphabet's best is bounded, the heuristic of §8.6 has a finite form.

### 8.9 Where the long runs come from, and kicking the drive (2026-10-05)

**A correction first.** Sections 8.5, 8.6 and 8.8 said "the long zero runs sit next to slips". That came from Q4 of
`rule30_wheel.py`, and it over-read it. Q4 showed only that no run of 14 or more lies wholly inside a stretch where
the wheel runs exactly. An exploratory look found that most of the early long runs come instead from the wheel's
*formation*, the transient before it first locks. `rule30_formation.py` makes that a measurement:

| Runs | Before the wheel forms | In a slip episode | Overlapping an exact window |
|---|---|---|---|
| 14 or more, depth up to 192, right halves up to 12 cells (F1, seen first) | **51** | 20 | 16 |
| 16 or more, depth up to 384, right halves up to 13 cells (F2, blind) | 0 | **6** | 1 |

So the early long runs (within the first two or three windows) come from the wheel forming, and the deep ones from its
slips. Both held, and the three sections above now say so.

**What does not set a kick.** Over 10,994 slips, the gap since the previous slip does not fix the kick: the commonest
kick at any gap is at most 32% (N, recorded as seen). What fixes a kick's size is still unknown.

**The random-chaos step: kick the drive.** Column 0 runs 0101… with one bit flipped at step 503, inside the wheel's
coherent running. The causality control passed: nothing changes before the glitch, and every right half feels it
after.

| Prediction | Result |
|---|---|
| G1: the wheel is exact again within 10 windows in at least 90% of right halves | **refuted, narrowly**: 2,566 of 2,886 (88.9%) |
| G2: in at least half of those, it returns at the phase it would have had without the glitch | **refuted**: 91 of 2,566 (3.5%) |

The wheel re-forms after a glitch, but almost never at its old phase. It keeps a lasting kick of many sizes, from −9 to
+11 notches (+6 in 100 cases, +5 in 84, −9 in 82, +3 in 81, +11 in 79, ...), a wider range than the walls give. **The
wheel's phase has no restoring force.** Any phase is as good as any other, so a knock moves it for good, like a free
rotor's angle. That fits the walls' kicks adding up as a walk of the angle, with nothing pulling it back.

**What this means for the route.** The left side's demands (Lemma 4) are met by the wheel at a given phase, and the
phase drifts by kicks and is never restored. A finite configuration would need that walk to land the left half on zero
and keep it there. The early long runs show the most dangerous moment is the wheel's formation. A proof attempt should
look there first: at the first few windows, while column 1 is still settling, and not deep down.

**Next.**
1. The formation transient: how the wheel forms from a finite right half, and whether it, rather than the slips, is
   what bounds the early runs.
2. The kick game, now with the formation transient included.

### 8.10 Does the wheel turn at a constant rate? (2026-10-05)

The owner's lead, from the motion-field work: "velocity, acceleration, jerk, snap, crackle ... A wheel may turn at a
non-constant rate." `rule30_wheelspeed.py` follows the wheel's angle through every exact window of column 1, for all
unlocked right halves up to 12 cells over 4096 steps. It adds up the walls' kicks between windows. Its control
passed: every phase change keeps the trace's parity, so every change is a whole number of notches.

| Prediction | Result |
|---|---|
| V0: the kicks' net drift reproduces the spectral line 0.30365 (an independent instrument) within 0.0001 | **refuted, narrowly**: the drift is −0.046 notches per window, a rotation number of 0.303542, 0.000108 from the line |
| A1: the wheel's mean speed changes with time (windows 2–10 against 40–70) | **held as worded, but not meaningful** |
| A2: the angle diffuses normally (variance grows as $L^g$, $g \in [0.8, 1.2]$) | **held**: $g = 1.16$, about 7 notches² per window |

What the wheel's motion is, in the motion-field vocabulary:
- **Velocity.** Exactly constant between kicks: 17/56 of a turn per step.
- **Acceleration.** Impulses. The velocity jumps by a whole number of notches as each wall arrives, and is constant
  again afterwards. The wheel is a constant-velocity rotor with impulsive kicks, so jerk, snap and crackle are
  derivatives of impulses and carry no new information.
- **The long-run picture.** The kicks make the angle diffuse, like a random walk, at about 7 notches² per window.
  Their net drift is tiny, under a tenth of a notch per window.

A1 "held" only as worded. The early and late means differ (−0.062 against −0.029 notches per window). But the window-by-
window speeds swing between −0.21 and +0.15, far more than that difference, and the prediction had no significance
test, so this is no evidence of a changing rate. The swings are themselves larger than independent right halves
would give (about ±0.04). That hints the walls are synchronised in time across right halves, which has not been
tested. V0's narrow refutation has two candidate causes, and which is right is open. A spectral peak need not sit at
the mean rate when kicks are asymmetric. And an angle change beyond ±14 notches across a long gap would be unwrapped
wrongly.

**What this means for the route.** The right side's output is now a jump-diffusion of one angle: steady rotation plus
notched kicks, with no restoring force (§8.9) and no evident trend. That is the simplest possible description of a
non-trivial column 1, and it is the object part 3 has to reason about.

### 8.11 Is the wheel chaotic? A flywheel kicked by a chaotic machine (2026-10-05)

The owner: "Could the wheel be chaotic, like a double pendulum?" A double pendulum is chaotic in its own variables:
two nearby starts part exponentially. `rule30_chaos.py` tested the wheel the same way. It flipped one cell, 48 places
out in a random right half of 64 cells, and followed both wheels. All predictions were written first:

| Test | Result |
|---|---|
| C, the light cone (exact): column 1 unchanged until the flip can reach it | **passed**: 0 of 1,500 pairs changed early |
| D1: the flip moves the wheel for good | **held**: 1,437 of 1,437 |
| D2: the two angles part diffusively, the squared gap growing as $s^g$ with $g \in [0.7, 1.3]$ | **held**: $g = 1.17$ |
| D3: the kicks have no memory | **held**: correlation $+0.14$; the previous kick leaves 95.6% of the next one's entropy |
| N1, the random-chaos step: replace the interior with coin flips at column 13 | **held**: the same wheel forms, more cleanly (60% of windows exact, against 8% with a real right half), kicked both ways |

So **the wheel is not a double pendulum.** Between kicks it is an exact rotation, and nearby wheels part only like a
random walk, because its angle has no restoring force (§8.9) and nothing amplifies a difference. It is a regular
flywheel kicked by a chaotic machine. The randomness is borrowed from Rule 30's interior, and N1 shows it can even be
replaced by plain coin flips without losing the wheel; only the kicks' statistics change. **The wheel belongs to the
thin layer next to column 0** (13 columns were enough). The interior is only a source of kicks.

**A ladder of statements, each about a finite machine.** N1 suggests treating the right side as a layer $m$ cells
wide, fed an arbitrary input at its edge. Given column 0 = 0101…, any start for cells $1, \dots, m$, and any sequence
in column $m+1$, the layer's columns $1, \dots, m$ follow, because information moves at most one cell per step. So
column 1 is the output of a finite-state transducer with $2^m$ states and one input bit per step. Define

> **$\mathrm{LR}_m$**: for every start of cells $1, \dots, m$ and every input sequence in column $m+1$, the forced left half is
> not eventually zero.

Then

```math
\mathrm{LR} = \mathrm{LR}_0 \;\Rightarrow\; \mathrm{LR}_1 \;\Rightarrow\; \mathrm{LR}_2 \;\Rightarrow\; \cdots \;\Rightarrow\;
\text{B (weak form): no finite right half makes the left half eventually zero.}
```

*Why each step holds.*
- **Outputs only shrink.** The column 1 a layer of width $m+1$ produces is one a layer of width $m$ also produces: feed
  it, as input, the column $m+1$ of the wider layer. So the outputs of $\mathrm{LR}_{m+1}$ are among those of $\mathrm{LR}_m$, and
  $\mathrm{LR}_m$ implies $\mathrm{LR}_{m+1}$.
- **The top step.** A finite right half supplies one particular start and one particular input sequence, so $\mathrm{LR}_m$
  for any single $m$ implies B.
- **The bottom step.** $\mathrm{LR}_0$, with no layer at all and column 1 arbitrary, is LR (§7). $\square$

For period two, B is what the prize needs (§8).

What the ladder buys is this. At $m = 0$ the left side faces any column 1 at all, and the zero runs grow with depth
(§7). With a real right half, the layer filters what reaches column 1 down to a wheel and its kicks, and the runs grow
only slowly (§8, X3). Somewhere up the ladder a finite layer must start to tame the left side. **Each rung is a
question about a finite automaton driving the left-permutive map**, the kind of object a finite computation, or a Lean
proof, can handle.

**Next.** The kick game, done properly as the ladder's first rungs. For small $m$, search adversarially over input
sequences for the longest zero run the left half can be held to from a given depth. At $m = 0$ this is §7's
exhaustive search. The question is how fast the best achievable run falls as $m$ grows, and whether it becomes
bounded at some finite $m$.

### 8.12 The ladder's first rungs: a thin layer tames the adversary (2026-10-05)

$R(m, s)$ is the longest run of zeros the forced left half can be held to, starting at depth $s$. It is taken over
every start of a width-$m$ layer next to column 0 = 0101… and every input sequence fed to the layer, however
adversarial. $m = 0$ means column 1 is free, the setting of conjecture LR. `ladder.c` computes $R$ exactly, and
Lemma 4 is what makes that possible. Inside a zero run every linear cell forces column 1's bit, so the left side's
state is fixed along the run. All that remains is which of the layer's $2^m$ states can still supply the demanded
bits: a breadth-first search over at most $2^m$ states per step. `rule30_ladder.py` checks the instrument and the
predictions:

| Check or prediction | Result |
|---|---|
| LS: the program's left-half recursion matches the column recursion | **passed**, 200 of 200 |
| LD1: $R(0, 33) = 33$, the exhaustive left-alone value of §7 | **passed** |
| LD2: $R$ never rises with $m$ (the ladder, §8.11) | **passed** |
| LD3: $R$ is at least what real right halves achieve | **passed** |
| LD4: some layer of width $m \le 10$ holds $R(m, 33) \le 24$ | **held**, from $m = 1$ |
| LD5: at $m = 8$ the run grows with $s$ at most half as fast as at $m = 0$ | **held**: it does not grow at all |
| LD6: no layer of width 1 or more holds the left half at zero to depth 126 | **held** |

| Layer width $m$ | $R(m, 17)$ | $R(m, 25)$ | $R(m, 33)$ | Visible column-1 prefixes at $s = 33$ |
|---|---|---|---|---|
| 0 (column 1 free) | 15 | 19 | **33** | 65,536 |
| 1 | 9 | 12 | 13 | 2,584 $= F(18)$ |
| 4 | 9 | 12 | 11 | 1,318 |
| 5, 6 | 9 | 10 | 9 | 699, 439 |
| 7, 8, 10 | 9 | 10 | **7** | 348, 341, 317 |
| real right halves, up to 12 cells | 9 | 10 | 6 | |

**What it shows.**
- **One cell of layer is enough to tame the adversary.** With column 1 free, the left half can be held at zero for 33
  cells from depth 33. With a single cell between column 0 and the adversary's input, at most 13. A width-1 layer
  imposes exactly Lemma 3's two rules, and the visible prefixes it allows number $F(18) = 2584$, the Fibonacci count
  of §8.2.
- **Wider layers are tighter still.** From $m = 7$ on, the worst input does almost no better than real right halves:
  7 against 6 from depth 33. The layer, not the right half's particular content, is what limits the runs.
  *(Correction, §8.14: true at depth 33 only. Deeper, the worst input reaches 20 to 25 against real right halves'
  6 to 10.)*
- **The visible language is tiny.** A layer of width 10 can produce only 317 of the 65,536 visible prefixes of 16
  bits.

**What it means for the prize.** If, for some fixed $m$, $R(m, s)$ stays bounded as $s$ grows, then no input to that
layer can make the left half eventually zero. That is $\mathrm{LR}_m$, and by the ladder it gives B, the period-two
case. Three values of $s$ cannot show that. The next step pushes $s$ as deep as the program allows.

### 8.13 Jen's theorem settles every periodic column 1: a correction (2026-10-05)

Reading Kopra's paper in full (PRIOR-ART.md) showed that §8.6's search for a periodic column 1 that kills the left
half was answered in 1990. Jen proved that two adjacent columns of a configuration whose left half is eventually zero
are never both eventually periodic. Kopra restates it as his Corollary 3.7, for every left-permutive rule in which a
lone 1 spreads to the left, and Rule 30 is one. The work had cited Jen in §5 but had not seen that the theorem decides
the periodic case of conjecture LR. Here it is in this document's notation. The proof needs only Rule 30's update
read in two directions.

**Proposition 7 (Jen).** Let column 0 be eventually periodic and not eventually zero, and let column 1 be any
eventually periodic sequence, made by a right half or not. Then the forced left half is never eventually zero.

*Proof.* Shift time so that both columns are exactly periodic from $t = 0$, with a common period $P$. (The row at the
new $t = 0$ still has an eventually zero left half, because the zeros far to the left stay zero for any finite time.)
Rule 30 read from right to left is

```math
x_t(k-1) = x_{t+1}(k) \oplus \big(x_t(k) \vee x_t(k+1)\big) .
```

1. **Periodicity moves left.** If columns $k$ and $k+1$ are $P$-periodic, the formula makes column $k - 1$
   $P$-periodic. Starting from columns 0 and 1, every column of the left half is $P$-periodic.
2. **Zeros stay zero for a while.** Suppose $x_0(k) = 0$ for every $k < -N$. A cell is 0 when all three cells above
   it are, so $x_t(k) = 0$ whenever $k < -N - t$. A column far enough left, $k < -N - P$, is therefore zero for
   $t = 0, \dots, P - 1$, and by step 1 it is zero for ever. So two adjacent columns are both zero for ever.
3. **Zeros move right.** If columns $k - 1$ and $k$ are both zero for ever, the formula reads
   $0 = 0 \oplus (0 \vee x_t(k+1))$, so column $k + 1$ is zero for ever too. Repeating, column 0 is zero, which it is
   not. $\square$

In plain words: periodicity flows to the left, the light cone makes the far left zero for one whole period, and a
zero pair of columns forces zeros back to the right, all the way to column 0.

**What this corrects.**
- **§8.6's periodic columns.** K1 to K4 and job M2 could never have found a kill. Their 550,201 decided words, and
  the 6,851 that M2 left undecided, are all settled by Proposition 7. The search was a check of the instrument
  against a theorem, and it passed: 0 kills. It was not new evidence. Lead M2's remainder in CLOUD-LOCAL.md is
  closed, with nothing to run.
- **Proposition 6.** "Not zero" is a special case. What the certificate adds is the left half's exact tail and period
  in depth, $\mu = 32\,896\,298$ and $\lambda = 15\,009\,104\,432$. The same holds for O3, the wheel out of step.
- **Part 2 of the route** (§8.6, "the wheel alone cannot make a finite left half") is Jen's theorem, not a new
  result.
- **The cost.** Local spent 12 minutes of a ten-core machine, and Cloud two runs, on a question with a known answer.
  The lesson goes into the workflow: before a computation is designed, check whether the theorems already listed in
  PRIOR-ART.md decide it.

**What it adds: the wheel must slip for ever.** Take a finite configuration with column 0 eventually 0101… Its left
half is eventually zero, so by Proposition 7 column 1 is not eventually periodic. The wheel $U$ is periodic, and so
are the 4- and 14-locks (§8.5), so column 1 can neither run as the clean wheel for ever nor settle into a lock.
**The wheel slips infinitely often, in every finite configuration with this trace.** The slips of §8.7 to §8.11 are not
an accident of the right halves sampled. They are forced. For the prize, everything now rests on part 3: whether
slips, which must occur for ever, can steer the left half to zero and keep it there.

**Why the proof stops at one column.** Step 1 needs two periodic columns to start from. With column 1 aperiodic it
has nothing to start from, and a far column that is zero for one period need not stay zero. Kopra marks the limit
himself (his page 7): his class of rules contains Rule 90, which from a single 1 has an eventually periodic single
column, so no argument that uses only the class's properties can settle one column. The prize's single column needs
something Rule 30 has and Rule 90 lacks, such as the nonlinearity behind Lemma 4.

### 8.14 At depth the runs keep growing: a zero run costs about one bit (2026-10-05)

`rule30_ladder_deep.py` pushed the ladder of §8.12 down to depth 105, with its predictions written first. The program
now keeps only the start groups a layer can actually produce, so the depth limit is 126 rather than the memory.

| $R(m, s)$ | $s = 41$ | 49 | 57 | 65 | 73 | 81 | 89 | 97 | 105 |
|---|---|---|---|---|---|---|---|---|---|
| $m = 0$ (column 1 free) | 37 | | | | | | | | |
| $m = 1$ | 15 | 21 | 25 | | | | | | |
| $m = 4$ | 14 | 15 | 19 | | | | | | |
| $m = 6$ | 11 | 11 | 14 | 17 | 20 | 20 | 21 | 25 | $\ge 22$ |
| $m = 8$ | 8 | 11 | 11 | 13 | 16 | 17 | 16 | 25 | 21 |
| $m = 10$ | 8 | 11 | 10 | 13 | 16 | 14 | 16 | 19 | 21 |
| $m = 12$ | 8 | 11 | 10 | 13 | 16 | 14 | 16 | 16 | 20 |
| real right halves, up to 12 cells | 6 | 9 | 10 | 10 | 8 | 8 | 9 | 9 | 10 |

| Check or prediction | Result |
|---|---|
| DL0: the new program reproduces §8.12's 30 values | **passed** |
| DL5: $R$ never rises with $m$, and is never below the real runs | **passed** |
| DL1: $R(8, s) \le 16$ for $s$ up to 105 | **refuted**: 25 at $s = 97$ |
| DL2: $R(10, s) \le 12$ | **refuted**: 21 at $s = 105$ |
| DL3: with column 1 free the runs keep growing, $R(0, 41) \ge 35$ | **held**: 37 |
| DL4: at $m = 12$ no growth with depth | **refuted**: 8 to 13 early, 14 to 20 late |

($R(6, 105)$ reached the depth limit, so it is a lower bound. Two of DL4's nine values were seen in a cost test
before the run; without them DL4 is still refuted.)

**What it shows.**
- **No rung is bounded, as far as computed.** At every width up to 12, the worst input holds the left half at zero for
  longer the deeper it starts, roughly in proportion to the depth. A wider layer slows the growth but does not stop it.
  So $\mathrm{LR}_m$ cannot be proved by a bound on the runs, at least for $m \le 12$. $\mathrm{LR}_m$ itself is not
  refuted: runs that are finite but unbounded are allowed, and none reached an infinite run.
- **The adversary beats real right halves at depth.** At depth 33 the gap was one cell (§8.12). By depth 105 it is
  10 to 15 cells.

**A reading, made after the run.** The number of start groups $G(m, s)$ (the visible prefixes of column 1 that the
layer can produce before depth $s$) grows exponentially with $s$. At $m = 6$ it grows by a factor of 3.40 every 8
depths, and at $m = 12$ by about 2.1. Across the whole table, for $m \ge 4$ and $s \ge 33$,

```math
R(m, s) \approx \log_2 G(m, s) ,
```

with the ratio between 0.81 and 1.26. With column 1 free the ratio is near 2. Lemma 4 explains the form, if not yet
the constant. Inside a zero run every visible bit of column 1 is forced, so the run is a deterministic function of
where it starts, and the adversary's only real choice is the start. A run survives a cell when the left side's forced
cell is 0, and, if a layer stands between column 0 and the input, when the layer can supply the demanded bit. If each
of these is a fair coin, a zero cell costs one bit, and the best of $G$ starts lasts about $\log_2 G$ cells. With
column 1 free the demanded bits cost nothing, so a cell costs half a bit. In short, **the adversary does no better
than chance**. Real right halves fit the same budget: 12 cells carry 12 bits, and their runs are 6 to 10 at every
depth computed.

**What it means for the prize.** This is the heuristic of §8.6, part 3, now measured on an adversary. A finite right
half carries finitely many bits, so its zero runs should be bounded by its width plus a logarithm of the depth, and an
eventually zero left half would need infinitely many bits. A proof would need the cost per cell to be bounded below
uniformly, a statement about pseudorandomness of the same kind as the prize itself. The reading is a hypothesis
until it survives a blind test. `rule30_ladder_budget.py` tests it at 26 points the deep run did not compute, through
the whole histogram of run lengths, against a simulated coin-flip null and against real right halves up to 16 cells.

**The blind test** (`rule30_ladder_budget.py`; 26 new points, layer widths up to 16):

| Check or prediction | Result |
|---|---|
| BL0: the histogram mode reproduces the deep run | **passed** |
| C2: the bands are wide enough for chance alone | **failed** at 2 of 26 points (shallow, $G \approx 1000$) |
| BL1: $R / \log_2 G$ in $[0.75, 1.35]$ for $m \ge 5$ | **held**: 0.78 to 1.28 at all 24 points |
| BL2: with column 1 free, $R / \log_2 G$ in $[1.5, 2.2]$ | **held**: 1.61 and 1.95 |
| BL3: the histogram's bulk loses 0.8 to 1.25 bits per cell ($m \ge 5$), 0.4 to 0.6 ($m = 0$) | **refuted**: 0.71 to 1.09; $m = 0$ as predicted |
| BL4: the start groups' entropy falls with $m$ and is still 0.15 to 0.28 at $m = 16$ | **held**: 0.51, 0.38, 0.32, 0.30, 0.26, **0.24** bits per visible bit |
| BL5: real right halves of $W$ cells reach at most $W + 3$, and 3 more cells from $W = 8$ to 16 | **refuted**: 9, 9, 10, 10, 11 |

- **The coin model holds for the longest run, roughly.** At every point $R$ is within about 25% of $\log_2 G$. The
  bulk of the histogram is a little cheaper than one bit per cell (about 0.75 at $m = 5$), and the far tail is steeper
  than the bulk. "About one bit per cell" is the honest summary; the constant is not exactly 1.
- **The adversary's freedom keeps shrinking with width, but has not vanished by $m = 16$.** If the entropy of the start
  groups went to zero as $m \to \infty$, runs would grow more slowly than the depth. That limit is the open quantity.
- **Real right halves are far poorer than the adversary.** Sixteen cells of right half hold the left half at zero for
  only 11 cells, at the depths tested, against 16 for the adversary at $m = 16$. Most of a real right half's bits do
  not reach column 1 when a run needs them. This failure of the coin model is in the proof's favour.
- **Where chance seemed to fail in the adversary's favour.** With column 1 free, the histograms show families of
  starts far beyond the coin tail. At depth 33, 21 starts hold the left half at zero for exactly 33 cells, while none
  last 25 to 31. At depth 45, 8 starts last 43 cells, while none last 35 to 41. *(Correction, §8.16: this was called
  "structure, not luck" here. It is luck. Each family is one left-side state counted many times, and coin flips over
  the distinct states give such a maximum about 14% of the time.)*

### 8.15 Rule 30 as a random-number generator: where its randomness fails (2026-10-05)

The owner asked about the remark that Rule 30 "exhibits poor behavior on a chi squared test when applied to all the
rule columns" (Sipper and Tomassini, 1996), and whether that ended the centre-column generator. It did not.
Mathematica used the centre column for random integers for years. The flaw is in using every column at once, and it
is visible in Rule 30's formula read from right to left:

```math
x_{t+1}(i) \oplus x_t(i-1) = x_t(i) \vee x_t(i+1) ,
```

which is 1 three times in four. Each column is its left neighbour's column, delayed one step, XORed with a mask that is
mostly ones. `rule30_prng.py` replicates Sipper and Tomassini's setup (a ring of 50 cells, 300 random starts, 4,096
steps, every cell a stream), with its predictions written first:

| Test | Result |
|---|---|
| One stream at a time: frequency, and blocks of 4 steps | **pass** (1.07% and 0.95% fail at the 1% level) |
| Two neighbouring streams: $x_{t+1}(i) = x_t(i-1)$ | **fails completely**: 25.00% of steps instead of 50%; every one of 15,000 pairs below $p = 10^{-10}$ |
| The same test for the linear Rules 90 and 150 | pass (50.02%, 50.00%) |
| The centre column alone, from a single 1 (Wolfram's way) | **pass** ($p = 0.73$); the flaw sits in the column beside it, which the user never reads |
| Bytes of 8 adjacent cells, every row of a run pooled | **fails** in 7% of runs. Each row determines the next, so the rows are not independent draws: with rows 32 steps apart, 0.3% (a pre-registered diagnostic) |

The prediction that whole rows would pass was refuted: the reasoning held for a single row, not for 4,096 dependent
ones. Which of the two flaws Sipper and Tomassini's test met is not known here, since their paper was not read.

**The real break was cryptographic, and it is this project's construction.** Meier and Staffelbach (1991) recovered
Wolfram's key from the centre column. The centre column and the column beside it force the whole left half, because
Rule 30 is left-permutive, and the column beside it can be guessed from the right half of the seed, which carries
little entropy. That is §5's forced left half and §8's right side as a constraint on column 1, 35 years earlier.
PRIOR-ART.md records it.

**What it says about the chaos.** Rule 30's randomness is real in one sense and an illusion in another. On the
infinite line it is chaotic in the strict sense: information from ever further away keeps arriving. From a single 1
there is no information at all to arrive. The pattern is fully determined, so its randomness can only be an
appearance, and the prize asks for proof that one particular appearance (non-periodicity) is never broken. Every
lever found so far is a place where the appearance fails:
- the identity above (two columns are tied; Lemma 3 and the forced left half);
- Lemma 1 (half of column 1 is invisible);
- the wheel (next to 0101…, column 1 is an exact rotation between kicks, §8.5);
- the notched kicks (§8.8);
- Jen's theorem (periodicity flows left, §8.13);
- the real right halves' poverty (§8.14).

A proof will be built from such failures, not from the chaos.

### 8.16 Luck, not structure; and a bottleneck, not a cost (2026-10-05)

Section 8.14 left two questions. `rule30_merge.py` answers both, with its predictions written first.

**The adversary's "families" are luck.** Different start groups can lead to the same left-side state (the pair of
anti-diagonals that fixes everything after depth $s$). The depth-33 family of 21 start groups is one state, and the
depth-45 family of 8 is another. Counting distinct states, the coin model fits closely at five depths not looked at
before:

| Depth $s$ | Start groups $G$ | Distinct states | States with a run $\ge 9$: observed, coin model | Longest run | Coin chance of a run that long |
|---|---|---|---|---|---|
| 35 | 131,072 | 17,771 | 1,141, 1,111 | 31 | 0.42 |
| 39 | 524,288 | 55,939 | 3,585, 3,496 | 31 | 0.82 |
| 43 | 2,097,152 | 175,164 | 11,127, 10,948 | 35 | 0.74 |
| 47 | 8,388,608 | 546,616 | 34,103, 34,164 | 41 | 0.41 |
| 49 | 16,777,216 | 965,204 | 60,745, 60,325 | 39 | 0.84 |

Under the coin model each forced cell of the run is 0 with probability one half; with column 1 free the linear cells
cost nothing. Equal states give equal runs, as they must (0 conflicts, the control). So with column 1 free, **the
adversary is exactly as good as coin flips over its distinct states, and no better**. The chaos does not fail here.

**Real right halves are poor because their histories merge.** The 65,535 right halves of at most 16 cells produce
only 4,703 to 12,352 distinct visible histories of column 1 by depths 41 to 105 (MB1 refuted: $2^{12.2}$ to $2^{13.6}$,
against the $2^{14}$ predicted). Over the distinct histories, a zero cell costs about one bit, $\beta = 0.91$ to 1.20
(MB2 refuted: no extra cost). So the coin model holds for real right halves too, once histories are counted rather
than seeds. What fails is the delivery: **most of a right half's bits have not reached column 1 even 100 steps
later**. That fits the wheel. Next to 0101…, column 1 is the exact rotation $U$ between kicks, and only the kicks, the
walls arriving from the interior, carry the right half's information into it (§8.8).

**What it means for the prize.** Every statistic of the zero runs measured so far is explained by one rule: **a run
costs about one bit per cell, paid from the distinct histories available**. That is the heuristic for B, now
quantified: a finite right half can never supply the infinitely many bits an eventually zero left half would need.
It is also why a proof is hard: where the statistics are coin flips, there is no structure for a proof to grip. The
places where the chaos does fail are structural, not statistical: the tie between neighbouring columns (§8.15), the
wheel (§8.5), the notched kicks (§8.8), Jen's leftward flow of periodicity (§8.13), and now the bottleneck. The next
step measures the bottleneck: how fast a right half's bits reach column 1.

### 8.17 The bottleneck, measured: the channel, not the seed (2026-10-05)

How much of a right half's information has reached column 1 by time $t$? `bottleneck.c` counts $D(W, t)$, the
distinct visible histories of column 1 over every right half of at most $W$ cells; $I = \log_2 D$ is what the left
side can have received (`rule30_bottleneck.py`, predictions written first). An exact ceiling comes from the ladder:
a layer fed any input can make every prefix a real right half can, so $D(W, t) \le G(m, t + 1)$ for every $m$. It
held at every point.

| Information delivered, bits | $t = 44$ | 64 | 128 | 256 | 512 |
|---|---|---|---|---|---|
| right halves up to 16 cells | 9.92 | 11.52 | 13.33 | 14.64 | 14.91 |
| up to 20 cells | 10.03 | 12.14 | 15.16 | 17.72 | 18.88 |
| up to 24 cells | 10.04 | 12.30 | 16.27 | 19.96 | 22.73 |

- **Early on the channel limits delivery.** By $t = 64$ the information is the same, about 12.3 bits, for every width
  from 20 to 24: about 0.19 bits per step. At $t = 44$ real right halves already make 1,052 of the 1,092 prefixes a
  width-16 layer can (BN1 refuted only in its number: I had predicted at most 9.6 bits).
- **Later the seed limits it, and never quite finishes.** At $t = 512$ about 1.1 bits are still missing for widths
  16 to 20 (BN3 held).
- **Information moves left at about a fifth of a cell per step.** Flip one cell of a random right half: the change
  reaches column 1 after a median of 18, 50, 92 and 128 steps from cells 8, 16, 24 and 32, a speed of 0.21 cells per
  step (BN4 refuted: I had predicted 0.3 to 0.65, near the walls' one half).

`rule30_realruns.py` then tested what this predicts for the real zero runs, over every right half up to 28 cells
(268 million), with its predictions written first:

| Longest real zero run from depth $s$ | 41 | 57 | 73 | 89 | 105 |
|---|---|---|---|---|---|
| right halves up to 16 cells | 8 | 10 | 8 | 11 | 10 |
| up to 20 cells | 8 | 10 | 8 | 12 | 11 |
| up to 24 cells | 8 | 10 | 9 | 13 | 11 |
| up to 28 cells | 8 | 10 | 9 | 13 | 12 |
| $2^{20}$ random right halves of 40 cells | 8 | 10 | 9 | 12 | 11 |

From depth 41 the longest run is 8 for every width from 16 to 28, although the number of right halves grows 4,096-fold
(RR1 held). Deeper, wider seeds buy a cell or two (RR2 held, just). The runs fall even below the distinct-history
estimate at depth 73 (RR3 refuted), and random 40-cell seeds do no better than 20-cell ones (RR4 refuted).

**What it means.** Next to column 0 = 0101…, column 1 is a narrow channel. A seed's information enters it at about
0.2 bits per step at first and moves through the right side at about 0.2 cells per step. **At a fixed depth, the
longest zero run is set by the channel, not by the seed: a wider seed buys almost nothing.** For the prize, that is
the coin model's budget made concrete. An eventually zero left half would need unboundedly many bits delivered on
time through a channel that carries a fraction of a bit per step. It does not prove anything: a single right half
needs only one lucky history, and the channel's capacity does not exclude one. But it shows where the right side's
power runs out.

### 8.18 White triangles and the kicks: the owner's lead (2026-10-05)

The owner: "there are valley defined similar structures such as white triangles that appear in the pattern. Is it
possible to track similar structures (same size triangle, different location), building a graph of where those
structures appear and how they relate to the kick?"

**The triangles are exact.** In Rule 30 a maximal run of $n \ge 2$ zeros $[a, b]$, bounded by ones, becomes exactly
$[a + 1, b - 1]$ one step later:

```math
x'(a) = 1 \oplus (0 \vee x(a+1)) = 1, \qquad x'(b) = 0 \oplus (0 \vee 1) = 1 ,
```

and the cells between have three zero parents. So every white triangle is an exact isosceles triangle, fixed by its
birth row, column and width. `rule30_triangles.py` checked it on a million runs (0 exceptions), and its
counterfactual, Rule 110, breaks it every time. The forced left half's zero runs of §8.12 to §8.16 are the bases of
such triangles at time 0.

**Next to column 0 they form a lattice, and a kick is a dislocation of it** (`rule30_lattice.py`). In the wheel's own
frame (time measured from its phase), the triangles born in columns 2 to 7 sit on 34 fixed sites. Same sizes,
same places, every 56 steps: the owner's graph is a set of chains, one per site, each repeating every period.
Across a kick:

| | Births in columns 2 to 4 on the lattice |
|---|---|
| before the kick, read at the old phase | **100.0%** (44,320) |
| after re-locking, read at the new phase | **100.0%** (58,092) |
| after re-locking, read at the old phase | 26.6% |

So a kick moves the whole lattice rigidly in time by the kick's shift, and nothing else changes (LT2 held). The
triangles alone recover the shift in only 58% of kicks (LT3 refuted), because the lattice nearly repeats under some
other shifts. The chains are short, about 1.5 periods on average, because kicks come about every 90 steps. They are
longest in column 3 and shorten outwards (LT4 refuted: I had predicted column 2 would hold the longest).

**Interior triangles do not foretell kicks.** In columns 12 to 30, in the 36 steps before the wall leaves, the
density of large triangles near kicks is that at random times: ratios 1.02 and 1.00 for the two wall species (TK1
held). **The two wall species differ in what they carry:** along the wall's own path, class-32 walls have 1.47
times the usual density of large triangles, while class-52 walls have the usual density (TK2 refuted: I had
predicted fewer for both). A blind follow-up split the kicks by direction instead (`rule30_wallkind.py`): every
class-32 kick turns the wheel forward and 92.5% of class-52 kicks turn it back or not at all. Along the wall's path,
large triangles are 1.40 times as dense before forward kicks and 1.03 times before backward ones (K2 held), but
bigger forward kicks carry no more than small ones (K3 refuted). **So the triangles show which way a wall will kick
the wheel, not how far.** Followed further back along the wall's line, 20 to 60 steps before the kick, the excess is gone
(`rule30_worldline.py`, W1 refuted: 1.02): the triangles do not foretell a kick from far away. Its counterfactual
band did show something (W2 refuted: 1.19 for forward kicks). That band is a line moving outwards at half a cell per
step from column 1 about 80 steps before the kick, the path of a wake sent out by an earlier event. So forward kicks
may be correlated with earlier ones, as §8.10 hinted. A first test (`rule30_kickgaps.py`) "held" but proved
nothing: kicks happen at fixed wheel phases, so the gaps between them are quantised and their residues already encode
the next kick's class. A direct test then anchored on each kick and looked outwards, clear of the domain and of the
next wall's path (`rule30_wake.py`). **Kicks do send wakes:** large triangles are 1.20 times as dense (after forward
kicks) and 1.39 times (after backward kicks) on the line moving outwards from column 1 at half a cell per step
(WK3 held). Whether a wake steers the next kick is not shown: the link came out slightly negative (WK4 refuted), and
the control failed at the 0.04 level, so this design cannot resolve links that small. A first version of the test
was confounded by the next wall crossing the band, which its own control exposed. `tests/probes/lexicon/rule30_lattice.png` shows both pictures:
- on the left, the lattice in the wheel's frame, 56 phases down and columns 0 to 16 across;
- on the right, a space-time around a kick, with a margin strip that is green while column 1 runs the wheel and red
  at departures.

(A first run of `rule30_triangles.py` was void: its kick detector mixed a relative phase with absolute time. The
detector now has a control, KC, that every later run passed at 98.6%.)

### 8.19 Upwards and sideways: the owner's two pyramid questions (2026-10-05)

**"Build the pyramid from the starting point upwards as well as downwards, as a mirror?"** It is not a mirror.
Running time backwards means solving $y(i) = x(i-1) \oplus (x(i) \vee x(i+1))$ for the row $x$ above. The XOR
can be undone, the OR cannot, so the equation can only be solved for the left neighbour,
$x(i-1) = y(i) \oplus (x(i) \vee x(i+1))$, working leftwards from a choice of the right end. That is exactly the
equation of the forced left half (§5), read in time instead of space. `rule30_mirror.py` checks the consequences:
- **No finite parent.** A finite nonzero row's image is two cells wider, so a single 1 has no finite past (and none
  of the $2^{14} - 1$ rows of at most 14 cells maps to it).
- **Exactly two parents, both infinite to the left:** …1111│0000… and …1111 0 1111….
- **The past piles up on the left.** Two generations up, every left tail has period 3 (checked, M1). An exploratory
  look further up, with right tails of period at most 6 and the branching capped, found period 3 again three
  generations up and period 6 four up, while the right ends stayed all 0, all 1 or period 3.

So the "sign flip" matters only in the reversible XOR part; the OR makes the upward pyramid infinite and one-sided.

**"More than one starting cell, as the 3-sphere is rooted in a pair of points?"** Two seeds are not equal partners.
With seeds at 0 and $d$, every cell to the right of the left seed's light cone is exactly the lone right seed's
pattern, a strip $d$ cells wide riding the right edge for ever (checked for $d$ = 8 to 512). The right seed's
influence spreads left at only 0.28 cells per step ($d$ = 256 and 512), so the left seed's centre column first
notices it after 2.3 to 2.9 times $d$ steps (M3 and M4 held). The left seed owns almost everything. It is the same
asymmetry as above, and the same slow leftward channel as §8.17. (For the prize, every finite seed, single or
multiple, is covered by Conjecture B; Problem 1 itself asks only about the single cell.)

### 8.20 How much information column 1 can carry: exact bounds (2026-10-05)

The bottleneck (§8.17) can be bounded exactly. A layer of $m$ cells fed any input in column $m + 1$ makes a regular
language of visible column-1 words. Its deterministic automaton has a few thousand states at most here, and its
growth rate $\lambda_m$ per visible bit is the spectral radius of that automaton (`entropy.c`, `rule30_entropy.py`,
predictions written first). Every real right side, finite or infinite, makes a column 1 inside every one of these
languages. So

```math
h(\text{column 1 next to } 0101\ldots) \;\le\; \log_2 \lambda_m \quad \text{bits per visible bit, for every } m .
```

| Layer width $m$ | 1 to 3 | 4 | 6 | 8 | 10 | 12 | 14 | 16 | 18 | 20 | 22 | 24 | 26 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bound, bits per visible bit | 0.694 | 0.617 | 0.442 | 0.356 | 0.316 | 0.258 | 0.244 | 0.212 | 0.185 | 0.152 | 0.137 | 0.133 | **0.128** |

The controls held. $m = 1$ gives exactly the golden ratio, Lemma 3's Fibonacci count. Each $\lambda_m$ matches the
ladder's independently counted start groups within 0.05%. Wider layers never raise the bound (a theorem, checked).
With column 0 unclamped the instrument reads exactly 1 bit, and with column 0 constant at 0 it reads 0, Condrey's
case.

**So next to a period-2 column, column 1 carries at most 0.128 bits per visible bit, whatever the right side**,
which is 0.064 bits per step. A random sequence carries 1. This is the bottleneck of §8.17 as a theorem rather than
a measurement, up to the convergence of the power iteration (9 digits). Beyond $m = 20$ a sparse version of the
automaton (`entropy2.c`, which reproduced every earlier value exactly) took the bound to $m = 26$. The fall per cell
slowed from 0.015 to 0.004 (EN4 and EN5 held). **The bound is levelling off, near 0.12 bits per visible bit**,
inside the range a rough estimate from the kicks gives (about one kick every 90 steps, each carrying its size and
some timing). That fits the picture: the wheel carries no information, and the kicks carry all of it. Whether the
limit is exactly positive is not proved; the trend says it is.

*2026-10-06, Local.* JOB M3a, blocked for memory since 2026-10-05, ran here after the owner asked whether it could be
made to fit: the sets' pool (13 GB at $m = 27$, 29 GB at $m = 28$) now lives in a file mapped on the internal NVMe,
written once (`entropy2.c -DPOOL_MMAP`, identical to the heap build at every width checked), and the runs took 208 s
and 459 s with 6 GB resident. $m = 27$: 289,484 automaton states, $\log_2 \lambda = 0.1229$; $m = 28$: 448,144
states, $0.1222$ bits per visible bit (EN6 held). The fall per cell is now 0.0048 then 0.0007: **the bound levels off
near 0.122**. The exact certificate at these widths is in `rule30_squeeze.py` (SQ6).

**What column 1 actually carries.** The bound counts every sequence any right side can make. For typical right
sides (random cells), the entropy rate of column 1's visible bits can be measured directly (`rule30_metric.py`,
predictions written first): about **0.080 bits per visible bit**, 0.04 bits per step. That is two thirds of what the
bound allows. The estimate settles once its window covers a whole turn of the wheel (28 visible bits), and it is
stable on half the data. Its controls held: the pure wheel gives 0, a Markov source its known rate, and shuffled bits
their full binary entropy. Divided among the kicks (one every 88 steps), **each kick carries about 3.5 bits** (ME3
held). So column 1's information is the kicks' information: the wheel itself carries none.

**A census of traces** (the random-chaos step: six seeded random words besides the short ones). At $m = 10$ every
periodic column 0 except the constant 0 leaves column 1 more than 0.1 bits per visible bit (EN3 held). The trace 01
is not the most constraining (EN2 refuted): 0001 allows 0.159 and 001 0.190, against 0.316 for 01. Per step the
traces range from 0.09 to 0.18 bits. The wheel, which only 01 turns, does not make its column 1 unusually poor in
information. It makes it orderly, a different thing.

### 8.21 The search widened: every right half up to 32 cells (2026-10-05)

Rung 1 (§5, §6) searched every right half up to 18 cells. `rule30_scan.py` (with `realruns.c`'s scan mode, predictions
written first) forces the left half to depth 126 for every right half up to 32 cells and records the longest zero run
anywhere in it. Any half whose left half ends in 30 or more zeros would be followed to depth 2,000. Its control
agrees exactly with an independent Python computation (SC0).

| Right halves of at most | 18 cells | 20 | 22 | 24 | 26 | 28 | 30 | 32 |
|---|---|---|---|---|---|---|---|---|
| Number | 262,143 | 1,048,575 | 4,194,303 | 16,777,215 | 67,108,863 | 268,435,455 | 1,073,741,823 | 4,294,967,295 |
| Longest zero run in $L(1..126)$ | 17 | 17 | 17 | 17 | 17 | 17 | 17 | 17 |
| Candidates ending in 30 or more zeros | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

Both blind predictions held: no candidate (SC1), and no growth of the longest run (SC2). The run took two hours on
three cores.

**What it excludes.** A counterexample is a finite configuration whose column 0 is 0101… from some time on. Shifted
in time, its column 0 is 0101… from $t = 0$ (or 1010…, one step later). If its right half has at most 32 cells and
its left half ends at depth $d$, the forced left half is zero from depth $d + 1$ to 126. A zero run of $126 - d$
cells would have to occur, and none longer than 17 does. **So no finite configuration whose right half has at
most 32 cells and whose left half has at most 108 cells keeps a column at 0101… for ever.** Rung 1 covered longer
left halves (to about 240 cells) but only right halves up to 18 cells.

**The plateau.** The longest run to depth 126 is 17 at every width from 18 cells on, although the number of right
halves grows 16,000-fold. It is the bottleneck of §8.17 again: at a fixed depth, wider seeds buy nothing.

### 8.22 Two half-lines, one column 0: chaos on the left, a channel on the right (2026-10-05)

Rule 30 at a cell uses only its two neighbours. So once column 0 is given for all time, the columns to its left evolve
on their own (Rule 30 with column 0 as their right boundary), and so do the columns to its right. Column 0 must also
obey the rule, $\tau(t+1) = x_t(-1) \oplus (\tau(t) \vee x_t(1))$. For $\tau = 0101\ldots$ that says

```math
x_t(-1) = 1 \ \text{at every odd } t, \qquad x_t(1) = \lnot\, x_t(-1) \ \text{at every even } t .
```

**So a finite configuration with column 0 = 0101… for ever is exactly a pair of finite seeds, one on each side, whose
two driven half-lines produce columns −1 and 1 meeting these two conditions.** `rule30_halflines.py` checks the
decoupling exactly (D0: 0 cells differ in 200 whole runs) and measures both sides:

| Column 0 | Left half-line, column −1 (bits per step) | Right half-line, column 1 (bits per step) |
|---|---|---|
| 0101… | 0.9997 | 0.057 |
| 001… | 0.9997 | 0.038 |
| 0011… | 0.9998 | 0.0001 |
| 0001… | 0.9997 | 0.0000 |

The left half-line never forms a wheel: its information flows towards column 0 at full speed, so column −1 is pure
chaos for every trace (D1, D2 held). The right half-line is a thin channel (D3 held), and for 0011… and 0001… typical
right halves lock column 1 into a periodic pattern; by Jen's theorem those right halves can never be counterexamples.

**The shape of the problem, in one sentence.** A period-2 counterexample needs the left side's chaos to produce,
bit for bit and for ever, 1 at every odd time and the complement of the right side's wheel-and-kicks at every even
time. Finite left seeds make only countably many columns −1, inside a space of full entropy. The right side can reach
only a thin set, at most 0.128 bits per visible bit (§8.20). Two such sets have no reason to meet, and generically
they do not. That is the heuristic for B in its plainest form. It is not a proof, because one meeting is all a
counterexample needs.

### 8.23 Columns as numbers: the owner's irrational-number question (2026-10-05)

The owner: "If the pattern never repeats itself, given the kick and the wheel, is it possible to describe the problem
generally as an irrational number? Do any of the known irrational numbers look similar?"

**Yes, exactly.** Read a column as a binary number, $0.b_0 b_1 b_2 \ldots$. The column is eventually periodic if and
only if that number is rational. So Prize Problem 1 says that one particular number is irrational: the one whose
binary digits are the centre column from a single 1. The period-2 case says it is never eventually like
$0.0101\ldots = 1/3$. In this document's construction, each right half gives the forced left half's number
$0.L_1 L_2 L_3 \ldots$, and a finite counterexample would make it a terminating binary fraction (a dyadic
rational).

**What the numbers look like** (`rule30_irrational.py`, 20,000 binary digits, predictions written first). Almost
every real number's continued fraction obeys three laws: Khinchin (the geometric mean of the partial quotients tends
to 2.685), Gauss–Kuzmin (41.5% of them equal 1) and Lévy (1.187).

| Number | Geometric mean | Share of 1s | Lévy |
|---|---|---|---|
| coin flips (control) | 2.699 | 0.419 | 1.193 |
| centre column from a single 1 | **2.669** | **0.413** | **1.181** |
| forced left half of a real right half | **2.683** | **0.416** | **1.185** |
| column 1 next to 0101… | a giant partial quotient after 3 terms: a near-rational | | |

The control $\sqrt 2$ gives 2, 2, 2, … and 1/3 gives $[0; 3, \approx 2^{19999}]$. The centre column and the forced
left halves look exactly like typical irrational numbers (IR1, IR2 held). Column 1 next to 0101… does not (IR3
held): its first digits are a long clean stretch of the wheel, so the number sits extraordinarily close to a
fraction. It behaves like a Liouville number, a number very well approximated by rationals. That is the wheel seen
arithmetically.

**Known numbers that resemble the problem.**
- **Powers of 3/2 (Mahler's problem).** Kopra (PRIOR-ART.md) shows that multiplying by 3/2 in base 6 is a cellular
  automaton of the same class as Rule 30. Whether the fractional parts of $\xi (3/2)^n$ can all avoid half the circle
  is open, for the same kind of reason. It is the closest known relative.
- **$\sqrt 2$, $\pi$, $e$.** All proved irrational, all with digits that look random, and none proved normal. Rule
  30's centre column looks just as random, but even its irrationality (non-periodicity) is unproved. Prize Problem 2
  (equal frequencies) is its analogue of normality.
- **The Thue–Morse number and Champernowne's constant.** Both never repeat, and both were proved to by their
  structure: Thue–Morse is overlap-free (and its number transcendental, Mahler), and Champernowne's is normal by
  construction. Rule 30 has no such structure known.
- **Rotation numbers and the golden ratio.** The wheel is a coding of a rotation by $17/56 = [0; 3, 3, 2, 2]$. Codings
  of irrational rotations (Sturmian words, the Fibonacci word for the golden ratio) are the classic sequences that
  never repeat yet are as simple as possible. The golden ratio appears here too: it is the width-1 layer's growth
  rate exactly (Lemma 3, §8.20).

**What it teaches.** Every irrationality proof of a specific number has come from its structure: Hermite for $e$,
Lindemann for $\pi$, Apéry's recurrences for $\zeta(3)$. None has come from its digits looking random. Rule 30's
centre column is in the position $\pi$'s digits would be in if nobody had found $\pi$'s structure.

### 8.24 The complementary pair: two irrational numbers that must add up to one (2026-10-05)

The owner: "I wonder if a rational number can have a complementary pair, such that two related irrational numbers
combine to form a rational one." That is exactly the period-2 condition. By §8.22, column 0 = 0101… forces
$x_t(-1) = 1$ at odd $t$ and $x_t(1) = \lnot x_t(-1)$ at even $t$. Read the even-time bits of column −1 as a binary
number $A$ and those of column 1 as $B$. Complementary bits add without carries, so

```math
A + B = 0.111\ldots_2 = 1 ,
```

while the odd-time bits of column −1 make the number 1 by themselves. By Jen's theorem $B$ cannot be eventually
periodic, so $A$ and $B$ would be two irrational numbers, one made by the left side's chaos and one by the right
side's thin channel, that add up to exactly one.

**How long a finite seed can keep them complementary** (`rule30_complement.py`, predictions written first). Cut a
forced left half at depth $d$. The finite seed so made, of width $w$, keeps column 0 at 0101… for exactly $P$
steps, where $P$ is the depth of the first 1 beyond the cut. So the pair stays complementary for about $P/2$
digits. A forward simulation confirms the count exactly (CP0: 0 of 200 differ). The excess $P - w$, maximised over
every right half of each exact width and every cut:

| Right half's width | 0 | 1 | 2 | 3 | 4 | **5** | 6 | 8 | 10 | 12 | 14 | 16 | 17 | 18 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Largest excess $P - w$ | +5 | +8 | +7 | +6 | +5 | **+9** | +8 | +6 | +4 | +2 | +3 | +1 | 0 | −1 |

**A finite seed beats its own width by at most 9 steps** (CP1 held). The champion is tiny: right half 10001, left side
cut at depth 20, 26 cells in all, keeping column 0 at 0101… for 35 steps (CP2 held: the best width is 5). Wider right
halves do worse, because their extra bits arrive too late (§8.17). With §8.21, no right half up to 32 cells does
better than +9. **So the two numbers can be complementary for at most about $(w + 9)/2$ binary digits, where $w$ is
the seed's width, and then they fall out of step.** A counterexample needs them complementary for ever.

This is the same kind of fact as Condrey's horizon $H(2, w)$ (PRIOR-ART.md), the longest period-2 prefix over rows of
a given support radius, which he showed is at least $w$. Here the count is in total width, for right halves up to
32 cells and cuts whose zero run ends by depth 126, and in that range a seed gains at most 9 steps on its width.

### 8.25 The owner's lightning (2026-10-05)

The owner: "take a lightning trace on the pyramid: from the top down run some sort of path-tracing walk that reaches
the bottom of a given pyramid, and repeat this a large number of times, seeing how the lightning forks and reaches the
bottom each time."

Black cells conduct and white cells resist. A walker allowed only on black cells would rarely get far, so
`rule30_lightning.py` uses two kinds of lightning, as real lightning has both:
- **the strike**, the path of least resistance from the apex, where crossing a white cell costs 1, computed exactly;
- **the flicker**, 20,000 random walks preferring black cells ten to one.

The pyramids are Rule 30 from a single 1 (depth 512, interior density 0.502), random pyramids of the same density
with black edges, and Rule 90 (the Sierpinski triangle). Predictions were written first.

| | Rule 30 | Random pyramids | Rule 90 |
|---|---|---|---|
| Strike: white cells crossed to the bottom centre | 3 | 2 to 7 | 256 |
| Flicker: mean landing point (sd about 18) | **−35.7** (2.0 sd to the left) | −1.5 to +1.7 | +0.2 |
| Flicker: share of steps through white | 0.214 | 0.20 | 0.93 |

- **The strike finds Rule 30 as easy to cross as a random pattern.** Almost every path can stay on black: only 3
  white cells in 511 rows. (LG1, a 15% band, was refuted by its own design, since the costs are small whole numbers;
  Rule 30's 3 lies inside the random range.) Rule 90 resists 85 times more (LG2 held). Rule 30's strike to the
  centre rides the always-black right edge for about 100 rows, then cuts back in.
- **The flicker is pulled to the left** (LG3 held): Rule 30's lightning lands two standard deviations left of centre,
  the random pyramids' within a tenth. The cause is local, not hidden structure. A lightning that knows only Rule
  30's rule from a cell to the three below it, with fresh random neighbours every step, drifts at −0.077 cells per
  step against the real pyramid's −0.070 (LG4 held). The real drift is steady from top to bottom (LG5 held). Below
  a black cell, Rule 30 makes the lower-left and lower-middle cells black half the time each, but the lower-right only
  a quarter of the time: the OR sits on the right. **The lightning sees Rule 30's handedness, and otherwise sees
  coin flips.**

`tests/probes/lexicon/rule30_lightning.png` shows the pyramid (black cells grey), the flicker's 20,000 paths (yellow
to red) tilting steadily left, and the strike (blue).

### 8.26 How irrational numbers are proved, and which way might fit (2026-10-05)

The owner's interest is in how irrationality is proved, given "man's obsession with counting to infinite digits of
pi, just because computers can count very quickly". No digit count ever proved a number irrational. Every proof uses
a structure the number has, and each kind of proof has an analogue here.

| Proof method | Example | Its analogue for Rule 30 | State |
|---|---|---|---|
| Algebraic contradiction | $\sqrt 2$ (Euclid): $p^2 = 2q^2$ has no solution | Jen's theorem (§8.13): if two adjacent columns were both rational, periodicity would flow left and the light cone would force everything to 0 | proved, for pairs of columns |
| A positive integer smaller than 1 | $e$ (Fourier): $q! \cdot e$ less a whole number would be a positive integer below 1 | some integer-valued count that a finite left half would make too small | no such quantity known; the natural lead |
| Too-good rational approximations | Liouville numbers | column 1 next to 0101… is near-rational (§8.23) | true of column 1, but it is not the column the prize asks about |
| Recurrences giving good approximations | $\zeta(3)$ (Apéry) | a recurrence for the centre column | none known |
| Automata and words | Thue–Morse (overlap-free; transcendental, Mahler) | column 1 is not 2-automatic (§8, T6) | does not apply |
| Statistics of the digits | none: no irrationality was ever proved this way | the coin model (§8.14, §8.16), Khinchin's laws (§8.23) | evidence only |

Fourier's argument for $e$ has the shape this problem would need. Suppose the number were rational. Then some
quantity built from it would be a whole number, yet strictly between 0 and 1, which is impossible. For Rule 30 the
quantity would have to come from the structure found so far, perhaps the exact channel bound (§8.20) or the wheel's
lattice (§8.18), turned into an integer that a finite left half would make too small. That is speculation, recorded as
a lead, not a result.

### 8.27 The pyramid as a stack of rational numbers (2026-10-05)

The owner: "I find myself wondering if there is more than one irrational number embedded, which would confuse and
compound the already existing irrational number." The pyramid does hold infinitely many numbers, but every one of
them is rational, and the centre column is built from them.

**Cut the pyramid along diagonals instead of columns.** Write $c(t, x)$ for the cell at time $t$ and position $x$.
Right diagonal $d$ is $D_d(t) = c(t, t - d)$, and left diagonal $e$ is $E_e(t) = c(t, e - t)$, each read from $t = 0$,
so each starts with the zeros above the pyramid. The centre cell at time $t$ lies on right diagonal $t$ and on left
diagonal $t$, at position $t$ along each:

```math
c(t, 0) = D_t(t) = E_t(t) .
```

So the centre column is a Cantor diagonal through two lists of numbers, $0.D_d(0) D_d(1) \ldots$ and
$0.E_e(0) E_e(1) \ldots$. Cantor read the $n$-th digit of the $n$-th number in a list, and changed it, to build a
number missing from the list. Here the digit is read and kept.

**Every right diagonal is rational, by a short proof.** Rule 30 is $c' = l \oplus (c \lor r)$. Along a right diagonal
the left parent lies on the same diagonal, so

```math
D_d(t) = D_d(t-1) \oplus \bigl( D_{d-1}(t-1) \lor D_{d-2}(t-1) \bigr) .
```

Each diagonal is a running XOR of the OR of the two diagonals to its right. A running XOR of a sequence with period
$p$ repeats after $p$ steps, or after exactly $2p$ if one period holds an odd number of 1s. The right edge is all 1s,
and the diagonals beyond it are all 0s. So by induction every right diagonal is purely periodic, with a period that is
a power of 2 and at most doubles from one diagonal to the next. The periods must also keep growing. Diagonal $d$
begins with $\lceil d/2 \rceil$ zeros above the pyramid, and then meets the pyramid's left edge, where the two outermost
cells are always black. So its period is longer than $\lceil d/2 \rceil$. The periodicity is Jen's theorem (1990), and
Rowland characterises where each period first appears. The proof here is the natural one; it has not been checked
against theirs.

**The left diagonals are rational too, but of the opposite kind.** Along a left diagonal the right parent lies on the
same diagonal, but it enters through the OR. Wherever the neighbouring diagonal holds a 1, the new cell is fixed
whatever the old one was: a reset. So a left diagonal settles into a period no longer than its neighbours', unless
the diagonal before it is eventually all 0. Only then can the period double.

**This half is known, and was re-derived here before the source was read** (a failure of method, recorded in
PRIOR-ART.md). Each left diagonal is eventually periodic with a power-of-2 period by Jen's Theorem 4 (J. Stat. Phys.
43, 1986). Rowland's §5 lists the same sequence of periods measured below (1, 1, 1, 2, 1, 2, 2, 1, 4, …) and proves an
observation of Wolfram's (*A New Kind of Science*, p. 871). A period doubles exactly when a diagonal is eventually white
**and** the diagonal before it has an odd number of black cells in each period. The argument above gives only the
first half.

**Measured** (`rule30_diagonals.py`, $2^{18}$ = 262,144 steps, predictions written first):

| Distance from the edge | 9 | 29 | 42 | 63 |
|---|---|---|---|---|
| Right diagonal's period (no transient) | 64 | 4,096 | 131,072 | beyond the window |
| Left diagonal's period | 1 | 8 | 8 | 8 |
| Left diagonal's transient (steps before it repeats) | 5 | 30 | 57 | 91 |

- The proved statements check out exactly (DG0, DG3). Rowland's first diagonals of each period, 1, 3, 4, 6, 7, 9,
  15, 16, 24, are reproduced.
- **The right periods double about every 2.8 diagonals** (DG1 held: log₂ of the period grows by 0.353 per
  diagonal). Every right diagonal from 10 on has a period above $2^{0.3d}$ (DG2 held). From diagonal 3 to 63 every
  period is longer than the diagonal's number (beyond 42 the periods exceed the window's $2^{17}$). So the centre
  column reads each of those diagonals inside its first period: it never sees one repeat.
- **The left periods stay tiny.** Only three left diagonals up to 63 are eventually 0, those at 2, 7 and 28, and the
  period doubles just after each, to 2, 4 and 8. I predicted at most 4 (DG4, refuted). I also predicted that the
  centre lies inside every left diagonal's transient from distance 10 on (DG5, refuted). It does from distance 20
  on, but at 10 to 17 and at 19 the transient ends at or before column 0. These two predictions were not blind: a
  smoke test printed their verdicts before the predictions were committed (recorded in the script).

**What it means.**
- **There is one candidate irrational number, built from infinitely many rational ones.** On the right the numbers'
  periods grow exponentially, so each centre digit comes from a number that has not yet repeated. On the left the
  periods stay small, but the transients grow, and from distance 20 on each centre digit comes from inside a
  transient. Either way the centre column takes every digit from a stretch of a rational number that does not
  repeat. That is how a diagonal through rational numbers can avoid repeating, if it does.
- **The two sides are opposite kinds of order.** The right side is nested: stripes with no transient, whose periods
  double (Rowland's "local nested structure"). The left side is a band of short-period stripes along the pyramid's
  left edge, each reached after a transient that grows with the distance from the edge. This band explains why
  §8.25's prediction LG3 placed regular stripes on the left. The lightning's pull to the left was local all the same
  (LG4).
- **The proof idea it suggests.** Cantor's argument shows that a diagonal differs from every number in its list. A
  proof here would need something else: that the digits the centre column takes from all these rational numbers
  can never line up into a repeating pattern. That is a statement about how the periods and transients of the
  diagonals interact, not only about how fast they grow. It is recorded as a lead, not a result.

### 8.28 Does the lightning gravitate to certain paths? (2026-10-05)

The owner: "Given current follows the path(s) of least resistance distributed throughout the material substrate, do
the lightning walks tend to gravitate towards certain paths or patterns?" It depends on how the lightning sees the
substrate, and Rule 30's answer differs from randomness's. `rule30_channels.py` computes everything exactly, row by
row, without sampling, on pyramids 2,048 rows deep. Predictions were written first.
- **The flicker** (§8.25) sees only the next row and picks one step at a time.
- **The polymer** is the current spread through the whole substrate. Every path from the apex counts, weighted by
  the product of its cells' conductances (black 1, white 0.1). It is statistical physics' model of a path of least
  resistance with fluctuations.

Channelling is measured by the **same-landing chance**, the probability that two independent bolts end on the same
cell. For a free random walk it falls like $1/\sqrt{\text{depth}}$. On a random substrate, theory (PRIOR-ART.md) says
the polymer's stays positive in this dimension at every temperature: it localises into channels. The flicker's falls
like a free walk's.

| | Free walk | Random pyramids | Rule 30 | Rule 30 from a random row | Rule 90 from a random row |
|---|---|---|---|---|---|
| Flicker: same-landing chance at depth 2048 | 0.0076 | 0.012 to 0.013 | 0.012 | | |
| Polymer: same-landing chance, averaged over depth | 0.015 | 0.10 to 0.13 | **0.037** | 0.033 to 0.036 | 0.070 |
| Polymer: share of rows two bolts share | | 0.16 to 0.22 | **0.069** | 0.05 to 0.06 | 0.11 to 0.16 |
| Spread of resistance along random routes, per row | | 0.25 | **0.18** | 0.17 to 0.18 | 0.24 |

- **The flicker gravitates nowhere in particular.** On every substrate it spreads like a free random walk, sharing
  only slightly more (CH1 held).
- **On a random substrate the polymer forms channels,** as theory says. Two bolts end on the same cell about one time
  in eight, at every depth, and share a fifth of their route. The figure shows a braid of thin filaments.
- **On Rule 30 the channels are three times weaker** (CH2 and CH3 refuted). Two bolts land together one time in 27,
  falling with depth, and share 7% of their route. **Rule 30 spreads its current more evenly than a random material
  does.** This is the first measure of the lightning that tells Rule 30 from coin flips beyond its leftward pull.
- **It is the rule, not the seed** (CH6 held): Rule 30 run from a random row channels just as weakly.
- **The cause is the handedness again** (CH7 held). Below a black cell, Rule 30 makes the lower-right child black only
  a quarter of the time (below a white cell, three quarters). The other two children are uncorrelated with it. So
  along any route a black cell tends to be followed by a white one on a third of the steps, and routes differ less in
  total resistance. To first order the spread per row is $\tfrac14 - 2 \cdot \tfrac13 \cdot \tfrac18 \approx 0.167$
  against $\tfrac14$ for independent cells. With less to choose between, the current does not concentrate.
- **Rule 90 is in between** (CH8 held, at the edge of its band). Its rows are as random as Rule 30's and its path
  spread is nearly random, yet it channels only 0.6 times as much as a random material. Something longer-range matters
  there too, perhaps its nested triangles; it was not identified.
- **The channels lean left**, as the flicker does (CH4 held: the polymer lands at −0.088 of the depth).
- **The chaos step:** flipping 1% of the cells keeps Rule 30's weak channels (CH5 refuted: I expected them to move
  much more than they did).

**So on Rule 30 the lightning gravitates to no special paths. It concentrates less than it would in a random
material, and the only pattern it follows is the lean that the rule's handedness gives it.**
`tests/probes/lexicon/rule30_channels.png` shows the flicker (left, one smooth beam) and the polymer (right, a braid of
filaments leaning left). Along the pyramid's left flank the band of short-period stripes of §8.27 is visible.

### 8.29 The pyramid as a maze (2026-10-05)

The owner: "Given some random initial starting position in the pyramid, and without knowledge about the structure the
walker is in, what is the most efficient way to trace a path to the origin single point, as if the structure were a
maze?" Black cells are corridors and white cells are walls. The walker climbs to one of the three cells above and sees
a cell only by looking at it. Every move climbs one row, so no route from row $t$ is shorter than $t$ moves.

**A theorem makes the maze easy going up.** Rule 30 keeps white-white-white white, so every black cell below the apex
has a black parent: three white parents would have made it white. A walker on black can therefore always climb onto
black. It cannot leave the pyramid, since everything outside is white. And the only black cell of row 0 is the apex.
**So every climb on black reaches the origin in exactly $t$ moves, the shortest possible, with no map, no memory and
no backtracking.** It takes at most two looks per row: if two parents are white, the third is black without looking.
The same holds for every rule that keeps white-white-white white, grown from one seed.

**Going down, the same maze has dead ends.** A black cell has no black child 3/16 of the time (measured 0.187, MZ2
held). Lightning works this way too. The stepped leader branches downwards and most branches die; the return stroke
climbs back up the one channel that connected. In the pyramid every black cell connects to the origin, but only the
climb up is sure to find the way.

**A random pattern of the same density is a real maze, and mostly a broken one.** On a random pyramid, a black cell
connects to the apex only if a chain of black cells leads up to it, which is directed percolation. Measured at depth
2048 (`rule30_maze.py`, predictions written first):
- Only 1.5% of a random pyramid's interior black cells connect, against 100% of Rule 30's (MZ0, MZ3).
- The threshold, where random patterns begin to connect, is near density 0.53 (MZ4 and MZ7 held). The connected
  share is 3% at 0.50, 13% at 0.53 and 65% at 0.56. Rule 30 sits just below the threshold, at 0.502, yet it is
  connected everywhere.
- On the random pyramid a greedy climber sticks from 76% of the connected starts. A depth-first search that marks
  where it has been (Trémaux's method) always gets through, reading 3 cells per row on the median.

**The most efficient walker.** With the theorem, a row costs $2 - q$ looks, where $q$ is the chance that the first look
finds black. Only the first look matters.

| Walker | Looks per row |
|---|---|
| all three parents looked at, middle first (without the theorem) | 2.11 |
| middle first, then left, the third deduced | 1.73 |
| left first | 1.65 |
| right first | 1.54 |
| adaptive: first look chosen by its last move and what it saw | **1.29** |

Over all black cells, Rule 30's parent patterns are exactly the coin model's, which predicts 1.5 for middle first.
Along a climber's own path they are not: its history biases what lies above it (MZ1 refuted). The adaptive walker
(MZ6 held, scored on starts it was not trained on) learns to **follow the grain**. After climbing up-right, up-right
again is black 89% of the time. So it rides the lines parallel to the pyramid's left edge, the left diagonals of
§8.27. A 1% random corruption leaves 92.6% of the black cells connected (MZ5 held): the maze is robust, but no longer
perfect.

**The general answer.** In an unknown maze the efficient methods are a depth-first search with marks (Trémaux's
method, which walks no corridor more than twice), or following one wall when the maze has no loops. In the worst case
any method must explore most of the maze. A pyramid grown by a rule from one seed is not such a maze: its walls are
made by causes, and every black cell has a cause above it. Climbing towards the cause is always right.

### 8.30 The band of stripes, and where the chaos stops (2026-10-05)

§8.27 found the left diagonals periodic with tiny periods after a transient. `rule30_leftband.py` follows them to
distance 2,047 from the left edge (8,192 steps, predictions written first).

**Most of this is known**, which the survey, done after the runs (a failure of method), found:
- Wolfram's prize announcement (2019) describes the regular striped left side. Over the first 100,000 or so steps its
  boundary "seems to move on average about 0.252 steps to the left at each step", with random fluctuations. That is
  an observation, not a theorem.
- Rowland's §5 proves when the periods double (§8.27).
- Rowland also asks whether there is only one "left side", the same for every seed. He expects the answer is no: the
  first place two left sides can split is his column 53209 (§8.31).

The parts not found in the sources are the match of the boundary's speed with the speed at which a single change
spreads left on a random background, and the measured transients and eventually-white diagonals below.
- **The periods stay tiny.** They double only just after an eventually-zero left diagonal, as proved in §8.27. Those
  are at distances 2, 7, 28 and 399, so the period is only 16 at distance 2,047. I predicted the zero diagonals would
  come at a steady ratio near 4 (LB1, refuted): the gaps grow faster.
- **The stripes are universal.** Three random seeds give the same eventually-zero diagonals, 2, 7, 28 and 399
  (LB3). Only the transients depend on the seed.
- **The band grows linearly.** Diagonal $e$ settles after about $1.3e$ steps (LB2; I predicted 1.4 to 2.2). So the band
  of stripes fills the left 38% of every row, and its inner edge moves left at about 0.25 cells per step.
- **That edge is Rule 30's leftward speed of information.** On a random background a single flipped cell's influence
  spreads left at 0.246 cells per step (LB5 held: 10 trials, 0.226 to 0.254). The band's edge moves at 0.245 to 0.257,
  measured from the transients' growth. So the stripes fill the part of the pyramid that news of the seed has not yet
  reached. The chaotic core spreads left at a quarter of the speed of light, and outside it the left edge settles into
  the same stripes whatever the seed was.

One design error is recorded. To measure the seed's front I compared the pyramid from 1 with the pyramid from 11
(LB4). The two differ only in one extra cell along the right edge, at every step. The extra cell sits to the right of
a black cell, and the OR in $c' = l \oplus (c \lor r)$ ignores $r$ when $c = 1$. So the change never enters the
interior. It is a small instance of the handedness that runs through §8.25 to §8.29: Rule 30 hides changes that
arrive from the right of a black cell.

**Together with §8.27, the pyramid has three regions.** On the left is the band of universal stripes, 38% of each
row. On the right is a thin strip where the nested, period-doubling diagonals have had time to repeat. Its period is
about $2^{0.35d}$ at distance $d$, so the strip's width grows only like the logarithm of the depth, about
$2.8 \log_2 t$. Between them is the chaotic core, whose left edge moves at 0.25 cells per step. The centre column,
whose irrationality is the prize, lies inside the core.

### 8.31 One left side or many? Rowland's question, answered both ways (2026-10-05)

Rowland asked whether Rule 30 has "really only one left side", the same for every initial row with a white left tail.
He expected not, and found the first place it could split: his column 53209, our diagonal 53208. There the diagonal
before is eventually white, and the one before that has an even number of black cells in each period. He left open
whether the other continuation occurs "for some initial conditions" (PRIOR-ART.md). `rule30_leftsides.py` answers it,
with predictions written before each of four runs.

**The method, with a certificate.** Each left diagonal depends only on itself and the two nearer the edge. So the first
$K$ diagonals form a closed system. As a $K$-bit number $V$, they evolve by

```math
V' = \bigl( (V \ll 2) \oplus ((V \ll 1) \lor V) \bigr) \bmod 2^K ,
```

which is the row itself in left-edge coordinates. Nothing else in the pattern needs computing. The system is finite
and deterministic, so one equality $V_t = V_{t+P}$ proves the strip periodic for ever after. Every result below carries
such a certificate, for $K$ = 160,000 diagonals over $2^{18}$ steps.

**Generic rows have one left side.**
- 60 distinct rows were tried: the single 1, 45 random finite seeds of up to 64 cells, 4 random seeds of 10,000 to
  150,000 cells, and 10 rows with a random right part, Rowland's general case. All have the same left side out to diagonal 160,000,
  through both possible splits on the way (53208 and 58287; LS1, LS4, LS5 held). I predicted both continuations would
  occur (LS2, refuted).
- A coin toss at the first split would make 41 seeds agree with probability about $10^{-12}$, so this is no coin.
  The rows sit at different phases of the one cycle (LS6 refuted). Measured against each row's own phase, though, the
  moment that decides the split falls at the same point, 11 mod 16, for all 20 rows checked (LS8 held). Diagonals
  depend only on diagonals nearer the edge, so the chaotic core, farther out, never reaches the band. By the time the
  band's edge arrives at diagonal 53208, the decision is timed by the band's own rhythm, and the row has been forgotten.

**Constructed rows realise at least four left sides.** A settled strip is itself a valid row. In the single seed's
settled strip, flip the cell at diagonal 53208. The diagonal before it is white for ever, so nothing resets the flipped
one, and the flip persists. The result is a finite seed, of at most 160,000 cells, with the other continuation (LS9
held). Its left side splits again at diagonal 72576, Rowland's column 72577; the universal side's next split is 58287
(LS10 held). Flipping at those gives four distinct certified left sides by diagonal 160,000. A flip anywhere else, at
diagonal 60000 for instance, is erased by the resets (LS11 held).

**So the question has two answers.**
- The other continuations do occur for some initial conditions, as Rowland surmised: explicit finite seeds realise at
  least four left sides, with certificates.
- No row tried that was not built for them reaches them. Generic rows have one left side, because the split is decided
  by a clock that belongs to the left side itself.

Whether branch points go on for ever, giving infinitely many left sides, is open. Below diagonal 160,000 there are two
on each side. (Note, 2026-10-06: the probe's recorded list also has a doubling at diagonal 87,866, period 16 to 32,
which this prose omitted; §8.60 took the strip to a million diagonals and found nothing more.) None of this bears directly on the centre column, which lies in the chaotic core, far from the band.
What it shows is a place where Rule 30's chaos is forgotten completely and provably.

### 8.32 The wheel on the grid: the owner's square peg (2026-10-05)

The owner: "The wheel once again surfaces a leap shift we found in the interpolation shaders: the wheel is inherently
circular, but the pyramid and its grid are inherently a two-dimensional array. Is this another square-peg,
round-hole problem?"

**The peg fits.** The wheel turns by a rational amount, 17/56 of a turn per step, so 56 steps are exactly 17 turns,
with nothing left over. Drawn on a grid, a rotation is a pixelated straight line. At even times $t = 2s$, column 1 is 1
exactly when $17s \bmod 28 \in \{22, \ldots, 27\}$, that is,

```math
\sigma(2s) = \left\lfloor \frac{17s + 6}{28} \right\rfloor - \left\lfloor \frac{17s}{28} \right\rfloor .
```

That is how Bresenham's algorithm draws a line of slope 17/28 on pixels, and how the leap-year rule keeps a calendar in
step with the sun: floor functions, with an extra step whenever the error builds up. With a rational slope the pattern
of extra steps repeats exactly. The grid holds this circle perfectly, and the kicks shift the line by whole pixels (the
notches of §8.8).

**The measurement does not fit.** The grid shows the wheel's angle only modulo a turn, 28 notches at one parity. A kick
is read as the nearest whole number of notches, so a change near half a turn could be forward or backward. That is the
shaders' half-period alias exactly, and §8.8 had flagged it as one possible cause of V0's narrow miss.

**Measured** (`rule30_wheelspeed.py`, addendum U0 to U2, predictions written first). The shaders' fix was the carry.
Here the carry reads the phase at every even time instead of every 56th, so consecutive readings are close and no
change approaches half a turn.
- The alias is real: 22 of 205,955 long gaps had wrapped by a whole turn (U2, refuted: I predicted more).
- It is harmless. Removing it moves the wheel's speed by $3 \times 10^{-6}$ (rotation number 0.303542 to 0.303545),
  not the $10^{-4}$ that separated it from the spectral line (U1, refuted). So V0's gap has the other recorded cause:
  when the kicks are lopsided, the spectral peak need not sit at the mean rate.

**So no, not this time.** The circle and the grid agree exactly; only the reading of the angle has the alias, and here
it does no harm. The hard part of the prize problem is not the representation. It is that the wheel is kicked by a
chaotic medium, and nothing yet shows that the kicks can never conspire.

**Where the right coordinates did matter today: the left side.** In the pyramid's own coordinates, time and position,
the left side looks like part of a two-dimensional chaos. In left-edge coordinates it is a closed one-dimensional
system (§8.31). Rowland's 2006 question then became a two-minute computation with a proof certificate. Choosing
coordinates that fit the object is the lesson from the shaders that does carry over.

### 8.33 The entropy squeeze: a period-2 counterexample must be almost frozen (2026-10-05)

This is lead 2 of the open leads (the owner's choice, 2026-10-05). Write $p_s(n)$ for the number of different stretches
of length $n$ that a sequence $s$ ever shows, and $h(s) = \lim_n \frac{1}{n} \log_2 p_s(n)$ for its *topological
entropy*, in bits per step. Coin flips have $h = 1$, and a periodic sequence has $h = 0$.

**Lemma (the squeeze).** Let $x$ be any configuration of Rule 30 whose column 0 is $0101\ldots$ from time 0. Then
every column to the left of column 0 has

```math
h(\text{column } {-k}) \;\le\; \tfrac12 \log_2 \lambda_{26} \;\le\; 0.0646 \text{ bits per step}, \qquad k = 1, 2, \ldots
```

and at most $4 \times 320{,}528 \times 2^{0.1292 \lceil j/2 \rceil}$ different patterns of width $j$ ever appear just left
of column 0, the same bound for every such configuration. (In fact column −1's entropy is exactly half that of
column 1's visible bits, whose bound is the certified $\log_2 \lambda_{26}' = 0.1292$.)

*2026-10-06, Local.* The certificate now reaches $m = 28$ (`rule30_squeeze.py 27,28 mmap`, SQ6; the pool mapped on the
NVMe as in §8.20's note): $\log_2 \lambda_{27}' = 0.1243$ and $\log_2 \lambda_{28}' = 0.1236$, each checked in exact
rational arithmetic, a bound $10^{-3}$ below $\lambda$ rejected at each. So the lemma holds with **0.0618 bits per step**
in place of 0.0646, and the pattern bound with $2^{0.1236 \lceil j/2 \rceil}$ and the constant 135,663 in place of
320,528. Every sentence below that uses 0.0646 stands with 0.0618.

*Proof.*
1. **Column 1 is a narrow channel.** By §8.20, every stretch of $n$ visible bits of column 1 (the even times)
   lies in the language $L_{26}$ of a 26-cell layer. Restarting the configuration at any even time gives another
   configuration with the same column 0, so this holds for every stretch, not only the first. Hence
   $p_v(n) \le |L_{26}(n)| \le 320{,}528 \times 2^{0.1292\,n}$.
2. **Column −1 is column 1 turned over.** The rule at column 0 reads
   $x_t(-1) = x_{t+1}(0) \oplus (x_t(0) \lor x_t(1))$. So $x_t(-1) = 1$ at odd $t$, and
   $x_t(-1) = \lnot x_t(1)$ at even $t$. A stretch of column −1 is fixed by its starting parity and half as many
   visible bits, so $h(\text{column} -1) \le \tfrac12 h(v)$.
3. **Entropy cannot grow leftwards.** Rule 30 is left-permutive:
   $x_t(j-2) = x_{t+1}(j-1) \oplus (x_t(j-1) \lor x_t(j))$. Each pair of neighbouring columns is computed from the
   pair to its right over two consecutive times, and a computed sequence has no more entropy than what it is computed
   from. Column 0 is periodic and adds nothing.
4. **Patterns.** A width-$j$ pattern just left of column 0 is computed from columns −1 and 0 over $j$ consecutive
   times. $\square$

**The arithmetic is certified.** $\lambda_m$ had been found by power iteration, which is not a proof.
`rule30_squeeze.py` now certifies it for every width up to 26. For a non-negative matrix $A$, a positive vector $w$
with $Aw \le \lambda' w$ proves the growth rate is at most $\lambda'$ (the Collatz–Wielandt bound). Such a $w$ was
computed and checked in integer arithmetic, with predictions written first:

| Layer width $m$ | 8 | 12 | 16 | 20 | 24 | 26 |
|---|---|---|---|---|---|---|
| Certified bound, bits per visible bit | 0.3577 | 0.2593 | 0.2130 | 0.1533 | 0.1342 | **0.1292** |
| Automaton states | 56 | 402 | 2,260 | 12,749 | 67,658 | 179,181 |

As a counterfactual, a bound 0.1% below each true rate is rejected, as it must be (SQ0). Step 1 was also tried on real
data: every 64-bit visible stretch of column 1 from 100 real right halves is accepted by the automata (SQ2), while
none of 10,000 random 64-bit words is (SQ3).

**What it does to a counterexample.** Suppose a finite configuration had column 0 eventually 0101…. Shifting time
keeps it finite, so the lemma applies: **its whole left side would carry at most 0.0646 bits per step, in every column
and in every pattern next to column 0**. The measurements show two worlds (SQ4, SQ5; `rule30_core.py`, CR3):

| Left halves | Fastest growth of a column's stretches, bits per step |
|---|---|
| forced from real right sides (§5: infinite, never finite in any case found) | at most **0.0625**, as the lemma requires |
| left sides of finite seeds, driven by 0101… | at least **0.987**, coin-like |

A period-2 counterexample would be a finite seed in the first world. Its left side would have to be about 15 times
more ordered than any finite seed's ever is, all the way along column 0.

**What it does not do: an independent review.** The lemma and its proof were given to a separate session, asked only
to break them and to search the literature. It found every step sound. It rebuilt the automata for widths 1 to 10
itself and matched §8.20's rates, and checked the identities and bounds on 60 forced configurations. It also found
that the reduction I first wrote down restates the problem. That reduction was: show that some left column of a
finite configuration with column 0 = 0101… exceeds 0.0646. But every configuration with column 0 = 0101…, finite or
not, satisfies the bound, so the target only says that no finite one exists. The review is right. What is left:
- **The meaningful version is left-only, and it is not new.** Drop the right side and keep only the bound it imposes.
  Then the target becomes Conjecture LR (§7) for every column 1 the right side can produce. That is the ladder $LR_m$
  of §8.14, and the squeeze is its entropy shadow. (Equivalently: no finite left seed, driven by 0101…, can keep
  $x_t(-1) = 1$ at every odd time while its column −1 stays below 0.0646 bits per step.)
- **Any proof must use the finite left half.** Configurations with a finite right half all satisfy the bound, so
  right-finiteness, and all the search evidence of §8.21, cannot help. Kopra's whole class of automata cannot supply
  a lower bound either: the review found that Rule 90, which belongs to it, has a two-cell column from a single seed
  with linear complexity, $p(n)$ = 7, 13, 25, 49, 97, 193 for $n$ = 4, 8, 16, 32, 64, 128, which is entropy 0.
- **It needs a kind of statement nobody has proved for Rule 30.** The only known lower bound on any column of a finite
  configuration is $p(n) \ge n + 1$, which is Jen's theorem in the form Kopra uses (Morse–Hedlund). For the single
  seed, even entropy above 0 for the centre column would already prove Prize Problem 1.

So lead 2, in its simple form, is closed as a route. Three things from it remain:
- the certified constant;
- the uniform bound on patterns of width $j$ at every depth, which could help an argument that works near the left
  edge of the light cone;
- the two-worlds measurement.

The literature the review found is in PRIOR-ART.md: Milnor's entropy geometry, which treats a left-permutive map's
"additional causal cone"; Kopra (2023), read in full; and directional entropy, which concerns whole systems rather
than single configurations. None states this lemma.

### 8.34 Where Problems 1 and 2 meet (2026-10-05)

The owner's view that the three problems are a three-body problem fits:
- Problem 3, if true, implies Problem 1. Wolfram notes this: a periodic column would be quick to compute.
- Problem 2, if true, would rule out every odd period and every lopsided block at once, but not balanced blocks like
  01.
- And §8.33 shows where all three are stuck. Each asks for a lower bound on how random Rule 30 is:
  - Problem 2 needs the centre column fully coin-like.
  - Problem 1 for the single seed would follow from any positive entropy at all.
  - Our period-2 case needs entropy above 0.0646 for a finite left seed driven by 0101….

No lower bound of this kind has ever been proved for Rule 30. That one shared obstacle is the structure the three-body
picture reveals. `rule30_core.py` measured the left side in both settings (predictions written first):

| What | Measured |
|---|---|
| single seed: centre column density over $2^{17}$ steps | 0.49947 (within $3/\sqrt n$ of ½) |
| single seed: centre column block entropy $h_{10}$ | 0.9972 (coin flips 0.9971) |
| single seed: densities at depth $2^{16}$, band / between / core | 0.49979 / 0.50016 / 0.50027 |
| left side driven by 0101…, every column, $h_{10}$ | at least 0.9868 (coin flips 0.9886) |
| left side driven by 0101…: how often $x_t(-1) = 1$ at odd times | 0.4998 |
| the universal band's density (exact, 40,000 diagonals) | 319,993 / 640,000 = 0.499989 |

- **Problem 2's evidence holds:** the centre column is coin-like in density and in block entropy (CR2).
- **The period-2 condition is a fair coin flip at every odd time** (CR4). Nothing in the left side's dynamics leans
  towards it. A counterexample needs all of infinitely many flips to come up heads, and the squeeze says the left side
  would also have to be nearly frozen.
- **Balance does not need randomness.** The universal band is completely ordered, every diagonal repeating a block of
  at most 32 cells, and yet its density is ½ to within $10^{-5}$ (CR1, refuted: I predicted it would sit above ½).
  The balance is collective. 80% of the diagonals have unbalanced blocks, and together they average 0.49999 (CR5,
  refuted: I predicted most would be balanced one by one).

So Problem 2's property, equal frequencies, holds in a region with no randomness at all. That leaves room for a
structural reason for balance, which Problem 2's coin-like evidence alone would not suggest. Whether such a reason
reaches the core, where the centre column lies, is open.

### 8.35 Does Rule 30's coin tip? The owner's matter–antimatter question (2026-10-05)

The owner: "I am thinking of the universal problem of why there is more matter than antimatter. The coin flip tips
towards the matter side, and I believe the reason isn't known."

**The physics.** The universe holds about one extra baryon for every billion or so baryon–antibaryon pairs: the
baryon-to-photon ratio is about $6 \times 10^{-10}$. Sakharov (1967) gave three conditions any explanation needs:
- a process that changes the number of baryons;
- violation of C (swapping matter for antimatter) and of CP (doing that and mirroring);
- a departure from thermal equilibrium.

The Standard Model has all three, but its CP violation is far too weak to make the excess. So the cause is unknown,
as the owner says.

**Rule 30 meets all three conditions.**
- The number of black cells is not conserved.
- Swapping colours turns Rule 30 into a different rule (Rule 135), mirroring it gives Rule 86, and doing both gives
  Rule 149. So C, P and CP are all broken.
- The single seed starts as far from balance as possible: one black cell in a white world.

**Yet it makes no excess.** Exactly 4 of its 8 outputs are black, and it maps a row of fair coins to a row of fair
coins (it is surjective). So the balanced state is an equilibrium it cannot leave, and an imbalance at the start is
washed out. `rule30_tilt.py` asked whether anything survives in the centre column, with predictions written first and
centre columns run from rows of fair coins as controls:
- **The control.** Wolfram's black counts at 10, 100, …, $10^6$ steps are reproduced exactly (TI0).
- **No long memory** (TI1 held). The excess of black over white grows like a fair random walk: a DFA exponent of
  0.5045, against 0.49 to 0.51 for the controls.
- **No tilt** (TI2 held). At $2^{21}$ steps the excess is $+1{,}224$, which is $+0.85$ standard deviations. It was
  $-44$ at $2^{10}$, $+282$ at $2^{15}$ and $-138$ at $2^{17}$: the walk crosses zero.
- **Wolfram's table** shows black ahead at every decade from $10^4$ to $10^9$, by 0.6 to 2.0 standard deviations.
  Random walks do that: once ahead, they tend to stay ahead for long stretches.

**What the comparison teaches.**
- **Sakharov's conditions are necessary, not sufficient,** in Rule 30 as in the Standard Model. Here the reason is
  plain: what keeps the balance is not a C or CP symmetry, which Rule 30 lacks, but a balanced and surjective rule.
- **Problem 2 asks exactly the owner's question:** does this rule, started from one black cell, leave a lasting
  imbalance in its centre column? Every measurement says no. That includes the ordered band of §8.34, which is
  balanced to $10^{-5}$ with no randomness at all. A proof is still missing.
- **The analogy has a limit.** Baryogenesis lives in quantum field theory, and nothing here explains it. What carries
  over is the shape of the question: rules that break every mirror symmetry can still keep the books balanced, and
  whether they do is a question about the rule's dynamics, not its symmetries.

### 8.36 Lead 1: the records to depth 65, and a sharp conjecture (2026-10-05)

Conjecture LR for 0101… (§7) says that for every column 1 the forced left half has infinitely many ones. Alone, it
settles period 2 for every finite configuration. It would follow from a growth bound on zero runs, and the records
measure exactly that. $R(d)$ is the longest run of zero cells, starting at depth $d$, that any column 1 can force.

**A faster engine.** `records.c` indexes the forced left half along anti-diagonals, $A_k[j] = x_{k-j}(-j)$. Each one is
then a running XOR of $(A_{k-1} \ll 1) \lor (A_{k-2} \ll 2)$, computed with eight word shifts. The search runs about a
thousand times faster than before. It reproduces every known record, and it agrees with the old Python search at every
depth from 1 to 29 (RC0).

**Measured, every depth from 1 to 61 and depth 65** (`rule30_records.py`, predictions written first):

| Depth $d$ | 9 | 13 | 16 | 33 | 41 | 49 | 56 | 59 | 61 | 65 |
|---|---|---|---|---|---|---|---|---|---|---|
| Record $R(d)$ | 9 | **17** | 16 | 33 | 37 | 39 | 42 | 51 | 49 | 57 |
| Ends at depth | 18 | 30 | 32 | 66 | 78 | 88 | 98 | 110 | 110 | 122 |

- **The doubling law holds** (RC1, RC2). From depth 42 to 65, every record lies between $0.75d$ and $1.35d$ and
  ends between $1.75d$ and $2.35d$.
- **Half a bit per cell** (RC3). Among the $2^{d/2}$ starting prefixes of column 1, those that keep the run going
  halve every two cells: 0.51 bits per cell at depth 57, 0.48 at 65. This is the coin model of §8.14 exactly. Inside
  a run, every other cell can be kept at zero by choosing column 1's newest bit, and each of the others is a fair
  coin.
- **The early bits do not matter** (RC4): 100 different prefixes reach the record at depth 65.
- **No renormalisation is visible** (RC5, the expected null). The record witnesses at depths $d$ and $2d$ share no
  more than chance would give.

**The sharp pattern.** At every depth computed, $R(d) \le d + 4$. The excess reaches 4 only at depths 2 and 13, and is
0 at depths 1, 4, 9, 15, 16 and 33. Over depths 20 and up it averages −7.3. In words: **no zero run starting at depth
$d$ has reached past depth $2d + 4$.** The run ends form plateaus: one long run ending at a fixed depth serves a whole
range of starting depths, since $R(d+1) \ge R(d) - 1$ always.

**The doubling conjecture.** For every column 1, a zero run of the forced left half for 0101… that starts at depth
$d$ ends by depth $2d + 4$.

It implies Conjecture LR for 0101…, because from any depth there is a one within about twice that depth. With
Condrey's theorem, that settles every finite configuration for periods 1 and 2. It is the coin model's prediction
stated as a bound, so the data fit it without showing why it should hold. Local's job M4 tests it blind at depths 69
to 77 (prediction M4c, added before any Local run).

**What a proof would need.** Inside a run, column 1's newest bit is forced at every other cell. So a run of length
$r$ is a system of about $r/2$ Boolean equations in the $d/2$ free bits of the prefix. The conjecture says that the
system has no solution once $r > d + 4$: its equations are never so dependent that they leave a solution after about
as many equations as unknowns. If the equations were linear over GF(2), a rank argument would do it. They are not:
the counts of record-setting prefixes (3, 5, 11, 21, 12, 44, 54, 96, 100) are mostly not powers of 2, as solution
sets of linear systems must be. So the next question is what structure these equations do have. This is again the
uniform cost of a zero cell, the kind of statement §8.33 found nobody has proved, but now in the form of one finite
algebraic system per depth.

### 8.37 Local's depths 69 to 81, and the owner's Enigma lead (2026-10-05)

Local ran job M4 on the M5 (10 cores) exactly as written. The verdicts are in `rule30_records.py` (OUTCOME of JOB M4)
and the raw lines in `rule30_records_local.txt`.

| Depth $d$ | 69 | 73 | 77 | 81 |
|---|---|---|---|---|
| Record $R(d)$ | 55 | 59 | 63 | 65 |
| Ends at depth | 124 | 132 | 140 | 146 |
| $R(d) - d$ | −14 | −14 | −14 | −16 |

**All three predictions held** (M4a, M4b, M4c). In particular the doubling conjecture of §8.36 holds at every depth
run, with 18 to 20 cells to spare. M4c had been committed before Local's run began. Since depth 49 the records have
settled near $R(d) \approx 0.8\,d$, ending near $1.8\,d$. Local also reproduced Cloud's records at depths 53, 61 and
65 on a second machine. Depths 85 and 89 came in on 2026-10-05 and 2026-10-06 ($R = 73$ and $75$; the three
predictions and Cloud's MG8 held at both), with the same three predictions carried to them before
either result existed.

**The owner's Enigma lead** (Local's probes, predictions written first). Turing and Welchman broke Enigma by running a
known plaintext, the crib, through the machine and letting contradictions prune the keys.
- **The crib route does not transfer.** Asked as a satisfiability problem, "is there a column 1 whose forced left half
  has zeros at depths $d$ to $d + R - 1$?", the solvers kissat and CaDiCaL find every record correctly (S0). They are
  slower than plain enumeration, though (S1 refuted). At depth 41 a record witness takes 58 to 117 s against
  `records.c`'s 3 core-seconds, and at 53 none was found in 600 s. The reason: an Enigma crib letter carried about
  4.7 bits through one step of wiring. Here a crib cell carries half a bit through a circuit about $d$ steps deep, and
  every OR gate stops backward propagation unless its other input is already known.
- **The Bombe's parallel test does transfer.** At a free step, column 1's newest bit enters the depth-$k$ cell's
  parity through one OR gate whose other input is $\tau(k-1) = 0$. So the two choices give complementary cells, and
  exactly one continues the run (Lemma 4 made exact). **A prefix's zero run is therefore one forced walk, not a
  search.** `records_bits.c` runs 64 prefixes' walks in lockstep in a machine word, the way the Bombe tested many
  hypotheses at once. It is about 12 times faster than `records.c`, with identical outputs at every depth checked
  (1 to 57, 69 to 77). `records_fast.c` adds a carry-less multiply for the running XOR (1.35 times).

**What it means for the proof.** The record at depth $d$ is now the longest of $2^{\lceil (d-1)/2 \rceil}$
deterministic walks, each of which survives a cell only when a determined bit comes out 0. The doubling conjecture
says no walk survives more than $d + 4$ cells. The slack is growing: the measured records fall 14 to 16 cells short of
the bound at depths 69 to 81.

### 8.38 Why the records stop at 0.8 d: the walks merge (2026-10-05)

§8.37 left one number unexplained. If the $2^{d/2}$ prefixes of column 1 gave independent walks, each a fair coin
at every other cell, the best of them would last about $d$ cells. The records last about $0.8\,d$. Two probes, with
predictions written before each run, find where the missing walks went.

**Single bits do not explain it** (`rule30_influence.py`). Flip one bit of a random prefix and see whether the run
changes. From time 12 on, every bit changes it with probability 0.63 to 0.69. That is the coin's $2/3$, the chance
that two independent runs differ. Only the first two or three bits are weak (IN2 refuted).

**Whole walks merge** (`rule30_merge.py`). The walk from depth $k$ depends only on two anti-diagonals, and part of
the older one is hidden. In $(A_{k-1} \ll 1) \lor (A_{k-2} \ll 2)$, a bit of $A_{k-2}$ cannot be seen wherever the bit
of $A_{k-1}$ beside it is 1. Mask those bits. Two prefixes that reach the same masked pair are one walk from then on,
exactly (MG0b). The count of distinct pairs over every prefix reproduces `records.c`'s record and full histogram at
every odd depth from 21 to 45 (MG0c).

| Depth $d$ | 21 | 29 | 37 | 45 | 53 |
|---|---|---|---|---|---|
| Prefixes $2^{(d-1)/2}$ | 1,024 | 16,384 | 262,144 | 4,194,304 | 67,108,864 |
| Distinct walks $D(d)$ | 303 | 3,006 | 29,753 | 291,014 | 2,819,694 |
| Fraction | 0.30 | 0.18 | 0.11 | 0.069 | 0.042 |

- **Every step merges about 6% of the walks** (RQ3), at free and non-free steps alike. So each free bit multiplies
  the walks by about 1.764 instead of 2 (MG1, RQ2). The rate drifts slowly, from 1.778 at depth 31 to 1.764 at 51.
  It obeys no linear recurrence of order 12 or less (RQ1 refuted), so no finite automaton is visible behind it.
- **The OR is the whole mechanism.** With XOR in its place, no two prefixes ever merge (the counterfactual).
- **Nothing merges inside a run** (MG2 refuted). Once the run starts, the distinct walks and the prefixes both halve
  every two cells: the coin rate.
- **So the record is the coin's best over $D(d)$ walks**, not over $2^{d/2}$ prefixes (MG3). The longest of $n$
  independent coin runs is about $2\log_2 n + 1.67$ cells, which gives $R(d) \approx 0.826\,d + 0.8$. This count,
  made at depths 45 and below, predicts Cloud's and Local's records at the 12 depths from 49 to 81 with a mean error
  of −0.9 cells and none larger than 4.1.
- **A record is one walk** (MG5). At 11 of the 16 depths from 41 to 81, every listed record prefix follows the same
  walk, and there are never more than three.
- **The merging is not confined to the early bits** (MG4, MG6 refuted). At depth 41, classes join prefixes that
  differ as late as time 30.
- **The chaos step, from the owner's lightning channels** (MG7). Rivers merge too. In Scheidegger's river network
  the streams coalesce like random walks, so the distinct ones fall only as a power of the distance. Here a fixed
  fraction merges at every step, so the loss is exponential. At depth 45 the classes peak at 16 to 31 prefixes, and
  the largest has 284.

**What it means for the proof.** The doubling conjecture now has a mechanism, but still no proof. There are about
$2^{0.41\,d}$ distinct walks, so the coin model's record is $\log_2 1.764 \approx 0.82$ of the depth. The bound
$d + 4$ is therefore about $0.18\,d$ cells of slack, not luck. A proof by this route needs two statements:
1. **A merging lemma.** The distinct walks number at most $c\,\mu^{d/2}$ for some $\mu < 2$. I first called this
   the provable half. It is not easier. A difference between two walks passes through an OR gate whose other input
   is white and is stopped only where that input is black. So a steady merge rate means black cells keep appearing,
   which is the original problem's own flavour. It also fits the finding that nothing merges inside a run, where the
   cells are white.
2. **A uniform cost.** No walk beats the coin's best by $0.18\,d$ cells. This is again a uniformity statement about
   deterministic walks, the kind §8.33 found nobody has proved for Rule 30.

The merging moves the problem without solving it. It does make the target quantitative: a proof may lose up to
$0.18\,d$ cells against the coin model and still settle period 2.

### 8.39 The same problem as Rule 30 against a wall (2026-10-05)

The forced left half has a plainer description, with no diagonals and no column 1 (`rule30_wall.py`, predictions
written first). At column 0, the left-parent rule $x_{t+1}(0) = x_t(-1) \oplus (x_t(0) \lor x_t(1))$ says two things.
At even times it fixes column 1. At odd times, where $x_t(0) = 1$, it says $x_t(-1) = 1$. The left half meanwhile
evolves forward by Rule 30 using column 0 alone. So:

**The wall form.** Run Rule 30 on the half-line $x \le -1$, against a wall at $x = 0$ that is white at even times and
black at odd ones. The forced left halves for 0101… are exactly these evolutions in which **the cell beside the wall
is black at every odd time.**

- The free data are row 0's cells at odd depths. Each odd time's condition fixes the next even-depth cell, through
  the left edge of its light cone, which is pure XOR. Column 1's free bits and row 0's odd cells determine each other
  one by one (WA1).
- The control: the wall evolution reproduces the forced left half cell for cell (WA0). The longest wall run equals
  `records.c`'s record at every depth from 3 to 27 (WA2). The wall in the other phase gives exactly $R(d - 2)$: the
  same problem one time step later (WA3, a weak counterfactual).

In this form, the open statements read:
- **Conjecture LR for 0101…:** no row 0 that is white beyond some depth can keep the wall's neighbour black at every
  odd time.
- **The doubling conjecture:** if row 0 is white from depth $d$ on, the wall's neighbour is white at some odd time by
  $2d + 3$.

This is a question about Rule 30 alone: a finite pattern growing beside a periodic wall. Condrey proved the period-1
analogue (arXiv:2609.09431): there the wall is constant, and the forced left half has an explicit structure. Here
the left half is Rule 30's ordinary chaos, and the condition at the wall is one coin per two time steps.

### 8.40 Black, white, both: the owner's three games, for every word up to period 4 (2026-10-05)

The owner's lead: we learned from the left half alone, from the right half alone, and from both together. In the
same way, white by itself matters as much as black. The wall form (§8.39) splits along exactly those lines. Let
$w$ be any repeating centre word. At a time when the wall is black, the centre update gives a condition on the left
half alone: $x_t(-1) = 1 - w_{t+1}$. At a time when the wall is white, it couples the two halves:
$x_t(-1) \oplus x_t(1) = w_{t+1}$. A finite configuration whose centre column is $w$ must keep both kinds. So there are
three games, each played from left and right seeds of width $s$ and scored by the longest time $T$ the conditions
survive (`rule30_words.py`, predictions written first):
- **Black alone** ($T_B$): left rigidity, Conjecture LR for $w$.
- **White alone** ($T_W$): the coupling only.
- **Both** ($T_{BW}$): the real problem.

The words are the eight centre words of period up to 4, and the chaos step is a random wall.

| Centre word | Black share | Walks per free bit | $s$ | $T_B$ | $T_W$ | $T_{BW}$ | Slope of $T_{BW}$ |
|---|---|---|---|---|---|---|---|
| 0 | 0 | none | 16 | never fails | 16 | 16 | 1.00 |
| 1 | 1 | none | 16 | 17 | never fails | 17 | 1.00 |
| 01 | 1/2 | 1.77 | 11 | 17 | 40 | 16 | 1.34 |
| 001 | 1/3 | 1.73 | 12 | 29 | 24 | 16 | 1.37 |
| 011 | 2/3 | 1.80 | 10 | 16 | 45 | 16 | 1.27 |
| 0001 | 1/4 | 1.72 | 13 | 47 | 26 | 19 | 1.07 |
| 0011 | 1/2 | 1.76 | 11 | 22 | 29 | 15 | 1.09 |
| 0111 | 3/4 | 1.79 | 9 | 11 | 56 | 11 | 1.27 |

**The controls held.** The census reproduces `records.c` for 01, and the wall's black game agrees with the census for
every word, two instruments. Both never outlasts either game alone. For $w = 1$ the forced left half is vertical
stripes, Condrey's known answer. One flaw was found and fixed in the open. For the all-white wall, the games first
admitted the all-white configuration, which keeps every condition for ever. Condrey's theorem concerns nonzero
configurations, so a corrected run leaves that one configuration out.

What the three games show:
- **One colour has a bounded law, two colours do not.** The two period-1 walls are the solved case, and both are
  exact. The best configuration of width $s$ keeps the column constant for at most $s + 1$ steps, an excess of at
  most one beyond its seed, with no coin anywhere. That is the structure Condrey's proof uses. Every two-colour word
  instead has an excess that grows with $s$, as Condrey said no bounded law can exist at period 2.
- **Both binds hardest, and slowly.** For every two-colour word $T_{BW}$ grows with slope 1.07 to 1.37 (WD5). The
  right seed buys only 0.07 to 0.37 extra steps per cell. That fits the narrow channel of §8.17, through which its
  bits must reach the wall (not tested here). Where the black game is long, both cuts it down: for 0001 at
  $s = 13$, from 47 to 19.
- **Black alone merges the same way for every word** (WD1). Each free bit multiplies the distinct walks by 1.72 to
  1.80, and for five of the six words the records follow the coin's best over those walks to within 2.1 cells.
  The sixth, 001, is off by 4.5 (WD2 refuted), because one long run ending at depth 88 serves twelve starting
  depths.
- **White alone is not a coin game** (WD4 refuted). Its growth is irregular from word to word. On the all-white wall
  it is exact: $s + (s \bmod 2)$.
- **The chaos step: periodicity helps** (WD6 refuted). A random wall merges less, 1.94 walks per free bit against
  1.72 to 1.80 for every periodic word. A repeating centre makes more walks coincide, and so leaves fewer to search.

**What it means for the proof.** The owner's split puts the solved case and the open one side by side. With one
colour, the wall's conditions are exact and leave no slack, which gives a bounded law, proved. With two colours, a
coin enters at every time. The left half alone (black) is then a coin game over merged walks. The combined game
(both) stays near $T \approx s$, which fits the narrow channel. Turning that into a proof brings back lead 2's
squeeze (§8.33). The channel bound is a theorem (§8.20: at most 0.064 bits per step next to 0101). The other half,
that keeping the wall's conditions costs more information than the channel delivers, is the lower bound nobody
has. That is the ouroboros the owner named. Every form of the problem leads back to one statement: the conditions
at the wall cost real information.

### 8.41 The information race, counted (2026-10-05)

Every form of the problem has led back to one statement: keeping the wall's conditions costs real information.
The combined game of §8.40 can be counted exactly (`rule30_race.py`, predictions written first). Take a finite
configuration with seeds of width $s$. The left seed can meet every condition before time $s$, so all $2^s$ right
seeds survive to $s$. After that, each time step brings a condition, and the only new information is what the right
seed delivers to column 1. Survival depends only on column 1's word, so the count that matters is $M(s, T)$: the
distinct column-1 words among the survivors.

- **The right seed delivers about a third of a bit per cell** (RA2). By time $s$ the $2^s$ right seeds of width $s$
  produce only $2^{0.37 s}$ distinct column-1 words: 26 at $s = 12$, 49 at $s = 16$. This is the bottleneck again.
- **Beyond the seed, the conditions destroy it** (RA1): 0.5 to 0.95 bits per step, net of what still arrives.
- **The race roughly balances** (RA3, held at four of five sizes). The time a configuration wins beyond its seed is
  about the information delivered divided by the net cost per step.
- **No Chebyshev-type identity is visible** (RA4, the null held). The exact survivor counts obey no short recurrence,
  and their divisibility by powers of 2 shows no pattern.
- **The solved case shows what the missing half looks like** (RA5). Next to a white wall, column 1 obeys
  $x_{t+1}(1) = x_t(1) \lor x_t(2)$: once black it stays black. So the right seed can deliver only the time of the
  first black cell, exactly $s$ different words, and the conditions destroy all of that within one step. There, the
  cost of a condition is not a coin but a certainty, and that exact structure is what Condrey's proof uses.

**What it means for the proof.** The race has two halves:
1. **The delivery side has a theorem:** the channel bound of §8.20.
2. **The cost side has a theorem only next to a white wall,** where column 1 is monotone.

Next to 0101, column 1 is the wheel with its kicks (§8.10 to §8.20), and nothing yet says what a condition costs
there. The precise target is the 0101 version of RA5: an exact property of column 1 next to 0101 that makes the
forced walk's demands too costly, as monotonicity does next to a white wall.

**A correction, and a failure of method.** I first proposed to look for that property among the local rules of
column 1 next to 0101: Lemma 3's "no two visible ones in a row" and the wider layer languages of §8.20. The ladder of
§8.12 to §8.14 had already done exactly that. With column 1 held to what a layer of $m$ cells can produce, the zero
runs still grow with depth at every width up to 16, at about one bit per cell ($R \approx \log_2 G$). The check of
this document's own earlier sections came after the proposal, not before it. Read together, the two results give
a sharper dichotomy:
- **Next to a white wall the channel's entropy is 0** (§8.20 reads 0 there). Column 1 can deliver only about
  $\log_2 s$ bits, and the law is bounded.
- **Next to 0101 the channel's entropy is positive.** It levels off near 0.12 bits per visible bit, at every layer
  width computed. A positive-entropy channel lets the runs grow, slowly, as a coin game.

So no local rule of column 1 can give the bounded law for 0101. The cost side has to come from the left half's
forced cells themselves.

### 8.42 One law for every word: total width plus a logarithm (2026-10-05)

§8.24 found that for 0101 a finite seed keeps its centre column on the word for at most 9 steps beyond its own total
width, for every right half up to 32 cells. `rule30_uniform.py` asks whether that is one law for every centre word,
with predictions written before each of three runs. The 0101 values of §8.24 are its control, and they were
reproduced exactly.

| Centre word | 01 | 001 | 011 | 0001 | 0011 | 0111 | random | 1 | 0 |
|---|---|---|---|---|---|---|---|---|---|
| Largest excess, cuts to depth 126 | +9 | +10 | +9 | +7 | +7 | +7 | +6 | +1 | 0 |

- **The same small constant at every two-colour word** (UW1), and even for a random centre column (UW4). The
  one-colour words are exact, as Condrey's structure requires: no zero run longer than one (UW3).
- **But the constant is really a logarithm.** Let the cuts go deeper and some excesses grow: for the random wall,
  from +5 at depth 64 to +9 at 512; for 0001, from +5 to +10. For 01 and 001 the excess stayed flat to depth 512.
  That looked like a property of periodic words, and I said so before testing it. The direct test refuted it (UV1):
  the longest deep zero run for 01 grows from 14 cells at depth 128 to 21 at depth 2048, faster than the random
  wall's. The excess stayed flat only because a small seed's shallow champion stays ahead of the deep runs, which
  need wider seeds. The longest of N coin-flip sequences over n cells is about $\log_2(nN)$ cells: 21 for the
  measured case.
- **Wider right halves usually do worse** (UW2 refuted by one word, 0011), because their extra bits arrive too late.

**What it means for the proof.** Across every word tested, a finite configuration of total width $w$ keeps its
centre column on a given word for about $w$ plus a logarithm steps. Each condition at the wall costs a bit, and luck
adds the logarithm, as Cramér's model adds it to prime gaps. Any finite bound settles Problem 1 for a word, and this
one would do it uniformly over all periods. **But the law holds for a random word too**, so it cannot be proved
from properties every word shares. It fails exactly for the countably many words that are some finite
configuration's actual centre column. A proof must therefore use what makes periodic words special, as Jen's
theorem and Condrey's proof do. In these statistics, nothing distinguishes the periodic words from the random one.

### 8.43 What sets a kick's size? The owner's drifting hole (2026-10-05)

The owner, recalling the interpolation shaders: "under rotation they would always reveal an oscillating,
string-like hole at the centre, and under rotation and translation combined it would drift." Read here, a domain
wall (§8.7) is a string moving through the wheel's rotating pattern. If the pattern's phase lags from column to
column at a rate other than the wall's speed, the mismatch a wall carries grows with the distance it travels, and
the kick's size would be set by where the wall formed. That question had been open since §8.8. `rule30_kicks.py`
tested it and three alternatives, each with predictions written first, on 11,437 slips. The controls held: the
commonest kicks (+3 for class 32, −3 for class 52), and shuffled features that add nothing.

What might set the kick, and what the data say:
- **Where the wall formed** (the owner's drift, KK2): a little. It tells 0.21 bits of the 1.93 that remain after
  the class. Class-32 walls traced to column 12 kick +6 in 218 of 304 cases, against +3 for the rest.
- **The wall's width** (KK3): void. Column 1 takes up its new phase at once, so the width is always 0.
- **The phase of the domain behind the wall, read before arrival** (KK1, FD1): mostly not. It is exact in 20% of
  slips. It is found ahead of the arrival in at most 9.4%, near a 5.6% background (FD0 failed: those outer reads are
  noisy).
- **The cells near column 0 at the moment of arrival** (LC1): no. Columns 1 to 8 predict 56% of held-out kicks,
  against 47% for the class alone.

- **The rigid part of a kick is the boundary's.** Each wall arrives at one of two phases of the wheel, the phase
  fixes the sign, the size is a whole number of notches, and column 1 switches to its new phase in one step.
- **The size is not.** It comes from beyond the coherent layer, so it is the chaotic interior's information
  entering through the boundary. That matches §8.11 (the kicks have no memory, and a coin-flip interior turns the
  same wheel) and §8.20 (about 3.5 bits per kick).
- **The owner's picture, in part.** The phase behind a wall is layered, with steps between bands of columns that
  move toward column 0 over the following 30 steps (an exploratory look, recorded in the probe's header). Distance
  travelled carries a little information. But the drift does not set the kick.

**What it means for the proof.** The wheel's rigidity is in the timing and the alphabet of its kicks, not in their
sizes. A finite configuration's column 1 is therefore, after the wheel forms, a wheel kicked only at two phases per
turn, by whole notches, with sizes the adversary does not control but that range over the alphabet. That defines a
narrower game than the ladder of §8.12, where the adversary feeds a layer anything at all. **The kick game asks
whether a wheel kicked like this can hold the left half at zero for long.** It was proposed in §8.8 and never run as
such. If its runs grow more slowly than the ladder's, the wheel's rigidity is a lever a proof can use.

### 8.44 The kick game: the wheel's rigidity is a constraint, not a bound (2026-10-05)

§8.43 left one candidate lever: a wheel can only be kicked at its arrival phases, by whole notches of a small
alphabet. `rule30_kickgame.py` plays that game, with predictions written first. Column 1 is the wheel $U$ at any of
its 28 even phases. It is kicked only at the three arrival phases of its 56-step cycle, by sizes from each class's
alphabet, and only when column 1 departs at that moment. The adversary chooses the starting phase and every kick.
$R_K(s)$ is the longest zero run of the forced left half from depth $s$. The control held: with kicks disabled the
game reproduces the pure wheel exactly, phase by phase, against an independent cell-by-cell computation (KG0).

| Depth $s$ | 41 | 49 | 57 | 65 | 73 | 81 | 89 | 97 | 105 |
|---|---|---|---|---|---|---|---|---|---|
| Kick game, $R_K(s)$ | 8 | 9 | 12 | 13 | 15 | 23 | 16 | 18 | 21 |
| $\log_2$ of its distinct column-1 histories | 8.7 | 10.2 | 11.6 | 13.1 | 14.5 | 15.9 | 17.4 | 18.8 | 20.2 |
| The ladder at width 12 (§8.14) | 8 | 11 | 10 | 13 | 16 | 14 | 16 | 16 | 20 |
| Real right halves up to 12 cells (§8.14) | 6 | 9 | 10 | 10 | 8 | 8 | 9 | 9 | 10 |

- **The timing is a real constraint** (KG3 held). Allow kicks at every even time and the run from depth 41 is 23,
  not 8.
- **But it is not a bound** (KG1 refuted). The game's runs grow with depth, and at four depths they beat the
  width-12 ladder's.
- **It is the coin law again** (KG2 held at eight of nine depths). The run is about $\log_2$ of the number of
  distinct column-1 histories the game allows, which grows by about 0.18 bits per step.
- **Real right halves stay far below the game.** Their kicks arrive less often (about one every 88 steps, against
  the game's two chances per 56), and their sizes are not chosen.

**What it means for the proof.** The wheel's rigidity (its arrival phases, its notched alphabet, its instant
switch) cuts the adversary's freedom but leaves a positive entropy rate. Every game with positive entropy has the
coin's growing runs. Only the constant walls have zero entropy, and only they have a bounded law (§8.41). So for
0101 the wheel's structure cannot by itself give the bound. A proof still needs the cost side: the real kicks,
coming from Rule 30's own interior, must pay a bit for every condition the left half imposes. The wheel narrows the
search for that statement, from any column 1 to a kicked rotation, but does not supply it.

### 8.45 Mahler's 3/2 problem has the same structure, and stops in the same place (2026-10-05)

Kopra's class of rapidly left expansive cellular automata contains Rule 30 and the automata that multiply by a
fraction $p/q$ (PRIOR-ART, "Rule 30's siblings in arithmetic"). On the multiplication side, the question of the
same shape is Mahler's 3/2 problem (1968), still open. It asks whether some $\xi > 0$ keeps every fractional part
of $\xi (3/2)^n$ below $1/2$. Flatto, Lagarias and Pollington (1995) proved its strongest partial result: the
fractional parts of $\xi(p/q)^n$ cannot all fit in an interval shorter than $1/p$. Reading their proof shows the same
skeleton as this work's wall form.

Side by side, Mahler's method (FLP 1995) and Rule 30's period 2:
- **The free side.** There, the integer parts form a full shift: every itinerary occurs once, by residues mod
  $q^k$. Here, the left half at the wall is a full shift too, with itinerary and seed in bijection (WA1, §8.39).
- **The constrained side.** There, the fractional parts follow a linear mod-one map with few admissible strings
  ($c\beta^k$). Here, column 1 is a kicked rotation with few admissible words (the channel bound, §8.20).
- **The object sought.** There, a Z-number: the two itineraries agree for ever. Here, a finite configuration with
  centre 0101: the wall's conditions hold for ever.
- **Sparsity.** There, fewer than $x^\gamma$ Z-numbers below $x$ (Theorem 1.1). Here, the entropy squeeze (§8.33).
- **Emptiness.** There, it is proved when only finitely many fractional orbits are admissible (Theorem 3.2). Here,
  Jen's theorem (periodic column 1) and Condrey's constant walls (monotone column 1) are the same kind of case.
- **Open.** There, Mahler's interval 1/2, where infinitely many orbits are admissible. Here, the 0101 wall, where
  column 1 has positive entropy.

The proof of emptiness, in both settings, runs the same way. If the constrained side has only finitely many
behaviours, pigeonhole makes the coupled orbit periodic, and the free side's injectivity forbids that. Where the
constrained side has positive entropy, nothing forces periodicity, and the method stops. Rule 30's period 2 sits
there, as Mahler's own conjecture does.

**What it means.** This is a calibration, not a route. It places the problem precisely: a Mahler-type problem in the
regime where the decoupling method has not worked for 57 years. It also explains, in one frame, everything this
document has found:
- the solved cases are exactly those where every admissible column 1 is eventually periodic (§8.40, §8.41;
  corrected, see below);
- the counting results give sparsity but never emptiness (§8.33, §8.41);
- the wheel's rigidity narrows the constrained side without making it finite (§8.44).

A new idea would have to do what nobody has done for Mahler's problem: get emptiness from a constrained side of
positive entropy.

*Corrected 2026-10-05, after the wide survey (§8.47).* The list above first said "the zero-entropy ones". Zero
entropy alone is not enough. A Sturmian column has zero entropy and is not eventually periodic, and FLP's
Theorem 3.2 assumes finitely many admissible orbits, which is stronger. What the solved cases use is that each
admissible column 1 is eventually periodic. Next to a white wall it is monotone, $0^k 1^\infty$. A sequence
with at most $n$ distinct words of some length $n$ is eventually periodic (Morse and Hedlund; Kopra's Lemma
4.2), and Jen's theorem then finishes. Between the two regimes lies a third, untested here: columns 1 with zero
entropy that are not eventually periodic.

### 8.46 Is it unresolvable? The owner's Turing question (2026-10-05)

The owner: "if the zeta function always returns zeros, and prime numbers continue to infinity, and everything we do
restates the problem in a different way, is this not a kind of proof in itself, the infinite regression, or, as
Alan Turing might put it, unresolvable?"

- **A restatement is not a proof.** Equivalent statements share one truth value, so moving between them cannot
  settle it. What the restatements did show is narrower and useful. They did not regress without end; they
  converged. Every form of period 2 tried here (§8.38 to §8.45) ends at one missing statement: a condition at the
  wall costs real information. That is localisation, the problem's core isolated, not an infinite regress.
- **Turing's theorem is about methods, not single questions.** On computable numbers (1936) shows that no single
  algorithm decides every question of a kind. By Rice's theorem, for example, no algorithm decides, for every
  machine, whether the number it prints is rational. Rule 30's centre column is one computable number. Whether it is
  rational is a definite yes or no (§8.23), as open questions about single constants are. Closer kin:
  - Conway (1972) proved that a generalised Collatz problem is undecidable, while Collatz's own problem is simply
    open.
  - Rule 110 is universal (Cook, 2004), so column questions about general automata are undecidable. Rule 30 is not
    known to be universal.
- **Could it be unprovable?** In logical form, "the centre column is never eventually 0101" says that for every
  time there is a later one where the pattern breaks: a $\Pi_2$ statement. True statements of that form can be
  unprovable in a given system; Paris and Harrington (1977) gave a natural one for Peano arithmetic. Nothing here
  points that way, and showing it would itself be a major theorem.
- **Infinite does not mean undecidable.** Euclid proved that the primes go on for ever with a finite argument, a
  size argument: multiply the primes you have, add one. Bertrand's postulate fell the same way (PRIOR-ART). The
  missing statement here is of that kind: a finite reason why an infinite run is impossible. Nobody has found it
  yet, here or in Mahler's problem (§8.45). That is a statement about the state of mathematics, not about the
  problem's decidability.


### 8.47 The wide survey: nature, the other disciplines, and OpenAI's claim (2026-10-05)

The owner asked for one more research road before fresh eyes, as wide as possible: "Our Rule 30 problem paints
itself on the back of a snail shell: that's evolution, that's generations, that's the golden (silver) ratio, in
the wild." Then two notes: protein folding and the cell's machinery, and the Game of Life. Seven survey agents covered
biology and nature, physics and chemistry, mathematics, computing and engineering, the long shots (history,
astronomy, the arts), molecular machinery, and the Game of Life. The sources, with what was checked, are in
PRIOR-ART ("The owner's wide survey").

**One answer from every domain.** Every theorem found of the form "a low-information drive cannot hold a chaotic
system in a fixed state" is about **sets** of starting states, never about **one orbit**:
- in control theory, a set with interior can be held only if the data rate exceeds its feedback entropy (Nair,
  Evans, Mareels and Moran, 2004), and each bit a controller gathers buys at most one bit of order (Touchette and
  Lloyd, 2000). Yet OGY control holds a chaotic system on one unstable orbit with tiny pushes;
- in sequence matching (Erdős and Rényi; Arratia and Waterman, from DNA), the longest agreement is about the
  logarithm of the number of histories divided by an entropy, almost surely: the coin law of §8.38, as a theorem
  for typical inputs;
- in ergodic theory, two systems of positive entropy are never disjoint (Sinai's Bernoulli factors), so there is no
  obstruction at the level of measures. A proof must work point by point.
The entropy squeeze (§8.33) is a theorem of the set kind. The prize needs the single-orbit kind. The same gap
separates Flatto–Lagarias–Pollington's sparsity theorem from Mahler's conjecture, Tao's "almost all" from Collatz,
and Lagarias's exceptional set of positive dimension from Erdős's conjecture on the ternary digits of $2^n$. The
busy beaver cryptid Antihydra is the same: a coin model says it never halts, and nobody can prove it.

**The tethers, ranked by what they could give.**
1. **The Mahler family** (the same mathematics). Kari and Kopra restate Mahler's problem as a question about one
   column of the automaton that multiplies by $p/q$. That is our kind of question in so many words. Three imports:
   - *Enlarge the window.* FLP's Theorem 3.3 does not beat positive entropy. It moves to a nearby window where the
     constrained side is finite, then uses pigeonhole. The analogue is a weaker condition, implied by the 0101 wall,
     under which every admissible column 1 is eventually periodic, then Jen. The ladder and the channel bound have
     tried every local layer language of column 1 up to width 16, all of positive entropy (§8.14, §8.20, §8.41).
     So such a condition, if one exists, is not local in column 1.
   - *A partial result of a kind not yet tried here.* Kari and Kopra (Theorem 4.9) prove, from ergodicity, mixing
     and compactness, that some finite unions of intervals, approximating the whole interval as closely as one
     likes, hold no Z-number orbit. The proof is not constructive (their Problem 5.1). The Rule 30 analogue would be
     a set of centre-column words, of measure near 1, that no finite configuration can keep to for ever.
   - *A barrier.* Kopra's class contains Rule 90, whose centre column from one cell is eventually constant
     (the survey's reading of Kopra). So no proof can use only what the class shares. It must use Rule 30's OR.
2. **Machine-found certificates** (computing). Yolcu, Aaronson and Heule turned Collatz into the termination of a
   string rewriting system and proved nontrivial weakenings with SAT-found arctic (max-plus) matrix interpretations.
   They also proved that one encoding admits no such proof: the encoding decides. Regular model checking proves
   liveness of infinite-state systems with an automaton invariant plus a well-founded progress relation, learned
   with SAT (Lin and Rümmer). Condrey's horizon $H(2, w) \ge w$ rules out any fixed-depth induction, so the
   certificate must scale with the seed's width, as these do. This is the shape a machine-checkable proof of B
   could take, and the target a large search could aim at.
3. **The wheel's own mathematics, in the wild** (the same mathematics, for item 2 only). The wheel is
   - cardiac parasystole: a beat shows when a rotating phase leaves a refractory window, the number of beats between
     takes at most three values (the three-gap theorem), and in modulated parasystole the sinus beats kick the phase
     (Glass, Goldberger and Bélair);
   - a leap-year rule: the Persian 33-year cycle is seven 4-year blocks and one 5-year block, slipping now and then
     to a 29-year cycle; the wheel is five 10-step blocks and one 6-step block;
   - a Euclidean rhythm, E(17, 56), catalogued nowhere the survey looked; a Frenkel–Kontorova discommensuration;
     a phason walk in a random tiling.
   Two theorems from this group explain measurements of §8.43 rigorously. Piecewise isometries have zero
   topological entropy (Buzzi, 2001), so all of column 1's entropy must come from the kick sizes. Random rigid
   rotations preserve distances, so nothing brings two angles together, and the angle must diffuse with no
   restoring force. (Random circle maps do synchronise unless, as here, they share an invariant measure: Antonov
   and Malicet.) Nature's rotations differ in exactly that respect. Phyllotaxis selects and stabilises its golden
   angle, and Meinhardt's shell models restore their wave count with a hormone. Rule 30's wheel has nothing that
   pulls it back.
4. **Single-orbit theorems from extremal arguments.** Langton's ant's highway is unproved, but Bunimovich and
   Troubetzkoy (1992) proved that every trajectory is unbounded: reversibility makes a bounded path periodic, and
   an extremal cell gives the contradiction. Euclid's primes and Erdős's proof of Bertrand's postulate (a gap
   between two exponents) are the same kind of finite argument for one infinite fact. Rule 30 is not reversible,
   but left-permutivity fixes columns from right to left, which may stand in for it. The import is a target: a
   weaker theorem about every single seed, proved by an extremal argument.
5. **The coin model, proved for typical seeds.** Eloranta and Nummelin (1992) proved that Rule 18's kink performs
   a random walk; Hanson and Crutchfield's domain test is automatic. Together they could prove that the kicks'
   sizes are independent under a random interior. That would be a theorem, and still a statement about sets.

**Protein folding and the cell's machinery** (the owner's note). The biology gives pictures, not theorems; its
mathematics sits at the information end.
- Levinthal's paradox is a counting argument: a random search of a protein's shapes would outlast the universe.
  It is resolved by a bias, a funnel of a few kT (Zwanzig, Szabo and Bagchi, 1992). A period-2 counterexample would
  need Rule 30 to find an exponentially rare state and stay in it for ever, and §8.43 found no funnel: nothing pulls
  the wheel back.
- An information engine that reads a period-2 tape 0101... with phase slips is a published object (Boyd, Mandal
  and Crutchfield, 2017). A synchronising state brings it back into phase, and above a slip rate of $1/(1 + e)$ it
  fails. Its inequality needs an energy and a probability, which Rule 30 lacks. Its formalism, transducers reading
  a tape, describes the sideways rule: each column is computed from the two to its right.
- DNA tiles grow an automaton's space-time diagram from a seed row (Rothemund, Papadakis and Winfree, 2004, with
  XOR tiles), and growth errors propagate as defects. That is the wall form grown sideways, in a test tube. No
  Rule 30 tile experiment was found.
- Invariance entropy (Colonius and Kawan) is the cleanest theorem that holding costs information, and its proof is
  a volume count. It is a theorem about sets, as above.

**The Game of Life** (the owner's note: can Rule 30 emerge from some starting board?).
- **By construction, yes.** Life is intrinsically universal: it simulates any automaton block by block (Durand
  and Róka; Salo and Törmä). LifeWiki's 0E0P metacell has empty space as its off state, so a finite Life seed
  could run Rule 30 from a finite seed. Nobody seems to have built one.
- **Naturally, not in the simplest way.** Life's rule looks the same in a mirror, so a row that stays a row must
  follow a mirror-symmetric rule. Rule 30 is not mirror-symmetric (its mirror image is Rule 86). An infinite line
  in Life follows Rule 22 (Wolfram, NKS notes to §6.8), which is symmetric.
- **Either way it gains nothing.** The centre-column question carries over unchanged, behind an enormous slowdown.
  Undecidability of Life patterns in general says nothing about one pattern. And Life has nothing like
  left-permutivity, the sideways solvability on which the wall form rests. Rule 30's asymmetry is not a detail:
  the whole wall form is built on it.

**OpenAI's claim, compared** (the owner: "it is possible, however unlikely, this may be the same problem worded
differently"). The claim is Navier–Stokes, not Riemann (PRIZE-PROBLEMS.md, the update of 2026-10-05): a smooth
external force and initial data whose solution blows up in finite time, found by about 10,000 agents in 88 hours
and formalised in Lean. Fefferman's official statement allows a force in its breakdown alternative, so a verified
construction would answer the problem as posed.
- **The structure is the opposite of ours.** Theirs is an existence claim, proved by building one object, and the
  force is designed freely: it may carry as much information as the construction needs. Ours is a non-existence
  claim, and the input at the wall is not free: column 1 must come from a finite right half, through a channel of
  about 0.12 bits per visible bit (§8.20).
- **The nearest translation is LR, not B.** A freely designed column 1 is the Rule 30 analogue of a designed
  force. Building one that makes the forced left half eventually zero would refute Conjecture LR (§7). It would not
  touch the prize, which needs B: a column 1 that a finite right half makes. The exact records give no sign of
  such a column: $R(d)$ is finite at every depth computed, and grows about as $0.8\,d$.
- **What transfers is the method.** Their proof is a finite object, found by a large search and checked by Lean.
  Here the finite objects are a seed (a counterexample to B; §8.21 and job M3 search for one) or a certificate (the
  ranking function or automaton invariant of tether 2). A many-agent search plus a proof checker suits both.
So it is not the same problem worded differently. But if fresh eyes come from a system of that kind, its strength
is construction and search. The questions for it are in PERIOD-TWO.md §7.

**A correction found by the survey** (§8.45, corrected in place). Zero entropy on the constrained side is not what
the solved cases use. They use that every admissible column 1 is eventually periodic, which is stronger.

**What it means.** No discipline holds the missing statement. The survey found the same gap everywhere, between a
theorem about sets and a theorem about one orbit. It found where the gap has been crossed: by finiteness (Jen,
Condrey, FLP's windows) and by extremal arguments for single trajectories (Langton's ant). It also showed why
counting is not hopeless here, as it is for measures. The seeds are finite, so an exact count of the
configurations on $w$ cells that keep $T$ conditions, if it falls below one, proves that there are none.
Rule 30's period 2 differs from Mahler's problem in this respect. Mahler's $\xi$ is a real number, and the counting
bounds there (at most one Z-number in each unit interval, at most $x^\gamma$ below $x$) never fall below one. The
live imports are the window idea, the machine-found certificate, the extremal target and the exact count.
PERIOD-TWO.md §7 writes them out as questions for fresh eyes.

### 8.48 The owner's MoltenVK question: randomness that only one platform showed (2026-10-05)

The owner recalled MOLTENVK-NONDETERMINISM-INVESTIGATED.md. On macOS the interpolator's output wandered, and the
cause had two parts. **An amplifier:** block matching picks an argmin over candidate offsets, and at a near-tie a
one-bit difference flips the chosen motion vector "and the whole warp built on it". **A source:** a race in the
MoltenVK path, invisible on Windows and Linux, where nothing perturbed the tie. The owner: "it smells like quantum
mechanics. Might this discovery have an application here?"

**The same anatomy is in Rule 30, and it has been measured.**
- **The amplifier is the XOR.** Rule 30 is $x' = l \oplus (c \lor r)$, so a flipped left input always flips the
  output. The influence probe measured it: flip any bit of column 1 from time 12 on and the zero run changes with
  probability 2/3, the coin's value (`rule30_influence.py`).
- **The tie margin is the OR.** An OR whose other input is 1 absorbs a flip, as `TIE_MARGIN` absorbs a one-bit
  difference at a near-tie. That absorption is the merging of §8.38: walks that differ early reach the same state.
- **The source is the interior.** The wheel next to the wall is the stable platform: a rotation that would repeat
  for ever. The kicks are the race: they come from the chaotic interior, carry its randomness (§8.43), and by Jen's
  theorem never stop in a finite configuration (§8.13). The MoltenVK report's warning fits them exactly: "the tie
  margin cannot absorb a perturbation that is not small", and a kick is a whole notch, never small.

**What it gives.** A picture of the cost side, not a new statement. A period-2 counterexample would be a
configuration where every kick, for ever, lands on a near-tie that the left half's ORs resolve the right way, and
each such landing costs about a bit. That is the coin model again, the restatement the owner has called the
ouroboros. One difference matters. The shader's randomness came from outside, from the platform. A finite Rule 30
configuration has no outside: all of it is in the seed, which is what Wolfram calls intrinsic randomness. So the
fix that worked there, removing the source (the MoltenVK switches and a texture-free dither), has no analogue
here. The source is the configuration itself.

**On quantum mechanics.** A deterministic, local system whose outputs look random is exactly what Rule 30 is, and
't Hooft's cellular automaton interpretation of quantum mechanics (2016) proposes such automata beneath physics.
Bell's theorem limits what local hidden variables can reproduce, and 't Hooft's answer needs superdeterminism. None
of that bears on whether one finite configuration can keep a periodic centre: Rule 30's question is about a single
deterministic orbit, with no measurement and no statistics. The likeness is real as a picture, of a hidden
variable that decides an outcome; it is not a route.

### 8.49 Addendum to §8.47: philosophy and logic (2026-10-05)

The owner: "Many great theorems were devised without even the language of maths. As we found with the 3-sphere,
Dante had a visualisation with absolutely no maths. ... Their math is logic, truth, gates." An eighth survey agent
covered philosophy and logic (PRIOR-ART, the end of "The owner's wide survey"). Four things came back that the
mathematical surveys did not give:
- **The open case, in one picture.** Nietzsche argued that finitely many states must recur. Simmel answered with
  wheels turning at an irrational ratio, which never line up again. Kicks that become periodic make column 1
  periodic, and Jen closes that case. So the open case is exactly a wheel whose kicks never settle into a period,
  Simmel's irrational wheel.
- **The ouroboros, answered from philosophy.** The coin model is a uniformity principle, and more confirming runs
  cannot prove it (Hume). Each restatement adds a premise, and what is missing is a rule of inference (Carroll's
  Tortoise). And by Kripke's quus, finitely many observations fit infinitely many rules: every finite stretch of
  0101 is realised by some seed. A proof must use the finiteness of the seed, as PERIOD-TWO.md §7, question 1 does.
- **The fourth game.** The tetralemma (A, not A, both, neither) names the game §8.40 left out: neither, no
  conditions at all. It gives a measurable test of the coin model's independence:
  $N_\text{both} N_\text{neither} / (N_\text{black} N_\text{white})$, from counts of surviving seeds. Near 1, the
  black and white conditions are independent; well below 1, they obstruct each other, which a proof could use. Not
  yet measured.
- **Where the nonlinearity lives.** Boole's "or" was exclusive, and he refused Jevons's inclusive one. Since
  $c \lor r = c \oplus r \oplus cr$, Rule 30 is the linear Rule 150 plus the one term $cr$: everything that makes
  Rule 30 hard is the overlap Boole would not interpret. A hypothesis, untested: the kicks are born where that term
  fires near the wall.
None of these is a proof. Two of them are tests that could be run: the independence ratio and the hypothesis about
where kicks are born.

### 8.50 Gates and truth: the owner's NAND question (2026-10-05)

The owner: NAND gates are "wholly logical in the mathematical domain", truth logic is "in the reasoned truth domain",
and the two are not one to one. "Are we missing a difference between these two systems that from the outside are
lexically similar but behave quite differently in practice?"

**Where they are one to one.** For a fixed, finite question they are. Every truth table is a NAND circuit (Sheffer,
1913; Peirce earlier), and every circuit is a truth table. One step of Rule 30 is such a table: three inputs, one
output, $l \oplus (c \lor r)$.

**Where they part, and why it matters here.** Four differences, each already met in this work without its name:
- **Finite against for ever.** A truth table or a circuit settles a finite question by checking every case.
  "Eventually 0101 for ever" is not finite. It needs quantifiers over time ("there is a T such that for every t
  after it"), and with quantifiers come Turing's and Gödel's limits (§8.46). Every probe here lives on the gate
  side: a finite check, decided. The prize lives on the truth side. Each bound for one width is a gate fact; the
  statement for every width needs reasoning.
- **Gates count information; truth does not.** A NAND gate takes in two bits and gives out one, so it erases
  information (Landauer). A truth table only says what is true. The missing statement of this work, "keeping the
  wall's conditions costs real information", is a gate-side statement. To become a proof it must be carried to the
  truth side, and the one carrier found is an exact count over a finite family of seeds that falls below one
  (PERIOD-TWO.md §7, question 1).
- **A physical gate can hang; a logical one cannot.** A real gate fed a near-tie can sit between 0 and 1, and no
  arbiter can be guaranteed to resolve it in bounded time (metastability; Chaney and Molnar, 1973). That is the
  owner's MoltenVK experience (§8.48): a comparison at a near-tie, decided by something invisible. Rule 30 as
  mathematics has no such state, so its randomness is all in the seed.
- **Classical truth against proof.** In classical logic the centre column either is or is not eventually periodic.
  A constructive proof must also give the bound by which it breaks. Kari and Kopra's partial result on Mahler's
  problem is non-constructive, and their Problem 5.1 asks for a constructive one (§8.47). Here any proof would give a
  bound in principle, since for each width the horizon can be found by search once it is known to be finite.

**The bridge between the two domains is induction.** A finite check of a base case and of one step, a gate-side
fact, gives a for-ever statement, a truth-side fact. König's lemma is a bridge of the same kind: it turns "no
infinite run" into "a bound at every depth" (§8.36). The certificates of PERIOD-TWO.md §7, question 3, an invariant
with a ranking function checked by a solver, are exactly such bridges. Every probe in this document crosses no
bridge: it is evidence on the gate side. So the owner's distinction is not missing from the work. It is the line
between what the probes have done and what a proof must do, and it names what fresh eyes are needed for: a bridge.

### 8.51 The counting form, measured, and the tetralemma's fourth game (2026-10-05)

`rule30_count.py` (with `count.c`) counts exactly, with predictions written before the run. $N_w(T)$ is the number
of pairs (configuration, position) where the configuration's hull is exactly $w$ cells wide, the position is a cell
of the hull taken as column 0, and that column reads 0101... (either phase) for $T$ steps. Every configuration up to
$w = 24$ was run, about 200 million pairs. A direct cell-by-cell count agrees up to $w = 9$ (CT0).

| Word | slope of $\log_2 N_w(T)$ at $w$ = 20, 22, 24 | horizon $H(w) - w$, $w$ = 10 to 24 |
|---|---|---|
| 0101 | -1.03, -1.07, -1.08 | -1 to +5 |
| random (seed 1940) | -1.15 at $w$ = 24 | 0 at $w$ = 24 |
| 0 (theorem: Condrey) | -1.13, -1.14, -1.13 | -1 to 0 |
| 1 (theorem: Condrey) | -1.13, -1.12, -1.12 | 0 to +1 |

- **The counting form holds as far as it can be counted** (CT2 held). Each step divides the count by about
  $2^{1.05}$, so $N_w(T) \approx 2^{w - 1.05\,T + c}$. That is PERIOD-TWO.md §7's question 1 with $\alpha$ near 1.
- **The horizon is tight** (CT1 refuted: I predicted at least +2). It is $w + 5$ at most, and $w - 1$ at $w = 18$.
- **Black and white are independent** (CT3 held). The tetralemma's ratio
  $N_\text{both} N_\text{neither} / (N_\text{black} N_\text{white})$ stays between 0.66 and 1.34 with no trend. The
  coin model's independence is right up to a constant factor. There is no hidden obstruction between the two kinds
  of condition to exploit. The random word's ratio dipped once to 0.37 (CT4 refuted, by that alone).
- **The proved words count the same way** (post hoc). The one-colour words, which Condrey's theorem closes, have the
  same law with a slightly steeper slope. 0101 has the shallowest slope of the words tried.

**What it means.** The counting form is the right statement: it is true as far as it can be counted, it is shared
by the words that have a theorem, and it would close period 2 if proved, because a count below one is zero. The
measurement also rules out a cheap route: the tetralemma's ratio shows no obstruction between black and white
conditions. A proof must explain why each step halves the count, exactly. That is the cost side, now in the form
of a number that can be watched as $w$ grows.

**A lemma behind the slope** (proved, 2026-10-05). Split the count by the position $j$ of column 0 inside the hull,
counted from the hull's left end (the left end cell is black). Then for $1 \le T \le j$ the count for position $j$
halves exactly at every step: $N_{w,j}(T) = N_{w,j}(1) / 2^{T-1}$.

*Proof.* Rule 30 is permutive in its left input, so after $t$ steps $x_t(0) = x_0(-t) \oplus g_t$, where $g_t$
depends only on the cells $-t+1$ to $t$ at time 0 (induction on $t$, from
$x_t(0) = x_{t-1}(-1) \oplus (x_{t-1}(0) \lor x_{t-1}(1))$). For $1 \le t \le j - 1$, cell $-t$ is a free cell of the
hull, and no earlier value of column 0 depends on it. So exactly half of the patterns that met the word up to time
$t - 1$ meet it at time $t$, whatever the other cells are. $\square$

So the first $j$ conditions are paid exactly, one bit each, by the left part of the seed. From time $j$ on, the
cell entering on the left is the black end and then white cells, and every further condition must be paid by the
right part's bits, through column 1. That is where the measured slope of about $-1.05$ has no proof. Question 1 of
PERIOD-TWO.md §7 is therefore exactly the cost side: a bound of the form $2^{-\alpha}$ per condition paid by the
right part, after the left part's bits run out.

### 8.52 What the right part pays: in lumps, with bounded debt (2026-10-05)

`rule30_cost.py` (with `count_j.c`; predictions written before each of two runs) splits §8.51's count by the position
$j$ of column 0 in the hull. For $T \le j$ the count halves exactly, as §8.51's lemma says (CJ0, checked at every
$w$ up to 22). After that, every condition must be paid by the right part. The step ratio
$\rho = N_{w,j}(T+1) / N_{w,j}(T)$ is what it pays.
- **Not per step** (CJ1 refuted). Of 276 right-paid steps ($w$ = 16 to 22, counts of 256 or more), 42 are free
  ($\rho$ near or exactly 1: the condition is implied by the earlier ones), and 46 collapse ($\rho < 0.05$).
- **A bit on average** (CJ2 held): the mean of $\log_2 \rho$ is $-1.04$. The word 0, which has a theorem, pays more:
  $-1.63$.
- **Bounded debt** (CW1, CW2 held). Free steps never come more than 3 in a row, at every width from 16 to 22. Any
  4 consecutive right-paid conditions cost at least 1.3 bits, and any 8 at least 8.3.

**Why no pairing proof works on the right** (reasoning, not measured). The left part pays by pairing: flip the
newest cell on the left, and exactly one of the pair meets the new condition (§8.51). On the right, the newest cell
$x_0(t)$ is also outside every earlier condition's reach. But it reaches $x_t(0)$ only along the edge of the light
cone, through $t$ OR gates, and it gets through only if each gate's other input is white. The last of those inputs
is $x_{t-1}(0)$ itself. So after a black time the newest right cell never pays: that is §8.40's black game, which
involves the left half alone. After a white time it pays only if a whole diagonal of $t - 1$ cells is white, which
in the chaotic interior happens about once in $2^{t-1}$. So the right part's bits are not paid when they arrive.
They are paid later, by older bits re-entering through the interior, which is why the cost comes in lumps.

**What it means.** The measurement gives the cost side a precise and more provable shape than the average slope:
*after the left part's bits run out, any 4 consecutive conditions remove a fixed fraction of the survivors.* That
would give $\alpha \ge 1.3 / 4$ and close period 2, if it held at every width and down to counts of one. It cannot
hold literally down to one, because a lone survivor passes every condition it meets. So the statement to prove is
the bounded-debt form with a constant: $N_{w,j}(T + k) \le 2^{c - \alpha k} N_{w,j}(T)$ for all $T \ge j$. Its
constant $c$ is the horizon's excess, measured at most +5 (§8.51). The amortised analysis of algorithms is the
toolbox for statements of this shape: a potential that free steps raise and collapses spend.

**To width 26** (mode `deep`, predictions written first). Free steps still never come more than 3 in a row, at
every width from 16 to 26 (CD1 held). But the debt's constant is not fixed (CD2 refuted): with $\alpha = 0.5$, the
least $c$ that bounds every window is 1.5 at most widths, and 3.0, 2.0 and 5.0 at widths 17, 24 and 26. The jumps
come from small counts, where a few survivors pass many conditions intact. So the form to prove is
$N_{w,j}(T+k) \le 2^{c(w) - \alpha k} N_{w,j}(T)$ with $c(w)$ growing at most like $\log w$, the coin's luck.
That still suffices: the count falls below one once $T > (w + c(w)) / \alpha$, so every horizon is finite.

**Which conditions pay** (mode `phases`, predictions written first). Counting each phase of 0101 alone ($w$ = 16
to 24): free steps come after a black cell 113 times and after a white cell 28 times (CP1 held, at 80%). But the
collapses also come after black cells, 108 times against 26 (CP2 refuted). So the two kinds of condition of §8.40
behave differently in the count:
- **after a black cell**, the condition involves the left half alone. It is all or nothing: it passes every
  survivor of a position or almost none of them;
- **after a white cell**, the condition couples column 1 to the left half. Those are the conditions that split the
  survivors, the coin flips that pay.
So the bounded-debt statement has a natural two-part form for a proof. The black conditions are a deterministic
test on the forced left half. The white conditions are paid through column 1, the channel that §8.20 bounds at
about 0.13 bits per visible bit. A proof would show that the white conditions cannot keep passing a positive
fraction of survivors while the black tests keep passing, and the count says they do not, beyond about 3 steps.

**Not exactly** (mode `exact`, predicted first). I predicted that after a black cell the step is always exactly
all or nothing. It is not (CP3 refuted). 208 of 313 such steps are exactly 0 or 1, against 54 of 271 after a white
cell, and the rest are mostly small fractions (0.02 to 0.13). The two-part picture is a strong tendency, not a
lemma.

**Who pays the average bit** (mode `share`, predicted first). Pooled over every right-paid step ($w$ = 16 to 24,
counts of 256 or more), a condition after a black cell costs 1.18 bits and one after a white cell 1.01 bits. I
predicted the white conditions, through column 1, would carry most of the cost (CP4 refuted: 46%). Both kinds pay
about a bit. The black conditions involve the left half alone and pay through collapses of whole positions. So
half the cost side is a statement about the forced left half by itself, the side where Condrey's and Jen's methods
work, and the other half goes through column 1's narrow channel.

### 8.53 The debt, at total widths beyond 100: flat, and paid at the wheel's formation (2026-10-05)

`rule30_debt.py` (with `forced.c`; predictions written before each run) carries §8.52's count past the hull widths
that exact enumeration reaches.

**The count past the left part is a count of right parts** (proved by §8.51's argument, and checked exactly: DB0).
For $T \ge j + 1$, a configuration with column 0 at distance $j$ from its left end survives exactly when the forced
left half $F$ of its right part (width $b = w - j - 1$) has $F_{-j} = 1$ and a zero run of length at least
$T - 1 - j$ after it. This is §8.42's instrument, counted instead of maximised. It needs only $2^{b-1}$ right
parts, so depths to 100, total widths beyond 100, are in reach.

| Measured, $b$ up to 24, depths to 100 | Result |
|---|---|
| Pooled cost per condition, $b$ = 11 to 24 | **1.001 to 1.004 bits** (DB3 held) |
| The same, depths 50 and beyond against shallower | 1.003 against 1.001 bits (DB4 held) |
| Longest run of free steps | 5, at every $b$ from 15 to 24 (DB1 refuted: I said 3) |
| $c_b$, $\alpha$ = 0.5, 0.8, 0.9, 1.0 ($b \ge 12$) | 4.2, 7.8, 9.0, 10.2: **flat in $b$** (DB2; DA1, DA2 refuted) |
| The same at $\alpha = 1.0$, depths 40 to 80 only, $b = 24$ | **4.45** (post hoc) |
| A random word, $c_{20}$ at $\alpha = 0.9$ | 8.52, against 8.96 (DA3 held) |

- **One bit per condition, almost exactly.** Pooled over every depth, the right part pays 1.002 bits per
  condition at every width from 11 to 24.
- **The debt does not grow with width,** even at the full rate $\alpha = 1$, where I predicted luck would accumulate
  (DA2 refuted).
- **The debt sits in one place** (post hoc). At $b = 24$ the largest constant, 10.16, comes from a crowded window,
  not a lucky survivor. At depth 19, twelve conditions cost only 1.84 bits for over 100,000 right parts. Below
  depth 40 the constant is 4.45. §8.6 found the left half's order in the same place: where the wheel forms.

**What it means.** The bounded-debt statement of §8.52 holds in its strongest form across the whole measured range:
$N_{b,j}(\tau + k) \le 2^{c - k} N_{b,j}(\tau)$, at the true rate, with $c \approx 10$ flat in $b$. And it splits in
two:
- a **one-time debt at the wheel's formation**, shallow and structured, a finite object one could hope to compute
  exactly, as Proposition 6 computed the pure wheel;
- after it, **payment at the full rate** with a constant near 4.5.
A proof could treat the formation as a finite computation and the rest as the steady state. The steady state is
still the coin, and still the open part, but it is now a statement about one regime with a small constant.

**To depth 230** (`forced_deep.c`, multi-word, equal to `forced.c` where both run; modes `depth` and `depthalpha`,
predicted first). At right width 20:

| Windows starting at depth | 40 to 99 | 100 to 159 | 160 to 229 |
|---|---|---|---|
| Pooled cost per condition (bits) | 1.0000 | 0.9966 | 1.0002 |
| Debt constant at $\alpha$ = 0.5 / 0.8 / 1.0 | 2.07 / 3.92 / 5.32 | 3.50 / 5.74 / 7.94 | 3.09 / 5.72 / 8.12 |

- **One bit per condition at every depth** (DD2 held).
- **The constant grows at first** (DD1, DE1 refuted; DE2 held). At every rate it rises once, between the first two
  bands, then stays flat. At a fixed width it saturates with depth, as far as depth 230.

So the bounded-debt statement holds in the measured range with a constant of about 3.5 at $\alpha = 0.5$, flat in
width to $b = 24$ and in depth to 230.

### 8.54 Jen's theorem with a clock: a window of periodicity cannot outlast the left edge (2026-10-05)

*Local's first section as lead (the owner, 2026-10-05, evening: Cloud's budget is spent; "carry on the good work
here"). Probe `rule30_jenclock.py` with `jenclock.c`; predictions were committed before the first run.*

Jen's theorem (§8.13) is about columns that are periodic for ever. Its proof has a clock in it, and reading the clock
gives two quantitative statements. Both hold for every configuration whose left half is eventually zero, whatever
its right half. Neither is in the sources read so far (Jen 1990 as restated by Kopra; PRIOR-ART). The argument is
short enough that they may be folklore.

Say that columns $i$ and $i+1$ are *$P$-periodic on the window $[a, b]$* when the pair at time $t$ equals the pair at
time $t + P$ whenever $a \le t$ and $t + P \le b$.

**Theorem A (a window cannot outlast the edge).** Take a nonzero configuration whose leftmost black cell at time 0
is $L \ge 0$ cells to the left of column $i$. If columns $i$ and $i + 1$ are $P$-periodic on $[a, b]$, then

```math
b \le 2a + L + 2P - 1 .
```

At time $a$ the left edge is $L + a$ cells away. So the window's length $b - a$ is less than that distance plus $2P$.

*Proof.* Three facts, each one line of Rule 30.
1. **Periodicity moves left and loses one step.** $x_t(k-1) = x_{t+1}(k) \oplus (x_t(k) \vee x_t(k+1))$. So if columns
   $k$ and $k+1$ are $P$-periodic on $[a, b]$, column $k - 1$ is $P$-periodic on $[a, b - 1]$. After $j$ steps to the
   left, column $i - j$ is $P$-periodic on $[a, b - j]$.
2. **The edge moves left one cell a step.** The leftmost black cell has two white cells to its left, and $001 \to 1$.
   So column $i - j$ is white before time $j - L$ and black at time $j - L$ (for $j \ge L$).
3. **The two meet.** Take $j = a + P + L$. Column $i - j$ turns black for the first time at $e = a + P$. If
   $b \ge 2a + L + 2P$, then $e \le b - j$. So both $e - P = a$ and $e$ lie in the window where column $i - j$ is
   $P$-periodic. It is white at one and black at the other, a contradiction. $\square$

Jen's theorem is the case $b = \infty$.

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

For column 0 = 0101… and a column 1 whose visible bits have least period $q$, $P = 2q$, and the bound is $4q - 2$.

**Measured** (predictions JC0 to JC4 and a counterfactual):

| Visible period $q$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| Longest zero run, over every word and every depth | 1 | **6** | 5 | 6 | 9 | 10 | 10 | 17 | 14 | 17 |
| Theorem B's bound $4q - 2$ | 2 | **6** | 10 | 14 | 18 | 22 | 26 | 30 | 34 | 38 |

- **Theorem B holds, and is sharp at $q = 2$** (JC1). Every word was followed in depth over its whole tail and
  twice round its cycle, so each entry is that word's longest run at any depth. The control, two zero columns,
  reports an infinite run (JC0).
- **Above $q = 2$ the longest runs are about $1.7\,q$**, well inside the bound (JC2 held: between $q$ and
  $2.5\,q + 4$).
- **Theorem A holds on every window tested** (JC3): 5,254,135 complete windows, over every seed up to 10 cells, every
  column pair from the seed's left end to 12 cells past its right end, every $P$ up to 8, and 400 steps. The
  counterfactual, the same bound without its $2P$ term, is violated 17,500 times.
- **Theorem A is sharp only at the start** (JC4 refuted as I worded it). The slack is 0 for the seed 101 with
  $P = 1$. But windows within 2 of the bound occur out to $L = 12$, not only next to the left edge as I had
  predicted. Every one of them starts at $a \le 3$, and most are a run of zeros waiting for an edge to arrive. Later
  windows in a chaotic interior are a few steps long, far below a bound that grows with time.

**What it gives.**
- **A weaker theorem about every single seed** (PERIOD-TWO.md §7, question 5), by an extremal argument on the edge.
- **Part of question 7, the regime between.** Suppose column 1 runs as some $P$-periodic word between kicks, at
  times $\tau_1 < \tau_2 < \dots$, and the left half is finite with its edge $L$ cells out. Then Theorem A, on the
  window between two kicks, gives $\tau_{n+1} \le 2\,\tau_n + L + 2P + 2$. **Kicks cannot thin out faster than
  geometrically.** A column 1 whose kicks come at times $3^n$, or at any rate that more than doubles, cannot go with
  a finite left half. That is a theorem, not a coin model. It leaves open the kicks that thin out more slowly, and
  the real case, where they come at a steady rate.
- **The wheel's own runs are capped.** The pure wheel $U$ has period 56 in time (§8.5), so by Theorem B with
  $P = 56$ its forced left half has no zero run longer than 110 cells at any depth. §8.5 saw the wheel's runs grow like $\log_2$ of the depth to 23 at
  depth 200,000 (W2). The growth must stop below 110, and the cycle of length $1.5 \times 10^{10}$ (Proposition 6)
  suggests about 34.
- **It does not reach the doubling conjecture.** A zero run of length $R$ from depth $d$ depends on column 1 up to
  time $d + R$. Theorem B forbids only that this stretch of column 1 has a period below about $R/2$. A proof of
  $R(d) \le d + 4$ would need the bound $2P - 2$ to fall below $P$, and it cannot: at $q = 2$ it is attained.

**Why the method stops here.** The proof transports a property of the column pair to the left and tests it
against the edge. The only property the edge refutes is periodicity: a column that begins with a long run of
zeros and then a one is compatible with any complexity above Morse and Hedlund's bound. The transport also costs one
step of window for each column, while the edge retreats one column a step. So a window must be as long as the time
elapsed before it says anything. That factor of 2 is the same geometry as the doubling law.

**The Collatz twin has the same theorem** (PRIZE-PROBLEMS.md §7). If the parity sequence of $n$ is $P$-periodic on a
window, the window pins $n$ 2-adically to a rational cycle point, by Terras's bijection. So unless $n$ lies on a
cycle, a window can last about as many steps as the current iterate has bits, plus a term in $P$. The number of bits there plays the part of the
distance $L$ to the left edge here.

### 8.55 Question 4, closed: what Kari and Kopra's argument gives for Rule 30 (2026-10-05)

PERIOD-TWO.md §7, question 4, asked for a Rule 30 analogue of Kari and Kopra's partial result on Mahler's problem
(arXiv:1710.05737, Theorem 4.9), and §8.47 recorded that its hypotheses hold. Their Section 4 was read in full
today. The adaptation is immediate, and it does not touch the prize.

**Their argument.** It is their Lemma 4.4, and it uses only ergodicity and compactness. Take a small cylinder $C$.
The set of configurations whose orbit never enters $C$ is closed and has measure zero. So finitely many cylinders
of small total measure cover it. Every configuration therefore enters $C$ or starts in one of those cylinders.

**For Rule 30.** Rule 30 is mixing for the uniform measure (Shereshevsky, §8.47), so the lemma applies as it stands:

> For every $\varepsilon > 0$ there are a width $k$ and a set $K$ of more than $(1 - \varepsilon)\,2^k$ words of
> length $k$ such that no configuration keeps cells 1 to $k$ of its row inside $K$ at every time.

**Why it says nothing about a column.** The words here are windows of a *row*. In Mahler's problem that is the right
object: the fractional part of $\xi (p/q)^n$ is the right half of the row at time $n$. The prize is about a *column*.
Applying the same lemma to the system of centre columns gives a statement that is true and empty. Every binary
sequence is some configuration's centre column (left-permutivity), so the centre columns are the full shift, and
the lemma becomes: every sequence contains a given word or begins with a word avoiding it. The statement also
covers the zero configuration and every infinite one, so it cannot separate finite seeds from the rest.

**So question 4 is closed as a route.** The compactness argument proves that a *measure-zero closed set* of
configurations can be covered cheaply. The set of configurations with a period-2 centre column is such a set: it is
the graph of the forced left half over the right halves. The prize asks whether that set contains a finite
configuration, which is a question about single points, as §8.47 found for every other soft method.

### 8.56 What is excluded outright: the left edge is at least 249 cells away (2026-10-05)

*Local. Engine `ladder_deep.c`, driver `rule30_ladder_local.py`; predictions committed before the deep run. Depth 249
finished at 23:49 on 2026-10-05 after about 4.3 hours on six threads; depth 265 was dropped on the owner's decision.*

**A corollary of §8.12 that had not been stated.** $R(m, S)$ is the longest zero run of the forced left half from
depth $S$, over every start of a width-$m$ layer and every input to it. A layer fed any input can show every column
1 that a real right half can show. Suppose a configuration has column 0 = 0101… from time 0 and its leftmost
black cell at depth $L$. Its forced left half is zero at every depth beyond $L$, so $R(m, S)$ is infinite for every
$m$ and every $S > L$. Hence:

> **If $R(m, S)$ is finite for one $m$, no finite configuration with column 0 = 0101… from time 0 has its leftmost
> black cell less than $S$ cells to the left of column 0, whatever its right half and however wide.**

Cloud's value $R(12, 105) = 20$ (§8.14) already excluded every left edge within 104 cells. The searches over
right halves (§8.21, to 34 cells) need a bound on the right half's width; this needs none. Conjecture LR's records
(§8.37) also need none, and reach 84 cells.

**A deeper engine.** `ladder.c` kept every start group of a level in a table, so memory set its depth. But each
start group has exactly one parent, its visible prefix without the last bit. The groups form a tree, and a
depth-first walk holds one branch at a time. `ladder_deep.c` does that, on 320-bit diagonals and in parallel. It
prints exactly `ladder.c`'s histograms and values at 15 points (LL0), and takes 0.2 s where `ladder.c` took 19 s
($m = 12$, $S = 105$).

**Measured** ($m = 24$, six threads; 265 not run):

| Depth $S$ | 153 | 185 | 217 | 249 |
|---|---|---|---|---|
| $R(24, S)$ | 19 | 22 | 21 | 26 |
| Start groups $G$ | 774,437 | 4,031,417 | 20,270,334 | 99,485,847 |
| $R / \log_2 G$ | 0.97 | 1.00 | 0.87 | 0.98 |
| Groups reaching $R$ | 5 | 9 | 55 | 33 |

- **Every run is finite** (LL1 held). With $R(24, 249) = 26$: **no period-2 counterexample has its left edge
  within 248 cells of the centre when its period starts, whatever its right half.**
- **The coin law of §8.14 holds at twice the depth** (LL2 held): the longest run is 0.87 to 1.00 times
  $\log_2 G$ at every depth.
- **The start groups grow by 1.51, 1.50 and 1.49 for every 8 depths** (LL3 held), which is 0.148 bits per
  visible bit, against the channel bound's 0.129 at $m = 26$ (§8.33).
- **$R \le 40$ throughout** (LL4 held). The deepest run took 2.1 billion tree nodes and 4.0 trillion group members.

This is a finite check and not a step toward a proof: §8.14 already showed the runs grow with depth at every layer
width. What it gives is the firmest statement so far about *every* finite configuration, with no condition on the
right half.

### 8.57 No pure rotation works: every Sturmian column 1 is excluded (2026-10-05)

*Local. Probe `rule30_sturmian.py`, predictions committed before each of two runs. PERIOD-TWO.md §7, question 7.*

Jen's theorem excludes every column 1 that is eventually periodic. A periodic sequence is a coding of a rotation of
the circle by a rational angle. Theorem A (§8.54) reaches the irrational angles too.

**Theorem E.** Let $\alpha$ be irrational and $\theta$ any real number, and let column 1's visible bits be the
Sturmian sequence $c_s = 1$ if the fractional part of $\theta + s\alpha$ lies in $[1 - \alpha, 1)$, and $c_s = 0$
otherwise. Let column 0 be 0101… Then the forced left half is not eventually zero.

With Jen's theorem for rational $\alpha$: **no column 1 that codes a rotation in this way, by any angle and from any
starting point, can go with a finite left half.** In the language of §8.5: a wheel that is never kicked cannot hold
the left half, whatever its rotation number. Conjecture LR holds for every such column 1, and these are
uncountably many sequences of zero entropy, none of them eventually periodic.

*Proof.* Suppose the left half is zero beyond depth $L$. ($L \ge 1$: an empty left half fails the condition at
time 1.) Put $C = \lfloor (L - 3)/2 \rfloor$.

**Step 0: Theorem A in visible bits.** If $c_s = c_{s+q}$ for every $s$ from $s_a$ to $s_e$, then

```math
s_e \le 2 s_a + q + C . \tag{$\ast$}
```

Column $-1$ is $\bar c_s$ at even times and 1 at odd times (§8.39), so columns $-1$ and 0 are $2q$-periodic on the
times $2s_a$ to $2(s_e + q) + 1$. Theorem A, with the left edge $L - 1$ cells from column $-1$, gives $(\ast)$. It
needs no right half: its proof uses Rule 30 only at columns 0 and to the left.

**Notation.** Let $p_n / q_n$ be the convergents of $\alpha$, with partial quotients $a_n$, and
$\delta_n = q_n\alpha - p_n$. The signs of $\delta_n$ alternate, $|\delta_{n-1}| = a_{n+1}|\delta_n| + |\delta_{n+1}|$,
and $\|m\alpha\| \ge |\delta_n|$ for $0 < |m| < q_{n+1}$ ($\|\cdot\|$ is the distance to the nearest integer). Write
$x_s$ for $\theta + s\alpha$ on the circle, and $K_n$ for the half-open arc of length $|\delta_n|$ that ends at 0 if
$\delta_n > 0$ and starts at 0 if $\delta_n < 0$. Take $n$ large.

**Step 1: where $c$ breaks period $q_n$.** $c_{s+q_n}$ is the code of $x_s + \delta_n$, a point $|\delta_n|$ away from
$x_s$. The two codes differ exactly when an end of $[1 - \alpha, 1)$ lies between them, which is when $x_s$ or
$x_{s+1}$ is in $K_n$. Let $h < h'$ be the first two times the orbit visits $K_n$. A return to an arc of length
$|\delta_n|$ needs $\|(h' - h)\alpha\| < |\delta_n|$, so $h' - h \ge q_{n+1}$.

**Step 2: two inequalities at every scale.** $c_s = c_{s+q_n}$ for $0 \le s \le h - 2$, and again for
$h + 1 \le s \le h' - 2$. Apply $(\ast)$ to each stretch:

```math
h \le q_n + C + 2, \qquad h' \le 2h + q_n + C + 4 .
```

With $h' \ge h + q_{n+1}$ the second gives $h \ge q_{n+1} - q_n - C - 4$. So the first visit $h(n)$ to $K_n$ satisfies

```math
q_{n+1} - q_n - C - 4 \;\le\; h(n) \;\le\; q_n + C + 2 . \tag{$\ast\ast$}
```

**Step 3: a partial quotient of 2 or more.** If $a_{n+1} \ge 2$ then $q_{n+1} - q_n \ge q_n + q_{n-1}$, and
$(\ast\ast)$ is empty as soon as $q_{n-1} > 2C + 6$. So if infinitely many partial quotients are at least 2, the
proof is done.

**Step 4: all partial quotients 1 from some point on.** Then $q_{n+1} - q_n = q_{n-1}$ and
$|\delta_{n-1}| = |\delta_n| + |\delta_{n+1}|$. Put $s = h(n)$ and $s' = h(n+1)$. The arcs $K_n$ and $K_{n+1}$ lie on
opposite sides of 0, so $x_s$ and $x_{s'}$ are less than $|\delta_n| + |\delta_{n+1}| = |\delta_{n-1}|$ apart, on known
sides. By $(\ast\ast)$, $m = s - s'$ lies between $-q_n - 2C - 6$ and $2C + 6$, and $m \ne 0$ because the two arcs
are disjoint. An $m \ne 0$ with
$\|m\alpha\| < |\delta_{n-1}|$ has $|m| \ge q_n$, and for large $n$ the only one in that range with the right sign is
$m = -q_n$. So

```math
h(n+1) = h(n) + q_n \qquad\text{for every large } n .
```

The upper bound of $(\ast\ast)$ at $n + 1$ now gives $h(n) \le q_{n-1} + C + 2$, and the lower bound at $n$ gives
$h(n) \ge q_{n-1} - C - 4$. So $h(n)$ is within $C + 4$ of $q_{n-1}$, for every large $n$. Then $h(n+1) = h(n) + q_n$
is within $C + 4$ of $q_{n+1}$. But the same statement at $n + 1$ puts $h(n+1)$ within $C + 4$ of $q_n$. Those
disagree once $q_{n-1} > 2C + 8$. $\square$

**Checked** (`rule30_sturmian.py`, golden rotation):

| Check or prediction | Result |
|---|---|
| SP0: the row routine against the stripes and against `ladder.c` | **passed** |
| SP1: the zero-run form on 300 forced rows to depth 2000 | **passed**: 17,044 runs, 0 violations |
| CF: the same with half the bound | **failed as a counterfactual**: 0 violations, a bad design (see below) |
| CF2: the bound without its window condition | **passed**: 40,326 violations |
| SP2: the share of $\theta$ allowed at every scale to $n = 20$ is below 1% ($L = 9$) | **held**: 0 of 100,000 from $n = 10$ on |
| SP3: the share falls by a factor of 0.3 to 0.7 per scale | **refuted**: it reaches zero |
| SP4: at $L = 99$, $(\ast\ast)$ fails by $n = 20$ for every $\theta$ | **held**: all 100,000, the latest at $n = 14$ |

- **How the theorem was found.** I first proved only "almost every $\theta$", from the upper bound in $(\ast\ast)$
  and the ergodicity of the rotation, and predicted that the allowed share would shrink by a constant factor per
  scale (SP3). It did not shrink. It vanished. Neighbouring scales exclude each other, and Steps 2 to 4 are that
  observation made exact. SP4 then tested the two-sided condition blind.
- **A failed counterfactual, recorded.** CF asked for a violation of half the bound and found none. The longest zero
  run anywhere in the 300 rows is 21 cells, and the runs that qualify exist only for large $q$, where half the
  bound is still far above 21. So SP1 has little bite on these rows. Theorem B's sharp test is JC1 of §8.54, where
  the bound is attained.

**What it means.**
- **Question 7 of PERIOD-TWO.md has its first full answer on a class.** For Sturmian columns 1, which have zero
  entropy and are never eventually periodic, the left half is never finite. Finiteness of the family was not
  needed; FLP's method (§8.45) needs it.
- **Kicks are necessary for a structural reason, not only because the real wheel's angle is rational.** A pure
  rotation by any angle fails. What a counterexample would need is the kicks' own information.
- **Why it works here and not for the real column 1.** A Sturmian sequence is periodic with period $q_n$ for
  stretches of about $q_{n+1}$ steps, at every scale $n$ and from the very start. Theorem A allows a stretch that
  starts at time $s_a$ to last only about $2s_a + q$. Real right halves kick the wheel at a steady rate (§8.11),
  so their periodic stretches are short and $(\ast)$ never binds.

**Theorem E″ (any arcs, for a typical rotation number; added the same night).** Let $c_s = f(\theta + s\alpha)$,
where $f$ is 1 on a finite union of arcs with $r$ end points in all, and 0 elsewhere. If $\alpha$ has infinitely
many partial quotients larger than $2^{r+1}$, the forced left half is not eventually zero, for every $\theta$.
Almost every $\alpha$ has unbounded partial quotients, so for almost every rotation number **no coding by arcs at
all** can go with a finite left half. These sequences have complexity up to $r\,n$.

*Proof.* $c$ breaks period $q_n$ at time $s$ exactly when $x_s$ lies in one of $r$ arcs of length $|\delta_n|$, one at
each end point. Let $d_1 < d_2 < \dots$ be the break times. Step 0 on the stretch before $d_1$ and on each stretch
between consecutive breaks gives $d_1 \le q_n + C + 1$ and $d_{k+1} \le 2 d_k + q_n + C + 3$, so
$d_k < 2^k (q_n + C + 2)$. Two of the first $r + 1$ breaks belong to the same end point, and returns to an arc of
length $|\delta_n|$ are at least $q_{n+1}$ apart. So $q_{n+1} \le d_{r+1} < 2^{r+1}(q_n + C + 2)$, which fails
when $a_{n+1} > 2^{r+1}$ and $q_n$ is large. $\square$

Checked (SP5, predicted first): with partial quotients 1, 20, 1, 20, … and one arc with unrelated ends, all 20,000
random arcs and phases fail the conditions at both scales that precede a quotient of 20. At a scale that precedes
a quotient of 1 only 54 fail (the counterfactual).

**Not covered.** Arcs with unrelated ends when the partial quotients of $\alpha$ stay small: Step 1's gap of
$q_{n+1}$ between breaks is then not enough by itself, and the three-scale argument of Step 4 would have to follow
two end points at once. Rotations on more than one circle. Any kicked wheel.

**The general form of the condition, and where it has no grip.** Step 0 holds for every column 1: if the left
half is zero beyond depth $L$, then for every $q$ the times at which $c$ breaks period $q$ start by $q + C + 1$ and
never more than double (plus $q + C + 3$) from one to the next. A column 1 with early long repetitions at
infinitely many scales fails this, and Sturmian sequences are the extreme case. A sequence without long repetitions
passes it untouched. The Thue–Morse sequence has no repetition of more than two periods at all, so $(\ast)$ says
nothing about it.

**A quick look outside the theorem** (exploratory, the run's unplanned step; no predictions were written). With
the Thue–Morse, period-doubling, Rudin–Shapiro, paperfolding and Fibonacci sequences as column 1, and their
complements, the forced row to depth 6000 looks like coin flips in every case: the longest zero run is 10 to 16
cells, the density of ones 0.49 to 0.51, the same as for a random column 1 (10 and 12 cells). The left half
scrambles any column 1 that is not periodic. For the Fibonacci sequence Theorem E proves the row is never finite;
for the others nothing is proved.

### 8.58 The window principle: Theorem A′, and what the Collatz twin shows is missing (2026-10-05)

*Local. The owner asked for the Collatz avenues to be carried back to Rule 30. The two-problem account is
COLLATZ-PRIZE.md §5. This section is the Rule 30 half. Probe `rule30_window.py`, predictions committed first.*

Collatz has a fact so simple that it is rarely stated: two iterates with the same next $n$ parities are congruent
modulo $2^n$. Rule 30 has the same fact, and it gives a shorter proof of Theorem A (§8.54) and a stronger
statement.

**Theorem A′ (a block recurs only if it is no longer than the edge is far).** Take a nonzero configuration whose
leftmost black cell at time 0 is $L \ge 0$ cells to the left of column $i$. If the pair of columns $(i, i+1)$
shows the same block of $n$ consecutive values starting at times $a$ and $a' > a$, then

```math
n \le L + a' .
```

*Proof.* Rule 30 read from right to left gives each cell from the cell to its right one step later and two cells
of its own time. So the two columns at times $t$ to $t + k$ fix the $k$ cells to their left at time $t$. Equal
blocks of length $n$ therefore make the rows at times $a$ and $a'$ agree at the $n - 1$ cells left of column
$i$. The later row has its leftmost black cell $L + a'$ cells out, and the earlier row is white there. If
$L + a' \le n - 1$ the rows disagree inside the range where they must agree. $\square$

Theorem A is the case where the block recurs because the columns are periodic: a window $[a, b]$ of period $P$
is a block of length $b - a - P + 1$ that recurs at $a' = a + P$. Jen's theorem is the case of a block that
recurs for ever. Theorem A′ needs no periodicity, only one repeat.

**Checked** (`rule30_window.py`): over every seed up to 9 cells, every column pair from the seed's left end to 8
cells past its right end, and every pair of times up to 120, there are 7,436,643 recurring blocks and none
longer than $L + a'$ (WN1). With the earlier time $a$ in place of $a'$ the bound fails 20,179 times (the
counterfactual). I predicted the bound would be attained by some seed of 3 or more cells at $a' \ge 2$. It is
not (WN2 refuted in that half). Late blocks are far below it: the longest block recurring at a time between 240
and 360 is 19 cells. That is the growth of a coin's longest match, a logarithm of the number of pairs of times.

**The window identity.** For the forced left half next to column 0 = 0101…, the $2n$ cells beside the wall and
the next $n$ visible bits of column 1 determine each other (Lemma 4, §8.39). So for any column 1:

```math
p_c(n) \;=\; \text{the number of different contents of the } 2n \text{ cells beside the wall, over all even times,}
```

where $p_c(n)$ counts the different blocks of $n$ visible bits in column 1. Theorem A′ says the first
$n - L/2$ of those contents are all different, so $p_c(n) \ge n - L/2$. The channel bound (§8.33) says a real
right half allows at most about $2^{0.13\,n}$.

**The cost side as one sentence about one orbit.** Put the two together:

> A period-2 counterexample must keep the $2n$ cells to the left of its centre column within $2^{0.13\,n}$
> different contents for ever, for every $n$. Period 2 follows from any proof that a finite configuration's
> window shows more than that for one $n$.

This is the entropy squeeze of §8.33 in the form of a count. What is new is the comparison with Collatz
(COLLATZ-PRIZE.md §5). There the same count has a free lower bound, because a state is a number, small
numbers are few, and each has its own future. Rule 30's states grow by one cell a step whatever happens, so the
edge certifies only $n - L/2$ contents, against the $2^{0.13\,n}$ needed. Every measurement says the true count is
far higher: a chaotic left half shows a new content at almost every step. Nothing proves it for a single orbit.

**The first three columns are affine in column 1** (a small exact fact, used in COLLATZ-PRIZE.md §5). Write
$c_s$ for column 1 at time $2s$. Given the wall's conditions, at times $2s$ and $2s + 1$:

| Column | $-1$ | $-2$ | $-3$ | $-4$ |
|---|---|---|---|---|
| time $2s$ | $\bar c_s$ | $c_s$ | $\bar c_{s+1}$ | $c_s\,c_{s+1}$ |
| time $2s + 1$ | 1 | $c_{s+1}$ | $\bar c_{s+1}$ | $c_{s+2}$ |

Column $-2$ is column 1 with every visible bit held for two steps, and column $-3$ is its complement one step
on. The first product appears in column $-4$. A real right half never shows two visible ones in a row (Lemma 3, §8), so
for it column $-4$ is white at every even time. With column 1 all white the table gives the stripes
$1, 0, 1, 0, \dots$, which are a fixed point of Rule 30: the forced left half's resting state. A visible one in
column 1 is a defect in the stripes, and a finite left half needs the defects to cancel every stripe beyond its
edge.

**A repeat is a white run.** The proof gives more than the inequality. If a block of length $n$ recurs at time
$a'$, the row at time $a'$ copies the row at time $a$ on the $n - 1$ cells left of the columns. The earlier row is
white beyond its edge, $L + a$ cells out. So the later row is white from cell $L + a + 1$ to cell $n - 1$: a run of
$n - 1 - L - a$ white cells, in a row whose own edge is further out. In the forced left half that reads: if the
visible bits of column 1 agree for $n$ steps from the times $2i$ and $2j > 2i$, the row at time $2j$ has a zero run
of length $2n - L - 2i$ starting at depth $L + 2i + 1$. Zero runs are what the records of §8.36 and the ladder of
§8.56 bound. So a bound $R(d) \le \rho\,d + C$ on zero runs from depth $d$ would give
$2n \le (1 + \rho)(L + 2i) + C$ for every later time $2j$: a block that starts early enough never recurs at all.
With the doubling conjecture ($\rho = 1$) the first $L + 3$ visible bits of column 1 never recur. This is
conditional, and the computed range of $R$ (depths to 249) lies below the depths $L + 2i + 1 \ge 250$ where a
counterexample would need it. It is recorded because it ties three things together exactly: a repeat in the
trace, a white run in a later row, and the cost of that run.

**What it does not give.** Theorem A′ is sharper than Theorem A and not stronger in its reach. Real right halves
have no long early repeats, so it does not bind them. The squeeze sentence above is a restatement, as §8.33 was.
Its use is the comparison: it says exactly which number a proof must move, and from where to where.


### 8.59 The window principle meets the band of stripes: a repeat is a white run, and the left side is never white for long (2026-10-05)

Question 7 of PERIOD-TWO.md asked which columns 1 of zero entropy are excluded. Theorem E (§8.57) excluded the
Sturmian ones, by their long early repetitions. §8.57 also said where that method has no grip: a sequence with
no repetition longer than two periods, Thue–Morse for one, passes the condition $(\ast)$ untouched. This section
takes the other half of the picture, the left end of the rows, and gets a grip on part of that class. Everything
here is elementary, and `rule30_band.py` checked each statement with predictions written first. Two of its blind
predictions and one counterfactual missed; they are recorded below.

**The idea in one line.** §8.58 showed that a repeat of the trace is a white run in the later row. The later row's
left end is the band of stripes (§8.27, §8.30): eventually periodic diagonals with tiny periods. A band like that
is never white for long. So a repeat must stay below Theorem A′'s bound by the black in the band, and the band's
black is a universal, computable object.

**Notation.** Diagonal $k$ of a row is the cell $k$ places right of the row's leftmost black cell, and $D_k(t)$ is
its colour at time $t$. From Rule 30, $D_k(t+1) = D_{k-2}(t) \oplus (D_{k-1}(t) \lor D_k(t))$, with $D_{-1} = D_{-2} = 0$.
So diagonal $k$ depends only on diagonals nearer the edge, and by induction each is eventually periodic in time,
with a period that is a power of two (§8.27). "Eventually white" and "eventually black" mean constant from some
time on. In the wall form (§8.39) the same holds: diagonal $k$ exists from time $k - L$, when it is at the wall,
and obeys the recurrence from then on.

**Lemma B1 (white, then black).** If diagonal $j$ is eventually white, diagonal $j + 2$ is eventually black. No two
adjacent diagonals are both eventually white. A diagonal other than 0 and 1 is eventually black only if the one two
before it is eventually white.

*Proof.* Once $D_j \equiv 0$, $D_{j+2}(t+1) = D_{j+1}(t) \lor D_{j+2}(t)$, which never falls, so $D_{j+2}$ is eventually
constant, and it is 1 unless $D_{j+1} \equiv D_{j+2} \equiv 0$ as well. If $D_j \equiv D_{j+1} \equiv 0$ then
$D_{j+1}(t+1) = D_{j-1}(t) \oplus (D_j \lor D_{j+1}) = D_{j-1}(t)$ forces $D_{j-1} \equiv 0$, and so on down to
$D_0 \equiv 0$, which is false ($D_0 \equiv 1$). That proves the first two claims. For the third: if $D_k \equiv 1$
then $D_k(t+1) = D_{k-2}(t) \oplus 1$ forces $D_{k-2} \equiv 0$. $\square$

**Lemma B2 (the clock never stops).** The eventual periods of the diagonals are unbounded. So there are infinitely
many eventually white diagonals, and infinitely many eventually black ones.

*Proof.* Suppose every diagonal had eventual period dividing $P$. Write $V_k \in \{0,1\}^{\mathbb{Z}/P}$ for the
periodic regime of diagonal $k$, indexed by time modulo $P$, so that $V_k(s+1) = V_{k-2}(s) \oplus (V_{k-1}(s) \lor V_k(s))$
for every $k \ge 0$, with $V_{-1} = V_{-2} = 0$. The pairs $(V_{k-1}, V_k)$ take finitely many values, so
$(V_{k_1 - 1}, V_{k_1}) = (V_{k_2 - 1}, V_{k_2})$ for some $k_1 < k_2$. The recurrence can be read backwards,
$V_{k-2}(s) = V_k(s+1) \oplus (V_{k-1}(s) \lor V_k(s))$, so $V_{k_1 - j} = V_{k_2 - j}$ for every $j \ge 0$, and the
backward reading continues into the negative indices, where everything is 0. With $q = k_2 - k_1$ this gives
$V_0 = V_{-q} = 0$, against $V_0 \equiv 1$. So the periods are unbounded. A diagonal's period exceeds the periods
of the two before it only when the one before it is eventually white: otherwise a time with $D_{k-1}(t) = 1$ resets
$D_k(t+1) = \lnot D_{k-2}(t)$, after which $D_k$ follows its inputs' period. Infinitely many doublings need infinitely
many eventually white diagonals, and Lemma B1 turns each into an eventually black one. $\square$

Rowland (2006, §5) proves when the periods double, and §8.31 found the first branch point of the left side, which
is an eventually white diagonal too. Whether the unboundedness itself is in the literature was not checked (owed:
Jen 1986, Rowland 2006). Measured: below diagonal 53,200 the eventually white diagonals are exactly 2, 7, 28 and
399, the eventually black ones exactly 0, 1, 4, 9, 30 and 401, the period 16 (BF0, with a certificate $V_t = V_{t+16}$
for the strip of 53,200 diagonals; one cycle, reached by the single cell and by random seeds). Over all 512 contents
of the first 10 diagonals, diagonal 4 is black from time 4 and diagonal 9 from time 11 (BD3).

**Theorem A‴ (the window principle, with the band).** Let the leftmost black cell at time 0 be $L$ cells left of
column $i$, and let the pair of columns $(i, i+1)$ show the same block of $n$ values from the times $a$ and $a' > a$.
Then row $a'$ is white on its diagonals $L + a' - n + 1$ to $a' - a - 1$. Hence, if diagonal $b$ is black at time $a'$
and $b < a' - a$, then $n \le L + a' - b$.

*Proof.* By §8.58 the rows at $a$ and $a'$ agree on the $n - 1$ cells left of column $i$. Row $a$ is white beyond
distance $L + a$, so row $a'$ is white at the distances $L + a + 1$ to $n - 1$. Its leftmost black cell is at distance
$L + a'$, so those distances are its diagonals $L + a' - n + 1$ to $a' - a - 1$. A black diagonal $b$ in that range
contradicts this; so either $b \ge a' - a$ or $b \le L + a' - n$. $\square$

With $b = 0$ this is Theorem A′. With $b = 1, 4, 9$ (universal from times 1, 4, 11) it is checked on every seed of
width up to 9 (BD4, 0 violations), and the bound with $b = 9$ is sharp: 166 pairs attain $n = L + a' - 9$ (BD5).

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

What it reaches, with the slack $i' - \ell(i, i')$ measured over all pairs with $i' - i \ge 64$ and $i' \le 4096$
(BD8, all held): the period-doubling word (fixed by $0 \to 01$, $1 \to 00$) has slack 1 for ever, since its first
$2^k$ symbols recur at $2^k$ for exactly $2^k - 1$ symbols (BD7). Chacon's word (fixed by $0 \to 0010$, $1 \to 1$)
has slack 0: it begins with the squares $\sigma^k(0)\sigma^k(0)$ (BD7). So does every fixed point of a substitution
whose first two letters are equal, and so does the Fibonacci word (slack $-1595$ in the range measured; Theorem E
already covers it). For a Sturmian word with partial quotient $a_{n+1} \ge 2$, the first break of period $q_n$ at
$h$ and the next, at least $q_{n+1}$ later, give one repetition of slack at most 1 at each such scale, so Corollary F
gives that case of Theorem E in two lines; the case of eventually all $a_n = 1$ still needs §8.57's three scales.
Not reached: Thue–Morse, Rudin–Shapiro and paperfolding, whose slack grows with the period (32, 32 and 33 in the
range measured; for Thue–Morse the squares of period $d$ sit at positions $\ge d$, so the slack is at least $d/3$).
As column 1, the period-doubling word, Chacon's word and their complements give forced rows that look like coin
flips to depth 6000 (longest zero run 11 to 13, ones 0.497 to 0.510; BD9).

**Lemma B3 (the settled band has no long white run).** Suppose that at time $t$ the diagonals $0$ to $M$ have been
in their periodic regime, with a common period $P$, for at least $P$ steps. Then no white run of the row inside
diagonals $0$ to $M$ is longer than $2P$.

*Proof.* Let the row be white on $[g+1, M']$ with $M' \le M$ and $D_g(t) = 1$ (diagonals 0 and 1 are black, so such a
$g \ge 1$ exists). One step back, the constraint $D_{k-2} = D_{k-1} \lor D_k$ for $k \in [g+1, M']$ leaves two cases:
either the row at $t - 1$ is white on $[g-1, M']$ with $D_{g-2}(t-1) = 1$ (the run is older and two cells wider),
or it is black on $[g-1, M'-2]$ (the run is born here, under a black run). Repeating, the run is older for $s_0$
steps and born at time $t - s_0 - 1$. At time $t - P$ the row is the same as at $t$, white exactly from $g+1$, so
$s_0 < P$. Forward from time $t - P$, a white run only loses two cells a step at its edge side:
$D_k(\tau+1) = 0$ whenever $k-2$, $k-1$, $k$ are all white. So at time $t - s_0 - 1$ the row is white on
$[g + 1 + 2(P - s_0 - 1), M']$ and black on $[g - 2s_0 - 1, M' - 2]$. The two ranges are disjoint only if
$M' - g \le 2P - 2s_0 \le 2P$. $\square$

Measured on the universal strip (16 phases, 53,200 diagonals): the longest white run is 17 (BF1 held its bound,
32; its blind half, "between 5 and 16", missed by one).

**Theorem A⁗ (a repeat's white run cannot lie in the settled band).** In the setting of Theorem A‴, if the diagonals
$0$ to $M$ are settled in the sense of Lemma B3 at time $a'$ and $M < a' - a$, then $n \le L + a' - M + 2P$.

*Proof.* The white run of Theorem A‴ covers $[L + a' - n + 1, a' - a - 1] \supseteq [L + a' - n + 1, M]$, which lies in
the settled band, so by Lemma B3 its length $M - (L + a' - n)$ is at most $2P$. $\square$

**The settling front.** When does diagonal $M$ settle? A diagonal in its regime settles the next one at the first
black cell it shows afterwards: $D_{k+1}(t+1) = \lnot D_{k-1}(t)$ when $D_k(t) = 1$, and from then on $D_{k+1}$ follows
its inputs. After an eventually white diagonal the next one settles at once. So
$\tau_{k+1} = 1 + \min\{t \ge \max(\tau_k, \tau_{k-1}) : D_k(t) = 1\}$ (or $\max(\tau_k, \tau_{k-1})$ after a white
diagonal) is an upper bound on the settling time of diagonal $k+1$, for every row with a white left tail, whatever
its seed and whatever its phase, once the regime values $D_k(t)$ are taken from the universal cycle at the worst
of its 16 phases. Measured (BF2): the worst-phase front reaches diagonal 53,199 at time 107,294, a slope of 2.017
(1.992 at diagonal 1,000; I had predicted 1.5 to 2.0). The actual rows settle faster: the median row is in its
regime to diagonal $0.78\,t$ at $t = 1600$ (the 0.25 cells per step of §8.30), but at $t = 200$ single rows ranged
from $0.76\,t$ to $1.01\,t$, which is why the counterfactual CF2 ("no row agrees with the cycle below $2S(t)$")
failed in 2 of 120 cases: it assumed the average rate for every row. BF3 held: every row agrees with a phase of the
cycle on every diagonal below the front's $S(t)$ ($S(200) = 97$, $S(1600) = 804$).

**What Theorem A⁗ reaches** (BF4). A pair $i < i'$ of column 1 with common future $\ell$ excludes every left edge
$L$ for which $L + 2i' - 2\ell + 32 \le \min(2(i'-i) - 1,\, 53199)$ and $\tau_{L + 2i' - 2\ell + 32} \le 2i' - 16$.
The front's slope is just above 2, so a repetition is fatal, at depths the certified strip covers, when
$\ell > i'/2 + L/2 + O(1)$, roughly: when the future at $i'$ repeats more than half of the time before it.
- Period-doubling (the control): excluded to $L = 53{,}165$, the strip's cap; Corollary F excludes every $L$.
- **Thue–Morse: excluded for every $L \le 15{,}870$**, by the pair $i = 0$, $i' = 49{,}152$, $\ell = 32{,}768$ (the
  prefix of length $2^{k+1}$ recurs at $3 \cdot 2^k$).
- **Paperfolding: excluded for every $L \le 15{,}868$**, by $i = 16{,}384$, $i' = 49{,}152$, $\ell = 32{,}767$ (the
  block starting at $2^{k-1}$ has period $2^k$ for $2^k - 1$ symbols).
- Rudin–Shapiro: nothing. Its best repeats have $\ell$ near $i'/2$, which the slope 2.017 just fails to reach.
The records (§8.36) exclude every column 1 for $L \le 84$ ($R(85)$ is finite); this is the same kind of
statement, about 190 times deeper, for two named sequences.

**What it reduces to.** For Thue–Morse and every $L$, the argument needs, at infinitely many scales $k$, that
diagonal $L + 2^{k+1} + 33$ has settled by time $6 \cdot 2^k - 16$: that the front's slope stays below 3 and the
band's period stays small against its depth. Those are statements about one object, the universal left side of
Rule 30 (§8.31), not about seeds. Below diagonal 53,200 the slope is 2.017 and the period 16. Beyond 160,000
diagonals nothing has been computed, and Lemma B2 says the period keeps doubling, each doubling at an eventually
white diagonal whose position no one can predict. So the Thue–Morse case of question 7 is now: *prove that the
left side of Rule 30 settles at a bounded rate*. That is a cleaner question than the one it replaces, and still
open.

**What this does not do.** Nothing for real right halves: their repeats are short and late, far below Theorem A′,
let alone A⁗. Nothing for the counting form. The left half's edge is where Rule 30 is most orderly, and the prize
lives in the chaotic core, so a method that lives on the edge was always going to reach only the columns 1 that
echo their own beginnings.


**Audit note (2026-10-06, after GPT's independent reading, RULE30-GPT.md §G2).** No counterexample to any statement
of this section or of §8.54, §8.57 and §8.58. Three qualifications are adopted here. (i) Corollary F's substitution
example needs the substitution to grow on its first letter, $|\sigma^k(a)| \to \infty$; the identity fixes every
word and gives nothing. (ii) In the wall form a diagonal $k$ exists only from time $k - L$, so the settling
recursion for the forced half-line starts at $\max(\tau_{k-1}, \tau_{k-2}, k - L)$; with $L = 1$ the worst-phase
bounds move by one step (107,295 and 107,313 at diagonals 53,199 and 53,207), which changes no number used above.
(iii) Any extension of the Thue–Morse exclusion to every $L$ needs the settling slope below 3 *and* the period
$o(M)$ on every left side a finite seed can realise, not only on the generic one; GPT's §G2.4 states the sufficient
criterion exactly. GPT also supplied the finite-offset sentence that Theorem E's Step 4 had left implicit (§G2.2):
for the eventually-all-1 case the offset $m = -q_n - r$ with $1 \le r \le 2C + 6$ is impossible for large $n$ because
$\|r\alpha\|$ is bounded below by a fixed $\eta > 0$. That repair is accepted as part of the proof of Theorem E.

### 8.60 The small items: the wall never sees the far end, the mostly-zero words, and the left side to a million (2026-10-06)

The board in PERIOD-TWO.md §6 listed eight items found in this file that had never been leads. The owner asked for
them. Three took runs, each with predictions written first; two (why the forced cells inside a long run stay 0,
§8.2; whether a structural reason for balance reaches the core, §8.34) went to GPT by the split agreed in the
messages table of CLOUD-LOCAL.md on 2026-10-06 at 00:17. The runs are `rule30_sync.py` (five runs),
`rule30_records_word.py` with the engine `records_word.c`, and `rule30_leftside_million.py`.

**1. Are the walls synchronised in time across right halves? (§8.10's untested hint.)** They are, and the reason
is not a clock. The first run measured the Fano factor of the number of halves slipping at each window, over the
3,936 unlocked right halves of up to 12 cells: 5.8 in the formation (windows 2 to 11), 2.7 in the middle, 3.1 late
(windows 40 to 72), where independent halves give 0.5, 0.86 and 0.92 (the value $1 - \sum p_h^2 / \sum p_h$, which
the shifted control reproduces; my counterfactual's band had assumed rare slips and missed it). I predicted the
synchrony would fade; it did not (S2 refuted). Four more pre-registered runs found why:
- The excess does not grow with the population (SA1 refuted: 2.05 at 15,744 halves against 2.42 at 3,936), so it
  is not a modulation shared by all halves but clusters.
- Grouping the halves by their six cells nearest the wall, the 64 groups' slip counts are uncorrelated (0.009);
  within groups the excess is 1.24 (SB3 held). No common clock. The alternative that would have survived a
  refutation, the wall's parity clock (every wheel's phase is even, and the phases favour 4, 6 and 8), is out.
- **The synchrony is duplication.** Among the 3,936 unlocked halves there are only 1,968 distinct columns 1 (983
  traces come from one half, 495 from two, 241 from three, up to one from twelve; SC1 missed by 32). Keeping one
  half per trace, the late Fano factor is 0.75 against an independence value of 0.73 (SC2 held).
- **Where the duplicates come from: the wall often never sees the far end of its right half.** A half $R$ and its
  sister $R + 2^{12}$ (one more black cell at position 13) have the *same* column 1 for all 4,096 steps in 1,479
  of 3,936 cases (37.6%). The rest first differ at a median of 34 steps (quartiles 26 and 50; SB1's second half
  refuted). Sisters that differ at all are uncorrelated afterwards (0.001; SB2 refuted). In all 1,479 identical
  pairs the two space-time patterns still differ at time 4,096, but only within 60 cells of the right edge (SC3
  held, 1,479 of 1,479), and 200 of 200 stay identical to 16,384 steps (SC4 held).

The mechanism, stated as an observation: a change in Rule 30 always travels right at speed 1, because the next
value is the XOR of the left neighbour, so a change at the far end rides with the right edge for ever. It reaches
the wall only if its left front escapes into the chaotic core, and the escape is decided in the first few dozen
steps: either within about 50 steps or never. The decision is made at the far end: grouping all 4,096 halves by
their outermost six cells, the share of identical sisters is 0 or 1 in 56 of the 64 groups (exploratory, no
predictions written). Not proved: that a change confined to the right edge's band (the thin strip of §8.30) can
never re-enter the core. Not explained: the 37.6%. Both are in the messages to GPT. For
the prize this is a fact about the instrument, not the problem: the counterexample searches over right halves
(§8.21) have been testing fewer distinct columns 1 than halves, about half as many at width 12.

**2. LR for the words that leave column 1 almost free (§7's "mostly zeros").** `records_word.c` computes the exact
record $R_w(d)$ for any periodic wall word $w$, by the anti-diagonal recurrence of §8.36 generalised: a free bit
branches below depth $d$ and is forced above it. Its controls: $R(d)$ for the 0101 wall equals the record file at
every depth 1 to 61 (W0); the word 0 reaches the cap from every depth, the word 1 gives the universal fibre
(0 from even depths, 1 from odd; my control W1 had said "1 at every depth", a wrong statement of the fibre, and
failed on that wording). W2, a cross-check against `rule30_rigidity.py`'s 14-free-bit maxima, gave per rotation 54, 52, 58, 56 for 0001 and 45, 66, 64, 48, 53 for 00001, against the recorded ranges "54 to 58" and "45 to 66": one rotation, 0010, lies 2 below the prose's range. Rerun here, `rule30_rigidity.py` itself (14 free bits, four jobs) gives exactly 54, 52, 58, 56, so the two implementations agree and the prose's lower end was imprecise.

| $d$ | 8 | 12 | 16 | 20 | 24 | 28 | 32 | 36 | 40 | 44 |
|---|---|---|---|---|---|---|---|---|---|---|
| $R_{0001}(d)$ | 24 | 28 | 32 | 52 | 52 | 80 | 76 | 84 | 96 | 100 |

| $d$ | 10 | 15 | 20 | 25 | 30 | 35 | 40 | 45 |
|---|---|---|---|---|---|---|---|---|
| $R_{00001}(d)$ | 35 | 45 | 50 | 85 | 85 | 105 | 115 | 130 |

No run reaches the cap at any depth (W3 held: LR holds to 36 free bits for these words). The growth is linear and not faster (W4 held), and well below the coin's slope (W5 refuted): a least-squares line from depth 24 has slope 2.11 for 0001 against the coin's 3, and from depth 25 slope 2.40 for 00001 against the coin's 4; for 0101 the measured law is 0.83 against 1. The record takes a smaller share of the coin's run the freer the column is: 0.83, 0.70, 0.60. The histograms printed by the engine (`rule30_records_word.txt`) show the bulk to be very nearly a coin, and not exactly one: from depth 45 with 00001, of the $2^{36}$ prefixes 34,359,738,788 end at the first forced cell (run 0), 420 more than half; 17,175,829,450 at the next (run 5), 4,039,734 fewer than a quarter; and so on down to the 314 that reach 130. I first wrote "exactly, to the last digit" here and in the chat; GPT read the file and corrected it (CHAT-LEDGER.1.md C008, RULE30-GPT.md §G3.5), with its own control: for 0101 from depth 21 the first forced cell leaves 512 of 1,024 and the second 268 of the 512. A forced cell is not a balanced function of the earlier free bits, and conditioning on earlier survival does not preserve balance; left-permutivity gives no such theorem. The record is the tail of a nearly fair coin, and the tail is shorter than independent fair coins would give (the merging of §8.38), more so the more free bits there are. $R < 4d$ and $R < 5d$ held throughout (W6).

**3. Do branch points go on for ever? (§8.31.)** Lemma B2 (§8.59) says the eventually white diagonals never stop,
and each is a doubling or a branch; its proof also gives an explicit if weak bound: while the period is $P$, the
pairs of consecutive diagonals' regimes are all distinct, so the period must grow within $4^P$ diagonals.
`rule30_leftside_million.py` ran the single cell's strip of $10^6$ diagonals for $2.2 \times 10^6$ steps (253 s)
and certified it periodic with period 32. Its eventually white diagonals: 2, 7, 28, 399 (doublings, periods 1 to
16), 53,207 and 58,286 (branches), 87,866 (a doubling, 16 to 32), and **none between 87,867 and 1,000,000**. The
list to 160,000 was already in `rule30_leftsides.py`'s recorded outcome; §8.31's prose had not repeated the
doubling at 87,866, and my predictions M0 to M2, built on the prose, missed it (M0 failed on that, M1 and M2
refuted). The worst-phase settling front of §8.59 has slope 2.0057 at a million (M3 held). The counterfactual
("not yet periodic 1,000 steps before the end") was ill set: the strip settles at about 2.006 steps per diagonal
and had 190,000 steps to spare. What the run adds: the gaps between eventually white diagonals, 5, 21, 371,
52,808, 5,079, 29,580, and then more than 912,000, follow no pattern seen; whether the branches among them go on
for ever stays open, and the next white diagonal lies beyond a million.

**Addendum, the four left sides (GPT's ask in CHAT-LEDGER.1.md C004; `rule30_leftside_million.py sides`, predictions L0
to L4 written first).** The four left sides that §8.31 realised, each run to a million diagonals from a settled
strip with the split diagonal flipped (a settled strip is itself a finite row): all four certify with period 32 at
a million (L1 held), and their worst-phase settling slopes are 2.0057, 2.0023, 2.0052 and 2.0076 (L4 held, within
0.01). But they differ beyond their splits (L2 and L3 refuted): the generic side doubles at 87,866; the side
flipped at 53,208 branches again at 72,575 and 165,748 and doubles at 183,183; the side flipped at 58,287 doubles
at 229,337; the side flipped at 53,208 and 72,576 doubles at 291,256. So "the universal left side" is universal
only below the first split, as GPT's audit said to make explicit; beyond it each side has its own white
diagonals. What the four share is what an all-$L$ statement needs: a period that stays tiny ($32$ at $10^6$ on every
side) and a settling slope near 2. That is data for a conjecture with the right quantifiers, not a proof of one.

**What the three items give the prize.** Nothing directly, as expected of small items. Item 1 corrects the
instrument (distinct traces, not halves, are the population of a right-half search). Item 2 tests conjecture LR
where it is weakest and finds the coin's law again. Item 3 settles a number and sharpens a question.


**GPT audit note on §8.60 (2026-10-06).** The committed histograms are approximately geometric, not exact
halvings. For 00001 at depth 45, half of 68,719,476,736 is 34,359,738,368, whereas the first death count
is 34,359,738,788 (420 more). For 0101 at depth 21, a fresh independent control gives survivors 1,024,
512, 268 at consecutive forced tests, not 1,024, 512, 256. Left-permutivity supplies no exact conditional
halving theorem here. Also the finite agreement windows in the synchrony runs need an additional invariant
proof before “for ever” follows. See RULE30-GPT.md G3.4–G3.5 and CHAT C008; the original prose is preserved
for Local to correct. These qualifications do not change the computed record maxima.


### 8.61 Question 3 assessed: the certificate it asks for is question 1 in another costume (2026-10-06)

Question 3 of PERIOD-TWO.md asked for a machine-found certificate: encode the forced walk inside a zero run as a
string rewriting system and search, with SAT, for an arctic matrix interpretation or an automaton invariant with a
ranking function that proves every run ends, as Yolcu, Aaronson and Heule did for weakenings of Collatz. It had
never been started. Before building an encoding (a leap), the step: what would such a certificate have to be?

**What a certificate is here.** The forced walk from depth $d$ (§8.37) has as its state the last two anti-diagonals
of the left half, about $d + k$ bits after $k$ steps, and it ends when a forced cell shows a 1. A termination
certificate is a function $\Phi$ of the state, non-negative, that falls by at least a fixed amount at every forced
cell passed and never rises at a linear one. Then no walk from a state of potential $\Phi_0$ can pass more than
$\Phi_0 / \delta$ forced cells, and the run from depth $d$ is bounded by about $2\Phi_0 / \delta$.

**Two things pin $\Phi$ down.** First, walks of length $0.83\,d$ from every depth $d$ exist (§8.36, exact to depth 85),
so $\Phi$ at the start must be at least linear in $d$: any certificate scales with the seed, as the question itself
noted from Condrey's bound. Second, the state's description also grows linearly, and no bounded-size interpretation
(a fixed finite automaton, a fixed matrix dimension) can carry a potential that is linear in an unbounded string
*and* knows which forced cells will be 0: the walk's forced cells are the chaotic core's own values. So $\Phi$ would
have to be a statistic of the whole state that falls at each forced cell, which is a counting statement: the
number of continuations still able to keep the run alive falls by a constant factor per forced cell. That is the
bounded-debt form of question 1, $N(T + k) \le 2^{c - \alpha k} N(T)$, written as a potential $\Phi = \log_2 N$.

**So question 3 waits on question 1.** The only potentials anyone here has named are counting ones, and a counting
potential is question 1. That is a statement about the candidates in hand, not an impossibility: GPT's audit
(RULE30-GPT.md §G5, CHAT-LEDGER.1.md C012) rightly objects that a fixed matrix can carry a potential linear in an
unbounded string (the unary counter), that a ranking need not be a population-decay curve ($2^d$ countdown paths
of length $2d$ have a linear ranking and a flat survivor count), and that "walks of length $0.83\,d$ from every
depth" is measured to depth 89, not proved. The first version of this section claimed an equivalence and an
impossibility; both are withdrawn. What stands: SAT can search only a finite family of candidates, none has been
named, and what SAT does well here it has already done (the crib of §8.37, the ladder's exhaustive checks). Closed
as a route of its own until a family of potentials is named; its tools would then serve, and the naming is where
the work is.


**GPT audit note on §8.61 (2026-10-06).** A fixed 2-by-2 matrix with diagonal entries 1 and upper-right
entry 1 represents unary length: its n-th power has upper-right entry n. Fixed dimension therefore
does not prohibit a potential linear in an unbounded word. Further, 2^d labelled paths all terminating
after 2d countdown steps have a decreasing linear ranking but no uniform fractional survivor
contraction: the population stays constant until termination, including a window beyond step d.
Thus an individual ranking is not equivalent to the stated bounded-debt count law. These examples
are not Rule 30 certificates; the practical deferral until an actual candidate remains reasonable.
The general impossibility/equivalence argument needs qualification. See RULE30-GPT.md G5 and CHAT C012.


### 8.62 The owner's question: what "period 1" means, whether period 2 had to follow, and the ladder by freedom (2026-10-06)

The owner asked, on the morning of 2026-10-06: the prize asks whether the centre column of Rule 30, from one black
cell, ever becomes periodic; Condrey proved that no nonzero finite configuration has an eventually constant centre
column, "period 1", and our work has been on "period 2" as his own next step. But what does period 1 even mean,
does period 2 necessarily follow, where else could one have started, and what would period 3 look like?

**What the words mean.** The centre column $c(t) = x_t(0)$ is *eventually periodic* if there are $T$ and $p \ge 1$ with
$c(t + p) = c(t)$ for every $t \ge T$. The prize's conjecture is that it is not; so the conjecture is the conjunction,
over every $p$, of "not eventually periodic with period $p$". "Period 1" is the case $p = 1$: the column eventually
constant, $000\ldots$ or $111\ldots$ from some time on. "Period 2" is the case of least period 2: $0101\ldots$ or
$1010\ldots$ from some time on. The cases are logically independent of one another, and there are infinitely many.

**Why a statement about all finite seeds from time 0 is the right shape.** The row of the single cell's pattern at
time $T$ is itself a finite configuration, of width $2T + 1$. So "the centre column is $p$-periodic from time $T$ on,
from the single cell" is the same as "the centre column is $p$-periodic from time 0, from that finite seed". A
theorem of the form *no nonzero finite configuration has a centre column $p$-periodic from time 0* therefore
settles period $p$ for the single cell, "eventually" included. That is the shape of Condrey's theorem (§5,
PRIOR-ART.md: no nonzero finite configuration has a centre column constant from time 0 for longer than $w + 2$
steps, sharp), and it is the shape of everything in this record: Conjecture B, the ladder, the records, the
exclusions. Period 1 was not a special case of the single cell's column; it was the first wall.

**Does period 2 follow?** Not logically. Nothing about period 1 implies anything about period 2, and settling
period 2 would settle nothing about period 3. The prize needs every period at once, so an enumeration by period
can never finish; what it can do is show the uniform argument somewhere. Period 2 was chosen as the smallest open
case and the simplest wall that is not constant. That choice is Condrey's, and it is natural, but it is not forced.

**The ladder that the record found is not the period but the freedom.** Fix the wall: column 0 equal to a word $w$
of period $p$ with $z$ white cells per period, from time 0. By Lemma 1 (§8.2), column 1 is visible to the left
half only at the white times, and by Lemma 4 the cells of the forced left half come in two kinds: a linear cell for
every white time (set at will by column 1's bit) and a forced cell for every black time (a condition). Write
$f = z / p$ for the wall's *freedom*. The coin model of §8.38 then says the record zero run grows like
$R_w(d) \approx \frac{f}{1 - f}\, d$, less a merging loss. On that scale:
- Condrey's wall $1^\infty$ has $f = 0$: no free bit, the universal fibre, $R = 1$. The proof lives here because
  the wall admits no choice at all.
- The one-hole walls $0\,1^{p-1}$ have $f = 1/p$: one free bit per $p$ steps, the least free walls there are, and
  the nearest to Condrey's. `rule30_rigidity.py` found them the most rigid of all words (§7, R5), and nobody has
  tried to carry Condrey's argument across to them.
- Our wall $0101$ has $f = 1/2$: the middle of the scale, with $R \approx 0.83\,d$.
- The words that are mostly white, $0^{p-1}1$, have $f \to 1$: §8.60 measured $R \approx 2.1\,d$ and $2.4\,d$ for 0001
  and 00001.
Period 3 is two walls on opposite sides of this scale, $011$ ($f = 1/3$) and $001$ ($f = 2/3$); every general
statement in this record (Jen's theorem; Theorems A, A′, B; E and E″; the band lemmas; the window principle)
holds for every period, and the records engine of §8.60 takes any word, but §8.8 found that no wall other than
$0101$ turns a wheel, so the specific structure of §8.4 to §8.11 does not carry. "Period 3" would be the same
missing statement (§5) with different numbers, twice.

**Where else one could have started.** Three places, by this reading.
1. *The Condrey end.* Extend his monotonicity (next to a constant wall, column 1 can only turn black once) to
   the one-hole walls, one free bit per period, and see what survives. This is the job given to GPT on the
   morning of 2026-10-06 (CHAT-LEDGER.1.md C018); the measurement that goes beside it is below.
2. *The single cell's own pattern.* The prize is about one configuration, which has structure no general finite
   seed has (the universal left side, §8.30 and §8.31; the nested right side; the core between). A proof that its
   centre column has unbounded zero runs, or unbounded factor complexity, would settle the prize without any
   wall. Nothing in this record reaches the core of the single cell's pattern, and the two bands are provably
   far from the centre, so this route has no foothold yet.
3. *The uniform count.* Question 1 of PERIOD-TWO.md, stated for every wall at once: the number of finite seeds of
   width $w$ whose centre keeps any period-$p$ word for $T$ steps falls like $2^{w - \alpha T}$. Only this shape
   wins the prize, whichever wall is studied first.

**The measurement at the Condrey end** (`rule30_records_word.py holes`, predictions H0 to H3 written first; the
engine `records_word.c` of §8.60 widened to 512 bits; results in `rule30_records_word.txt`). H0 and the counterfactual passed (0111's 14-free-bit maximum is 19, as rigidity recorded; the word 0 caps and the word 1 never exceeds 1). **H1 held: no run reaches the cap**, so LR holds for the six one-hole walls to 32 free bits, at depths up to 256.

| Word $w$ ($f = 1/p$) | depths | $R_w(d)$ | $R/d$ at the deepest | coin's $f/(1-f) = 1/(p-1)$ | share |
|---|---|---|---|---|---|
| 011 | 24, 48, 72, 96 | 9, 20, 27, 39 | 0.406 | 0.500 | 0.81 |
| 0111 | 32, 64, 96, 128 | 18, 19, 26, 43 | 0.336 | 0.333 | 1.01 |
| 01111 | 40, 80, 120, 160 | 8, 18, 24, 30 | 0.188 | 0.250 | 0.75 |
| 011111 | 48, 96, 144, 192 | 10, 18, 23, 32 | 0.167 | 0.200 | 0.83 |
| 0111111 | 56, 112, 168, 224 | 6, 14, 25, 31 | 0.138 | 0.167 | 0.83 |
| 01111111 | 64, 128, 192, 256 | 8, 16, 22, 31 | 0.121 | 0.143 | 0.85 |

H3 held ($R \le 1.5\,d/(p-1) + 10$ throughout). H2, the slope between the two deepest points within 70% to 130% of the coin's, was refuted: two-point slopes of small numbers are noise (0.60 to 1.59 of the coin's), and the
ratio $R/d$ at the deepest point is the better statistic. It says something the free side did not: **on the rigid side the record keeps about 0.8 of the coin's share** (0.75 to 1.01 across $p = 3$ to $8$; the one outlier, 0111 at depth 128, is a lucky walk reached by 16 of $2^{32}$ prefixes), the same share as the 0101 wall's 0.83, while on the free side it fell to 0.70 and 0.60 (§8.60). So the merging loss is a property of freedom above one half, and below it the coin model with one fixed factor describes every wall measured. The one-hole walls are not more rigid than the coin predicts; they are rigid because the coin gives them one free bit per $p$ steps. For GPT's job that is the number to match: a proof at the Condrey end would have to allow runs of about $0.8\,d/(p-1)$, and Condrey's own argument allows $w + 2$ with no free bit at all.

**An exploratory negative, the same morning (no predictions written; it died at once).** I had hoped the one-hole
walls were *perturbed Condrey*: next to the constant wall the left half is the alternating fibre, on which Rule 30 is
affine, so a hole might inject a single ray travelling left at speed 1 and flip one cell of the time-0 row, which
would bound the record by about $2d/(p-2)$ at once. Three facts for $p = 3, 4, 6, 8$ kill it: with every hole
zero the left half is not the fibre (the wall has white cells); a single hole flips 11 to 115 of 160 depths, its
whole leftward cone, chaotically; and the map from holes to the row is not linear (38% to 47% of cells disagree
with the XOR of single-hole effects). There are no rays. What survives of Condrey's monotonicity has to survive
chaos in the left half; the one strong constraint the holes leave is that column $-1$ is pinned at $p - 1$ of every
$p$ times (CHAT-LEDGER.1.md C021).

**The two Condrey ends (after GPT's reading of his proof, RULE30-GPT.md §G11, CHAT-LEDGER.1.md C020).** Condrey's
period-1 theorem has two mechanisms, one per constant wall. Next to the white wall $0^\infty$ the latch: when
$x_t(0) = 0$, $x_{t+1}(1) = x_t(1) \lor x_t(2) \ge x_t(1)$, so column 1 can only turn black, once. Next to the black wall
$1^\infty$ the fixed checkerboard, with no latch. So the freedom scale has a Condrey end at each end, and they are
different problems. At the black end, $0\,1^{p-1}$, the checkerboard survives one hole only as a prefix: GPT's
§G11 proves that at each white time $np$ the first $p-1$ left cells are $[h, h, 1-h, 1, 0, 1, 0, \ldots]$ with
$h = 1 - \sigma(np)$, which for $p \ge 5$ forces a black cell at depth $2\lfloor (p-1)/2 \rfloor$ and excludes any
smaller initial left support; the comparison cone reaching the next hole is where the argument stops, and the
left half past the hole is chaotic (above). At the white end, $0^{p-1}1$, LR is false for the limit wall (column 1
zero gives the zero configuration), so the statement must be B, with a real right half, as Condrey's own proof
needed; and the latch gives a one-line lemma there: *between two black times of the wall, column 1 is
non-decreasing; at a black time it may fall to $\lnot(x_t(1) \lor x_t(2))$.* So per period column 1 takes one of at
most $p + 1$ shapes, $0^a 1^b$ then one reset, and carries at most $\log_2(p+1)/p$ bits per step: 0.79 for $p = 2$,
0.40 for $p = 8$, against one condition per $p$ steps. The bound falls like $\log p / p$ and the conditions like
$1/p$, so the latch alone closes no white-end wall: §8.45's positive-entropy gap in miniature. Freedom orders the
slopes of the records, not their values: GPT notes the maximal run from depth 1 is 1 for 0101 and 2 for 0111.


### 8.63 If period 2 had never been proposed: the next steps after Condrey, and a reframing of the work (2026-10-06)

The owner, after §8.62: "Can you expand on what alternative next steps might be imagined, as if Condrey's period 2 had
not been proposed. This becomes a full workflow reframing of where we should give our attention, as the current
pathway and projection is built off a predicate that does not, necessarily, follow logically." This section is that
expansion. It is reasoning, with one measurement started beside it; nothing here is a theorem.

**1. What a next step has to be.** The prize is one orbit, and "eventually periodic" quantifies over every period $p$
and every starting time $T_0$. Because the row at time $T_0$ is a finite seed, the only statements that bear on the
prize are theorems over *all finite seeds* (or over all $T_0$ at once). A finite exclusion never helps: computing the
single cell's centre column to time $T$ excludes every $(p, T_0)$ with $T_0 + 3p < T$ for every $p$ at once, which
is more than any of this record's finite exclusions (the ladder's 248 cells, the records' 84) says about the prize.
Those exclusions are evidence for conjectures LR and B and tests of mechanisms; they are not steps toward the prize.
So "the next step after Condrey" means: *the next family of walls over which a theorem can be proved*, chosen so
that the mechanism found there has a chance of being the uniform one.

**2. The two coordinates of a wall.** A periodic column 0 is a word $w$ of period $p$. Two numbers describe how it
treats the left half. Its *freedom* $f$, the share of white cells, is the share of steps at which column 1 is
visible to the left half (Lemma 1, §8.2) and hence the rate at which the right half can inject bits; §8.62 is the
ladder along $f$. Its *switch density* $s$, the number of colour changes per step, is the rate at which the wall
interrupts the two mechanisms of Condrey's proof: next to a white stretch, column 1 can only turn black (the latch),
and next to a black stretch of $r$ steps the forced left half is the checkerboard to depth $r - 1$ whatever column 1
is (Lemma 1 again: $x(-k, t) = (k+1) \bmod 2$ whenever $\tau(t), \ldots, \tau(t+k)$ are all black). Condrey's walls
have $s = 0$. The wall $0101$ has $s = 1$, the largest possible: it switches every step, so neither mechanism ever
has time to act, and a third one appears there and nowhere else, the wheel (§8.8). Measured by $s$, period 2 is not
the simplest non-constant wall; it is the one farthest from Condrey's.

**3. The alternatives, as a map.**
- *Along $f$ at small $s$: the one-hole walls* $0\,1^{p-1}$ (§8.62, GPT's §G11 to §G13). Freedom $1/p$, switch density
  $2/p$. The checkerboard survives each hole as a prefix; past the hole the left half is chaotic; LR there is the
  statement, measured at $0.8\,d/(p-1)$.
- *Along $s$ at any $f$: the slow walls* $0^a 1^b$ with $a, b \to \infty$. One switch pair per period, and each
  mechanism gets its stretch. What the left half sees per period is explicit: during the black stretch nothing
  from the right (column 1 is invisible, the checkerboard forms by force to depth $b - 1$); during the white
  stretch, column $-1$ copies column 1 ($x(-1, t) = \sigma(t)$ while the next wall cell is white, and its complement
  at the last white step), and column 1 from a real right half is latched, $0^{a'} 1^{a - a'}$, one integer. (Two
  endpoints, after GPT's §G18: the checkerboard to depth $b - 1$ holds at the *start* of the black stretch, and at its
  last black time the first left cell is already 1.) So a real right half injects $O(\log a)$ bits per
  period into the left half, against about $a + b$ conditions, and the target for the left half is nearly
  deterministic: its own column $-1$, under its own autonomous evolution with the wall as boundary, must read
  $0^{b-1} 1$ through every black stretch and a monotone word through every white one. This is the cleanest form of
  the question anywhere on the map: a finite half-line seed, a periodic boundary, and a column that must be a fixed
  word on long stretches for ever. The one-hole walls are its $a = 1$ corner. In the other corner, $a \gg b$, the
  latch dominates and the statement must be B (LR is false for $0^\infty$).
- *Along $p$ at $s \approx 1$: the by-period ladder.* Period 2, then 3 (two walls, $011$ and $001$), then 4. Each is
  a new wall with the switches every step or two; the wheel of period 2 does not carry (§8.8), so each would need
  its own structure. This is the ladder the project has been on. Its justification was that 0101 is the smallest
  open case, which is true, and that the uniform argument must show itself somewhere, which is true of every
  family.
- *The single cell itself.* The prize's orbit has structure no general seed has (the universal left side, the nested
  right side, the core). A direct proof that its centre column has unbounded complexity or unbounded runs would
  need a handle on the core, and the two bands are provably far from it (§8.30). No foothold is known.
- *A condition that forces a neighbour column periodic* (question 2's move). Next to a white stretch the latch
  makes column 1 eventually constant; with $p \to \infty$ that is Condrey's white case through Jen's theorem. On
  slow walls the latch holds per stretch, which is why they are the family where this move has the most to work
  with.

**4. What the measurements say so far.** §8.42 measured the horizon of real seeds for every word up to period 4 and a
random word: total width plus 6 to 10 steps, the same law for all, which says that for *real* right halves the cost
per step is about one bit whatever the wall, because the right half pays for column 1 too (§8.51). §8.60 and §8.62
measured LR's records across $f$ and found the coin's law with a share between 0.6 and 1.0. Neither measured $s$ at
fixed $f$. `rule30_records_word.py slow` (predictions SW0 to SW3, written first) now takes the walls $0^a 1^a$, which
have 0101's freedom and switch densities $1/a$, for $a = 2, 4, 8, 16$: if the law stays $0.83\,d$ the checkerboard
stretches cost nothing and freedom is the whole story; if it falls, switch density is a second axis and the slow
walls are a genuinely different problem. **Measured** (8 threads, 7 minutes; SW0 and SW1 passed, no cap): $R/d$ at depth 48 is 0.812, 0.812, 0.667 and
0.792 for $a = 2, 4, 8, 16$, against 0.83 for 0101 and the coin's 1. SW2, which predicted a fall to below 0.60 at
$a = 16$, is **refuted**; SW3 held with room to spare (the longest run at $a = 16$ is 38). So no fall of the predicted
size was seen: in this run the checkerboard stretches did not cost the free column 1 what I expected. That is what
the data say and no more (GPT's qualification, CHAT-LEDGER.1.md C033, is right: four ratios at one depth do not fix
an asymptotic slope, and a switch-density effect stays unresolved; my first wording, "freedom is the whole story",
overstated it). What the slow walls change for certain is the B side: the budget of a *real* right half, which the
latch cuts to one integer per white stretch, and which GPT's §G15 makes exact for the width-one relaxation: a rate
of $\log_2(a+1)/(a+b)$ bits per step. The reframing below is adjusted accordingly.

**5. The reframing, as a workflow.** Three changes, offered for the owner's decision (DECISION OWED):
1. *Stop extending finite exclusions as a goal.* The ladder's next depth and the records' depth 93 would cost days
   and move no theorem; §1 above says why they cannot. They remain useful as instruments for testing a mechanism
   (the records engine took any wall in minutes this morning) and should be run for that purpose only.
2. *Give the slow walls the attention period 2 has had, on the B side.* The measurement above says LR is no easier
   there, so the target is B: a real right half, whose column 1 the latch cuts to one integer per white stretch,
   driving a finite left half that must answer every black stretch with the fixed word $0^{b-1}1$. The first
   theorem to try: with the right half's injection explicit ($O(\log a)$ bits per period against $a + b$
   conditions), prove the bounded-debt count of question 1 for this family, where the "debt" is paid by a single
   integer per period rather than by a chaotic column. GPT's exact finite mechanisms at the one-hole corner (§G11
   to §G13) are the right kind of object for the two switch events. GPT's §G18 and §G19 (2026-10-06, hours later) already
   supply the first pieces: for $b \ge 3a + 1$ the row at the first white time is the checkerboard on depths $4a$ to
   $a + b - 1$ whatever the inputs; on balanced walls the real-right latch excludes freely driven prefixes (a finite
   support exclusion, interior latch positions minimising); and the caution that certifying both switches does not
   make the per-period state finite, because the spatial tail is a state of its own that needs a closure or cost
   theorem. That tail is the precise missing item.
   *Measured the same morning (`rule30_uniform.py slow`, US0 to US3 written first):* next to $0^a 1^a$ for $a = 4, 8, 16$
   every right half of width up to 16 keeps its centre on the word for at most its total width plus 9, 7 and 6 steps
   (the empty right half next to $0^{16} 1^{16}$ alone reaches +15), and for $a = 8$ and $16$ the excess is negative from
   width 7 on. Three blind predictions missed on the empty right half and on a flag's semantics (the probe's outcome
   says how); the law of §8.42 stands on the slow walls, with smaller constants than 0101's. That is the B side's
   promise in numbers: the latch leaves a real right half little to say, and the left half pays for it.
3. *Keep period 2's record as the measured reference, not the route.* Its wheel is special, its channel bound is
   certified, its counting form is measured to width 26; a proof on the slow walls would be tested against it,
   not derived from it.
What does not change: the uniform count of question 1 is still the only shape that wins, whichever family it is
first proved on, and the method (predictions first, failures kept, two readers) is the same on every wall.

The owner's second question the same morning, what we would investigate if we were not chasing the money, is answered
in [CONSTELLATION.md](CONSTELLATION.md), which also carries this section's families as its Part A.


### 8.64 What makes 30 special among the 256: the left band of every rule (2026-10-06)

Row 14 of CONSTELLATION.md, taken as the cheapest question that bears on all the others: which of this record's facts
are Rule 30's and which belong to its class. `rule30_otherrules.py` (predictions OR0 to OR4 and CF written first; two
runs, 7 s and 3 s) runs the band instrument of §8.30, §8.31 and §8.59 on every elementary rule for which the instrument
is valid: the left edge of the single cell must move at light speed, $f(0,0,1) = 1$, and the white tail must stay white,
$f(0,0,0) = 0$. There are 64 such rules. (The first run used the 128 with $f(0,0,1) = 1$ alone; six of its nine
"nontrivial bands" were artefacts of a frame no configuration realises, among them Rule 135, Rule 30's colour-complement,
which showed Rule 30's band exactly. The scope error is in the probe's outcome; the second run is the result.)

**The result.** Of the 64 rules, from the single cell to 8,192 diagonals:
- **three** have a certified band with a small period: **Rule 30** (period 16; eventually white diagonals 2, 7, 28,
  399), **Rule 110** (period 32, doublings at diagonals 2, 3, 5, 7 and 45, no eventually white diagonal) and **Rule
  118** (period 4, no eventually white diagonal; nearly trivial);
- 47 are trivial (every diagonal of period 1 or 2);
- 14 do not certify within period 1,024: the additive and nested rules, 18, 22, 26, 82, 86, 90, 102, 126, 146, 150,
  154, 182, 210 and 218, whose diagonal periods grow too fast for the strip to repeat.

Three of the four blind predictions were refuted: I expected 5 to 30 rules with a nontrivial band (OR2: 3), Rule 30's
period to be the smallest among them (OR3: 118 has 4 and 110 has 32), and some other rule to share the white diagonals
2 and 7 (OR4: none). OR1 held: the mirror 86 and the linear rules do not certify.

**What it says.** The odometer at the left edge is rare: two rules in sixty-four have one worth the name, and they are
the two famous ones, 30 and 110. Rule 30 is the only rule whose band grows its period through eventually white
diagonals, which is Rowland's parity mechanism (§8.27, §8.31) and depends on Rule 30's OR and XOR; Rule 110's band
doubles by some other mechanism, five times in the first 45 diagonals and then not again below 8,192. So of the facts in
this record, the universal band's existence is shared with 110 and 118, its white-diagonal clock is Rule 30's own, and
the nested right side belongs to the additive-like rules that fail to certify here. The wheel, the channel and the
forced left half were not tested on other rules; they need the wall form, which is next (the instruments take any
rule's truth table). Recorded in CONSTELLATION.md, row 14.

**Addendum, the same morning.** The wall-form instruments (the forced left half, the records, the channel) need
left-permutivity, $f(0, c, r) \ne f(1, c, r)$ for every $(c, r)$. Among the 64 rules above exactly four are left-permutive:
30, 90, 150 and 210; 90 and 150 are linear. So Rule 210, $x' = l \oplus (\lnot c \land r)$, is the one sibling on which
the wall-form instruments can be tried as they stand (its OR becomes an AND-NOT in the anti-diagonal recurrence); its
single-cell band did not certify within period 1,024 at 8,192 diagonals. Rules 110 and 118, which share the odometer,
are not permutive in either direction, so they have no forced left half and the comparison stops at the band.

**The chaos item (GPT's seed, CHAT-LEDGER.1.md C045): the background is part of the object.** Colour-complement
conjugacy, $f'(n) = \lnot f(\lnot n)$, maps a rule on a white background with a black defect to its conjugate on a black
background with a white defect. Checked: the physical strip of Rule 135 (a white defect in black, the black tail kept
black) is the complement of Rule 30's strip at every one of 300 steps. The six artefacts of the first run have
conjugates 37, 25, 41, 9, 30 and 22: two of them (135 and 151) are Rule 30 and Rule 22 seen through the wrong
background, and four (91, 103, 107, 111) are conjugate to rules whose single cell does not even move at light speed,
so their "bands" were frames of nothing at all. The 128-rule census double-counted by conjugation; the 64 valid rules
are the whole census up to it. (Rule 30's own artefact frame, a black tail, turns white in one step because
$f(111) = 0$, which is why the artefact showed Rule 30's band two diagonals shifted.)


### 8.65 Rule 210, the one sibling: conjecture LR is false there (2026-10-06)

§8.64 found that among the 64 rules whose single cell has a light-speed edge and a quiescent white tail, exactly one
other rule is nonlinear and left-permutive: Rule 210, $x' = l \oplus (\lnot c \land r)$. Its inverse reads
$l = x' \oplus (\lnot c \land r)$, so the forced left half of §8.39 exists for it with the OR of Rule 30's inverse replaced by
an AND-NOT, and `records_word.c -DRULE210` runs the same search (predictions Z0 to Z3 and CF written first; the run took
seconds). The question was whether Rule 30's rigidity at period 2, conjecture LR with its records at $0.83\,d$, belongs to
the rule or to its class.

**It belongs to the rule.** Next to the wall 0101, Rule 210's forced cells never show a 1: from every depth tried (1, 8,
16, 24, 32) every prefix of column 1 continues to a zero run that reaches the search's cap, 509 cells (Z1, Z2), while the
control with Condrey's black wall gives $R = 0$ as it must (CF). An independent greedy computation by the column
recurrence confirmed zero runs of 112 cells from depth 8 for all 16 prefixes, and found an explicit column 1 whose
forced left half is **empty at time 0**: visible bits $1\,0\,1^2\,0^4\,1^8\,0^{16} \cdots$ (I first wrote "$1011\,0000\,1111\,1111$
then zeros", which is wrong: with zeros after the sixteenth bit a 1 appears at depth 65; GPT's §G26 caught it). The
left half-line is white and stays consistent with the wall for ever, and GPT's §G26 proves it: on the empty left half
the occupied cells satisfy $t + j$ odd, so no two neighbours are both black, the AND-NOT reduces to XOR, and the system
is Rule 90 driven by 0101; the visible bits are $\sigma(2n) = \lfloor \log_2 n \rfloor \bmod 2$, the parity of Rule 90's
Catalan return paths, which switches at the powers of two. So conjecture LR, that no column 1 at all gives a finite forced left half, is
false for Rule 210 at period 2, from the very first depth.

**What is not settled.** Conjecture B, that no finite configuration keeps the centre 0101, is open for Rule 210: a search
over every right half of width up to 20, the wall at its left end, found none that keeps 0101 for 300 steps (Z3; most die
within a few steps, as for Rule 30). So Rule 210 is a rule where the one-sided conjecture fails and the two-sided one
may still hold, which is the gap between LR and B made concrete on a rule where it can be studied cheaply.

**What it means for the record.** Rule 30's records ($R \approx 0.83\,d$), the exact halving of survivors at the forced
cells, Theorems A to E and the band lemmas were all derived for Rule 30's OR. The band exists on Rule 110 and 118 too
(§8.64); the rigidity of the forced left half does not survive the change of one gate. "Rule 30 is special" now has
two measured senses: the white-diagonal clock in its band, and LR. CONSTELLATION.md row 14 is updated.

**Addendum, the same hour: Jen does not rescue B for Rule 210, and the empty-left-half column is a doubling-runs
sequence.** The hope of CHAT-LEDGER.1.md C053 was that every zero-keeping column 1 of Rule 210 might be eventually
periodic, so that Jen's theorem would give B. `rule210_streams.py` (predictions ZS0 to ZS2 and CF written first) followed
every zero-keeping stream from depths 1, 8, 16 and 24, all 4,369 of them, for 4,000 depths: **none shows a period up
to 64 over its last 2,000 visible bits** (ZS1 and ZS2 refuted outright; a finite test, as GPT's C057 notes, but the
empty-left-half stream is proved aperiodic by §G26's formula, which already defeats the hope). So the zero-keeping choice is not a bounded-window function of the row, and B for
Rule 210 is a real open question, not a corollary. The stream that keeps the whole left half empty from depth 1 is,
$1\,0\,1^2\,0^4\,1^8\,0^{16} \cdots$, runs of lengths $1, 1, 2, 4, 8, \ldots$ (measured to 1024, then proved for all $n$ by
§G26: $\sigma(2n) = \lfloor \log_2 n \rfloor \bmod 2$), with no limiting frequency of ones (the run ends give subsequential
densities $1/3$ and $2/3$; my "0.34" was one window's count) and factor complexity
$p(n) = 10, 15, 20, 25, 31, 40, 63$ at $n = 4, 6, 8, 10, 12, 16, 24$: linear, so zero entropy. A chaotic-looking rule
whose empty left half is kept by a sequence of doubling runs is the kind of object CONSTELLATION.md is for; its proof
is GPT's §G26 (a linear subsystem, Rule 90, inside a nonlinear rule), and its right half (B) stays a search item.

**Second addendum: next to 0101, Rule 210's forced left half is always Rule 90's.** `rule210_streams.py parity`
(PS0 to PS2 and CF written first) asked which zero-keeping streams share the parity-sparse regime of §G26. All of them:
every one of the 4,368 streams from depths 8, 16 and 24 has no two horizontally adjacent black cells anywhere in a
300 by 300 window (PS1 refuted the other way). The reason is a two-line theorem that holds for *every* column 1.

**Theorem (the parity invariant).** With column 0 equal to 0101... ($x(0, t) = t \bmod 2$) and any column 1, every
black cell $(-m, t)$ of Rule 210's forced left half has $t + m$ odd, and the forced left half is exactly Rule 90's:
$x(-m, t) = x(-m+1, t+1) \oplus x(-m+2, t)$.

*Proof.* Column 0 is black at odd $t$, parity $t + 0$ odd. Column $-1$: $x(-1, t) = \tau(t+1) \oplus (\lnot \tau(t) \land \sigma(t))$
is $1 \oplus \sigma(t)$ at even $t$ (parity $t + 1$ odd) and $0$ at odd $t$. Induction on $m$: the inverse rule is
$x(-m, t) = x(-m+1, t+1) \oplus (\lnot x(-m+1, t) \land x(-m+2, t))$, and the cells $(-m+1, t)$ and $(-m+2, t)$ have
parities $t + m - 1$ and $t + m$, so by the invariant they are never both black: when $x(-m+2, t) = 1$ its neighbour is
white and the AND-NOT equals $x(-m+2, t)$; when it is 0 the term is 0. So the term is $x(-m+2, t)$ in every case,
the rule is Rule 90's inverse, and $x(-m, t) = 1$ needs one of $(-m+1, t+1)$, $(-m+2, t)$ black, both of parity $t + m$,
so $t + m$ is odd. $\square$

**Consequences.** Everything in §8.65 follows at once: the forced left half is a linear function of column 1 over
GF(2), so "row zero beyond depth $d$" is a system of linear equations on the visible bits and the zero-keeping
streams form an affine space. Linearity alone does not make that space non-empty (an affine system can be
inconsistent; GPT's point in C061, taken): what does is GPT's finite-support construction (§G27.3), which inverts
the first $2n$ cells of any $n$-bit visible prefix and sets the deeper initial cells to zero. So every prefix
extends, conjecture LR fails, and the empty-left-half stream is the particular solution §G26 computed. Conjecture B for Rule 210 at period 2 becomes a
clean question: *does any finite right half of Rule 210, evolving against the wall 0101, produce visible bits that
satisfy that linear system?* The width-20 search says none does; the search can now be replaced by linear algebra over
the right half's own dynamics, which is nonlinear (the AND-NOT fires on the right, where the invariant does not hold).
For Rule 30 the same induction fails at the first step: its OR is 1 whenever either neighbour is black, so no parity
invariant forces linearity, and the forced left half is chaotic. That is the exact sense in which Rule 30's rigidity
is its OR.


### 8.66 The leftward light speed is the background's: $0.246 = 1 - 0.41 \times 1.84$; the checkerboard heals, the band locks (2026-10-06)

CONSTELLATION.md row 3, chosen by a random draw after the owner asked the two models to stop converging on the same
rows. Rule 30's rightward speed of influence is exactly 1; the leftward one was measured at 0.246 on a random
background (§8.30, LB5) and never derived. `rule30_damage_speed.py` (predictions DS0 to DS5, CF, then DL1 and DL2,
written and pushed before each run) measures it on structured backgrounds, with the two factors that make it.

**The identity.** In diagonal coordinates $k = x + t$ the rule reads $D_k(t+1) = D_{k-2}(t) \oplus (D_{k-1}(t) \lor D_k(t))$ on the whole plane, so a difference between two configurations never reaches a lower diagonal. Its lowest
damaged diagonal $k_{\min}(t)$ can only rise, and it rises exactly when the undamaged diagonal below it is black at
that step: then $D_{k_{\min}}(t+1) = D_{k_{\min}-2}(t) \oplus 1$ is the same in both copies. The leftmost damaged
cell is at $x = k_{\min} - t$, so

```math
v = 1 - P(\text{heal}) \cdot E[\text{jump} \mid \text{heal}],
```

an identity (it held within 0.009 on every background). I had written in the predictions that the jump is at most
2, because $D_{k+2}(t+1) = D_k(t) \oplus (\cdots)$ always carries damage two diagonals up; that is wrong where the
damage is dense, since the OR can then differ too and cancel the XOR, and the instrument check DS1 caught it: jumps
of 5, 7 and 10 occurred. The error is kept in the probe's header.

**What the run found** (eight random trials and eleven structured backgrounds, $2^{13}$ steps each).
- *Random background:* $v = 0.2468$ (DS0 held; LB5's 0.246). $P(\text{heal}) = 0.410$, not $1/2$, and $E[\text{jump}]   = 1.84$, not $1.5$ (DS5 refuted both ways): the front sits preferentially above white cells because it heals at
  black ones, a selection effect, and the jumps are long for the cancellation reason above. So $0.246 = 1 - 0.410   \times 1.839$ to the run's accuracy, and neither factor is the background's density: the first is the density of
  the diagonal below the front *as the front sees it*. A derivation of 0.246 is a derivation of that conditional
  density, which is where the directed-percolation flavour of row 3 lives.
- *The checkerboard* (a fixed point of the rule): $v = -0.388$. The damage front moves RIGHT. Healing happens every
  other step (the diagonal below alternates) with mean jump 2.5, and $0.555 \times 2.5 > 1$: the chaotic region a
  flipped cell creates drifts rightward as a whole and the checkerboard closes behind it. A fixed point that heals
  its left side faster than light. (DS2 predicted $1/4$.)
- *The single cell's own band:* damage put on diagonal 64 at $t = 4096$ climbs for 429 steps and then LOCKS on
  diagonal 400 for ever ($v = 1$ exactly). The mechanism is the band's eventually white diagonals (§8.31): once
  $D_{399}$ is white, $D_{400}(t+1) = D_{398}(t) \oplus D_{400}(t)$ and a difference on 400 is permanent. DL1 held
  for 64 → 400 and 10 → 29, failed for 3 (which is already above the white diagonal 2 and never moves; my
  misapplication) and for 20, which passed 29 and 399 and climbed to 6,259 at $v = 0.2453$: the lock is not
  certain, because $k_{\min}$ jumps, and if diagonal $w + 1$ happens to be undamaged when the front passes $w$ the
  damage goes on. So the eventually white diagonals are *partial barriers* for information moving outward through
  the band, and this is a new role for the doubling positions 2, 7, 28, 399, 87,866. Above 399 the band carries
  damage at the random background's speed (DL2 held: a flip on 500 climbs at 0.2510), so the band's period-16
  diagonals are, as the front sees them, as black as random ones. (DS3 predicted the random speed for the band;
  refuted by the lock, then held above it.)
- *Periodic backgrounds* tiled from one cycle state of each ring $n = 3..10$: speeds from $-0.388$ to $1$ (DS4's
  "spread above 0.05" held by a factor 28; its "densest is slowest" refuted: the densest, ring 10 at 0.700, is among
  the fastest at $2/3$). Where the heal is periodic and the jump exactly 2 the speed is an exact rational: ring 4
  (1000) $1/2$, ring 5 (11001) $1/3$, ring 10 (0011111011) $2/3$; ring 7 gives $0.2222$ and ring 9 $0.2632$; ring 8
  (11000001) gives $v = 1$ with $P(\text{heal}) = 0.0006$, a white diagonal running through it on which the damage
  locks as in the band.

**What it says.** The leftward speed of information is not a constant of the rule. It is $1 - (\text{heal rate})$,
and the heal rate is set by the black cells of the background's diagonals as the front meets them: zero on a white
diagonal (speed 1, the band's lock), every other step on the checkerboard (negative speed), 0.41 on a random
background and, as it turns out, on the band's periodic diagonals too (0.246). The rightward speed 1 and the
leftward 0.246 are therefore different kinds of number: the first is the rule's XOR, the second a statistic of the
orbit. Row 3's "is 0.246 algebraic" becomes "is the front's conditional density algebraic", which nobody should
expect. What is exact and new is the structural fact: the eventually white diagonals of the universal left side are
one-way barriers that information crossing the band outward can be caught on, with the catch probabilistic.

Reproduction: `python3 tests/probes/lexicon/rule30_damage_speed.py 13` (70 s) and `... 13 lock` (40 s). The
outcomes are in the probe's header; the predictions were pushed in `5cee204` and `bfa54ab` before each run.

**Addendum (the same day): each white diagonal is, as measured, a fair coin.** (GPT's caution in C071, taken: the one-half and the independence are exact measurements at three barriers, not a theorem; the heading says "measured" until one exists.) Two more runs of the probe (`lockprob`, `lockphase`;
predictions LP0 to LP3, LQ1 to LQ3 pushed first, most refuted). The catch is deterministic in the flip's diagonal and
$t \bmod 16$, and at every barrier exactly half of the phases that reach it are caught, independently of what
happened at the earlier barriers: at 8 two residues of four (the period above it is 4), at 29 four of eight, at 400
eight of sixteen for every one of eleven flip positions from 30 to 395. So a flip below 8 ends locked with
probability $1 - 1/8$, below 29 with $1 - 1/4$, below 400 with $1/2$, and the damage's density plays no part (LP2
refuted). Which phases catch depends on the flip's diagonal (at 400: flips 300 and 395 are caught on complementary
sets of phases), so the barrier is not a single bit of the clock (LQ3 refuted). Why exactly half is open; the hint
is the doubling itself: the diagonal above a white one is the running XOR of the one two below, so what reaches it
is a parity of the damage's history, and a parity of a long chaotic history is balanced over the phases. For the
owner's question about information in the band: a perturbation anywhere in the single cell's band changes the
phase of the strip above the next white diagonal with probability exactly one half, and the probabilities at
successive barriers multiply.

### 8.67 Rule 30 on rings to $n = 24$, complete: cycle counts, transients longer than cycles, and every cycle a glider on prime rings (2026-10-06)

CONSTELLATION.md row 10, by the random draw; literature first (PRIOR-ART.md: OEIS A334497 and A334496 tabulate the
maximum period and the single cell's period; nothing tabulates the number of cycles, the periodic states, the
transients or the gliding cycles). `ring_census.c` visits all $2^n$ states for $n \le 24$ and certifies every cycle
by a state and a length; `rule30_ring_census.py` carries the predictions (RC0 to RC4, CF, pushed in `71f704c`
before the run) and the table is `rule30_ring_census.txt`. Both OEIS sequences are reproduced to $n = 24$ (A334497's
b-file reaches 36). The four new columns, and what was wrong in my expectations:
- *Cycle counts* $c(n)$: 1, 3, 1, 4, 2, 3, 9, 5, 3, 6, 13, 12, 5, 18, 31, 9, 7, 18, 5, 27, 60, 24, 4, 49. Not divisor
  structure in the way I predicted (RC2 refuted at 7 and 11): prime rings have few cycles *unless* one length is
  repeated, in which case rotation supplies $p$ copies at once (seven 4-cycles at $n = 7$, eleven 17-cycles at 11).
- *Periodic states* $P(n)$: 431 at 12, then 1431, 2082, 1776, 10291, 13805, 4350, 4124, 33926, 16619, 15744, 43172,
  194991 at 24; a fitted $2^{0.553 n}$ (RC1 predicted 0.6 to 0.8) but the fit means little: the periodic set is a
  vanishing and erratic fraction of the ring.
- *Transients*: the longest preperiod is 9,568 at $n = 24$ (RC3 predicted below 200), and at $n = 21$ and $22$ it is
  LONGER than the longest cycle (4,308 against 2,793; 5,477 against 3,553). On a ring Rule 30 can wander longer than
  it cycles.
- *Gliding cycles* (rotation by one cell maps the cycle to itself, so the pattern travels): at every prime $n$ from 13
  to 23 every cycle is gliding. This is a pigeonhole, worth stating because it is exact: rotation permutes the cycles
  of each length and its orbits on a prime ring have size 1 or $p$; at $n = 13, 17, 19, 23$ every cycle length occurs
  once, so every cycle is rotation-invariant and rotation is a power of the time map on it. The 63-cycle of the
  7-ring is one (the 7-periodic tails of §5 are travelling patterns), and the one non-gliding class at 7 and 11 is
  the one repeated length. Which parts are proved, then: the glider statement is proved for the listed $n$ by the
  census plus the pigeonhole; the growth of the maximum period is not proved for any $n$ beyond the table.

What would change the picture: a cycle count that stayed smooth in $n$ would have said the ring's cycles do not
come from sub-rings; they do not, in the way I had assumed, and the count is dominated instead by whether rotation
classes are full. Reproduction: `python3 tests/probes/lexicon/rule30_ring_census.py 24` (40 s, 300 MB).

### 8.68 The triangle census of the single cell: the core's triangles are the uniform measure's to three decimals, $3 \cdot 2^{-(L+4)}$ per cell (2026-10-06)

CONSTELLATION.md row 13, the last cheap-run row nobody was on. `rule30_triangle_census.py` (predictions TC0 to TC4
and CF pushed in `ac4f5c4` before the run) counts the tops of white triangles (§8.18's shrink theorem makes every
triangle exact and fixes it by its top) in the single cell's light cone to $t = 10^5$, by width $L$ and position
$x/t$; the vectorised census was checked top by top against a set-based one over sixty rows.

**The core** ($|x/t| \le 0.3$, area $3.0 \times 10^9$ cells): the counts by width are $281{,}011{,}418$;
$140{,}641{,}871$; $70{,}333{,}586$; $35{,}178{,}509$; $17{,}580{,}624$; \ldots; $137{,}109$ at $L = 12$; \ldots; one
top of width 29. The ratios $N(L+1)/N(L)$ are $0.500, 0.500, 0.500, 0.499, 0.503, 0.500, 0.496, 0.495, 0.507, 0.485$
for $L = 3$ to $12$ (TC1 predicted $[0.4, 0.6]$). The exact law was derived after the run and then matched: the
uniform Bernoulli measure is invariant under Rule 30 (the rule is surjective, being left-permutive), and under it a
maximal white run $[i, j]$ of length $L$ has probability $2^{-(L+2)}$ (white inside, black at both ends) while the
run is a *continuation* with probability $2^{-(L+4)}$ (the $L + 2$ cells above white, and the two beyond them black
so that the run below is exactly $[i, j]$, since $100 \to 1$ and $001 \to 1$). So the density of tops of width $L$
is $2^{-(L+2)} - 2^{-(L+4)} = 3 \cdot 2^{-(L+4)}$ per cell. Against the core's area that predicts $281{,}250{,}000$;
$140{,}625{,}000$; $70{,}312{,}500$; $35{,}156{,}250$; $17{,}578{,}125$ for $L = 1$ to $5$: measured within $0.09\%$,
$0.01\%$, $0.03\%$, $0.06\%$, $0.02\%$; $549{,}316$ at $L = 10$ (measured $547{,}147$); $536$ at $L = 20$ ($505$);
$1.05$ at $L = 29$ (two tops of 28, one of 29; TC2 held). *At the level of triangle births, the core of the single
cell is the uniform measure to three decimals through twelve octaves.* This is Problem 2's kind of statement made on
a two-dimensional object, and the deviation at $L = 1$ ($-0.09\%$ on $2.8 \times 10^8$ counts, far outside Poisson
noise) is real and small; what it is, is not known.

**The right edge.** The widest triangles of the whole cone sit *on* the edge, $x/t = 1.000$, at the times $m \cdot 2^k$: width 40 at $t = 65{,}536$, 38 at $32{,}768$ and $98{,}304$, 36 at $16{,}384$, $49{,}152$, $81{,}920$, 35 at
$8{,}192$ and its odd multiples. They grow like $\log_2 t + 22$, so TC3's "more than twice the core's" was wrong:
the nested side's triangles are large by position, not by scale, and the core's widest ($29 = \log_2$ of $3 \cdot \text{area}/16$) keeps pace with them.

**The left band** ($x/t < -0.6$): tops of width 15 ($21{,}916$) and 16 ($5{,}882$) exist and none wider, against
TC4's "under 12"; the band's ratios are near $1/2$ to $L = 9$ and structured beyond ($0.61$ at 10, $0.88$ at 15).
A reading, not pre-registered: the band's widest white run is its period, 16.

Reproduction: `python3 tests/probes/lexicon/rule30_triangle_census.py 100000` (4 minutes). Literature (PRIOR-ART.md):
NKS note 6.1 has the ratio, "roughly like $2^{-n}$" for rules 126, 30, 150, 182 on random initial conditions, with
no constant and no derivation; the exact $3 \cdot 2^{-(L+4)}$ and the single-cell match were not found there (NKS
p. 871 still to be read; the 1984 paper is a scan not readable here).

**Addendum (the same day): the law is exact, the deficit is the orbit's.** The same census on a random row, counted
only inside the inner light cone where the field is exactly the uniform measure (predictions TR0 to TR2 and CF
pushed in `0a44d87` first), gives deviations of $-0.002\%, +0.003\%, -0.006\%, +0.000\%, -0.004\%, +0.004\%$ from
$3 \cdot 2^{-(L+4)} \cdot \text{area}$ for $L = 1$ to $6$ on $1.25 \times 10^{10}$ cells, Poisson-sized (TR1), and
$-0.002\%$ at $L = 1$ (TR2 held). So the derivation is exact, and the single cell's $-0.09\%$ deficit of width-1 tops
in its core is a property of that orbit. I first wrote "about fifteen standard deviations"; GPT objected (C080)
that tops on a deterministic space-time are dependent and a total count does not license Poisson errors, and the
calibration it asked for (ten time blocks, two halves; predictions TB0 to TB3 and CF pushed in `35ae8a9` first)
proved it right: the width-1 deviation by block is $-0.034\%, -0.220\%, +0.034\%, -0.314\%, +0.087\%, -0.189\%, -0.100\%, -0.074\%, +0.025\%, -0.136\%$, mixed signs with a scatter near $0.13\%$ against a Poisson $0.02\%$. The
sigma claim is withdrawn. What the blocks show instead is where the departure lives: the right half of the core
($0 \le x/t < 0.3$) matches the law at $-0.011\%$ with blocks within $\pm 0.06\%$ and a white density within
$0.003\%$ of one half, while the left half ($-0.3 \le x/t < 0$) carries $-0.161\%$ with blocks from $-0.64\%$ to
$+0.21\%$ and a white density wandering by up to $0.033\%$. So the single cell's core is the uniform measure to
about $0.01\%$ on the side facing the nested edge and only to a few tenths of a percent, block by block, on the
side facing the ordered band, whose influence evidently reaches past $x/t = -0.3$. That is the finding; the
$-0.09\%$ total was an average of it.

**Second addendum: the uniform core begins at the leftward light speed.** Two more pre-registered runs (`bins`, then
`fine`; TN0 to TN3, TF1 to TF3, pushed first) locate the departure. In bins of $x/t$ the width-1 deviation from
$3/32$ is $-1.48\%, -0.89\%, -0.38\%, -0.42\%$ for $x/t$ from $-0.6$ to $-0.2$ and then $\pm 0.05\%$ in every bin
from $-0.2$ to $+0.6$: a front, not a gradient (TN2 refuted). At resolution $0.02$ the last bin with a deviation
above $0.2\%$ is $[-0.26, -0.24)$, and the width-4 excess ($+0.95\%$ to $+1.19\%$ in $[-0.34, -0.26)$: fewer short
white runs, more long ones) ends at the same place (TF1, TF3 held; TF2 missed by one bin at the $0.1\%$ scatter).
So the single cell's pattern is the uniform measure's, at the level of triangle births, exactly from $x/t = -0.24 \pm 0.02$ rightward, and $0.246$ is Rule 30's leftward speed of information (§8.30, LB5; §8.66): *the uniform core
is the region that news of the seed has reached.* (I first wrote here that "between the band's settled edge near
$-0.5$ and $-0.25$ lies a zone that is neither band nor coin". That was wrong: I never measured the band's edge.
Measured afterwards, with predictions TE1, TE2 and CF pushed first (`edge` mode), the settled edge, below which every
diagonal already has its period 16, is at $x/t = -0.254$ at $t = 40{,}000$ and $-0.252$ at $t = 80{,}000$, on the
triangle front. So there are two regimes, not three: the triangle law fails on the settled band and holds exactly
off it, and the front is the band's inner edge, which §8.30 already showed moves at the leftward speed.) Bears on: nothing in PERIOD-TWO.md §7 directly; it is the sharpest statement in
this record of where the single cell's randomness lives, and it ties rows 3 and 13 of the constellation together.

### 8.69 The slow walls from the left: the left half's own conditions stop every seed of width 16 within one period (2026-10-06)

The slow walls' B question (§8.63 item 5.2) from the side nobody had enumerated. Next to a periodic column 0 the left
half evolves on its own with the wall as boundary; the right half reaches it only through two conditions on column
$-1$ that no right half can lift: at black times $x(-1, t) = \lnot\tau(t+1)$ (column 1 is invisible, Lemma 1), and
at white times the implied stream $\sigma(t) = \tau(t+1) \oplus x(-1, t)$ must be non-decreasing inside each white
stretch (the latch, PROOFS.md C.2). `leftside_horizon.c` takes every finite left seed of width $W$ (cell $-W$
black) and every phase of the wall and finds the first failure; $H_L(W)$, the best over seeds and phases, bounds
the lifetime of every two-sided configuration whose left half has width $W$. Predictions LH0 to LH3 were pushed at
09:45 (`5cee204`) and the run waited until nobody else was on the slow walls (claimed in CLOUD-LOCAL.md).

- *Controls.* Black wall: $H_L(W) = W \pm 1$ (the checkerboard seed holds until its left end's defect arrives at
  speed 1). White wall: the empty seed lives for ever.
- *The wall 0101.* $H_L(W) = 1, 7, 6, 5, 6, 9, 10, 12, 17, 18, 17, 30, 29, 28, 32, 31, 30, 31, 33, 38, 37$ for
  $W = 0$ to $20$: width plus a constant of about 17 from $W = 11$ on (LH1's bracket of 12 was too tight; the shape
  held), against the two-sided law's "total width plus 6 to 10" (§8.42). So next to 0101 the left half's own
  conditions already give the law; the right half tightens the constant.
- *The slow walls $0^a 1^a$, $a = 2, 4, 8, 16$.* Over every seed of width $\le 16$ and every phase the best lifetime
  is $29, 22, 22, 21$ steps. Two consecutive complete black stretches span at least $3a$ steps from any phase
  ($24$ for $a = 8$, $48$ for $a = 16$), so **no finite left seed of width at most 16 survives two consecutive black
  stretches next to $0^8 1^8$ or $0^{16} 1^{16}$**, whatever phase it starts at; for $a = 16$ it does not even
  survive one period (21 < 32). For $a = 2$ and $4$ seeds of width 16 outlive several periods (29 and 22 steps
  against periods 4 and 8), so the width of the seed against the stretch is what matters, as §8.63 said. (LH2 held.)
  *Correction, 11:35 the same day:* this paragraph first said "for $a = 8$ and 16 that is less than one period",
  which is false for $a = 8$ (22 steps against a period of 16: the best seed passes one black and one white stretch
  and dies six steps into the second black stretch); my misreading, caught on rereading, corrected everywhere.
- *Record seeds do not nest* (LH3 refuted).

What it says for the reframing (§8.63): the slow walls are, from the left, a *harder* family than 0101 at the
widths measured, and the theorem to try there (column $-1$ cannot read $0^{b-1}1$ through two consecutive black
stretches for $b$ large against the seed) has its finite evidence at $b = 8, 16$ against seeds of width 16, and is
false for $b = 2, 4$ against the same seeds, which is the "large against the seed" clause doing its work. Bears on: PERIOD-TWO.md
§7 question 2 (B next to the slow walls). Single-party. Reproduction: `python3 tests/probes/lexicon/rule30_leftside_horizon.py 20 100`
(seconds).

**Addendum (11:28 the same day): wider seeds pass.** Widths 17 to 24 (`wide`; LW1 to LW3 and CF pushed in `13a7b23`
first; all three blind predictions refuted, the control held). Next to $0^8 1^8$: $H_L = 24, 25, 26, 29, 31, 30, 34, 36$ for $W = 17$ to $24$: a seed of width 20 passes two consecutive black stretches and one of width 24 lives two full
periods and four steps more. Next to $0^{16} 1^{16}$: $21, 24, 26, 26, 26, 29, 30, 32$: width 24 reaches exactly one
period and dies at the second black stretch. So "the wall sets the horizon" (LW3) was wrong; the seed's width
against the stretch is the whole hypothesis: $W = 2b$ fails and $W = 2.5\,b$ passes at $b = 8$, $W = 1.5\,b$ fails at
$b = 16$. The theorem to try is therefore: *next to $0^a 1^b$, no left seed of width $W < 2b$ (or thereabouts) can
hold condition (i) through two consecutive black stretches*; the checkerboard triangle of depth $b - 1$ must be
rebuilt across the white stretch from what the seed carries, and width about $2b$ is what it takes. Next to 0101
the law continues ($H_L(24) = 42$). Single-party.

**Second addendum (11:37): the hypothesis is the period, not $2b$.** GPT (G003) asked that the $2b$ threshold be kept
tentative across white-stretch lengths; the run `white` (LA1 to LA3 and CF pushed in `03aec91` first) fixes $b = 8$
and varies $a = 4, 8, 16, 32$: the least width whose best seed survives two consecutive complete black stretches is
$P = 13, 17, 23$ and none to width 24 (for $a = 32$, which needs 48 steps). So $P(a) \approx a + b + 1$: the passing
width is about the wall's **period**, and the earlier "$W < 2b$" was the special case $a = b$. GPT's caution was
right and the hypothesis of the theorem to try is now: *next to $0^a 1^b$, no left seed narrower than about the
period $a + b$ holds the forced $0^{b-1}1$ through two consecutive black stretches.* Below the passing width the
horizon barely depends on $a$ (the seed dies in the second black stretch at about the same depth whatever the
white stretch was). A fourth run with $b = 4$ and $16$ (LB1, CF registered) tests the period reading from the other
side. Single-party.

**Third addendum (11:38): the period, to within two cells, from both sides.** The run `period` (LB1 and CF pushed in
`04ada9b` first) with $b = 4$ and $16$: $P(4,4) = 6$, $P(8,4) = 10$, $P(4,16) = 20$, $P(8,16) \ge 25$. Against the
period $a + b$ over all eight walls measured today: $6/8$, $10/12$, $13/12$, $17/16$, $23/24$, $20/20$, $\ge 25/24$,
$\ge 25/32$. **The least width of a left seed that survives two consecutive black stretches next to $0^a 1^b$ is
the wall's period to within two cells**, for $4 \le a + b \le 24$. (LB1's two tightest brackets were off by one
cell; kept.) The theorem to try is now stated with its hypothesis measured: next to $0^a 1^b$ a left seed narrower
than $a + b - 2$ cannot hold the forced $0^{b-1}1$ through two consecutive black stretches. Why the period and not
the black stretch alone: the seed must carry, across the white stretch, both the checkerboard the next black
stretch forces and the monotone latch word the white stretch demands, and the sum of their lengths is the period.
That sentence is a reading, offered to GPT as the reasoning item; single-party.

**Addendum to §8.67 (the same day): rings to $n = 29$.** The census was extended to $n = 25$ to 29 (`deep` mode;
predictions RD0 to RD3 and CF pushed first; the OEIS b-files of A334497 and A334496 read before the run as controls,
both reproduced). The prime ring $n = 29$ has 14 cycles, of 14 distinct lengths (the longest 1,466,066), and all 14
are gliders, as the pigeonhole of PROOFS.md C.6 requires when the lengths are distinct: the pattern seen at 13, 17,
19 and 23 continues at 29. Cycle counts 16, 33, 40, 60, 14 for $n = 25$ to 29. My prediction that some ring in 25 to
28 would again have a transient longer than its longest cycle failed: 21 and 22 stay the only such rings found. The
first attempt at $n = 29$ thrashed this 16 GB machine and was stopped; the engine now needs 8 bytes per state.

# Prize problems a GPU might reach

*Written 2026-10-04 by Cloud at the owner's request: "identify the open mathematics problems with outstanding cash
prizes that may be discoverable inside GPU shader compute". Status checked the same day against the sources linked
in §1, because this field moved in 2026. The notation comes from [LEXICON.md](LEXICON.md). The first experiment's
script, [tests/probes/lexicon/rule30_periodic.py](tests/probes/lexicon/rule30_periodic.py), states its predictions
in its header, written before it ran.*

## The honest summary

No open prize problem is one computation away. The one where heavy computation was the leading line of attack,
Navier–Stokes, was claimed on 2026-09-08, for the case with a smooth external force, and Clay is evaluating the
claim. For the rest, a computer can win in only two ways:

- **Find a counterexample.** This is a finite computation, and it would be decisive (Beal, Collatz, Riemann). For
  each of these, the best heuristics say no counterexample lies within any reachable search.
- **Check the finitely many cases that a theorem has reduced the problem to.** That needs the theorem that does the
  reducing: the idea, which no amount of hardware supplies.

The problem where this project's tools fit best is **Rule 30 Problem 1** ($10,000).
- Its arithmetic is exact bits, so there is no rounding to argue about.
- Its evolution is literally a shader.
- Its frontier moved one step on 2026-09-08, to exactly the case this document's first experiment examines.

That experiment ran today. Its controls reproduce the published theorem exactly. It found no finite configuration
with a periodic column for periods 2 to 6, over every right half up to 18 cells (27,262,976 cases, §5 and §6). That is
evidence, not a proof, and a proof is what the prize pays for.

---

## 1. The prizes, as of 2026-10-04

| Problem | Prize | Status | What wins it | Sources |
|---|---|---|---|---|
| Navier–Stokes existence and smoothness | $1M (Clay) | **"Active"**. OpenAI announced finite-time blowup with a smooth external force on 2026-09-08 (Clay's alternatives C and D, with a Lean formalisation). Clay said on 2026-09-11 that the problem "has apparently been settled", with evaluation to follow its rules. A priority dispute has been raised. | Either direction counts (rules §5b) | [Clay](https://www.claymath.org/millennium-problems/), [Wikipedia](https://en.wikipedia.org/wiki/Millennium_Prize_Problems) |
| Riemann hypothesis | $1M (Clay) | Unsolved. Rigorously verified up to height $3 \cdot 10^{12}$ by interval arithmetic (Platt and Trudgian, 2021) | A proof; or a counterexample that "effectively resolves the Problem" (rules §5c) | [Platt–Trudgian](https://arxiv.org/abs/2004.09765), [Clay rules](https://www.claymath.org/wp-content/uploads/2022/03/millennium_prize_rules_0.pdf) |
| P vs NP | $1M (Clay) | Unsolved | Either direction | Clay |
| Yang–Mills existence and mass gap | $1M (Clay) | Unsolved | A proof | Clay |
| Hodge conjecture | $1M (Clay) | Unsolved | A proof, or a resolving counterexample | Clay |
| Birch and Swinnerton-Dyer | $1M (Clay) | Unsolved | A proof, or a resolving counterexample | Clay |
| Beal conjecture | $1M (held by the AMS) | Unclaimed | A proof, or a counterexample, published in a respected refereed journal and approved by an AMS committee | [Andrew Beal](https://www.andrewbeal.com/beal-conjecture), [UNT](https://sites.itservices.cas.unt.edu/~mauldin/beal.html) |
| Collatz conjecture | ¥120M (Bakuage, 2021) | Open. Verified by computer for every start below $2^{71}$ | A proof or a disproof, under the company's rules | [Bakuage](https://en.antaranews.com/news/178694/bakuage-offers-prize-of-120-million-jpy-to-whoever-solves-collatz-conjecture-math-problem-unsolved-for-84-years), [Wikipedia](https://en.wikipedia.org/wiki/Collatz_conjecture) |
| Rule 30 Problems 1, 2, 3 | $10,000 each (Wolfram) | All open. Partial result 2026-09-08: no column of a nonzero finite configuration is eventually constant (Condrey) | "A full proof ... to the satisfaction of the Prize Committee" | [rule30prize.org](https://rule30prize.org/), [arXiv:2609.09431](https://arxiv.org/abs/2609.09431) |
| Erdős problems | from tens of dollars to a few thousand | 586 of 1,220 solved on erdosproblems.com (2026-09-11), many by AI systems since 2025 | Per problem | [Quanta, 2026-08-03](https://www.quantamagazine.org/why-the-legendary-erdos-problems-are-falling-to-ai-20260803/), [erdosproblems wiki](https://github.com/teorth/erdosproblems/wiki/Notable-cases-of-AI-contributions-to-Erd%C5%91s-problems) |

The OpenAI claim is after this assistant's training data. It is reported here as the sources state it, not as a
fact checked by reading the proof.

---

## 2. Two ways a computer can win a prize

**A counterexample** is a finite object that can be checked: three numbers with $A^x + B^y = C^z$, a Collatz cycle, a
zeta zero off the critical line. Finding one is pure search, the kind of work GPUs do best. The question is whether
any lies within reach, and the evidence is heuristic:

- **Beal.** Many exponent patterns are already proved to have no primitive solution by modular methods, for example
  $x^n + y^n = z^2$ and $z^3$ (Darmon and Merel, 1997). The conjectured finiteness of all such solutions (the
  Fermat–Catalan conjecture) leaves very little room.
- **Collatz.** A divergent orbit can never be shown by a finite computation. A cycle would have to be astronomically
  long, and every start below $2^{71}$ is already checked. Tao (2019) proved that almost all orbits attain almost
  bounded values.
- **Riemann.** Every zero up to height $3 \cdot 10^{12}$ is on the line. The statistics of the zeros match random
  matrix theory with no hint of a defect.

None of these is impossible. Each is a lottery ticket.

**A reduction plus a finite check** is how the famous computer proofs worked:
- the four-colour theorem (Appel and Haken, 1976);
- the Kepler conjecture (Hales; formally verified by Flyspeck, 2014);
- the Busy Beaver value $BB(5)$ (2024, checked in Coq);
- the rigorous zero counts behind the Riemann record.

In each case a human idea turned an infinite question into finitely many cases, and the computer checked them.

---

## 3. Ranked for this project

What this project is good at:
- exact GPU programs;
- measurement with controls and counterfactuals;
- determinism across devices (MOLTENVK-NONDETERMINISM-INVESTIGATED.md);
- writing code as mathematics (LEXICON.md).

| Rank | Problem | Prize | Path | Fit | Odds, in words |
|---|---|---|---|---|---|
| 1 | Rule 30 Problem 1 (no eventual period) | $10k | Prove "no finite configuration has an eventually $p$-periodic column", period by period, computing the structure first and then proving it, as Condrey did for $p = 1$. A uniform argument over all $p$ would win. | **Best.** Exact bits; a cellular automaton is a shader; left-permutivity gives an exact inverse construction | Each period is a realistic, publishable target. The uniform argument is the open idea. |
| 2 | Beal | $1M | A GPU modular sieve beyond the published search bounds | Good: exact integer arithmetic, embarrassingly parallel | Lottery. The public record of searched bounds is the sure output. |
| 3 | Collatz | ¥120M | Cycle search, or extending the verified bound past $2^{71}$ | Good: integer, parallel, and already done on GPUs by others | Lottery |
| 4 | Riemann | $1M | Rigorous zero verification beyond $3 \cdot 10^{12}$ | Needs rigorous floating point on the GPU (§4, job G1) | A counterexample is not expected. A new record is a publishable result with no prize. |
| — | Navier–Stokes | $1M | — | — | Claimed, and under evaluation |
| — | P vs NP, Yang–Mills, Hodge, BSD | $1M each | No computational path is known | — | — |
| — | Rule 30 Problems 2 and 3 | $10k each | Problem 2 is a statement about averages, Problem 3 about complexity | Computation gives evidence only | Proof-type problems |

---

## 4. The magician's trick: how a computer takes part in a proof

The owner asked for "the magician's tricks that make maths work". Computer-assisted proofs rest on three, and each
has a word in LEXICON.md.

1. **Exactness.** Integers and bits are exact on a GPU. Rule 30 is a polynomial over $\mathbb F_2$ (LEXICON.md §3.5),
   so a Rule 30 computation either is correct or has a bug. The defence against bugs is the one this project already
   uses: a known-answer control (here, OEIS A051023 and Condrey's theorem), a counterfactual that must fail, two
   independent implementations that must agree, and, at the end, a proof assistant (Lean or Coq).
2. **Enclosure.** Floats are not exact, but the rounding can be bounded or undone. TwoSum recovers the error of an
   addition exactly (LEXICON.md §3.7, check C7). Interval arithmetic carries a guaranteed lower and upper bound
   through every step. That is how the Riemann record was proved. On a GPU the risk is the compiler: a "fast-math"
   rewrite silently destroys TwoSum (C7's counterfactual). So before any float result can count, each GPU must be
   measured (job G1, §6).
3. **Reduction.** A theorem turns "for every $p$" or "for every configuration" into finitely many cases. The lift
   (LEXICON.md §3.6) is the reduction's natural language. "Is this column eventually periodic?" becomes "does this
   operator have an eigenvalue on the unit circle?", a question about the program's loops. Finding the reduction is
   the idea, and it is the part nobody can schedule.

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

---

## 6. The rungs from here

Each rung is a result on its own, whether or not the next one succeeds.

| Rung | What | Who | Status |
|---|---|---|---|
| 0 | The lexicon, machine-checked (LEXICON.md, `lexicon_check.py`) | Cloud, CPU | done 2026-10-04 |
| 1 | Rule 30, periods 2 to 6, exhaustive over small right halves, with the published control | Cloud, CPU | done: right support 14 at depth 192 (1,703,936 cases, 4m38s on one core), then right support 18 at depth 256 (27,262,976 cases, 4 cores); the control holds to $w = 8$ (256 maximisers); no eventually-zero left half anywhere |
| 2 | **The $p = 2$ structure.** The 7-periodic tails are explained (§5: 7-ring orbits). Next: find the forced left half's form for both period-2 traces, as Condrey did for constant traces; whether every forced left half eventually settles into some ring orbit was asked first and answered no: at depth 768, 1,999 of 2,048 period-2 right halves up to 10 cells show no period up to 128 over their last 256 cells, and the other 49 have periods 7, 14 or 28 (`rule30_rings.py`). So the argument must handle aperiodic left halves, and prove from their form that they are never eventually zero. Formalise in Lean. | Cloud | next |
| 3 | Periods $3$ to $6$ the same way, then look for the pattern across $p$: the uniform argument, which is the prize | Cloud | open |
| G1 | Does an error-free transformation (TwoSum, FMA-based TwoProd) survive each GPU's compiler? The prerequisite for any float-based proof on the GPU. Prediction to be written with the job. | Local, Arc and M5, minutes | to be written |
| 4 | Beal: a GPU modular sieve beyond the published bounds; publish the bounds | Cloud writes, Local runs | optional |

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

---

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

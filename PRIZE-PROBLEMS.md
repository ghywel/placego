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

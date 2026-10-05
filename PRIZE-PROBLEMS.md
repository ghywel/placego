# Prize problems a GPU might reach

*Written 2026-10-04 by Cloud at the owner's request: "identify the open mathematics problems with outstanding cash
prizes that may be discoverable inside GPU shader compute". Status checked the same day against the sources linked
in §1, because this field moved in 2026. The notation comes from [LEXICON.md](LEXICON.md). The first experiment's
script, [tests/probes/lexicon/rule30_periodic.py](tests/probes/lexicon/rule30_periodic.py), states its predictions
in its header, written before it ran. On 2026-10-05, at the owner's request, the Rule 30 work (sections 5, 7 and 8,
and the Rule 30 rungs of section 6) moved to [RULE30-PRIZE.md](RULE30-PRIZE.md), with its section numbers
unchanged; this document keeps the prizes as a whole.*

## The honest summary

**Update, 2026-10-05, evening.** §7 records what the Rule 30 work carries to the other prizes. The strongest
transfer is Collatz: the same counting structure, measured to 30 bits, plus the arithmetic that Rule 30 lacks (§7.1
to §7.3).

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
- Its frontier moved one step on 2026-09-08, to exactly the case this project's first experiment examines.

That experiment ran on 2026-10-04. Its controls reproduce the published theorem exactly. It found no finite
configuration with a periodic column for periods 2 to 6, over every right half up to 18 cells (27,262,976 cases,
[RULE30-PRIZE.md](RULE30-PRIZE.md) §5 and §6). That is evidence, not a proof, and a proof is what the prize pays for.

**The Rule 30 work has its own document.** Everything done on Rule 30 since then (left-side rigidity, the right side
as a complement, the wheel, the records, the wall form, and where period 2 stands) is in
[RULE30-PRIZE.md](RULE30-PRIZE.md), with its own honest summary. [PERIOD-TWO.md](PERIOD-TWO.md) is the standalone
handover of the period-2 work.

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

*Update, 2026-10-05 (from the sources, not from reading the proof).* The Navier–Stokes claim is a construction: a
smooth external force and initial data with finite-time blowup, found by a run of about 10,000 agents over 88 hours
and formalised in Lean. OpenAI says it will not claim the prize. Clay keeps the problem "active" until peer review
([Wikipedia, Navier–Stokes priority controversy][ns-pc]). OpenAI has made no claim on the Riemann hypothesis. It is
reported to be aiming the same system at Riemann and P vs NP. Separately, an Anthropic model raised a proven lower
bound on the share of zeta zeros on the critical line, reported at 67%. It was checked by two mathematicians and
formalised in Lean, and it is not a proof of the hypothesis ([TechCrunch, 2026-08-11][tc-rh]; the figure from
[Live Science][ls-rh]).

[ns-pc]: https://en.wikipedia.org/wiki/Navier%E2%80%93Stokes_priority_controversy
[tc-rh]: https://techcrunch.com/2026/08/11/an-unreleased-anthropic-model-made-progress-on-one-of-maths-biggest-unsolved-problems/
[ls-rh]: https://www.livescience.com/technology/artificial-intelligence/this-is-what-happened-with-claude-and-me-ais-failed-attempt-to-crack-the-riemann-hypothesis-led-mathematician-to-a-breakthrough

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


## 5. The Rule 30 work (moved)

Sections 5, 7 and 8 of this document, the Rule 30 work, moved on 2026-10-05 to [RULE30-PRIZE.md](RULE30-PRIZE.md),
with their numbers unchanged. A reference to "PRIZE-PROBLEMS.md §5", "§7" or "§8.x" written before then means that
section of RULE30-PRIZE.md. So do the Rule 30 rungs of §6 (rungs 1 to 3), which moved with them.

---

## 6. The rungs from here

Each rung is a result on its own, whether or not the next one succeeds.

| Rung | What | Who | Status |
|---|---|---|---|
| 0 | The lexicon, machine-checked (LEXICON.md, `lexicon_check.py`) | Cloud, CPU | done 2026-10-04 |
| G1 | Does an error-free transformation (TwoSum, FMA-based TwoProd) survive each GPU's compiler? The prerequisite for any float-based proof on the GPU. Prediction to be written with the job. | Local, Arc and M5, minutes | to be written |
| 4 | Beal: a GPU modular sieve beyond the published bounds; publish the bounds | Cloud writes, Local runs | optional |
| 1 to 3 | Rule 30: the search, the period-2 structure, then periods 3 to 6 | Cloud, Local | in [RULE30-PRIZE.md](RULE30-PRIZE.md) §6 |

The GPU is not needed for rungs 1 to 3 at these sizes. A CPU does them exactly in minutes. It enters if the search
must go much further, or for G1 and rung 4. The project's real advantage is not the hardware. It is the method: a
prediction before every run, a known answer beside every new one, and a counterfactual that must fail.

---

## 7. What the Rule 30 work carries to the other prizes (2026-10-05)

*The owner's question, after a day on Rule 30 Problem 1, period 2: "We don't have a proof but we have lots of clues,
and a huge amount of evidence. Does anything we have learnt here translate over to any one of the other open cash
prize math problems, worthy of study by future fresh eyes?"*

**Where the Rule 30 work ended up** (RULE30-PRIZE.md, the evening update; PERIOD-TWO.md). Every restatement of
period 2 converged on one missing statement: keeping the wall's conditions costs real information. The work took
it to a precise and measured form. The number of configurations on $w$ cells whose centre follows 0101 for $T$ steps
falls by one bit per condition. The bits of the seed's left part pay exactly, which is proved. The right part pays
1.002 bits per condition on average, with a debt that does not grow with width, measured to total widths beyond
100. A count of finite objects that falls below one is zero, so a proof of that bound would close period 2. What
blocks it is the same thing that blocks every relative surveyed: the theorems available are about sets of cases,
and the prize is about every single case.

**Four lessons that are not about Rule 30:**
1. **The decoupling skeleton.** A free side in bijection with the seed, a constrained side of low entropy, and
   agreement for ever. Mahler's 3/2 problem, Collatz, Erdős's ternary digits of $2^n$ and the busy beaver cryptid
   Antihydra all have it. In each, the solved cases are those where the constrained side is eventually periodic,
   and the open case is positive entropy.
2. **Sets against single cases.** Probabilistic and information-theoretic theorems (Tao's "almost all" for
   Collatz; zero-density estimates for the zeta function; data-rate theorems in control) prove statements about
   sets. Single-case theorems come from finiteness or from exact counting of finite objects.
3. **Turn a maximum into a count.** A record ("the longest run is about $w$") cannot be proved by sampling. A count
   ("at most $2^{w - \alpha T}$ seeds survive $T$ conditions") can be, and when the objects are finite a count
   below one is a proof. Split the count by where the free bits come from: the part that pays exactly
   (permutivity, a bijection) is provable at once, and what remains is a precise statement about the rest.
4. **The method.** Predictions committed before runs, a control with a known answer beside every new number, and a
   counterfactual that must fail. Over a day it caught a dozen wrong guesses of mine, each recorded.

**The prizes, by how much carries over:**

- **Collatz (¥120M): strong.** The same skeleton. Terras's theorem (the first $k$ parity steps of $n$ are a
  bijection with $n \bmod 2^k$) is the left part's exact payment. Past the free bits the question is open, as on
  Rule 30's right part. The counting form: if fewer than $2^{w - \alpha T + c}$ numbers of $w$ bits stay above
  their start for $T$ steps, every stopping time is finite and the conjecture follows. Tested in §7.1.
- **Rule 30 Problems 2 and 3 ($10k each): strong for tools, nothing yet for a proof.** The same system and every
  instrument: the wall form, the forced left half, the channel bound, the exact counts. Problem 2 asks for the
  centre column's density, and the counts already measure the pattern statistics of forced left halves.
- **Erdős problems (tens to thousands of dollars): moderate, problem by problem.** Many concern finite structures,
  where an exact count can reach zero. The method suits the kind that fell to AI-assisted search since 2025.
- **Riemann ($1M): weak.** Cramér's model is our coin model, and zero-density theorems are set theorems. The gap is
  the same, and nothing here crosses it.
- **Navier–Stokes ($1M): a lesson, not a route.** A construction with a freely designed force is the analogue of
  refuting LR, not B (RULE30-PRIZE.md §8.47).
- **P vs NP ($1M): a lesson, not a route.** Gates against truth (RULE30-PRIZE.md §8.50): finite checks against
  for-ever statements, with certificates as the bridge.
- **Beal ($1M): weak.** Its objects are finite, so a count could in principle reach zero, but its partial results
  come from modular methods.

### 7.1 The counting form, carried to Collatz

`tests/probes/prizes/collatz_count.py` (with `collatz.c`; predictions written before the run) counts every number
of 16 to 30 bits. $S_w(T)$ is the number of $w$-bit numbers whose orbit under $T(n) = n/2$ or $(3n+1)/2$ stays at
or above $n$ for $T$ steps. The coin is Terras's random walk of parity vectors: $P(T) = V(T)/2^T$, with $V(T)$ the
number of parity vectors whose coefficient $3^{a_t}/2^t$ stays above 1.
- **The free bits pay exactly** (CZ0, the control). For $T < w$ the coefficient count is $2^{w-1-T} V(T)$, by
  Terras's bijection. This is the Collatz form of RULE30-PRIZE.md §8.51's lemma.
- **Past the free bits, the high bits pay the coin's rate** (CZ3 held). At $w = 30$, $\log_2 S_w(T)$ falls by 0.0637
  bits per step from $T = 30$ to 285, against 0.0640 for the coin. That is the counterpart of Rule 30's 1.002 bits
  per condition.
- **The excess over the coin does not grow** (CZ4 held): at most 3.7 bits, at every width from 16 to 30, and
  1.8 and 2.7 at widths 31 and 32 (CZ6, predicted first). At 32 bits the slope past the free bits is $-0.0610$
  against the coin's $-0.0618$ (CZ5).
- **Stopping time equals Terras's coefficient stopping time** for every number of 20 to 30 bits (CZ1 held).
- **The horizon** grows by about 21 steps per bit (CZ2 refuted: I said 8 to 20).

**What it means.** Collatz behaves in the count exactly as Rule 30 does. The free part pays exactly, the open part
pays the coin's rate, and the excess stays bounded. So the Rule 30 statement has a Collatz twin: *the number of
$w$-bit numbers whose stopping time exceeds $T$ is at most $2^{c} \cdot 2^{w-1} P(T)$ for every $T$.* Since $P(T)$
decays exponentially, the count then falls below one at $T \approx (w + c)/0.064$, so every stopping time is
finite, and the conjecture follows by induction. Terras's theorem proves it with $c = 0$ for $T < w$. Beyond $w$ it
is open, and measured here with $c \le 3.7$ to $w = 30$. The agreement with the coin is long known in spirit (Lagarias
and Weiss's stochastic models, 1992). What carries over from Rule 30 is the framing: an exact count of finite
objects, split into the part that pays exactly and the part that pays on average. In both problems the second part
is the whole difficulty, so a method that bounds it in one may transfer to the other. That is the most concrete
cross-prize lead this work has produced.

### 7.2 The avenue Collatz has and Rule 30 lacks: the state after the free bits is an explicit integer

The owner: "As a different problem it should yield an avenue of attack that wasn't possible on the Rule 30 side." It
does: arithmetic. For $n = 2^{w-1} + r$, Terras's affine formula gives, after the $w - 1$ free steps,
$T^{w-1}(n) = 3^a + T^{w-1}(r)$, with $a$ the number of odd steps. This $y$ is an explicit integer. Its low $j$ bits
fix the next $j$ parities, by Terras again. So "past the free bits the count follows the coin" (§7.1) is exactly
the statement that $y \bmod 2^j$ is close to uniform over the numbers still above their start. That is an
equidistribution question about explicit integers, which exponential sums can attack. Tao (2019) proved "almost
all orbits attain almost bounded values" from the 3-adic analogue, the near-uniformity of the Syracuse offsets
modulo $3^n$. Rule 30's right part has no formula of this kind: its bits enter through OR gates.

`tests/probes/prizes/collatz_blocks.py` (with `collatz_blocks.c`; predictions written before the run) measured it
at $w = 26$, on 573,162 survivors among $2^{25}$ numbers:
- **The affine formula holds for every $n$** (CB0, the control), and the counterfactual $y \bmod 3$ is far from
  uniform (CB4), so the instrument sees arithmetic where it exists.
- **Uniform at the level of sampling noise** in total variation, at every $j$ to 12 (CB2 held).
- **But not perfectly** (post hoc). The largest odd Fourier coefficients at $j$ = 12 and 13 are about 0.012:
  small, yet far beyond noise. There is fine 2-adic structure in the survivors' state. It is smaller at $w = 26$
  than at $w = 24$.

So the Collatz twin of the bounded-debt statement reduces, block by block, to bounding exponential sums
$\sum_v e(h\,y_v / 2^j)$ over the parity vectors that stay up. That is a concrete analytic target of the kind
Tao's method addresses. Whether the structure fades as $w$ grows is the next measurement (§7.3).

### 7.3 The structure fades with width, and why the two problems are one shape

**Measured** (`collatz_blocks.py scaling`, predicted first). The largest odd Fourier coefficient of the survivors'
state $y \bmod 2^j$, at $w$ = 20, 22, 24, 26, 28:

| $j$ | $w = 20$ | 22 | 24 | 26 | 28 | slope of $\log_2 F$ per bit |
|---|---|---|---|---|---|---|
| 12 | 0.0528 | 0.0196 | 0.0166 | 0.0133 | 0.0036 | $-0.415$ |
| 14 | 0.0521 | 0.0361 | 0.0378 | 0.0074 | 0.0071 | $-0.401$ |

- **The structure fades** (CS1 held), nearly as fast as sampling noise, which falls by 0.5 per bit.
- **At $w = 28$ it can no longer be seen** at $j = 12$ (CS2 refuted: 1.67 times the noise baseline).
- So the state after the free bits equidistributes modulo $2^j$ as the width grows. That is the asymptotic shape a
  proof by exponential sums needs: errors that vanish as $w \to \infty$ at each fixed scale.

**Why the two problems are one shape.** Bernstein and Lagarias's conjugacy $Q$ sends $n$ to its parity sequence,
read as a 2-adic integer (PRIOR-ART, the wide survey). It is triangular: bit $k$ of $Q(n)$ is bit $k$ of $n$ XOR a
function of the lower bits. In the language of this project it is permutive in its newest input, as Rule 30 is in
its left neighbour. A finite $n$ fixes every input bit above the top one. Then:
- **Collatz:** do the output bits beyond the free part, which are functions of the free bits alone, behave like
  coins?
- **Rule 30, period 2:** the forced left half is the output of a triangular bijection from the seed, and a finite
  seed fixes every input cell beyond its edge. The question is the same.

Both are about a triangular bijection evaluated on inputs of finite support. The difference is the functions
behind the bits. In Collatz they are arithmetic, carries of $3x + 1$ with the multiplicative structure of $3^a$,
so they can be written as exponential sums and attacked analytically. In Rule 30 they are Boolean circuits of XOR
and OR, with no arithmetic to use. That is the avenue the owner asked for: the same question, with tools on one
side that the other lacks. A method that proves the Collatz form might suggest what a Rule 30 proof would need: a
substitute for that arithmetic, as §8.45 already concluded for Mahler's problem.

### 7.4 The state after the free bits is a remainder modulo a power of 3 (2026-10-05)

*Local's addition (`tests/probes/prizes/collatz_residue.py`, predictions written before the run).*

§7.2 found that after the free bits the Collatz state is an explicit integer $y$, and asked for its distribution
modulo powers of 2. That integer has an exact description.

**Lemma.** Let $0 \le r < 2^k$, and let $a$ be the number of odd steps among the first $k$ steps of $r$. Then

```math
0 \le T^k(r) < 3^a \qquad\text{and}\qquad T^k(2^k m + r) = 3^a m + T^k(r) \ \text{ for every integer } m .
```

So $T^k$ trades a remainder modulo $2^k$ for a remainder modulo $3^a$, and passes the quotient $m$ through unchanged.
By Terras's formula $T^k(r) = (3^a r + c_v)/2^k$, the new remainder is the least non-negative residue of
$2^{-k} c_v$ modulo $3^a$, where $c_v = \sum_j 3^{a-1-j}\,2^{i_j}$ over the positions $i_j$ of the odd steps.

*Proof.* The second identity is Terras's: adding $2^k$ to a number leaves its first $k$ parities alone and adds
$3^a$ to its $k$-th iterate. Take $m = -1$. The number $r - 2^k$ is negative, and $T$ maps negative integers to
negative integers. So $T^k(r) - 3^a < 0$. $\square$

**Checked** for every $r < 2^k$, $k \le 18$ (CR0, CR1). I had predicted the weaker "least residue, or that plus
$3^a$, the second case rare" (CR2). The second case never occurs, and the proof above came after the run. The
counterfactual modulus $3^{a+1}$ fails for two numbers in three, as it must. The lemma is elementary and is probably
in the Collatz literature; it was not looked up.

**What it adds to §7.2 and §7.3.**
- **The Collatz twin is a statement about one number written in two bases.** The next parities of an orbit are the
  low *binary* digits of a remainder modulo a *power of 3*. "Past the free bits the count follows the coin" (§7.1)
  says exactly that those binary digits are equidistributed over the parity vectors that stay up. That is the
  setting of Furstenberg's $\times 2 \times 3$ problem and of Erdős's question on the ternary digits of $2^n$
  (PRIOR-ART), where two bases are also known to be independent on average and unknown case by case.
- **It is Tao's object, not a counterpart of it.** Modulo $3^a$, the remainder $2^{-k} c_v$ is the offset whose
  distribution Tao (2019) studies as the Syracuse random variable, for random parity vectors. His fine-scale mixing
  estimate (his Proposition 1.14, cited from memory) gives errors that fall like a power of $a$. The binary digits
  of a least residue are read off by Fourier coefficients modulo $3^a$ whose total weight is about $a$, so such an
  estimate should give the *set* form of §7.1's statement: almost every number pays the coin's rate. The count
  below one needs errors smaller than $2^{-w}$, which is exponentially beyond a power of $a$. This is §7's lesson 2
  again, now with the exact place where it bites.
- **The same shape as Rule 30's left and right parts.** The quotient $m$ is the free side: it passes through a
  bijection, as the seed's left cells do (RULE30-PRIZE.md §8.51). The remainder is the finite-support side, and
  its new digits are functions of the old ones alone.
- **Jen's theorem with a clock has a Collatz form** (RULE30-PRIZE.md §8.54). A parity sequence that is $P$-periodic
  on a window pins the number 2-adically to a rational cycle point, so the window is at most about as long as the
  number has bits. The bit length is to Collatz what the distance to the left edge is to Rule 30.

### 7.5 The window principle: what the two problems share exactly, and what each lacks (2026-10-05)

*Local. The owner asked how the avenues that Collatz opens might apply to Rule 30, with both prizes given equal
attention. Cloud's closing remarks named two things: the bounded-debt statement, and the exponential sums that
Collatz's arithmetic offers. Probes: `tests/probes/prizes/collatz_window.py` and
`tests/probes/lexicon/rule30_window.py`, predictions committed before each run.*

**One statement, exact in both problems.** Look at the state through a window of $n$ digits. In both problems
that window and the next $n$ symbols of the trace determine each other. So:

> **A block of the trace can repeat only if it is no longer than the state is large.**

| | Collatz | Rule 30 |
|---|---|---|
| State | a rational $N/D$ with $D$ odd | a row with finitely many black cells on the left |
| Trace | its parity sequence | two adjacent columns |
| Window of $n$ digits | the residue modulo $2^n$ | the $n - 1$ cells to the left of the columns |
| Why window and trace match | Terras's bijection | Rule 30 read from right to left |
| Size of the state | $\log_2 \lvert N \rvert$ | the distance $L$ to the leftmost black cell |
| Size after one step | grows by at most $\log_2 \tfrac32 = 0.585$, or shrinks | grows by exactly 1 |
| The statement | blocks of length $n$ at times $i, j$ are equal exactly when $2^n$ divides $N_i - N_j$ (W1) | a block of length $n$ recurs at time $a'$ only if $n \le L + a'$ (Theorem A′) |

*Proof for Collatz (W1).* Terras's bijection holds on the rationals with odd denominator: the first $n$ parities
of $y$ determine $y$ modulo $2^n$, and conversely. The iterates $N_i/D$ and $N_j/D$ have the same next $n$
parities exactly when they are congruent modulo $2^n$, and $D$ is odd. $\square$ The Rule 30 proof is the same
sentence with rows for residues (RULE30-PRIZE.md §8.58).

**What follows on the Collatz side.**
- **W2, complexity is at least the sojourn.** Let the orbit of $x = N/D$ be infinite, and let $p(n)$ be the number
  of different blocks of length $n$ in its parity sequence. Iterates with $\lvert N_i \rvert < 2^{n-1}$ are different
  numbers closer than $2^n$, so by W1 their blocks differ. Hence $p(n)$ is at least the number of such iterates.
  An iterate grows by at most $3/2$ a step, so

```math
p(n) \;\ge\; \frac{n - 1 - \log_2(\lvert N \rvert + D)}{\log_2 (3/2)} \;\approx\; 1.71\,n .
```

- **W3, no rational has a Sturmian parity sequence.** A Sturmian sequence has $p(n) = n + 1$, which is below
  $1.71\,n$. This holds for every slope, the critical slope $\ln 2/\ln 3$ included, and every intercept. More
  generally, the 2-adic number with parity sequence $v$ is irrational whenever $v$ is aperiodic and
  $p(n) \le 1.7\,n$ for infinitely many $n$.
- **The slower an orbit diverges, the more complex its parity sequence must be.** An orbit that grows by $\sigma$
  bits a step needs $p(n) \ge n/\sigma$. One that grows more slowly than any exponential needs $p(n)$ to grow
  faster than any linear function.

**How new this is.** W1 is Terras's theorem, and W2 and W3 follow from it in three lines, so they may be folklore.
I did not find them stated. What I found:
- López and Stoll (Integers 9, 2009) compute the 2-adic number for Sturmian sequences of intercept 0, and by the
  account of a later reader they leave its irrationality open.
- Their preprint arXiv:2101.12747 (2021) claims more than W3: that a rational with a divergent orbit must have
  ones at density exactly $\ln 2/\ln 3$. Its proof shows that the *real* sum of Bernstein's series is irrational,
  and then (its equations 15 and 16) treats that real number and the *2-adic* sum of the same series as one
  number. A series of rationals can have different limits in the two metrics. As far as I can tell that step is
  not justified, so I do not rely on the claim.
- A public repository (`eoc-divergence` on GitHub) carries a draft on the irrationality of the critical Sturmian
  value, so the question is being worked on.
W3 is weaker than the 2021 claim and has a complete proof. A proper literature check by someone who knows this
field is owed.

**Checked** (`collatz_window.py`, two runs):

| Check or prediction | Result |
|---|---|
| CW0: Terras's bijection to $n = 12$ | **passed** |
| CW1: common future = 2-adic valuation of $N_i - N_j$ ($D$ = 1, 3, 5, 7; $\lvert N \rvert \le 300$) | **passed**: 4,910,527 pairs |
| CW2: blocks of length $n$ and residues modulo $2^n$ are equally many | **passed** |
| CF, then CF2: a wrong partner breaks the identity | first design **failed** (too weak); CF2 **passed** |
| CW3, then CW3b: the 2-adic digits for Sturmian sequences are balanced and aperiodic | CW3 **refuted by my error**; CW3b **held** |
| CW5: periodic parity sequences give periodic digits, periods 21 and 166 | **passed** |
| CW4: the least integer with the first $M$ parity symbols has more than $M - 24$ digits | **held** |

Two errors of mine, recorded. The first counterfactual compared $N_i + N_j$ with $N_i - N_j$, which share their
low powers of 2 for three pairs in four, so it could not fail. And three of my four "Sturmian" slopes (0.7, 0.8,
0.9) were rational, so those sequences were periodic. The probe then found what it should: digit periods 21 at
slope 4/5 (the cycle's denominator is $2^5 - 3^4 = -49$, and 2 has order 21 modulo 49) and 166 at slope 7/10. I
kept that as a control.

**Why Collatz gets more from the same principle.** The principle bounds repeats by size, so everything turns on
how fast size grows compared with the window. A Collatz iterate gains at most 0.585 bits a step and can lose
bits, so the first $1.71\,n$ iterates fit a window of $n$ bits, and all their blocks differ. A Rule 30
configuration gains exactly one cell a step for ever, so only the first $n - L$ rows fit a window of $n$ cells.
The same count gives Rule 30 only $p(n) \ge n - L$, which is Morse and Hedlund's bound again. That is why
RULE30-PRIZE.md's Theorem E, the Sturmian case, needed a second argument across three scales of the continued
fraction, where W3 needs none.

**What each problem has that the other lacks.** Count the contents of the window that one orbit ever shows; by
the principle that number is the trace's complexity $p(n)$.

| | Lower bound, proved for every single orbit | Upper bound, forced on a counterexample |
|---|---|---|
| Collatz, a divergent orbit | $1.71\,n$, and $n/\sigma$ for slow growth (W2) | none: only the long-run share of ones is forced, at 0.63 or more |
| Rule 30, a period-2 counterexample | $n - L$ (Theorem A′) | $2^{0.13\,n}$: the channel bound (RULE30-PRIZE.md §8.33) |

- **Rule 30 has the squeeze.** A counterexample must keep the $2n$ cells beside its centre column within
  $2^{0.13\,n}$ contents for ever. Collatz has nothing like it: divergence fixes only the long-run share of
  ones, which costs a parity sequence 5% of its entropy and puts no ceiling on $p(n)$.
- **Collatz has the sojourn.** Its states can be small, small states are few, and each has its own future.
  Rule 30's states are never small.
- **So the two gaps differ in kind.** Rule 30 period 2 would follow from *any* proof that the window beside the
  centre of a finite configuration shows more than $2^{0.13\,n}$ contents. Collatz has no ceiling to break, so
  no count of window contents can close it. In this form Rule 30 period 2 is the better posed of the two: it
  has a target.

**Cloud's closing remarks, answered.**
1. *"A proof on the Collatz side would show what a Rule 30 proof has to replace."* What Collatz's arithmetic
   supplies is a size that the trace controls. Rule 30's only size is the distance to its edge, which grows at
   the speed of light whatever the trace does. A Rule 30 proof has to replace the size by a count: a lower bound
   on how many contents the window shows. The edge gives $n - L$. The prize needs $2^{0.13\,n}$.
2. *The exponential sums.* §7.4 identified them: they are Tao's sums, read in base 2. They cannot close either
   problem, whatever is proved about them. An exponential sum estimates a count as a main term plus an error, and
   the error is never below the square root of the population. Truly random data would not do better. So this
   avenue can reach the bounded-debt statement only while many survivors remain. The last survivors, which are
   the whole of both prizes, are out of its reach in principle. It is still the right tool for the *density*
   form of bounded debt, which is unproved on both sides.
3. *What does reach a single case.* Only exact statements have so far: a bijection (the free bits, the seed's
   left part), the window principle (cycles and Jen's theorem, W3 and Theorem E), and finite checks. Tonight's
   additions on both sides are all of the second kind, and they stop at the same place: traces with long early
   repetitions are excluded, and traces that look random are not.

**Where the nonlinearity sits.** One more exact parallel, with no theorem attached yet. Both maps are affine once
one bit is known. Collatz is $x \mapsto 3x/2$ or $x/2$ plus a source of $1/2$ at the odd steps, and the trace
records exactly those steps, so knowing the trace makes the whole orbit affine (Terras's formula). Rule 30 is the
linear Rule 150 plus a source wherever two adjacent cells are black:
$x_{t+1}(i) = x_t(i-1) \oplus x_t(i) \oplus x_t(i+1) \oplus x_t(i)\,x_t(i+1)$. Its sources fill a field in space
and time, and the trace records only one column of it. Next to the 0101 wall the trace does make the first three
columns affine (RULE30-PRIZE.md §8.58), and no more.

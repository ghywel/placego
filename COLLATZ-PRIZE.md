# Collatz: the prize, and what the Rule 30 method gives it

*Split out of [PRIZE-PROBLEMS.md](PRIZE-PROBLEMS.md) §7 on 2026-10-06 at the owner's request ("I'd quite like to win the
money there as well"). Sections 1 to 5 are the former §7.1 to §7.5, unchanged in text; the honest summary, the board
in §6 and the table in §7 are new. The Rule 30 record is [RULE30-PRIZE.md](RULE30-PRIZE.md); the method and the
working rules are [WORKFLOW-SAVED-MEMORY.md](WORKFLOW-SAVED-MEMORY.md) and [WORKING-TOGETHER.md](WORKING-TOGETHER.md).*

## The honest summary

**No proof, and nothing to submit.** The prize is Bakuage's, ¥120M (2021), for a proof or a disproof of the Collatz
conjecture under the company's rules (PRIZE-PROBLEMS.md §1 has the link). The conjecture has been verified by
computer for every start below $2^{71}$; no counterexample lies within any reachable search, and a proof is what the
prize pays for.

**What this record holds** (all from 2026-10-05, with pre-registered probes in `tests/probes/prizes/`):
- *The counting form, measured* (§1): the number of $w$-bit starts whose orbit stays at or above its start for $T$
  steps follows Terras's coin to 0.5% past the free bits, to $w = 30$, with an excess below 3.7 bits. This is the
  Collatz twin of Rule 30's question 1: the left part (the first $w - 1$ parities, a bijection with $n \bmod 2^{w-1}$)
  pays exactly; what the rest pays is the open part.
- *The avenue Collatz has and Rule 30 lacks* (§2, §3): after the free bits the state is an explicit integer,
  $3^a + T^{w-1}(r)$, and the question becomes one about its binary digits; its Fourier structure fades with width.
- *The least-residue lemma* (§4): $T^k(2^k m + r) = 3^a m + T^k(r)$ with $0 \le T^k(r) < 3^a$: the state after the
  free bits is a remainder modulo a power of 3, Tao's object read in the other base. Known: Terras 1976, Lagarias
  1985; the bound is Kontorovich and Sinai's structure theorem in another form (PRIOR-ART.md).
- *The window principle* (§5): a block of the parity sequence can repeat only if it is no longer than the state is
  large (Terras's bijection). It gives W1 (equal futures are congruent presents), W2 (an infinite orbit's parity
  sequence has complexity at least $1.71\,n$) and W3 (no rational has a Sturmian parity sequence). **Not new**: W2 is
  Dubickas, Glasgow Math. J. 51 (2009), Theorem 5; W1 and W3 are in three unrefereed 2026 notes (§5, PRIOR-ART.md).
  What is ours is the pairing with Rule 30's Theorem A′ and the conclusion that exponential sums cannot reach a
  single case on either side.

**What the problem needs, in this record's terms.** A count. If fewer than $2^{w - \alpha T + c}$ numbers of $w$ bits
stay above their start for $T$ steps, every stopping time is finite and the conjecture follows (§1). The free bits
pay exactly; the open part is whether the remainder modulo $3^a$ keeps paying, which is a statement about one orbit's
binary digits, not about almost all of them (Tao 2019 is about almost all). Every theorem surveyed that bounds a
chaotic system's cost is about sets of cases; the prize is about every single case (RULE30-PRIZE.md §8.47).

**Where the two prizes meet.** Collatz is Rule 30's period 2 with arithmetic attached (§3): a bijection permutive in
its newest input, fed an input of finite support, and the question whether the output past the free part behaves
like coins. A proof on either side would show what a proof on the other has to replace.

## 1. The counting form, carried to Collatz

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

## 2. The avenue Collatz has and Rule 30 lacks: the state after the free bits is an explicit integer

The owner: "As a different problem it should yield an avenue of attack that wasn't possible on the Rule 30 side." It
does: arithmetic. For $n = 2^{w-1} + r$, Terras's affine formula gives, after the $w - 1$ free steps,
$T^{w-1}(n) = 3^a + T^{w-1}(r)$, with $a$ the number of odd steps. This $y$ is an explicit integer. Its low $j$ bits
fix the next $j$ parities, by Terras again. So "past the free bits the count follows the coin" (§1) is exactly
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
Tao's method addresses. Whether the structure fades as $w$ grows is the next measurement (§3).

## 3. The structure fades with width, and why the two problems are one shape

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

## 4. The state after the free bits is a remainder modulo a power of 3 (2026-10-05)

*Local's addition (`tests/probes/prizes/collatz_residue.py`, predictions written before the run).*

§2 found that after the free bits the Collatz state is an explicit integer $y$, and asked for its distribution
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

**What it adds to §2 and §3.**
- **The Collatz twin is a statement about one number written in two bases.** The next parities of an orbit are the
  low *binary* digits of a remainder modulo a *power of 3*. "Past the free bits the count follows the coin" (§1)
  says exactly that those binary digits are equidistributed over the parity vectors that stay up. That is the
  setting of Furstenberg's $\times 2 \times 3$ problem and of Erdős's question on the ternary digits of $2^n$
  (PRIOR-ART), where two bases are also known to be independent on average and unknown case by case.
- **It is Tao's object, not a counterpart of it.** Modulo $3^a$, the remainder $2^{-k} c_v$ is the offset whose
  distribution Tao (2019) studies as the Syracuse random variable, for random parity vectors. His fine-scale mixing
  estimate (his Proposition 1.14, cited from memory) gives errors that fall like a power of $a$. The binary digits
  of a least residue are read off by Fourier coefficients modulo $3^a$ whose total weight is about $a$, so such an
  estimate should give the *set* form of §1's statement: almost every number pays the coin's rate. The count
  below one needs errors smaller than $2^{-w}$, which is exponentially beyond a power of $a$. This is §7's lesson 2
  again, now with the exact place where it bites.
- **The same shape as Rule 30's left and right parts.** The quotient $m$ is the free side: it passes through a
  bijection, as the seed's left cells do (RULE30-PRIZE.md §8.51). The remainder is the finite-support side, and
  its new digits are functions of the old ones alone.
- **Jen's theorem with a clock has a Collatz form** (RULE30-PRIZE.md §8.54). A parity sequence that is $P$-periodic
  on a window pins the number 2-adically to a rational cycle point, so the window is at most about as long as the
  number has bits. The bit length is to Collatz what the distance to the left edge is to Rule 30.

## 5. The window principle: what the two problems share exactly, and what each lacks (2026-10-05)

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

**How new this is: not new.** W1 is Terras's theorem, and W2 and W3 follow from it in three lines. A literature
search on the night of 2026-10-05 (by a search agent of Local's; pages and abstracts read, no PDF opened) found:
- **W2 is Dubickas's, for integers.** A. Dubickas, "On integer sequences generated by linear maps", Glasgow Math. J.
  51 (2009) 243-252, read in full on 2026-10-06 (the open-access PDF). Theorem 3: for coprime $p > q > 1$ and
  $x_n = \lceil p x_{n-1}/q \rceil$, the sequence $w_n = q x_{n+1} - p x_n$ has $\liminf P(w, n)/n \ge \log q / \log(p/q)$.
  Corollary 4: for $x_n = \lceil 3x_{n-1}/2 \rceil$ the parity sequence has $P(X, n) > 1.70951129\,n$ for all large $n$.
  Theorem 5: for the 3x+1 map $U$ on *positive integers* with $x_n \to \infty$ (a divergent trajectory, which he
  calls a speculative result because none is known to exist), the parity sequence has $P(X, n) > 1.70951129\,n$
  for all large $n$. He conjectures $P(X, n) = 2^n$. So W2 for integer orbits is his Theorem 5 exactly, with the
  same constant; W2 for rationals with odd denominator (ours) is a small extension he does not state, by the same
  argument; and W3 for divergent integer orbits follows from his theorem at once, since a Sturmian sequence has
  $P = n + 1$.
- **His conjecture, measured** (`collatz_threehalves.py`, predictions TH0 to TH3 written first; two runs, the second
  after a slip in the control's start value). For the 3/2 map $x \mod 2^n$ fixes the next $n$ parities, so
  $P(X, n) = 2^n$ means the orbit of 1 visits every residue class modulo $2^n$. Over the first 4,000,000 terms it
  does so for every $n \le 18$; at $n = 20$ it has visited 1,025,602 of the 1,048,576 classes, a coverage of 0.97809
  against the 0.97796 that fair coins would give after as many draws; the share of ones is 0.49955. So the
  conjecture holds as far as four million terms can see, and the orbit's residues look like coins to four digits.
  That is the Collatz-side shape of Rule 30's cost side as a count (RULE30-PRIZE.md §8.58): the trace is as complex
  as it can be, and nobody can prove it on either side.
- **W1 and W3 appear in three 2026 notes, none refereed**: a GitHub note of 2026-07-22 (Lemma 1 is W1's one
  direction, Corollary 5 is W3 by this argument); a GitHub note of 2026-09-22 (every slope and intercept, by a
  2-adic Liouville argument); and a Zenodo record of 2026-10-02. For slopes below $\log_3 2$, W3 is also implied
  by Monks and Yazinski (2004), Theorem 2.7(b), by a secondary account.
- **The lemma of §4**: the identity $T^k(2^k m + r) = 3^a m + T^k(r)$ is Terras (1976) and Lagarias (1985,
  Theorem B), stated verbatim as Lemma 2.3 of arXiv:2602.10466; the bound $0 \le T^k(r) < 3^a$ is the second part
  of Kontorovich and Sinai's structure theorem (arXiv:0910.1944, Theorem 5.2) in another form.
- López and Stoll (Integers 9, 2009) compute the 2-adic number for Sturmian sequences of intercept 0; by
  Lagarias's annotated bibliography they only conjectured the full complexity of the image.
- Their preprint arXiv:2101.12747 (2021, one version, no journal) claims more than W3: that a rational with a
  divergent orbit must have ones at density exactly $\ln 2/\ln 3$. Its proof shows that the *real* sum of
  Bernstein's series is irrational and then (equations 15 and 16) treats that real number and the *2-adic* sum
  of the same series as one number. A series of rationals can have different limits in the two metrics. The same
  objection, with counterexamples, stands unanswered in a public issue (2026-09-30) of a repository that works on
  the question. I do not rely on the claim.
So W1 to W3 are recorded here as known results with proofs written out, credited to Dubickas (2009) for W2 and
to the 2026 notes for W1 and W3. What stays ours is the pairing with Rule 30 (Theorem A′) and the conclusion that
exponential sums cannot reach a single case on either side.

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
2. *The exponential sums.* §4 identified them: they are Tao's sums, read in base 2. They cannot close either
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


## 6. Leads and their status

**The status board** (started 2026-10-06 06:57; the time is from the shell). The tags are those of PERIOD-TWO.md §6: OPEN,
PART, RUNNING, DONE, CLOSED, BLOCKED, with the section that settles each. When a lead moves, its row changes in the
same commit as the result.

| Lead | Status | What has been done | What is left |
|---|---|---|---|
| The counting form (§1): fewer than $2^{w - \alpha T + c}$ survivors | **OPEN** | Measured to $w = 30$: the coin to 0.5%, excess below 3.7 bits. | The proof. The same gap as Rule 30's question 1. |
| The state after the free bits as an integer (§2, §4) | **DONE** as a lemma | The least-residue lemma, checked to $k = 18$; known (Terras, Lagarias, Kontorovich–Sinai). | Use it: a statement about the binary digits of a remainder modulo $3^a$, for one orbit. |
| The Fourier structure of the survivors' state (§3) | **DONE** as a measurement | The largest odd coefficient fades with width. | Nothing: it says exponential sums will not reach single cases. |
| Exponential sums as a route to single cases | **CLOSED** (§5) | Their error is at least the square root of the population. | Nothing. |
| W1 to W3, the window principle (§5) | **DONE**, known | Proved here; W2 for integers is Dubickas 2009, Theorem 5 (read in full 2026-10-06); W1 and W3 are in three 2026 notes; our rational extension is a trivial step he does not state. | Nothing. The credit is settled. |
| A statement beyond complexity $1.71\,n$ for one orbit | **OPEN** | Dubickas conjectures the maximum, $P(X, n) = 2^n$, for the 3/2 orbit of 1 (§5). | The Collatz twin of Rule 30's "cost side as a count" (RULE30-PRIZE.md §8.58): the same unproved shape on both sides. |
| Dubickas's conjecture $P(X, n) = 2^n$ for the 3/2 map, measured (§5) | **DONE** as a measurement | Every residue class modulo $2^n$ visited for $n \le 18$ over four million terms; 0.97809 of the classes at $n = 20$ against a coin's 0.97796 (`collatz_threehalves.py`). | Nothing a computer can add; a proof would be the 3/2 problem's. |
| The 2021 preprint's claim (density exactly $\ln 2 / \ln 3$) | **NOTED** | Its equations 15 and 16 take a real limit for a 2-adic one; the objection stands unanswered in public. | Not ours to repair. |

## 7. How to reproduce

| Script | What it measures | Time |
|---|---|---|
| `collatz_count.py` + `collatz.c` | the counting form, every number of 16 to 30 bits, against Terras's coin (CZ0 to CZ4) | minutes |
| `collatz_blocks.py` + `collatz_blocks.c` | the state after the free bits modulo $2^j$ and its Fourier structure against width (CB, CS) | minutes |
| `collatz_residue.py` | the least-residue lemma (CR0 to CR2, CF), to $k = 18$ | a minute |
| `collatz_window.py` | the window principle, W1 to W3 (CW0 to CW5, CF2), two runs recorded | a minute |
| `collatz_threehalves.py` | Dubickas's conjecture for the 3/2 map as residue coverage modulo $2^n$ (TH0 to TH3, CF), two runs recorded | five minutes |

All are in `tests/probes/prizes/`, each with its predictions written before its first run and its OUTCOME in its
header, failures included. After editing this file run `python3 tests/probes/mathcheck/check.py COLLATZ-PRIZE.md`.

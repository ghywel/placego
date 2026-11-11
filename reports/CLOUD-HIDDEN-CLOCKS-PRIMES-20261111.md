# What Rule 30 hides: the clocks, the cipher and the primes

Cloud, CL776 and CL777, 11 November 2026, in answer to the owner's question of that day. Nothing here is a prize
statement and nothing changes a status on the board. New hand statements are PROOF-SKETCH until another worker
reads them. A sub-agent sweep meant to accompany this stopped at a usage limit after two of its five record
searches; no lens or skeptic ran, and what it did return is a self-check.

**GPT review, GC2931.** The left-edge lemma is carried with scalar periods dividing the stated product. The review adds proposed exact second and third clocks, unbounded left-prefix periods at every prime, and explicit 2-adic cascade bounds. Statistical conclusions below have been narrowed to their tested scope. [Carrying read and strengthenings](GPT-HIDDEN-CLOCKS-REVIEW-20261111.md).

**The owner's question.** The kit collects provable statements and nobody has a bearing on the prize questions.
We know what a counterexample must look like; can it be proved impossible? "I eternally feel the pull of the
primes … hidden by some non obvious transformation. Perhaps a transformation that shifts even as time is run like
a cyclic cipher." The image: a two-factor code that changes every thirty seconds and still unlocks the account.
"What is rule 30 hiding."

**Outcome.**
1. The two-factor picture is exactly true, and already proved: at its right edge the single cell's pattern is a
   binary counter read through a fixed scrambler. The centre column reads wheel number t at time t. Controlling those phases across changing depths remains open.
2. There is a transformation under which every prime appears: reading Rule 30's polynomial over the integers.
   It is in the literature. What is new here is its left edge, where each odd prime p sees a clock whose period
   is the multiplicative order of 2 modulo p. The tested centre counts and selected joint tables are compatible with the stated uniformity and independence reference models.
3. On the time axis the centre column has now been tested against the three kinds of arithmetic a tick number
   has: its residues (every modulus to two million), its digits (bases 2, 3, 5, 7) and its factorisation (the
   primes, Liouville, Möbius, at last to 2^24). Results in §4 and §5.
4. Whether the counterexample can be proved impossible is where it was. §6 says why, in the record's and the
   kit's own words, and what the lift does and does not add.

## 1. Record searched

By me before proposing anything, and by the two searches that finished: INSTINCT.md 15 and 16 October (the
owner's primes hunch, refined to "some sweep we haven't seen, diagonal or irregularly diagonal, perhaps even the
sum of 2 primes masking it"); RULE30-PRIZE 8.114 to 8.116 (the direct reading killed at 2^22 with a drift handed
to JOB CS-01; the structural reading; the observer thesis); G301 and CL398 (a sweep must be fixed in advance);
PROOFS entries 33 and 34 (Propositions 20 and 21: the centre column as an autokey cipher); 8.15, 8.37, 8.70, 8.90,
8.110; DEEP-QUESTIONS DQ-030 ("the centre reads diagonal k = t, a moving target"); genealogy §3 (S2, S3), §15.1,
§25, §29; CONSTELLATION rows 2, 7, 11, 21; PERIOD-TWO §1 and §5; the kit catalogue `equivalents/CATALOG.md` at
c791556, §7 items 2, 4, 5, 6, 8, 9, 11, 13; `record_find` on some thirty terms (CL776). Outside: Nersissian,
*Diagonal Bases and Diagonal Periods of Elementary Cellular Automata*, arXiv 2609.25078 (abstract, §3 Remark 6,
§10.2, §12.1, §17 read today); Coven, Pivato and Yassawi 2007 as cited by the kit.

Not found anywhere: the left diagonals of the integer lift; the lift's centre column modulo odd primes as a
sequence; Artin's conjecture in any role; a direct power spectrum of the single-seed centre column; a kernel test
in a base other than 2; an outcome for CS-01; the owner's two-factor image.

## 2. What is known to be hidden

All of this is in the record or the kit. Nothing in this section is mine.

| What | Exact statement | Status and place |
|---|---|---|
| A cipher with nothing hidden | For a random start the centre column is an exact fair coin, independent of the right half. One fresh bit of the left half enters the centre at each tick by XOR. | Lean, kit `RandomConfigurations` (`measurePreserving_trace`, `indepFun_trace_rightHalf`); as an autokey cipher, PROOFS 33 and 34 |
| The single cell is the empty message | With a white left half there is nothing to transport. The centre column is the cipher's own output on the all-white message with the all-white key. | PROOFS 33 |
| A counter at the right edge | In the frame of the right edge the single cell's orbit closure is the binary odometer. The cells behind the edge evolve by the triangular bijection Φ(x) = x xor (2x or 4x), and the cell at depth j has period dividing 2^j. | Coven, Pivato and Yassawi 2007; Lean, kit `Odometer.isClosedEmbedding_seed`, `TFunction.orbit_two_pow_mod`; periods at most 2^⌈(2j−1)/3⌉ (G249) |
| Clocks at the left edge | Left diagonals are eventually periodic with power-of-two periods, after transients. | Jen 1986, Rowland; Lean, kit `Ld_periodic`; our Lemmas B1 to B3 |
| The moving target | The centre column reads row t of the diagonal array at time t: inside that row's first period on the right, inside the transient on the left. | Kit catalogue §7 item 9; DQ-030; genealogy §15.1: "No known clock reaches there" |
| One nonlinear gate | Rule 30 is rule 150 plus the product of the centre and right cells. Rules 90, 150 and 210 share every structural hypothesis and have eventually constant centres, so a proof must use that product. | Lean, kit `Rule30Realization.barrier`; sibling barriers in our carry reports |
| The carry | The correction that separates Rule 30 from a Gray step is a two-time AND, and under the coin measure the column carry is a hidden two-state chain with an exact entropy rate. | 8.90, the owner's question of 11 October, solved |

## 3. The two-factor picture, exactly

A two-factor code is code = f(secret, counter). The app and the server share the secret, the counter is the
time, and the same secret is used for ever.

At Rule 30's right edge:
- the counter is the tick number t, written in binary;
- the wheels are the right diagonals: the cell at depth j behind the edge is a fixed function of the low bits of
  t, with period 2, 2, 4, 8, 8, 16, 32, 32 at depths 1 to 8 (COMPUTED here; the record has them to depth 16);
- the scrambler is fixed once and for all by the rule.

So far it is the app. The difference is which wheel is read. The centre column is the cell at depth t at time t.
Each tick reads a new wheel, and from the third wheel on, at every depth computed, that wheel's period is longer
than t. These observations concern the measured wheels. Increasing wheel periods alone do not force an aperiodic sampled diagonal. The missing condition must relate successive wheels at the phases the centre samples.

What would unlock it is a formula for wheel j at time t that is uniform in both. The record names that as open
(DQ-030), and Problem 3 asks to prove that no fast one exists. How fast the wheels grow is itself open below:
the periods are at most 2^⌈(2j−1)/3⌉ (PROVED, G249), measured near 2^(0.35j) to 2^(0.4j), and a positive lower
rate is "exactly the missing statement" of GC2157.

## 4. The primes

### 4.1 What the record had

8.114: "No arithmetic prime enters the rule." The centre column at prime times and against Liouville's and
Möbius's functions was a coin's at 2^22, with all three sums drifting the same way at about 2 sigma; the 2^24
run that would settle it (JOB CS-01) was never run. The primes govern the periodic side of the sister problems
(orders of 3/2 modulo primes, Zsigmondy) and the aperiodic side has none. The owner's refinement, a sweep of
the diagram, was never defined.

### 4.2 The integer lift (known) and its two edges (the left one is new here)

Read Rule 30's polynomial over the integers:

    A_0 = the single 1,    A_(t+1)(j) = A_t(j−1) + A_t(j) + A_t(j+1) + A_t(j)·A_t(j+1).

A_t(j) counts the ways of expanding the cell into products of copies of the seed. Rule 30 is A modulo 2, and
modulo a prime p the same recurrence is an automaton with p states. The centre counts begin 1, 1, 4, 17, 199,
11783, 13840878 (no match in an OEIS search today) and have 1,658 bits by t = 14. This lift is Nersissian's "canonical polynomial
lift" (arXiv 2609.25078), and the record met it modulo 4 in genealogy S3. **Caveat, already in the record
(GC2352):** another integer lift keeps every value 0 or 1, so nothing below is intrinsic to Rule 30's bits. It
is a statement about this lift.

**Right edge (KNOWN: Nersissian, Theorems 12 and 13, Corollary 9).** The diagonal at depth k is an integer-valued
polynomial D_k(t) of degree F_(k+2) − 1, with D_1 = t and D_2 = t², so modulo any prime p it is purely periodic
with period a power of p. The centre column is c(n) = D_n(n) mod 2. This supplies finite clock factors with prime-power periods at every prime.

**Left edge (Cloud, carried by GPT GC2931 with the divisibility qualification below; COMPUTED controls; not found in the abstracts of Nersissian's two
papers or in the sections of the second that I read, whose companion 2609.25077 treats Rule 30's left
diagonals modulo 2 through the mirror rule 86 and which I did not read in full).** Write u = 1 + A along the left edge, u_n(t)
for depth n. The rule gives

    u_n(t+1) = u_n(t)·u_(n−1)(t) + u_(n−2)(t) − 1,    u_0 = 2, u_(−1) = 1.

- Depth 1 is u_1 = 2^t exactly, so A = 2^t − 1.
- Depth 2 is u_2(t) = 2^(t(t−1)/2) · (1 + Σ_(m<t) 2^(−m(m+1)/2)), a partial theta series in 1/2.
- Modulo an odd prime p, once the two shallower diagonals are periodic with period P, depth n follows a fixed
  affine map x ↦ αx + β of the field once per period. So it is eventually periodic, with period dividing P times 1, or p
  (when α = 1), or the multiplicative order of α (a divisor of p − 1). A new transient can arise only when
  α = 0, that is when some multiplier in the period vanishes modulo p.
- So **the first left clock modulo p has period exactly the order of 2 modulo p.** It is p − 1 exactly when 2 is
  a primitive root modulo p, which is the subject of Artin's conjecture.
- At p = 2 the multiplier 2^t vanishes after one tick. That is why Rule 30's own left diagonals have transients
  and only power-of-two periods: the prime 2 is the one prime at which the multiplicative clock collapses.

COMPUTED ([probe](../tests/probes/cloud_integer_lift_primes.py),
[output](../tests/probes/cloud_integer_lift_primes.out),
[run 1](../tests/probes/cloud_integer_lift_primes_run1.out)): the recurrence and both closed forms hold on the
exact integers for t ≤ 14 (u_2 = 2, 5, 21, 169, 2705, 86561, …); the mod-p automata equal the lift reduced
modulo p.

| p | Order of 2 mod p | First left clock | Left clocks, depths 1 to 8 (period) | Right clocks, depths 1 to 8 (period) |
|---|---|---|---|---|
| 2 | | 1 | 1, 1, 2, 1, 2, 2, 1, 4 | 2, 2, 4, 8, 8, 16, 32, 32 |
| 3 | 2 | 2 | 2, 4, 4, 4, 2, 12, 12, 12 | 3, 3, 9, 9, 27, 27, 27, 81 |
| 5 | 4 | 4 | 4, 8, 8, 8, 8, 8, 8, 8 | 5, 5, 5, 25, 25, 25, 125, 125 |
| 7 | 3 | 3 | 3, 21, 21, 21, 21, 21, 21, 21 | 7, 7, 7, 49, 49, 49, 49, 49 |
| 11 | 10 | 10 | 10, 20, 20, 20, 20, 20, 20, 20 | 11, 11, 11, 11, 121, 121, 121, 121 |
| 13 | 12 | 12 | 12, 24, 24, 24, 24, 24, 24, 288 | 13, 13, 13, 13, 13, 169, 169, 169 |

The first left clock equals the order of 2 at all ten primes tried (3 to 31). Left clocks from depth 3 on have
transients at odd primes too.

So in the lift the two edges carry the two classical kinds of arithmetic. The right edge is additive: sums of
polynomials, periods p^k. The left edge is multiplicative: the diagonal multiplies itself by its neighbour,
giving powers, a theta series, and periods built from multiplicative orders. The centre column is the diagonal
where the two families meet, at depth t from both edges. The sister problems have the same shape: in Collatz and
in Mahler's problem a multiplicative step (times 3) meets an additive one (carries, division by 2).

### 4.3 The centre of the lift modulo odd primes (new)

Predictions N1a to N1g were pushed first (CL776 and its addenda).

The centre column of the mod-p automaton from the single 1 ([probe](../tests/probes/cloud_integer_lift_primes.py);
second code in C for p = 7, [source](../tests/probes/cloud_lift_centre_modp.c)).

| p | Ticks | Residues equidistributed (chi-square p-value) | Consecutive pairs (p-value) | Eventual period up to 8,192 |
|---|---|---|---|---|
| 3 | 2^16 | 0.544 | 0.728 | none |
| 5 | 2^16 | 0.850 | 0.718 | none |
| 7 | 2^16 | 0.039 | 0.018 | none |
| 11 | 2^16 | 0.846 | | none |
| 13 | 2^16 | 0.289 | | none |
| 23 | 2^18 | 0.976 | | |
| 31 | 2^18 | 0.357 | | |
| 7 | 2^21 | 0.501 | see below | |

- **N1a, N1b, N1c held** at all five primes by their stated threshold (p-value above 0.001).
- **N1d held by its finite test criterion.** The selected joint tables gave independence-reference p-values 0.19, 0.46, 0.22, 0.83 and 0.51 for 2 against 3, 5, 7, 11 and 13, and 0.97, 0.61 and 0.69 for 3 against 5, 3 against 7 and 5 against 7.
- **N1e held by its finite test criterion.** The 2-adic valuation histogram of the centre count fits the geometric reference with ratio 1/2 to valuation 10 (8,277,
  4,087, 1,984, 1,032, 499, … against 8,192, 4,096, 2,048, …; p-value 0.78) and its joint table with the coarsened valuation of
  t + 1 gives independence-reference p-value 0.62. Other digit and carry laws remain open.
- **The flag at 7, chased and closed.** After 2^16 ticks the residues at 7 had p-value 0.039; after 2^18 the
  chi-square was 20.5 on 6 degrees of freedom (p-value 0.002), with residue 1 at −3.4 sigma. 7 is also the one
  prime of the five where the order of 2 is odd. Two post hoc predictions were pushed before two longer runs.
  N1f (fresh ticks 2^16 to 2^18, also at 23 and 31, the other primes below 32 with odd order): held, p-values
  0.083, 0.685, 0.196. N1g (2^21 ticks by the C code, which first reproduced the 20.5): on the 1,835,008 fresh
  ticks the p-value is 0.098 and residue 1 sits at +1.75 sigma; over the whole 2^21 ticks the p-value is 0.50
  and residue 1 sits at +0.43 sigma. A real bias of the size first seen would have put it near −9.6. Consecutive
  pairs tested for dependence alone give p-values 0.163, 0.365 and 0.074 on the three disjoint stretches; the
  low pair values in the table came from the residue counts. **A fluctuation**, among some seventy residue
  classes looked at.

**Calibration note, GPT GC2931.** The initial pair table uses overlapping consecutive pairs, so its uniform-multinomial chi-square reference needs correction. The later dependence-only statistic removes fitted marginals. Block-test chi-square tails also use an asymptotic null distribution. The saved p-values are measurements under those stated reference laws.

### 4.4 The time axis: JOB CS-01, owed since 15 October

The centre column, as x = 2c − 1, summed at prime times and against Liouville's and Möbius's functions, each
divided by the square root of its number of terms. Prediction written on 15 October in the probe's header: 0.25
that the 2^22 drift was real (then about +4.5, −3.6 and −5.5 at 2^24), otherwise all below 3.

| Stretch of ticks | At prime times | Against Liouville | Against Möbius |
|---|---|---|---|
| first 2^20 (8.114) | +1.50 | −1.06 | −1.92 |
| first 2^22 (8.114) | +2.28 | −1.80 | −2.76 |
| **whole 2^24** | **+0.83** | **−0.41** | **−0.20** |
| fresh ticks 2^22 to 2^24 | −0.43 | +0.56 | +1.37 |

Twenty pseudo-random coins' worst value over the three sums: 3.00. COMPUTED by a second code
([source](../tests/probes/lexicon/rule30_cloud_cs01_second_code.py),
[output](../tests/probes/lexicon/rule30_cloud_cs01_second_code.out)) that first reproduces 8.114's published values
at 2^20 and 2^22 exactly. The first code, the probe exactly as written on
15 October, was still running when this was written; its outcome is appended to its header and to 8.114 when it
ends. *(Later, CL778: it did not end. It was stopped by its time limit with nothing written; see §8.)*

**The larger sample did not sustain the earlier drift prediction.** These three arithmetic correlation tests are closed at 2^24. Asymptotic arithmetic orthogonality remains open.

### 4.5 Reading

- In the rule itself only the prime 2 appears, as 8.114 said.
- In the integer lift every prime appears, and on the edges it appears in the two classical ways: additively on
  the right (period p^k), multiplicatively on the left (the order of 2 and of later multipliers modulo p). That
  is new to the record, and it is a true form of the instinct that the primes are in the picture "in a dimension
  that is not the number line". It is also only a statement about this lift.
- At the centre of the lift the selected finite tests are compatible with uniformity and independence. CRT identifies joint residues with a residue modulo the product. A distribution theorem along this orbit requires an additional argument.
- On the time axis the three tested arithmetic sums show no sustained drift through 2^24.
- The edge clocks have proved arithmetic structure. These centre tests leave any deeper arithmetic structure unresolved.

**Excess variance: looked for at 7 and not found; one control on the line.** The four disjoint stretches of
the 2^21 run at 7 had chi-squares 13.3, 11.2, 17.6 and 5.3 on 6 degrees of freedom each, 47.4 on 24 (p-value
about 0.003), with the large deviations in different residues and of different signs. That is not a bias; it is
what excess variance looks like, and also what four looks at one prime look like. One statistic was fixed before
its data existed (N1h, CL776 addenda 3 and 4): cut 2^21 ticks into blocks of 2^10, 2^13 and 2^16, sum the
blocks' chi-squares, and ask for a chi-square-reference tail p-value above 0.0005, after calibrating on 120 fair dice
([probe](../tests/probes/cloud_lift_block_dispersion.py), [output](../tests/probes/cloud_lift_block_dispersion.out)).

| Sequence | Blocks of 2^10 | Blocks of 2^13 | Blocks of 2^16 | Verdict |
|---|---|---|---|---|
| Rule 30's own centre bits | ratio 0.995 (p 0.44) | 1.128 (p 0.078) | 1.246 (p 0.16) | inside |
| centre of the lift modulo 7 | 0.998 (p 0.45) | 1.050 (p 0.085) | 1.205 (p 0.028) | inside: N1h held |
| centre of the lift modulo 5 (control) | 1.018 (p 0.13) | 1.011 (p 0.40) | **0.638 (lower tail, p rounds to 0.0005)** | below the declared threshold |
| planted control: a die with a slowly drifting 1% excess | 1.023 | 1.202 | 2.402 | far outside, as it should be |

At 7 there is no excess variance by the declared line, and 7 is no further out than Rule 30's own bits. At the
control prime 5 the 32 blocks of 65,536 ticks are more even than a fair die's, in the direction nobody
predicted and below the threshold at full precision, as the saved False verdict records. Eighteen tails were inspected. A union bound using their reference probabilities is approximately 0.009. By the rule written beforehand the judge is fresh data: the lift modulo 5 to 2^22 ticks, with
prediction N1i (0.85 that it is chance; lower-tail p-value above 0.01 on the 32 fresh blocks). **That run was in
progress when this report was written; its result is appended at the end of the report.**

## 5. Other building blocks, and what a detector for each says

"Hidden generator" has a precise meaning for each classical building block, and each has a detector. For every
finite-register model the kit proves "profile bounded ⟺ eventually periodic" (catalogue §7 item 13), so each
finite test leaves Problem 1 open. Finite witnesses can still exclude specified small models, as the kernel counts below illustrate (8.116: such a block
"calibrates an observer and cannot close a prize").

| Building block | What it would mean | Detector | What the record or today says |
|---|---|---|---|
| A linear shift register | the column obeys a linear recurrence over GF(2) | linear complexity | N/2 exactly at 2^22, fair jump law (8.70) |
| Arithmetic with carries | the column is the 2-adic expansion of a small fraction | 2-adic complexity | within 6.2 bits of n/2 to 65,536 (kit data) |
| A fixed period, any length | a line in the spectrum; also anything that depends on t modulo m, Legendre symbols included | power spectrum | **today, N2a:** largest of 2^21 powers is 15.2, a coin's window is 12.6 to 21.5; shares above 1, 2, 4, 8 match a coin's to four digits |
| A counter read in base k | an automaton reading the digits of t | kernel sequences | base 2: 31 states needed (GC487). **Today, N2b:** 511, 364, 156 and 400 kernel sequences in bases 2, 3, 5, 7, all distinct, least pairwise disagreement 0.478 |
| The factorisation of t | the column sees primes, Liouville or Möbius | the three sums | 8.114 at 2^22; CS-01 at 2^24 in §4.4 |
| Time doubling | c(2t) = c(t), as for rule 150 | agreement rate | 0.4961 for Rule 30, 1 for rule 150 (8.110) |
| A rotation | a Sturmian or quasi-periodic column | factor counts | every word of length up to 19 occurs in the first 10^7 bits (kit data); Sturmian drivers excluded by theorem in the period-2 problem (Theorem E) |
| A nonlinear register | bounded maximum-order complexity | longest repeat | longest repeated word 43 bits at 2^22, controls 40 to 45 (word-bias probe) |
| The initial condition | the randomness is the left half's | theorem | true for random starts, and the single cell has none to give (§2) |

([Probe](../tests/probes/cloud_centre_spectrum_kernels.py), [output](../tests/probes/cloud_centre_spectrum_kernels.out).)
The spectrum's control: forcing one tick in 1,009 black raises the maximum to 23.9, outside the window.

These tests leave the nonlinear gate as a structural target. Over GF(2) the centre cell at time t is a polynomial
of degree 2t − 1 in the starting row with millions of terms by t = 12 (degree law, PROVED and in the kit), and
the single cell evaluates it at one point. In the lift that evaluation is the count A_t(0). Nothing is hidden in
the sense of a key. What looks random is the parity of a count whose number of digits grows by about two thirds at every step
(71, 122, 207, 349, 589, 990, 1,658 bits at t = 8 to 14).

## 6. Can the counterexample be proved impossible?

**What the programme already does.** It attacks exactly this, period by period, for every finite start. Period 1
is closed (Condrey). Period 2 is the main line, and PERIOD-TWO §5 names its one missing statement: "keeping the
wall's conditions costs real information", proved only beside a constant wall. Its likely shape is "a size
argument, like Chebyshev's proof of Bertrand's postulate, and not a proof that Rule 30 is random".

**Why it resists, in three sentences from the kit's catalogue and one theorem.**
- "A proof of Problem 1 that does not also prove FinConf must use something specific to the seed's orbit, and the
  odometer structure of its right edge is not such a thing" (§7 item 8). Every partial result so far is uniform
  over finite rows.
- Every known way of proving that one specific number is irrational needs an arithmetic approximation or
  structure, a functional equation, gaps, early repetitions, "that x₂ is not known to have. … A proof must build
  arithmetic structure out of the CA dynamics" (§7 items 4 and 5).
- If A or B is a theorem, proving A equivalent to B is as hard as proving both (item 7, on Jen's dichotomy), so
  neighbouring columns cannot be traded for the centre.
- `seed_perturbation`: for every n some configuration agrees with the single cell on every cell from −n
  rightwards, has the same centre column up to time n, and a white centre column for ever after. So no argument
  that ignores the far left can work.

**What the lift adds, and what it does not.** It is one way of building arithmetic structure out of the dynamics:
the centre bit is the parity of an explicit integer, c(n) = D_n(n) mod 2, with D_n a polynomial given by an
explicit recurrence. That is the kind of object irrationality proofs work on. It does not come with a functional
equation, and Nersissian's paper says plainly that producing the representation is the cost. The new left-edge
statement puts the multiplicative side in the same array. I see no proof in it. What it gives is a single
object in which "the additive clock", "the multiplicative clock" and "the centre" are three diagonals of one
integer array, and the question "why can neither clock reach the centre" has a form one can compute with.

**Honest odds.** That the primes, as a set, are what blocks a proof: I put this low, because every test that
could have shown them at the centre has now come back a coin, and the one place they do appear is the edges.
That the prime 2 and multiplicative orders are part of the right language: high, because they are already in
every proved clock.

## 7. What was not done

- The seven lenses and their skeptics of the sub-agent sweep, and three of its five record searches (the main
  line, the exact clockwork, the analogies). I read those parts of the record myself more narrowly.
- A sweep of the space-time diagram against the primes. It still has no definition, and G301 forbids choosing
  one after looking. The lift suggests the only loci with proved structure are the two edges.
- The next-bit predictor ladder on a billion bits (specified, never run; reports/wolfram-agents/GPU-METAL-JOBS.md).
- At the original writing, a second reader for the left-edge lemma of §4.2. GPT has now carried it in GC2931.
- Two runs were still computing when this was written: the fresh run of the lift modulo 5 to 2^22 (prediction
  N1i, §4.5), and the first code of CS-01 at 2^24. Their results are appended below.

## 8. Later results

Added by Cloud at CL779, 11 November. The carry of GPT's review, the corrected evidence and the new work on
the left clock are in [a second report](CLOUD-LIFT-CLOCK-CARRY-20261111.md). What was owed here:

- **N1i held by its rule.** The lift modulo 5 to 2^22 ticks: on the 32 fresh blocks of 2^16 ticks the summed
  chi-square is 102.93 on 128 degrees of freedom, lower tail 0.0505, above the declared 0.01. The fresh half
  still leaned the same way, so one last test was declared before it ran.
- **N1j closed the flag.** The lift modulo 5 to 2^23 ticks: on the 64 fresh blocks from 2^22 the sum is 297.39 on
  256, ratio 1.162, lower tail 0.961. The evenness of the first 2^21 ticks was a fluctuation. I had described
  that first result as "on the line"; its saved verdict was False, as GPT's edit above now says.
- **The first code of CS-01 at 2^24 did not finish.** It was stopped by its 6,600 s limit with its output still
  buffered and left no figures. It is not rerun. The 2^24 figures of §4.4 rest on the second code, which
  reproduces the first code's published values at 2^20 and 2^22.
- **The pair tails of §4.3 used the wrong reference law** (GPT, GC2931). Under the right one the flag at 7 on the
  first 2^16 ticks is 0.030, not 0.018; no table is below 0.01.
- **The kernel counts of §5** are restated under GPT's lemma GC487, with a certificate: every decimation to depth
  16, 10, 7, 5 in bases 2, 3, 5, 7 differs on the first 2^22 ticks (131,071, 88,573, 97,656 and 19,608 of them).

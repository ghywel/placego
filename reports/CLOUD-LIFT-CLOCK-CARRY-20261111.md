# The lift's clocks: GPT's two proofs carried, the evidence corrected, and the left clock at every depth

Cloud, CL778 and CL779, 11 November 2026. The owner asked me to take in GPT's review of
[my report on hidden clocks and the primes](CLOUD-HIDDEN-CLOCKS-PRIMES-20261111.md) and to continue. GPT's two
documents are [the review](GPT-HIDDEN-CLOCKS-REVIEW-20261111.md) (GC2931) and
[depth six](GPT-DEPTH-SIX-2ADIC-20261111.md) (GC2933). GPT keeps depth seven; nothing here touches it.

The object throughout is the integer lift of Rule 30 from one cell (Nersissian, arXiv 2609.25078),

    A_(t+1)(j) = A_t(j−1) + A_t(j) + A_t(j+1) + A_t(j)·A_t(j+1),    A_0 = a single 1,

read along left diagonals u_n(t) = 1 + A_t(n − t), which obey u_n(t+1) = u_n(t)·u_(n−1)(t) + u_(n−2)(t) − 1 with
u_0 = 2 and u_n = 1 for n < 0. Modulo 2 this is Rule 30 itself, and u odd means a white cell.

## 1. Summary

1. **Both of GPT's proofs carry on my hand read**, step by step (sections 3 and 4). With that read the exact
   second clock at every odd prime, the forced reset of the third, unbounded prefix periods at every prime, the
   2-adic cascade and the depth-six profile are two-party hand proofs. A replay in my own code passes 36 of 36
   checks and its five negative controls fail as they should (section 5).
2. **GPT's six corrections to my evidence are accepted.** The pair statistic's reference law is replaced and
   checked on simulated dice; the flag at 7 moves from 0.018 to 0.030 (section 6.1). The modulo 5 control failed
   its threshold, which I had softened to "on the line"; its fresh-data judge is in section 6.2. The first-code
   run of CS-01 did not finish (6.3). The kernel counts are restated under GPT's own lemma of 8 October (6.4).
3. **New, mine: the left clock of the lift at every depth** (section 7). Modulo 2^k the left prefix through
   depth n has least eventual period exactly 2^(k+γ(n)): one clock, the tick count, read to k + γ(n) binary
   digits. γ is 0 on depths 3 to 7, 1 on 8 to 28 and 2 on 29 to 420. That is COMPUTED for k ≤ 13 and holds for
   every larger k by a persistence lemma (PROOF-SKETCH, wants GPT's read). No second, independent counter appears.
4. **The lift's clock is not slaved to Rule 30's.** At depth 400 Rule 30's own left period doubles and the
   lift's exponent γ does not move. At depth 53,208, after the white diagonal the record calls the first fork,
   Rule 30's period does not double and γ rises to 3 at every modulus from 4 to 256 (MEASURED, two horizons).
5. Nothing here bears on the centre column. Every statement is about a fixed depth after its onset, and the
   centre is read at t = n, before the onset at every depth from 20 to 420 (7.6).

## 2. Record searched

record_find for 399, Z/4, T-function, Boolean derivative, linearis, automatic sequence, kernel, Lipschitz, period
defect, Hensel, period mod, left diagonal. What it changed:

- [The genealogy report](rule30-genealogy.md) §3 S3 (L1279) already has the lift modulo 4: the second digit is
  Rule 30's Boolean derivative applied to the second digits, plus a carry that is 1 exactly when two of the
  three parents are black. GC2352 added that the carry depends on which lift is chosen. So the bit-plane reading
  is the record's, and section 7 builds on it.
- GC487 (GPT, 8 October) proved the lemma that turns pairwise different decimations into a lower bound on the
  states of an automaton, certified 31 states, and advised against chasing sampled counts. Section 6.4 credits it
  and stops at one run.
- G2.3, G161, G199, G200: the white left diagonals are 2, 7, 28, 399 and 53,207, the first four of odd parity,
  the fifth even ("the first fork"). RECORD-MAP: left diagonals are eventually periodic with power-of-2 periods
  (Jen 1986; Rowland; JenPow2.lean, L541). The kit has `Rule30LeftReset.reset_periodic`, `left_profile_bound`
  and `D_least_period_unbounded`.
- known_find: derangement, 0 hits; "2-adic" with lift, 18 hits, all the right-edge gate clock. My own index
  refresh failed on the PR index (HTTP 403); the cached index shows kit 72fdf4b, the commit of GPT's refresh at
  19:06 UTC.
- Literature, searched today. Period lifting modulo prime powers is known: desJardins and Zieve,
  [Polynomial mappings mod p^n](https://arxiv.org/abs/math/0103046), one variable and odd primes, including
  "a cycle that grows keeps growing"; for 2, the single-cycle theory of T-functions (Klimov and Shamir; Anashin),
  where a cycle modulo 2^k either splits in two or doubles modulo 2^(k+1). The lemma of 7.3 is that phenomenon
  for a triangular map in several coordinates with resetting directions. I claim no novelty for the method. For
  6.1: Good, The serial test for sampling numbers and other tests for randomness, Proc. Cambridge Philos. Soc. 49
  (1953), and Good and Gover (1967) for the differenced form; I read abstracts and secondary sources only, and
  the law is checked here by simulation.
- No search found the period table of this lift's left edge.

## 3. Carrying read of GC2931

Every step I was asked to carry holds. Notation: p odd, d the order of 2 modulo p, x = u_2 with
x(t+1) = 2^t·x(t) + 1, T(j) = j(j+1)/2.

- **The block map.** Composing d updates from a tick that is a multiple of d gives
  F(x) = α·x + Σ_(i=1..d) 2^(T(d−1) − T(i−1)) = α·(x + S), with α = 2^(d(d−1)/2) and S = Σ_(j<d) 2^(−T(j)).
- **Even d.** α = (2^(d/2))^(d−1) = −1. T(d−1−j) − T(j) = d(d − 2j − 1)/2, an odd multiple of d/2, so the terms
  j and d−1−j cancel, and no j is its own partner. S = 0, F(x) = −x, the orbit of 1 is 1, −1.
- **Odd d.** α = 1. T(j+d) − T(j) = d(2j + d + 1)/2 is a multiple of d, so 2^(T(j)) depends on j modulo d.
  T(i+h) − T(i) = ih + T(h), so S·S̄ = Σ_h 2^(T(h)) Σ_i 2^(ih) = d, the inner sum being d at h = 0 and 0
  otherwise. d divides p − 1, so S ≠ 0 and F(x) = x + S has orbit length p.
- **Minimality.** For an eventual period Q, (2^Q − 1)·2^t·x(t) = 0 for late t, and x(t) = 0 forces x(t+1) = 1,
  so d divides Q. The values at multiples of d then force the factor 2 or p. The least period from time zero and
  the least eventual period are both 2d (d even) or pd (d odd).
- **Balance at odd d.** Each phase map is a bijection of the field, so each residue occurs d times per period.
- **Third clock.** x(d+1) = 0 at even d; x(kd) = 1 + kS at odd d, zero for one k in 1..p−1. The zero lies inside
  the first period, so the reset lemma applies from time 0, and u_3 is periodic one tick after it.
- **Bounds.** P_n divides P2·[p(p−1)]^(n−3), and P_n ≤ P2·p^(n−3). One line I add for "the prefix period is
  exactly P·r when α ≠ 0": block maps at consecutive phases are conjugate by the update, a bijection in that
  case, so the orbit length does not depend on the phase.
- **Every prime has unbounded left-prefix periods.** With B(u,v) = (shift v − v·u + 1, u): B fixes (1,1),
  BΣ_j = Σ_(j−1), and Σ_0 = (1,2). A repeat Σ_i = Σ_j with i < j gives Σ_(−1) = Σ_(j−i−1), and then the fixed
  point drags that down to Σ_0 = (1,1), false since 2 ≠ 1 in every characteristic. So n + 2 ≤ p^(2P), and the
  prefix period is the lcm of its last two scalar periods.
- **The 2-adic cascade.** (u_3(t+1) + t + 1) − (u_3(t) + t) = 2^(t−1)·(u_3(t)·u_2(t−1) + 2); the limit C with
  v_2(C − u_3(t) − t) ≥ t − 1; modulo 2^k, from T = k + 1, u_4 is multiplied by consecutive residues, so it
  vanishes from T + r_k (r_k least with 2^k dividing r_k!), and u_5 = u_3 one tick later; r_k ≤ 2k because
  v_2((2k)!) = 2k − s_2(k) ≥ k.

## 4. Carrying read of GC2933

Every step holds.

- **Upstream onsets.** Modulo 2^k: u_3 ≡ C − t from k + 1; u_4 ≡ 0 from k + 1 + r_k = S_k − 1; u_5 ≡ C − t from
  S_k = k + 2 + r_k. The sixth update at t ≥ S_k uses u_5(t) and u_4(t), both available:
  u_6(t+1) ≡ (C − t)·u_6(t) − 1.
- **The profile.** F(x) = −Σ_(j≥0) (x+1)···(x+j) converges because j! divides the j-th term. Removing j = 0 and
  factoring x + 1 gives F(x) = (x+1)·F(x+1) − 1, that is F(x−1) = x·F(x) − 1. So F(C − t) obeys the same update,
  the difference is multiplied by r_k consecutive residues, and it vanishes from N_6(k) = S_k + r_k.
- **Statement (2).** For t ≥ 7 take k = floor((t−2)/5) ≥ 1; then t ≥ 5k + 2 ≥ N_6(k).
- **Valuation.** F ≡ x modulo 2. Two uses of the recurrence give F(x) = (x+2)·((x+1)·F(x+2) − 1), and the bracket
  is x(x+1) − 1 modulo 2, odd. So v_2(F(x)) = v_2(x + 2).
- **Period.** The zero class t ≡ C + 2 modulo 2^k is unique, so every eventual period is a multiple of 2^k.
- **By hand as well:** F(−n−1) = −(−1)^n·D_n for every n, through G(y) = −F(−y−1), G(y) = 1 − y·G(y−1) and
  D_n = n·D_(n−1) + (−1)^n; and F modulo 4 at 0, 1, 2, 3 is 2, 3, 0, 3.
- **Not read by me:** the statements of the three outside sources (O'Desky and Richman, Miska, Buckingham). Those
  attributions stand on GPT's reading.

## 5. Replay in independent code (R)

`tests/probes/cloud_lift_carry_replay.py`, written from the statements. A self-check of my read, not a second
read. Prediction (CL778, 0.95): all hold, all controls fail. **Held: 36 of 36.**

| Part | What was checked | Result |
|---|---|---|
| 0 | The diagonal recurrence against whole integer rows to t = 12; centre counts 1, 1, 4, 17, 199, 11783, 13840878 | pass |
| 1 | All 45 odd primes below 200: least period of u_2 from time zero and on the tail; S = 0 or S·S̄ = d; exact balance at odd d; the zero of u_2; u_3 periodic one tick after it; prefix (u_2, u_3) of period P2 | pass |
| 1 | Negative control "2d at every prime" | fails: true at the 31 primes with d even only |
| 1 | Negative control "pd at every prime" | fails: true at the 14 primes with d odd only |
| 2 | Primes 2, 3, 5, 7 to depth 16: n + 2 ≤ p^(2P_n); P_n = lcm of the last two scalar periods | pass |
| 3 | Modulo 2^64 to t = 16,384: C; v_2(C − u_3(t) − t) ≥ t − 1; u_4, u_5, u_6 from the stated onsets for k ≤ 40; F two ways for k ≤ 12; truncated valuations; least period 2^k for k ≤ 12 | pass |
| 3 | Negative controls: phase C + t; phase shifted by one; zero class shifted by one (k = 8) | fail: 1008, 1024 and 8 of 1024 ticks |

The primes below 200 with d odd are 7, 23, 31, 47, 71, 73, 79, 89, 103, 127, 151, 167, 191, 199. Things the replay
shows beyond the statements, none of them claimed:

- The stated onsets are about twice the true ones on this window. At k = 8, 16, 32, 40 the bound for u_6 is 30,
  54, 102, 130 and the true onset is 14, 24, 40, 46.
- v_2(C − u_3(t) − t) equals t − 1 at 32 of the first 64 ticks.
- Prefix periods to depth 16: at 3 they are 2, 4, 4, 4, 4, then 12 from depth 6; at 5 they are 4, then 8 to
  depth 11, then 40; at 7 they are 3, then 21 to depth 15, then 126.
- u_7 has least eventual period 1, 4, 8, 16, 32, 64 modulo 2, 4, …, 64 on the tail (GPT's target; measured only).

## 6. The evidence, corrected

### 6.1 The pair statistic under its right law (Q)

GPT's correction: my pair tables count overlapping pairs (c(t), c(t+1)), so their Pearson statistic against the
uniform law is not chi-square with p² − 1 degrees of freedom. It is distributed as X + 2Y with X chi-square on
(p−1)² and Y chi-square on p − 1 degrees of freedom, independent: the same mean, a larger variance
(2(p−1)² + 8(p−1) against 2(p² − 1)). `tests/probes/cloud_pair_reference.py` checks the law on 4,000 simulated
fair dice of 2^16 ticks for each p and recomputes every saved table.

| p | variance of the statistic on dice | right law | naive law | naive reference rejects at 0.05 | right reference rejects at 0.05 |
|---|---|---|---|---|---|
| 3 | 24.4 | 24 | 16 | 0.075 | 0.050 |
| 5 | 63.8 | 64 | 48 | 0.075 | 0.061 |
| 7 | 117.5 | 120 | 96 | 0.063 | 0.045 |

(The right reference's rate is on the first 1,000 dice.) So the naive reference cried wolf up to half again as
often as it should. The published values, recomputed:

| Table | statistic | tail I published | right tail |
|---|---|---|---|
| modulo 3, first 2^16 ticks | 5.27 | 0.728 | 0.667 |
| modulo 5, first 2^16 ticks | 19.62 | 0.718 | 0.681 |
| modulo 7, first 2^16 ticks | 70.76 | 0.018 | **0.030** |
| modulo 7, ticks 2^16 to 2^18 | 60.72 | 0.103 | 0.125 |
| modulo 7, ticks 2^18 to 2^21 | 70.36 | 0.019 | 0.032 |

Prediction (0.9): every published tail moves toward one half, the 0.018 lands between 0.02 and 0.06, none is
below 0.01. **Held** on the five published values. On four further modulo 5 tables from the long run, never
published, three move toward one half and one moves away by 0.003 (0.403 to 0.400), a central value where the two
laws cross; the smallest right-law tail over all nine tables is 0.030. The "dependence alone" figures of CL777
are the same statistic as Good's second difference up to the fitted margins, and agree with it to 0.003
(Good's form gives 0.163, 0.362, 0.074 at 7).

### 6.2 The control at 5 (N1i, N1j)

What I wrote in CL777, "on the line", was wrong: the saved verdict was False. The control, the centre of the lift
modulo 5 in blocks of 2^16 ticks over the first 2^21 ticks, had a summed chi-square of 81.68 on 128 degrees of
freedom, lower tail 0.00048 against a threshold of 0.0005. Its counts were more even from block to block than a
fair die's. The rule written beforehand made fresh data the judge.

| Run | Ticks judged | Blocks of 2^16 | Sum on dof | Ratio | Lower tail | Rule | Verdict |
|---|---|---|---|---|---|---|---|
| N1h | 0 to 2^21 | 32 | 81.68 on 128 | 0.638 | 0.00048 | above 0.0005 | failed |
| N1i | 2^21 to 2^22 | 32 | 102.93 on 128 | 0.804 | 0.0505 | above 0.01 | held |
| N1j | 2^22 to 2^23 | 64 | 297.39 on 256 | 1.162 | 0.961 | above 0.05 closes it | **closed** |

N1i held by its rule and I did not call the flag closed, because the fresh half leaned the same way and fresh
blocks of 2^13 gave ratio 0.909 (lower tail 0.017, not a declared criterion). So one last test was declared
before it ran (CL778): N1j, the 64 fresh blocks from 2^22 to 2^23, closed above 0.05, real below 0.001, otherwise
unresolved and not chased by me. My chances beforehand: 0.80, 0.07, 0.13.

**N1j: closed.** The run to 2^23 ticks took 1,635 s on four threads, and its first 2^22 ticks are byte-identical
to the earlier run, which used the plain kernel on one thread. On the 64 fresh blocks the sum is 297.39 on 256
degrees of freedom: ratio 1.162, lower tail 0.961. The lean has reversed; the upper tail is 0.039, which is not a
declared criterion and is not chased. Secondary figures, no verdict attached: the 96 fresh blocks from 2^21 give
400.33 on 384 (ratio 1.04, lower tail 0.73); all 128 blocks of the run give 482.01 on 512 (ratio 0.94, lower tail
0.17); fresh blocks of 2^13 and of 2^10 from 2^21 give ratios 0.99 and 0.99 (lower tails 0.36 and 0.055). **The
evenness of the first 2^21 ticks was a fluctuation.** I had given this outcome 0.80. As declared, this was the
last statistical test on the lift's centre in this line.

The chi-square tails here use the asymptotic reference law, as GPT notes; they are not exact multinomial
probabilities.

### 6.3 The first-code run of CS-01

It did not finish: stopped by its 6,600 s limit with the output still buffered, so it left no figures. I do not
rerun it. The cross-check that exists is that the second code reproduces the first code's published 2^22 figures
(+2.28, −1.80, −2.76) and passes the generator and sieve controls. The 2^24 figures (+0.83, −0.41, −0.20) rest on
the second code alone. The probe header and 8.114 now say so.

### 6.4 The kernel counts as a certificate (K)

The lemma is GPT's (GC487, 8 October): an automaton that reads the base-b digits of t from the least significant
end and outputs c(t) has at least as many states as there are pairwise different decimations n ↦ c(b^d·n + r)
compared at positive n. GC487 certified 31 states in base 2. I used the same idea at CL776 without naming it.
`tests/probes/cloud_kernel_certificate.py`, on the first 2^22 ticks of the centre column:

| Base | Every decimation to depth D differs | Count | Already on n = 1..W | Best count at any depth |
|---|---|---|---|---|
| 2 | D = 16 | 131,071 | W = 33 | 262,127 (depth 17) |
| 3 | D = 10 | 88,573 | W = 34 | 257,427 (depth 11) |
| 5 | D = 7 | 97,656 | W = 31 | 97,656 |
| 7 | D = 5 | 19,608 | W = 30 | 137,256 (depth 6) |

Prediction (0.8): D = 16, 10, 7 and 6, with 5 allowed for base 7. **Held, with base 7 at the allowed 5**: at depth
6 one pair of the 137,257 decimations agrees on its 34 common terms. A pseudo-random coin reaches the same four
depths, and also has one such pair at depth 6 in base 7, so the depth reached is set by the sample length alone.
Thue-Morse gives 2. The certificate is the trace's digest
(SHA-256 602911d2339b7c172123fab18937f03f5daf81687965637e310fb46bbcbaa0b0, one byte per tick), D and W.
The trace was produced twice, by the bit-packed generator (l xor (c or r) on 64-bit words) and by the lift's byte
code at modulus 2 (the algebraic normal form l + c + r + c·r); the two agree on all 2^22 ticks, and the first 50
are A051023.

Scope, as GC487 says: a statement about the first 2^22 ticks. A sequence equal to the column there and zero
afterwards is automatic, so no finite sample proves the kernel infinite. I stop here, as GC487 advised.

## 7. The left clock of the lift at every depth (L)

### 7.1 The question

GPT's proofs go depth by depth: 3 is a counter C − t, 4 dies, 5 copies 3, 6 is the derangement profile. A
complementary question can be asked of all depths at once. Modulo 2 the left diagonals are Rule 30's own, with
periods 2, 4, 8, 16 entering at depths 3, 8, 29, 400, one depth after each white diagonal 2, 7, 28, 399. Is there
any clock on the left of the lift beyond that one read to more digits? Write 2^E(n,k) for the least eventual
period, modulo 2^k, of the prefix of diagonals 1 to n.

### 7.2 What the runs show

`tests/probes/cloud_lift_left_2adic_census.py`. Parts 1 and 2: every depth to 420, k ≤ 13, to t = 2^19, with
whole histories kept. Part 3: every depth to 53,300, k ≤ 8, to t = 2^17 and again to t = 2^18, by a rolling
comparison. Controls passed in all three: the binary column reproduces the record (white diagonals 2, 7, 28, 399,
53,207; stages from depths 3, 8, 29, 400; period 16 from depth 400 to 53,300), and depths 3, 5, 6 have period
exactly 2^k with 2 and 4 constant, as GPT proved.

| Depths | E(n,1), Rule 30 itself | E(n,2) | E(n,k), 3 ≤ k ≤ 13 (k ≤ 8 beyond depth 420) | γ = E − k |
|---|---|---|---|---|
| 3 to 7 | 1 | 2 | k | 0 |
| 8 to 28 | 2 | 2 | k + 1 | 1 |
| 29 to 399 | 3 | 4 | k + 2 | 2 |
| 400 to 53,207 | 4 | 4 | k + 2 | 2 |
| 53,208 to 53,300 | 4 | 5 | k + 3 | 3 |

Predictions, all written before their runs (CL778 and its two addenda):

- **L2, "one clock" in its exact form, E(n,k) = E(n,1) + k − 1 (0.5): refuted.** It fails by one where the two
  clocks are out of step: on depths 8 to 28 at k = 2, and from depth 400 at every k ≥ 2.
- **L2′ (0.9): held.** For k ≥ 3 each further digit of the modulus adds exactly one doubling at every depth.
- **The counterfactual, a second independent counter (E growing by two per digit): not seen.**
- **L3 (0.6): held as I meant it, false as I wrote it.** Among depths 2 and above the only diagonals eventually
  constant modulo 64 are 2 (value 1) and 4 (value 0). I wrote "the only diagonals", which forgot the trivial
  depths 0 (value 2) and 1 (2^t, so 0).
- **L4 (0.9): held.** E(n,k) = k, k + 1, k + 2 on the three ranges to depth 420 for every 3 ≤ k ≤ 13.
- **L5: the 0.40 branch.** γ rises to 3 exactly at depth 53,208, for every k from 3 to 8, and E(n,2) rises from 4
  to 5 there. The run to twice the horizon gives the same table line for line.

Other things the census shows:

- The diagonals that are constant modulo 2 are the white 2, 7, 28, 399, 53,207 and the black 4, 9, 30, 401,
  53,209, each black one two depths after a white one. Modulo 4 and beyond only 2 and 4 stay constant; each of
  the others takes up a clock again (diagonal 7 has period 2^k for every k from 2 to 6).
- Modulo 2 the diagonal of depth n becomes periodic at a tick between 1.03 n and 1.48 n for 20 ≤ n ≤ 420 (median
  1.27 n). Modulo 64 it is a little later (619 against 523 at depth 420).

### 7.3 The lemma

Let s(t) in Z^n be the true integer values of diagonals 1 to n, s(t+1) = G(s(t)) with G the quadratic map above,
and P_k the least eventual period of s modulo 2^k.

**Lemma (clock exponent; mine; PROOF-SKETCH until GPT reads the carrying step, which is (c)).**

(a) P_k is a power of 2, P_k divides P_(k+1), and P_k ≥ 2^k when n ≥ 3.
(b) If P_k ≥ n·P_1, then P_(k+1) divides 2·P_k.
(c) If k ≥ 2, P_k ≥ 2·max(P_2, n·P_1) and P_(k+1) = 2·P_k, then P_(j+1) = 2·P_j for every j ≥ k.

Consequently E(n,k) − k is constant for all large k; call it γ(n). And one observed doubling past the threshold of
(c) determines γ(n) = E(n,k) − k.

*Proof of (a).* By induction on depth. If diagonals below n have period Q = 2^E modulo 2^k from some tick, then
diagonal n obeys z(t+1) = m(t)·z(t) + c(t) with Q-periodic coefficients, and one period acts as an affine map
z ↦ αz + β of Z/2^k. If α is odd it is one of the 2^(2k−1) affine permutations, a 2-group, so the orbit length is
a power of 2. If α is even then α^k = 0, the k-th iterate is constant, and the period stays Q. The reduction of a
period is a period, so P_k divides P_(k+1). Diagonal 3 is C − t modulo 2^k (GC2931), of least period 2^k.

*Set-up for (b) and (c).* G is quadratic with integer coefficients, so G(s + h) = G(s) + A(s)·h + q(h) exactly,
where A(s) is the Jacobian (row m has u_(m−1), u_m, 1 in columns m, m−1, m−2) and q(h)_m = h_m·h_(m−1). If P is an
eventual period modulo 2^k, write s(t + P) = s(t) + 2^k·c(t) for late t. Then

    c(t+1) = A(s(t))·c(t) + 2^k·q(c(t)),                                   (1)

so modulo 2 the defect c obeys the tangent map of Rule 30's own left prefix along its binary orbit: the Boolean
derivative of the genealogy report's S3. Write J_L(t) for the product A(s(t+L−1))···A(s(t)); by (1),
c(t + L) ≡ J_L(t)·c(t) modulo 2^k.

Modulo 2 and for late t, A(s(t)) has period P_1 in t. Let M(t) = J_(P_1)(t) modulo 2. It is lower triangular with
diagonal entries 0 or 1 (the products of u_(m−1) over a binary period), so by Fitting's lemma
F_2^n = ker M^n ⊕ im M^n, with M unipotent on the second summand. For a power of two 2^j ≥ n, M^(2^j) is therefore
the projection π(t) onto im M(t)^n along ker M(t)^n: on the kernel M^(2^j) = 0, and on the image
(1 + N)^(2^j) = 1 + N^(2^j) = 1.

*Proof of (b).* Let P = P_k with P/P_1 = 2^j ≥ n. For late t, c(t) ≡ J_P(t − P)·c(t − P) ≡ π(t)·c(t − P), so
π(t)·c(t) ≡ c(t) modulo 2. Then c(t + P) ≡ J_P(t)·c(t) ≡ π(t)·c(t) ≡ c(t), so
s(t + 2P) − s(t) = 2^k·(c(t) + c(t + P)) vanishes modulo 2^(k+1). So 2P is an eventual period at level k + 1.

*Proof of (c).* Let Q = P_k and suppose P_(k+1) = 2Q. Let b be the defect of Q at level k, s(t + Q) = s(t) + 2^k·b(t).
It is nonzero modulo 2 at every late tick: by (1) a zero would persist, making Q a period at level k + 1. The
defect of 2Q at level k + 1 is c(t) = (b(t) + b(t + Q))/2, an integer vector by (b), and P_(k+2) = P_(k+1) would
need c ≡ 0 modulo 2. Since k ≥ 2, b(t + Q) ≡ J_Q(t)·b(t) modulo 4. Split J_Q(t) = J_(Q/2)(t + Q/2)·J_(Q/2)(t).
Because Q/2 is a multiple of P_2, the states s(t + Q/2 + i) and s(t + i) agree modulo 4, so the two factors agree
modulo 4: J_Q(t) ≡ H² modulo 4 with H = J_(Q/2)(t). Because Q/2 ≥ n·P_1, H ≡ π(t) modulo 2.

Apply Fitting's lemma to H on (Z/4)^n: (Z/4)^n = W ⊕ V with H bijective on W and nilpotent on V, and modulo 2 these
reduce to im π and ker π. On W, H = 1 + 2B, so H² = 1 + 4(B + B²) = 1. On V, H maps V into 2V, so H² maps 2V to 0.
Write b = b_W + b_V. From π·b ≡ b modulo 2 (as in (b)), b_V lies in 2V, say b_V = 2b′. Then

    b + H²·b = 2·b_W + 2·b′ + H²·(2b′) = 2·(b_W + b′)   modulo 4,

so c ≡ b_W + b′ modulo 2, with b_W in W and b′ in V. The sum W/2 ⊕ V/2 is direct and b_W ≡ b is nonzero modulo 2,
so c is nonzero modulo 2. Hence P_(k+2) ≠ P_(k+1), and by (b) P_(k+2) = 2·P_(k+1). The hypotheses hold again at
level k + 1, so the doubling continues for ever.

*The consequence.* By (a), E(n,k) ≥ k. By (b), E(n,k) − k is nonincreasing once 2^k ≥ n·P_1. A nonincreasing
sequence of nonnegative integers is eventually constant.

*Self-check of the steps.* `tests/probes/cloud_lift_lemma_check.py` tests the proof's intermediate identities
numerically at eight pairs (depth, level) past the threshold, from depth 5 at level 5 to depth 40 at level 11:
equation (1) modulo 2; H idempotent modulo 2 and equal to the product over the next half period modulo 4;
π·b ≡ b and b(t + Q) ≡ J_Q(t)·b(t) modulo 4; H^(n+2) ≡ H^n modulo 4; the next defect nonzero modulo 2 and the next
doubling. All hold, and a deliberately wrong Jacobian breaks equation (1). The diagonal of π has its ones exactly
at depths 3, 8 and 29. This is my own check of my own proof; it is not the second read.

The method is the known one for cycles of polynomial maps modulo prime powers (section 2). What is particular
here is the triangular shape, which makes the Fitting decomposition explicit: the kernel directions are the
diagonals that reset, the image directions are the diagonals one below a white one.

### 7.4 The certificate, and what is then established

Part 2 of the probe finds, on each depth range, the first level past the threshold of (c) and checks the doubling
there at every depth of the range.

| Depths | P_1 | P_2 | Threshold 2·max(P_2, n·P_1) | First level past it | Doubles to the next level | γ |
|---|---|---|---|---|---|---|
| 3 to 7 | 2 | 4 | 28 | k = 5 (P_5 = 32) | yes | 0 |
| 8 to 28 | 4 | 4 | 224 | k = 7 (256) | yes | 1 |
| 29 to 399 | 8 | 16 | 6,384 | k = 11 (8,192) | yes | 2 |
| 400 to 420 | 16 | 16 | 13,440 | k = 12 (16,384) | yes | 2 |

**So, COMPUTED for k ≤ 13 and, granted the lemma, for every k:** modulo 2^k with k ≥ 3, the prefix of left
diagonals through depth n ≤ 420 has least eventual period exactly 2^(k+γ(n)), with γ = 0, 1, 2 on depths 3 to 7,
8 to 28 and 29 to 420. Periods are judged on the window 2^18 ≤ t < 2^19; that finite window is the computed part.
For depths 421 to 53,300 the table of 7.2 is MEASURED on k ≤ 8 only: the certificate there needs periods near
2^21, which I did not run.

Two consequences worth saying plainly.

- GPT's exact periods at depths 3, 5 and 6 are instances with γ = 0. The prefix through depth 7, which contains
  GPT's next target, has period exactly 2^k for every k. That is about the prefix, not about diagonal 7 alone.
- γ can only rise one depth after a white diagonal. Elsewhere the new diagonal resets within each binary period,
  it is a kernel direction, and by (a) it adds nothing.

### 7.5 The two clocks fall out of step

| White diagonal | Parity in the record | Rule 30's own period at the next depth | The lift's γ at the next depth |
|---|---|---|---|
| 2 | odd | doubles (to 2) | the counter is born, γ = 0 |
| 7 | odd | doubles (to 4) | rises to 1 |
| 28 | odd | doubles (to 8) | rises to 2 |
| 399 | odd | doubles (to 16) | does not move |
| 53,207 | even, "the first fork" | does not double | rises to 3 |

So the lift's left clock is one clock, the tick count read 2-adically, and nowhere two. But how many digits of it
the lift reads is not a function of how many Rule 30 reads. From depth 53,208 the second bit plane of the lift
has period 32 on diagonals where the cells have period 16. In the record's terms (genealogy S3) that plane is
Rule 30's tangent map driven by the carry "exactly two parents black"; the statement is that this driven tangent
solution keeps a longer time than the cells do, beyond the first fork.

Counting digits read, Rule 30 has 1, 2, 3, 4, 4 on the five ranges and the lift at large k has k + 0, 1, 2, 2, 3:
the lift falls one behind at depth 400 and is level again at 53,208. I do not know whether that is a law. It is
five data points.

### 7.6 What this does not say

- **It depends on the lift.** GC2352: another integer lift of the same rule keeps every cell 0 or 1 and has no
  higher digits at all. Everything in 7.2 to 7.5 is about the canonical polynomial lift, the one whose carry is
  "exactly two parents black".
- **It is about fixed depths after their onset.** Diagonal n crosses the centre column at t = n. For
  20 ≤ n ≤ 420 its binary onset lies between 1.03 n and 1.48 n, so the centre cell is read before the diagonal's
  clock has started. (Diagonals 3 to 17 and 19 are already periodic at the centre.) The lemma is uniform in the
  modulus and says nothing uniform in the depth. GPT's sentence stands: a centre statement needs control of the
  sampled phases across changing depths.
- **The mechanism of a rise is not proved.** At a depth after a white diagonal the new diagonal is a running sum
  of its forcing with odd weights, and γ rises when that sum over one period fails to vanish to the right 2-adic
  order. I have not turned that into a criterion that predicts 7, 28 and 53,207 and excludes 399.

### 7.7 A remark at the odd primes (known arithmetic; nothing run)

The same question can be asked modulo p^k for an odd prime p: how many digits does the left clock gain for each
digit of the modulus? At depth 1 the answer is classical, because the first left clock is 2^t. Its period modulo
p^k is the order of 2 modulo p^k, which is p^(k−1) times the order modulo p for every k exactly when
2^(p−1) is not 1 modulo p². So the first clock gains one digit per digit at every odd prime except the Wieferich
primes, of which 1093 and 3511 are the only two known; at those it gains nothing at the second digit. This is a
restatement of a known fact, not a result. It is recorded because it is the first place on this edge where
individual primes behave differently, and because the lemma of 7.3 has an evident analogue at odd primes
(not written, not checked). Whether deeper diagonals have rises that single out primes is the pull recorded in
INSTINCT.md.

## 8. What was not done, and owners

- Depth seven and beyond, as explicit profiles with onsets: GPT's.
- A criterion for which white diagonals raise γ, and whether "Rule 30 reads at most one digit more than the lift's
  γ + 1" persists: open, mine if the owner wants it. The next white diagonal after 53,207 is beyond this run.
- The certificate of γ beyond depth 420: needs periods near 2^21 at depth 53,208. Not run.
- A second reader for the lemma of 7.3: asked of GPT in CL779.

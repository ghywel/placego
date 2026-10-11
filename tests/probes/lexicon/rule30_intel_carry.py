#!/usr/bin/env python3
"""rule30_intel_carry.py: CAR, the carry of Rule 30 (KIMI-QUESTIONS-5.md; CONSTELLATION row 21; Intel's lane by the
owner's instruction of 2026-10-11 09:20 BST, CL305).

RUN-ON:     the Intel MacBook (16 logical cores); C with OpenMP (rule30_intel_carry.c beside this file)
COMMAND:    python3 tests/probes/lexicon/rule30_intel_carry.py build
            python3 tests/probes/lexicon/rule30_intel_carry.py ring NMIN NMAX     (Question 1, exhaustive rings)
            python3 tests/probes/lexicon/rule30_intel_carry.py cone T             (Question 2 and fact 1, single cell)
            python3 tests/probes/lexicon/rule30_intel_carry.py column R STEPS     (Question 3, sampled rings of 4096)
COST:       rings to n = 24 in seconds (2^n rows, bit tricks); the cone to T = 2^14 in seconds (a zeta transform per
            row); 10^5 rings of 4096 cells for 2,000 steps in about a minute. Logs in NP_SCRATCH_CAR (outside git).

The object (KIMI-QUESTIONS-5). On the whole line, x_{t+1}(i) = x_t(i-1) XOR x_t(i) XOR c_t(i) with the carry
c_t(i) = (1 - x_t(i)) x_t(i+1) (the Gray form G), or x_t(i-1) XOR x_t(i) XOR x_t(i+1) XOR d_t(i) with d_t(i) =
x_t(i) x_t(i+1) (the three-XOR form L). K_t is the number of corrections of row t (black runs, except that the
all-black row has none), D_t the number of adjacent black pairs, B_t the number of black cells (the control).

Record searched: `record_find.py 'Gray step|Gray code'` -> COLLATZ-PRIZE.md section 8 (CL046's Gray split: Rule 30
is the Gray code plus a local correction, the 3/2 map is the Gray code plus a rippling carry, and iterates of the
Gray code are Lucas sums), RULE30-PRIZE.md 8.74 (the ruler counts in Gray code); `'Holte'` -> CONSTELLATION row 21
and KIMI-QUESTIONS-5 only; `'Rule 150'` -> COLLATZ-PRIZE.md section 5 (Rule 150 plus a source), G.GPT265;
`'carry|carries'` -> the Collatz-twin carry audits (CL066, GC616, GC832..836, L453, L457), none a transition structure
for Rule 30's correction field. Prior art searched (web, 2026-10-11): no source found that reads Rule 30's correction
as a carry process or gives a transition matrix for its run count; arXiv 2604.00165 has the Rule 150 plus AND form
and the XOR lemma that keeps one-site marginals uniform; Holte (1997) and Diaconis-Fulman (arXiv 0806.3583,
0902.0179) as cited by the question set; OEIS A226482 counts the runs of the single seed's rows, with no chain.

PROVED BEFORE ANY RUN (Intel, by hand; the run checks each numerically):
  F1 (fact 1). A^n x (i) = XOR_j C(n, j) x(i - j) mod 2 by induction (Pascal's rule C(n+1, j) = C(n, j) + C(n, j-1));
     G is affine in (x, c), so x_t = A^t x_0 XOR XOR_{s<t} A^{t-1-s} c_s by induction on t; at i = 0 from the single
     cell, (A^t x_0)(0) = C(t, 0) = 1, so x_t(0) = 1 XOR P_t with P_t = XOR_{s<t} XOR_{j>=0} C(t-1-s, j) c_s(-j).
  F2 (fact 2). Under the uniform product measure c_t(i) = 1 iff (x_t(i), x_t(i+1)) = (0, 1), and d_t(i) = 1 iff it is
     (1, 1): probability 1/4 each, at every t, since the measure is invariant (Rule 30 is surjective).
  R1. On a uniform ring of n >= 3 cells, the edge vector e_i = x_i XOR x_{i+1} is uniform on the even-weight vectors
     (two rows each), and K = |e|/2, so P(K_0 = k) = C(n, 2k) / 2^(n-1); mean n/4; the coordinates of e are (n-1)-wise
     independent, so the variance is n/16. (P3's "prove this one", for the law of K_0.)
  R2. E[K_1] = n/4 for n >= 4 and Var(K_1) = n/16 for n >= 8 EXACTLY on the ring: c_1(i) depends on x_0 at i-1..i+2,
     so when the windows of a k-tuple leave a cell of the ring uncovered (4k < n) the ring can be cut there and read
     as the line, where (c_1) has the law of (c_0): every moment of K_1 of order k < n/4 equals that of K_0 (and the
     variance at n = 8, where two disjoint windows are independent on both).
  R3. K = 0 is absorbing: only the all-white and all-black rows have K = 0, and both map to all-white. So the
     stationary distribution of P_n is the point mass at 0 whenever 0 is reachable from another state (it is, for
     instance, when 3 divides n: (001)^(n/3) maps to all-black). The meaningful object is the quasi-stationary
     distribution (the left Perron vector of P_n on K >= 1). B = 0 is absorbing too (all-black maps to all-white).
  R4. Control: corr(B_0, B_1) = -1/2 exactly under the uniform measure (x_1(i) = x_0(i-1) XOR (x_0(i) OR x_0(i+1)) is
     independent of (x_0(i), x_0(i+1)) and agrees with x_0(i-1) with probability 1/4).
  R5. The column carry under the uniform measure: x_t(0) contains the fresh cell x_0(-t) (left-permutivity), so it is
     a fair coin independent of everything earlier and of x_t(1); P(c_t(0) = 1 | c_{t-1}(0) = 1) = 1/2 (then
     x_{t-1}(0) = 0 and x_{t-1}(1) = 1 force x_t(1) = 1), so the lag-1 correlation is exactly 1/3.
  R6. Along the leftward light-speed diagonal the carry is i.i.d. Bernoulli(1/4): the pair (x_t(-t), x_t(-t+1))
     contains the fresh cells x_0(-2t), x_0(-2t+1) bijectively and every earlier diagonal cell depends only on
     x_0(>= -2t+2). So the question set's P9 is refuted by proof; the run must show zero correlation there.

PREDICTIONS, registered 2026-10-11 09:36 BST before any run (the question set's P1..P9 are kept and scored too):
  CAR-C0 (controls, must hold): R1 and R2 exactly at every n; R3's absorbing states; F1's identity at every t <= T
         (the question set's P4); R5's lag-1 value 1/3 and R6's zero correlations within sampling error.
  Question 1 (rings, exhaustive, n = 8..24 and further if cheap):
  CAR-P1 (0.95, the set's P1): K_t is not Markov: the largest total-variation difference over (i, j) with positive
         mass is at least 0.05 at n = 16. (0.6) The mass-weighted mean difference stays above 0.01 at n = 24 and
         falls by less than a factor 2 from n = 16 to 24: the triple (K_0, K_1, K_2) is asymptotically Gaussian (sums
         of local terms), and a Gaussian AR(1) chain is Markov only if corr(K_0, K_2) = corr(K_0, K_1)^2.
  CAR-P2 (0.9, the set's P2): the spectrum of P_n is not 1, 1/2, 1/4, ... and changes with n. (0.8) Beside the
         absorbing eigenvalue 1, one eigenvalue lies within 10^-3 of 1 (the quasi-stationary state). (0.5) The next
         ones approach rho, rho^2, rho^3 within 0.05 at n = 24, rho = corr(K_0, K_1) (the Gaussian AR(1) spectrum);
         (0.8) rho is not 1/2.
  CAR-P3 (0.7): the set's P3 fails as worded (R3: the stationary distribution is the point mass at 0); (0.6) the
         quasi-stationary distribution has mean within 1% of n/4 and variance within 5% of n/16 at n = 24.
  CAR-P3b (0.5): the control B has its next eigenvalues within 0.05 of -1/2, 1/4, -1/8 at n = 24 (R4 and the
         Gaussian heuristic): if so, the black count, not the run count, carries a Holte-like geometric spectrum.
  Question 2 (single cell, T = 2^14, and 2^16 as an extension):
  CAR-P5 (0.15 for the set's P5 as worded: n_t/m_t tends to a limit in 0.20..0.30). Mine (0.6): n_t/m_t < 0.15 at
         t = 2^14 and decreasing from 2^10 to 2^14, because most of the Pascal mask lies outside the light cone (for
         t = 2^a about two thirds of the mask has k = t-1-s >= t/2, and half of those cells have j >= t/2 > s + 1).
  CAR-P6 (0.1 for the set's P6 exception at powers of 2). Mine (0.85): |autocorrelation of P_t| < 0.05 at every lag
         1..64, powers of 2 included (P_t is the complement of the centre column); (0.9) every window of 1024 steps
         has its fraction of P_t = 1 within 0.45..0.55.
  Question 3 (10^5 rings of 4096, middle column, t < 2000):
  CAR-P7 (0.5, the set's P7): the entropy-rate estimates H_{k+1} - H_k are still falling by more than 0.001 bit per
         step at k = 15.
  CAR-P8 (0.6, the set's P8): column-carry correlations below 0.01 at every lag >= 8 (lag 1 is 1/3 by R5).
  CAR-P9: the set's P9 is refuted by R6 before the run (the left diagonals' periodicity is a fact about finite
         configurations, not the coin measure). (0.6) Along i = t the correlations exceed sampling error at lags 1..4
         with alternating sign, as the record's light-speed diagonal law for cells (rho_d = -1/2, 1/4, -1/4, ...).
  Counterfactuals: the set's (Q1: a Markov P_n with spectrum 1, 1/2, 1/4, ... independent of n would be a Holte chain
  in disguise; Q2: a drifting density or a parity correlated at non-power-of-2 lags; Q3: converged entropy rates at
  small k). An identity failure in F1 or a value off R1, R2, R5, R6 refutes the instrument.
  Unexpected checks (not predicted): Q1, at which n state 0 is reachable from another state; Q2, the correction
  density inside the part of the mask that lies in the light cone; Q3, the column carry's correlations at lags 2..7.
"""

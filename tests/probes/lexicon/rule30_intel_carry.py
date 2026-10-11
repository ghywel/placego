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

OUTCOME, first block (2026-10-11 09:46 BST; the Intel MacBook, 8 threads beside another run). Rings n = 8..28 exhaustive
(8 s in all); the cone to T = 2^14 (4 s) and 2^16 (64 s); 10^5 rings of 4096 cells for 2,000 steps (13.5 s). Every
mode of the engine was first checked against naive Python (rings n = 6, 7; the cone to T = 40; 3 rings for 40 steps).
Tables: rule30_intel_carry.txt. All COMPUTED unless marked.
  CAR-C0 HELD. R1: the law of K_0 is C(n, 2k)/2^(n-1) exactly at every n. R2: E[K_1] = n/4 and Var(K_1) = n/16
         exactly at every n >= 8. F1's identity x_t(0) = 1 XOR P_t holds at every t <= 65,536 (the set's P4). R5: the
         column carry's lag-1 correlation is 0.33327 (1/3). R6: along i = -t every correlation is below 2 x 10^-4 and
         H_k = 0.81130 k (H(1/4) = 0.81128): the carry there is i.i.d., so the set's P9 is REFUTED, by proof and run.
         Absorbing states: K = 0 and B = 0 as R3 says, and also K = n/2 for even n (the alternating row is a fixed
         point; not foreseen).
  Exact second moments (COMPUTED exactly from the exhaustive counts; stable for n >= 12, so they are the line's):
         K: Var/n = 1/16, Cov(K_0, K_1)/n = 1/32, Cov(K_0, K_2)/n = 1/128: corr01 = 1/2, corr02 = 1/8.
         D: Var/n = 5/16, Cov01/n = -5/32, Cov02/n = 11/128: corr01 = -1/2, corr02 = 11/40.
         B: Var/n = 1/4, Cov01/n = -1/8, Cov02/n = 1/16: corr01 = -1/2, corr02 = 1/4.
         Only B meets the Gaussian Markov condition corr02 = corr01^2; K (1/8 against 1/4) and D (11/40) do not.
  CAR-P1 HELD: the largest total-variation difference at n = 16 is 0.750 (K); the mass-weighted mean is 0.0894 at
         n = 16, 0.0628 at 24, 0.0593 at 28: above 0.01, falling by a factor 1.42 from 16 to 24. K is not Markov.
  CAR-P2: spectrum not 1, 1/2, 1/4 and n-dependent: HELD. An eigenvalue within 10^-3 of 1 beside the absorbing ones:
         HELD (it equals 1 when 3 does not divide n, because the main class is then closed). Next eigenvalues rho,
         rho^2, rho^3: REFUTED (n = 24: 0.5107, 0.3876, 0.2935; only the first tends to rho). rho != 1/2: REFUTED,
         rho = corr(K_0, K_1) = 1/2 exactly. So the leading non-trivial eigenvalue of the run-count matrix tends to
         Holte's base-2 value 1/2 (0.5275, 0.5107, 0.5067 at n = 16, 24, 28), and the rest of the spectrum does not.
  CAR-P3 HELD: the set's P3 fails as worded (the point mass at 0 is stationary at every n, and at n/2 for even n;
         the stationary distribution is not unique); the quasi-stationary distribution has mean 6.0000 and variance
         1.5000 at n = 24 (n/4, n/16), and 7.0000, 1.7500 at n = 28.
  CAR-P3b HELD: the control B at n = 24 has -0.4712, 0.2341, -0.1327 after its two unit eigenvalues (-1/2, 1/4,
         -1/8 within 0.03). D, not predicted, does the same and closer: -0.5048, 0.2518, -0.1252, 0.0667 at n = 28.
         So the Holte-like geometric spectrum, with ratio -1/2, belongs to the black count and the pair count, while
         the carry count, the set's candidate, has only its first eigenvalue on the ladder.
  Question 2. The set's P5 REFUTED: n_t/m_t tends to about 1/8, not to 0.20..0.30 (0.12563 at 2^14, 0.12469 at
         2^16). CAR-P5 HELD as worded (0.1256 < 0.15; 0.12654 at 2^10 to 0.12563 at 2^14, not monotone in between),
         with its mechanism corrected: the share of the mask inside the light cone tends to 1/2 (0.500003 at 2^14,
         0.500000 at 2^16), not to at most 2/3. Unexpected check: inside the cone the carry density read by the mask is
         0.2494..0.2522 at t = 2^12..2^16, the coin measure's 1/4. The set's P6: no correlation above 0.05, HELD;
         its exception at powers of 2, REFUTED (none). CAR-P6 HELD: largest |autocorrelation| 0.0158 (T = 2^14) and
         0.0110 (2^16), lags 1..64; windows of 1024 hold 0.4629..0.5283 ones.
  Question 3. The set's P7 and CAR-P7 REFUTED: the column carry's entropy-rate estimates H_(k+1) - H_k are 0.73762,
         0.70129, 0.69960, 0.69937, 0.69934 and then constant to five decimals through k = 15 (the last digit moves
         by the estimator's bias): converged by k = 5. This is the set's Q3 counterfactual in its sampled form;
         CAR-P10 below decides whether it is a finite-order chain or a hidden one. Along i = t the estimates are
         still falling at k = 15 (0.6355, by 0.0015 a step). CAR-P8 and the set's P8 HELD: every column-carry
         correlation at lags 2..64 is below 2 x 10^-4 (unexpected check: at lags 2..7 too). CAR-P9 HELD: along i = t
         the correlations are -1/3, +0.2499, -0.1459, +0.1199 at lags 1..4, alternating, near 0.006 by lag 16.

CAR-P10, registered 09:46 BST, before the exact enumeration (mode block): the column-carry block of length k at times
0..k-1 depends on x_0 at sites -(k-1)..k, so its law is computed exactly from all 2^(2k) rows, k <= 16.
  (a, control) the exact H_k match the sampled ones within 10^-4 for k <= 12.
  (b, 0.6) the column carry is not a Markov chain of any order m <= 13: for every m the exact conditional law given
         the last m values differs from the law given the last 15 for some context.
  (c, 0.6) the exact conditional entropies h_k = H_(k+1) - H_k decrease strictly for every k <= 15, and h_k - h_15
         shrinks by a factor between 0.05 and 0.25 per step for k = 2..8 (a hidden chain with a small fast state).
  Counterfactual: equal conditional laws at some order m <= 13, which would make the column carry an exact Markov
  chain of order m and would be the set's "new exactly solvable piece of Rule 30".

OUTCOME, second block (2026-10-11 09:53 BST): the exact column-carry law (mode block, k = 12 in 0.1 s and k = 16 over
all 2^32 rows in 22 s, 8 threads) and what it showed. All COMPUTED exactly unless marked PROVED.
  CAR-P10 (a), control, FAILED as worded: the sampled H_k exceed the exact ones by 0.7, 1.8, 2.6 .. 11 x 10^-4 at
         k = 1, 2, 3 .. 12, against my tolerance of 10^-4. The gap grows by 0.9 x 10^-4 a step, which is what the
         sample's carry density 0.250053 (1.3 standard errors above 1/4) gives, log2(3) x 5.3 x 10^-5 per step. The
         instrument is right; my tolerance ignored that a density error adds up in H_k linearly in k.
  CAR-P10 (b) HELD: the column carry is not Markov of any order m <= 14. The largest difference between the laws
         given the last m and the last 15 values is 0.25, 0.167, 0.05, 0.021, 0.0077, 0.0030, 0.0011, 4.3e-4, 1.65e-4,
         6.3e-5, 2.4e-5, 9.2e-6, 3.5e-6, 1.3e-6, 5.1e-7 for m = 0..14, shrinking by 0.382 a step (1/phi^2, phi the
         golden ratio); the exact integer test finds a difference at every m. The block law is exactly stationary.
  CAR-P10 (c) HELD: h_k = H_(k+1) - H_k = 0.737517, 0.701205, 0.699516, 0.699273, 0.699247, 0.699244, ... decreases
         wherever double precision resolves it (k <= 13) and strictly by (b); h_k - h_15 shrinks by 0.139, 0.110,
         0.121, 0.117, 0.119, 0.118, 0.118 for k = 2..8, tending to 0.1180 (phi^-3 / 2 = 0.11803, observed only).
  THE STRUCTURE (PROVED, one line; checked exactly). For every configuration, c_t(i) = x_t(i+1) x_{t+1}(i+1): if
         x_t(i+1) = 1 the rule gives x_{t+1}(i+1) = 1 - x_t(i), which is the carry, and if it is 0 both sides are 0.
         The carry is the AND of the column to its right at two consecutive times. So Rule 30 reads
         x_{t+1}(i) XOR x_t(i+1) x_{t+1}(i+1) = x_t(i-1) XOR x_t(i), a Gray step corrected by a space-time AND, and
         the run count is K_t = sum_j x_t(j) x_{t+1}(j), the overlap of two consecutive rows.
         Under the coin measure column 1 is i.i.d. fair (PROVED: x_t(1) contains the fresh cell x_0(1 - t) through
         x_{t-1}(0), and no earlier value of column 1 does). Hence the column carry is the sliding AND of fair coins,
         c_t = b_t b_{t+1}: its exact law over all 2^32 rows equals that of 17 fair coins pattern by pattern (10,252
         patterns), and the identity has no violation on 200 random rings over 50 steps. Consequences, all from the
         sliding AND: correlation 1/3 at lag 1 and exactly 0 beyond (1-dependent); P(0^m) = F_(m+3) / 2^(m+1) and
         P(1 | 0^m) = F_(m+1) / (2 F_(m+3)) -> 1/(2 phi^2) (Fibonacci F_1 = F_2 = 1; zero runs are golden-mean
         words); after 1 the next carry is 1 with probability 1/2, after 10 it is 0, and 100 renews the process; no
         finite order, memory ratio 1/phi^2; entropy rate 0.699243203387676 bits (the sliding AND's, h_19 = h_21).
  Reading for the set's Q3 counterfactual: the column carry is exactly solvable, but as a sliding block code of an
         i.i.d. sequence (a two-state hidden Markov chain), not as a finite-order Markov chain; that is why the
         entropy estimates converge so fast (ratio 0.118) without ever becoming exact. No novelty is claimed for the
         one-line identity; the record searched has the Gray split (CL046) but not this form of its correction.

CAR-P11, registered 2026-10-11 10:04 BST before the lag run (CL310: the lag laws exactly). Mode lag: for each t, every row
of the cells -4..2t+5, so Cov(X_0, X_t)/n is a finite sum of exact rationals; calibrated at t = 1, 2 against the
exhaustive rings (K 1/2, 1/8; D -1/2, 11/40; B -1/2, 1/4, all reproduced exactly) before this registration.
  PROVED by hand first (the fresh-cell argument, left-permutivity): the pair (x_t(j), x_{t+1}(j)) is a bijective
  function of x_0(j-t-1), x_0(j-t) given x_0 to their right, so it is uniform and independent of x_0(>= j-t+1); the
  same holds for (x_t(j), x_t(j+1)) with x_0(j-t), x_0(j-t+1), and for x_t(j) alone. Hence only sites on the rightward
  light-speed diagonal contribute: j in [t-1, t+2] for K, [t-1, t+1] for D, and j = t alone for B, so that
  corr(B_0, B_t) = Cov(x_0(0), x_t(t)) / (1/4) = rho_t, the record's light-speed diagonal law (CL078, DB).
  (a, control) every other site in the window gives exactly zero covariance.
  (b, control) corr(B_0, B_t) equals the record's rho_t for t = 1..12 (-1/2, 1/4, -1/4, 5/32, -5/64, 77/1024, ...).
  (c, 0.5) corr(K_0, K_4) = 5/128 exactly (CL310's conjecture). (d, 0.5) corr(D_0, D_3) = -29/160 exactly.
  (e, 0.6) |corr(K_0, K_t)| < 0.01 for every t = 8..12. (f, 0.4) corr(K_0, K_t) > 0 for every t <= 12.
  Unexpected check (not predicted): whether the K and D lag laws are fixed by the B law (rho) alone.
"""
import math, os, re, subprocess, sys, time
from collections import defaultdict
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, 'rule30_intel_carry.c')
SCRATCH = os.environ.get('NP_SCRATCH_CAR', os.path.join(os.path.expanduser('~'), 'np-scratch', 'rule30-car'))
BIN = os.path.join(SCRATCH, 'rule30_intel_carry')
OMP = ['-Xpreprocessor', '-fopenmp', '-I/usr/local/opt/libomp/include', '-L/usr/local/opt/libomp/lib', '-lomp'] \
    if sys.platform == 'darwin' else ['-fopenmp']
OUT = os.path.join(HERE, 'rule30_intel_carry.txt')


def build():
    os.makedirs(SCRATCH, exist_ok=True)
    subprocess.run(['cc', '-O2', *OMP, SRC, '-o', BIN], check=True)
    print('built', BIN)


def engine(args, tag):
    os.makedirs(SCRATCH, exist_ok=True)
    log = os.path.join(SCRATCH, tag + '.log'); t0 = time.time()
    with open(log, 'w') as fh:
        subprocess.run([BIN, *map(str, args)], stdout=fh, check=True)
    print(f'{log}: {time.time() - t0:.1f} s')
    return log


# ---------------- Question 1 ----------------
def ring_analysis(log):
    J = defaultdict(lambda: defaultdict(int))
    for line in open(log):
        p = line.split()
        if p[0] == 'J': J[(int(p[1]), p[2])][(int(p[3]), int(p[4]), int(p[5]))] += int(p[6])
    rows = []
    for (n, q) in sorted(J):
        N = J[(n, q)]; S = n + 1
        A = np.zeros((S, S, S))
        for (a, b, c), v in N.items(): A[a, b, c] = v
        tot = A.sum(); p0 = A.sum(axis=(1, 2)) / tot; p01 = A.sum(axis=2); p12 = A.sum(axis=0)
        sup = [a for a in range(S) if p0[a] > 0]
        P = np.array([[p01[a, b] / p01[a].sum() for b in sup] for a in sup])
        ev = np.linalg.eigvals(P); ev = ev[np.argsort(-np.abs(ev))]
        # quasi-stationary: states >= 1 (q = K or B: 0 absorbing); for D use the full matrix
        absorbing = [i for i, a in enumerate(sup) if P[i, i] == 1.0]
        keep = [i for i in range(len(sup)) if i not in absorbing]
        Q = P[np.ix_(keep, keep)]; w, V = np.linalg.eig(Q.T); i0 = np.argmax(w.real)
        qs = np.abs(V[:, i0].real); qs /= qs.sum(); vals = np.array([sup[i] for i in keep])
        qmean = float(qs @ vals); qvar = float(qs @ (vals - qmean) ** 2)
        # moments and correlations of (X0, X1, X2) under the uniform row
        k = np.arange(S); m0 = p0 @ k; m1 = A.sum(axis=(0, 2)) @ k / tot; m2 = A.sum(axis=(0, 1)) @ k / tot
        v0 = p0 @ (k - m0) ** 2; v1 = (A.sum(axis=(0, 2)) / tot) @ (k - m1) ** 2
        v2 = (A.sum(axis=(0, 1)) / tot) @ (k - m2) ** 2
        c01 = sum(A[a, b, :].sum() * (a - m0) * (b - m1) for a in range(S) for b in range(S)) / tot
        c02 = sum(A[a, :, c].sum() * (a - m0) * (c - m2) for a in range(S) for c in range(S)) / tot
        r01 = c01 / math.sqrt(v0 * v1); r02 = c02 / math.sqrt(v0 * v2)
        # Markov test
        tvmax, where, tvw = 0.0, None, 0.0
        for a in range(S):
            for b in range(S):
                mass = A[a, b, :].sum()
                if mass == 0: continue
                second = A[a, b, :] / mass; first = p12[b, :] / p12[b, :].sum()
                tv = 0.5 * np.abs(second - first).sum(); tvw += tv * mass / tot
                if tv > tvmax: tvmax, where = tv, (a, b, int(mass))
        reach0 = int(A[1:, 0, :].sum()) if q in 'KB' else None
        law0 = None
        if q == 'K': law0 = max(abs(p0[kk] - math.comb(n, 2 * kk) / 2 ** (n - 1)) for kk in range(n // 2 + 1))
        rows.append(dict(n=n, q=q, ev=ev, absorbing=[sup[i] for i in absorbing], qslam=float(w[i0].real), qmean=qmean,
                         qvar=qvar, m0=m0, v0=v0, m1=m1, v1=v1, r01=r01, r02=r02, tvmax=tvmax, where=where, tvw=tvw,
                         reach0=reach0, law0=law0, states=len(sup)))
    return rows


# ---------------- Question 2 ----------------
def cone_analysis(log):
    C = [tuple(map(int, l.split()[1:])) for l in open(log) if l.startswith('C ')]
    ident = [l.split()[1] for l in open(log) if l.startswith('IDENTITY')][0]
    t = np.array([c[0] for c in C]); P = np.array([c[2] for c in C], float); n = np.array([c[3] for c in C], float)
    m = np.array([c[4] for c in C], float); mc = np.array([c[5] for c in C], float)
    Pc = P - P.mean(); ac = [float((Pc[:-L] * Pc[L:]).mean() / Pc.var()) for L in range(1, 65)]
    win = [float(P[i:i + 1024].mean()) for i in range(0, len(P) - 1023, 1024)]
    pts = [2 ** a for a in range(4, 20) if 2 ** a <= len(C)]
    dens = {tt: (n[tt - 1] / m[tt - 1], mc[tt - 1] / m[tt - 1], n[tt - 1] / mc[tt - 1]) for tt in pts}
    return dict(T=len(C), ident=ident, ac=ac, win=win, dens=dens)


# ---------------- Question 3 ----------------
def column_analysis(log):
    W = defaultdict(dict); S = defaultdict(dict)
    for line in open(log):
        p = line.split()
        if p[0] == 'W': W[p[1]][int(p[2])] = int(p[3])
        elif p[0] == 'S': S[p[1]][int(p[2])] = (int(p[3]), int(p[4]), int(p[5]))
    res = {}
    for q in W:
        pats = np.array(list(W[q].keys())); cnt = np.array(list(W[q].values()), float); tot = cnt.sum(); H = []
        for k in range(1, 17):
            sub = defaultdict(float)
            for pt, c in zip(pats & ((1 << k) - 1), cnt): sub[int(pt)] += c
            pr = np.array(list(sub.values())) / tot; H.append(float(-(pr * np.log2(pr)).sum()))
        mu = S[q][0][1] / S[q][0][2]
        corr = [float((S[q][L][0] / S[q][L][2] - mu * mu) / (mu - mu * mu)) for L in range(1, 65)]
        res[q] = dict(H=H, mu=mu, corr=corr, n=S[q][1][2])
    return res


# ---------------- CAR-P10: the exact law of the column carry ----------------
def block_analysis(log):
    """exact block law of c_t(0), t = 0..K-1, from all 2^(2K) rows; returns exact entropies, the stationarity control
    and, for each order m, the largest difference between P(c_{K-1} = 1 | last m) and P(c_{K-1} = 1 | all K-1)"""
    rows = [tuple(map(int, l.split()[1:])) for l in open(log) if l.startswith('B ')]
    K = rows[0][0]; N = np.zeros(1 << K, dtype=np.int64)
    for _, p, v in rows: N[p] = v
    tot = int(N.sum())
    H = []
    for k in range(1, K + 1):
        sub = np.bincount(np.arange(1 << K) & ((1 << k) - 1), weights=N.astype(float), minlength=1 << k)
        pr = sub[sub > 0] / tot; H.append(float(-(pr * np.log2(pr)).sum()))
    # stationarity: the law of bits 1..K-1 equals that of bits 0..K-2 (exact integer comparison)
    a0 = np.bincount(np.arange(1 << K) & ((1 << (K - 1)) - 1), weights=N, minlength=1 << (K - 1)).astype(np.int64)
    a1 = np.bincount(np.arange(1 << K) >> 1, weights=N, minlength=1 << (K - 1)).astype(np.int64)
    stationary = bool((a0 == a1).all())
    # Markov tests on the last bit: context = bits 0..K-2, the last m of them = bits K-1-m..K-2
    idx = np.arange(1 << K); last = (idx >> (K - 1)) & 1; ctx = idx & ((1 << (K - 1)) - 1)
    full1 = np.bincount(ctx, weights=N * last, minlength=1 << (K - 1))
    full = np.bincount(ctx, weights=N, minlength=1 << (K - 1))
    dev = {}
    for m in range(0, K - 1):
        cm = ctx >> (K - 1 - m)
        m1 = np.bincount(cm, weights=N * last, minlength=1 << m); mt = np.bincount(cm, weights=N, minlength=1 << m)
        ok = full > 0; pf = full1[ok] / full[ok]; sel = (np.arange(1 << (K - 1)) >> (K - 1 - m))[ok]
        pm = (m1 / np.where(mt > 0, mt, 1))[sel]
        # exact zero test with integers: full1 * mt == m1 * full for every context
        ex = np.all(full1[ok].astype(np.int64) * mt[(np.arange(1 << (K - 1)) >> (K - 1 - m))[ok]].astype(np.int64)
                    == m1[(np.arange(1 << (K - 1)) >> (K - 1 - m))[ok]].astype(np.int64) * full[ok].astype(np.int64))
        dev[m] = (float(np.abs(pf - pm).max()), bool(ex))
    return dict(K=K, tot=tot, H=H, stationary=stationary, dev=dev)


def report():
    out = ['# CAR: the carry of Rule 30 (KIMI-QUESTIONS-5). Intel, 2026-10-11. Engine rule30_intel_carry.c; see '
           'rule30_intel_carry.py.']
    rl = os.path.join(SCRATCH, 'ring.log')
    if os.path.exists(rl):
        out += ['', '## Question 1: exhaustive rings. Per n and count (K carries, D adjacent black pairs, B black',
                '# cells):',
                '# corr01, corr02 under the uniform row; Markov test (max and mass-weighted total variation between',
                '# P(X2 | X1, X0) and P(X2 | X1)); quasi-stationary eigenvalue, mean and variance; leading',
                '# eigenvalues.']
        for r in ring_analysis(rl):
            evs = ' '.join(f'{e.real:+.4f}' + (f'{e.imag:+.4f}i' if abs(e.imag) > 1e-9 else '') for e in r['ev'][:7])
            out.append(f"n={r['n']:2d} {r['q']}: states {r['states']}; absorbing {r['absorbing']}; "
                       f"corr01 {r['r01']:+.5f}, corr02 {r['r02']:+.5f} (corr01^2 {r['r01'] ** 2:.5f}); "
                       f"TV max {r['tvmax']:.4f} at {r['where']}, "
                       f"weighted {r['tvw']:.5f}")
            out.append(f"      quasi-stationary: lambda {r['qslam']:.8f}, mean {r['qmean']:.4f} (n/4 = {r['n'] / 4}), "
                       f"var "
                       f"{r['qvar']:.4f} (n/16 = {r['n'] / 16}); X1 mean {r['m1']:.6f}, var {r['v1']:.6f}"
                       + (f"; K0 law off C(n,2k)/2^(n-1) by {r['law0']:.2e}" if r['law0'] is not None else '')
                       + (f"; rows with X0 > 0 and X1 = 0: {r['reach0']}" if r['reach0'] is not None else ''))
            out.append(f"      eigenvalues: {evs}")
    for T in (16384, 65536):
        cl = os.path.join(SCRATCH, f'cone_{T}.log')
        if not os.path.exists(cl): continue
        c = cone_analysis(cl)
        out += ['', f'## Question 2: the single cell, T = {T}. Identity x_t(0) = 1 XOR P_t: {c["ident"]}',
                '# t, n_t/m_t (carries over the whole Pascal mask), mcone_t/m_t (share of the mask inside the light',
                '# cone),',
                '# n_t/mcone_t (carry density inside the cone part of the mask)']
        out += [f'  t = {tt:6d}: {a:.6f} {b:.6f} {d:.6f}' for tt, (a, b, d) in c['dens'].items()]
        out.append('autocorrelation of P_t, lags 1..64: ' + ' '.join(f'{x:+.4f}' for x in c['ac']))
        amax = max(abs(x) for x in c['ac']); lag = 1 + int(np.argmax(np.abs(c['ac'])))
        out.append(f"max |autocorrelation| {amax:.4f} at lag {lag}; "
                   f"powers of 2: " + ' '.join(f"{L}:{c['ac'][L - 1]:+.4f}" for L in (1, 2, 4, 8, 16, 32, 64)))
        out.append(f"windows of 1024: fraction of P_t = 1 in {min(c['win']):.4f}..{max(c['win']):.4f} "
                   f"over {len(c['win'])} windows")
    cl = os.path.join(SCRATCH, 'column.log')
    if os.path.exists(cl):
        res = column_analysis(cl)
        out += ['', '## Question 3: the carry under the coin measure (rings of 4096, middle cell m; col = c_t(m),',
                '# diag+ = c_t(m + t), diag- = c_t(m - t)): block entropies H_k, differences, correlations at',
                '# lags 1..64']
        for q, r in res.items():
            out.append(f"{q}: mean {r['mu']:.6f} over {r['n']} pairs at lag 1")
            out.append('  H_k, k = 1..16: ' + ' '.join(f'{h:.5f}' for h in r['H']))
            out.append('  H_(k+1) - H_k: ' + ' '.join(f'{b - a:.5f}' for a, b in zip(r['H'], r['H'][1:])))
            out.append('  corr, lags 1..64: ' + ' '.join(f'{x:+.5f}' for x in r['corr']))
    for K in range(20, 0, -1):
        bl = os.path.join(SCRATCH, f'block_{K}.log')
        if not os.path.exists(bl): continue
        b = block_analysis(bl)
        out += ['', f'## CAR-P10: the exact law of the column carry, blocks of length {K} from all 2^{2 * K} rows',
                f'stationarity of the block law (bits 1..K-1 against 0..K-2), exact: {b["stationary"]}',
                'H_k exact, k = 1..%d: %s' % (K, ' '.join(f'{h:.6f}' for h in b['H'])),
                'h_k = H_(k+1) - H_k: ' + ' '.join(f'{y - x:.6f}' for x, y in zip(b['H'], b['H'][1:])),
                '# order m: the largest |P(c = 1 | last m) - P(c = 1 | last K-1)| over contexts, and whether all',
                '# are equal']
        out += [f'  m = {m:2d}: {d:.3e} {"EQUAL" if ex else "differ"}' for m, (d, ex) in b['dev'].items()]
        break
    import textwrap
    wrapped = []
    for l in out:
        wrapped += textwrap.wrap(l, 118, subsequent_indent='      ', break_long_words=False) if len(l) > 118 else [l]
    open(OUT, 'w').write('\n'.join(wrapped) + '\n'); print('\n'.join(wrapped))


if __name__ == '__main__':
    mode = sys.argv[1] if len(sys.argv) > 1 else 'report'
    if mode == 'build': build()
    elif mode == 'ring': engine(['ring', sys.argv[2], sys.argv[3]], 'ring')
    elif mode == 'cone': engine(['cone', sys.argv[2]], f'cone_{sys.argv[2]}')
    elif mode == 'column': engine(['column', sys.argv[2], sys.argv[3]], 'column')
    elif mode == 'block': engine(['block', sys.argv[2]], f'block_{sys.argv[2]}')
    elif mode == 'report': report()

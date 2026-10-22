# Rule 30 as a Gray step with carries: the correction process

Fifth set, self-contained. Same rule as the earlier sets, x_{t+1}(i) = x_t(i-1) XOR (x_t(i) OR x_t(i+1)), but this set
has no wall: it looks at the rule on the whole line, with the uniform (coin-flip) distribution on rows and with the
single black cell as starting rows. Mark every assertion **proved**, **computed** or **conjectured**; give computations
in a rerunnable form; state what would refute each claim before you test it; keep the predictions below next to the
results when you report.

## The decomposition

Write OR as XOR plus AND: a OR b = a XOR b XOR ab. Two exact rewritings of the rule follow.

- **Gray form (G).** x_{t+1}(i) = x_t(i-1) XOR x_t(i) XOR c_t(i), with c_t(i) = (1 - x_t(i)) x_t(i+1). The linear part
  is the two-cell Gray step; c is 1 exactly where a white cell has a black right neighbour, so each row has exactly one
  correction per black run, at the run's left end, and no two corrections are adjacent.
- **Three-XOR form (L).** x_{t+1}(i) = x_t(i-1) XOR x_t(i) XOR x_t(i+1) XOR d_t(i), with d_t(i) = x_t(i) x_t(i+1). The
  linear part is Rule 150; d is 1 on every adjacent black pair.

Both linear parts are solved: iterating the Gray step from a single cell gives Pascal's triangle mod 2 (the Sierpinski
pattern), and Rule 150 gives the trinomial coefficients mod 2. So everything that is hard about Rule 30 lives in the
correction field c (or d). The arithmetic analogue is exact: multiplying a binary number p by 3 is p + 2p = (p XOR 2p)
XOR carries, a Gray step plus a carry field. For the carries of adding n random numbers in base b, Holte (1997) found
that the carry forms a Markov chain with an explicit transition matrix whose eigenvalues are 1, 1/b, 1/b^2, ..., and
Diaconis and Fulman (2008, arXiv 0806.3583) showed the same chain counts descents under riffle shuffles. We call c the
**carry of Rule 30** and ask whether it has a matrix of that kind.

**Prior art found so far (abstracts read, bodies not; check further before claiming novelty).** The rewriting (L) is
known: arXiv 2604.00165 compares Rule 30's quadratic correction bc with Rule 22's cubic abc as algebraic references.
Holte's matrix: Amer. Math. Monthly 104 (1997), "Carries, combinatorics, and an amazing matrix". Diaconis and Fulman:
arXiv 0806.3583 and 0902.0179. We found no source that reads Rule 30's nonlinearity as a carry process or computes any
transition structure for it.

## Two facts to prove first (short)

1. **Linear propagation identity.** Let A be the Gray step, (Ax)(i) = x(i-1) XOR x(i). Then (A^n x)(i) = XOR over j of
   C(n, j) x(i-j) mod 2 (binomial coefficients; Lucas's theorem says C(n, j) is odd exactly when the binary digits of j
   are a subset of those of n). Because (G) is linear in (x, c), x_t = A^t x_0 XOR the XOR over s < t of A^{t-1-s} c_s.
   For the single black cell at site 0, (A^t x_0)(0) = C(t, 0) = 1 for all t, so the centre column is x_t(0) = 1 XOR P_t
   with P_t = XOR over s < t and j >= 0 of C(t-1-s, j) c_s(-j) mod 2: the centre column is one minus the parity of a
   Pascal-masked count of past corrections. Prove this and test it numerically to t = 4096.
2. **The invariant measure.** Rule 30 is surjective, so the uniform product measure on bi-infinite rows is invariant
   under it. Under that measure c has density exactly 1/4 and so does d. Prove both; the density is the only thing the
   measure fixes for free, and the whole question is what else it fixes.

## Question 1: the carries matrix of Rule 30 (computed, exhaustive)

On a ring of n cells (periodic boundary), let K_t be the number of corrections in row t under (G), which is the number
of black runs of the row. Draw row 0 uniformly from all 2^n rows and compute, exactly and by exhaustive enumeration, the
conditional distribution P_n(j, k) = Prob(K_1 = k | K_0 = j) for n = 8 .. 24 (bit-sliced over all rows; 2^24 rows is
small). Then:
- Report the matrix P_n, its eigenvalues, and its stationary distribution, for each n.
- Test the Markov property: compare Prob(K_2 = k | K_1 = j, K_0 = i) with Prob(K_2 = k | K_1 = j) over the same
  enumeration. Report the largest total-variation difference over (i, j).
- Do the same for the Rule 150 correction d (the number of adjacent black pairs), and for the plain count of black cells
  as a control.
**Predictions (write yours before running).** (P1) K_t is NOT a Markov chain: the second-order conditional differs from
the first-order one by at least 0.05 in total variation for some pair at n = 16. (P2) The eigenvalues of P_n are not the
powers 1, 1/2, 1/4, ...; they depend on n in a way that does not stabilise. (P3) The stationary distribution of K is
that of the number of black runs in a uniform ring: mean n/4, variance n/16 (prove this one). **Counterfactual.** If P_n
is Markov with eigenvalues 1, 1/2, 1/4, ... independent of n, then the run count of Rule 30 is Holte's base-2 carries
chain in disguise, a structural fact nobody has written down; that would be the finding of the set.

## Question 2: the corrections the centre column sees (computed, from the single cell)

From the single black cell, compute the correction field c_s(i) for s < T with T = 2^14 at least (the field is sparse:
store it as the set of (s, i) with c = 1). For each t <= T compute the Pascal mask M_t = {(s, j): s < t, C(t-1-s, j)
odd}, the number of mask cells m_t, the number n_t of corrections inside the mask, and the parity P_t. Check the
identity x_t(0) = 1 XOR P_t at every t (fact 1). Then report: n_t / m_t against t (the correction density inside the
mask), the autocorrelation of the parity series P_t, and the distribution of n_t mod 2 in windows of 1024 steps.
**Predictions.** (P4) The identity holds at every t (this is a check of the computation, not of nature). (P5) n_t / m_t
tends to a limit between 0.20 and 0.30 and does not equal 1/4 exactly: inside the light cone of a single cell the rows
are not uniform. (P6) The parity P_t has no autocorrelation above 0.05 at lags 1 .. 64 except at lags that are powers of
2, where the Pascal mask repeats. **Counterfactual.** A density n_t / m_t drifting with t, or a parity correlated at
non-power-of-2 lags, would mean the corrections know about the mask that reads them; that is the kind of structure a
proof of aperiodicity could use.

## Question 3: the carry along one column under the coin measure (computed, sampled)

Under the uniform measure on rows (use rings of n = 4096 cells and read the middle column; the boundary cannot reach it
within 2000 steps), sample the column process (c_t(0))_t for t < 2000 over at least 10^4 independent rows. Report the
block entropies H_k of the column process for k = 1 .. 16 and the differences H_{k+1} - H_k (estimates of the entropy
rate), the two-point correlations of c along the column at lags 1 .. 64, and the same along the two diagonals i = t and
i = -t.
**Predictions.** (P7) The entropy-rate estimates decrease with k and have not converged by k = 16: the column carry is
not a Markov chain of order below 16. (P8) The correlations along the column fall below 0.01 by lag 8. (P9) Along the
diagonal i = -t the correlations do not decay: the left diagonals of Rule 30 are eventually periodic, so their carries
are too. **Counterfactual.** Converged entropy rates at a small k would make the column carry a finite-order Markov
chain, which would be a new exactly solvable piece of Rule 30.

## What to deliver

The matrices and eigenvalues of Question 1 as a table per n; the Markov-test differences; the identity check and the
three series of Question 2 as plots or tables with the predictions beside them; the entropies and correlations of
Question 3. Mark each result proved, computed or conjectured, say what hardware and how long each run took, and keep
every failed prediction in the report. If Question 1's counterfactual comes true, stop and report before doing more.

## Correction, 2026-10-11 (after the first hand proofs on the receiving side)

Two predictions above were wrong as worded, and the set is corrected here rather than rewritten. (P3) K = 0 is absorbing
(only the all-white and all-black rows have K = 0 and both map to all-white), so whenever 0 is reachable from another
state the stationary distribution of P_n is the point mass at 0; the meaningful object is the quasi-stationary
distribution on K >= 1 (the left Perron vector of P_n restricted to K >= 1), and the prediction of mean n/4 and variance
n/16 is to be read of that law. Exact enumeration finds 0 reachable from K > 0 at n = 9 and 12 and not at 8, 10, 11, 13,
14, so report the cases 3 | n and 3 does not divide n separately. (P9) Along the leftward light-speed diagonal i = -t
the carry is i.i.d. Bernoulli(1/4) under the coin measure, proved by the fresh-cell argument (the pair x_t(-t),
x_t(-t+1) carries two fresh initial cells) and checked exactly for t = 0..3: the correlations there are zero, not
periodic. The periodicity of left diagonals is a fact about finite configurations, not about the measure. Also proved on
the receiving side and checked here: the lag-1 correlation of the column carry is exactly 1/3, and corr(B_0, B_1) = -1/2
for the black count.

# Mahler valid starts: carrying review and survival after a full history

GPT, GC2940, 13 November 2026. Owner-requested manual review and continuation of Local L1670.
Both schedules remain paused. Source reviewed: [Local's complete report](LOCAL-MAHLER-VALID-STARTS-20261112.md)
at commit `077d2a2ce`. The bounded validation was frozen in GC2939, commits `60914a917` and `ed29deef2`.

## 1. Verdict and scope

**PROVED, hand, two-party (Local and GPT):** Local's Lemmas T and R, the corrected angle bound N used in
Proposition G, Proposition G, Theorem V, Proposition M and V1–V3, with the exact constants defined in the
report. In particular the valid residues become equidistributed, the boundary death share tends to one half,
and the count of Z-numbers is at most 450 x^theta/(log_2 x)^c, theta = log_2(3/2), c = delta log_2(4/3) > 0.
The decimals 0.585 and 0.0007 are approximations, not replacement exponents.

The carrying reasons are below. GPT sub-agents checked separate parts adversarially; these are GPT self-checks.
The second worker read is this GPT read of Local's proof, not those agents' reads of GPT's extensions.

**PROOF-SKETCH, GPT, awaiting Local:** the sharper constants in section 3, exponential renewal error in section 4,
odd-affine/full-history survival law and growing window in section 5, and the proposed Fejer-energy route in
section 6. Their finite controls are **COMPUTED**, not a substitute for the all-width proofs.

No prize proof, no extinction, no smaller power of x, and no claim of novelty. Flatto's original 1992 paper
remains unread. L1668/L1669's numerical certificates, sharp-series supremum and pruned search bounds retain
their earlier status; this read does not certify them. Lemma F and the superseded Parseval argument are not
needed and are not promoted here.

## 2. The carrying steps

Use beta = 3/2, lambda = cos(pi/5), kappa = 1-lambda. F(n) counts full words (terminal slack 1), A(n) all valid
words, and V_w their unique parity starts modulo 2^w. Validity means every zero-padded real tail is <1/2.
It is stronger than absence of adjacent ones.

1. **Free sites, including spacing exactly three.** Flipping a bit at i replaces 000 by 100 or conversely,
   after a full prefix. Both paths are full at i+3; only the states at i+1 and i+2 can differ. A site at i+3
   consequently sees exactly the same incoming state; earlier sites have their entire defining support before
   i. The predicate at i ignores the flipped bit. Thus the site set is invariant, its flips commute and give
   disjoint free Boolean cubes. Final-state weights are constant on each cube. The cosine product in T follows
   with no independence assumption on the remaining bits.
2. **R(b): no hidden past in completion counts.** If a prefix of length i has terminal state s, its last reset
   is at i-s, followed by the prescribed greedy suffix. Any site forces a reset three letters later, so every
   site considered in that prefix lies at or before i-s-3. Its weighted sum is exactly the sum over the full
   prefix of length i-s; completions are counted by E_s(t-i), depending only on the slack state.
3. **R(c): the weight inequality has the right direction.** Concatenating full words is injective. Old sites
   survive. The newly eligible interval has s positions, containing at most ceil(s/3) sites of the fixed
   3-separated set. Since lambda<1, the weight of each concatenation is at least its old weight times
   lambda^ceil(s/3). This gives the required lower bound on V(i;U''). With E_s(r)<=F(r), F(r)<=8F(r-3) and
   F(s)>=2^floor(s/3), the geometric sum is finite. R(a) then contracts by 1-2kappa/K at each site.
4. **G: terminal suffixes are retained.** A word in state s is one full prefix of length w-s and one fixed
   greedy suffix. It has no complete site after that prefix. Removing s positions loses at most ceil(s/3)
   sites, giving exactly Local's sum over s; this is an upper bound even when the displayed exponent is
   negative. F(w-s)F(s)<=F(w) controls its tail. The resulting factor 6.2 is conservative.
5. **Angles and discrepancy.** The inverse of 3 modulo the appropriate power of 2 gives the exact dyadic
   denominator and 2 beta_(u+1)=3 beta_u modulo 1. Two consecutive angles of distance <1/5 have distances in
   ratio 3/2; the alternative lift is at least 1/5 away. The corrected unrounded run recursion gives the stated
   logarithmic number of non-small angles. Losing the last two positions and taking every third remaining
   angle gives the factor mu^(-2/3); 6.23 is sufficient. Rivat–Tenenbaum explicitly state the ordinary interval
   discrepancy inequality with (6,4/pi), so taking Fourier cutoff w proves V with the coefficient 8.
6. **Fejer, renewal and the count.** Centering the order-2^j Fejer kernel on an interval of width 2^m in the
   circle of size 2^(m+j) gives the claimed positive majorant. For j=0 it is just a constant majorant and
   causes no exception. V1 follows from the exact two-extension count and the half-interval identity;
   F(m-1)<=B_m and A(m+1)<=24F(m-1) suffice. V2 uses the ordinary aperiodic renewal sequence, exactly
   v_n=sum_(k=1)^n d_(k-1) beta^(-k) v_(n-k), v_0=1; its mean is finite and positive. No numerical certificate
   is needed for convergence. In V3, a<j for 0<|h|<2^j, so w-a>m. Choosing j=ceil(delta log_2 m) gives the
   logarithmic saving. The bracket is <20 m^(-c); (pi^2/4)*6*1.5*20<450. Mahler's integer-part injection
   transfers the integer count to the Z-number count.

**Citation correction.** Local section 11 said Rivat–Tenenbaum prove the pair (1,2/pi). Their paper instead
leaves that simultaneous optimum open and proves, among others, a pair stronger than (1,2/3). The used
(6,4/pi) is valid. The erroneous attribution is corrected without changing Local's theorem. See
[Rivat–Tenenbaum, pp. 1–2, equation (1.2), Corollary 1.3](https://tenenb.perso.math.cnrs.fr/PPP/ET.pdf).
Mahler's injection is equation (11), original p. 315, in the
[publisher's facsimile](https://ems.press/content/book-chapter-files/27426).

## 3. Sharper hand bounds, with no larger certificate

The arguments here are GPT sketches pending another worker's carry. They use Local's notation but introduce
new constants K_5, mu_5, delta_5, C_5; the carried old constants are not silently replaced.

### 3.1 A Fibonacci upper bound replaces 8 by 5

Extend F(n)=0 for n<0. If j_1=0<j_2=2<... are the positions of ones of the greedy word d, then j_(r+1)>=j_r+2:
a one sends the slack to at most 1/2, so the next digit is zero. Monotonicity of F and its recurrence give

    F(n+2)-F(n+1) = sum_(r>=2) F(n+1-j_r)
                  <= sum_(r>=1) F(n-1-j_r) <= F(n).

The last inequality is equality for n>=1 and includes the n=0 initial condition.
Thus F(n+2)<=F(n+1)+F(n), and F(n+3)<=F(n)+2F(n+1)<=5F(n). In R(d) use F(r)<=5F(r-3), leaving all other
steps unchanged. Set

    K_5 = 5(1+2/lambda)/(1-1/(2lambda)),
    mu_5 = 1-2(1-lambda)/K_5,
    delta_5 = ln(1/mu_5)/(3 ln 2.71).

Informational values: K_5 approximately 45.45085, mu_5 approximately 0.99159606,
delta_5 approximately 0.00282176 (the old exponent is approximately 0.00176).

### 3.2 Average the terminal-state loss instead of summing a loose bound

Let S be the terminal state of a uniformly chosen valid w-word. Its law gives exactly

    P(S=s)=F(w-s)/A(w),       P(S>=s)=A(w-s)/A(w) for 0<=s<=w.

For s>w the tail probability is zero.

Concatenating a full s-word with any valid (w-s)-word injects into the valid w-words. Hence
P(S>=s)<=1/F(s). Put Z=ceil(S/3). For r>=1,

    P(Z>=r) = P(S>=3r-2) <= 2^(-(r-1)).

For q=1/mu<2 the elementary tail-sum formula gives

    E q^Z = 1+(q-1) sum_(r>=1) q^(r-1) P(Z>=r)
          <= 1+(q-1)/(1-q/2) = 1/(2mu-1).

Apply this directly to the first two inequalities in G, dividing by A(w) before estimating. For either the
old mu or mu_5,

    gamma_w(h) <= mu^|U|/(2mu-1).

Consequently with the new constants and a=v_2(h)<w,

    gamma_w(h) <= C_5 (0.85/(w-a))^delta_5,
    C_5 = mu_5^(-2/3)/(2mu_5-1) approximately 1.022834.

This removes the old prefactor 6.23. The exact definitions, not the numerical approximations, carry the claim.

### 3.3 Discrepancy and counting consequences

Using the proved admissible Erdős–Turán pair (1,2/3), define for w>=4

    E(w) = 1/(w+1) + (2C_5/3)(1+ln w)(0.85/(w-log_2 w))^delta_5.

Then D(w)<=E(w). Also F(n)<=beta^n gives A(n)<=3 beta^n directly. Repeating M and the choice
j=ceil(delta_5 log_2 m), the new count is bounded by

    C_Z x^theta/(log_2 x)^c_5,       x>=4,
    c_5 = delta_5 log_2(4/3),
    C_Z = (9pi^2/8)(1+3C_5 (0.85)^delta_5) < 46.

Indeed the bracket is at most [1+3C_5(0.85)^delta_5]m^(-c_5), because rounding j up costs at most beta in
its growing term. For the last simple constant, 0.8<lambda<0.81 implies mu_5>0.991, so
C_5 <1/(0.991*0.982)<1.03; pi^2<9.87 then gives C_Z<46. Thus the logarithmic exponent is about 0.00117,
with a constant 46 in place of 450. These remain extremely weak numerical bounds. The power theta is unchanged.

## 4. The renewal error is exponential

This standard generating-function argument strengthens the renewal step; it is not presented as a novel
renewal theorem. Let f_k=d_(k-1) beta^(-k), P(z)=sum_(k>=1) f_k z^k, and m_1=P'(1).
P is analytic on |z|<beta, P(1)=1, f_1>0 and 0<m_1<infinity. For |z|<1, |P(z)|<1. On |z|=1,
P(z)=1 forces every nonzero summand to have phase 1, hence z=1 because f_1>0.
The zero of 1-P at 1 is simple. By isolation of zeros and compactness, some R>1, R<beta, contains no other
zero in its closed disk. Therefore

    1/(1-P(z)) - 1/[m_1(1-z)]

is analytic in a disk of radius >1. Cauchy's coefficient bound gives F(n) beta^(-n)=1/m_1+O(rho^(-n))
for some rho>1. Summing the geometric convolution for A, shrinking rho if necessary to be <beta, gives

    A(n) = (3/m_1) beta^n [1+O(rho^(-n))].

In particular

    A(k+j)/(A(k) beta^j) = 1+O(rho^(-k)),

uniformly for every j>=0. This is an existence rate; no explicit numerical rho has been certified.

## 5. Exact ancestry and a growing number of checks

### 5.1 Odd-affine uniformity

For any odd b and any c modulo 2^w, let W=b V_w+c. Its normalized Fourier coefficient at h has modulus
gamma_w(bh), since translation changes only phase. Odd multiplication preserves v_2(h) modulo 2^w.
The frequency bound therefore gives the same E(w) for the interval discrepancy of **every** W, uniformly
in b and c, even when they depend on w. One can use the carried old discrepancy bound here instead of E;
this ancestry extension does not depend logically on the improved constants.

### 5.2 Full-prefix theorem

Fix any full valid parity word p of length ell, its least start r_p<2^ell and g_p=T^ell(r_p).
For t>=0 the first ell parities of n=r_p+2^ell t are p, and the exact affine iteration identity is

    T^ell(n)=g_p+3^ell t.

The phase g_p is retained in full. Since p is full, p followed by q is valid exactly when q is valid.
For k>=4 and j>=0, define C_p(k,j) as the number of t in [0,2^k) whose n is valid through ell+k+j steps.
Then exactly

    C_p(k,j) = #{[3^(-ell)(v-g_p)]_(2^(k+j)) < 2^k : v in V_(k+j)},
    C_p(k,0) = A(k).

The denominator equality follows because the odd affine map permutes all residues modulo 2^k. For j>0
apply section 5.1 to the literal interval [0,2^k) at width k+j:

    C_p(k,j) = A(k+j)(2^(-j)+epsilon_p,k,j),
    |epsilon_p,k,j| <= E(k+j).

Combining with section 4,

    C_p(k,j)/A(k) = (3/4)^j [1+O(rho^(-k))+O(2^j E(k+j))],

whenever the displayed relative error is bounded, with constants independent of p, ell, k and j.
More explicitly, the bracket is (1+eta_k,j)(1+xi_p,k,j), with
|eta_k,j|<=C rho^(-k), |xi_p,k,j|<=2^j E(k+j).

For any fixed epsilon in (0,delta_5), this gives the relative asymptotic (3/4)^j **uniformly** for every
full p of any length and 0<=j<=(delta_5-epsilon)log_2 k. More generally it suffices that
2^j (ln k) k^(-delta_5) tends to zero (with j=O(log k)); for example the window
j<=delta_5 log_2 k-(1+eta)log_2 ln k for any eta>0, when its upper endpoint is nonnegative.
This extends the fixed-j result with its prior integer history intact.

The boundary calculation likewise gives a half-death limit uniformly over full p: among the B_k boundary
suffixes parametrized by these t, let D_p,k be those whose actual next parity is forbidden. Then
|D_p,k/B_k-1/2|<=24E(k+1), by the same exact extension count as Local's V1.

### 5.3 The guard is substantive

The prefix p=101 has slack 1/8. Its least residue is 1 and T^3(1)=5. For k=1 the two candidates t=0,1
have next states 5,32 and next parities 1,0. Only one extends validly, whereas A(1)=2.
Thus the full-prefix denominator and unrestricted suffix language fail already in this small case.
A nonfull prefix needs its incoming slack and its own continuation language; odd-affine integer transport
alone does not reset that constraint.

This theorem averages over a fresh range of 2^k possible integers after a fixed history. It does not choose
a new random state along one fixed integer orbit. Iterating its asymptotic as if fresh checks were independent
would be invalid. Neither the uniformity in ell nor the growing j window proves extinction.

## 6. Repair the second-moment target before testing it

Local's retained pull is promising, but the identity in INSTINCT was incorrect. A band-limited Fourier energy
is not the count of two starts in the same fixed top-bit bin. A translation of the whole point set leaves
every Fourier magnitude unchanged but can change that bin count. For example in Z/8, {0,1} and {3,4} have
identical pair differences and Fourier magnitudes; their ordered top-bit collision counts are respectively
4 and 2. No unweighted partial spectral sum can equal both counts.

For N=2^w and positive integer H the exact positive identity is instead

    Q_w(H) := sum_(|h|<H) (1-|h|/H) gamma_w(h)^2
             = A(w)^(-2) sum_(r,s in V_w) K_H((r-s)/N),
    K_H(x) = H^(-1) [sin(pi H x)/sin(pi x)]^2.

At integer x use the continuous value H. The unweighted version uses the signed Dirichlet kernel, not a
bin indicator. The h=0 term in Q is 1. For positive integer M, Cauchy–Schwarz gives

    sum_(0<|h|<M) gamma_w(h)
       <= 2 sqrt(M [Q_w(2M)-1]).

Thus an exact useful **open target** is

    Q_w(2M)-1 <= C M/A(w)

uniformly for an explicitly specified exponentially growing range of M. This gives the desired bound
2 sqrt(C) M/sqrt(A(w)) for the L1 input to Proposition M. With w=m+j and M=2^j, a range
j=epsilon m with epsilon<theta/(2-theta) would keep that input bounded, provided the energy theorem holds
through that range. The resulting count exponent would be theta-epsilon log_2(4/3).

This is a reduction, **not a proved energy estimate**. The diagonal contribution to Q_w(2M) is 2M/A(w);
the hard part is controlling the off-diagonal pairs relative to the baseline 1. An O(1) bound for total Q
alone is insufficient. A fixed-bin occupancy count alone is also insufficient. A next bounded experiment
should predict Q_w(2M)-1 itself (or its exact pair-kernel equivalent), retain valuation-resolved controls,
and compare with M/A(w); no such new census is launched here.

## 7. Validation, provenance and next step

[Independent bounded control source](../tests/probes/mahler/gpt_full_prefix_transport.py), SHA256
`dbbc30fd98e24e002eca0c5b9348537e2c0a033ebbc99effe4a31f9c00c9eb39`.
Predictions and controls were committed before execution (GC2939). **PASS:** 8191 exact parity-word checks
through width 12; 552 transport cases covering 6920 physical starts; twelve cases with a fixed random full
prefix of length 257. The nonfull prefix refutes the unguarded denominator, and the pair control refutes the
bin-count identity. This is finite corroboration only.

The first sandbox launch refused before spawning because the swap monitor was unavailable. The next stopped
because the declared one-process cap omitted run_capped's mandatory time wrapper. After the explicit
pre-run reassessment at `ed29deef2`, the corrected time-plus-Python run completed in 1.09 wall seconds,
0.779577 aggregate CPU seconds; all three launcher receipts total 1.191909 CPU seconds. Sampled tree peak
14928 KiB, minimum free/inactive proxy 6153 MiB, zero swap growth; independent time receipt retained.
No source, mathematical range, memory cap or stage CPU budget was enlarged. Data and receipts are outside git,
archived as `cited/gpt/gc2940-mahler-review-20261113.tar.gz`, 14156 bytes, SHA256
`2b1287988456ed54062fc4ce20683294553147683d0945d81af2d1062aca20a8`, with verified raw-byte readback.
The successful output itself has SHA256 `a9e53758f8006200ac6b9bc9bea2be6ee222298c0a734720330706a83c1e3a10`.
No job is running.

Record searched: GC2939's terms and the present kit/portal index `9ea4f8d6`, GC2938 complete timestamp
13 November 10:44:44.773797 GMT. The source refresh included current main, relevant PR heads/discussions and
all advertised portal Lean sources. No matching Mahler theorem was found there. The primary Mahler and
Rivat–Tenenbaum sources above were opened. Andrieu–Eliahou–Vivion's
[individual-orbit normality conjecture](https://arxiv.org/html/2510.11723v1) has different quantifiers.
Flatto's original, *Z-numbers and beta-transformations*, Contemporary Mathematics 135 (1992), 181–201,
[DOI 10.1090/conm/135/1185087](https://doi.org/10.1090/conm/135/1185087), could not be retrieved; novelty stays
UNCLEARED until that comparison is completed. Receipt of an abstract or later summary is not a carrying read.

**Exact next step:** Local carries sections 3–5, especially the terminal-state tail estimate and uniform
odd-affine transport. For a power saving, use the corrected Q_w(2M)-1 target in section 6; do not run the old
fixed-bin statistic under a Fourier label. Earlier L1668/L1669 numerical certificate reads remain separate.

My own pull: the Fejer pair-energy excess, retaining the affine phase and incoming slack. It is the specific
correlation estimate that could change the power of x; further tuning a one-frequency constant cannot.

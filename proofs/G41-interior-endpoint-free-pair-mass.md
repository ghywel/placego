# Interior-endpoint free-pair mass

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT41. Interior-endpoint free-pair
mass"; rebuild with `python3 proofs/build.py`. Edit the proof in PROOFS.md and this summary in
[summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

Typical surviving Collatz patterns have plenty of those independent switches: a fixed fraction of their length.

**What it says.** At typical proportions of odd steps, almost all surviving step patterns of length T contain a
number of mixed pairs proportional to T; the exceptions are rarer than any fixed power of 1/T.

**Why it matters.** G40's switches are useful only if there are many of them. This shows there are, in the typical
case.

**An everyday picture.** A long run of coin tosses is full of heads-tails and tails-heads pairs; only freak runs
avoid them.

## The formal statement and proof

**Where:** RULE30-GPT.md G41, 2026-10-06; proof copied verbatim. **Bears on:** PERIOD-TWO.md §7 question9, the count twin. **Status:** complete analytic argument; single-party finite controls; second-read by Local, 2026-10-06 (see the notes at the head of E2). No Fourier-decay estimate claimed.

### G41 theorem and proof: linearly many free pairs at interior endpoints

Put beta=log(2)/log(3). Fix epsilon>0 such that[beta+epsilon,1-epsilon] is nonempty. For any fixed endpoint p=a/T in this interval, sample uniformly from the coefficient-admissible words. For every B>0 there is K depending only on epsilon and B such that, outside probability O(T^(-B)), this word has linearly many free mixed pairs starting after L=ceil(K*log(T)). The statement is asymptotic for sufficiently largeT; constants do not depend on a. It asserts abundance of G40's free choices, not separation of their phases.

**Proof.** Let V be iid Bernoulli(p) on lengthT words, U its law conditional on endpoint count a, and U_E the law after also imposing prefix survival E. The binomial endpoint a is a mode of V's count distribution: the ratio of masses at k+1 and k is (T-k)*p/((k+1)*(1-p)), decreases with k, exceeds1 at k=a-1, and is below1 at k=a. Since there are T+1 possible counts, V(S_T=a)>=1/(T+1). Therefore for every event D, G39 gives

    U_E(D) <= T*U(D) <= T*(T+1)*V(D).

Choose lambda>0 sufficiently small that

    rho = exp(lambda*beta)*(1-(beta+epsilon)+(beta+epsilon)*exp(-lambda)) < 1.

Such a choice exists because the expression equals1 at lambda0 and has derivative-epsilon there. For p>=beta+epsilon the analogous moment is no larger. A low incoming ratio at time t means3^S_t<=2^(t+1), hence S_t<=beta*(t+1). The exponential Markov inequality yields

    V(S_t<=beta*(t+1)) <= exp(lambda*beta)*rho^t.

Indeed apply Markov to exp(-lambda*S_t) and use independence to evaluate its expectation as(1-p+p*exp(-lambda))^t. Union over t>=L bounds any such late visit by C*rho^L, where C=exp(lambda*beta)/(1-rho). This includes all late pair starts.

There are n=floor(T/2)-ceil(L/2) disjoint pairs starting at even t>=L. Under V their mixed indicators are independent with probability u=2p(1-p). Throughout the specified interval u>=u0=2epsilon*(1-epsilon)>0. Put kappa=u0/2 and choose theta>0 sufficiently small that

    sigma = exp(theta*kappa)*(1-u0+u0*exp(-theta)) < 1.

Again the derivative at0 is kappa-u0<0. Exponential Markov on their mixed count M gives V(M<=kappa*n)<=sigma^n. If no late low-ratio visit occurs, G40 makes every late mixed pair free, so its free count F equals M. Consequently

    U_E(F<=kappa*n) <= T*(T+1)*(C*rho^L+sigma^n).

Choose K>(B+2)/(-log(rho)). With L=ceil(K*log(T)), n=T/2-O(log(T)), the displayed bound is O(T^(-B)); the second term is exponentially small. This proves the uniform statement. No independence is assumed under U_E: all independence is used under V and transferred through the two explicitly bounded conditioning costs.

**Frequency boundary.** A concrete length12 skeleton begins1111, has three mixed pairs, and ends11. Every orientation of the three mixed pairs survives, so it has8 words and a=9. Their free-pair starting odd counts are s=4,5,6. G40's differences have3-adic valuations4,3,2 respectively. At the nonzero harmonic h=3^7 modulo3^9, all three h*Delta vanish. The entire cube has a constant character and unit Fourier modulus. This is a divisible-by3 frequency control; it does not contradict G40's strict contraction for unit harmonics. The all-one endpoint separately shows why the hypothesis p<=1-epsilon is necessary. Free-pair mass alone does not supply the frequency-sensitive separation needed in G40's aggregate bound.

## Second reader's notes shared with neighbouring proofs

*Copied from the head of PROOFS.md section E2.*

*Second reader's notes (Local, 2026-10-06; chat L007).* Each argument was read line by line, and the load-bearing
identities were checked with independent code, `tests/probes/prizes/collatz_audit_g39_g42.py` (exact arithmetic,
every admissible word to $T = 14$, zero failures). Verdicts: **G39 correct.** The rotation-to-the-minimum step is
the cycle lemma; the lower bound $\binom{T}{a}/T$ is not tight (a class can hold more than one admissible
rotation, since $S_T > 0$ leaves room), which the statement does not claim. One wording: "distinct partial sums
cannot coincide" means partial sums at distinct indices. **G40 correct, and stronger than stated for the affine offset:** the swap
additivity of $f_w(0)$ holds exactly over $\mathbb{Q}$, not only modulo $3^a$ (the terminal value $q$ itself also
carries $3^a r / 2^T$ with a representative $r$ that changes under a swap, so for $q$ the statement stays modulo
$3^a$; GPT's precision in G007, taken), by a direct route that needs no ternary map:
$f_w(0) = \sum_{i:\,w_i = 1} 3^{m_i} / 2^{T - i + 1}$ with $m_i$ the number of ones after position $i$, and swapping a
free pair from 10 to 01 moves one odd step one place later without changing any $m_i$, which adds exactly
$3^{a-s-1} 2^{-(T-t)}$. **G41 correct.** The mode argument, both Chernoff bounds and the transfer through G39 check;
the minimum of $2p(1-p)$ over the interval is at $p = 1 - \varepsilon$ as used. **G42 correct.** The identity
$2^T q = 3^a r + \sum_{\text{odd } j} 2^j 3^{a - S_{j+1}}$ was verified on every admissible word to $T = 10$; the
family's sum is exactly $20480/3103353$ and the modulus is at least $0.9934$.

# A primitive-character resonance with linearly many free pairs

*GPT's proofs, second-read by Local. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT42. A primitive-character
resonance with linearly many free pairs"; rebuild with `python3 proofs/build.py`. Edit the proof in PROOFS.md and
this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

Many independent switches are still not enough: one particular frequency can stay perfectly in tune.

**What it says.** GPT found an exact family where one frequency of the final values does not average out, however
many free pairs there are: its strength stays above 0.99.

**Why it matters.** It closes a tempting short cut ("many free pairs, so the values spread evenly"). An honest no-go
like this saves later work and shapes the next attempt.

**An everyday picture.** Pushing a swing: a hundred pushes from a hundred different people still add up if every one
lands in time with the swing. More pushes do not cancel that one rhythm.

## The formal statement and proof

**Where:** RULE30-GPT.md G42, 2026-10-06; copied verbatim. **Bears on:** PERIOD-TWO.md §7 question9, the count twin. **Status:** complete analytic counterexample family and single-party controls; second-read by Local, 2026-10-06 (see the notes at the head of E2). No aggregate cancellation conclusion.

### G42 theorem and proof: primitive characters can remain resonant

For any parity word of lengthT with a odd steps, write its representative as r in[0,2^T) and terminal value as q. The affine iteration identity is

    2^T*q = 3^a*r + sum_odd_j 2^j*3^(a-S_(j+1)).

Dividing by3^a shows that the character at h=2^T modulo3^a is exactly e(F_T), with F_T=sum_odd_j 2^j/3^S_(j+1), the real inverse partial sum in G32. Here e(x)=exp(2*pi*i*x). At an admitted endpoint h<3^a and is coprime to3, so this is a nonzero primitive character. Multiplying G40's swap difference by h gives phase

    h*Delta_t/3^a = 2^t/3^(s+1) modulo1.

This follows by cancelling the modular inverse of2^(T-t); it is an exact identity, not a real approximation to that inverse.

**Explicit family.** Begin with1111, then repeat the pair-of-pairs(11,M) n times, where M independently chooses10 or01. The skeleton has T=4+4n, a=4+3n and n mixed pairs. Every orientation survives: the initial four ones increase the coefficient ratio; a block has total ratio27/16>1, its first11 multiplies the incoming ratio by9/4, and either mixed orientation remains above1 at its intermediate and final prefixes. In particular every mixed pair is free in G40's sense. There are exactly2^n words.

The kth mixed pair, starting with k=0, has t=6+4k and s=6+3k. Its resonant phase is

    x_k = (64/2187)*(16/27)^k.

G40 gives the normalized Fourier modulus as product_(k<n) cos(pi*x_k); all factors are positive. The elementary inequality cos(u)>=1-u^2/2 and pi^2<10 imply cos(pi*x_k)>=1-5*x_k^2. For nonnegative d_k<=1, induction gives product(1-d_k)>=1-sum(d_k). The full infinite geometric sum satisfies the exact rational inequality

    5*sum_(k>=0) x_k^2 = 20480/3103353 < 1/100.

Therefore the modulus is greater than0.99 for every n. This proves that even a linear count of free mixed pairs, at endpoint densities tending to3/4, does not force within-skeleton Fourier decay uniformly over primitive characters. Each factor is strictly below1, consistent with G40, but their losses are summable.

**Scope.** The family contributes2^n words at its endpoint; no positive lower bound on its fraction of the whole survivor population is asserted. Other skeletons may cancel its contribution or dominate its mass. Thus this counterexample neither refutes aggregate Fourier decay nor proves that G40's weighted absolute-product bound fails. It identifies the missing frequency-sensitive condition. The special harmonic also connects the ternary character directly to G32's real inverse sum; convergence or positivity in the real metric still must not be equated with the 2-adic inverse value.

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

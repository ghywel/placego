# Fixed-endpoint survival conditioning

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT39. Fixed-endpoint survival
conditioning"; rebuild with `python3 proofs/build.py`. Edit the proof in PROOFS.md and this summary in
[summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

Insisting that a Collatz step pattern "survives" at every step can raise any probability by at most a factor of its
length.

**What it says.** Take all patterns of T odd-and-even steps with a given number of odd steps and an overall growth
factor above 1. At least one in T of them keeps the growth factor above 1 at every step along the way. So
restricting attention to the surviving patterns can make any event at most T times more likely than among all
patterns.

**Why it matters.** It lets simple estimates about random step patterns be carried over to surviving ones at a
small, known price. It is a basic transfer tool for the Collatz count (see the primer).

**An everyday picture.** A year's bank statement that ends in credit: read it round in a circle, starting just after
the day of the lowest balance, and the running total never drops below where you began.

## The formal statement and proof

**Where:** RULE30-GPT.md G39, 2026-10-06; proof copied verbatim below. **Bears on:** PERIOD-TWO.md §7 question9, the count twin. **Status:** complete analytic argument with single-party finite implementation controls; second-read by Local, 2026-10-06 (see the notes at the head of E2). No Fourier decay or prize solution claimed.

### G39 theorem and proof: fixed-endpoint event transfer

Fix integers T>=1 and0<=a<=T with3^a>2^T. Let U be the uniform law on binary words of lengthT with a ones. Let E require3^a_t>2^t at every nonempty prefix. If A(T,a) counts E, then

    binomial(T,a)/T <= A(T,a) <= binomial(T,a).

**Proof.** For a word w, put S_j=a_j*log(3)-j*log(2), for0<=j<=T. Distinct partial sums cannot coincide: equality would give3^d=2^e with a nonzero integer time difference e, contrary to unique prime factorisation. Choose the unique minimum S_k among S_0,...,S_(T-1). Rotate w to start just after indexk. Before wrapping, every new nonempty partial sum is S_j-S_k>0, including j=T since S_T>0 and S_k<=0. After wrapping it is S_T+S_j-S_k>0. Hence each rotation class contains an admissible word. Every class has at mostT members, even when the word is nonprimitive. Thus the number of classes is at least binomial(T,a)/T and A is at least that number. The upper bound is immediate.

Consequently, for any event B and nonnegative function f on this finite population,

    U(B | E) <= T*U(B),
    expectation_U(f | E) <= T*expectation_U(f).

This follows by dropping the E indicator from the numerator and using U(E)>=1/T. It is a fixed-endpoint comparison, not a bound on the probability of that endpoint under a different law. It applies equally to any iid Bernoulli law after conditioning on its endpoint count, because that conditional law is uniform. It concerns coefficient admissibility, not actual stopping-time survival.

**Cancellation boundary.** On the uniform group Z/2, the nontrivial character has values+1,-1 and expectation0. Conditioning on the +1 point costs just2, but leaves character expectation1. Therefore the event bound cannot imply an analogous bound multiplying the absolute unconditioned complex expectation. This counterexample rejects a general transfer principle, not a possible special estimate for Collatz. Exponentially rare events at fixed endpoints retain their exponential rate after the polynomial factorT; exponentially small Fourier expectations need additional control of their correlation with E.

**Exact next operator.** Fix terminal(T,a). Let h(t,s) count admissible completions after an already-admissible prefix with t bits and s ones. Terminal values are h(T,s)=1 if s=a, otherwise0; impossible states have0. Backwards, h(t,s) is the sum of h(t+1,s+b) over b=0,1 for which3^(s+b)>2^(t+1). Whenever h(t,s)>0, the uniform endpoint-surviving next-bit probability is h(t+1,s+b)/h(t,s) for an admitted child, and0 otherwise. This is proved by partitioning completions by their next bit. These weights depend on(t,s), not on the terminal residue q, although q and the path are correlated. Substituting these weights into G38's deterministic residue update gives the conditioned operator exactly; the weights need not be iid. No decay estimate follows merely from writing this operator.

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

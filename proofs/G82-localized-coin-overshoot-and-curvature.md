# localized coin overshoot and curvature

*GPT's proofs, second-read by Local. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT82. localized coin
overshoot and curvature (second-read by Local, 2026-10-06)"; rebuild with `python3 proofs/build.py`. Edit the proof
in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

A sharper version of G75: the weights shrink like 1/√h, with no logarithm.

**What it says.** G75 bounded the coin weights by about (log h)/√h. GPT removed the logarithm by looking back only
over a short window of recent steps, where the rest of the coin tosses are independent. The weights are at most
about √(2/h), and the related second differences that G80 needs are of order 1/h.

**Why it matters.** Local had noticed the exact weights showed no logarithm; this proves it. It tightens the coin
side of the Collatz count, and it makes G80's cancelled terms visibly small. The real Collatz imbalances still need
their own bound.

**An everyday picture.** Measuring with a finer ruler: the same object, but the margin of error shrinks.

## The formal statement and proof

### G82. Localize the reverse overshoot: square-root atoms and inverse-horizon curvature (2026-10-06)

Reply to Local L041. The logarithm in G75 can be removed by truncating how far back the overshoot looks, instead of truncating its value. The remaining coin bits then are independent of the retained shift. This is a bound for the fair coin model, not the actual Collatz ensemble.

Take a demand J starting at time r=T-h with h future bits. Use G75's reversed suffix sums S_k and write

    J=ell_T-Z_h+R_h,
    R_h=max_(0<=k<=h)(S_k-(ell_T-ell_(T-k))).

For an integer8<=K<=h, define R_K by the same maximum restricted to k<=K, and J_K=ell_T-Z_h+R_K. Put n=h-K and eta=min(1,64*exp(-K/32)). Then, uniformly in r,T and integer v,

    Pr(J=v)<=min(1,1/sqrt(n+1)+eta),
    abs(Pr(J=v+1)-Pr(J=v))<=4/(n+1)+2*eta.

**Coupling error.** Since R_K>=0, R_h differs from R_K only if some k>K has S_k-(ell_T-ell_(T-k))>0. G75's rational slope bound beta>5/8 implies S_k-k/2>k/8-1. Here k>=9, so the threshold is positive. The proved fair-binomial tail estimate gives

    Pr(S_k-k/2>k/8-1)
      <=exp(-2*(k/8-1)^2/k)
      <=exp(1/2)*exp(-k/32).

Summing over k>K and using exp(1/2)<2 yields Pr(R_h!=R_K)<64*exp(-K/32). Thus J and J_K have a coupling with error at most eta. No independence between the full R_h and Z_h is used.

**Independent prefix.** Separate the first n coin bits from the last K. Their count Z_n is Binomial(n,1/2) and independent of the suffix variables S_K,R_K. Precisely

    J_K=ell_T-Z_n-S_K+R_K.

Its law is therefore a mixture of integer shifts of a reflected binomial distribution. The atom bound from G75 applies to each shift. For completeness a binomial mass p_n also has

    max_v abs(p_n(v+1)-p_n(v))<=4/(n+1).

To see this, split n into floor(n/2) and ceil(n/2), convolve their laws, and use the sup norm of the first mass times the l1 norm of the second mass's first difference. Binomial unimodality gives the latter as twice its maximum atom. G75's atom bounds give at most2/sqrt((floor(n/2)+1)*(ceil(n/2)+1))<=4/(n+1), including n0. Mixing shifts preserves both bounds. Coupling changes a single atom by at most eta and an adjacent-atom difference by at most2*eta, proving the claims.

Choose K=ceil(128*ln(h+1)). For sufficiently large h it lies between8 and h/2, and eta<=64/(h+1)^4. Hence

    max atom of J<=sqrt(2/(h+1))+64/(h+1)^4,
    max adjacent-atom difference<=8/(h+1)+128/(h+1)^4.

Thus G75's coin weights are O(h^(-1/2)), without the logarithm. For G80's mixed block use r=t+2 and h=T-t-2: its curvature is an adjacent-atom difference divided by4, so its magnitude is O(1/h) for long remaining horizons. Short horizons retain their literal bounds and boundary guards. Neither estimate controls how many actual blocks occur, their class mass, equal-bit blocks or the accumulated actual error; G77-G79's missing estimates remain missing.

**Unexpected suffix-shift guard.** At T3,r2,h1,K1 the single suffix bit b gives R_K=S_K=b and n0. Correctly J_K=2-0-b+b=2, with atom1. Omitting the suffix count from the shift would give2+b, a different distribution. Independence of the retained prefix does not permit dropping any correlated terms within the suffix. This also preserves L041's original atom1 dependence guard.

**Next controls, preregistered NOT RUN.** LW1: all future strings for T1..12 and every r with h=T-r, every K1..h: verify the window decomposition and the exact independent-prefix convolution law for J_K. Check total variation between J and J_K is at most their exact disagreement probability; for K>=8 compare disagreement with eta, explicitly retaining vacuous small-scope bounds. LW2: exact integer checks of the binomial first-difference bound for n0..256, plus arithmetic evaluation at h4096 and8192 of the chosen K and both displayed finite bounds; predict K<=h/2 and nonvacuous atom/curvature bounds. These two arithmetic evaluations are not distribution measurements. Independently enumerate the suffix-shift guard; counterfactual omitting S_K must fail. No actual-start scan, asymptotic fit or repeated Local h200/300 job. Independent Local reading requested; this is elementary concentration and convolution using the recorded backward equations, with no novelty claim.

*Second reader's note on G82 (Local, 2026-10-06; chat L044).* Correct. $R_h \ne R_K$ needs some $k > K$ with
$S_k - k/2 > k/8 - 1$, and $e^{1/2} \sum_{k > K} e^{-k/32} < 64 e^{-K/32}$; the last $K$ reversed bits carry $S_K$ and $R_K$ while the
first $n = h - K$ bits give an independent $Z_n$, so $J_K$ is a mixture of shifts of a reflected binomial; the split
convolution gives the first-difference bound $4/(n+1)$; coupling costs $\eta$ per atom and $2\eta$ per adjacent difference; the
suffix-shift guard checks. Checked exactly (`collatz_audit_g67_g69.py`, G82 part): the joint law of $(J, J_K)$ by dynamic
programming in 22 $(h, K)$ cases with $h \le 96$ (total variation $\le \Pr(J \ne J_K) \le \eta$; atom and adjacent-difference
bounds); the binomial first-difference bound for $n \le 256$; and at $h = 4096$ and 8192, $K = 1065$ and 1154 (both $\le h/2$)
with non-vacuous atom bounds 0.0221 and 0.0156 and curvature bounds 0.00195 and 0.00098. This answers L041: the
logarithm in G75 was a cost of the proof, and G82 removes it.

### G82 window controls outcome (2026-10-06)

LW1 passes163872 exact window decompositions and364 independent-prefix convolution/total-variation controls on all future strings for T1..12. All35 comparisons with the geometric window bound are vacuous at this small scope; the exact coupling comparisons remain separately verified. LW2 passes257 exact integer binomial first-difference controls for n0..256, including the unimodality l1 identity. Its arithmetic evaluations give(h,K,atom upper bound,curvature upper bound)=(4096,1065,0.01816,0.001319) and(8192,1154,0.01192,0.0005683). These are double-precision evaluations of the proved bounds, not observations of a demand distribution or empirical decay. The suffix-shift counterfactual is independently refuted: actual J is constant2, while omitting S_K gives2+b.

Probe: `tests/probes/prizes/collatz_gpt_window_smoothing.py`; predictions at42e96b1, GPT's Intel host, Python, about1 s. No control failed. The asymptotic improvement is analytic and independently reviewed by Local L044. No actual-start population or Local h200/300 distribution job was repeated, and no bound on actual block mass or total signed discrepancy is inferred.

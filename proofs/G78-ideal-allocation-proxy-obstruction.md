# ideal allocation proxy obstruction

*GPT's proofs, second-read by Local. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT78. ideal allocation proxy
obstruction (second-read by Local, 2026-10-06)"; rebuild with `python3 proofs/build.py`. Edit the proof in PROOFS.md
and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

Even a perfectly fair spread of numbers would leave that crude bound growing, so the route needs real cancellation.

**What it says.** GPT computed the crude bound for an ideal fair-coin population, where the true discrepancy is
exactly zero. The bound still grows with the horizon: at eight times the number of free bits it already exceeds that
number, and it keeps growing. So replacing each imbalance by its whole class size throws away too much.

**Why it matters.** It shows the problem is the method, not the data. Any working bound must use the signs of the
imbalances, not just their sizes.

**An everyday picture.** A scale that reads heavy even with nothing on it: the fault is in the scale, not the load.

## The formal statement and proof

### G78. Even ideal coin-class allocation leaves a growing full-class proxy (2026-10-06)

G77 leaves allocation-aware triangle estimates open. One qualification is needed: merely matching the coin odd-count allocation does not make the bound from replacing abs(I) by K uniformly small. Define v(t,a) as the number of admitted length-t words with a ones and

    q_w(t,a)=2^m*v(t,a)/2^t,
    U_coin(m,T)=(1/2)*sum_(t=m)^(T-1) sum_a q_w(t,a)*Delta_t(a).

These are ideal coin class masses and their full-class proxy, not actual Collatz measurements. Let d=T-m. Choose a length-T admitted word uniformly, and let Z_tail be its number of ones after the first m bits. Then exactly

    U_coin(m,T)/Q_w(T)=E[2*Z_tail-d | admitted through T].

**Proof.** Keep the admitted first-m-bit ensemble with one unit of mass per word and replace only the d future bits by independent bits of odd probability p. Its final mass is the finite polynomial

    F(p)=sum over admitted length-T words of p^z*(1-p)^(d-z),

where z=Z_tail. Thus F(1/2)=V(T)/2^d=Q_w(T), and differentiation gives

    F'(1/2)/(2*F(1/2))=E[2*Z_tail-d | admitted through T].

Independently, differentiate one tail coordinate at a time. An admitted prefix at time t has mass q_w(t,a) when all tail coordinates are fair. Making its next bit odd rather than even changes its future completion probability by Delta_t(a). A prefix already killed contributes0. The coordinate sum is therefore F'(1/2)=sum_(t=m)^(T-1) sum_a q_w(t,a)*Delta_t(a)=2*U_coin. This is the finite increasing-event differentiation formula often called Margulis-Russo; the complete specialization is proved here and no external theorem is required.

Since each surviving full word has at least ell_T ones and its prefix at most m, Z_tail>=ell_T-m. Consequently

    U_coin(m,T)/Q_w(T)>=2*ell_T-T-m.

In particular beta=log(2)/log(3)>5/8 gives, at T=8*m with m>=1,

    U_coin(m,8*m)/Q_w(8*m)>m.

The ideal full-class proxy thus grows along a fixed linear horizon. A classwise comparison K_w(t,a)<=K*q_w(t,a), followed by abs(I_w(t,a))<=K_w(t,a), yields A_w(T)<=K*U_coin(m,T). Its sufficient right-hand side cannot establish a uniform A/Q bound by itself. This is not a lower bound on actual A: in an exactly fair coin ensemble the signed class imbalance vanishes, even though the proxy is positive. Sharper estimates for actual abs(I), or a signed cancellation argument, remain open. No assertion is made that actual classwise domination holds.

**Unexpected proxy-versus-error guard.** At m2,T5 the four admitted full words have tail words011,101,110,111. Their tail signed counts2*z-3 are1,1,1,3, with mean3/2. Here Q=1/2 and U_coin=3/4. Ideal fairness has zero count discrepancy despite that positive proxy. Replacing a zero imbalance by the full class size is therefore a substantive loss, not just a change of normalization.

**Next controls, preregistered NOT RUN.** PC1: m1..8,T=m..24, compute U_coin by exact rational backward weights and compare it with an independent forward integer recurrence for admitted word counts and summed tail odd counts. Predict identity and the endpoint lower bound; retain T=m. PC2: coin dynamic programming only, m1..32,T=8*m; verify the strict lower bound U_coin/Q>m by the moment formula and independently enumerate the m2,T5 guard. Counterfactual: an ideal fair ensemble's full-class proxy equals its signed discrepancy0; must fail on the positive3/4 guard. No actual-start scan, Local job, or empirical claim about actual class domination. Independent Local reading requested.


### G78 controls outcome (2026-10-06)

PC1 passes164 exact rational backward-proxy/forward-tail-moment comparisons at m1..8,T=m..24, including8 empty-tail cases. Endpoint lower bounds pass. PC2 passes32 exact strict inequalities U_coin(m,8*m)/Q_w(8*m)>m for m1..32, using integer counts and moments only. Independently enumerating the m2,T5 words gives tails011,101,110,111, normalized proxy3/2 and proxy3/4, refuting equality with the ideal fair ensemble's zero signed discrepancy.

Probe: `tests/probes/prizes/collatz_gpt_coin_proxy.py`; predictions at14fde39, GPT's Intel host, Python, under1 s. No control failed. The asymptotic obstruction is proved in G78; these are finite instrument checks. No actual-start population, classwise-domination claim or Local computational job was run. Independent proof reading remains pending.

*Second reader's note on G77 and G78 (Local, 2026-10-06; chat L042).* Both correct. G77: $C = Q + D \le Q + A$; each
term of the infimum is at least $1/\sqrt{h+1}$, so $b(h) \ge 1/\sqrt{h+1}$; $\sum_a |I| \le C_w(t)$; with $Q$ nonincreasing
the bootstrap coefficient is at least $\tfrac12 \sum_{j \le d} j^{-1/2} \ge \sqrt{d+1} - 1$, which closes only that coarse
route. G78: $F(\tfrac12) = V(T)/2^d = Q$, and both the derivative of $F$ and Russo's coordinate sum give
$U_{\mathrm{coin}}/Q = E[2Z_{\mathrm{tail}} - d]$; every surviving word has at least $\ell_T$ ones, so the ratio is at least
$2\ell_T - T - m$, which exceeds $m$ at $T = 8m$ because $\beta > 5/8$; the $m = 2$, $T = 5$ guard reproduces. Checked
by coin dynamic programming (`collatz_audit_g67_g69.py`, G77/G78 part): the moment identity, the endpoint bound and
the bootstrap floor on 104 $(m, T)$ cases, and $U/Q > m$ at $T = 8m$ for every $m < 200$.

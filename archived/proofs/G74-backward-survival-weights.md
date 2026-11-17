# backward survival weights

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT74. backward survival weights
(second-read by Local, 2026-10-06)"; rebuild with `python3 proofs/build.py`. Edit the proof in PROOFS.md and this
summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

The gap between the real Collatz count and the coin-toss prediction is an exact sum of odd-even imbalances.

**What it says.** Weight each surviving number by the chance that fair coin tosses from its current state would
survive to the end. Following these weights step by step, the final difference between the real count and the coin
prediction equals a sum, over all steps, of how unbalanced the odd and even numbers are, times how much one extra
odd step matters.

**Why it matters.** It reduces the Collatz count's central question to controlling those imbalances, with exact
weights.

**An everyday picture.** A household budget kept in a foreign currency whose rate changes: the final balance is each
month's surplus or deficit, converted at that month's rate, all added up.

## The formal statement and proof

### G74. Backward survival weights isolate the final count discrepancy (2026-10-06)

G71's hazard ratio is exact but changes both the critical-class occupancy and its parity allocation. A standard backward-equation telescoping argument instead writes the final additive discrepancy directly in terms of parity imbalances at each odd count. This is an application of finite first-step analysis, not a novelty or mixing claim; prior-art scope is recorded in PRIOR-ART.md.

Fix w=m+1, m>=1 and final horizon T>=m. Let K_w(t,a) count width-w starts coefficient-admitted through t with a odd steps. Let I_w(t,a) be the number of these starts with odd current state minus the number with even current state. Counts include multiplicity of starts, even if terminal states merge. Put I=0 for absent classes.

Define f_t(a) as the probability that independent fair future parity bits survive every coefficient barrier from the already-admitted state (t,a) through T. Set f_t(a)=0 when a<ell_t, f_T(a)=1 when a>=ell_T. For admitted a and t<T, first-step analysis gives

    f_t(a)=(f_(t+1)(a)+f_(t+1)(a+1))/2,
    Delta_t(a)=f_(t+1)(a+1)-f_(t+1)(a).

The definition extends f_t to every integer a; a killed state stays killed. Coupling the same future bits from a and a+1 proves monotonicity in a. Hence0<=Delta_t(a)<=1. Also Delta_t(a)=0 for a>=ell_T, since either child then survives even an all-zero future. Only admitted classes with ell_t<=a<ell_T can contribute.

Let H_t=sum_a K_w(t,a)*f_t(a). An odd actual current state sends its input to a+1; an even state sends it to a. Inadmissible children have f=0, matching their removal. Subtracting the fair average for each parent gives exactly

    H_(t+1)-H_t=(1/2)*sum_a I_w(t,a)*Delta_t(a).

At the free-bit boundary K_w(m,a) equals the number of admitted length-m words with a ones, by the parity bijection. Therefore H_m=Q_w(T)=2^m*V(T)/2^T, while H_T=C_w(T). Telescoping proves

    C_w(T)-Q_w(T)
      =(1/2)*sum_(t=m)^(T-1) sum_a I_w(t,a)*Delta_t(a).

This includes T=m (empty sum) and empty later ensembles. It requires no conditional probabilities of the actual ensemble and no positive-count assumption. In particular

    abs(C_w(T)-Q_w(T))
      <=(1/2)*sum_(t=m)^(T-1) sum_a abs(I_w(t,a))*Delta_t(a).

The weights have a concrete interpretation. Take fair bits for steps t+2 through T, with cumulative ones Z_k and Z_0=0. Put

    J=max_(j=t+1)^T (ell_j-Z_(j-t-1)).

A child with a ones survives precisely when a>=J. Thus Delta_t(a)=Pr(J=a+1). Over all integer a these weights sum to1. On the actual admitted classes their sum is at most1; consequently the previous bound is at most half the sum over t of max_a abs(I_w(t,a)). This coarse bound is not known to be small. The sharper weighted signed sum is the selected object; no cancellation, bounded excess or exponential count rate is proved.

**Unexpected immediate-loss guard.** Width3 has a single admitted start at m2: n7, with trace7,11,17,26,13 through T4 and odd counts1,2,3,3. Step2 to3 is noncritical (ell_2=ell_3=2), yet I_w(2,2)=1 and Delta_2(2)=1/2, since f_3(2)=1/2 and f_3(3)=1. Its contribution is1/4. At step3 the only class is a3, where Delta_3(3)=0. Here V(4)=3, Q_w(4)=3/4 and C_w(4)=1: the entire additive discrepancy comes from a noncritical step. Dropping noncritical terms from this formula gives0, incorrectly. This does not contradict G71: noncritical steps have no immediate count loss, but their parity allocation changes a later critical-class occupancy.

**Next controls, preregistered NOT RUN.** BW1: widths2..10, every final T from m through24; compute rational backward f and independent direct survivor states, verify each H increment, the final telescoping identity, monotone/nonnegative weights and the weighted absolute bound. Retain zero ensembles and separate noncritical contributions. Predict exact equality and no bound failure, without predicting the signs or a decay rate. BW2: for final T<=10, independently enumerate future coin strings to check the J distribution against backward Delta on every integer a in its support. Counterfactual: only critical steps contribute to the additive sum; must fail on width3,T4 as above. No large stopping scan, entropy measurement or Local job. Independent Local reading requested; next controls are an instrument check, not a proof of the count conjecture.


### G74 controls outcome (2026-10-06)

BW1 passes180 width/final-horizon cases and1740 exact rational H increments at widths2..10, T=m..24. All516 empty-parent increments are retained; terminal telescoping, nonnegative weights and the weighted absolute bound pass. BW2 independently enumerates future coin strings for T1..10 and matches440 backward weights to the maximum-demand distribution. The unexpected critical-only counterfactual is refuted: width3,T4 has total discrepancy1/4 and noncritical contribution1/4.

Probe: `tests/probes/prizes/collatz_gpt_backward_weights.py`; preregistration at4a78c0b, GPT's Intel host, Python, under1 s. No control failed. These validate the finite identity and its guard, not a uniform bound or cancellation rate. Independent Local proof reading remains pending. Next reasoning should target the signed weighted sum, rather than discard noncritical steps or substitute a bound on terminal information loss.

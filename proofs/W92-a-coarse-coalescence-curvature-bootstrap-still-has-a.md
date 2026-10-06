# A coarse coalescence-curvature bootstrap still has a growing coefficient

*The waiting room (not yet verified). Derived from [PROOFS.md](../PROOFS.md), entry "G92. A coarse
coalescence-curvature bootstrap still has a growing coefficient (2026-10-06)"; rebuild with `python3
proofs/build.py`. Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** in the waiting room: stated with a proof, not yet checked by a second reader.

## In plain words

A coarse maximum-curvature bound still cannot close the constant count estimate by itself.

**What it says.** Grant that unmatched inputs cancel completely, and bound all matched pairs by the largest available curvature bound. Replacing the matched count by half the survivor count leaves a coefficient growing at least as the logarithm of the paid tail. This is growth of the estimate's right-hand side, not of the actual error.

**Why it matters.** Matching improves the old square-root obstruction but needs actual allocation or signed information to become a global result. An exact pair has zero meeting-step contribution at a slightly longer horizon despite a positive bound, demonstrating the distinction. Independent review remains pending.

**An everyday picture.** Charging every paired traveller the largest possible toll overestimates the total even when some actual tolls are zero. The improved price cap alone does not settle the bill.

## The formal statement and proof

G91's curvature identity is useful only with actual allocation or signed control. Here is a limitation of a specific triangle route, even if its entire unmatched signed sum is granted to be zero. Define c(0) = 1/2, and for h >= 1 put

    c(h) = min(1/2, inf_(1 <= K <= h) [2/(h-K+1) + min(1,64*exp(-K/32))]).

The first bound follows from 0 <= Delta <= 1; the second is G91's reviewed-window consequence. Thus each matched pair contributes at most c(h) in absolute value. Since the matched count is at most C_w(t)/2, the resulting sufficient estimate, under the stated zero-unmatched grant, is

    abs(D_w(T)) <= (1/2) sum_(t=m)^(T-1) C_w(t)*c(T-t-1).

Feed a putative preceding-horizon bootstrap C_w(t) <= K0*Q_w(t) into precisely this estimate. Its normalized coefficient is

    B_(m,T) = (1/2) sum_(t=m)^(T-1) c(T-t-1)*Q_w(t)/Q_w(T).

Each window expression is at least 2/h, since h-K+1 <= h and its other term is nonnegative. Consequently c(h) >= min(1/2,2/h). The coin mass is nonincreasing, so for paid-tail length d = T-m >= 5,

    B_(m,T) >= sum_(h=4)^(d-1) 1/h >= log(d/4).

The final comparison integrates 1/x on [4,d]. Hence this sufficient right-hand side grows at least logarithmically, including along T = 8*m. It cannot certify a uniform count ratio by this fixed-constant bootstrap alone, even after granting the missing unmatched cancellation. G77's analogous maximum-atom estimate grew at least as a square root; curvature improves the estimate but does not finish it.

This is not a lower bound on actual matched error, D or A, nor a refutation of the count conjecture. The actual adjacent differences may vanish or cancel, and the matched mass can be much smaller than C/2. No such sharper allocation or signed estimate is supplied here. Only the route that replaces every matched weight by this maximum-window bound and every matched count by C/2 is closed. G91's exact identity and actual unmatched signed contribution remain available.

**Unexpected zero-contribution guard, exact arithmetic rather than a run.** Use G90's two actual parents at time 33 but final horizon T = 35. Now ell_34 = 22 and ell_35 = 23. The one-step fair continuation weights at time 34 for counts 21, 22, 23 are respectively 0, 1/2, 1. Therefore Delta_33(21) = Delta_33(22) = 1/2 and the matched pair contributes exactly zero, even though c(1) = 1/2. Their common state at time 34 is even, so both fail the next coefficient barrier; zero contribution at the meeting step is not zero final error for the selected pair. This guard demonstrates why the positive coefficient above cannot be called observed error. No new experiment, rate fit, wider collision search or external novelty claim; the proof specializes G77 and G91 and retains the domain of the smoothing bound.

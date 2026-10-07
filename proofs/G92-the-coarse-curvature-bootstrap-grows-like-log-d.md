# the coarse curvature bootstrap grows like log d

*GPT's proofs, second-read by Local. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT92. the coarse curvature
bootstrap grows like log d (second-read by Local, 2026-10-06)"; rebuild with `python3 proofs/build.py`. Edit the
proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

Even with the pairing tool, the crude estimate still grows, slowly, with the length of the run.

**What it says.** Grant generously that unpaired paths cancel completely, and bound every pair by the largest amount
it could contribute. The estimate still grows like the logarithm of the number of steps, so it cannot give the fixed
bound that is wanted.

**Why it matters.** It improves on the square-root growth of G77, and shows that the remaining gap needs real
information about which paths pair up.

**An everyday picture.** The builder's quote of G77 again, now with the worst cases paired off against each other:
it still creeps up, only more slowly than before.

## The formal statement and proof

### G92. A coarse coalescence-curvature bootstrap still has a growing coefficient (2026-10-06)

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

*Second reader's note on G92 (Local, 2026-10-06; chat L047).* Correct. Each window expression is at least $2/h$
since $K \ge 1$, the coin mass is nonincreasing, and $\sum_{h=4}^{d-1} 1/h \ge \log(d/4)$. Checked (M4, M5): $c(h) \ge \min(1/2, 2/h)$ for $h \le 10^4$ and the coefficient exceeds $\log(d/4)$ for $5 \le d \le 10^4$ (64.2 against
7.8 at $d = 10^4$, so the bound is far from tight); the zero-contribution guard checks exactly (weights 0, 1/2, 1 at
time 34; the common state even and failing at 35). Only the coarse route is closed.

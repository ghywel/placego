# Gap-matrix coarse squeeze for every periodic wall

*GPT's proofs, second-read by Local. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT54. Gap-matrix coarse
squeeze for every periodic wall"; rebuild with `python3 proofs/build.py`. Edit the proof in PROOFS.md and this
summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

A simple two-by-two calculation bounds the information reaching the left half, for every repeating wall.

**What it says.** List the gaps between the wall's white beats. Each gap gives one of three small 2-by-2 tables;
multiply them together. The size of the product (its largest eigenvalue) gives a ceiling on how fast information can
reach any column on the left.

**Why it matters.** It is a quick, explicit bound for every rhythm at once. It is coarse, so it does not close the
gap on its own.

**An everyday picture.** A train of gears, each with a known ratio: multiply the ratios along the train and you know
the most the last gear can turn for each turn of the first. It is a ceiling, not the actual speed.

## The formal statement and proof

**Where:** RULE30-GPT.md G54; copied proof. **Status:** second-read by Local, 2026-10-06 (note below). Reuses G14/G15; no new channel data.

### G54 corollary and proof: coarse squeeze for every periodic wall

Let tau have period p and at least one white phase. List its white phases cyclically, let g_1,...,g_z be the positive gaps between consecutive white times (including the wrap gap), and put

    M=B_(g_1)*...*B_(g_z),
    B_1=A=[[1,1],[0,1]],
    B_2=F=[[1,1],[1,0]],
    B_g=J=[[1,1],[1,1]] for g>=3.

Then every fixed column to the left of the wall has entropy at most log2(rho(M))/p, where rho is the spectral radius.

G15 proves these are the exact allowed visible pairs in the width-one relaxation with an independently chosen next-right input. Its language contains every actual right-column visible itinerary. A word of n complete periods has nz visible symbols; its pair constraints use n cyclic matrix products apart from fixed endpoint factors. Equivalently counts are obtained from M^(n-1) with fixed nonnegative two-state boundary factors. Their growth is at most a constant times(n+1)*rho(M)^n, allowing a Jordan block; rho(M)>=1 because the all-zero visible path is allowed. Thus the period-vector entropy is at most log2(rho(M)). G53 propagates the bound to every fixed left column and divides by p physical steps per period. No equality is asserted for an actual orbit. If the wall has no white phase, its left-neighbour trace is periodic and all fixed left columns have entropy0 by inversion.

The same bound is independent of which white phase starts the product: cyclic products have the same trace and determinant, hence the same characteristic polynomial in this two-state case. For an explicit exact value, with t=trace(M),d=det(M), rho(M)=(t+sqrt(t*t-4*d))/2. These nonnegative products have real eigenvalues since the discriminant equals(a-d_entry)^2+4bc>=0. This algebraic value is an upper bound from the relaxation, not a new large-layer certificate.

For wall0^(p-1)1, the product A^(p-2)F=[[p-1,1],[1,0]] recovers G14's bound log2(((p-1)+sqrt((p-1)^2+4))/2)/p. For the one-hole wall01^(p-1) with p>=3, it is J and gives1/p. Neither closes the single-orbit information-cost gap.

Unexpected units check: G14's p8 visible rate0.354491897 is already per physical step, so it bounds fixed left-column entropy directly; dividing it by8 again would be wrong. G15's period8 examples00111111 and01101111 instead have per-period roots3 and4, so the respective physical bounds are log2(3)/8 and2/8. White fraction alone does not determine this certificate. These examples and calculations are reused from G14/G15, without a new experimental or novelty claim.

*Second reader's note on G53 and G54 (Local, 2026-10-06; chat L026).* Both correct. G53: at a white phase
$\pi(t) = \tau(t+1) \oplus \sigma(t)$ and at a black phase $\pi(t)$ is fixed, so aligned period blocks of $\pi$
correspond one to one with the vectors $v$; $P_v(n) \le P_\pi(pn)$ and $P_\pi(m) \le p\,P_v(\lceil m/p \rceil + 1)$ give
$h(\pi) = h(v)/p$ (the lower bound along $m = pn$ suffices for the limsup), and column $-k$ over $m$ times needs
$\pi$ over $m + k - 1$ times and one phase, so it inherits the bound. G54: G15's gap matrices bound a superset of
every actual visible itinerary; cyclic products share trace and determinant; the discriminant $(a - d)^2 + 4bc$ is
nonnegative; and the examples check exactly: for $0^7 1$ the product $A^6 F$ has spectral radius $(7 + \sqrt{53})/2$
and gives $0.354491897$ bits per step, **exactly G14's recorded rate**, which confirms the units; $00111111$ and
$01101111$ give $\log_2 3/8$ and $2/8$; the one-hole walls $1/p$; and $0101$ gives $\log_2 \varphi / 2 = 0.3471$, the
coarse bound that the certified $0.0618$ improves on (`rule30_audit_g53_g54.py`, all checks pass). With these two
entries the Generality index's last "~" is resolved for a coarse bound: every periodic wall has a squeeze; a sharp
one needs a deeper-layer certificate per wall.

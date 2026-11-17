# Word length is the first escape time on each open band — GC2500

GPT, 3 November 2026. **Mathematics PROVED hand/two-party, Local L1403, including the open-band identity, width-tail normalization, divergent weighted length and compact finite-survivor bound.** No new computation.

## 1. Exact observable, including the endpoints

Let beta=3/2, r=2/3 and G(x)=beta*x−floor(beta*x) on[0,1).
For X in(0,1), define

`tau(X)=min{k>=1:G^k(X)>X}`,

with tau=infinity if no such k exists. This is the first time the
orbit exceeds its own initial value, not the time to hit a fixed hole.
The carried change-set criterion says tau(2a)=infinity exactly when
a belongs to E.

Take a full-class word w, lengthL, and its carried plateau endpoints
A,S,T as in[GC2494](GPT-MAHLER-COMPLETE-PLATEAUS-20261103.md).
For **every a strictly inside(S,T)**,

**`tau(2a)=L`.**

The endpoints are deliberately excluded: S,T belong to E and have
infinite tau. Thus Local's R4 sampled test over(S,T] missed a genuine
endpoint exception; it cannot establish the identity on that closed
side. The endpoint has length zero but matters to the exact statement.

## 2. Hand proof

Use ordinary proper beta-greedy codes of states X<1. The finite word
w0∞ is such a code for2A: all its numerical tails are bounded by the
corresponding tails of delta=w∞, hence by2S<1. The finite upper word
u0∞, with the last0 ofw changed to1, is the carried proper threshold
code of2T. Monotonic greedy coding therefore puts the code of every
X in(2S,2T) between w0∞ and u0∞. Its firstL digits must be exactly w:
any earlier difference is outside that lexicographic interval.

For1<=j<L, the strict suffix predicate compares w[j:L] strictly
below w[0:L-j]. This comparison settles the shifted code versus the
original code within those firstL−j digits, whatever follows. Both
are proper greedy codes. Their numerical states obey

`G^j(X)<X` for1<=j<L.

At tickL the affine remainder from the fixed firstL digits is

`G^L(X)=beta^L*(X-2A)`.

Since2S=2A/(1−r^L), elementary rearrangement gives

`G^L(X)>X iff X>2S`.

This holds in the open band, proving the first escape is preciselyL.
No extrapolation of eventual speed, random independence, numerical
word enumeration or bound on the unknown future was used.

As a separate bottom component, for0<a<1/3, X=2a is below2/3 and
G(X)=beta*X>X, so tau=1. At a=1/3, G(2/3)=0 and tau=infinity.

## 3. An exact tail identity in ordinary length

By carried GC2494 and GC2496/L1398, the complement of E is precisely
the bottom component and the countably many open word bands, and E
has zero ordinary length. Hence for each integer n>=1,

**`Leb_X{X in(0,1):tau(X)>n}=2*sum_(w:|w|>n)(T_w-S_w)`.**

The factor2 is the linear coordinate change X=2a. In the ceiling
coordinate omit that factor. This is an exact series identity, even
though a finite floating-point enumeration does not give a rigorously
rounded value without its own error accounting. It also holds with
>=/different n only after the corresponding indexing change; here
lengthL bands satisfy tau>n iffL>n.

Consequently an asymptotic c/n for the full waiting-time tail, IF
proved, is equivalent to the corresponding band-width tail asymptotic.
It is not automatically equivalent to a pointwise length-L width
asymptotic c/(2L^2): differentiating an asymptotic tail needs extra
regularity. Irregular oscillations between lengths are not excluded.

## 4. L1400's infinite mean: carrying read and a precise repair

Let mu be the carried ergodic invariant Parry probability with
1/3<=rho<=3. For a stationary forward process X_j=G^j(X_0), X_0~mu,
let N_N count weak suffix maxima in the block X_0,...,X_N. Directly,

`E_mu N_N=sum_(m=0)^N P_mu(tau>m)`.

For each fixedN, stationarity identifies the LAW of this suffix count
with the weak record count R_N of X_0,X_-1,...,X_-N in a stationary
two-sided extension. Such an extension is standard for a stationary
process; no inverse single-valued beta map is being asserted.

For each q<1 the probability that all N+1 backward values avoid(q,1)
equals, by stationarity of the block, the analogous forward avoidance
probability. Ergodicity and mu(q,1)>0 make that limit zero. A countable
rational q sequence then shows that the backward running maxima tend
to1 almost surely. No coordinate ever equals1, since the state domain
is[0,1). There must be infinitely many STRICT record increases.
Therefore the weak record count R_N increases to infinity almost
surely, and monotone convergence gives E_mu R_N tending to infinity.
By the equality of expectations above,

**`E_mu tau=infinity`.**

The correction is narrow but necessary: forward suffix counts N_N
need not increase withN. L1400's phrase "N_N→infinity almost surely"
does not follow merely from equality in law for eachN. Apply monotone
convergence to the BACKWARD counts R_N and transfer their expectations.
That proves the intended conclusion without a pathwise identification.
The numerical conclusion in L1400 is carried with this repair.

Since mu<=3Leb, integrating the nonnegative tau gives
`integral tau dLeb >= (1/3)integral tau dmu=infinity`.
Combined with the open-band identity,

**`sum_w |w|*(T_w-S_w)=infinity`.**

The bottom interval contributes only1/3 to the unnormalized ceiling
integral. The change set's infinite values have no ordinary-length
mass. This proves infinite average band word length, not a1/n tail
bound at every n, not its constant, and not an integer-orbit law.
The measure/record methods are classical in substance, reproved here.

## 5. Read scope, computational guards and next step

L1400 complete argument, current record_law_check.py (including R3/R4)
and all output read. No independent Intel rerun, cap receipt audit or
extra M5 measurement is claimed. Its "exact" n=10/16/20 values are
rounded evaluations from a finite floating-point word sum through the
now proved tail identity; do not relabel them exact rational receipts.

The exact dyadic orbit recurrence is consistent with its stated map.
R3 full-domain n=50/100 and R2 n=200 give independent sampling controls
on the deficit; the large-n R1 entries remain WINDOW contributions
unless the omitted part is bounded. The exp(−60/c) omission estimate
belongs to the Poisson model being tested, not a proven actual-tail
bound. No sample establishes the proposed limiting constant, a fixed
asymptotic deficit, or the exclusion of log(n)/n corrections. Fine-grid
sampling is not needed to establish the two hand results here.

Record searched: existing G50/G51 arithmetic split, carried word
constructor GC2494/L1397, nullity GC2496/L1398, direct counts GC2498,
Local L1398–1400; actual kit/portal complete10:21:10Z, mainc42f6e51.
The standard stationary record-count idea is credited to Local's known-
in-substance formulation, not claimed as a new record theorem. The
specific c/n literature remains unread and no such theorem is imported.

Please carry section2 and the endpoint/tail normalization. Local's
infinite-mean step is adopted PROVED hand/two-party with the explicit
expectation repair in section4. The word-length consequence uses the
new identity, so remains PROOF-SKETCH until that identity is carried.

Next executable step: use the full-domain/tail identity to distinguish
an actual omitted-window bound from Poisson prediction before another
record-law sampling stage. GPT's independent alternative remains G50's
moving-age height on near-minimal separated-prefix padding. No duplicate
compute, automatic grid or stronger statistical inference requested.

My own pull: the identity turns a sampled coincidence into an exact
bridge; the unsolved arithmetic filter is the next independent test.

## 6. GC2501: a direct finite-survivor bound on every compact range

**PROOF-SKETCH, GPT, awaiting carrying read.** This is the refinement
announced in GC2500, using the explicit count now carried L1401, rather than a
positive-hole-mass heuristic. It does not require Local's measurements.

Fix w and put Q=2S_w<1. If0<X<=Q and tau(X)>n, then G^jX<=X<=Q
for0<=j<=n. All those proper beta-greedy codes are therefore at most
delta=w∞. Let p be the firstn digits of X. The zero extension p0∞
has each shift before positionn at most the corresponding shifted
actual greedy code, since replacing its future digits by zeros only
decreases it. All later shifts are zero. Consequently p0∞ belongs
to H_w. This uses a finite SURVIVAL hypothesis, not just membership
in E, so it actually controls the transient states.

There are at most N_n<=gamma^(n+L) such p. Actual beta-state expansion
places X in the interval

`sum_(i=1)^n p_i beta^(-i)+[0,beta^(-n))`.

Thus, in ordinary X length,

**`Leb{0<X<=2S_w : tau(X)>n} <= gamma^L*(gamma/beta)^n`.**

For any fixed Q0<1 choose a carried cofinal2S_w>=Q0. The same bound
holds below Q0. With q=gamma/beta<1 and layer-cake integration,

`integral_(0,Q0] tau(X) dX <= Q0+gamma^L*q/(1-q)<infinity`.

We used the trivial n=0 length Q0 separately and the displayed bound
for all n>=1. The zero state, if included, is a null singleton. The
same finite integral holds in a after linear scaling. For a band's
larger upper endpoint2T_w, its open band has tau=L and its endpoint
is null, so the same escape bound holds there for n>=L.

The new count therefore proves actual exponential finite-survival
tails and finite mean on EVERY fixed range below1. Combined with
Local's carried infinite global mean, the divergence must arise in
arbitrarily small neighborhoods of1 (a approaching1/2). This supplies
a precise reason for the boundary's importance.

It does NOT justify exp(−60/c) for the portion below Q_n=1−60/n in
Local's experiment. Choosing a new dominating w_n there changes BOTH
gamma_n and the prefactor gamma_n^L_n; the fixed-range estimate is not
a uniform asymptotic in that moving cutoff. The displayed bound is a
concrete route to a certified omitted-tail control if those constants
can be made effective enough. No automatic larger sampling stage.

Next executable step: Local carries this zero-extension argument and
the open-band identity; independently apply G50 height to separated
prefix blocks. The moving-cutoff question is left with an exact bound
and an explicit constants obstruction, not an unearned Poisson bound.

My own pull: compact finite means versus infinite global mean isolates
the endpoint as a mathematical mechanism, not just a plotting choice.

## L1401 source/output read — GC2502

The new R5 source addition and both output rows were read. It supplies measured
annulus evidence, not the remaining region below1−240/n; no whole omitted-tail bound
is adopted. L1401 carries GC2498 by hand, so the count input to section6 is now
PROVED hand/two-party. The new transient zeroextension/escape identity still await
their own carry. No future review, extra run or confidence certificate claimed.

GC2503 adoption: L1403 complete carrying argument read; GC2500/2501 mathematics PROVED hand/two-party, including endpoint exceptions, exact tail identity, infinite weighted length and finite compact means. L1404 full scan source/output read as M5 measurements; no Intel rerun or cap-receipt audit. Its log-periodic prediction is refuted on the sampled range, c/n remains conjectural. New near-minimal G50 padding control is retained in INSTINCT, still a sketch.

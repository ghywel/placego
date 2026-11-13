# Mahler pair energy: ancestry resonances and the physical multiplier

GPT, GC2941–GC2942, 13 November 2026. Owner-authorized approximately forty-minute manual block.
Both schedules remain paused. This continues [GC2940](GPT-MAHLER-VALID-STARTS-REVIEW-20261113.md)
and Local's [valid-start theorem](LOCAL-MAHLER-VALID-STARTS-20261112.md).

## 1. Outcome and status

The desired physical low-frequency bound is still open. This block finds an analytic obstruction to the
stronger bound uniform over all odd multipliers, and separates that obstruction from the physical case.
The exact ancestry phase formula also explains the large measured spikes without resampling the past.

**PROOF-SKETCH, GPT, awaiting Local:** the centered pair recurrence, signed valuation formula, suffix-cluster
obstruction, state-centroid error bound and physical same-suffix estimate below. Parallel GPT readers are
self-checks, not a second worker. Exact finite identities are **COMPUTED**; FFT results are **MEASURED**.
The odd-dilation average is a standard Parseval consequence, not a Mahler novelty claim. There is no new
power saving, extinction statement or prize proof. Flatto's original paper remains unread; novelty is uncleared.

Write beta=3/2, theta=log_2 beta, N=2^w, V_w for the admissible parity starts, and A(w)=|V_w|.
Let e(x)=exp(2 pi i x), G_w(h)=sum_(r in V_w)e(hr/N), and gamma_w(h)=|G_w(h)|/A(w).
For integer 1<=H<=N define

    Q_b(H) = sum_(|h|<H) (1-|h|/H) gamma_w(bh)^2
           = A(w)^(-2) sum_(r,t in V_w) K_H(b(r-t)/N),
    K_H(x) = H^(-1) |sum_(j=0)^(H-1) e(jx)|^2 >= 0.

The target is Q_1(H)-1<=C H/A(w). At H comparable to 2^j, Cauchy–Schwarz would give the
L1 estimate needed by Local's majorant, with j/w below theta/2. The minus one is essential.

## 2. Exact centering does not give a scalar renewal closure

Use the greedy slack states s: allowed branches are (d_s,s+1), and also (0,0) when d_s=1.
Write A_s(w) for their continuation counts. For two states s,t let P_(s,t,w)(d) count ordered
pairs with residue difference d modulo N, and put

    Z_(s,t,w)(d)=N P_(s,t,w)(d)-A_s(w)A_t(w).

Let u_b=A_(s_b)(w-1), v_c=A_(t_c)(w-1), with missing branches assigned zero;
Delta_s=u_0-u_1 and Delta_t=v_0-v_1. Directly from 2(T(r)-T(t))=3(r-t)+b-c,

    Z_(s,t,w)(d)
      = 2 sum_(b,c allowed; b-c=d mod2)
          Z_(s_b,t_c,w-1)((3d+b-c)/2 mod N/2)
        + (-1)^d Delta_s Delta_t.

The new source is entirely at the Nyquist frequency. A band H<=N/2 annihilates it at this level,
but the child kernels acquire affine phases. Removing those phases is not justified.

Equivalently, split words at their first reset. A triangle inequality on a proposed random-scale child
bound multiplies its constant by the square of sum_L beta^(-L/2). The first return lengths 1 and 3 alone
make this sum greater than 1.36. This approach cannot close the same bound without cross-return
cancellation. After this second occurrence of the same phase gap, the block changed representation.

## 3. The correct null model and valuation background

For **any** finite V subset of Z/N, A=|V|, and a uniform odd multiplier b,

    E_b[Q_b(H)-1] <= H(1/A-1/N).

At H=2^J the exact value is

    E_b[Q_b(H)-1] = H/A-C_(w-J)/A^2,

where C_m counts ordered pairs agreeing modulo 2^m. Proof: at valuation a<J the total nonzero
Fejer weight is H/2^(a+1), while its odd-dilation orbit has N/2^(a+1) frequencies. Every included
shell is therefore weighted by H/N; Parseval and the omitted multiples of H give the formula.
For arbitrary H the corresponding weight ratio is at most H/N. For w>=3, the odd units are
plus or minus powers of 3 and Q_b=Q_(-b), so a complete powers-of-three cycle has exactly this mean.
A short consecutive segment need not resemble it.

There is also a Mahler-specific correction to the random baseline. If h has valuation a and
m=w-a, take a valid parent p of length m-1, its residue r_p, its terminal state s_p and
sigma_p=T^(m-1)(r_p) mod2. For odd u,

    G_w(2^a u) = sum_p (-1)^sigma_p Delta_(s_p)(a) e(u r_p/2^m),
    Delta_s(a) = A_(s_0)(a)-A_(s_1)(a),

again omitting forbidden branches. The two possible next bits have opposite phases. Averaging over
odd u eliminates different parents, so

    mean_(v2(h)=a) gamma_w(h)^2
      = A(w)^(-2) sum_p Delta_(s_p)(a)^2.

In particular A(w) times the complete odd-shell mean tends to **1/3**, not 1. The valuation-one
limit is **7/9**: its exact numerator is A(w-2)+3(F(w)-F(w-1)). Thus Local's odd low-band means
near 0.3 do not alone demonstrate special low-band suppression. The comparison must retain valuation.

## 4. A genuine obstruction to uniformity in the multiplier

### Exact prefix phases

Write w=ell+n. For a valid prefix u of length ell put

    B_ell(u)=sum_(i<ell) u_i 2^i 3^(ell-1-i),       0<=B_ell(u)<3^ell/2.

For each compatible suffix v of length n, the inverse parity map gives exactly

    3^ell r(uv) = 2^ell r(v)-B_ell(u) mod 2^w.

The suffix is valid from its actual incoming slack and therefore from the maximal slack. Consequently
all occurring suffixes belong to V_n. No independent choice of prefix and suffix is assumed.

### Positive pair lower bound

For b=3^ell, all starts sharing one suffix v lie in a circle arc of diameter less than 3^ell/(2N).
Under the guard H3^ell<=N, every such pair has distance at most 1/(2H), where
K_H(x)>=4H/pi^2. If M_v counts compatible prefixes for v, then sum_v M_v=A(w) and at most
A(n) classes occur. Positivity and Cauchy–Schwarz give

    Q_(3^ell)(H) >= (4H/pi^2) sum_v M_v^2/A(w)^2 >= 4H/[pi^2 A(n)].       (C)

Choose 0<eta<log_beta 2-1, ell=floor(eta n), and dyadic H with 8A(n)<=H<16A(n).
The guard holds eventually because H3^ell/N=O(beta^(n+ell)/2^n) tends to zero.
Then Q_(3^ell)(H)-1>2, whereas H/A(w)=O(beta^(-ell)) tends to zero. Thus **no absolute C**
can prove Q_b(H)-1<=C H/A(w) for all odd b, widths and bands.

More precisely, log_2 H/w tends to theta/(1+eta). For every alpha>theta^2 this gives counterexamples
with H<=2^(alpha w) eventually. Here theta^2 is about 0.34218, strictly above theta/2, about 0.29248.
This does **not** refute the desired shorter range, or b=1 at any range. It limits an attempted
odd-affine strengthening of the energy estimate; GC2940's much weaker odd-affine discrepancy bound survives.

The bandwidth threshold cannot be lowered from clustering alone: equally weighted clusters centred on a
regular K-point grid have zero Fourier coefficients for 0<|h|<K. Additional information about suffix
masses or their locations would be necessary. The small H=8 spikes below need such information.

## 5. State-specific centroids explain the observed small-band spikes

The exact Fourier form of the prefix identity is

    G_w(3^ell h)=sum_u e(-h B_ell(u)/N) G_(s(u),n)(h).

Let C_s=F(ell-s), m_s be the conditional mean of B_ell, and v_s its conditional variance for
prefixes ending in s. Define

    T(h)=sum_s C_s e(-h m_s/N) G_(s,n)(h).

Taylor's formula, with the conditional first-order term zero, gives

    |G_w(3^ell h)-T(h)|/A(w)
      <= (2 pi^2 h^2/N^2) sum_s C_s v_s A_s(n)/A(w).                    (V)

The means must remain state-specific. A global centroid does not cancel the first-order term against
different child transforms. Since v_s<=3^(2ell)/16, a rough bound is pi^2 h^2 3^(2ell)/(8N^2).
The square-root nonzero Fejer energies differ by at most the coefficient of h^2 in (V), times
sqrt[H(H^2-1)(2H^2-3)/30]. This is a rigorous formula; the pilot's numerical evaluations are floating controls.

The moments have a small exact dynamic program. At depth l, an allowed bit b sends B to 3B+b2^l,
so each successor receives C, 3M+b2^l C, and 9S+6b2^l M+b2^(2l)C from counts and moments (C,M,S).
The pilot compared these exact integers with literal prefix enumeration.

Selected H=8 measurements, normalized as A(w)(Q_b(H)-1)/H:

| w | ell | Actual | Centroid | Relative square-root-energy error |
|---|---|---|---|---|
| 20 | 9 | 29.0076 | 29.1134 | 0.1823% |
| 22 | 11 | 64.5353 | 65.7377 | 0.9273% |

The physical b=1 values at these widths were 0.2858 and 0.6207. The exact prefix-phase identity
matches FFT values in every frozen case. These spikes reflect an ancestry-weighted shorter transform,
not independent noise. The centroid approximation predicts their finite magnitude, but is not a proof
of the shorter transform's all-width energy.

## 6. The physical same-suffix contribution

This section isolates a part of the physical energy that can be bounded without averaging the multiplier.
Let q=3^ell<=min(H,N), H integer. Two distinct starts in the same suffix class obey

    q(r-r') + B_ell(u)-B_ell(u') = kN.

The B values are distinct integers: successive reduction modulo 3 recovers the last bit and then all
previous bits. Their difference has magnitude <q/2. Thus the physical locations lie near distinct
points of a q-grid; they do not cluster as after multiplication by q.

For a fixed point, each nonzero circular grid distance j/q occurs at most twice, and its perturbed
physical distance is at least j/(2q), since N>=q. Hence K_H is at most q^2/(H j^2) for each such point.
The diagonal contributes H. Summing 2 sum_(j>=1) j^(-2)=pi^2/3 gives the row bound

    H + pi^2 q^2/(3H) <= (1+pi^2/3)H.

Therefore, over **all** same-suffix pairs,

    A(w)^(-2) sum_v sum_(r,r' with suffix v) K_H((r-r')/N)
      <= (1+pi^2/3) H/A(w).                                         (D)

The missing part is now precise: the cross-suffix contribution **minus one** must be at most
O(H/A(w)). It may be negative. Bounding the positive cross-suffix sum by itself would throw away
exactly the baseline cancellation we need. This is the retained physical pull, with q chosen comparable
to H and actual prefix/slack compatibility retained.

### A scalar saving, and the stronger elementary baseline

Put P_n=A(w)^(-2) sum_v M_v^2 and E_n=D_n-P_n, where D_n is the same-suffix contribution.
By the finite Fourier expansion, E_n is a nonnegative sum of squared class transforms over h!=0.
Cauchy across at most A(n) classes gives Q_1(H)-1<=A(n)E_n<=A(n)D_n. Also
F(ell)A(n)<=A(w), since every full prefix concatenates with every valid suffix. Consequently

    Q_1(H)-1 <= [H+pi^2 3^(2ell)/(3H)]/F(ell).

Choosing ell=floor(log_3 H) and using the carried renewal asymptotic gives O(H^log_3 2).
This is a deterministic physical estimate, but **it is weaker than an elementary truncation baseline**
found in the adversarial continuation. If I is a circular interval of L consecutive residues and
r=ceil(log_2 L)<=w, every w-valid point is r-valid, and I meets each class modulo 2^r at most once.
Thus, exactly,

    #(V_w intersect I) <= A(r).

Since A(w)>=F(w-r)A(r), this implies a uniform concentration estimate mu_w(I)<=C(L/N)^theta.
The standard direct annular sum K_H(x)<=min(H,1/(4H||x||^2)) then gives the stronger
Q_1(H)<=C' H^(1-theta). The constants may use the positive renewal lower bound; no explicit
sharp constant is claimed. For circle arcs not aligned to residues, replace L by ceil(N|I|)+1.

This does not improve the survivor count: at L=2^m in width w=m+j it says exactly
#<=A(m), the existing truncation bound. It is retained to prevent mistaking the weaker grid-based
scalar bound for progress. The new useful content of (D) is its control of a *specific family of pairs*.

### The centered hierarchy is an exact ternary valuation decomposition

Let two distinct full words have exactly n common trailing bits. Their numerators satisfy
v3(B_w(p)-B_w(p'))=n: the last unequal bit contributes a 3-unit times 3^n, and all preceding
terms are divisible by 3^(n+1). Define D_n as above, P_n as its pair-count baseline, E_n=D_n-P_n.
Then E_0=Q_1(H)-1, E_w=(H-1)/A(w), and

    E_n-E_(n+1) = A(w)^(-2) sum_(exactly n common trailing bits) [K_H((r-r')/N)-1].

The baseline telescopes exactly. Each E_n>=0, but differences need not have a fixed sign.
The remaining target is a signed estimate for the coarser ternary valuation shells, not a new
bound on their absolute masses.

## 7. Move the energy to the compatible ternary residue tree

The underlying transport is **already in the record**, G51/GC2350 and Cloud CL782 H3, carried by
GC2936. It is not a new encoding. The additional application here is a quantitative energy comparison.
Put R=3^w and, for each valid word, let

    k = 2^(-w) B_w mod R,       0<=k<R.

The exact integer identity is Rr+B_w=Nk, with k=T^w(r). Hence

    r/N = k/R-B_w/(RN),       0<=B_w/(RN)<1/(2N).

The map to k is injective. For a trailing word v of length n,

    k mod3^n = 2^(-n) B_n(v) mod3^n.

Thus suffix compatibility becomes an exact nested ternary congruence, with all ancestry retained.
Let Q^ter_w(H) be the Fejer energy of these k/R points. The point displacement gives

    |sqrt(Q_1(H)-1)-sqrt(Q^ter_w(H)-1)|
      <= (pi/N) sqrt[H(H^2-1)/6].                                  (T)

Proof: the normalized Fourier transforms differ by at most pi|h|/N; apply the triangle inequality
in the weighted nonzero-frequency Euclidean norm. The weaker absolute bound is
|Q_1(H)-Q^ter_w(H)|<=(2pi/(3N))(H^2-1).

For comparison with the target H/A(w), (T)'s relative square-root error is at most
(pi/sqrt(6)) H sqrt(A(w))/N. It tends to zero for H<=2^(alpha w) whenever
alpha<1-theta/2, about 0.70752, and therefore throughout the desired range alpha<theta/2.
A random-scale bound on this **specific** ternary tree would consequently transfer to the physical set.
Averaging over ternary multipliers would again discard the question: the multiplier here is 2^(-w).

This is not a reopening of the old closed “bowtie” route in MAHLER.md: that route attempts to gain
pinning information by splitting an already-known word into coprime windows. Here the word is unchanged;
the new objective is the signed pair statistic, with an explicit error relative to its target.
No extra independence, information or count saving is inferred from the change of modulus.

### A second signed identity from the spatial order

The final changed-representation pass orders the valid beta-cylinders by their real starting points.
This uses the standard beta-transformation cylinder partition, not a new encoding. If a word ends
in slack c_s, its possible real tails occupy

    [B_w/3^w, B_w/3^w+beta^(-w)c_s/2).

These intervals partition [0,1/2). Thus consecutive sorted numerators have gap 2^(w-1)c_s.
Write q_s=2^s c_s, an odd integer. Choose a=3^(-w) **modulo 2^(w+1)**, and let G_(s,w)(h)
sum the physical Fourier phases of words ending in s (terminal state here, unlike A_s's incoming state).
Telescoping the phases of the cylinder endpoints gives exactly

    sum_(s=0)^w [1-e(-a q_s h/2^(s+1))] G_(s,w)(h)
      = 1-e(-h/2^(w+1)).                                            (F)

The last cylinder, the greedy word, has the half-integer endpoint 3^w/2 in numerator coordinates.
The lift of a modulo 2N is needed for its coefficient and the small right side; modulo N alone
would leave an ambiguous sign at that endpoint. All physical G_(s,w) are unaffected by changing
that lift. This is an additional exact signed constraint retaining terminal states.

It is not a closed system: one relation contains w+1 state transforms. Evolving those transforms
introduces fractional frequencies/extra affine phase. A scalar absolute-value estimate again loses
the missing cancellation. The two attempts to close the same correlation this way are now parked;
reopening requires a norm or a state-resolved covariance inequality that uses (F), not another
triangle inequality or a longer frequency census.

### Exact positive kernel for the retained ancestry

There is a more concrete continuation than a generic CRT count. For w=ell+n, two prefixes u,u'
can share precisely the suffixes admissible from min(c_(s(u)),c_(s(u'))). This minimum is taken
in **slack value**, not in the state index. The suffix-language intersection is nested by monotonicity.
Since the common suffix cancels from B_w(uv)-B_w(u'v), the ternary E_n equals

    A(w)^(-2) sum_(0<|h|<H) (1-|h|/H)
      sum_(u,u') A_(min slack)(n)
        e(h 2^(-w)(B_ell(u)-B_ell(u'))/3^ell).                        (G)

Here 2^(-w) is reduced modulo 3^ell. Order the finitely many positive prefix slacks as
c_1<...<c_J, set a_j(n)=A_(c_j)(n), and set a_0(n)=0 as an artificial baseline. Then
Delta a_j=a_j-a_(j-1)>=0 and the exact pair kernel factors as

    A_(min(c_u,c_u'))(n)
      = sum_j Delta a_j(n) 1_(c_u>=c_j) 1_(c_u'>=c_j).

Thus (G) is a positive weighted sum of squared **threshold-filtered prefix polynomials**:

    E_n^ter = A(w)^(-2) sum_(0<|h|<H) (1-|h|/H)
      sum_j Delta a_j(n) |sum_(u:c_(s(u))>=c_j)
                           e(h 2^(-w) B_ell(u)/3^ell)|^2.            (G')

For n=0, all positive-slack a_j(0)=1; only the first increment is nonzero. The artificial a_0=0
must not be confused with the genuine maximal-slack state numbered 0, which has c_0=1.
This factorization keeps the actual shared history and both incoming slacks; replacing its weight by
a product of separate continuation counts would be false. It supplies a finite positive-kernel target,
not an estimate of it. The next proof attempt should combine this kernel with (F)'s signed constraints
at the actual multiplier, or give a counterexample to the proposed contraction before any enlarged run.

### The warm continuation: an ordinary beta transfer operator

Fix the final prefix length ell>=1 and a **positive even** integer a congruent to 2^(-w) modulo 3^ell.
Use that same lift at every intermediate depth k<=ell. Let P_(k,t) be the threshold polynomial
in (G'), with phase e(h a B_k/3^k), and 0<t<=1. Appending a final bit gives exactly

    P_(k,t) = P_(k-1,t/beta)
               + z_k 1_(t<=1/2) P_(k-1,(1+t)/beta),
    z_k=e((ha/2) beta^(-k)),       P_(0,t)=1.

The two diagonal pieces of its squared integral partition the old threshold interval, so

    I_k := integral_0^1 |P_(k,t)|^2 dt
      = beta I_(k-1)
        + 3 Re[z_k integral_0^(1/3)
                   P_(k-1,s+2/3) conjugate(P_(k-1,s)) ds].           (H)

The first coefficient is exactly beta, not a triangle-inequality factor two. The displayed cross
correlation is the missing signed term.

More usefully, define the ordinary Lebesgue transfer operator of x -> beta x mod1,

    L f(t)=beta^(-1)[f(t/beta)+1_(t<1/2) f((1+t)/beta)].

With omega=ha/2, a direct phase conjugation yields, almost everywhere,

    P_(k,t)=e(-omega beta^(-k)t) beta^k L^k[e(omega t)](t),
    I_k=beta^(2k) ||L^k e(omega t)||_2^2.                            (I)

The signs follow because z_k cancels the extra phase of the second inverse branch. The even lift
makes omega a nonzero integer for h!=0, so the initial function has exactly zero Lebesgue mean.
This is an application of the known beta-transfer operator, not a new operator or a mixing theorem.

Two guards prevent a false conclusion. First, (G') has exact finite continuation-count increments,
not Lebesgue threshold weights. For a **fixed** prefix length, renewal gives
A_s(n)/A(n)->c_s: use A_s(n)=1+sum_(t<n) d_(s+t) A(n-1-t) and dominated renewal ratios. Thus the normalized increments tend to slack gaps.
A growing-prefix use requires a quantified error multiplied by the sizes of the polynomials.
Second, a can be of size 3^ell: a spectral gap for each fixed frequency, with a BV constant proportional
to |omega|, does not supply the required uniform frequency/time estimate. Neither guard is dropped.

There is also an exact endpoint version with **no** finite-weight approximation. Take ell=w and
choose the even lift a_w=2^(-w) modulo 3^w. Below the least positive terminal slack, P_(w,t)
contains every valid word. Taking t down to zero gives

    G_w^ter(h)=beta^w [L^w e_(h a_w/2)](0+),
    A(w)=beta^w [L^w 1](0+).                                       (J)

The one-sided value exists for these finite-step piecewise smooth functions. It avoids an arbitrary
endpoint branch convention. Consequently the exact remaining nonzero energy is

    sum_(0<|h|<H) (1-|h|/H)
      |[L^w e_(h a_w/2)](0+)|^2 / |[L^w 1](0+)|^2.

The next executable pull is this **joint high-frequency/time boundary estimate** along the actual
modular frequencies. It uses a familiar transfer operator without exchanging a renewal limit and a
growing prefix. The L2/finite-kernel formulations remain alternative ways to control that boundary value;
L2 mixing alone does not automatically control point evaluation. This is a sharper research question
than another unconditional multiplier average or a larger census.

## 8. A conditional frequency reduction, not a solution

For any incoming state, the one-step identity is

    G_(s,w)(3h)=sum_(b,t allowed) e(-hb/2^w) G_(t,w-1)(h).

If the primitive-frequency sum over 0<h<H, 3 not dividing h, were <=c H A_s(w), uniformly in
all required states and real cutoffs, Cauchy–Schwarz and at most two branches would bound the
full positive-frequency sum by 3c H A_s(w). The induction contracts by 2/3 because the child
cutoff is H/3 and sum_t A_t(w-1)=A_s(w).

This hypothesis is substantial: H=2 already requires square-root cancellation at frequency 1.
Moreover 3-units can remain resonant when h is close to plus or minus 2^w modulo a large power of 3.
After h=2^a u, the correct tags include v3(u), v3(u-2^(w-a)), v3(u+2^(w-a)). At w=20 and 22,
the mean of A(w)gamma(h)^2/beta^a for maximum tag at least 4 was respectively 3.744 and 5.401 times
the mean for tags at most 1, on the frozen h=1..2047 sample. This supports a joint ternary/valuation
partition, not independence or a uniform bound for its complement.

## 9. Tests, prior art and next carrying read

Frozen sources: [stage 1](../tests/probes/mahler/gpt_fejer_pair_energy.py), SHA256
`a793b2d2991b6a43673c437460f62688048da9f8e3a70ab46ad8d0c66c253dba`, at `5379d1180`;
[stage 2](../tests/probes/mahler/gpt_fejer_resonance.py), SHA256
`e3c99380f65c5d211740d76707ddb65f431eec6c931ca8baf6c15dce19396b27`, at `b309e431e`.

Stage 1 checked 12750 centered-pair entries, 2550 direct starts and 255 signed-boundary coefficients,
plus the complete small odd-unit/powers-of-three mean and Parseval. P1 held on all 15 selected cells:
physical excess <=3H/A. **P2 was refuted:** only 8/15 physical values fell below the random-multiplier
median, against the predicted at least 10/15. This is recorded, not reinterpreted as a success.
Stage 2's exact moment/phase controls passed. P3 (selected centroid error <=20%) and P4 (ternary-tag
mean ratio >=2 at w=20,22) both held. Results at larger widths were not sought.

Intel run receipts: stage 1 used 0.817929 aggregate CPU seconds, 1.1 wall, sampled tree RSS 65496 KiB,
launch free-memory proxy 5878 MiB, minimum 5827 MiB and zero swap growth. Stage 2 used 0.579051 aggregate
CPU seconds, 0.55 wall and launch proxy 5989 MiB; it finished before the first periodic RSS sample, so
its sampled zero is **not** a zero-memory measurement. Both used the frozen 120 CPU/300 wall/768 MiB
RSS stages, two tracked processes, single numerical thread, swap-growth stop 4096 MiB, 4096/1024 MiB
free-memory gates and 16/128 MiB file/stage limits. No job remains running.

The final structural control, [source](../tests/probes/mahler/gpt_fejer_ternary_controls.py), SHA256
`245c37b15c94111abed2efd774517f6e90d32f825265379938be41c270e7b842`, frozen at `169083aac`,
passed 265 literal orbit transports, 2437 suffix congruences, 1392 exact pair valuations, 5460
circular intervals, 3064 distinct ternary grid slots and 89 floating same-suffix energy bounds.
The common-prefix replacement failed on 1013 pairs, as predicted. This stage used 0.310393 aggregate
CPU seconds and 0.54 wall, with no periodic RSS sample; its 30 CPU/60 wall/256 MiB RSS caps and
other gates were declared beforehand. All three stages together used 1.707373 aggregate CPU seconds.

Evidence is byte-verified in the shared store at `cited/gpt/gc2942-mahler-energy-20261113.tar.gz`, SHA256
`60c9c3c3c62e99532287058c8e5d39b2622146133f0273cf376df559521c4802`, 293644 bytes. It contains the frozen probes, predictions, run receipts,
outputs and mathematical self-check notes; subsequent hand continuations are recorded in this report.

Record searches: `pair energy`, `Fejer`, `large sieve`; GC2938's complete kit/portal snapshot at
`9ea4f8d68638715c146ed4226f66e1c50cd5227c`, 13 November 10:44 GMT, has no matching Mahler statement.
The closest primary method found is [Mosquera–Shmerkin, Proposition 2.3](https://www.acadsci.fi/mathematica/Vol43/vol43pp0823-0834.pdf):
sparse exceptional Fourier frequencies for independent-digit self-similar measures. Our conditioned slack
language and dyadically prescribed sample do not satisfy that theorem's hypotheses. The fixed finite-IFS
assumptions in [Varju–Yu, Theorem 1.5](https://arxiv.org/pdf/2004.09358) likewise require a bridge;
its algebraic-integer reciprocal corollary excludes 3/2. Broad Fourier-product and exceptional-frequency
methods are prior art. No applicable pair-energy theorem was found; no novelty claim follows.

**Local, requested carry:** (C)'s exact compatibility and bandwidth scope; (D)'s modular grid separation;
(V)'s terminal-state conditional moment cancellation; (T)'s energy-error scale; (F)'s endpoint lift; (G')'s shared-suffix minimum-slack kernel; and (I)'s phase conjugation and finite-weight guard, and (J)'s one-sided endpoint. Please keep the open physical cross-suffix excess
separate from the refuted unrestricted slope extension. GC2940's sharper constants/full-prefix carry remains
pending independently. The next executable research step is to express the physical cross-suffix excess as
the joint frequency/time boundary estimate in (J). If approached through (I), carry (G')'s exact finite weights and justify point evaluation. Fixed-frequency mixing alone is insufficient; the elementary truncation baseline remains the control.

My own pull: the exact beta-transfer boundary estimate in (J), at the actual modular frequencies. It keeps
all ancestry without a limiting-weight approximation and makes the missing correlation explicit.

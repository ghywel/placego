# Review of Cloud's prime clocks and the integer lift

GPT, GC2930–GC2931, 11 November 2026. Review of CL776–CL777 at
`8a1edc4d`. The owner requested a manual review and strengthening.
Both scheduled automations remain paused.

Cloud's left-edge recurrence, first clock, depth-two closed form and
finite-field affine argument carry, with the scalar-period qualification
below. These are PROVED hand, two-party. The strengthenings below are
PROOF-SKETCH pending Cloud's independent read. GPT sub-agent reads and
small exact replays are self-checks. No new Lean compilation is claimed.

## Sources and prior work

Record searched using separate searches for integer lift, multiplicative
order and Gauss, plus the actual kit sources and catalogues. Complete
index refresh at 2026-11-11 19:06:45 UTC, kit
`72fdf4b4a7b3dfd7a1fb4d956f971cdb69552e18`, portal index timestamp
2026-11-11T19:06:34Z, fourteen open PRs. Candidate integer-lift hits in
arithmetic transport concern a different recurrence. No matching
odd-prime depth-two classification was found in this search. This is a
scoped comparison, with the general literature novelty question open.

Nersissian's integer lift and polynomial right diagonals are prior work.
The companion's binary reset theorem and backward-profile bound also
supply the method extended in this review. The kit already formalizes
`Rule30LeftReset.reset_periodic`, `Rule30LeftUnbounded.Sig_inj`,
`left_profile_bound`, `D_common_period_bound` and
`D_least_period_unbounded`. The finite-field extension below credits that
argument. [Diagonal bases, §12.1](https://arxiv.org/html/2609.25078v1#S12.SS1),
[companion, §4](https://arxiv.org/html/2609.25077v1#S4).

The finite quadratic-sum calculation below uses elementary root-of-unity
orthogonality. The application to this initial-value problem is the
proposed strengthening.

## The carried affine lemma

Use the chosen integer lift

    A_(t+1)(j) = A_t(j-1) + A_t(j) + A_t(j+1) + A_t(j) A_t(j+1),
    A_0(j) = 1 if j=0, and 0 otherwise.

Put u_n(t)=1+A_t(n-t). The negative-depth values are 1, u_0=2,
and u_n(0)=1 for n>0. Substitution gives, from time zero,

    u_n(t+1) = u_n(t) u_(n-1)(t) + u_(n-2)(t) - 1.

In particular u_1(t)=2^t. Writing x=u_2 gives x(0)=1 and
x(t+1)=2^t x(t)+1. Dividing by 2^[t(t-1)/2] and telescoping gives
Cloud's partial-theta expression.

Over F_p, suppose the preceding coordinates have common period P from T.
A period of updates at the next coordinate is an affine map

    F(x) = alpha x + beta,
    alpha = product of u_(n-1)(T+j), 0<=j<P.

If alpha is nonzero, F is a permutation. Its orbit length r is 1 or p
when alpha=1, and 1 or ord_p(alpha) otherwise. The coordinate is periodic
from T with period dividing P r. If alpha=0, the first zero multiplier
at z in [T,T+P) makes the coordinate P-periodic from z+1. This follows
by comparing updates at z and z+P, then inducting forward.

Thus a zero multiplier is necessary for an additional transient and
permits one. The least period of an individual coordinate can be a
proper divisor of P r. Cloud's depth-five period 2 at p=3, with shallower
common period 4, illustrates the distinction. For a prefix whose base
has least eventual period P, the extended prefix has period exactly P r.

## Exact second clock at every odd prime

Let p be odd and d=ord_p(2). The least period of u_2, including from
its initial time zero, is

    P2 = 2d  when d is even,
    P2 = pd  when d is odd.

The d-step update at phase zero has multiplier
alpha=2^[d(d-1)/2] and translation alpha S, where

    S = sum of 2^[-j(j+1)/2], 0<=j<d, in F_p.

When d is even, alpha=-1. Pair j with d-1-j. Their triangular
exponents differ by d(d-1)/2 modulo d, so the summands cancel.
Consequently S=0 and F(x)=-x. Starting at 1 gives orbit length 2.
This negation describes samples at multiples of d. The maps at other
phases can have different additive constants.

When d is odd, alpha=1. Define Sbar by replacing each exponent in S
by its negative. The triangular exponent is well-defined modulo d.
In S Sbar, put the second index equal to the first plus h modulo d.
For each h the inner sum is a constant times sum_j 2^(hj). It vanishes
unless h=0, since 2 has order d. For h=0 it is d. Hence

    S Sbar = d in F_p.

Since d divides p-1, S is nonzero. The map F(x)=x+S has orbit length p.
In either case the resulting prefix period is P2 and holds from zero.

To prove scalar minimality, let Q be any eventual period of x.
Comparing its recurrence at t and t+Q gives

    (2^Q-1) 2^t x(t) = 0.

Consecutive x values cannot both be zero. Therefore 2^Q=1 and d divides Q.
At sufficiently late times that are multiples of d, the stroboscopic
orbit forces Q/d to be divisible by 2 or p, respectively. This proves
least eventual period and least period from zero at once.

For odd d, each fixed phase modulo d traverses every field value once
in p blocks, because the within-block affine map has nonzero multiplier.
Thus every residue occurs exactly d times in a full period P2. An exactly
balanced residue sequence can therefore be periodic in this very lift.

For p=7, d=3 gives P2=21. For p=23 and 31 the theorem gives 253 and 155.
The distinction follows from the parity of d without assuming Artin's
conjecture.

## The third clock must reset

Depth two reaches zero at every odd prime. For even d,
x(d)=-1 and x(d+1)=0. For odd d, x(kd)=1+kS, so a k between 1 and p-1
makes it zero. The depth-three multiplier is x(t). The carried reset
lemma therefore makes depth three P2-periodic by time d+2 in the even
case, or by (p-1)d+1 in the odd case. Earlier resets are possible.

The prefix through depth three has least eventual period exactly P2,
since it includes depth two. This proves the plateau seen in Cloud's
first three clocks at every odd prime. If P_n is the least eventual
period of the prefix through depth n, then for n>=3

    P_n divides P2 [p(p-1)]^(n-3),
    P_n <= P2 p^(n-3).

Each subsequent coordinate adds at most one preceding prefix period to
the transient. The bounds follow by applying the affine lemma one depth
at a time.

## Every prime has unbounded left-prefix periods

This extends the known binary backward-profile proof. Fix a common
period P for depths through n and extend their eventual tails to
P-periodic profiles v_j. Let Sigma_j=(v_(j-1),v_j), for -1<=j<=n.
On the p^(2P) profile pairs define

    B(u,v) = (v shifted by one tick - vu + 1, u).

The recurrence gives B Sigma_j=Sigma_(j-1). Sigma_(-1)=(1,1) is fixed,
while Sigma_0=(1,2) differs from it in every characteristic. Any repeated
pair, iterated backward, would identify these two boundary pairs.
Therefore all n+2 pairs are distinct and

    n+2 <= p^(2P).

This proves unbounded common periods as depth grows for every prime.
Backward reconstruction also shows that a common period of the last two
coordinates is a common period of the entire prefix. Hence the prefix
period equals the least common multiple of those two scalar periods.

This lower bound concerns eventual tails at fixed depths. The onset
still varies with depth, while the centre samples u_t(t). A centre proof
requires additional control of these sampled phases.

## Cloud's 2-adic cascade with explicit error bounds

Cloud's parked pull in INSTINCT also has a short proof. Fix k>=1 and
T=k+1. For t>=T, u_1(t)=0 and u_2(t)=1 modulo 2^k. Thus

    u_3(t+1) = u_3(t)-1 mod 2^k.

This is an eventual congruence for each modulus. Over the integers,

    [u_3(t+1)+t+1] - [u_3(t)+t]
      = 2^(t-1) [u_3(t) u_2(t-1)+2],  t>=1.

Consequently u_3(t)+t converges in Z_2 to a constant C, with
v_2(C-u_3(t)-t)>=t-1. This makes the drifting clock precise.

Let r_k be the least r with v_2(r!)>=k. From T onward the depth-four
recurrence modulo 2^k is homogeneous, with multiplier u_3(t). Hence

    u_4(T+r) = u_4(T) product_(0<=i<r) [u_3(T)-i] mod 2^k.

A product of r consecutive integers is divisible by r!. Thus u_4=0
modulo 2^k from T+r_k onward, and the next recurrence gives u_5=u_3
from T+r_k+1 onward. Since r_k<=2k, the simpler onsets 3k+1 and 3k+2
also hold. This proves u_2 tends to 1, u_4 tends to 0 and u_5-u_3
tends to 0 in the 2-adic topology, while u_3 tracks C-t.

The next useful proof target is the depth-six recurrence after inserting
these controlled errors. It must retain the modulus-dependent onset.
The first steps already justify Cloud's proposed counter and running
product mechanism. They give a proof before any enlarged diagonal census.

## Evidence corrections

The complete report and the probe implementations were read. Existing
output files remain historical measurements.

- CRT is a bijection of residue spaces. A distribution theorem along
  A_t(0) would require joint equidistribution modulo the product. For
  example, the repeating integers 0,0,4,1,5,5 have uniform marginals
  modulo 2 and 3 but joint table [[2,1,0],[0,1,2]]. Cloud's selected
  contingency tests detected no departure from their reference model.
- Growing primitive wheel periods alone do not settle the centre.
  The wheels f_j(t)=1 when t=j modulo 2^(j+1), and 0 otherwise, have
  increasing primitive periods, while f_t(t)=1 for every t. A proof
  needs the Rule 30 relation between successive wheels and their phases.
- The valuation experiment compares coarsened v_2(A_t(0)) with
  coarsened v_2(t+1). It leaves other digit and carry laws open.
- The raw uniform-pair Pearson statistic uses overlapping pairs.
  Its multinomial reference with p^2-1 degrees of freedom needs
  recalibration. Under IID uniform symbols, row and column fluctuation
  modes coincide up to endpoints. Their sum contributes twice a
  chi-square with p-1 degrees of freedom, and the interaction modes
  contribute an independent chi-square with (p-1)^2 degrees of freedom.
  This decomposition is a hand self-check. Cloud's later statistic
  removes the fitted marginal modes. A replay can use the saved raw
  tables and the corrected reference without regenerating the trace.
- Chi-square tails in the block test evaluate an asymptotic reference
  distribution. They are not exact finite multinomial probabilities.
  The saved modulo-5 verdict is False at the declared threshold. Its
  displayed 0.0005 is rounded. Cloud owns the pending fresh-data run.
- The arithmetic sums and spectra describe the tested windows and
  observables. They do not establish asymptotic independence or exclude
  all arithmetic descriptions.

The kernel experiment has a positive rigorous interpretation. Subject
to validation of its generated trace, differing finite prefixes prove
that the corresponding infinite kernel elements differ. The reported
counts give at least 511, 364, 156 and 400 kernel elements in bases
2, 3, 5 and 7. They also bound the states of an automaton reading digits
least-significant first, with leading-zero conventions fixed. Extracting
one witness position per distinct pair would produce a compact finite
certificate. A proof that such distinguishable families grow without
bound would imply nonautomaticity, and hence nonperiodicity, in that
base. That uniform construction remains open.

## Small independent controls and next read

The independently written Python check compares full integer rows
through time 12 with the diagonal recurrence and both closed forms.
For the ten odd primes through 31 it checks a complete phase orbit,
every divisor of its candidate period, the finite-sum identity, the
odd-order residue counts and the forced third-coordinate reset. All
pass. The false prediction that all second periods equal twice the
order is rejected. These are tiny exact self-checks of the hand proofs.

The shared store holds the verified raw files
`cited/gpt/gc2930-lift-check.py`, SHA256
`b743b802cb49d31396b4a8efc26e11365ac2090d16fb80614fd0ab785c7211b2`,
and `cited/gpt/gc2930-lift-check.json`, SHA256
`37d79b7a10adbb5d2fcca81d3834939c7f29a8051fb7f6bf326b8efdfd4d4cab`.

Cloud's next read is the odd-order sum identity, scalar minimality,
forced third reset, the all-prime backward-profile transfer and the
2-adic error bounds. These
are complete proposed proofs. The most direct formalization would first
prove the affine/reset lemma, then the quadratic-sum identity and the
physical diagonal bridge. The centre question still needs a statement
uniform in the moving depth.

My own pull: carry the 2-adic clock and reset error bounds into the next diagonal.

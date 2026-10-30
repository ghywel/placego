# DQ-024: the spatial geometry of the known edge odometer

GPT, 29 October2026, GC2157. **PROOF-SKETCH, awaiting Local's carrying read on resumption.**
This is a hand application of known odometer and tree-boundary machinery, not a new density theorem,
formal certificate or proposed portal package. No dynamics run or larger census was performed.

The pull is to keep the actual single seed while changing the question. Instead of seeking an
autonomous law for a few parity coefficients, ask how many different spatial edge prefixes occur as
the orbit phase varies. The known periods answer that counting question exactly. They also turn the
missing lower-density bound into a precise geometric statement, without supplying its proof.

## Sources and conventions

Record searched: orbit closure, odometer, prefix count, Hausdorff/Minkowski dimension, capacity,
DQ-024. Known kit main932cf8dde039b89b1dcbe9636867bb1b2057fef0 actual sources read:

- `equivalents/Rule30Equivalents/Odometer.lean`: `agree_G_iff`, `G_bits`, `ψ_natCast`,
  `ψ_add_one`, `continuous_ψ`, `ψ_injective`, `range_ψ`, `isClosedEmbedding_seed`, `range_seed`.
- `equivalents/Rule30Equivalents/TFunctionCycles.lean`: `iterate_mod_iff_dvd`, `Phi_cycle`,
  `seed_rows_return_iff`, `per_unbounded` and the least-period interfaces they use.
- `lean/Ruliology/CellularAutomata/Rule30RightPeriods.lean`: least exponents, their monotonicity
  and unit increments, `leastExp_antiperiod`, `leastExp_two_mul_le`, `leastExp_le_B`,
  `per_upper_half`; `Rule30RecordCharge.lean`: `Q_le_iff`, `pow_le_threshold`, `exponent_le_Q`.

The fresh kit/portal index at12:15:19Z lists21open kit PRs and0added/changed/no-longer-listed sources.
No matching geometric theorem was identified in the searches; that is not a novelty certificate.
The odometer conjugacy is established prior art, not discovered here. Primary background actually read:

- Coven–Pivato–Yassawi, [Prevalence of Odometers in Cellular Automata](https://arxiv.org/pdf/math/0511030),
  Theorem1 and its proof, preprint2005, Proceedings AMS135 (2007),815–821: finite-column periods
  construct the odometer conjugacy. The metric conclusions below require additional counting.
- Lyons, [Phase Transitions on Nonamenable Graphs](https://rdlyons.pages.iu.edu/pdf/review.pdf),
  Journal of Mathematical Physics41 (2000),1099–1126, author-version section6: tree-boundary
  dimension, growth and capacity. The elementary homogeneous-tree argument is written out below;
  no percolation or random-walk conclusion is being imported as a CA theorem.

Let `Phi(x)=x XOR ((x<<1) OR (x<<2))`, and let R_j(t) be bit j of Phi iterated t times from1.
These are right-edge depth coordinates, not fixed physical spatial columns of the full pyramid.
Let e_j be the least exponent of the temporal period of R_j, and

    J_k = max {j : e_j <= k},       a_k = J_(k-1)+1  (k>=1).

Known facts give e_0=0, monotone increments0or1, unbounded e_j, e_(J_k)=k and e_(J_k+1)=k+1.
The whole prefix0..j has least period2^e_j: it contains R_j, and all earlier periods divide its period.

Let K be the closure of the actual orbit rows in the one-sided binary product space. Fix the metric

    d(x,y) = 2^(-r),  r = the first coordinate where x and y differ;  d(x,x)=0.

In particular the common bit0 is1. This normalization matters for exact energy constants below.
The known map psi=ψ1 is a homeomorphism from the2-adic integers onto K, conjugating addition of1
to G. Write mu for the image of uniform2-adic Haar probability under psi.

## Exact prefixes and the free spatial positions

**Claim1.** There are exactly2^e_j allowed prefixes through coordinate j. Each has the same mu mass
2^(-e_j). At coordinate j, every existing prefix has one continuation if the exponent stays unchanged,
and two continuations if it increases.

Proof: projection to coordinates0..j maps the orbit onto a finite cycle of least length2^e_j.
Projection of its closure has the same finite image. Projection from this cycle to the previous
prefix cycle has equal fibers, of size the period ratio, either1or2. Two distinct children with
the same parent must have opposite new bits. Haar phase is uniform on each finite residue cycle,
which proves the masses. Thus the prefix tree has level-dependent branching, but no branching
imbalance between different prefixes at the same level.

The positions a_1,a_2,... are consequently free coordinates for this *space of possible phases*.
More explicitly, for desired values z_1,...,z_k, start with t_0=0 and recursively set

    t_k = t_(k-1) + 2^(k-1) * (z_k XOR R_(a_k)(t_(k-1))).

The antiperiod at a_k is2^(k-1). This flips its bit when needed, while leaving all preceding
coordinates unchanged. It gives the unique phase residue t_k modulo2^k with those free bits.
Under mu these coordinates are independent fair bits, because every k-bit assignment has mass2^-k.
This coding need not be quick to evaluate: it still asks for actual R values at the selected phases.

It does **not** make the actual seed's selected spatial bits fair. At phase0 every bit j>0 is white.
Every finite-time physical row has finite support, so its free-coordinate word is eventually white.
These orbit points are countable and dense in K, and have mu measure0. No converse identifying
all eventually-white free-coordinate words with finite-time rows is asserted. Nothing here gives
a typicality statement for the centre column or a faster algorithm to compute it.

## The exact metric dictionary

**Claim2.** If alpha and beta are distinct2-adic phases, and k is the2-adic valuation of alpha-beta,

    d(psi(alpha),psi(beta)) = 2^(-J_k-1).

They agree modulo2^k, so all coordinates through J_k agree. At coordinate J_k+1 the period is
2^(k+1) and the half-period2^k is an antiperiod. The two residues there differ by exactly that
half-period, so this is their first differing coordinate. This proves the formula.

G itself preserves spatial-prefix distance (`agree_G_iff`). That does not say psi preserves the
usual2-adic distance: the latter is2^-k, whereas the image distance is2^(-J_k-1). DQ-024 would say
that the image distance is the square of the phase distance up to a subpower correction. Topological
conjugacy alone gives no such quantitative assertion.

## Dimension is exactly the missing lower density

For length n>=1, the allowed prefix cylinders are exactly the nonempty radius2^-n closed balls in K.
Their number is

    N_n = 2^(e_(n-1)).

Distinct length-n prefixes cannot share such a ball. Hence the lower and upper box dimensions are
respectively liminf and limsup of e_j/(j+1).

**Claim3.** The Hausdorff dimension is also

    dim_H(K) = liminf_(j->infinity) e_j/(j+1).

For the upper bound, let s exceed this liminf. Along a subsequence of n, the sum of the s-th powers
of the diameters of all length-n cylinders is at most2^(e_(n-1)-sn), which tends to0. They cover K.

For the lower bound, let0<s<liminf. There is a finite constant C such that every length-n cylinder
has mu mass2^(-e_(n-1))<=C*2^(-sn). If a nonempty set U has diameter delta with
2^(-n-1)<delta<=2^-n, all its points have the same first n coordinates. Thus
mu(U)<=C*2^s*delta^s. Summing over any small-diameter cover gives a positive lower bound on its
total s-content. Singletons have mu mass0 since e_j is unbounded. This proves the lower bound;
when the liminf is0 the lower bound is automatic.

The known half-rate theorem gives upper box dimension at most1/2. Therefore the original conjecture
has the exact reformulation

    e_j/j -> 1/2    iff    dim_H(K) = 1/2.

The forward implication also makes both box dimensions1/2. The reverse uses the *known upper bound*
as well as Claim3. No equality of dimensions has been established here. This is the same unresolved
lower bound in another language, not a proof obtained by changing language.

There is a separate useful distinction: the temporal topological entropy of G on K is0. Indeed G
is an isometry, so the maximum of d(G^t x,G^t y) over any finite time interval is just d(x,y).
The number of separated initial states at fixed resolution is finite and independent of the time
interval. Positive spatial fractal dimension, if proved, would coexist with zero temporal entropy.

## An exact energy test, and a critical obstruction already forced by the upper bound

For s>0 and any probability nu on K, define its s-energy I_s(nu) as the integral of d(x,y)^(-s)
over two independent nu samples, allowing infinity on the diagonal. Expanding the kernel by common
prefix length, with all terms nonnegative, gives

    I_s(nu) = 1 + (2^s-1) * sum_(j>=0) 2^(sj) * sum_(C length j+1) nu(C)^2.

There are2^e_j such cylinders. Cauchy's inequality bounds their mass-square sum below by2^-e_j;
mu achieves equality at every level. Consequently its extended energy is minimal, and

    I_s(mu) = 1 + (2^s-1) * sum_(j>=0) 2^(sj-e_j)
            = sum_(k>=0) 2^(s*(J_k+1)-k-1).

The second equality also follows directly from Claim2: the valuation k of the difference of two
independent Haar phases has probability2^(-k-1). This is a useful normalization check, not a
sampling assumption about a chosen physical trajectory.

**Claim4.** Unconditionally, every probability on K has infinite1/2-energy. Equivalently, the
1/2-Riesz capacity of this metric space, defined as the reciprocal of the minimum energy, is0.

Use only the existing stronger finite upper bound e_(2m)<=m+Q(0,m). For m>=1 choose
q=floor(log2(m))+1. The known inequality threshold(0,q)>=2^q>m and `Q_le_iff` give Q(0,m)<=q.
Also2^q<=2m. At j=2m, the critical series term therefore satisfies

    2^(j/2-e_j) >= 2^(-Q(0,m)) >= 1/(2m).

The even-index subseries diverges. Thus I_(1/2)(mu)=infinity, and the levelwise Cauchy lower bound
forces the same for every nu. This is a hand corollary of the known record-charge bound plus the
standard energy identity. It does not refute Hausdorff dimension1/2: zero capacity at the critical
exponent is compatible with that dimension. No novelty or new submission is claimed for this corollary.

In contrast, the still-open target has the equivalent energy formulation

    for EVERY 0<s<1/2,   sum_(j>=0) 2^(sj-e_j) < infinity.

If e_j/j tends to1/2, each of these series has an exponentially decreasing tail. Conversely their
convergence makes e_j-sj tend to infinity for each such s, forcing liminf e_j/j>=1/2; the known
upper bound finishes the equivalence. No one of these positive-s convergence statements is proved
in this note. Merely reproving divergence at the critical exponent would not advance that task.

## What this teaches, and the next discriminating question

The edge's exponent counts exactly how many independent phase choices fit inside a spatial prefix.
That makes the phrase 'memory per cell' precise for the orbit closure. The wall frame's free bits
belong to a different construction; equal dimension or equal numerical counts would not supply a
map between them. No wall-to-edge bridge has been proved.

This view also exposes the risk in talking about randomness: the phase ensemble has independent
free coordinates, but a particular orbit point, including the root itself, need not look typical.
The actual unresolved issue is how densely the free positions a_k are placed, not whether their
possible labels fill a binary tree; the latter is already exact.

Next useful hand question: can actual-root ancestry force enough spatial branchings to make even
one subcritical energy finite, or can an exact geometric comparison bound the free-position spacing?
A general odometer conjugacy or arbitrary placement of free coordinates cannot do that. Do not
open a dimension-estimation simulation, larger gap table or seed census to replace the missing
inequality. Reopen the generic parity-compression route only with a specific actual-seed relation
that determines the omitted support intersections (GC2156). Local's independent read is pending;
Local remains offline and no M5 run is queued.

## GC2220: the known accounting bound restarts in every spatial window

GPT,30 October2026. **PROOF-SKETCH, solo hand argument; no new compilation or independent carrying read.**
The pull was to turn GC2205's exceptional-block count into a bound uniform over starting depth,
including windows cut inside a long block. The cheap objection is decisive: subtracting two upper
bounds on initial prefixes does not bound their difference. The actual kit supplies a better route.
Its `Path` assumptions permit restarting at any pair of diagonals, with the inherited resource.
This is an application of the existing accounting theorem, not a new mechanism for the00 transition.

### Exact source and prior-art comparison

Record searched: Assouad, uniform/spatial windows, local covering, shifted half-rate and exponent
bounds. Actual kit main932cf8dde039b89b1dcbe9636867bb1b2057fef0 carrying definitions/proofs read:
`Rule30RecordCharge.Path`, `record_potential`, `exponent_bound_before_threshold`, `Q_spec`,
`Q_le_iff`, `pow_le_threshold`; `Rule30RightPeriods.pairPath` and `leastExp_two_mul_le`.
Crucially, `Path` has **no condition on resource(0)**. File identities:

- `Rule30RecordCharge.lean`: SHA256 ce3fa36b5f961f39ee6fc7e6df1230be67080127165fb1ae924ea670f805c96c.
- `Rule30RightPeriods.lean`: SHA256 9ef3c374ff394f9727706b54f25a7d8fa1dce329efc6cd4f6c4821f6c03975ad.
- `equivalents/Rule30Equivalents/Odometer.lean`: SHA256 a4d27a2590fd75f6edbc6129689f16fbeecc87b252d71cf3d3c5b468b0f81512;
  its already-read conjugacy supplies the finite prefix cycles used above.

The complete portal/open-PR refresh remains00:10:27Z,22openPRs. PR55 head
918284e3b0097b7a6e896d56506f86a1cc813128 already reuses RecordCharge for right-bounded prefix
clocks; its corresponding interfaces were compared, not claimed as new. Portal e67465's
`adjSrc_density_le_half` counts temporal occurrences of `cell(t,0) AND cell(t,1)`, a different
sequence from the spatial period-growth flags here. No first-in-literature claim or submission
clearance follows from these searches.

Primary geometric background: Banaji–Rutar–Troscheit,
[Interpolating with generalized Assouad dimensions](https://pmc.ncbi.nlm.nih.gov/articles/PMC12255623/)
(2025), introduction equation1.1 and section2.1 Proposition2.1/proof read. The usual Assouad
definition asks for a uniform bound on the number of radius-r balls covering the portion of a
space inside any radius-R ball. The argument below counts our binary cylinders directly; it
does not import a Euclidean Moran-set formula into this ultrametric space.

### Restart the path, rather than subtracting prefix bounds

Write a general `Path nu` as (E,w,A), where E(0)=0, E(i+1)=E(i)+w(i), and w takes values0,1,2.
The resource axioms are

    w(i)=2  =>  A(i)=0 and A(i+1)+1=2^(nu+E(i+1)-1),
    w(i)=1  =>  A(i)<=A(i+1)+1.

For any a>=0 define

    E_a(i)=E(a+i)-E(a),   w_a(i)=w(a+i),   A_a(i)=A(a+i),
    nu_a=nu+E(a).

Since E is nondecreasing, all subtractions are exact nonnegative differences. The initial and
step axioms hold. Both resource conditions are inherited, because

    nu_a+E_a(i+1)-1 = nu+E(a+i+1)-1.

This identity also respects truncated natural subtraction. Thus the restarted triple is a
`Path(nu+E(a))`, with no need to find a zero-resource starting point.

Let T_nu(q) be the kit threshold: T_nu(0)=1 and

    T_nu(q+1)=T_nu(q)+2^(nu+T_nu(q)+q).

Induction in q gives T_nu(q)>=T_0(q). Applying the existing
`exponent_bound_before_threshold` to the restarted path, with
q=Q(nu+E(a),d), gives the sharper bound

    E(a+d)-E(a) <= d+Q(nu+E(a),d) <= d+Q(0,d).

The second inequality follows from threshold monotonicity in nu and `Q_le_iff`, not from a
heuristic about the resource. For the actual single seed, `pairPath` has E(i)=e_(2i). Hence

    e_(2a+2d)-e_(2a) <= d+Q(e_(2a),d) <= d+Q(0,d).             (1)

This includes d=0. It is uniform in the starting pair a.

For arbitrary j>=0 and N>=1, surround [j,j+N] by the even endpoints2a and2b, where
a=floor(j/2), b=ceil((j+N)/2). Put d=b-a and M=floor(N/2)+1; then d<=M.
Monotonicity of e bounds the desired difference by e_(2b)-e_(2a). Since
M<T_0(Q(0,M)), the same threshold argument at d gives

    e_(j+N)-e_j <= M+Q(0,M),          M=floor(N/2)+1.           (2)

For M>=1, `pow_le_threshold` gives Q(0,M)<=floor(log2 M)+1. Thus the number of doublings in
every N-letter spatial window is at most N/2+O(log N), with the constant independent of j.
In particular their upper Banach density is at most1/2. This is an upper bound only: no existence
of the ordinary density, positive lower density or sharpness is proved.

The argument handles partial blocks without classifying them. In particular it does not infer
that sparse exceptional events have small downstream influence; that inference remains invalid.

### Local covering of the actual orbit closure

Use the same K and first-difference metric as above. Fix a nonempty cylinder with prefix length
m>=1. Every such cylinder contains exactly

    2^(e_(m+N-1)-e_(m-1))

allowed extensions of length m+N, for N>=0. This is the equal-fiber property of the finite prefix
cycles. A length-m cylinder is a radius2^-m closed ball; its extensions are exactly the
radius2^-(m+N) balls needed to cover it. Branching plateaus can make balls at successive radii
coincide, but do not change this covering count.

Apply (2) with j=m-1. For every epsilon>0 there is a finite C_epsilon, independent of m and N,
such that this count is at most

    2^(M+Q(0,M)) <= C_epsilon * 2^((1/2+epsilon)*N).

Indeed M<=N/2+1 and Q(0,M)<=log2(M)+1; the remaining polynomial factor is dominated by
2^(epsilon*N). N=0 costs one ball. For arbitrary0<r<R<=diam(K), round R upward and r downward
to dyadic radii. The ratio of the rounded radii is at most4R/r, so the same bound holds after
changing C_epsilon. The largest-scale ball is K itself, also the common length-one cylinder.
Consequently

    dim_Assouad(K) <= 1/2.                                    (3)

This controls local covering uniformly in position and scale. It is stronger in scope than an
initial-prefix box-dimension bound, but follows from the same known accounting machinery.
The mathematical specialization and geometric deduction remain solo PROOF-SKETCH. No independent
review, formal export, new experiment, priority claim or portal package is asserted.

### What remains unsettled

Neither (2) nor (3) supplies a lower bound or solves DQ024. They also do not prove a uniform
critical estimate C*(R/r)^(1/2): the subexponential factor may be unbounded. The exact criterion
for that stronger estimate is bounded spatial-window excess

    sup_(j>=0,N>=1) [e_(j+N)-e_j-N/2] < infinity.

Next bounded hand discriminator: construct or refute an abstract flag word satisfying the exact
ruler-closing law while this excess is unbounded. That would identify whether a critical
constant needs more actual-root information. Such a word would be a symbolic control only,
not a Rule30 realization. Do not infer an actual-root counterexample from it or launch another
period census. The independent alternative remains the named bounded-type/Rote source comparison.

## GC2221: the ruler law permits unbounded critical excess

GPT,30 October2026. **PROOF-SKETCH, solo hand control, not an actual Rule30 orbit.** The GC2220
discriminator succeeds. This tests the exact carried closing law, including its conditional iff,
and the no111 rule. It does not assert compatibility with full temporal profiles, every other
known flag restriction or the complete `Path` resource axioms.

Record searched: ruler/exceptional/record-charge with sharpness, attainment, symbolic controls and
critical excess; current kit932cf8dd actual `Path` and threshold definitions, portal/open-PR index
00:10:27Z. GC2201/CL645/GC2205 supply the exact law and tower recurrence; GC2151/GC2197 already
show abstract Path tails need not determine density. The classical local-cover definition is the
same primary Banaji–Rutar–Troscheit equation1.1 read in GC2220. This is a sufficiency check on those
known mechanisms, with no novelty claim or new external theorem imported.

### Construction and every occurrence of the closing law

Start with x_1 x_2=10 and E_n=sum_(j=1..n) x_j. Set s_1=3 and e_1=1. Recursively define

    q_r=2^e_r,
    e_(r+1)=e_r+q_r,
    s_(r+1)=s_r+2q_r-1.

On the half-open integer interval [s_r,s_(r+1)), write the word

    1(10)^(q_r-1).

These intervals concatenate, cover the remaining positions and each contain q_r ones and q_r-1
zeros. Hence E_(s_r-1)=e_r, exactly the exponent used in the next block's rule. The starts are
3,6,21,4116,... and their exponents are1,3,11,2059,... . These are hand evaluations of the
recursion, not simulated Rule30 data.

Every11 starts at some s_r, and every such11 has a0 before and after it. Thus no111 occurs.
An occurrence1(10)^m1 with m>=1 must start at s_r, since its first two symbols are11. Within
that block it exists precisely for1<=m<=q_r-1. Its following symbol is0 for m<q_r-1 and1 at
m=q_r-1, when the next block starts. For larger m the next11 breaks the required alternation.
This checks every occurrence, not only the designated completed blocks. In particular it satisfies
the full carried assertion

    m<=2^E_(s-1)-1,
    x_(s+2m+2)=1 iff m=2^E_(s-1)-1

whenever1(10)^m1 starts at s. Each completed block shares its closing11 with the following
block's initial11. The sparse-count inequality e_next>=e+2^e is attained at equality in this
symbolic class; this says nothing about its attainment by the actual root.

### Unbounded excess, despite density one half

Summing the two recursions gives

    s_r=2e_r-r+2,
    2E_(s_r-1)-(s_r-1)=r-1.

Thus E_n-n/2 is unbounded. Within block r the signed excess2E_n-n is between r-1 and r+1:
the initial11 raises it twice, and each later01 pair keeps it within those bounds. Since
e_(r+1)>=2e_r, we have r/(s_r-1)->0. Therefore E_n/n->1/2, while the excess still diverges
along the displayed endpoints. A limiting half-density does not imply a bounded additive excess.

For an abstract homogeneous binary tree branching at exactly these positions, the covering ratio
at the critical exponent includes

    2^(E_n-n/2)=2^((r-1)/2),       n=s_r-1,

which is unbounded. This tree is an explanatory control; it is not asserted to be the edge orbit
tree. In particular it does not refute a critical covering bound for the actual K.

### A finite actual prefix does not remove this symbolic freedom

More generally take any finite actual flag prefix of length L ending00, with e=E_L>=1. Start the
same construction at s_1=L+1,e_1=e. No new11 or alternating antecedent can cross the final00.
All earlier complete implications retain their actual values, and the tail proof above applies
unchanged. Now

    2E_(s_r-1)-(s_r-1)=2e-L+r-1,

so the excess is still unbounded and the limiting density still1/2. Such a prefix exists in the
already-retained depth24 witness: its first14 flags are10110110100000 and E_14=6. This merely
checks the boundary hypothesis against existing data; no new prefix generation was performed.
The resulting continuation is symbolic, and may violate other actual-root constraints immediately.

**Disposition.** The exact ruler law and any such finite actual prefix cannot by themselves prove
a uniform critical covering constant. An actual-root proof would need an additional inequality
controlling excess accumulated across successive closures, or an equivalent restriction on their
realizable spacings. A larger sample or more manipulation of the same upper bound does not supply
that condition. Park this upper-bound-only route until such a specific relation appears.

The next independent carrying read is the previously indexed PR48 edge-clock restriction source,
whose full proof has not yet been read here. Its period/antiperiod obstruction may clarify which
symbolic continuations fail actual temporal compatibility. Read its exact head and linked sources
before adopting any consequence. This is a change of representation and a source review, not a
new request to the offline workers or a generic literature search.

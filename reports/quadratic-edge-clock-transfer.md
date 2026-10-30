# Boolean edge clocks: Cloud's breaks and a shared half-rate mechanism

GC2256, 30 October 2026. Cloud CL650/CL652 hand rules are independently carried below, with explicit period guards. The broader transfer in sections 3–4 is **PROOF-SKETCH**, GPT alone. No new Lean compilation, official replay, submission or density limit is claimed.

## 1. Objects and prior art

Write x_j(t) for bit j in the right-edge frame, with missing negative bits zero. E_j is the exponent of the least period of the **whole prefix** 0 through j, including j. It is not necessarily the least period of bit j alone. Let P_j = 2^E_j.

Record searched: CL642, CL649–CL652, GC2008, GC2153, GC2201 and GC2220; record_find queries for rule120, reversal, quadratic cocycles, Newton and binomial bases. The older sibling probe already includes Rule120: `tests/probes/lexicon/rule30_siblings.py` (4 October). Thus “no prior record” in CL652 is too broad. That probe concerns a finite period-two trace search, not the new edge comparison.

Current external index refreshed successfully at10:47:52UTC: kit `a6399ef15ff409d4dc0c5feb119b289aa31588a4`, 15 open PRs. Actual sources read: `TFunctionCycles.lift_iff`, `iterate_mod_iff_dvd`, the cycle construction; `Rule30DifferenceOrder.dif_shift_sum`, `difs_past`, `order_reset_before`, `order_countdown`; `Rule30RecordCharge.Path`, `record_potential`, `exponent_bound_before_threshold`; `Rule30RightPeriods.pairPath`. The complete PR55 `Rule30RightPrefixBound` at head `918284e3b0097b7a6e896d56506f86a1cc813128` already transfers the OR proof to general prefix clocks. Its `Clock.recurrence` specifically requires OR. This is the immediate predecessor of the proposed quadratic transfer, not a new prefix-clock idea. The relevant kit/equivalents catalogues and indexed portal/PR sources were searched. This is not an exhaustive historical literature search or a priority claim.

[Anashin–Khrennikov–Yurova, section 2.4.1, Theorem 2](https://arxiv.org/html/1111.3093v2) supplies the classical triangular-map framework. Bijectivity does not imply a single cycle or a fair sampling law. [Nersissian, sections 2 and 10](https://arxiv.org/html/2609.25078v1) supplies the known Pascal/OR-convolution support calculus. No new representation is claimed here.

## 2. The four carrying reads

For any triangular invertible map, the next prefix period is P or 2P according to the parity of the new bit's forcing over one old prefix cycle P. This is the existing lifting theorem.

**P17 (CL650), PROVED by hand, two-party for the even-period conclusion.** Reversing seed bit k preserves every lower stream and complements stream k at every time. It therefore preserves all prefix periods through k. Write A=x_k, B=x_(k-1), and use the common prefix period P=P_k in the original and reversed runs. Pointwise over F2,

```text
(NOT A OR B) XOR (A OR B) = 1 XOR B.
```

Consequently the two next-doubling flags differ by `(P mod 2) XOR parity_P(B)`. At P even this is exactly Cloud's criterion. At P=1 the extra 1 is essential: seed0, reversal k=1 gives seed2; the older bit0 stays zero, but bit2 changes from constant to alternating. All59 reported controls lie in the even-period scope. The explicit period-one formula and counterexample are GPT self-checks, not a further independent review. This is an elementary Boolean derivative combined with known lifting, not a new source of randomness.

**P21, PROVED by hand, two-party for the same even-period scope.** First reverse k-1, obtaining run B; compare B to B with bit k reversed. Apply P17 to B and its period P_k(B). This compares the pair-reversed run with the single-reversed run, not directly with the untouched run, and uses B's supplier weight. The period-one correction is unchanged.

**P23 and the structural part of P24, PROVED by hand, two-party.** Clamp bit30 to zero from time zero. The prefix period through30 equals that through29. The forcing at31 is x29, and at32 is x31. Their doubling flags are their respective weight parities over the preceding **prefix** cycle. Measuring either weight only over that supplier's own shorter least cycle could give a different parity. The reported finite frequencies are separate Cloud measurements.

**P25, PROVED by hand, two-party.** Changing only the gate at30 preserves the prefix through29. Over that common cycle, the next doubling flag is parity(A AND B) for AND and parity(A) XOR parity(B) for XOR. These identities do not compare later trajectories, which have already changed.

The complete `edge_reverse.c`, `edge_break.c` and `edge_break_analysis.py` were read. Their E_n output is a prefix clock, matching this scope. No Cloud trajectory was rerun and no independent resource receipt for those runs is asserted. A standalone P17 submission would package a short specialization of existing lifting; a reusable Boolean-derivative lemma is the more useful implementation target.

## 3. The quadratic difference identity

Consider any time-independent family of gates

```text
g_j(b,s) = b*s XOR alpha_j*b XOR beta_j*s XOR gamma_j,
x_j(t+1) = x_j(t) XOR g_j(x_(j-1)(t), x_(j-2)(t)).
```

The quadratic coefficient is1 at every depth j>=2. The three other coefficients may vary with j. The first two bits may use any invertible triangular update. OR is (alpha,beta,gamma)=(1,1,0); AND is (0,0,0). Hard clamping and time-varying coefficients are outside this theorem.

Let s be M-periodic, b(t+M)=1 XOR b(t), and let Delta h = g(b,s), with fixed gate coefficients. Then

```text
Delta (h(t+M) XOR h(t)) = s(t) XOR alpha.
```

Proof: difference the shifted sum and substitute the recurrence; the two b terms are complementary and the s terms equal. The Boolean derivative of g in b is s XOR alpha. Beta and gamma cancel.

If M is a power of two, Delta^M is shift-by-M XOR identity. Therefore

```text
Delta^(M+1) h = s XOR alpha,
Delta^(M+1+r) h = Delta^r s       for every r>=1.
```

The second line is identical for OR and AND. It is the exact line used in the kit's reset/countdown proof. For nonconstant s, if d(s) is its least vanishing difference index, d(h)=M+1+d(s). Constant s needs separate treatment; it is not covered by that equality.

Define order(f,L) exactly as the kit: the largest r<=L-1 for which Delta^(L-r)f=0, with value0 if there is no positive such r. For an L-periodic stream this agrees with L-d(f), capped at L-1. The identity proves:

- If h is complemented by a shift2M, order(s,M)=0. For M=1 this follows from the cap. For M>=2, positive order would give Delta^(M-1)s=0, hence Delta^(2M)h=0, contradicting complementation.
- order(s,M)<=order(h,2M)+1. If the left side is0 or1 this is immediate. Otherwise set r=M-order(s,M)>=1 in the identity; the required vanishing index is2M-order(s,M)+1.
- An M-antiperiodic stream has order(h,2M)=M-1, as in the unchanged kit theorem.

Thus the algebraic kernel transfers to every gate in this family. This is a generalization of the known proof, not a replacement mechanism.

## 4. Whole-prefix half-rate bound, including shifted windows

Fix any seed (finite or infinite binary), any starting depth a>=0, and let nu=E_a. Triangular invertibility gives periodic prefix orbits, E_(j+1)-E_j in {0,1}, and complementation of the new bit after the old period whenever this difference is1. No individual-period monotonicity is needed.

At pair i define

```text
e_i = E_(a+2i) - nu,
w_i = E_(a+2i+2) - E_(a+2i),
r_i = order(x_(a+2i), 2^E_(a+2i)).
```

These form the existing `RecordCharge.Path nu`:

1. w=2 means two doublings. The first makes the middle bit M-antiperiodic; the second makes the last bit2M-antiperiodic. Section3 gives r_i=0, and the last bit's antiperiod gives r_(i+1)+1=2^(nu+e_(i+1)-1).
2. w=1 with pattern01 makes the last bit M-antiperiodic, so r_(i+1)=M-1>=r_i.
3. w=1 with pattern10 uses the section3 countdown, giving r_i<=r_(i+1)+1.
4. w=0 needs no resource condition, exactly as in the current Path definition.

Write T_nu(0)=1 and T_nu(q+1)=T_nu(q)+2^(nu+T_nu(q)+q). The unchanged record-charge theorem gives

```text
E_(a+2m) - E_a <= m + Q_nu(m),
Q_nu(m) = least q such that m < T_nu(q).
```

Since nu>=0, Q_nu(m)<=Q_0(m). One extra bit adds at most1. Hence every window of n bits has exponent increase at most ceil(n/2)+Q_0(floor(n/2)). In particular the limsup exponent per depth is at most1/2 for AND as well as OR, and for spatial mixtures of these quadratic gates. The same cylinder-count argument as GC2220 gives an Assouad upper bound1/2 for each orbit closure; it supplies no lower bound, density existence or equality between rules.

**Status: PROOF-SKETCH.** The carrying target is the generic identity plus the three Path clauses above. The kit proves their OR specialization; no independent read of this broader scope has yet occurred.

## 5. A known exact AND comparison: the two-cell seed

[Skirrow's author notes, “on nearsighted binary counters”, Theorems1–2 and Corollary3](https://oeis.org/wiki/User:Natalia_L._Skirrow/on_nearsighted_binary_counters) describe the AND map from an n-cell block. This is public author research, not a referee or Lean certificate. The n=2 case supplies an exact comparison; it is not a new discovery here.

Here is an independent reconstruction for seed3. Let B_m(t)=binomial(t,m) modulo2. Lucas and Pascal give B_u*B_v=B_(u OR v) and Delta B_(m+1)=B_m. Consequently

```text
x_j(t)=B_(o_j)(t),
o_0=o_1=0,     o_j=1+(o_(j-1) OR o_(j-2)) for j>=2.
```

The seed values and the AND recurrence establish this by induction. For j>=2 the least period is2^bit_length(o_j): the highest set bit is essential in the Boolean monomial B_o. This avoids mistaking a merely available period for a least one.

For completeness, the n=2 closed form can be checked without relying on a numerical fit. Let U(q) read the binary digits of q in base4, let v=v2(q), and q>=1. Then

```text
o_(3q)   = 6U(q) - 4^(v+1),
o_(3q+1) = 6U(q) - 2*4^v,
o_(3q+2) = 6U(q) + 1.
```

Proof by blocks: write A=o_(3q). The preceding value is A-1, and A has lowest set bit2v+1. Thus 1+(A OR (A-1))=A+2^(2v+1), the middle expression. The first two expressions have OR equal to6U(q), yielding the third. Finally their last two values have OR6U(q)+1; the next is6U(q)+2. Binary carry gives

```text
U(q+1)-U(q) = (2*4^v2(q+1)+1)/3,
```

so that next value is exactly the first expression for q+1. The base values at j2,3 are1,2. This also proves the recurrence is nondecreasing.

If 2^m<=q<2^(m+1), the three values lie between2*4^m and2*4^(m+1)-1. Thus their period exponents lie between2m+2 and2m+3. Prefix exponents are therefore2log2(j)+O(1), with limiting doubling density0. This is a known nontrivial infinite orbit with slow clocks. It neither determines the density for other AND seeds nor the unknown OR limit.

Even more simply, the AND map fixes every seed with no adjacent11, including seed1. OR's unbounded-prefix theorem for nonzero finite seeds cannot transfer. Equal finite frequencies for Cloud's64 selected seeds therefore do not identify a universal asymptotic law.

## 6. What this suggests next

The useful comparison is the destruction of the singleton Newton support, not another density estimate. AND from seed3 closes on one basis element per column. Under OR, the two linear supplier terms create a symmetric difference of supports as well as their OR-convolution. That calculus is already known from Nersissian and our GC2008; any new work must identify a preserved or controlled class of supports, not rename it. A bounded next hand question is whether the first non-singleton perturbation of the domino has an invariant finite-component description. An uncontrolled support-size increase is a precise reason to park that route.

No Parry copy is needed for this step. The owner declined sourcing that paper; its unread comparison stays parked.

## 7. One frozen finite control (GC2256; pre-run specification)

Exact source `tests/probes/quadratic_edge_clock_control.py`, SHA256 `47b14a16401150195675b5c28b64add653f4aee25c65a1a92f4698659cc07810`; unchanged supervisor `tests/probes/wolfram/run_capped.py`, SHA256 `c8c58b49e032fc4c20b61675adc4194646713e692a51815996791ac8943ffc56`. Syntax-only py_compile passes. No numerical execution before this freeze.

Prediction: all80 fixed cases (eight homogeneous quadratic gates plus two prescribed spatial mixtures, eight fixed seeds,12bits) satisfy literal/ANF equality, minimal-prefix/lifting equality, all800 pair-resource clauses and6240 spatial-window bounds. The known seed3 singleton formula must match1024 independently evaluated binomial cells. Counterfactual: any mismatch defeats the proposed universal implementation or exposes a scope error; retain the failure and do not rerun or enlarge. This is a discriminating implementation control, not proof by enumeration or a density sample. Searches and carrying source are in sections1–5.

Independent controls: explicit four-entry truth tables versus a bit-parallel ANF; first actual return of each prefix versus lifting parity; direct cyclic differences for resource; integer binomial coefficients for the known domino. Unexpected check: the uncorrected period-one reversal criterion must be rejected by the explicit seed0/bit1 example. Fixed zero, single-bit, domino, separated, alternating and mixed-bit seeds keep constants and active cases distinct.

Intel host measured before launch:8physical/16logical cores,16GiB RAM, about6884MiB free+inactive,161.25MiB swap used, load about2.1; no research compute job running. Exactly one Python compute process/thread, no payload subprocess creation, nice10. Its60second RLIMIT_CPU is therefore an aggregate bound on all research payload CPU, not an inferred multithread/tree budget. The supervisor and its short monitoring commands are overhead, recorded separately; no claim that the existing runner provides a hard aggregate CPU limit over that overhead. This tiny control is not a substantial multistage computation. Wall30s, RSS768MiB, file16MiB, stage disk128MiB, process-group/tree cap2 (time wrapper plus payload), launch free+inactive4096MiB, running floor3072MiB, swap growth64MiB. No concurrent job or GPU. Stop on any limit, monitor failure or failed assertion; no automatic repair/retry. All output stays in one fresh scratch stage and will be retained by digest. A stage lasting less than the sampling interval may have zero periodic monitor samples; then only launch gates and actual child measurements are claimed.

## 8. GC2257: the fixed control passed once

Freeze commit `9a8b4ea6`; actual execution10:59:07UTC. COMPLETED rc0. All80cases,800pair clauses (339weight0,344weight1,117weight2),6240windows and1024domino cells passed. The period-one counterexample rejects the omitted correction. No repeat or enlargement.

Actual time receipt:0.09s child wall,0.07s user+0.01s system,14,688,256bytes peak RSS. Supervisor wall0.55s and CPU0.099s. Launch headroom6852MiB free+inactive,161.25MiB swap. The process ended before a periodic sample, so zero sampled RSS/pressure maxima are **not measurements of zero usage**; ongoing pressure/swap stability is not independently sampled. No leftover was detected; no cleanup signal was needed. Outputs total about32KiB before the launcher receipt.

Raw files are retained, with verified TLS raw-body upload and byte-exact readback, at shared-store `cited/gc2257-quadratic-clock-control/`. Manifest SHA256 `1657a65cf54ad846f0918711d5a2d3f0f2daec27f7acd1ed71a6675f9dc1c385`. The finite control validates implementation and boundary conventions; sections3–4 remain solo hand results.

## 9. GC2258: the first genuine domino branch has an exact label

**PROOF-SKETCH, hand only.** This uses the known support calculus and section5, not an additional run. First eliminate apparent perturbations that merely change time: the AND orbit of3 begins3,7,11,15,19. In particular flipping just bit2,3 or4 of3 gives an already-known phase. The first single higher-bit flip outside this family is bit5, giving35.

More generally the only indices j>=2 for which3 XOR 2^j belongs to the domino's forward orbit are

```text
j=2, or j=3*2^m, or j=3*2^m+1   (m>=0).
```

They are exactly the positions where o_j is a power of two, as follows from the closed form. Each temporal bit has one such spatial position. If time t has two or more set bits, at least two of those positions are black, so it cannot give a single added bit. A one-bit time gives exactly the matching position because the positive o_j are strictly increasing. This is a direct consequence of the credited domino formula.

There is a simpler exact detector for the first departure. Under the AND map with x0=x1=1, write u=x2, v=x3, w=x4 and z=x5. Then

```text
u'=u XOR 1,  v'=v XOR u,  w'=w XOR uv,  z'=z XOR vw.
C = z XOR uvw is invariant.
```

The first three equations are a three-bit binary counter. If u=0, the new product u'v'w' is vw; if u=1, it is0. In both cases the product changes by vw, exactly as z does. Thus C is a conserved **prefix branch label**, with eight states in each C-class, each forming an8cycle. It is not a spatially summed conserved density, and has no relation to a claimed conservation law for Rule30.

Seed3 has C=0; seed35 has C=1. Since the six-bit quotient is invertible, these two quotient cycles never merge. The domino identity x5=x2*x3*x4 therefore detects an actual orbit-class difference, not merely a poor choice of phase.

For seed35 the all-time Newton supports through j9 are obtained by multiplying B_a B_b=B_(a OR b), cancelling equal terms, then incrementing indices; insert the seed's constant term at j5:

| j | support of x_j(t) |
|---|---|
| 0,1 | {0} |
| 2 | {1} |
| 3 | {2} |
| 4 | {4} |
| 5 | {0,7} |
| 6 | {5,8} |
| 7 | {6,8,9,16} |
| 8 | {8,9,10,15,22,25} |
| 9 | {9,10,11,12,25,27,31,32} |

For the final step the forcing's index31 occurs in exactly three products: (15,16), (22,9), (25,6); it survives parity and integrates to32. All these are polynomial identities in t, not observations over a finite time window. A nonzero Newton polynomial of largest index d has least dyadic period2^bit_length(d), so the two prefix exponent histories agree through j8, namely0,0,1,2,3,3,4,5,5, but E9 is5 for seed3 and6 for seed35. This does not refute a law retaining the full upstream profiles. It shows exactly why the recorded period history alone loses information.

The hoped-for two-term support class already fails at j7; six and eight terms follow. Park that specific ansatz. Reopen only with a representation that controls the actual cancellations, not a longer support list or a density fit. The prefix label and generic upper bound remain useful without deciding growth for seed35.

## 10. GC2258: the upper bound actually covers every two-input Boolean gate

The quadratic-coefficient-one restriction in sections3–4 is unnecessary for the **inequalities**. Write an arbitrary gate as

```text
g(b,s)=lambda*b*s XOR alpha*b XOR beta*s XOR gamma,
lambda in {0,1}.
```

The shifted identity becomes Delta^(M+1)h=lambda*s XOR alpha, and for r>=1 becomes Delta^(M+1+r)h=lambda*Delta^r s. For reset-before with M>=2, positive old order would force Delta^(2M)h=0 for either value of lambda, contradicting the required antiperiod. For countdown, old vanishing forces new vanishing in the forward direction; no cancellation or division by lambda is used. Both implications therefore still hold when lambda=0. Reset-after is the unchanged antiperiod identity. Thus the same Path proof covers **all16** choices of g, with arbitrary time-independent spatial variation of all four coefficients. It assumes own-bit XOR and only the two older bits as inputs; arbitrary longer-memory T-functions are not covered.

Equivalently, the Boolean derivative g(1 XOR b,s) XOR g(b,s) is a function of the single bit s, hence one of0,1,s,NOT s. One additional time difference removes its constant term. That is the common reason for the upper bound. The stronger exact difference-index equality for nonconstant s in section3 still requires lambda=1.

For the affine subclass lambda=0 (allowing spatially varying affine coefficients), an even stronger standard linear-algebra bound applies. On n prefix bits the map is Ax+c with A unitriangular. Add one homogeneous coordinate: the resulting(n+1)-dimensional matrix is I+N with N^(n+1)=0. In characteristic2, (I+N)^(2^r)=I+N^(2^r). Hence every prefix period divides2^ceil(log2(n+1)). With c=0 the augmentation is unnecessary and n replaces n+1. This is a bound, not the exact period for every seed.

This all16 extension is **PROOF-SKETCH** and has not been rerun or compiled. The finite control of section8 tested exactly the earlier ten quadratic families; it is not described as a test of the enlarged class. Known T-function, nilpotent-matrix and record-charge machinery are credited. No novelty clearance, new submission or asymptotic equality is claimed. The next useful carrying target is this generic vanishing argument, followed by a minimal reusable formalization if accepted; DQ009 remains an independent alternative.

## 11. GC2278: exact static implementation obligations

**PROOF-SKETCH; implementation map, not compiled code.** The actual kit at
`a6399ef15ff409d4dc0c5feb119b289aa31588a4` and PR55 at
`918284e3b0097b7a6e896d56506f86a1cc813128` were read again. In particular,
PR55's `Clock.recurrence` is explicitly OR, and its `Clock.exponent_zero`
is zero. Reuse its proof organization with credit; neither field can simply
be asserted for arbitrary gates or a shifted window.

The smallest algebraic interface is a fixed gate `g : Bool -> Bool -> Bool`
and its derivative `D_g(s)=g(true,s) XOR g(false,s)`. This unary Boolean
function is constant, identity or complement; its ANF is `alpha XOR lambda*s`.
The proposed replacements for the OR-specific lemmas are:

1. `dif_shift_sum_gate`: under s(t+M)=s(t), b(t+M)=NOT b(t) and
   h(t+1)=h(t) XOR g(b(t),s(t)), the first difference of h(t+M) XOR h(t)
   is D_g(s(t)). This needs no dyadic assumption on M.
2. `difs_past_gate`: for M=2^v and k>=0,
   Delta^(k+2+M) h = lambda*Delta^(k+1) s.
   Reuse `difs_add`, `difs_two_pow`, `difs_xor` and `difs_const`.
   Multiplication by the fixed Boolean lambda commutes with every difference;
   prove by its two values. No inverse implication is used.
3. `order_reset_before_gate`: if h(t+2M)=NOT h(t), then order(s,M)=0.
   M=1 follows directly from `order_le`. For M>=2, positive order implies
   Vanish(M-1,s); use k=M-2 in item 2. The result would be both
   Delta^(2M)h=0 and Delta^(2M)h=1, a contradiction for either lambda.
4. `order_countdown_gate`: order(s,M)<=order(h,2M)+1. For old order r<2,
   use nonnegativity. Otherwise r<=M-1, so k=M-r-1>=0 and item 2 sends
   Vanish(M-r,s) to Vanish(2M-(r-1),h). Apply `le_order_iff` at r-1.

`order_of_antiperiod` is unchanged. For a shifted prefix window, use
nu=E_a, e_i=E_(a+2i)-nu and the actual period 2^(nu+e_i) in the resource.
The four step patterns are 00 (no condition), 01 (antiperiod gives resource
M-1), 10 (item 4), and 11 (item 3 plus antiperiod at the next scale).
These prove exactly the existing `Path nu` fields. Keeping the subtraction
in e_i is what supplies `Path.exponent_zero`; no assumption E_a=0 is made.

The prefix-period lift is a separate obligation: a cycle of the old prefix
has a constant return XOR on the new bit, so it either fixes or complements
that bit. This proves period P or 2P and the needed antiperiod for own-bit-XOR
updates. It uses the known triangular-map lifting mechanism, not OR.
Optional affine/choked refinements remain separable from this core.

## 12. GC2278: curiosity pull — a fixed dyadic phase clock can be absorbed

**PROOF-SKETCH, solo hand argument.** This extends the proposed mechanism;
it is not yet part of the submission package. No trajectory enumeration,
compiler replay, independent carrying read or priority claim accompanies it.

**Pull and discriminator.** Is autonomy essential, or is bounded periodic
forcing enough? Copying the unscaled static resource is the cheap objection.
It really fails, but dividing that resource by the forcing period repairs
the same record-charge argument. This identifies a structural role for the
external clock rather than merely fitting a different exponent rate.

Record searched: GC2256/2258/2277, this report's static restriction,
CL658/663, `record_find.py 'periodic.*gate|gate.*periodic|time.varying|wreath'`,
and the actual current kit/portal/PR index with
`non.autonomous|time.periodic|wreath|periodic.coefficient`. The hits include
inverse gate-past closing and driven-boundary statements, not a source read
establishing this bound. Current `DifferenceOrder`, `RecordCharge.Path` and
PR55's complete `RightPrefixBound` were read. PR61's new controlled example
is external forcing and remains distinct from a genuine black-edge ancestry.

The triangular invertibility framework is classical; see
[Anashin–Khrennikov–Yurova, Theorem 2](https://arxiv.org/html/1111.3093v2).
Periodic switching/skew products also predate this work:
[Anashin, Wreath Products in Stream Cipher Design](https://arxiv.org/abs/cs/0602012)
is a relevant primary lead. Its abstract was read; a full theorem comparison
is still required before novelty clearance. General triangular maps may use
all earlier bits, whereas the claim below keeps exactly two earlier inputs.

GC2279 follow-up: the relevant definition and theorem hypotheses have now
been read, with a [scoped disposition and credited static essay outline](GPT-PROOF-DELIVERY-RESUMPTION-20261030.md#gc2279-primary-source-disposition-and-static-essay-outline).
The comparison advances the source audit; it does not upgrade this sketch's
review status or establish priority.

### Scope and the failed unscaled law

Fix L=2^ell, common to all sites. Permit arbitrary L-periodic time dependence
of the four coefficients at each site:

    x_j(t+1) = x_j(t) XOR g_(j,t)(x_(j-1)(t),x_(j-2)(t)),
    g_t(b,s) = lambda(t)*b*s XOR alpha(t)*b XOR beta(t)*s XOR gamma(t).

Use zero missing inputs, or explicitly declared triangular invertible
updates on the first two coordinates. Include t mod L in the state. Let
P_j=2^E_j now denote the least period of this **augmented** prefix orbit.
Thus E_j>=ell; it is not the least period of the data bits after forgetting
the phase. The finite augmented map is a permutation: undo the phase first,
then the triangular bit map. Starting with the phase cycle, each added bit
still either keeps or doubles the prefix period.

For a hand control take L=M=2, p(t)=t mod 2, s(t)=0, b(0)=h(0)=0,
Delta b=p and Delta h=p*b. Then b=0011 repeated and h=00001111 repeated.
The s-prefix with phase has period 2, the b-prefix period 4 and the h-prefix
period 8. Thus this is an actual two-doubling instance, while order(s,2)=1.
The original unscaled reset-before claim would incorrectly demand zero.
The scaled resource below is floor(1/2)=0, as required. These eight values
are a hand calculation, not a new computation receipt.

### Block-difference identity

Suppose M=2^v with v>=ell, s has period M, b is M-antiperiodic, and h obeys
the displayed gate recurrence. Since L divides M, the coefficients at t+M
equal those at t. Exactly the static cancellation gives

    Delta^(M+1) h = alpha(t) XOR lambda(t)*s(t).

For any L-periodic coefficient c,

    Delta^L(c*f) = c*Delta^L f,

because Delta^L=S^L+I and c(t+L)=c(t). Also Delta^L alpha=0. Iterating
in blocks proves, for every positive multiple r of L,

    Delta^(M+1+r) h = lambda(t)*Delta^r s.

The assertion is only for positive multiples of L. Applying the ordinary
product rule as though lambda were constant would be wrong.

### Scaled reset and countdown

Write O(f,P)=order(f,P) and R(f,P)=floor(O(f,P)/L).

**Reset before.** Assume h is 2M-antiperiodic. If M=L, O(s,M)<=L-1 already
gives R(s,M)=0. Otherwise M>=2L. If R(s,M)>0, then O(s,M)>=L and hence
Vanish(M-L,s). The positive multiple r=M-L in the block identity gives
Vanish(2M+1-L,h), and monotonicity gives Vanish(2M,h). Antiperiodicity
instead gives Delta^(2M)h=1, a contradiction. Therefore R(s,M)=0.

**Countdown.** Put q=R(s,M). If q<=1 there is nothing to prove. Otherwise
O(s,M)>=Lq, so Vanish(M-Lq,s). Since O(s,M)<=M-1 and L divides M,
r=M-Lq is a positive multiple of L. The block identity yields
Vanish(2M+1-Lq,h), hence O(h,2M)>=Lq-1. Therefore

    R(s,M) <= R(h,2M)+1.

**Reset after.** An M-antiperiodic stream has O(h,2M)=M-1 by the unchanged
kit theorem, so R(h,2M)=M/L-1. In a double-doubling pair, apply this with
antiperiod 2M and total period 4M: the new resource plus one is 2M/L.
For pattern 01, the new resource is M/L-1, at least the old resource;
pattern 00 again has no resource obligation.

### Consequence and limits

At pair i starting at depth a, use

    nu = E_a - ell,
    e_i = E_(a+2i) - E_a,
    R_i = floor(order(x_(a+2i), 2^E_(a+2i))/L).

The preceding laws give exactly `RecordCharge.Path nu`. In particular its
reset-after field is R_(i+1)+1=2^(nu+e_(i+1)-1); the phase exponent ell has
been removed by the division by L. The unchanged accounting would therefore
give

    E_(a+2m)-E_a <= m+Q_(E_a-ell)(m) <= m+Q_0(m).

The proposed half-rate upper bound survives any fixed common dyadic clock
and arbitrary spatial mixtures of its gate schedule. L=1 recovers the
static proof; L=2 answers the initial curiosity question. No lower bound,
density equality, odd-period-clock extension, unbounded site-dependent
forcing period, or nonperiodic forcing conclusion follows here.

The next discriminator is an independent carrying read of the positive-
multiple identity and the floor inequalities, with the explicit L=M=2
counterexample to the unscaled law. A small separately frozen control could
test those exact obligations if useful; this result does not authorize an
automatic gate census or enlarge Package A before its static core is ready.

## 13. GC2281: use a phase-step difference for any fixed forcing period

**PROOF-SKETCH, solo hand argument.** The dyadic restriction on the forcing
period in section 12 can itself be removed by changing the difference
operator. This is a further separate research candidate, not an enlargement
of the static package or an independently accepted theorem.

The pull is the exact boundary exposed by the phase-2 control: the resource
should count forcing cycles rather than ordinary ticks. The cheap objection
is that composing L gates over one forcing cycle increases spatial memory,
so applying the static two-input theorem to that composite map is invalid.
The argument below keeps the original one-tick recurrence and uses two
commuting time differences instead; it makes no locality claim about that
composite map. Record/source comparison is GC2278–2279, including actual kit
DifferenceOrder/Path, PR55 and the primary skew-product construction. No new
computation or additional novelty clearance has occurred.

### Objects and the one carrying implication

Fix any integer L>=1, the same at all sites, and L-periodic gate schedules.
Include the phase t mod L in the prefix state. Standard triangular cycle
lifting gives least prefix periods P_j=L*2^K_j, with K_j nonnegative and
each increment either 0 or 1. Let

    Delta f(t)=f(t+1) XOR f(t),
    D_L f(t)=f(t+L) XOR f(t).

These operators commute. For m=2^v, D_L^m=S^(Lm)+I, irrespective of whether
L is odd or even. Let s be Lm-periodic, b be Lm-antiperiodic, and let
Delta h=g_t(b,s), where g_t has L-periodic ANF coefficients. Cancellation at
times t and t+Lm gives

    Delta(D_L^m h)=alpha(t) XOR lambda(t)*s(t).

Multiplication by an L-periodic coefficient commutes with D_L, and D_L kills
such coefficients. Therefore, for every r>=1,

    Delta(D_L^(m+r) h)=lambda(t)*D_L^r s.

If D_L^r s=0, then F=D_L^(m+r)h has Delta F=0. Thus F is constant in
ordinary time, so in particular D_L F=0. The needed implication is

    D_L^r s=0  ==>  D_L^(m+r+1) h=0       (r>=1).

This is only a forward vanishing implication; no cancellation of lambda or
inverse difference is used. It remains true when lambda changes with phase.
The final step from Delta F=0 to D_L F=0 holds for every positive L and is
what removes the previous power-of-two restriction.

### The unchanged resource argument in phase units

Define O_L(f,N) as the largest q<=N-1 such that D_L^(N-q)f=0, with value
zero if no positive q works. The cap and monotonicity of vanishing follow
exactly as for the kit's order. Vanishing here is for every original time
t, not merely one chosen phase.

If h is Lm-antiperiodic, D_L^m h is the constant one stream and
D_L^(m+1)h=0. Hence O_L(h,2m)=m-1 by the same upper/lower argument as the
kit's `order_of_antiperiod`.

For **reset-before**, suppose h is 2Lm-antiperiodic. If m=1, the old order
is zero by its cap. If m>=2 and O_L(s,m)>0, then D_L^(m-1)s=0. The carrying
implication with r=m-1 gives D_L^(2m)h=0, contradicting antiperiodicity.

For **countdown**, write q=O_L(s,m). For q<=1 the inequality is automatic.
Otherwise 2<=q<=m-1, so r=m-q>=1 and D_L^r s=0. The implication gives
D_L^(2m-(q-1))h=0, whence O_L(h,2m)>=q-1. Thus the order drops by at most
one across pattern 10. Pattern 01 has new order m-1, at least the old order;
pattern 11 has old order zero and new order 2m-1; pattern 00 needs no law.

At a pair starting at depth a, take

    nu=K_a,
    e_i=K_(a+2i)-K_a,
    R_i=O_L(x_(a+2i),2^K_(a+2i)).

All `RecordCharge.Path nu` fields follow, including the exact reset-after
value R_(i+1)+1=2^(nu+e_(i+1)-1). The proposed result is therefore

    K_(a+2m)-K_a <= m+Q_(K_a)(m) <= m+Q_0(m)

for every fixed common finite forcing period L. When L=1 this is the static
argument. When L=2^ell, D_L=Delta^L, so O_L(f,2^K) is exactly
floor(order(f,L*2^K)/L); this recovers section 12 rather than changing its
resource. The explicit phase-2 negative control still has resource zero.

### Review boundary

This supplies a written argument for arbitrary fixed finite-period forcing,
including odd L. It supplies no statement for nonperiodic forcing, an
unbounded family of site-dependent forcing periods, or a gate with more than
two earlier inputs. The clock always includes the external phase; forgetting
that phase can reduce the observed data period. No limiting density or
centre-column conclusion follows.

The sharp carrying question is the implication through the two commuting
differences, followed by the global-in-time order definition and the actual
prefix lifting. These are ready for an independent read. Local's static
implementation task is unchanged; no duplicate formalization has begun.

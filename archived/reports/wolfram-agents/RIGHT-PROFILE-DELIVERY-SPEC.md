# Right-profile parity identities: exact proposed delivery scope (GC2059)

GPT,29 October2026. Statement specification for the agreed L1082 row5: GPT prepares scope, Local formalizes,
with mutual carrying reads. No new formalization, compiler run, census, PR or posting is claimed here. The
101/mod4/cascade hand arguments already have the GC2011/GC2014 read. The generic interface below still needs
its exact assembled formal source and independent read before release.

**Record searched:** record_find.py 'universal start' (record-only), followed by freshly refreshed known_find.py
'101' 'doubl'; PROOFS/PRIOR-ART L1079; complete rule30-doubling-word sections3/5 and the committed
`doubling_after_101.py` and `universal_start.py`. Kit main remains932cf8dde039b89b1dcbe9636867bb1b2057fef0;
portal refreshed02:27:56Z. Read actual TFunctionCycles `par`, `per`, `per_eq_two_pow`, and the locations/statements
of `lift_iff`, `Phi_bit`, `Phi_cycle`; RightPeriods `S_rule`, `inp_least_period`, `no_three` are the relevant
single-seed comparisons. The search's word101 hits in constrained-boundary/shield modules have different
hypotheses/objects. This does not certify exhaustive novelty.

## Known mechanism to reuse, not resubmit

For a rightmost black cell initially at0, set D_d(t)=x_t(t-d). Then D_0=1, D_(-1)=0 and

    D_d(t+1) = D_d(t) XOR (D_(d-1)(t) OR D_(d-2)(t)).

A running XOR doubles its input period exactly when the input's weight parity is odd. That mechanism is already
recorded in section8.27 and formalized in the kit's right-period and triangular-function cycle machinery.
The seed echo is also known (`Phi_cycle`, plus lifting); single-seed period monotonicity and its111 ban are
known (`per_mono_all`, `no_three`). They are background, not separate additional headlines.

Use Q_d for the common period of the entire prefix through diagonal d (its least common multiple, equal to the
largest dyadic period), and x_d=[Q_d>Q_(d-1)]. Do not replace Q_d by the individual period of D_d: arbitrary-seed
individual-period monotonicity is not proved. Prefix-period doubling is sufficient for the arguments below.

## A precise profile-level shift law

Let q>=2 be even. Write old=d, a=D_j, b=D_(j+1), c=D_(j+2), z=D_(j+3). For the generic finite-profile interface
require, for every t>=0,

    d(t+q)=d(t),                 a(t+q)=NOT a(t),
    b(t+2q)=b(t),                c(t+2q)=NOT c(t),
    b(t+1)=b(t) XOR (a(t) OR d(t)),
    z(t+1)=z(t) XOR (c(t) OR b(t)).

Define E_q(d)=XOR of d(2s),0<=s<q/2, and eta=parity(q/2) XOR E_q(d). The target is

    z(t+4q)=z(t) XOR eta, for every t.

These hypotheses capture the101 event without postulating a forbidden period drop or specifying any initial
bits. The original doubling-letter conclusion then needs the actual right-diagonal/prefix-period bridge:
if Q_(j-1)=q and x_j x_(j+1) x_(j+2)=101, then x_(j+3)=eta. Here q is dyadic; eta=false means the prefix period
stays4q, eta=true means it doubles to8q. This is not a claim that z's own least period equals4q in the false case.

**Carrying calculation.** Pair t and t+2q in the parity of c OR b over4q. Complementing c and repeating b gives
(c OR b) XOR ((NOT c) OR b)=NOT b. There are2q pairs, so their constants cancel and the forcing parity is
XOR of b over2q. The parity of an even cyclic integral equals the XOR of its forcing at even ticks. Pair those
even ticks at q (q must be even): a complements and d repeats, giving NOT d on each of q/2 pairs. The result
is eta. Periodicity of the forcing over4q makes that total independent of the starting time t. Formalize this
last shift-invariance explicitly; a calculation only at t0 is not the full shift-law theorem.

## Mod4 identity and cascade

For q divisible by4, if d(t+1)=d(t) XOR h(t), then

    E_q(d) = XOR of [h(4s) XOR h(4s+1)], 0<=s<q/4.

Indeed d(4s) XOR d(4s+2)=h(4s) XOR h(4s+1); group the even samples in adjacent pairs. This finite identity
needs no full-period assumption on d or h, only the recurrence through the indicated interval. The actual
right-diagonal h is the OR of its two feeders.

For the10101 cascade, additionally x_(j-2) x_(j-1)=10 and q>=8. D_(j-2) complements at q/2; D_(j-3) repeats
there. Since q/2 is divisible by4, pairing the selected forcing ticks at q/2 preserves their residue class.
The constants occur q/4 times, an even number. Thus

    x_(j+3) = XOR of D_(j-3)(s) for 0<=s<q/2 with s mod4 in {0,1}.

Do not turn a few layers of this identity into an unproved all-depth residue cascade.

## Consequences with guards

- If D_(j-1) itself doubled into q, q>=4, pair its even ticks at q/2 to get E_q=q/4 mod2.
  For dyadic q>=8, eta=false. This excludes11011 when the prefix immediately before its middle101 is q>=8
  (equivalently, before the first1 of11011 it was at least4). At q4, eta=true; retain the exception.
- If d has period dividing q/2, q>=4 dyadic, E_q=0, so eta=false. Consequently1011 requires an inherited full
  q-period profile with odd even-tick parity. This is a necessary condition, not an occurrence/ancestry theorem.
- No probability, independence, asymptotic doubling density, universal plateau length or prize conclusion follows.

## Universal start: a separate exact finite obligation

For a finite nonempty seed with right edge at0, D1 and D2 alternate. No positive right diagonal is constant:
a constant would require both its nonnegative Boolean feeders to be white for ever, contradicting the black
edge by backward propagation. Before leaving prefix period2 the two feeders therefore alternate. Their OR
has odd weight over2 precisely when their phases agree. If seed bits are s_d=x0(-d), the first period>2 is at

    j=1+min{d>=2 : s_d=s_(d-1)}.

This minimum exists for finite seeds. It need not exist for a right-finite world with an infinite alternating
left tail, so an arbitrary-rightmost-cell statement needs that explicit existence hypothesis.

The accepted finite check uses exactly two equal-alternating feeder phases and seven free start bits:256 cases.
It gives individual periods D_j,...,D_(j+5)=(4,8,8,16,32,32), with the next individual period32 or64. The older
Python receipt is not a Lean certificate; a proposed core formalization must prove its generic recurrence
bridge and kernel-check all cases, preserving the two genuine feeder phases. Enumeration of all16 arbitrary
period<=2 feeder pairs is a counter-control, not a valid substitution for those hypotheses.

## Assembly order and delivery gates

After the immediate temporal-profile submission: agree one posting owner. Local can formalize generic parity
lemmas/actual right-diagonal bridge, with GPT checking the carrying source. Keep the universal-start finite
certificate separate if it needs a different evaluation budget; do not launch a new seed census. Prefer core
Lean if convenient, while retaining the actual Rule30 evolution link. A theorem only on abstract profiles
must say so in its abstract; no claim of finite-seed occurrence follows from a profile satisfying the equations.

Before compiling, freeze exact source, predicted success, retained failure conditions and stage-wide caps. Keep
proof statements, current-kit/checker outcome, notebook/resource validation and actual portal verification
separate. Main unresolved delivery work here is the assembled formal artifact; existing controlled evidence and
hand proofs do not need to be regenerated merely to make a fresh result.

## GC2177: finite cascade versus an unproved all-depth classifier — packaging disposition

The remaining label "deeper cascade" must distinguish three things. The delivered profile package
R30-20261029-7d47a9/PR51 already exports shift_law, E_mod4, eta and their actual rightDiag bridge.
The retained10101 formula is one more finite pairing of those identities, already carried GC2011/GC2014.
An all-depth residue classifier is not a proved stockpiled theorem awaiting submission. The known
resource/difference-order law along a doubling-plateau pair is background, not a proof of such a classifier.

Record searched: complete retained rule30-doubling-word section3, GC2011/GC2014 and this specification;
actual delivered Rule30RightProfiles source declarations/bodies E_mod4, xr_halves, xr_xor, xr_not,
rightDiag_shift_law; current-kit932cf8dd RightPeriods.S_rule's full-period forcing parity. The latter is
not an exact replacement for the arbitrary-profile shift law, which is already separately delivered.
No new novelty or exhaustive literature-search claim is made by this packaging disposition.

For clarity, the exact finite corollary has a short source-level derivation. Write

    F_h(v)=XOR of v(t), 0<=t<h and t mod4 in {0,1}.

Assume8 divides q, d(t+1)=d(t) XOR (u(t) OR v(t)), u(t+q/2)=NOT u(t) and
v(t+q/2)=v(t). E_mod4 gives E_q(d)=F_q(u OR v). Since q/2 is divisible by4, pairing selected
positions t and t+q/2 preserves their residue classes. Each pair contributes NOT v(t). There are
q/4 selected positions in the half interval, an EVEN number, so the constants cancel and

    E_q(d)=F_(q/2)(v), hence eta(q,d)=F_(q/2)(v).

Putting d=D_(j-1), u=D_(j-2), v=D_(j-3) gives precisely the existing10101 cascade, with actual
prefix-letter/antiperiod hypotheses retained. The selected mask, half-period and parity guard matter;
q>=8 alone would not justify this calculation for arbitrary nondyadic q. It asserts neither occurrence
of10101 nor scalar individual-period monotonicity. No simulation or new proof mechanism is involved.

**Disposition:** keep this finite corollary in the record and existing package's explanatory material;
no additional standalone submission merely to restate the one extra pairing. It is not claimed as an
exact named theorem already exported. Reopen adding a named formal convenience lemma if a subsequent
proof needs that interface or a maintainer requests it. Keep the all-depth classifier OPEN with its
actual requirement: a recursively specified mask, scale/divisibility guards and root-compatible
ancestry must be proved, not inferred from the first two layers or finite frequencies. The observed
110 overlap obstruction in section3 remains outside this finite corollary.


## GC2197: a binomial mask for every finite alternating run

**Status: PROOF-SKETCH, new explicit conditional consequence awaiting Local's carrying read.**
**Current review, GC2198/L1197: PROVED hand/two-party; the original sketch label is dated history.** This uses the
known difference-order/countdown mechanism, not a new resource or density theorem. No computation, formalization,
posting owner or novelty clearance. GC2196 announced a25-minute hand budget; the result changes the representation
rather than starting another census. L1195's exact countdown is the key available ingredient.

### Statement with actual prefix ancestry

Let D_d(t) be the right diagonals of any start with rightmost black cell at0. Write Q_d for the least common
period of the complete prefix through d, and x_d=1 iff Q_d=2Q_(d-1). These periods are dyadic; using prefix
periods avoids an arbitrary-seed individual-period monotonicity assumption. Take a>=2 and m>=1 and suppose

    x_a x_(a+1) ... x_(a+2m) = (10)^m 1.

Set M=Q_(a-1), f=D_(a-1), and P_f(X)=sum_(0<=t<M) f(t) X^t over F2. Let mu be its multiplicity at X=1.
Then

    m <= mu <= M-2,
    x_(a+2m+1)=1 iff mu=m,
    x_(a+2m+1) = XOR_(0<=t<M) [binomial(t+m,m) is odd] f(t).

Equivalently the selected times are exactly those with bitwise(t AND m)=0. This is an exact finite profile
formula, conditional on the preceding alternating doubling word. It says neither that such words occur at
arbitrary lengths nor how frequently they occur. Initial source a=1 is excluded: D_0 is constant black,
and the ordinary nonconstant countdown need not apply there.

### Proof: the known countdown supplies the missing guard

The edge has D_0=1 and D_(-1)=0, so D_1 and D_2 alternate. Any later constant diagonal would force both
feeders identically white; induction contradicts the already nonconstant positive feeder. Thus f is nonzero
and nonconstant. Periodic lower forcing makes its integral repeat after twice that period, starting at time0;
induction also justifies the dyadic prefix periods used above.
For a nonzero stream of dyadic period H, let d be its least vanishing difference index. The known polynomial/
difference dictionary is mu_H=H-d; nonconstancy gives d>=2 and mu_H<=H-2.

The exact countdown needs only that H is a period bound, not that it is the least individual period. Indeed,
if s has period H, b is antiperiodic at H, Delta h=b OR s, and h has period2H, the existing identities give
Delta^(H+1)h=NOT s. The last nonzero and first zero differences of nonconstant s give d(h)=H+1+d(s), hence

    mu_(2H)(h)=mu_H(s)-1.

This explicitly checks the extension from least periods to prefix period bounds; no monotonicity shortcut.
A prefix doubling makes its newly added diagonal antiperiodic at the old prefix period: the forcing repeats
there and its full-cycle XOR is independent of the starting tick. A plateau makes that diagonal periodic at
the unchanged prefix period. Therefore every10 in the assumed word supplies the above countdown hypotheses.
After k such pairs, the source D_(a+2k-1) has prefix period H_k=2^k M and resource mu-k. Nonnegativity
at k=m gives mu>=m, and the initial nonconstant bound gives m<=M-2.

For the final1, let s=D_(a+2m-1), b=D_(a+2m) and h=D_(a+2m+1), H=2^m M. The new b complements at H.
The XOR of b OR s over2H ticks pairs to XOR_(t<H) NOT s(t). Since H is even, this is XOR_(t<H)s(t).
That forcing parity is precisely the next prefix-doubling flag. It is1 iff P_s(1)=1, equivalently iff its
resource is0. Thus the flag is1 iff mu-m=0, proving the middle assertion.

Now compute the coefficient of Y^m in the finite polynomial

    (1+Y)^m P_f(1+Y).

Expanding the summands shows that this coefficient is the displayed binomial-weighted XOR. Since mu>=m,
P_f(1+Y)=Y^mu G(Y), G(0)=1, the coefficient is1 exactly when mu=m. If mu>m it is0. This proves the mask
formula. The antecedent supplies the lower-coefficient cancellations; omitting mu>=m would make the last
inference false. This proof is shorter than rebuilding a separate repeated-summation argument at every depth.

The binary support is the classical Lucas rule, not a new combinatorial theorem. Over F2,
(1+Y)^n is the product of(1+Y^(2^b)) over the1-bits of n, so its degree-k coefficient is1 iff k is a bit
submask of n. For n=t+m and k=m, no common1-bit of t,m means addition has no carry and m is a submask.
Conversely, at the lowest common1-bit no carry can arrive from below, and the corresponding bit of t+m is0;
thus m is not a submask. This proves the equivalent bitwise selector directly.

### Hand controls and a failed boundary shortcut

The masks, written from t0 over their shortest dyadic period, are:

| Number m of10 pairs | Selected positions modulo that period | Binary mask |
|---|---|---|
|1|0 mod2|10|
|2|0,1 mod4|1100|
|3|0 mod4|1000|
|4|0,1,2,3 mod8|11110000|
|5|0,2 mod8|10100000|
|6|0,1 mod8|11000000|
|7|0 mod8|10000000|

m1 recovers the even-tick101 formula: mu>=1 and mu<=M-2 force dyadic M>=4, so its old constant parity(M/2)
is0. m2 recovers the carried10101 mask on residues0,1 mod4 with initial M>=4 (the final101 base is2M>=8).
At m3 a4-tick base would make mask1000 have odd total. Silently cancelling its constant would be wrong;
but an actual nonconstant starting profile has mu<=2 there and cannot supply three10 pairs at all.
The countdown eliminates that boundary rather than pretending its parity is even.

Two temporal polynomial controls test the coefficient interpretation by hand at M8. P_f=(1+X)^3 has mu3:
the m1/m2 masks give0 and m3 gives1. P_f=(1+X)^4 has mu4 and the m3 mask gives0. They are coefficient
controls, not claimed actual-root profiles. Removing the mu>=m guard fails already for P_f=1,m1: the mask
returns1 although mu=0. No numerical scan was run.

The masks do not shrink monotonically: going from m3 to m4 changes1000 into11110000. What increases is the
coefficient order being tested, not the sparsity of selected times. A run supplies m vanishing low coefficients;
its next decision tests the next one. These are exact joint relationships among changing cells. They do not
justify assigning probability2^(-m) to the actual seed, whose temporal profile is not a uniformly sampled word.

### Scope, prior art and the unresolved parent question

Record searched: GC2196's two record/actual-kit/portal/PR queries, with current complete16:54:35Z refresh:
kit932cf8dde039b89b1dcbe9636867bb1b2057fef0,21openPRs. Only the already-reviewed public horizon proof/entry
dc3d17 became newly indexed; no changed external carrying source. Known RightProfiles.shift_law/E_mod4,
DifferenceOrder.dif_shift_sum/difs_past/order_countdown, GC2008's Newton argument and L1195's exact countdown
are the actual mechanism. PR23 DyadicSources.choose_odd_submask and its classical Lucas source concern the
same binary support rule in a different spatial-source expansion, not this prefix-doubling antecedent.
Primary Rowland and the previously read source comparisons remain credited; negative searches do not clear
novelty. This is an explicit application of known machinery, not another submission assembled from it.

The remaining all-word/overlap classifier, physical occurrence restrictions and DQ024 lower-density bound
stay OPEN. In particular this does not control00 transitions, reopen the parked ancestor ladder, or show that
an indefinitely alternating pattern describes the single seed. Local's separate GC2154–2158 reads continue.
The carrying questions are the prefix-period countdown scope and the conversion to the binomial coefficient;
no run is requested.

Search/index receipts retained at cited/gc2197-alternating-mask/review-manifest.json,
SHA25628641deecb68776c463581a9cb5df1e319cdbcbf09793c2f091f05efda185baa. The newly indexed horizon source is
exact791e45ed1aef3955035989f1443f43a3427ea82b0cb01a8ad088bc221ec57110, matching the already-reviewed release;
no compiler/checker/notebook rerun. This is a source identity check, not a new verification claim.


## GC2198: the110 overlap law needs its small-period constant

**GC2197 review update:** complete L1197/5d202c42 and the carrying source read. Both the countdown at prefix
period bounds and the binomial-coefficient conversion carry independently; the conditional arbitrary-m mask
is now **PROVED (hand, two-party)**. Local also checked all seven masks and the hand guard controls. Its
right-edge base facts are explicitly the known kit recurrence/boundary. No occurrence/frequency/00 conclusion.

**Current review, GC2200/L1199:** the corrected110 law and the actualq2 counterexample are now PROVED
hand/two-party. The original sketch label below is historical; the unguarded shorthand remains REFUTED.

**New hand question:** does the old110 overlap shorthand retain the smallest allowed base? Its unguarded
version is **REFUTED at q2 by the actual single seed**, below. The corrected all-even-q formula is a
**PROOF-SKETCH awaiting Local's carrying read**. This is a correction to the research note, not a new
submitted theorem or a contradiction of the delivered101 law.

Let q>=2 be even, and let a,b,c,z be Boolean time profiles satisfying

    a(t+q)=NOT a(t),       b(t+2q)=NOT b(t),       c(t+4q)=c(t),
    Delta c(t)=a(t) OR b(t),       Delta z(t)=b(t) OR c(t).

Write Pi_L(f)=XOR_(0<=t<L) f(t), and product bc for pointwise AND. Then the corrected shift claim is

    z(t+4q)=z(t) XOR kappa, all t>=0,
    kappa=parity(q/2) XOR Pi_(4q)(bc).

For a genuine prefix110 based at q, kappa is its next doubling flag. In the dyadic case the old
product-only shorthand is therefore valid for q>=4. At q2 the missing constant is1.

**Carrying calculation.** Complementarity gives b period4q and Pi_(4q)(b)=0. For any even L and L-periodic
c, pairing adjacent values gives Pi_L(c)=XOR_(even t<L) Delta c(t). At L=4q, pair those even ticks at2q:
a repeats there and b complements, so each pair of a OR b contributes NOT a. There are q such pairs,
and q is even. Pair the remaining even a samples at q, where a complements; there are q/2 pairs. Hence

    Pi_(4q)(c)=parity(q/2).

Pointwise b OR c=b XOR c XOR bc, so its full-period parity is exactly kappa. Its forcing is4q-periodic,
making the full-cycle parity independent of the starting tick and giving the stated all-time shift law.
This uses actual joint product parity; we have not proved that no alternative statistic of older profiles
could encode it. The older finite failure to find three marginal residue parities stays a finite NOT FOUND.

### Hand counterexample at the single seed's first110

Time0 first, one8-tick cycle; all start bits at positive depth are0:

| Profile | Word at t0..7 | Least period | Black count |
|---|---|---|---|
|D1=D2|01010101|2|4|
|a=D3|00110011|4|4|
|b=D4|00101101|8|4|
|c=D5|00010101|8|3|
|b AND c|00000101|divides8|2|
|b OR c|00111101|divides8|5|

The cycles are obtained by hand from Delta D_d=D_(d-1) OR D_(d-2), D0=1, D(-1)=0. Their successive forcings
are01010101 for D3,01110111 for D4, and00111111 for D5, with the correct return at8. D3 complements at2,
D4 at4, and D5 is8-periodic but not4-periodic. Thus x3 x4 x5=110 at baseq2. The final forcing has odd weight5,
so D6 complements at8 and x6=1. Product-only parity is0 and predicts the wrong flag; the corrected constant
restores1. No numerical scan, certificate or fresh dynamics run was used; these are eight explicit hand updates.
This is consistent with the already-delivered universal start, not new universal-start evidence.

Record searched:110 with overlap/product-parity, then110 with q/2 or q>=4 variants. Actual cached kit932cf8dd,
portal16:54:35Z and21PR sources searched: prior101 constants/guarded11011 statements are different antecedents.
The actual old report's section3 next-case paragraph has no q>=4 guard. The corrected claim is a direct
application of its known forcing/integral parity identities, with no novelty or standalone packaging claim.
It supplies a boundary repair, not a closed all-word/overlap classifier, a density theorem or an excuse for
another search census.

Search receipts: cited/gc2198-overlap-guard/review-manifest.json, SHA2568a33ca28052e876b474ea622e8a69ff0eb9788652a5a62177b86092db31383bf.


## GC2200: the110 joint statistic is ordered history, insensitive to two recent start bits

**Status: PROOF-SKETCH awaiting Local's carrying read.** This is the hand target published in GC2199, using
GC2198/L1199's corrected shift law. No computation, new autonomous state model, formalization or submission.
The point is to identify what the overlap reads, rather than replace a missing correlation by a coin.

Use the same generic110 hypotheses: even q>=2, P=4q, a antiq, b anti2q, c periodP, Delta c=a OR b,
and Delta z=b OR c. Put epsilon=parity(q/2), B(t)=XOR_(0<=u<t)b(u), and

    O(a,b)=XOR_(0<=t<P) a(t) AND NOT b(t) AND B(t).

Then the full-cycle shift bit is

    kappa=epsilon XOR O(a,b).

Thus a given full period can be read with two parity accumulators: the parity p of b already seen,
and a result r. Start both at0; at tick t toggle r by a(t) AND NOT b(t) AND p, then toggle p by b(t).
The result is epsilon XOR r at the known cycle endpoint. This reads PROVIDED temporal profiles over4q
positions; the input, period endpoint and its potentially growing length are not supplied by those two bits.
No closed spatial-depth generator or bounded-cost prediction follows.

### Eliminating c by an ordered-pair calculation

Unroll its exact recurrence over the fixed time0 cut:

    c(t)=c(0) XOR XOR_(u<t) b(u) XOR XOR_(u<t) a(u) AND NOT b(u).

Multiply by b(t) and sum over P. Since b is anti2q it has exactly2q black cells and Pi_P(b)=0. The initial
c(0) term vanishes. The self-pair term is choose(2q,2) modulo2, which equals q(2q-1)mod2=0 because q is even.
The remaining term is

    Pi_P(bc)=XOR_(u<t<P) a(u) AND NOT b(u) AND b(t).

Reversing the finite summation order replaces the last factor by the parity of b AFTER u. Total b parity
is0, so this is B(u) XOR b(u). The b(u) part vanishes against NOT b(u). This gives Pi_P(bc)=O(a,b), and
the carried corrected110 law gives kappa. The ordering, not only separate colour totals, occurs explicitly.
We have not proved that every conceivable older-profile statistic is insufficient.

### The b-start phase also cancels

Complement b to b'=NOT b and let c' be ANY integral of a OR b'. Then e=c XOR c' satisfies

    Delta e=NOT a.

Since a is antiq, NOTa has q black cells over2q. q is even, so e has period2q, regardless its initial value.
Consequently c'=c XOR e is P-periodic, so the corrected110 law applies to both pairs. Over P,

    Pi_P(c'b') XOR Pi_P(cb) = Pi_P(c) XOR Pi_P(e) XOR Pi_P(eb).

The three terms are epsilon,0,epsilon respectively. The first is GC2198/L1199. The second vanishes because
e repeats twice. For the third, pair b at2q while e repeats, giving Pi_(2q)(e). Its even-tick integral
identity gives XOR_(even t<2q) NOTa(t); q constants cancel and pairing a atq leaves q/2 ones. Thus the two
epsilon terms cancel and the overlap, and hence kappa, is unchanged.

Separately, complementing c alone changes Pi_P(cb) by Pi_P(b)=0. This is the already-known general
one-diagonal-delayed seed-bit identity in this particular regime (GC2014/L1070), not another novelty claim.
The b-complement calculation is the additional conditional step. In particular the q2 constant cannot be
silently discarded in its proof: Pi_P(c) and Pi_(2q)(e) are BOTH1 there, and they cancel.

### Actual seed interpretation and the precise remaining input

In a genuine prefix110, a=D_j, b=D_(j+1), c=D_(j+2), d=D_(j-1), and Delta b=a OR d. Flipping the seed bit
at depth j+1 complements all of b, changes c by the integral above, and leaves a,d unchanged. Its anti2q
period remains. The new c is still P-periodic, so the prefix110 history is preserved, and its next flag
is unchanged. Flipping the bit at depth j+2 only complements c and is also irrelevant to that next flag.
Any combination of those two flips has the same conclusion; all other seed bits may be held fixed.
This concerns the next growth flag conditional on110, not every later flag or a still older seed bit.

An explicit way to remove both recent start bits is to define

    b0(t)=XOR_(u<t) [a(u) OR d(u)],    with b0(0)=0.

Actual b differs from b0 only by a constant. Thus kappa=epsilon XOR O(a,b0): the two older full profiles
a,d suffice. Producing b0 from a,d requires its additional integral accumulator. The older profiles retain
their whole temporal information; this is not a claim that a few marginal parities of d or its feeder close
the dynamics. The earlier finite NOT FOUND statement about such residue parities remains finite evidence.

### Hand8-tick finite-seed control

For q2, keep a=D3=00110011. The original single seed and the finite seed obtained by also making cell -4
black have respectively b=D4 and c=D5 as follows, time0 first:

| Choice | b | c | b AND c | Overlap weight | b OR c weight |
|---|---|---|---|---|---|
|Single seed|00101101|00010101|00000101|2|5|
|Flip depth4 only|11010010|01010001|01010000|2|5|

The second c has forcing11110011 and returns to0 at8. Its difference from the first c is e=01000100,
which has period4 and Delta e=11001100=NOTa. Both histories are110 and both next flags are1. In the original
ordered reader, a AND NOTb occurs at ticks3,6; B is1 at both, so O=0. In the flipped reader those ticks are
2,7; the respective b-prefix parities are0,0, again O=0. The fixed epsilon1 gives kappa1 in each case.
These are hand recurrence checks on eight specified bits, not a new machine test or a universality inference
from the control. No claim is made that changing the physical seed has no other effect on its evolution.

Record searched:110/seed-bit/phase with ordering/prefix-parity/complement/two-bits, and110 with
complement/invariant/initial/seed. Actual kit932cf8dd, portal16:54:35Z and21PR sources searched. The known
GC2014 delayed-bit identity and universal-start finite certificate are controls; no exact general b-phase
claim has been identified from their actual statements. This is not novelty clearance. Elementary unrolling,
finite pair counting and the carried shift law are the mechanism; no external density theorem is imported.
The current target is complete as a sketch. Local's carrying questions are the ordered-pair reduction,
the e-period/epsilon cancellation, and the seed/prefix interpretation. No extra run or packaging requested.

Search receipts: cited/gc2200-inherited-overlap/review-manifest.json, SHA25648c5ab98ae7e311ca3f517529b465d26f72160e700dee2a4764f14f0cf77d835.


## GC2201: a preceding doubling forces a power-of-two closing length

**GC2200 review update:** complete L1201/1041afde and its carrying source read. The ordered-pair reduction,
b-phase cancellation and actual seed interpretation now carry independently: **PROVED (hand, two-party)**,
with provided-profile/cycle-endpoint, next-flag-only and no-older-bit/later-flag qualifications intact.

**New short hand consequence, PROOF-SKETCH awaiting Local.** CL643 asks whether some masked parities are
forced on actual histories. A preceding doubling provides exactly such an additional hypothesis. Keep the
prefix periods Q and flags x from GC2197. Let s>=1,m>=1 and suppose the word starting at x_s is

    1 (10)^m 1.

Set q0=Q_(s-1), so Q_s=2q0. Then

    m <= q0-1,
    x_(s+2m+2)=1 iff m=q0-1.

In particular, the complete word

    1 (10)^m 11

can occur only if m+1=q0 is a power of two. Thus1101011, the m2 case, is forbidden in every genuine
prefix-doubling word of a row with a rightmost black cell. It is a statement about growth flags indexed
by diagonal depth, not the same binary word occurring as physical colours in time or space.

**Proof and indexing.** Since x_s=1, f=D_s complements at q0. The known order_of_antiperiod lemma gives
its multiplicity over M=2q0 as mu=q0-1. Apply the already-carried GC2197 with a=s+1>=2. Its assumed
(10)^m1 is exactly the remainder of the displayed prefix, and its next flag is x_(s+2m+2). It gives
m<=mu and nextflag1 iff mu=m, proving both assertions. Finally q0 is dyadic. No individual-period
monotonicity for arbitrary seeds, new valuation theorem or infinite occurrence claim enters the proof.

**Controls and scope.**
- For m1 this recovers the known11011 rule: closure requires q0=2, while q0>=4 forces the final0.
  The actual single seed's flags x3..x7=11011 supply the existing boundary control q0=2. The old101
  base in that case is M=2q0, not q0; these period conventions must not be interchanged.
- For m2 closure would require q0=3, impossible. For m3 it would require q0=4, but we have NOT proved
  that this permitted arithmetic value yields an actual occurrence. The criterion is necessary;
  its iff concerns the next flag GIVEN the preceding1(10)^m1 at that scale.
- m0 is outside this corollary; the known111 ban and its initial edge case remain separately proved.
- The initial profile is positive-depth D_s, so the constant D0 exception of the countdown is avoided.
- The symbolic words(10)^infinity and(0001)^infinity contain no11 and avoid the whole family, yet
  have densities1/2 and1/4. They are symbolic controls, not actual-root orbits. Thus this family alone
  does not fix the density, let alone resolve the00 balance or the half-limit conjecture.

This is an explicit forbidden-word consequence of the known antiperiod resource and the carried conditional
mask, not a new mechanism or a novelty-cleared submission. It answers CL643's hand direction with the
EXTRA preceding1 made visible. A statement about every unqualified(10)^m1 cannot silently assume this
antiperiodic source. No new fair-transition model, census, compiler or posting owner is proposed.

Record searched:1101011/Mersenne/alternating with gap/doubling/power-of-two; literal1101011/Mersenne in the
record and actual kit932cf8dd/portal16:54:35Z/21PR sources. G268's0001101011 ban was read: it is a temporal
colour profile of a forward normalized G orbit, a different object. Known no_11011, no_three and universal
start are credited, not repackaged. Direct current-source search found no named no_1101011 export; neither
that nor the primary search's unrelated PRNG hits clears novelty. No external theorem is imported beyond
the actual kit antiperiod order and already-carried mask. Local's carrying question is the source-period/
index conversion and the global growth-word consequence, not a new numerical test.

### CL642 Case A/B carrying read, with explicit period conventions

Complete CL642/CL643, GC2164 and L1200 read. CL643 accepts the asymptotic scope correction; L1200 correctly
keeps GC2156/2157/2158 pending. No Cloud work is assigned. The following is a hand read of the three
parity rules, not a replay of Cloud's C outputs, pooled numbers or enforcement receipts.

For the SINGLE SEED use least periods p_j, d_j their exponent increments, P=p_(j-1), and omega_j the
weight parity over p_j. The known per_mono_all/unit-increment theorem and S_rule supply the framework.
If d_(j-1)=1, the older period is exactly P/2 and pairing OR at P/2 gives parity(P/2) XOR omega_(j-2).
For P>=4 this is omega_(j-2), Case A. If d_(j-1)=0, both least periods equal P and expanding OR gives
omega_(j-1) XOR omega_(j-2) XOR Pi_P(product), Case B. For a nondoubling output at even period P,
its weight parity equals the even-tick forcing XOR by adjacent pairing. A newly doubled output has
half its own period black, hence even weight once that period is at least4. These are **KNOWN,
reproved here and now hand/two-party with CL642 in precisely this single-seed scope**.

One written guard needs clarification: the quarter-period P/4 is even only for P>=8. The smaller initial
case for no_three is handled separately by D1,D2 alternating; the kit's actual no_three proof retains
its positive-depth/nonconstant guard. Do not replace that guard by the sentence “P/4 is even” at P4.
For arbitrary-seed PREFIX periods the safe counterparts use Pi_P and Pi_(P/2) explicitly; omega over
an individual least period may differ because a prefix cycle repeats that profile. The pooled block
exponents in CL642 part2 therefore do not automatically inherit the original omega notation.
The withdrawn limit/sharpness conclusions remain withdrawn; no new distribution or runtime verdict follows.

## GC2205: exceptional ruler closures have a deterministic sparse count

**Carrying read completed.** CL645's composition was read at its actual carrying step. With b=s+1,
its M=Q_b=4q0 and M/4-1=q0-1; its source D_(b-1)=D_s is exactly GC2201's antiperiodic source.
For m>=1 the statements coincide, with prefix periods and positive-depth guard retained. The forced
closing-length law is now **PROVED (hand, two independent derivations; Cloud CL645 read by GPT)**.
This accepts the precise composition, not Cloud's finite pooled counts, Markov assumptions, or
claim that the question has been completely reduced to two fair coins. No new Cloud work requested.

**New count, PROOF-SKETCH awaiting independent review.** Write Q_j=2^E_j, x_j=E_j-E_(j-1), E_0=0.
A completed exceptional block is an occurrence1(10)^m11, starting at s>=1, m>=1. Put

    e=E_(s-1), q=2^e=m+1, u=s+2m+1.

The closing11 starts at u. There are no other11 starts strictly between s and u. There are exactly
m+1=q ones from x_s through x_(u-1), hence

    E_(u-1)=e+2^e.

List all completed exceptional blocks in increasing start order (s_i,u_i,e_i,m_i). Two cannot have
the same start: the earlier closing11 would break the longer required alternation. The next start
cannot be strictly inside(s_i,u_i), since it would need another11 there. Thus s_(i+1)>=u_i, INCLUDING
the possible shared closing/starting11. Monotonicity of prefix exponents gives

    e_(i+1) >= e_i + 2^e_i.

The proof does not assume independence, typicality, a finite seed, or unbounded exponents; it uses
actual prefix flags and the carried closing-length law. Since m_i>=1, e_i>=1. Define a_1=1 and

    a_(r+1)=a_r+2^a_r:       1,3,11,2059,... .

If C(N) blocks are completed within x_1..x_N then a_(C(N))<=E_N<=N, whenever C(N)>0. In particular,
2^e>=e for e>=1 gives a_r>=2^(r-1), so

    C(N) <= 1+floor(log2 N),       C(N)/N -> 0.

The a_r bound is much stronger than the displayed logarithmic simplification. The quantity being
counted is a specific completed block, not every11, every zero, or every nondoubling pair. Blocks
may share their boundary11; the proof explicitly charges only the bits before that shared start.
A long block cut off at N contributes nothing yet. There is no assertion that every allowed
length occurs or that the lower tower bounds are attained by a Rule30 root.

**What this changes.** Cloud explicitly neglected the ruler exception in its heuristic. The count
above supplies a deterministic reason that its *event frequency* vanishes. It does not couple the
actual word to a word with those events removed, bound the later influence of an event, establish
fairness of either unresolved transition, or prove density2/5. A sparse event can change the later
regime for a long time. The residual00 mechanism remains a separate open task.

**Known mechanism, no priority claim.** Current kit932cf8dd Rule30RecordCharge.threshold,
record_potential, record_time_lower_bound and threshold_tower_step already give tower-sized costs
for excess-exponent records, and Rule30RightPeriods.per_upper_half is already proved. Our a_r
counts particular unaligned word closures; it is not the kit's threshold sequence1,3,19,2^21+19,... .
This is a word-level explanation of the same reset/countdown mechanism, not a newly proved half-rate
bound or a novelty-cleared package. GC2203's record/current-kit/portal/PR search and Rowland2006
primary background apply; no new external arithmetic theorem is imported.

**GC2204 actual outcome: COMPUTED/PASS**, once at fixed depth24/65536ticks. The exact prefix returns,
first-return and column-halving periods agree, and substring and consecutive11 readers both find
exactly the universal-start block(s,u,e,m)=(3,6,1,1). Prefix flags are101101101000001100000001.
This checks indexing and includes the actual small boundary; it does not validate the infinite
counting argument or meaningfully exercise a second exceptional closure. No wider run is requested.
Intel:0.23seconds wall,0.22childCPU,15458304bytes maxRSS by time; launch headroom5806MiB, existing
swap225.25MiB. Child finished before a supervisor sample, so sampledRSS/swap-growth maxima are
unavailable rather than measured zero. ExitCOMPLETED/0, no job remains. Source/freezeae1f39a4 and
immutable receipt cited/gc2204-ruler-control/manifest.json SHA256
8fb100ba539bcd1e6411a636e16c652a3e17d2646ad85b598b8c2bb845ed9a75.

**Next step:** inspect the new a4691a backward-operator source at its actual definitions and heads,
then return to a concrete00 question only if it retains information beyond the parked generic
parity/ancestor proposals. Do not rerun this small control or reinterpret it as density evidence.

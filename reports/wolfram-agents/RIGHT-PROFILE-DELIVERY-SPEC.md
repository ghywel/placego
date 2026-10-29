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

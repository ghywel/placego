# Multiple-driver response and complete-parent calibration

*The waiting room (not yet verified). Derived from [PROOFS.md](../PROOFS.md), entry "GPT G281 — Multiple-driver
response and complete-parent calibration (GPT, 2026-10-10; waiting room, GC897)"; rebuild with `python3
proofs/build.py`. Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** in the waiting room: stated with a proof, not yet checked by a second reader.

## In plain words

Several changed driver bits produce XORs of final-driver reset intervals, so their effects can cancel.

**What it says.** The exact difference equation is a linear reset equation forced by delta times the complement of the original child. For fixed nonzero drivers and uniformly all parent words, response rank is the number of changed ticks, collision probability is2^-k, and expected response weight is half the union of intervals. A q4 example reduces two lengths totaling five to one changed bit. Second reading pending.

**Why it matters.** Response lengths are not additive charges. Excluding the two terminal parents changes the collision rate, and neither averaging measure represents a rooted history without a new premise. No return-growth bound is supplied.


**W281 continuation (GC899).** At fixed parent x, child z is compatible iff z*(1+x+S z)=0. Its nonzero-driver fibre has2^weight(z)-indicator[x=Delta z] members: driver bits on child-black sites are free. Direct q4 controls and constant-child/terminal/q1 guards agree. Primitive alternating fibres are realized across distinct rooted prefixes, with2^(q/2)-2^(q/4) drivers for dyadic q>=4. Cross-driver collisions do not violate pair-map injectivity and give no within-history frequency or growth law. Second reading pending.


**W281 second-reading receipt (2026-10-10 00:16 BST).** Local L511 atb9f47663 independently checks GC897's forcing law, Green intervals, rank/collision/union mean, cancellation and measure guard, and GC899's fibre formula, endpoints and primitive rooted-prefix count. PASS by hand with scope retained: no rooted frequency or return bound. Formal promotion remains separate.


**W281 continuation (GC901).** Alternating child under parent1 is followed by complemented doubled driver bits, recovering primitive q, possibly with weight2. The prefix examples are zero-started fixed-q excursions; ancestry from the smaller-period physical root is not asserted. No full-state coalescence, recurrence frequency or stage-growth bound follows. Second reading pending.


**GC901 second-reading receipt (2026-10-10 00:26 BST).** Local L512 at77967ffa verifies the reset/copy formula, primitive-period transfer, q4/q8 sparse controls and full-alternating terminal guard by hand. PASS with zero-started-root scope and no physical ancestry, rooted frequency or return bound. This continuation is reviewed; formal promotion remains separate.


**W281 scope correction (GC903).** The q4 zero-starts0/1110 and0/1011 are on the same28-step B cycle; a seven-step-to-rotation certificate proves nonabsorption. GC899's rooted-prefix wording means arbitrary zero-started excursions only: these controls are NOT in the physical(0,1) root tree. Fibre/period-recovery formulas and their reviews remain valid; no larger-q ancestry conclusion. Second reading pending.


**W281 continuation (GC904).** Antiperiodic driver and nonzero half-periodic parent force primitive dyadic child. At a genuine doubling prefix0,c,1,e,f, f is primitive and G201 implies q/4<=weight(f)<=q/2. Parent0 and q2 guards retained. One-profile corollary only, no cumulative charge or stage bound; second reading pending.

## The formal statement and proof

#### GC897 — Multiple driver changes combine by XOR; full-parent collision law (2026-10-10 00:01 BST)

**Registered actual-recurrence hand continuation; second reading pending.** Record searched: (perturb/difference) + (driver/reset) ->87 hits in21 files. GC896 and G4's averaging-scope warning read. Predict modified-driver reset intervals superpose by XOR, not by adding their lengths. Independent q4 two-removal control, unexpected terminal-parent conditioning and zero-driver guard. No trajectory, random draw, census or rooted distribution claim. The Boolean/reset mechanism is credited; this is its finite-row response/calibration, not a growth invariant.

**Exact response.** For fixed parent x and nonzero drivers y,y', let z,z' be their unique cyclic children. Work over F2, put delta=y+y' and d=z+z'. Expanding OR gives

S d=(1+y')*d+delta*(1+z).

The scalar products are pointwise. The linear operator L_(y')(v)=S v+(1+y')*v is invertible: a homogeneous solution resets to zero after any black tick of y' and remains zero everywhere by cyclic propagation. Therefore

d=L_(y')^(-1)(delta*(1+z)).

For each changed tick j, let I_j be the cyclic interval from j+1 through the first black tick of y' strictly after j, inclusive. Its length is1..q, allowing a full turn when j is the only black tick of y'. Direct propagation gives L_(y')(1_(I_j))=e_j. Hence

d = XOR_(j:delta(j)=1) [(1+z(j))*1_(I_j)].

All intervals use the FINAL driver y', not independently toggled intermediate drivers. Supports may overlap and cancel. Both drivers must be nonzero; no common black tick between them is required for this multiple-change identity. It recovers GC896 when there is just one toggle and a common remaining reset.

**Exact complete-parent average, not a rooted law.** Fix distinct nonzero y,y', with k=weight(delta)>=1, and choose x uniformly from all2^q parent words. The map z->x=y+L_y(z) is affine bijective by reset, so z is uniform on all words. The forcing delta*(1+z) is uniform on the k-dimensional coordinate subspace supported at changed positions. Invertibility of L_(y') makes d uniform on the k-dimensional span of the interval vectors. Consequently

P(z'=z)=2^(-k),   E weight(d)=|union_(delta(j)=1) I_j|/2.

Each coordinate in that union is a nonzero linear functional of the k fair forcing bits, so is1 half the time; outside the union it is always0. The mean is half the union size, not half the sum of lengths. This is exact finite averaging over all parents; it does not assume Rule30 spatial trajectories select those parents uniformly.

**Independent literal cancellation control.** At q4 use x=1111,y=1110,y'=1000. Their children z=1000 and z'=1010 satisfy all four equations directly, giving d=0010. Changed ticks1 and2 have final-driver intervals I_1={2,3,0}, I_2={3,0}. Both forcing bits1+z(j) equal1. Their indicators1011 and1001 XOR to0010: the sum of lengths is5 but the response weight is1. Over the complete parent domain the four equally likely response words are0000,1011,1001,0010. Their mean weight is3/2, half the three-position union, rather than5/2; the collision probability is1/4. This four-word algebraic control is not a random experiment or a trajectory enumeration.

**Unexpected live-domain conditioning guard.** Complete-parent averaging includes x=y (original child0) and x=y' (new child0). Neither can be a collision when y!=y': a common zero child would force both parents to equal their drivers. Removing these two distinct terminal parents leaves the same2^(q-k) collision parents among2^q-2 choices, so the simultaneous-nonterminal collision rate is

2^(q-k)/(2^q-2),

not2^(-k). In the q4 control it is4/14=2/7, not1/4. This does not compute a conditional mean weight or justify any rooted sampling law. If either driver is zero, L may be singular and child uniqueness fails; the formulas require the stated nonzero-driver hypotheses.

**Disposition.** Actual response intervals can cancel heavily, and full-parent probabilities are structural calibration rather than evidence of randomness or lower growth. This prevents using independent one-bit response lengths as additive charges. A Q7 argument needs retained backgrounds/occurrences or a cancellation-resistant quantity along the actual rooted history. No sensitivity census or new averaging-based growth shortcut is proposed. Next requested review or a rooted coupling obstruction; scratch deferred and room closed.


**GC897 duplicate audit (2026-10-10 00:03 BST).** W281 hard checks pass; nearest W280/G201 were read in full in the preceding blocks, and G185 read in full here. W280 supplies the credited single-toggle mechanism; G201 supplies a different sibling-support relation/failure; G185 warns against transferring ambient behaviour to growth. This continuation keeps final-driver Green intervals, XOR cancellation and the explicit complete-parent measure. No promotion or rooted law.


#### GC899 — Exact fixed-parent same-child driver fibres (2026-10-10 00:10 BST; W281 continuation)

**Hand corollary of GC897; second reading pending.** Record searched: (driver/parent) + (collision/fibre/fiber/same.child) ->16 hits in7 files; W281 and G4.4 read. Prediction: driver changes supported on child-black positions are invisible, except for exclusion of the zero driver. Independent q4 controls; unexpected constant child1 needs parent0. No census, trajectory or rooted measure claim. This makes the existing reset/OR mechanism explicit rather than claiming a new dynamical principle.

Fix q>=1 and parent x. For a proposed child z let a=x+S z over F2. The actual equation is a=y OR z. At every z-black tick it requires a=1, while y is free; at every z-white tick it requires y=a. Hence the nonzero-driver fibre is empty unless

z*(1+x+S z)=0.

If this compatibility holds, its exact cardinality is

2^weight(z) - indicator[x=Delta z],   Delta=I+S.

Indeed the bits on z's black support are free, so there are2^weight(z) drivers before exclusion. The zero driver is in the fibre precisely when a=z, equivalently x=Delta z. Every remaining nonzero driver gives a unique cyclic child by reset; conversely all such drivers have been listed. Equivalently, two nonzero drivers give the same child under fixed x exactly when their difference is supported on that child's black positions, as follows directly from GC897's invertible response operator. This counts the complete driver domain, not the drivers encountered on a rooted path. Zero-child fibres are terminal states, not live continuations.

**Independent controls.** At q4, x=1111 and z=1010: S z=0101, a=1010=z and Delta z=1111. The allowed drivers are exactly1000,0010,1010; all give child1010, while0000 is excluded. The other alternating child0101 similarly has drivers0100,0001,0101. Thus fixed-parent cross-driver injectivity is false, despite injectivity of the pair map (its outputs retain the driver coordinate). For z=1000, S z=0001 and a=1110; the driver bits at positions1,2,3 are1,1,0, while position0 is free. The two drivers are0110 and1110. Here x!=Delta z=1001, so no driver is removed. These are direct four-bit substitutions, no enumeration.

**Unexpected endpoint controls.** For z=1, compatibility forces x=0; its fibre is all2^q-1 nonzero drivers, recovering the already credited prefix edge (0,y)->(y,1). For z=0, compatibility is vacuous and the sole possible driver is y=x; its count is1 for x!=0 and0 for x=0, exactly the terminal guard. At q1 the same formula yields just (x,y,z)=(0,1,1) or(1,1,0), so no hidden q>=2 assumption is used.

For every even q>=2, x=1 and either alternating z has2^(q/2)-1 nonzero drivers producing that same child. **Rooted control, not just ambient:** for dyadic q>=4, exactly2^(q/2)-2^(q/4) of those drivers are primitive. The nonprimitive words are precisely those of period dividing q/2; their allowed alternating support has q/4 free bits, so subtraction gives the count. Each primitive y occurs at depth2 of the genuine prefix (0,c)->(c,1)->(1,y), with c=1+S y (thus y=1+S^(-1)c); c is also primitive. The next state is (y,z). At q4 the primitive drivers1000 and0010 both give z1010, from roots c1110 and1011 respectively. These are different roots, not repeated events on one history, and their successor pairs remain different. No return length, charge, probability or growth conclusion follows. The fibre equation closes only a cross-driver injectivity shortcut, including across rooted prefixes. Next require within-history occurrence information rather than more complete-domain averages; scratch deferred.


**W281 second-reading receipt (2026-10-10 00:16 BST).** Local L511 atb9f47663 independently checks GC897's forcing law, Green intervals, rank/collision/union mean, cancellation and measure guard, and GC899's fibre formula, endpoints and primitive rooted-prefix count. PASS by hand with scope retained: no rooted frequency or return bound. Formal promotion remains separate.


#### GC901 — Alternating-child collisions recover the driver one profile later (2026-10-10 00:20 BST; W281 continuation)

**Hand continuation, second reading pending.** Record searched: (alternat/period2) + (recover/driver/doubl) ->110 hits in34 files. Read G128.1's period-two closure guard, G201's nonpersistent sibling separation and G185's period/order recovery failure. Prediction: GC899's shared alternating child is followed by a profile that duplicates complemented driver bits. Countercontrol period recovery need not have large Hamming weight; unexpected q2/full alternating driver and rooted-ancestry guards. No trajectory, census, new order-growth claim or novelty claim for reset recovery.

Fix dyadic q>=4, m=q/2, parent x=1 and shared child z with z(2r)=1,z(2r+1)=0. GC899's driver fibre consists of nonzero y with y(2r)=b_r and y(2r+1)=0. Let v be the unique child of (y,z). A black z tick resets the following v bit, and a white z tick has y=0 and copies v. Therefore, cyclically,

v(2r+1)=v(2r+2)=1+b_r.

This explicit inverse recovers b_r=1+v(2r+1); distinct drivers in the same fibre cannot produce the same v. Its weight is q-2*weight(y). If y is primitive q, b is primitive m and nonconstant. For any proper dyadic divisor p>=2 of q, shifting v by p preserves the pair phases and is equivalent to shifting y by p; constant v would force constant b. Hence v is primitive q too. The other alternating phase follows by translation. This is profile-period recovery, not a new stage entry or exit.

**Independent substitutions.** q4, y1000 and z1010 give v1001; y0010 with the same z gives v0110. Each triple satisfies S v=y+(z OR v) directly. Their zero-started prefixes are (0,1110),(1110,1),(1,1000),(1000,1010),(1010,1001), and the corresponding root1011 with driver0010. Distinct successor pairs were never merged; the projected child alone collided.

**Sparse recovery family.** Take b all1 except one0. For m>=2 it is primitive m, so y is primitive q, yet v consists of exactly two adjacent black bits at the complementary pair. At q8 choose y10101000,z10101010,v10000001; the shared z has period2 while v recovers period8 with weight2. Thus profile-period recovery alone supplies no weight growing with q. This is a literal family of actual Boolean transitions in zero-started fixed-q excursions: c=1+S y is primitive, and (0,c)->(c,1)->(1,y) is the known prefix. It does not prove those starts occur after a smaller-period stage of the physical rooted history, or recur on one selected path. GC899's “different rooted prefixes” must be read with this same fixed-q zero-started scope; no physical-root ancestry was added by the count or by L511's hand review.

**Unexpected terminal guard.** If y equals the full alternating z then b=1 and v=0, as y=z is the terminal condition; y has period2 and is excluded from primitive q>=4. At q2 it is the sole nonzero fibre driver, so the claimed recovery fails there. If y=0 then b=0 and v=1, but the original fibre excludes that driver. These extremes explain both exclusions without a run.

Disposition: the response's loss of visible driver information is temporary in this family, and the next profile retains it sparsely. Cross-driver collision size is neither coalescence of full states nor a large-charge certificate. This is a W281 scope corollary, not a replacement for G184's within-history normalized stage-length obligation. Next a concrete physical-ancestry or within-history constraint, no new full-domain census; scratch deferred, room closed.


**GC901 second-reading receipt (2026-10-10 00:26 BST).** Local L512 at77967ffa verifies the reset/copy formula, primitive-period transfer, q4/q8 sparse controls and full-alternating terminal guard by hand. PASS with zero-started-root scope and no physical ancestry, rooted frequency or return bound. This continuation is reviewed; formal promotion remains separate.


#### GC903 — The q4 fibre examples lie on a nonrooted predecessor cycle (2026-10-10 00:31 BST; W281 scope correction)

**Bounded exact check and short hand certificate; second reading pending.** Record searched: (root/ancestr) + (first.hit/backward/predecessor) ->266 hits in49 files; (1110/1011) + (ancestr/cycle/root) ->84 hits in28 files. Read G7/G156/G157 and reviewed G199's absorption criterion; reset/ancestry mechanisms are existing results, not new claims. Predicted GC899's q4 zero-starts share a nonabsorbing orbit. Two named starts only, <=256 states each, independently scalar-bit and packed implementations, cap1 control and unexpected all-rotation checks. No census, new large run, physical-seed evolution or all-q ancestry classification.

**Exact result.** For B(a,b)=(S b XOR(a OR b),a), the start (0,1110) returns to itself after28 steps, with no transient or zero visit. (0,1011) lies on that same orbit,14 steps away. Scalar and packed predecessor updates agree throughout each named chain; cap1 (0,1) hits zero in1 step and (1,0) in3. All four simultaneous rotations have the same28-cycle result. These computations are exact small-state controls, not evidence of absorption for any untested family.

**Seven-step certificate, words in increasing temporal order.** The successive B states are

(0000,1110), (0011,0000), (0011,0011), (0101,0011),
(0001,0101), (1111,0001), (1101,1111), (0000,1101).

Each arrow is direct substitution. The last state is (0,S(1110)); B commutes with simultaneous S, so four copies give B^28(0,1110)=(0,1110). None of the seven states is zero, and the rotations of their seven pair types are distinct: the two zero-coordinate types have distinct coordinate locations, the equal pair has neither zero nor alternating/constant companion, the alternating-driver and alternating-first types differ, and the two constant-one types have different coordinate locations. Within each type a primitive four-bit coordinate distinguishes its four rotations. Thus the cycle has exactly28 distinct states. This short certificate proves nonabsorption without trusting a long trace. Since1011=S^2(1110), its start is reached at14 steps and has the same property.

By G199, a nonzero pair is in the physical-root tree exactly when some B iterate reaches(0,0); its last nonzero predecessor would necessarily be(0,1). These q4 starts fail that test, as do all their actual prefix/continuation states from GC899/GC901. More strongly, their zero-first-coordinate starts are themselves cyclic, so compatibility and a finite zero-started excursion are not physical ancestry. Root phase shifts cannot repair this, because B commutes with temporal rotation.

**Correction retained.** GC899's earlier “rooted control” and “all realized at depth2 from different roots” refer only to arbitrary zero-started fixed-q excursion starts. They must not be cited as occurrence in the physical tree rooted at(0,1). GC901 already narrowed that claim; GC903 now proves physical nonrootedness for the q4 controls. L511/L512 validate the fibre and sparse-recovery algebra, not physical ancestry. Their reviews remain valid in that narrowed scope. The formulas, primitive-driver count and q8 algebraic control are unaffected, but no larger-q physical rejection or rooted occurrence claim is inferred.

Disposition: close physical-root transfer of these q4 fibre examples; retain the within-history Q7 obligation. This is an application of the known ancestry barrier, not a new prize avenue or periodic-point classification. Next an actual physical-tree constraint or peer review, rather than another ambient-family extrapolation; scratch deferred, room closed.


#### GC904 — Genuine doubling entries exclude the alternating-fibre collapse (2026-10-10 00:36 BST; W281 continuation)

**Hand corollaries of reset and G201; second reading pending.** Record searched: (complement/half-shift/half-difference) + (primitive/period-f/last-profile) ->187 hits in36 files. Read G157/G162/G185/G188 and G201 in full. Predict an antiperiodic driver with a nonzero half-periodic parent forces primitive dyadic child. Countercontrol parent0 permits constant child1. No solver, trajectory or census. The preregistered broad expectation of no weight-growth consequence was too strong: G201 gives a linear ONE-profile weight bound below, while cumulative charge and stage growth remain unproved. A draft q4 control child0010 failed substitution; reset recomputation corrected it to0001, and all four triples then pass. The failed control is retained, not attributed to the theorem.

**Primitive-child guard.** Let q>=2 be dyadic, T=S^(q/2), Tx=x!=0, Ty=1+y, and let z be the unique q-periodic child of (x,y). If Tz=z, subtract the original and shifted compatibility equations to obtain

0=(y+Ty)*(1+z)=1+z.

Thus z=1. Its original equation would give1=x+1, forcing x=0, a contradiction. Hence Tz!=z. Every proper divisor of dyadic q divides q/2, so z has least period q. The nonzero-parent hypothesis is essential: (0,y) always has child1 for nonzero y, including antiperiodic y. No order-maximality claim is made.

**Actual doubling application.** At an odd zero-driver integration from q/2 to q, the prefix is0,c,1,e,f with Tc=1+c and e=1+S^(-1)c, so Te=1+e. The guard with parent1 gives f primitive q. This applies at every genuine doubling entry, including physical ones, without asserting that every arbitrary antiperiodic c has physical ancestry. At q>=4 it excludes GC899/GC901's alternating child at this early position. For q2 alternation itself is primitive, so it is not excluded.

**G201's one-profile charge, now symmetric in half-shift.** The child of (1,Te) is Tf by reset uniqueness and translation. G201's complementary-driver equations give f*(Tf)=0 and D=f+Tf has no cyclic00. Since weight(Tf)=weight(f),

q/4 <= weight(f) <= q/2.

The lower inequality follows from weight(D)>=q/2 and the upper from disjointness. Interpret these integer inequalities with rounding when q2. This is an explicit consequence of the reviewed G201 coupling, not a new invariant. Thus the entry's shared-child collapse is ruled out both by primitive period and, for larger q, by a one-profile mass constraint. The bound is not summed across later profiles: G201 already supplies an actual rooted counterexample to persistent sibling disjointness.

**Independent controls and sharpness.** The q4 genuine doubling prefix a1010,0,c0110,1,e1100,f0001 satisfies all four scalar triples. Its f has weight1=q/4 and primitive4. At q8 take e11110000 and f00000101; black resets and four white toggles give that child directly, with weight2=q/4 and primitive8. Then c=1+S e=00011110 has complementary halves and Delta c=00100010 repeats the odd block0010, so this is an actual odd-doubling-compatible prefix (physical ancestry not asserted). Parent0 gives constant1, the exceptional guard. At q2 the entry c01,e01,f01 is the known smallest doubling and f is primitive2, consistent with the lemma and weight interval.

Disposition: a genuine entry has more structure than arbitrary zero-started fibres; GC903's nonrooted q4 controls cannot be transferred there. This closes that early-position collapse scenario, not later same-period branch scenarios or all-period ancestry. The main Q7 obligation remains normalized lengths along each physical history. Next exploit retained actual backgrounds or review CL125's repaired gates; scratch deferred, room closed.


**W281 GC904 second-reading receipt (2026-10-10 00:53 BST).** Cloud CL127 independently checks half-shift subtraction, primitive-period guard, prefix antiperiodicity and G201 weightq/4..q/2, including q4/q8/q2 substitutions. PASS by hand; physical-entry data are Cloud's disclosed additional control, not GPT replay. Same-period branch starts do not inherit the doubling-entry guard. No cumulative charge or stage bound.


**G276 second-reading receipt (2026-10-10 01:00 BST).** Cloud CL129 verifies GC872's composition law, factorial moments, variance/covariance, fifteen-composition control and q8 arithmetic by hand. Independent primitive q8 orbit replay gives T7443 and odd-doubled live lengths87/370. PASS; the abstract null is a calibration, not an invariant or physical ancestry law. No GPT rerun.


#### GC909 — Equality in the doubling-entry q/4 weight bound (2026-10-10 01:04 BST; W281 continuation)

**Hand equality audit; second reading pending.** Record searched: q/4/quarter/lower-bound + G201/half-shift/antiperiod ->18 hits in11 files; GC904, full G201 immediate coupling and G199 physical-entry exclusion read. Prediction: equality forces alternating union and a one-parity source. Countercontrol sharp ambient q8 example is not physical; unexpected finiteq8 exclusion must not become an all-period assertion. No solver, trajectory or census. This refines the reviewed coupling bound, not its cumulative/stage scope.

Let q>=4 be dyadic, T=S^(q/2), and e the antiperiodic entry driver, with child f of(1,e). GC904/G201 give f*Tf=0 and D=f+Tf no cyclic00. If weight(f)=q/4, then weight(D)=q/2. A cyclic binary word with no00 and exactly half ones must alternate: every zero has a following one, exhausting the ones, so no11 can remain. Thus D is one alternating parity indicator and f vanishes on the opposite parity. On the supported parity, Tf=1+f.

The driver is then forced, not free:

    e = 1 + f + S f.

At a supported tick t the next f is0. If f(t)=0, its child equation requires e(t)=1. If f(t)=1, the half-shifted tick has f=0 and hence Te(t)=1; antiperiodicity gives e(t)=0. At the other parity f(t)=0, so the child equation says e(t)=1+f(t+1). Together these are the displayed identity. Conversely if f is supported on one parity and f+Tf equals its alternating indicator, defining e by that identity gives Te=1+e and S f=(1+e)(1+f) at both parities. Its weight isq/4, because each half-shifted support pair contributes exactly one black bit.

In the integration prefix, c=1+S e and the preceding source a=Delta c. Therefore

    a = S e + S^2 e = S f + S^3 f.

Both terms lie on the parity opposite f, so a vanishes on f's parity. The known odd-half-block integration condition is retained; this identity does not prove physical ancestry of a. It identifies the precise extra shape a future ancestry exclusion would need to rule out, rather than testing generic sparse drivers.

Independent literal substitutions: q4 f0001 gives e1100 and a1010, the reviewed physical sharp control. q8 f00000101 gives e11110000 and a00100010, the reviewed ambient sharp control. Its source is a rotation of RC88's repeated one-hot half-source17, so G199/GC907 excludes physical ancestry atq8. By the existing unique physical q8 entry class, equality cannot occur there (Cloud CL127 separately reports weight3); rotations do not change weight. This is a finite known-ancestry consequence, not a new all-q strict inequality. No claim that every larger physical source fails the one-parity shape, or that even a strict one-profile bound can be summed over a stage.

Disposition: equality characterized exactly in the antiperiodic-entry class; parity support is a concrete ancestry test target, not yet an asymptotic obstruction. Next check the existing physical-source record for this shape before any computation; scratch deferred, room closed.


**W281 GC909 second-reading receipt (2026-10-10 01:09 BST).** Local L514 checks equality forces alternating D, one-parity f and e=1+f+Sf; verifies converse and source a=Sf+S^3f by hand, including q4/q8 literal controls. PASS, with no all-q ancestry exclusion or stage-growth claim.


#### GC911 — One-parity odd sources exactly produce sharp doubling entries (2026-10-10 01:14 BST; W281 continuation)

**Hand converse, second reading pending.** Record searched: one-parity/vanishing-parity + integration/equality/source ->20 hits in6 files. GC909/L514 and G157/G158 integration facts read. Predict one-parity odd sources give both sharp children. Countercontrol physical mixed-parity source119 has weight3 atq8; unexpected use the source's own period, not its even cap repetition. No ancestry/tree census or solver; only q4/q8 small integration controls.

Fix dyadic q>=4 and m=q/2. Let a be m-periodic with odd weight over one m-block, represented at capq, and supported on one temporal parity. Seek f supported on the opposite parity satisfying

    (1+S^2) f = S^-1 a.

On that parity, S^2 is a single cycle of lengthm. The right side has even total weight at capq (two copies of the odd m-block), so cyclic integration has exactly two solutions there; off that parity set f=0. Advancing by T=S^m crosses half of this decimated cycle. The accumulated right-side parity is the odd weight of a's one m-block, so Tf=1+f on its supporting parity. The two solutions differ by that parity indicator D and are half-shifts of each other. Consequently each has weightq/4.

Set e=1+f+Sf and c=1+Se. GC909's converse proves Te=1+e and f is the unique child of(1,e). Further,

    Delta c = Se+S^2e = Sf+S^3f = a.

Thus c is a valid integration child of(a,0). Switching f by D switches e by D+SD=1 and switches c by1, so these are exactly the two integration choices, not just one special branch. Conversely GC909 already proves any sharp child has a one-parity source. Therefore among odd-doubling sources, sharp entry weight is equivalent to source support on one parity, and it occurs for both branches or neither. No physical membership is implied by this equivalence.

Scalar control directly closes the child recursion for both integration choices of every one-parity odd half-source atq4/q8: four and eight branch controls respectively give weightq/4 and a=Sf+S^3f. Mixed-parity physical source119 atq8 gives weight3 for both choices. These are finite equation controls, not a census of physical sources. The odd flux is over the m-block; counting capq parity would incorrectly give0 and lose antiperiodicity, the same guard as G199.

Disposition: the planned ancestry test is now an exact source-shape test, not a generic sparsity heuristic. A future proof that physical odd zero returns of least period>=4 cannot be supported on one parity would rule out equality at all doubled periods>=8; that hypothesis is OPEN. Even proving it gives only strict one-profile weight, not G184's stage budget. Next examine a concrete inverse-history constraint for the source mask; no new full-domain scan. Scratch deferred, room closed.


**G275 second-reading receipt (2026-10-10 01:14 BST).** Cloud CL131 verifies GC870's period invariance, primitive counts, rotation freeness for chains, equivariant lifts, tail law and small controls by hand. Independently replays pooled chain/cycle masses atq2/4/8 and detects nontrivial cycle phase lifts. PASS with all-source/null scope; restricted physical-source growth remains open. No GPT mass replay.


#### GC912 — Backward mask preflight: retain the pair, not one profile (2026-10-10 01:18 BST; W281 continuation)

**Hand shortcut audit; no general ancestry result.** Record searched: parity/mask/support + backward/predecessor ->226 hits in56 files; GC911/G199 and CL132 read. Predicted single-profile parity support fails as a backward invariant. Countercontrol physical q4 source suffers the same mask loss. Unexpected structured fourth pair must not be treated as a new zero-driver source. No solver, physical-tree census or growth claim.

Let a be any nonzero word supported on one parity at an even capq. Then a and Sa have disjoint support, so OR equals XOR for those two words. Four direct applications of B(x,y)=(Sy+(x OR y),x) give

    (a,0) -> (a,a) -> (a+Sa,a) -> (a,a+Sa) -> (a+S^2a,a).

For the second arrow, a OR a=a. For the third, (a+Sa) OR a=a+Sa because a and Sa are disjoint, and Sa+(a+Sa)=a. The fourth uses a OR(a+Sa)=a+Sa, giving S(a+Sa)+(a+Sa)=a+S^2a. These are backward steps, not the forward zero-return excursion.

At B^2 the first profile a+Sa has black bits on both parities for every nonzero a. Therefore the property “first profile supported on one parity” is not backward invariant, even on physically ancestral controls. At B^4 both profiles again have support on a's parity, but the second is a!=0; this is not a renewed zero-driver state and supplies no source-only decimation recursion. The full pair is essential. At least-period2 source a1010 at cap4, S^2a=a and B^4=(0,a), consistent with the known physical prefix, so mask loss cannot certify nonphysicality by itself. No conclusion about higher-period absorption follows from these four steps.

Literal scalar controls over the six q4 and thirty q8 nonzero one-parity words agree with all four pairs and the mixed-parity B^2 claim. These are finite local identities, not an ancestry census. The immediate single-profile invariant shortcut is closed; a pair-level inverse condition or a later zero-return constraint would be new required input.

**GC911 second-reading receipt.** Cloud CL132 checks decimated cycle/half-cycle flux, GC909 converse, source identity and exact correspondence of the two integration choices by hand. Independent all-odd-source replay toq32 agrees, with mixed-parity minimumq/4+1 there. PASS; replay is Cloud's evidence, not GPT execution, and does not assert physical ancestry. Next seek an actual pair-level constraint or change lane if none emerges; scratch deferred, room closed.


#### GC913 — Four-step pair-mask closure fails beyond period 2 (2026-10-10 01:22 BST; W281 continuation)

**Hand Boolean preflight; second reading pending.** Bears on Q7: closes the masked-pair recursion shortcut, not physical ancestry or either growth gap. Record searched: backward/inverse/predecessor + decimation/four-step/parity-mask/pair-mask ->13 hits in6 files; GC912 and GC911 read. Predicted shared-parity support at B4 is lost at B8 beyond period 2. Countercontrol: the physical alternating source must absorb instead. Independent one-hot q8 substitutions below; unexpected check proves both parity parts nonzero, rather than assuming a surviving term cannot cancel. No computation, census, solver or source-frequency claim.

Let q be even, with all words cyclic at cap q, and let a be supported on one parity. S is the one-tick shift, addition is XOR, products are pointwise AND. Set

    d = a + S^2 a,    h = a OR S^2 a,    r = a * (1 + S^2 a).

GC912 gives B^4(a,0)=(d,a). Since d is supported inside h, and Sa lies on the opposite parity, four further applications of B(x,y)=(Sy+(x OR y),x) give

    B^5 = (h + Sa, d),
    B^6 = (h + S^3 a, h + Sa),
    B^7 = (r, h + S^3 a),
    B^8 = (h + S^4 a + Sr, r).

For B5, d OR a=h. For B6, (h+Sa) OR d=h+Sa, and Sd=Sa+S^3a. For B7, the union is h+(Sa OR S^3a)=h+Sh, while the shifted second profile is Sh+S^2a. Their XOR is h+S^2a=r. For B8, r is contained in h, so the union is h+S^3a. Its XOR with Sh+S^4a has opposite-parity part Sh+S^3a=S(a*(1+S^2a))=Sr, giving the formula. These are local substitutions in the full pair, not a source-only map.

If a differs from S^2a, then r is nonzero: otherwise supp(a) is contained in supp(S^2a), and equal cyclic weights force equality. The even-side term h+S^4a (the parity supporting a, whether literally even or odd) is also nonzero. If it vanished, wt(h)=wt(a); since h contains both a and S^2a, again a=S^2a. Thus B8's first profile has both parities whenever a is not period-2 invariant. The second profile is nonzero and remains on a's parity. The condition that BOTH profiles lie on that parity is therefore not invariant under four backward steps: it holds at B4 and fails at B8. If a=S^2a, then r=0 and h=S^4a=a, so B8=(0,0). This also covers a=0; no nonzero higher-period source absorbs within these eight steps. Later absorption is unresolved by this calculation.

**Independent literal controls.** Define S to send support j to j-1 modulo q. For q8 and a supported at {0}, the eight pairs, after the initial ({0},empty), are

    ({0},{0}), ({0,7},{0}), ({0},{0,7}), ({0,6},{0}),
    ({0,6,7},{0,6}), ({0,5,6},{0,6,7}),
    ({0},{0,5,6}), ({0,4,6,7},{0}).

Each follows directly by shifting the second set and taking the symmetric difference with the two sets' union. It checks the formula without Boolean expansion. For q4 and a={0,2}, GC912 ends at (empty,a); the next four pairs are (all,empty), (all,all), (empty,all), (empty,empty). This is the known physical period-2 source, so it refutes any claim that losing the intermediate mask itself forbids physical ancestry.

**Disposition.** The B4 shared-parity pair does not give a closed four-step decimation dynamics. Both the single-profile shortcut (GC912) and this pair-mask shortcut are closed; actual physical one-parity source exclusion remains OPEN. The algebra introduces the directed decimated boundary r, but no monotone quantity or persistent charge follows. Do not extend this local expansion into an unregistered long trajectory search. Next change to a concrete incoming proof audit or a different open Q7 constraint. Duplicate gate W281 passes; nearest W280, G201 and W273 were read in preceding blocks and supply different response, sibling and component results. Scratch deferred, room closed.


#### GC914 — The ambient mixed-source minimum is q/4+1 at every dyadic q>=8 (2026-10-10 01:26 BST; W281 continuation)

**Hand construction, second reading pending.** Bears on Q7: calibrates the strict one-profile bound, without a physical stage estimate. Record searched: G201/half-shift/antiperiod + converse/minimum/q/4+1 ->11 hits in5 files; G201, GC904, GC909/GC911 and CL132 read. Predict CL132's measured mixed-source minimum extends to every dyadic q>=8. Independent q8 literal control below; countercontrol admissible integration does not imply physical ancestry (G199's source17). Unexpected check uses half-block flux to prove the source's least period, not merely its cap period. No run, scan or external theorem is used; this is a converse construction from the recorded child equation.

**A general realization guard.** Put m=q/2 and T=S^m. Suppose a binary f has f*Tf=0, no cyclic11, and D=f+Tf has no cyclic00. Define the driver at each tick by

    e(t) = 1+f(t+1) if f(t)=0;   e(t) = f(t+m+1) if f(t)=1.

Then Sf=(1+e)(1+f): at a white tick this is the defining formula, and at a black tick both sides vanish because f has no11. Also Te=1+e. If D(t)=1, exactly one of f(t),Tf(t) is black; the two case formulas at those ticks sum to1. If D(t)=0, both are white, and e(t)+Te(t)=Sf(t)+STf(t)=D(t+1)=1. Thus e is antiperiodic and nonzero. Define c=1+Se and a=c+Sc. Then Tc=1+c, Ta=a, and (a,0,c,1,e,f) is an admissible integration prefix. In particular a's weight on any m-block is odd: XOR over that block of c(t)+c(t+1) telescopes to c(t)+c(t+m)=1. Since m is a power of2, any smaller least period would repeat an even number of times in that block and give even parity. Therefore a has least period m. This guard realizes a child; it does not certify a's physical ancestry.

**Explicit near-sharp family.** Index ticks 0..q-1 in increasing time. Set f black at every even tick in 0..m-1, and at the single tick m+1, and white elsewhere. For q>=8, m>=4 is even. The first half ends in a white tick; the second half has an isolated black tick at m+1; the cyclic join also has no11. Its half-shift is disjoint from it. D is the alternating even-parity indicator with two extra black ticks at1 and m+1, so it has no00. The guard therefore realizes a genuine odd doubling entry, with

    wt(f) = m/2+1 = q/4+1.

GC911's reviewed equivalence implies the source a is mixed-parity: a one-parity source would instead force wt(f)=q/4. Conversely every mixed-parity odd source has weight strictly greater than q/4 by GC909/GC911, hence at least q/4+1 by integrality. The construction attains it at every dyadic q>=8. Both integration choices have the same weight, since their entry children are half-shifts. This turns CL132's finite ambient minimum into a hand all-period statement. It makes no claim about the minimum over physical sources.

**Independent q8 literal check.** In increasing time order the construction gives

    f=10100100, e=10010110, c=11010010, a=01110111.

Directly shift each string one tick left cyclically to check Sc=a+c, Se=1+c and Sf=(1+e)(1+f). Also Te=1+e, and a repeats the odd-weight block0111. Its entry child has weight3, equal to8/4+1. The source is the known physical source119 from GC907/CL132, so this smallest control is physical; that does not promote the whole constructed family. In contrast, G199's cap8 source17 gives valid odd integration and sharp weight2 but is nonphysical, refuting the general admissibility-to-ancestry inference.

**Disposition.** Merely excluding one-parity sources cannot strengthen the ambient weight bound beyond q/4+1; a larger physical bound must use an additional ancestry restriction. This is a calibration of a possible argument, not a claim that one-bit improvement is useless or that it bounds a whole stage. No persistent charge or growth inference follows. Next ask for the realization guard and period-flux check to be second-read, then choose a physical-history constraint or a concrete audit rather than resuming mask expansions. Scratch deferred, room closed.

**GC914 filing check.** W281 duplicate gate passes; nearest W280, G201 and W273 supply response, sibling and component mechanisms rather than this realization family. G201 was reread in full this block. Draft future time labels were corrected before publication to the verified clock at 01:26 BST; the claim and predictions were written before the hand derivation. No computational experiment or formal promotion.


#### GC915 — Physical sharp-entry witness independently verified; exclusion REFUTED (2026-10-10 01:30 BST; W281 continuation)

**Fixed-witness computational audit of Cloud CL134 at 2b55b6cb.** Bears on Q7: closes the proposed universal physical one-parity-source exclusion. Record searched: one-parity/1010100010100000 + physical/87867 ->30 hits in6 files. Read SE's full source/header, CL134 and GC911. Predictions and countercontrols were registered before execution in rule30_gpt_sharp_witness_audit.py, which imports neither SE nor ZF. The initially intended study of GC914's source family was deferred for this priority counterexample.

The time-order source a=1010100010100000 has weight 5, least period 16, and all odd ticks white. An independently written literal-cell B recurrence reaches (0,0) from (a,0) in exactly 87867 steps. The repeated cap 32 lift reaches it at the identical step. Both integrations and the following prefix give entry children of weight 8=32/4; every local child equation was independently tested. Controls: physical q 4 source1010 absorbs at 8; nonphysical q 8 source10001000 instead enters a backward cycle with transient 29 and cycle 28. All checks PASS. The identified unexpected cap-lift check preserves absorption depth exactly. No ZF tree, SE randomness, census, branch count or TM6b parse was replayed.

Thus a physical odd source of least period 16 is one-parity, and its doubled entry is sharp. GC911's possible universal exclusion for least period >=4 is REFUTED. Its equivalence and GC909's equality characterization remain valid; only the proposed physical exclusion fails. GC913's mask-closure failures also remain valid. Proposition8/CL134 identify this exact witness as the single cell's own minimum-N5 history; that attribution is credited to the existing certificate, while the independent calculation verifies its physical absorption and entry weight. Cloud's rarity counts (one of sixteen period 32 entries, none of 56 recorded period64 exits) remain Cloud-only evidence, not a GPT census.

**Review receipt.** CL134 separately verifies GC913's B5..B8 identities, containment/nonvanishing and literal control by hand, then replays small caps and samples cap 32. Accepted as the second reading of the hand shortcut; no quantitative ancestry result follows. Its new physical witness is the separately replicated counterexample above.

**Disposition.** Board note corrected to REFUTED and failure retained in the master. Do not reopen universal parity exclusion without an explicitly narrower new hypothesis. Sharp mass can occur on the target history, so any eventual ancestry-based inequality must allow exceptions or use another quantity. Next examine a different physical-history constraint or a concrete review, not a further parity-mask expansion. No prize claim; scratch deferred, room closed.


**GC914 second-reading receipt and scope guard (GC915 follow-up).** Cloud CL135 checks the realization guard, antiperiodicity, admissible prefix, half-block flux and explicit family by hand; accepted. It independently replays q=8,16,32,64, giving weights 3,5,9,17. These are Cloud's controls, not GPT runs. Its ancestry comparison excludes the constructed source at source periods 8 and 16 (entry periods 16 and 32), using the complete ZF trees. That finite comparison does not establish nonphysicality at every larger period: CL135's wording “physical only at q=8”/“beyond q=8” must be scoped to the compared members unless a further argument is supplied. The all-dyadic ambient minimum proof is unaffected.


#### GC916 — Exact three-state language for all antiperiodic entry children (2026-10-10 01:35 BST; W281 continuation)

**Hand converse audit; second reading pending.** Bears on Q7: identifies an ambient compression without an ancestry filter. Record searched: antiperiod/half-shift/G201 + bijection/three-state/converse/realization ->15 hits in3 files; reviewed G201 necessity and GC914/CL135 realization guard. No run or census. The independent control is a cap4 literal word; countercontrol uses the wrong ordinary closing edge; the unexpected check counts the full language against the antiperiodic driver domain.

Fix dyadic q>=4, m=q/2 and T=S^m. A word f is the child of (1,e) for some Te=1+e if and only if all three conditions hold:

    f has no cyclic11;   f*Tf=0;   D=f+Tf has no cyclic00.

Necessity: Sf=(1+e)(1+f) forbids11. Tf is the complementary-driver sibling by equivariance and uniqueness, so G201 gives disjoint support and the no00 union. Sufficiency is precisely GC914's reviewed realization guard. The driver is unique: at f(t)=0, e(t)=1+f(t+1); at f(t)=1, Tf(t)=0 and the half-shifted white-tick equation plus antiperiodicity gives e(t)=f(t+m+1). Thus admissible f words biject with the 2^m antiperiodic driver words. This is an exact finite alphabet statement, not a claim of physical occurrence or a new growth mechanism.

Write s_t=(f(t),f(t+m)) for t=0..m-1, with three possible states A=00, B=10, C=01. The three conditions above are exactly that adjacent states differ. An A->A edge violates the union's no00 condition; B->B violates f's no11; C->C violates Tf's no11. Every other edge satisfies these local tests. The closing edge is from s_(m-1) to P(s_0), where P fixes A and swaps B,C, because shifting m ticks exchanges the two coordinates. It is NOT an ordinary cyclic closing edge to s_0. The conditions at the second half's join are the coordinate swap of this same test.

**Unexpected exact count.** Let M be the three-by-three matrix with zero diagonal and ones off the diagonal, and P its swap permutation. The number of half-word sequences with this closing condition is tr(M^m P). On the constant-vector subspace M has eigenvalue2 and P acts as1. On the two-dimensional zero-sum subspace M acts as-1, while P has trace tr(P)-1=0 there (the full permutation trace is1). Consequently

    tr(M^m P) = 2^m.

This agrees with the driver bijection. Ordinary cyclic closure instead gives tr(M^m)=2^m+2*(-1)^m, hence 2^m+2 for the present even m. Agreement of the correct count does not select the physical subset: every ambient antiperiodic driver is already included.

**Independent literal cap4 control and falsifiable wrong-boundary check.** At m=2 the allowed half-words are AB, AC, BA, CA. Their f words are respectively0100,0001,1000,0010. For AB, f=0100 and the guard gives e=0011. Directly, Sf=1000=(1+e)(1+f), and Te=1100=1+e. All four words are the known weight1 sharp entries, matching 2^2 drivers. Ordinary closure also admits BC, which gives f=1001 and has cyclic11 across the actual temporal join; it cannot satisfy the child equation. Thus the boundary guard can genuinely fail and is not a bookkeeping preference.

**Disposition.** The three-state representation is an exact converse of the one-profile sibling conditions. It may be a useful encoding, but those conditions alone cannot add a physical-source obstruction: they already realize all ambient antiperiodic drivers. G199 supplies nonphysical integrations and GC915 a physical sharp integration inside that domain. No claim that encoding is useless for future coupled constraints, no new entropy estimate, and no stage-length inference. Next require an explicit ancestry or within-history condition before treating this compression as a prize route. W281 duplicate gate passes; nearest W280/G201/W273 were read in preceding blocks, with G201 reread for GC914. Scratch deferred, room closed.

**Control correction before publication.** The draft swapped e and Te in the cap4 example. Literal substitution rejects e=1100 (its right side is0011, not Sf=1000); e=0011 gives the stated equation. This was a hand transcription failure, corrected before filing; no computational experiment was run.


#### GC917 — Sharp entry sparsity is followed by exact next-profile density (2026-10-10 01:40 BST; W281 continuation)

**Hand actual-recurrence lemma; second reading pending.** Bears on Q7: two adjacent profiles, not a stage budget. Record searched: G201/sharp/q/4/one-parity + next-profile/next-child/3q/4/compensation ->12 hits in8 files. GC909's reviewed equality identity and G201's next-child equation read. No run or census. Independent physical q 4 literal control; countercontrol later siblings staying disjoint; unexpected exact intersection of those next siblings. W281 duplicate gate passes; nearest W280/G201/W273 were read in preceding blocks.

At a genuine sharp doubling entry of dyadic q>=4, let f be the child of (1,e), with wt(f)=q/4. Put T=S^(q/2) and D=f+Tf. GC909 gives alternating D, f supported on D, and e=1+f+Sf. The next actual profile g is the unique child of (e,f). Then

    g = f + SD.

Indeed f and SD have disjoint support, so f is contained in g and f OR g=g. Hence

    e+(f OR g) = 1+f+Sf+f+SD = Sf+D = Sg,

using 1+SD=D and S^2D=D. The driver f is nonzero, so reset uniqueness identifies this compatible candidate as the actual child. Consequently

    wt(g)=3q/4,    wt(f)+wt(g)=q,    f*g=f.

Also g has no00: it is black on every tick of the parity opposite f. Its least period is q. Otherwise f=g+SD would have a proper period dividing q (or period2 if g were constant), contradicting GC904's primitive entry f. This is a within-history consequence and therefore applies to GC915's physical sharp period 32 entry as well as ambient sharp entries; no new physical trajectory was run.

**Unexpected sibling overlap.** Since q/2 is even, T fixes SD. The complementary branch's next profile is Tg=Tf+SD. Thus

    g*Tg=SD,    g OR Tg=1.

Their intersection has weight q/2, exactly the parity that was empty in both entry siblings. This refines G201's failure of persistent disjointness in the sharp class, rather than trying to reinstate that false property.

**Independent physical q 4 control.** In increasing time order take the known prefix driver e=1100 and f=0001. Then D=0101, SD=1010 and g=1011. Direct substitution gives Sg=0111=e+(f OR g). The other branch has Te=0011, Tf=0100 and Tg=1110; its equation gives S(Tg)=1101=Te+(Tf OR Tg). Intersection 1010 and union 1111 refute the disjointness countercontrol exactly. The weights are 1 and 3 on each selected branch, summing to 4.

**Scope.** Low entry weight does not persist even one additional profile in this equality class. However f is contained in g, so the two-profile mass includes repeated black ticks; it is not a cancellation-resistant charge or a conservation law over a stage. No bound on later profiles, return lengths, exception frequency or normalized growth follows. Keep the universal source exclusion REFUTED. Next seek a condition that survives along a selected history or review a concrete incoming proof; scratch deferred, room closed.


**GC916 second-reading receipt (2026-10-10 01:41 BST).** Cloud CL136 verifies the converse, unique driver, swapped closing edge, trace count and corrected cap4 control by hand. Accepted; its independent replay through q32 remains Cloud's evidence. Its additional upper-bound argument also checks: weight(f)=q/2 would require D=1, leaving only B/C states alternating over even m. Then s_(m-1)=P(s_0), violating the closing edge. Thus wt(f)<=q/2-1 for every such entry. Attainment at q4/8/16/32 is Cloud's finite replay, not an all-period maximum proof or a physical count. No stage estimate follows.


#### GC918 — Two-profile compensation needs the sharp guard; no persistent density floor (2026-10-10 01:45 BST; W281 continuation)

**Hand scope preflight, no experiment.** Bears on Q7: retains two failed strengthenings before a stage argument. Record searched: weight/mass/compensation + GC917/10100100/10010001/inverse-shift-f ->8 hits in6 files. GC914's physical control and GC917 read. Independent literal local equations below; countercontrol universal mass>=q; unexpected exact third sharp profile. No trajectory/census or quantitative stage bound.

**A physical mixed-entry counterexample.** GC914's q 8 prefix has a=01110111, c=11010010, e=10010110 and f=10100100. The source is a rotation of the known physical source 119 (GC907), so the actual compatible continuation has physical ancestry. Its next child is g=10010001: f OR g=10110101, and

    Sg=00100011=e+(f OR g).

Reset uniqueness for nonzero f makes this the actual child. Both f and g have weight 3, so wt(f)+wt(g)=6<8. This refutes the tempting extension “every physical doubling entry has two-profile mass at least q.” GC917 stated it only for sharp entries and remains correct. The physical control itself suffices; no ambient-to-physical inference or new B walk is needed.

**Unexpected sharp third-profile identity.** In GC917's sharp class, put h=1+S^-1 f. Then h is black on all of f's supporting parity, while g is black on its opposite parity. Hence g OR h=1, and

    Sh=1+f=f+(g OR h).

Since g is nonzero, h is the unique actual child of (f,g). Thus wt(h)=3q/4, and h has least period q by complement and shift of primitive f. The first three entry profiles have weights q/4,3q/4,3q/4. This is a third-profile formula, not a density floor for all later profiles.

The known physical sharp q 4 control makes that further counterfactual fail. GC917 gives e=1100, f=0001 and g=1011. The formula gives h=0111; its equation is Sh=1110=f+1111. The next actual child is k=0110, because h OR k=h and Sk=1100=g+h. Nonzero h gives uniqueness. Its weight 2 is below 3q/4=3. Thus even the selected physical sharp history does not maintain the three-quarter floor past g,h.

**Disposition.** Sharp-entry compensation has a real, explicitly bounded extent. The universal two-profile mass extension and persistent three-quarter floor are REFUTED by physical local controls. No temporal independence, conserved charge, return bound or exception-frequency statement follows. Any stage argument must track a quantity beyond these first weights. Next change to a different history constraint or an incoming audit rather than continue unsupported profile expansions. Scratch deferred, room closed.

**Review receipts (2026-10-10 01:45 BST).** Local L516 independently verifies GC917's substitution, uniqueness, weight, primitive period, next-sibling intersection/union and physical q4 control by hand; PASS with no persistent-charge claim. Cloud CL137's q 4/q 8 compressed-graph replay complements CL105's earlier GC866 hand classification; received with finite replay scope and no growth estimate. Local's ledger rotation is ingested before this append. L515's two-sided Lean certificate kernel-cost limitation remains Local's lane, not an independent GPT verification. W281 duplicate gate passes; nearest W280/G201/W273 were read in preceding blocks.


**GC918 second-reading and CL138 receipt (2026-10-10 01:52 BST).** Local L519 and Cloud CL138 independently second-read GC918 by hand: PASS. Cloud's physical-tree replay and period-32 weight control remain its measurements. Its additional fourth-profile formula is second-read here: PASS by direct substitution, with no census. Let D indicate f's supporting parity, A=1+D its opposite, u=S^-1 f and v=S^-2 f. Then g=f+A, h=1+u and k=A+u+v. On D, h=1; on A, v=0 and k=1+u=h. Therefore h OR k=h everywhere. Also SA=D, Su=f, Sv=u, so Sk=D+f+u=g+h. Nonzero h gives the unique actual child. On D, k=v has weight q/4; on A, k=1+u has weight q/4. Thus wt(k)=q/2. The independent q 4 control gives 1010+1000+0100=0110, as CL138 states. This proves the formula for every sharp entry; it does not prove convergence to half weight, a later density floor or a stage budget. L518's upward ceiling corrections and L519's map folding received; Q7 remains PART.


#### GC924 — CL143 fifth sharp-profile formula independently verified (2026-10-10 02:20 BST; W281 continuation)

**Provenance and audit scope.** Cloud CL143 at ff25d5f3 derives the formula post hoc after its SL2 experiment; GPT independently verifies it here by hand, without running SL2. Record searched: sharp/twisted plus domain-wall/fifth/rising/SL2 ->9 hits in6 files. W281 duplicate check: 298 entries, no repeats; nearest G201, W280 and W273 read in full. They provide sibling support, reset response and return-interface facts, not this fifth-profile identity. G201/GC909 supply the sharp class and CL138 supplies h,k; those mechanisms are credited. Prediction before this audit: parity elimination and the twisted count hold for every dyadic q>=4. Independent q4 control, ordinary-cycle countercontrol and q4 endpoint exception specified before derivation. No new proof unit.

**Independent derivation.** Let f be sharp, supported on parity pi, with weight n=q/4 and half-shift Tf=f+1_pi. Use reviewed h=1+S^-1 f and k=1_(pi+1)+S^-1 f+S^-2 f. Its next child l satisfies Sl=h+(k OR l). For s on pi put b_s=f(s), A_s=l(s). At parity pi, h(s)=1 and k(s)=b_(s-2), hence

    l(s+1)=(1+b_(s-2))(1+A_s).

At parity pi+1, h(s+1)=k(s+1)=1+b_s, hence

    A_(s+2)=b_s*l(s+1)=R_s*(1+A_s),
    R_s=b_s*(1+b_(s-2)).

The same equation two ticks earlier gives A_s<=R_(s-2). Consecutive rises cannot occur: R_s*R_(s-2)=0. Therefore R_s*A_s=0, A_(s+2)=R_s, and substituting back gives l(s+1)=1+b_(s-2). In full-word notation this proves Cloud's formula

    l=1_(pi+1)+S^-3 f+S^-2 f*(1+S^-4 f).

The two terms supported on pi+1 give weight n there. On pi the last term marks rising edges of the parity-cycle word b. That full word is u followed by its complement, with |u|=n. Its changes are twice the changes tau in u followed by NOT u_1; a cyclic binary word has equally many rises and falls. Thus wt(l)=n+tau. The twisted edge XOR sum is 1, so tau is odd. Choosing its tau change positions and the first bit reconstructs u uniquely, giving exactly 2*C(n,tau) half-words per parity. This count uses the full ambient sharp class; no physical-source count is inferred.

**Controls and unexpected endpoint.** For the known physical q4 f=0001, h=0111 and k=0110, the formula yields l=1100. Literal substitution gives Sl=1001=h+(k OR l), independently verifying the scalar equation; weight 2 equals n+tau=1+1. For q16 and u=0000, the ordinary cyclic count is 0 but the twisted count is 1, giving weight 5, not 4. For u=0101 it is 3, giving weight 7. At q8 n=2 every twisted tau is 1, explaining the same first varying-profile weight throughout that class; no claim about later profiles is derived.

Unexpected q4 guard: n=1 gives tau=1 and even weight 2. For dyadic q>=8, n is even and tau is odd, so wt(l) is odd, with n+1<=wt(l)<=2n-1. Neither this upper range nor oddness extends to q4. The q>=16 weight variation follows because tau=1 and tau=3 both occur. Cloud's longer profile census, symmetry and physical example remain its computations; this hand audit verifies the formula, count and boundary, not the whole run.

**Verdict.** CL143's ambient formula and twisted-count theorem are independently second-read: PASS, with q4 range/parity exception retained. The original experimental hypotheses and failures stay unchanged and post hoc algebra stays labelled post hoc. No ancestry exclusion, stage budget, persistent density or prize claim. Stop density-profile extrapolation without a quantitative path input; next actual reached-history constraint or incoming review.

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

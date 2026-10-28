# PROOFS, section E2, volume 4: G.GPT278 to GPT G343

*Part of [PROOFS.md](../PROOFS.md), section E2 (GPT's proofs, second-read). Moved here unchanged on 2026-10-28 by Local at the owner's request: PROOFS.md had reached 1.9 MB, and E2 was 85% of it. PROOFS.md section E2 indexes every proof in the four volumes. 84 proofs.*

### G.GPT278. Boundary-only matching countermodel (second-read by Cloud, 2026-10-09)

**Promoted from the waiting room, 2026-10-10 (GC965; Local L554).** Second reader: Cloud, chat CL120. Waiting-room heading: "GPT G278 — Boundary-only matching countermodel (GPT, 2026-10-09; waiting room, GC894)".


#### GC894 — Exact boundary edges still allow arbitrary matching in the relaxed interface (2026-10-09 23:46 BST)

**Registered hand preflight; second reading pending.** Record searched: (source/endpoint) + (matching/bijection) ->94 hits in27 files. Read G203's boundary proof and GC865/GC870 mechanisms; targeted search finds no five-boundary construction. Predict those exact boundary edges alone leave arbitrary rotation-equivariant endpoint matching in a partial-bijection relaxation. Countercontrol q2 has overlapping boundary sets. Unexpected omitted assumption is the middle bridge's successor-coordinate constraint. No actual trajectory, enumeration or random draw. This refines the known limitation of GC869's abstract null; it supplies no Rule30 example or prize claim.

**Construction.** Fix dyadic q>=4. Let C be the set of words of least temporal period q, S the temporal shift and Delta=I XOR S. For each c in C and w in C, define five families of live pairs:

A_c=(0,c), B_c=(c,1), C_c=(1,1 XOR S^(-1)c), D_w=(Delta w,w), E_w=(w,w).

The symbols0 and1 here denote the constant q-words. Every displayed pair has nonzero driver and least pair period q. Each family has |C| distinct members. All five families are disjoint: A has first coordinate0 and the others do not (Delta w cannot vanish for primitive w); B has second coordinate1 while the other families do not; C has first coordinate1, which cannot equal w or Delta w for primitive w of period at least4; D=E would require S w=0. In particular Delta w=1 would force an alternating w of least period2, excluded here.

Let pi:C->C be ANY bijection commuting with S. In the primitive live domain define the chains

A_c -> B_c -> C_c -> D_(pi(c)) -> E_(pi(c)),

with E terminal, and give every remaining primitive live pair an identity self-loop. This is a rotation-equivariant bijection from nonterminal pairs to nonstart pairs. Chains are disjoint by the five-family disjointness and pi's injectivity; complement states are identical domain/range leftovers, so their self-loops complete the bijection. Their period strata remain primitive. The first two arrows and D_w->E_w are genuine Rule30-compatible edges: S1=1, S(1 XOR S^(-1)c)=1 XOR c, and S w=Delta w XOR w. Also E_w has the genuine exit to(w,0). Thus the model retains the exact forced three-pair prefix and two-pair suffix, but its source-to-endpoint matching is the arbitrary pi. Each primitive word orbit is free of size q, so arbitrary permutations of the source orbits and arbitrary relative rotations define such pi.

**Independent literal control and missing interior.** At q4 take pi the identity and c=w=1000 in increasing temporal order. The five pairs are(0000,1000),(1000,1111),(1111,1011),(1001,1000),(1000,1000), all distinct. The bridge from the third to fourth pair fails the actual successor-coordinate condition: the next pair's first word1001 is not the previous driver1011. Hence this is explicitly NOT a compatible Rule30 excursion or a claimed return at r6. It is a countermodel only to deductions using the preserved boundary facts, partial bijectivity, period and rotation constraints. The complement self-loops may likewise violate Rule30; they are included solely to complete that comparison model.

At q2, c=w=01 gives C_c=(11,01)=D_w, because Delta w=11. The five-family construction fails exactly at the boundary overlap already identified in G203's r5 control. This is why q>=4 was imposed. It is not a defect repaired by counting the same vertex twice.

**Disposition.** Boundary-only source-to-endpoint matching is CLOSED as a route to an additional invariant: every equivariant matching is represented in a comparison model satisfying these particular boundary constraints. The actual interior recurrence, including the successor-coordinate relation and the Boolean child equation, is indispensable to distinguish Rule30. This does not show arbitrary matching in Rule30, does not model physical-root ancestry, does not satisfy G202's whole-path overlap identity, and does not rule out a mechanism using those omitted facts. Next select an interior relation that is not implied by the boundary package; do not spend a census rediscovering boundary period/rotation correlations. Q7 remains PART.


**GC894 duplicate audit (2026-10-09 23:47 BST).** W278 hard checks pass. Nearest W275 and W273 were read in full earlier this session and credited; W277 was reread in full for this block. They supply quotient symmetry, endpoint injection and reservations, while this comparison construction deliberately retains G203's exact boundary edges and shows their insufficiency without the interior equation. It is not an arbitrary-matching claim for Rule30. No promotion.


**W278 second-reading receipt (GPT, 2026-10-09 23:52 BST).** Cloud CL120 atc9361fcf verifies GC894's genuine boundary arrows, five-family disjointness, primitive pair periods, equivariant partial bijection and q4/q2 controls by hand. Boundary-only closure accepted with the omitted-interior scope preserved. No actual Rule30 matching or trajectory claim, and no review of GC895 follows; formal promotion is separate.


### G.GPT279. Coordinate-preserving driver-row comparison (second-read by Cloud, 2026-10-09)

**Promoted from the waiting room, 2026-10-10 (GC965; Local L554).** Second reader: Cloud, chat CL121. Waiting-room heading: "GPT G279 — Coordinate-preserving driver-row comparison (GPT, 2026-10-09; waiting room, GC895)".


#### GC895 — Restoring successor coordinates leaves driver-row permutation freedom (2026-10-09 23:51 BST)

**Registered hand preflight; second reading pending.** Record searched: (permutation/bijection) + (driver/coordinate) ->8 hits in5 files. GC869/GC870/GC894 and G203 boundary facts read. Predict the successor-coordinate constraint converts the comparison into driver-row permutations; retained boundaries still leave many maps, whereas the Boolean equation selects the actual map. Independent q4 swap, q2 reserved-slot countercontrol and unexpected pair-versus-profile period check. No trajectory, random draw or new actual endpoint census. No claim that endpoint matching remains arbitrary after adding coordinates.

**Row description.** At cap q let Q be all N=2^q temporal words. Live pairs have y!=0. Nonterminal pairs exclude x=y, and nonstart targets have first coordinate nonzero. Any bijection between those domains satisfying the successor-coordinate rule has the form

f(x,y)=(y,g_y(x)),  g_y:Q\{y}->Q\{0} a bijection for every y!=0.

Indeed each domain row has N-1 inputs and its targets are exactly the N-1 pairs with first coordinate y and nonzero second coordinate. Global injectivity makes each row injective, hence bijective; conversely row bijections give a global one. This retains a unique inverse, but not the specific Boolean reconstruction H.

**Retained boundaries, dyadic q>=4.** Keep the actual Rule30 rows for nonprimitive drivers, including driver1. For each primitive driver y, the forced prefix and suffix require just

g_y(0)=1,   g_y(Delta y)=y,

where Delta=I XOR S. These are two distinct inputs and outputs: Delta y!=0, Delta y!=y, and y!=1. The fixed driver1 row already supplies g_1(c)=1 XOR S^(-1)c for primitive c. Thus GC894's exact prefix/suffix edges are preserved. Every remaining primitive row admits (N-3)! completions.

To impose rotation equivariance choose a completion for one driver in each primitive rotation orbit and transport it by

g_(S y)(S x)=S(g_y(x)).

Primitive drivers have free orbits of size q, so this is consistent without extra stabilizer restrictions. With P primitive words and a=P/q driver orbits, this constructs ((N-3)!)^a distinct maps. For primitive y both input and target pairs have least pair period q because they contain y. Nonprimitive rows are unchanged actual rows, so all pair-period strata are preserved. Global partial bijectivity, starts, terminals, exact boundary edges, successor coordinates and rotations therefore do not uniquely determine the interior map. This is a comparison-family count, not a statistical law or a Rule30 orbit count.

**Independent literal swap at q4.** Let y=1000, S y=0001 and Delta y=1001 in increasing temporal order. The actual row has g_y(1111)=1010 and g_y(0001)=0111. Directly checking S z=x XOR(y OR z) verifies both. Inputs1111 and0001 are distinct and outside the reserved slots0,1000,1001. Swap these two outputs and transport the swap over y's rotation orbit, leaving all other rows unchanged. The altered edge(1111,1000)->(1000,0111) preserves the successor coordinate and injective row structure but fails the actual equation at time0: its child bit at time1 is1, while1111(0) XOR(1000(0) OR0111(0))=0. The genuine forced prefix with c=1110 reaches(1,y), so the altered edge changes the first interior continuation of an admissible start. No return endpoint or depth in this altered map was computed.

**Unexpected period scope and small-period guard.** The actual child1010 in this control has least profile period2, though its pair with1000 has least period4. The model correctly preserves pair period, not the period of every individual child. At q2 choose y=01: Delta y=11, so the proposed input1 is a reserved suffix slot and the swap is invalid. This independently prevents extending the q4 witness to the exceptional boundary-overlap case. No q2 model count or rigidity claim follows.

**Disposition.** Coordinate restoration removes GC894's artificial bridge defect but does not recover the Rule30 equation. The decisive remaining condition is x=S z XOR(y OR z); for each actual row it fixes the permutation through reset uniqueness. Adding that full equation exactly recovers the original dynamics, so it is not by itself a reduction of Q7. This preflight closes attempts to infer unique interior continuation from boundary/coordinate/permutation structure alone. It does not close endpoint invariants common to this stronger family, physical-root ancestry or any actual recurrence-based growth route. Next seek an inequality or obstruction using the Boolean equation without merely enumerating its whole dynamics; no further bare permutation-family census is warranted. Q7 stays PART.


**GC895 duplicate audit (2026-10-09 23:52 BST).** W279 hard checks pass. W278 reread in full; W275 and W277 were read in full earlier this session. W278 omits the middle coordinate; this continuation restores it globally using driver rows, without claiming arbitrary endpoint matching. W275 supplies credited free rotations/pair-period scope; W277 supplies credited live interface/reserved endpoints. No new Rule30 growth theorem or promotion.


**W279 second-reading receipt (GPT, 2026-10-09 23:57 BST).** Cloud CL121 atefb7b0c3 verifies GC895's driver-row decomposition, two boundary slots, rotation transport/count and literal q4/q2 controls by hand. Comparison scope accepted; no actual endpoint permutation, return trajectory or GC896 review follows. Formal promotion remains separate.


### G.GPT280. Exact one-driver-bit reset response (second-read by Cloud and Local, 2026-10-10)

**Promoted from the waiting room, 2026-10-10 (GC965; Local L554).** Second reader: Cloud, chat CL122, and Local, chat L510. Waiting-room heading: "GPT G280 — Exact one-driver-bit reset response (GPT, 2026-10-09; waiting room, GC896)".


#### GC896 — One driver-bit perturbation has an exact reset-interval response (2026-10-09 23:56 BST)

**Registered actual-recurrence hand block; second reading pending.** Record searched: (affine/linear) + (driver/reset) ->40 hits in15 files. Targeted perturbation/rank-one search finds no identical one-bit response formula. Read G2 reset mechanism and GC895's actual row equation; these are the credited basis, not a new reset theorem. Predict one-bit driver change, with a common remaining reset, affects either no child bits or the precise interval before that reset. Independent q4 direct substitutions; last-reset countercontrol; unexpected sharp q-1 response. No trajectory, census, random model or literature novelty claim.

**Statement.** Let x,y be q-periodic binary words, q>=2. Toggle y at one temporal position j to get y'. Assume there is a black position in y other than j, hence a common black reset in y,y'. Both drivers are nonzero and their children z,z' solving

S z=x XOR(y OR z),   S z'=x XOR(y' OR z')

are unique. Let k be the first common black position strictly after j in cyclic temporal order. Let I consist of positions j+1 through k inclusive, with cyclic length d between1 andq-1. Then

z' XOR z = (1 XOR z(j))*1_I.

Thus the exact Hamming distance is0 if z(j)=1, and d if z(j)=0. It need not be bounded independently of q.

**Proof.** At any common black position t, both equations reset the following bit to1 XOR x(t), so their difference is zero immediately after that position. Starting at the preceding common black and propagating forward to j encounters no driver difference; at a white tick the difference propagates unchanged and at a black tick it resets to zero. Hence z'(j)=z(j). At the changed tick j the two OR expressions, with identical child bit z(j), differ by1 XOR z(j), so the child difference at j+1 is that value. Until k the common driver is white, hence the difference propagates unchanged. At k it resets to zero at k+1 and stays zero up to j again. This gives exactly the stated cyclic interval. The argument uses actual Boolean equations, not merely global injectivity, row permutations or boundary matching.

**Independent direct q4 controls.** Take x=1111,y=1000,j=1, so y'=1100. The cyclic children are z=1010,z'=0001. Directly substituting their four equations verifies both; their XOR1011 is supported at positions2,3,0, precisely I before the common reset at0. Here z(1)=0 and distance3=q-1. Conversely toggle j=2 instead: y'=1010 while z(2)=1, and z'=1010 remains unchanged. At the changed tick the child1 masks the OR driver change; direct substitution verifies the unchanged child. This latter comparison need not preserve the driver's least period, and no such premise was used.

**Sharp family and unexpected locality failure.** For every q>=2 choose x=1, y black only at0, and toggle the white position j=1 to black. The original reset forces z(1)=0. The first common reset after1 is0 after a full cyclic gap, so d=q-1 and the children differ at every position except1. This realizes the maximal response in actual cyclic equations, for arbitrary q; it is not a physical-root reachability claim. Locality of the Boolean rule in time does not give uniform sensitivity of its cyclic inverse.

**Last-reset countercontrol.** If the only black bit is toggled off, there is no common reset and the stated law does not apply. At q4,x=1111,y=1000, turning y into0000 leaves the two alternating children1010 and0101. Thus the new child is not unique, and the perturbation cannot be assigned one deterministic interval response. This is the same zero-driver integration exception already handled in G2/G158, retained here as a domain guard.

**Relation to row affinity and scope.** For fixed y, write the inverse equation over F2 as x=y+S z+(1+y)*z. It is affine in z; nonzero y makes its linear part invertible by reset uniqueness. This is another expression of the existing reset mechanism, not a growth reduction. The interval formula supplies a specific cross-driver consequence of that equation and a sharp failure of uniform local sensitivity. Comparing different drivers does not show either pair is reached in the physical-root tree, control the frequency of perturbations along a spatial path, or bound a first-return depth. Next require a rooted occurrence/cancellation mechanism before using the interval law for Q7; no sensitivity census is requested. Q7 remains PART.


**GC896 duplicate audit (2026-10-09 23:57 BST).** W280 hard checks pass; nearest G162/G157/G201 read in full. They supply credited reset/run accounting, period preservation and a two-sibling one-profile identity. This entry compares the actual children for one changed driver bit with the same parent, retaining the exact common-reset interval and last-reset guard. No rooted-growth or new reset theorem is claimed; no promotion.


**W280 second-reading receipt (GPT, 2026-10-10 00:03 BST).** Cloud CL122 at8a63a8ae and Local L510 at89e95f43 independently verify GC896's common-reset interval, changed-tick gate, q4 controls, sharp family, singular last-reset guard and affine form by hand. The actual cross-driver lemma is second-read; no rooted reachability/return bound or GC897 review follows. Formal promotion remains separate.


### G.GPT281. Multiple-driver response and complete-parent calibration (second-read by Local, 2026-10-10)

**Promoted from the waiting room, 2026-10-10 (GC965; Local L554).** Second reader: Local, chat L511 (GC897, GC899); its continuations carry their own receipts below. Waiting-room heading: "GPT G281 — Multiple-driver response and complete-parent calibration (GPT, 2026-10-10; waiting room, GC897)".


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

**GC903 second-reading receipt (cited at promotion, Local L554).** Cloud CL126 (CHAT-LEDGER.10.md, line 1323): "GC903 second-read, PASS". GPT acknowledged it there (line 1381) and confirmed it in GC965.


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

**GC913 second-reading receipt (cited at promotion, Local L554).** Cloud CL134 (CHAT-LEDGER.10.md, line 1655): "GC913 PASS", B5 .. B8 by hand and replayed in rule30_cloud_sharp_entry.py. GPT accepted it in GC915's review receipt and confirmed it in GC965.


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


### G.GPT282. The clamped-clock finite seed 1001 has an eternal two-gap train

**Status:** PROVED. Independently re-derived and read by Cloud (CL189)
and Local (L595), 2026-10-10; promoted from W282 by GPT.
This applies Local's existing P8Lock, not a new one-hole lock theorem.
The key new step is causal feedback: only a finite *past* of the proposed
boundary is needed to guarantee the next band update. No eternal boundary
is assumed in the induction. Q3 and the prize remain open.

**Claim.** Under the externally clamped boundary x_t(0) = t mod 2,
the right seed x_0 = 1001000... has x_t(1) = 1100 repeating for all
t >= 0. More strongly, from t = 16 its first fourteen cells equal
P_(t mod 8), where sites are written left to right:

    phase    P_phase
      0      10011000100101
      1      11110101111101
      2      00000101000001
      3      00001101100011
      4      10011001010110
      5      11110111010101
      6      00000100010101
      7      00001110110101

**Finite premises, independently encoded controls.** The retained
`tests/probes/lexicon/rule30_train_p8_closure.py` checks all the following.
Literal Rule 30 lookup and packed Boolean updates agree. A shrinking
46-cell cone checks x_t(1) for 0 <= t <= 32 and the displayed band for
16 <= t <= 32. These checks need no assumption about sites beyond 46.
Every displayed row, with boundary phase mod 2, advances to the next
row for either exterior bit, except phase 4: there it does so exactly
when x_t(15) = 0. In particular column 14 reads 11110111, a rotation
of the one-white/seven-black wall.

**Causal lock, existing result.** If a cell reads 0111111101111111
at times a through a+15, its right neighbour is white at a+16,
whatever the five-cell starting state and whatever inputs arrive at the
sixth cell to its right. This is the n = 0 case of Local's
`tests/probes/lean/P8Lock.lean`, `p8_lock`; GC878 audits its causal
physical transfer. Only the sixteen specified wall bits are used.
To make the finite premise reproducible without a Lean installation,
start with all 32 five-bit states and repeatedly take the union of
both exterior-input successors, using these sixteen wall bits.
The successive image sizes are

    25,20,22,20,20,18,16,13,11,11,15,17,17,15,14,10.

The final image is exactly

    00000,00001,01000,01001,01010,
    01011,01100,01101,01110,01111.

Every member begins white. The probe reconstructs these exact sets
using independent literal and packed update implementations. Unioning
both inputs at every step covers every possible exterior sequence,
including exterior bits correlated with the interior. The eight-tick
image still contains a black-first state, so replacing sixteen by eight
in this argument fails its countercontrol. The established Lean theorem
was source-read; no new Lean compilation is claimed.

**Induction proving eternity.** The warmup supplies all rows from
16 through 32. Suppose the displayed band has held through time t,
where t >= 32. If t mod 8 is not 4, its last cell is black and masks
site 15; the finite transition table gives the correct band at t+1.
If t mod 8 is 4, then t >= 36 and a = t-16 >= 20. By the induction
hypothesis, site 14 on times a through t-1 is exactly two copies of
01111111. Apply the causal lock to sites 15..19, treating site 20 as
arbitrary at every update. It gives x_t(15) = 0, which is precisely
the missing condition for the phase-4 band transition. Thus the band
also advances correctly in this case. Strong induction proves the
band for all t >= 16. Its first cell has profile 11001100; the checked
warmup handles earlier times. This proves the claim.

**Unexpected stronger consequence.** The same conclusion holds for
*every* initial right half whose first 46 cells are 1001 followed by
42 zeros, with no restriction on the remaining tail. Finite speed
makes the warmup identical; the induction already allows every
subsequent exterior input. The probe checks zero and all-one finite
far-tail controls, but the universal-tail assertion follows from the
cone and the proof, not from those two tests. Neither periodicity nor
aperiodicity of site 15 is required or proved.

**Why the earlier window searches do not refute this.** Their failure
was closure of the particular sets sampled along the orbit. This proof
keeps a sixteen-tick boundary history and uses the exact five-cell
all-input lock; it never assumes that a sampled window set is closed.
The original first-macro gate at the 0111 boundary need not be invariant
(GC1018). The proof closes at the farther 01111111 boundary instead.

**Scope and credit.** Cloud's corrected fourteen-site observation
(CL187) identifies the useful boundary; Local's P8Lock supplies the
lock; GPT supplies the phase table and causal self-consistency induction.
The earlier seven-ring certificate (GC1013) realized the same visible
train with a periodic right tail; it did not prove this specified finite
right seed or the arbitrary-tail cylinder result. No finite left half
or all-depth record bound is constructed. `proof_dupes.py --near G271`
returned 03, C1, C2; all three read. Their white latch/checkerboard
rules and G271's black lock are antecedents, not the finite-seed
feedback induction proved here. Waiting-room referral only until
independent review; no new reviewed proof number is claimed.

**Filing check for waiting entry W282.** `proof_dupes.py --near W282`
returned G271, 10 and 37; all read in full. G271 contains the reused
P8 lock and its language consequence, but not this seed or feedback
induction. Entry 10 requires a leftmost black cell and bounds paired
repeats; entry 37 excludes constant columns in a nonzero finite global
seed. Neither applies to the imposed alternating boundary here. W282
is filed for review with its own summary; it is not yet a reviewed entry.

**Independent reviews (CL189 and L595, 2026-10-10).** Both reviewers
used their own implementations to reproduce the warmup, all eight band
transitions, the sixteen-tick all-input image and the failed eight-tick
control. Both accepted the strong induction and the arbitrary-tail
cylinder consequence. Local retained `rule30_gc1020_review.py`; Cloud's
review is in CL189. No assertion about site 15's full trace is needed.
The prior waiting-room wording above records the filing history; this
entry is now reviewed. Neither review claims a solution to Question 3.


### G.GPT284. Primitive birth endings charge a constant after every fixed prefix (second-read by Local, 2026-10-13)

*Where:* RULE30-GPT.md GC1198; transition reused from G13 and GC1191.

**Claim (PROVED; GC1198, Local L683).** Fix any valid header and any body prefix in GC1191's formal primitive-seed grammar. Among its n-bit body extensions ending in1, for n>=3, exactly 3*2^(n-3) are accepted: 2^(n-3) Q and 2^(n-2) P. Acceptance is therefore3/4, independently of the fixed prefix, parity or first child sample. This counts formal prototypes, not clock survivors or realized records.

**Proof.** G13 reads u by (a,b)->(b,u XOR(a OR b)). Two successive bits u,v produce pair(c,e), where c=u XOR(a OR b) and e=v XOR(b OR c). For each target(c,e) there is exactly one input pair: u=c XOR(a OR b), v=e XOR(b OR c). Thus two free bits distribute uniformly over the four states, from any fixed starting pair. Each state also has two incoming labelled edges, so uniformity persists through the remaining n-3 bits. Immediately before the stipulated final1, each state has 2^(n-3) inputs. That1 maps00 to01 (Q), 01 and11 to10 (P), and10 to00 (reject). Summing proves the counts. Consequently the terminal grammar alone cannot give a bound C*2^(-alpha*n) on its acceptance fraction with fixed finite C and alpha>0. Joint temporal clock and child-origin cut checks are not included and may impose additional cost.

**Unexpected boundary check, by hand.** At n=2, initial00 accepts both extensions01 and11, whereas initial11 accepts01 and rejects11. The n>=3 guard is essential; no two-bit or per-word rejection follows from the fraction. No experiment or survival census was run.

**Filing check.** proof_dupes.py --near W284 reports E1, E2 and G131; all three read. E1 gives G13's reset-word characterization, E2 a protected backward window, and G131 a Sturmian block-factor exclusion. This reuses E1's decoder but counts primitive terminal completions after a fixed prefix; it does not restate those claims.

**Promotion receipt (GPT, 2026-10-13).** Local L683 at ebe7a00f reads the two-bit bijection, uniformity, terminal count and n2 guard by hand; no experiment replay. Promoted from W284.


### G.GPT285. A certified cut charges the first zero beyond the depth125 witness (second-read by Local, 2026-10-13)

*Where:* RULE30-GPT.md GC1199; tests/probes/lexicon/rule30_young_birth_zero_ray.py.

**Claim (PROVED; GC1199, Local L684; fixed prefix only).** In phase1, fix initial left depths1..124 to the published depth125 witness in site/wolframcollatzmahler/data/records.json. No actual right trace can coexist with these cells and zeros at depths125..146 for the corresponding query horizon. This excludes a one-cell extension of this witness prefix, not every depth125 prefix or every depth.

**Carrying proof.** A left-neighbour observation at tick t depends only on initial left depths1..t+1 and the fixed wall. Thus every such row gives the same trace through145 as the named zero-ray calculation; farther cells, including147, cannot repair it. The calculation by independent packed-integer and literal lookup evolution gives the visible word at white ticks71,73,...,145 as00100100001000010000100001000010000101. This38-bit word is in the committed phase1 minimal forbidden catalog, whose absence certificate is already adopted. It contradicts any actual right trace. The finite calculation and the prior certificate are tier1 inputs; the all-tail locality implication above is the carrying step read by Local L684. The earlier white samples reproduce the fixture, while the forced last visible1 closes the cut. Equivalently, with the original prefix through145 fixed, that cut requires initial depth146 black.

**Unexpected horizon guard.** With depths146/147 respectively00, the first black-clock failure is146. Setting only147 to1 repairs it without changing any earlier trace or the cut at145. Therefore that zero-ray clock failure alone does not exclude all length22 extensions. The certified cut does: it reads no cell beyond146. No real canonical parent, extra clock tick or all-depth bound is assumed.

**Filing check.** proof_dupes.py --near W285 gives G130, G234 and G240; all three read. G130 supplies general triangular locality, G234 controls delayed deep resonance outside a clock cone, and G240 gives source/edge restrictions. This uses locality and an adopted cut to pin one previously measured white-terminal pivot; it does not restate those results or claim a new coding theorem. GC1155's existing depth125 free-pivot control is credited in GC1199.

**Promotion receipt.** L684 at61f014b8 reads the locality and exact horizon and independently checks the word under three random tails. Its catalog certificate is adopted, not rerun. Promoted from W285.


### G.GPT286. A visible cut residual loses a zero-tail clock charge (second-read by Local, 2026-10-13)

*Where:* RULE30-GPT.md GC1200; uses the already-proved GC1197 gate.

**Claim (PROVED; GC1200, Local L685; exact clock prediction only).** A finite visible suffix, the child phase, and depth modulo28 do not determine the next black-clock verdict of every zero-terminated left row. This also applies to an ordinary finite forbidden-word residual as the visible summary. It does not exclude nondeterministic relaxations or richer finite hidden states.

**Proof from the established guard.** In phase1, let A^1 be GC1197's seven-ring reference. Set b_j=A^1_0(j) for j<ell and b_j=0 for j>=ell. Choose ell_+=14+56u and ell_-=42+56u, with u arbitrarily large. Both are first discrepancies: A^1_0(ell)=1. Before their arrivals, all black-clock tests pass and their visible prefixes are respectively(10)^(3+14u) and(10)^(10+14u). These are actual train prefixes: shifting GC1020's phase0 realization forward three ticks gives phase1 with the same visible(10)^infinity. Hence every sound finite cut catalog accepts them. Their next white sample at tickell-1 is0, since the front flips the reference left-neighbour0 to1. Their next black sample at tickell differs: GC1197's proved phase1 gate permitsell mod56=14 and rejectsell mod56=42. Thus the values are1 and0.

Given any suffix lengthK, choose u so both prior words exceedK. Their finalK symbols agree, both histories have phase1, the next observation has the same time colour, and ell_+=ell_- modulo28. For a catalog of maximal word lengthM, its standard cut residual depends only on the lastM-1 letters; chooseK>=M-1. The residuals are therefore identical before the common next visible0 is consumed, yet the following black guards differ. Hence the specified summary cannot predict that guard exactly.

**Unexpected scope check.** Depth modulo56 distinguishes this pair and suffices for GC1197's narrow two-arrival gate. So the counter is no obstruction to all finite-type certificates, no proof of unbounded memory after adding other coordinates, and no failure of a sound overapproximation that retains both black outcomes. No real long-band membership is asserted for either zero-terminated row, and the passing first guard is not infinite survival. This audits a proposed state compression using proved controls; no new train scan, residue refinement or widening ran.

**Filing check.** proof_dupes.py --near W286 gives G162, G167 and G285; all three read. The first two concern periodic-driver reset costs, and G285 pins one early-departure endpoint by a certified cut. This applies the established GC1197 clock gate to a suffix-state compression claim; it restates none of those results and supplies no new train scan.

**Promotion receipt.** Local L685 at0af287ef reads the two prior words, their phase and depth congruence, the next white sample and both black guards. Its earlier direct B2 controls already contain the named verdicts. No new computation requested or replayed; promoted from W286.

### G.GPT287. A zero triangle fixes the entry packet of its absolute clock guard (second-read by Local, 2026-10-13)

**PROVED, Local L688 at6a84b181.** Source: RULE30-GPT.md GC1203. In an actual clock row with x_0(d-1)=1 and x_0(d..E)=0, d>=2, let k=d+2a+e, c=a+1 and n=d+a-1+e, for a>=0,e in{0,1}, k+1<=E. The row at c has (x_c(n),x_c(n+1))=(1,1-e). The persistent black inner boundary of the white triangle and one literal update prove the packets11/10; no backward real parent is assumed.

For the moving adjacent pair F_u=x_(c+u)(n-u), r_u=x_(c+u)(n-u-1), write h_u=(1-F_u)(1-r_u). Summing the literal update of the cell just behind that pair gives x_k(1)=(1-e) XOR(n mod2) XOR XOR h_u. Thus a black-clock guard requires XOR h_u=(d+a-1) mod2. The final h_u, at white time k-1, is the actual right visible bit demanded by the clock. The full derivation, sharp final-cell and d1 controls are in GC1203; independent fixed controls in rule30_zero_triangle_guard_transport.py. This supplies an origin-preserving guard interface, not a finite-state closure or a record bound. Local's L688 hand read verifies both packets, the exact horizon, guard sum, terminal-white bit and fixed offset class; no computation requested.

### G.GPT288. Adjacent zero-triangle charges encode the actual visible00 pair (second-read by Local, 2026-10-13)

**PROVED, Local L689 atf7e087e2.** Source: RULE30-GPT.md GC1204, following second-read G287. Under its black-offset convention and k+3<=E, let S_t(j)=x_t(j+2)x_t(j+1) XOR [(1-x_t(j))(1-x_t(j-1))][x_t(j+2) XOR x_t(j+1)]. On the old moving path, omit its final position to obtain parity R_a. Then R_a=(1-q(k-1))(1-q(k+1)) for the actual successive white visible bits.

**Proof sketch.** The local empty-pair update has difference S. Shift G287's path one tick and one outward depth; the next path adds exactly one terminal hole q(k+1). At the old terminal, the black guard fixes depth2=1-depth1 and makes S=q(k-1). The required total hole parities differ by1, giving R_a=1 XOR q(k-1) XOR q(k+1). The real no11 gate converts this to the stated00 indicator. Hence valid consecutive R_a cannot contain101, or1111 (the latter would force the old absent word00000). GC1204 gives the complete endpoint proof and registered controls. This is an origin-preserving coupled gate, not a finite-state update, a cost bound or a new proof of no11. L689 hand-reads the local law, shifted path, both endpoints, horizon and visible00 interpretation; no computation requested.

### G.GPT289. An integer hole flux balances adjacent triangle paths (second-read by Local, 2026-10-13)

**PROVED, Local L690 at92e87905.** Source: RULE30-GPT.md GC1205, under G288's actual triangle and horizon. The integer change of the spatial hole after shifting by one time and one outward depth is Delta=AB-h(A+B), where h=(1-C)(1-D) and A,B are the outward cells. If h0 this is AB; if h1 the new hole is(1-A)(1-B), giving AB-A-B. Summing over adjacent paths and using the old black guard makes the terminal Delta=-q_old. Hence J_(a+1)-J_a is the sum of the strict interior signed changes, where J excludes the terminal visible hole. The first change is0 from G287's entry packet.

GC1205's fixed actual125 fixture has J26->31->26 at consecutive a0/1, and31->29 at a8, with direct counts matching creations minus destructions. Thus a proposed monotone cost using J alone is refuted. This is a finite counter, not a repeatable full-state cycle or an impossibility for richer costs. Registered controls in rule30_zero_triangle_hole_flux.py retain the failed prediction. L690 hand-reads the signed law and terminal cancellation, adopts the fixed counts as tier1 and checks the recoding scope.

### G.GPT290. The ordinary fringe already meets the proposed middle-turnover floor (second-read by Local, 2026-10-13)

**PROVED, Local L691 at3ae23c02.** Source: RULE30-GPT.md GC1206. For its d>=8 black-ended zero band and N consecutive eligible charge paths a>=4, the real middle parity is1 on visible triples001/010. Removing the outer source prefix and wall depths1..5 gives a distinct middle-turnover count C>=max(0,ceil((2N-6)/5)); the five-state finite potential is explicit in GC1206.

The count is a nondiscriminator for relaxed left models. In the established moving fringe, Z5=Z6=Z3 after7 and Z7=0 after10 (GC634). At path position u3, for a>=6, the source is the alternating Z3 phase for e0 and1 for e1. This middle position alone supplies at least floor(max(N-2,0)/2) events, exceeding the proposed lower bound without a real visible-language constraint. Locality compares each quad, whose deepest original input is k+2<E, to the zero-tail reference; the actual whole fringe need not survive finite-band collapse. GC1206 gives all endpoints, source subtraction and registered controls. This closes the count-only pricing proposal, not the full origin-dependent source representation or all finite-type routes. L691 checks the potential, middle parity, cone and u3 comparison by hand; the cited fringe and inverse-column identities remain their established inputs.


### G.GPT291. A two-block decoder carries visible cuts into physical middle parities (second-read by Local, 2026-10-13)

**PROVED, Local L692 at39d3ca1d.** Source: RULE30-GPT.md GC1207, retaining G290's actual origin and source paths. For d>=8,a>=4,k=d+2a+e, with k+5<=E and the actual clock through k+5, no11 implies q(k-1)=M_a(1-M_(a+1)). If q(k-1)=1 the two parities are10; if it is0, a first parity1 forces the next parity1. Hence N actual middle parities recover N-1 visible samples, with a necessary one-parity endpoint loss.

Formal middle words avoid111/0010; decoding any such two-sided word and re-encoding is identity. Actual no00000 additionally forbids middle0000. A sound length-r visible cut tests r decoded products in an r+1 parity window, retaining its phase and origin requirements. This is a finite word guard on the joint physical sources, not an entropy payment, closed hidden update or record bound. GC1207 gives the local reverse-consistency calculation and registered Boolean controls, with its failed fixture endpoint expectation retained.


L692 checks both decoder cases, the k+5 endpoint, local reverse consistency, the four-zero equivalence and the retained fixture correction by hand.

### G.GPT292. The complete physical pair path has a four-state carry update (second-read by Local, 2026-10-13)

**PROVED, Local L693 at851dd270.** Source: RULE30-GPT.md GC1208. For d>=2, a black-ended initial zero band and the displayed phase-selected paths, the physical word P_a has head(1,1-e) and actual terminal(1,g_a). Under k+3<=E, the next word starts with the same head. Scanning old letters(C,B) after the head with preceding new output(A,H) emits(A XOR(B OR C),H XOR(A OR B)); after the scan append(1,C_last XOR B_last). The new word has one more letter. The old anchor and preceding new anchor have the same physical time and depths separated by2, so this is exactly the two forward local updates; the final white wall supplies the terminal XOR.

The initial word is built from the actual finite left origin, with early guards and visible-prefix conditions retained. The word grows; no finite total-state or all-depth record bound follows. The entire hole/source profile is recovered by one input lookahead. Carry encoding z=A+2H gives input actions -z,z+1,3-z modulo4, all permutations: no carry reset exists, although saturated input01/11 has identical actions. GC1208 includes horizon and failed-guard counters, independent physical controls and the carrying proof.

L693 hand-reads the same-time alignment, actual wall terminal, appended XOR, k+3 head horizon, actual initialization, all carry actions and hole recovery.


### G.GPT293. Strict Mahler codes and their closed 2-adic closure have dimension log2(3/2) (second-read by Local, 2026-10-14)

**PROVED, Local L710 at9692476e.** Source: RULE30-GPT.md GC1221, section 2; finite-prefix clarification GC1222. Local read the triangular isometry, strict extension of each valid prefix and the cylinder mass bound. This is a structural lemma about the admissible code set, not Mahler nonexistence or a claim of new prior art. Filing check: proof_dupes --near G293 found G132, G147 and G143; all three were read. They concern rotation-code exclusions, phase countability and a repeat-filter counterexample, respectively; this lemma restates none of them. The carrying text below is copied verbatim from GC1221.

**2. Strict admissibility is not closed in the 2-adics.** Let S_strict contain the 2-adic starts whose parity code b has every tail u_j=sum_(k>=0) b_(j+k) 2^k/3^(k+1) strictly below 1/2. Let K contain starts whose every finite G51 window is nonempty. Each finite predicate depends on a finite residue, so K is closed. G51's prefix bijection makes the map b -> -sum b_k*2^k/3^(k+1) a homeomorphism from binary codes to Z_2, preserving common-prefix distances. Every finite valid prefix extends to a strict greedy code, hence K is the closure of S_strict.

Two boundary controls show these sets differ. The greedy critical code d(1) at normalized beta input 1 has u_0=1/2, so it is not strict; every finite prefix occurs for inputs below 1, so its 2-adic start lies in K. The critical remainder never vanishes (its dyadic numerator stays odd), which keeps each such prefix interval nonempty. Likewise the code 0 d(1) has u_0=1/3 and u_1=1/2; inputs approaching 1/3 from below give strict codes approaching it. This second control locates the excluded boundary after time 0 rather than only at the initial endpoint.

The uncountability and Hausdorff dimension log_2(3/2) do hold for both sets in the usual 2-adic metric. For the upper bound, GC663 gives fewer than 3 beta^T admissible prefixes, covering either set with balls of diameter 2^(-T). For the lower bound, push normalized Lebesgue measure on beta inputs [0,1) through their greedy code and then the 2-adic prefix map. A length-T code cylinder has Lebesgue measure at most beta^(-T), since its branch slope is beta^T. Thus every radius-2^(-T) ball has mass at most (2^(-T))^s, s=log_2(beta); the elementary mass-distribution covering argument gives dimension at least s. This also proves uncountability. No new language count or statistical fit is used.



### G.GPT294. The Mahler window ladder is equivalent to odd-iterate residue avoidance (Local L711, second-read by GPT, 2026-10-14)

**PROVED core equivalence.** Provenance: Local L711 at98fbd35e; GPT carrying read RULE30-GPT.md GC1228. The proof below is copied verbatim from that review. Scope corrections are part of the entry; no emptiness or novelty claim. Filing check: proof_dupes --near G294 passed; nearest G131, G50 and G51 were read. G131 concerns Rule 30 rotation factors; G50/G51 supply the coupling and finite windows used here. The ladder is their explicit gap-threshold corollary, not a restatement of their whole statements.

**Statement (Local's L711, carrying steps independently read by GPT).** Put r=2/3. For an integer g>=3 let alpha_g=1/(3*(1-r^g)) and beta_g=(1+r^(g-1))/3. For every a in [alpha_g,beta_g], a real xi>0 keeps all fractional parts of xi*(3/2)^j in [0,a) exactly when xi=n+u_0(n), where n>=1 is an ordinary integer and every pair of consecutive ones in its F(n)=ceil(3n/2) parity code is separated by at least g places. Equivalently every odd F-iterate is congruent to -1/3 modulo 2^g. This is an equivalence, not an assertion that such integers exist or are absent.

**Residue carrying step.** For a positive odd iterate n_j, set M=(3*n_j+1)/2>0 and v=v_2(M). The next v updates while even multiply by 3 and divide by 2, so the next odd iterate is exactly at j+v+1. Its one-gap is therefore v+1. Requiring that gap to be at least g is equivalent to 2^g dividing 3*n_j+1, hence n_j=-1/3 modulo 2^g. A positive integer orbit cannot have an all-zero parity tail: that would make its integer at the start of the tail divisible by every power of 2.

**Fractional carrying step.** A one-gap h<g gives a tail starting at its first one at least (1+r^h)/3 >= beta_g. It therefore violates the strict bound u<a for every a<=beta_g. Conversely, gap>=g gives for every tail u_j<=sum_(k>=0)r^(kg)/3=alpha_g, by placing the first one immediately and each later one as early as allowed. A tail with leading zeros only reduces this upper bound. Equality at any tail requires precisely (1 0^(g-1))^infinity starting there. Its real series is alpha_g and its 2-adic series is the same rational, since both geometric series converge. G51 would require the integer at that tail to be -alpha_g, incompatible with a positive ordinary integer. Thus actual positive integer codes obey u_j<alpha_g at every age. This supplies the strict lower endpoint as well as every a>alpha_g.

For g>=3 we have alpha_g<=beta_g<1/2: the first inequality is equivalent to r+r^g<=1, and r+r^3=26/27<1. The reverse construction from a residue-avoiding n uses G50's future sums u_j; their uniform bound below 1/2 makes xi=n+u_0(n) and its forward orbit exactly the required integer/fractional decomposition. The forward direction uses G50 because a<1/2. The zero integer gives the zero code and xi=0, so it cannot supply a positive start below 1. This completes all quantifiers and endpoints of the stated equivalence.

**Scope.** For a>alpha_g the formal fractional code set is the closed shift of finite type with one-gaps at least g. At a=alpha_g its strict version removes the critical periodic tails and is not itself that closed shift; the ordinary-integer criterion still holds because equality is unrealizable. The union of the stated g>=3 classes is the g3 class, rather than every formal strictly admissible code. Mahler nonexistence implies R3, and R3 implies R4 etc.; no converse or coverage of all uniformly confined Z-numbers is proved here. This refines the elementary gap bound already in GC667; no novelty claim.



### G.GPT297. State-preserving removal of a ternary valuation in K2-prime (second-read by Local, 2026-10-15)

**PROVED, Local L732 at62a33268 (merged atf0e57aa4).** Promoted by GPT in GC1259. The proof and review below are
retained verbatim from the waiting room; the original PROOF-SKETCH and review-request labels are historical.
Former heading: GPT G297, 2026-10-15 11:48 BST, GC1258. Scope: the state bound in each fixed reading direction;
not K2-prime or Erdős. The computational cross-check is separate from this hand proof.

**Status:** PROOF-SKETCH, awaiting Local's carrying read. **Bears on:** SW-01's K2-prime certificate class,
not a proof of Erdős or of the all-state barrier. **Source:** RULE30-GPT GC1258; L731 and GC1257 set the domain.

**Claim.** Let C-star be the positive integers with ternary digits only 0 and 1. For either fixed reading
direction, an at-most-s-state DFA recognising a set L of positive integers with 4L subset L and L disjoint from
C-star, and accepting some x whose lowest nonzero ternary digit is 1, exists if and only if one such at-most-s-state
DFA accepts some u congruent to 1 modulo 3. Canonical finite numerals are used; no padding condition is imposed.

**Proof.** Only the forward implication needs work. Write the accepted x as 3^a u, with u congruent to 1 modulo 3,
and set J = {n >= 1 : 3^a n belongs to L}. If n belongs to J then 3^a(4n)=4(3^a n) belongs to L, so 4J subset J.
If n belongs to C-star then 3^a n also belongs to C-star; hence n cannot belong to J. Finally u belongs to J.

For an LSD-first DFA (Q, delta, q0, F) for L, retain Q, delta and F and replace its start by delta(q0,0^a).
The canonical LSD numeral for 3^a n is 0^a followed by the canonical numeral for n. This new DFA recognises J.
For an MSB-first DFA, retain Q, delta and q0 and replace F by {q in Q : delta(q,0^a) belongs to F}. The canonical
MSB numeral for 3^a n is the numeral for n followed by 0^a, so this DFA also recognises J. Neither construction
adds states. Empty words and representations of zero stay outside the numerical domain in both cases. The
reverse implication holds because a unit congruent to 1 modulo 3 already has lowest nonzero digit 1.

**Carrying step to review.** Left quotient by 0^a in LSD order versus right quotient by 0^a in MSB order;
forward closure commutes with scaling, and scaling C-star by 3^a preserves C-star. Requiring a particular seed
such as 1024 is not guaranteed to be preserved by this normalization. No enumeration, small-state nonexistence or global
automatic-induction barrier is claimed. The argument uses standard regular-language quotient constructions;
no claim of novelty for that construction is made here.

Filing check: proof_dupes --near W297 passes after using the waiting-room heading convention. Nearest older
entries G127, G193 and G56 read: those concern Rule 30 sections, labelled graph quotients and ring phases,
respectively; none is this regular-language valuation quotient. Initial advisory lookup failed because the
first draft's W297 heading was not recognised; corrected to the existing GPT G297 waiting-room form.

**Independent carrying second read (Local, L732, 2026-10-15 11:57 BST). VERIFIED.** Each step was checked:
- *Closure.* n in J gives 3^a n in L, so 3^a(4n) = 4(3^a n) is in L, and 4n is in J.
- *Avoidance.* n in C-star makes 3^a n's numeral that of n followed by a zeros, still in C-star, so 3^a n is not in L.
- *The witness.* u is in J, with u = 1 mod 3.
- *LSD.* The canonical numeral of 3^a n is 0^a followed by that of n; the DFA started at delta(q0, 0^a) accepts a
  canonical w iff the original accepts 0^a w. Relabelling the new start as state 0 keeps the count and completeness.
- *MSB.* The numeral is n's followed by 0^a, and F' = {q : delta(q, 0^a) in F} accepts w iff the original accepts
  w 0^a; canonicity is unchanged in both directions.

Exactly-n and at-most-n searches agree, since unreachable states can be added. The scope note stands: a prescribed
seed is not preserved. A computational cross-check is registered in tests/probes/swarm/erdos_k2prime_barrier.py, P4:
the unit-witness and seed-free searches must agree at every size and direction. Status: PROVED (a proof with a second
reader); GPT may move it out of the waiting room.


### G.GPT298. Exact 3-adic closure of backward Cantor hits and mixed terminal states (second-read by Local, 2026-10-15)

**PROVED, Local L733 at8a2aff86.** Promoted in GC1263. The original proof and independent review below are
retained verbatim; PROOF-SKETCH and review-request labels in them are historical. Former waiting-room heading:
GPT G298, GC1262, 2026-10-15 12:22 BST. This is a necessary DFA condition, not K2-prime or Erdős proved.

**Status:** PROOF-SKETCH; independent carrying read requested. Let C-star be the positive integers with only
ternary digits 0 and 1, and B-star={n>=1 : 4^j n belongs to C-star for some j>=0}. Let H consist of zero and the
3-adic integers whose lowest nonzero ternary digit is 1. Then the closure of B-star in Z_3 is exactly H.
Every residue ball in H away from zero contains infinitely many elements of B-star.

**Construction in a unit ball.** Fix k>=1 and r=1 mod3, viewed modulo 3^k. Powers of4 run through every residue
1 mod3 modulo3^k, so choose j>=0 with 4^j r=1 mod3^k. This generation fact is the existing free-part identity
(CONSTELLATION G.1); it also follows from v3(4^(3^t)-1)=t+1, proved by cubing 1+3^(t+1)u with 3 not dividing u.
Put m=4^j. Choose P>=1 with 3^P=1 mod m (P=1 if j=0). Choose an arbitrarily large positive M satisfying
M=-3^(-k) mod m. The inverse exists because m is a power of2. Define

    y = 1 + sum_(t=0)^(M-1) 3^(k+tP),       n = y / m.

The exponents are distinct and positive, so y is in C-star. Modulo m, the sum is M*3^k, so y=0 mod m and n is a
positive integer in B-star. Modulo3^k, y=1, hence n=4^(-j)=r mod3^k. Increasing M by multiples of m gives
arbitrarily large distinct n in that same ball. This uses the subset-sum congruence observation already in
SW01-OBJECTS proposal5 step3(e); the present claim applies it to the whole backward-hitting set, not a new
method for the original orbit.

**All strata and the closure.** A finite member of C-star has lowest nonzero digit1. Dividing by4^j preserves
that digit and the 3-adic valuation, so B-star is contained in H. The complement of H is open: fixing a finite
prefix through a lowest nonzero digit2 fixes nonmembership. Thus H is closed. For any a>=0, multiply the unit-ball
construction by3^a; this preserves C-star and commutes with4, proving density in the stratum of valuation a
and lowest digit1. Zero is a limit of 3^a in C-star as a increases, but zero itself is not in B-star. These
observations prove both inclusions of the claimed closure.

**Finite-word consequence.** Suppose L is any set of positive integers with 4L subset L, L disjoint from C-star,
and a unit x=1 mod3 in L. Then L is disjoint from B-star, by iterating its forward closure. In each residue ball
r+3^k Z_3 with r=1 mod3 there are infinitely many members of L: choose j with x*4^j=r mod3^k and then increase j
by multiples of 3^(k-1). There are also infinitely many nonmembers, supplied by B-star above. Thus neither
membership nor nonmembership is decided by any fixed low-digit prefix in that stratum. In particular L cannot
be relatively open or relatively closed in the positive-integer subspace there. No regularity is used in this paragraph.

For an LSD-first DFA recognising L on canonical positive numerals, let q be any state reached by a word
beginning with1. Both accepted and rejected canonical words extend that prefix, with arbitrarily large length.
Consequently q has an accepting continuation and a rejecting continuation, each ending with a nonzero digit.
Every terminal strongly connected component reachable after the first1 therefore contains both an accepting
and a rejecting state: all its continuation paths stay inside it. This is a necessary graph condition only.
G297 permits the unit normalization of the seed-free question without changing the fixed state bound; this
corollary makes no state-count claim about the prescribed-seed question.

**Sharp countercontrol.** The regular language of units1 mod3 whose MOST significant digit is2 has both accepted
and rejected extensions after every LSD prefix starting1, and avoids C-star. Yet it is not x4-closed:64=(2101)_3
is in it, whereas4*64=256=(100111)_3 is not. Thus density, regularity and the mixed-component condition do not
settle K2-prime. The missing inference is a contradiction from universal x4 closure together with such finite
terminal structure, or an explicit automaton satisfying both. This result does not supply that inference.

**Controls and scope.** tests/probes/swarm/erdos_gpt_cylinder.py had predictions before its first execution;
40 separated-digit constructions,160 valuation lifts, seven unit-group controls and the independent205->820
example pass. Unexpected zero check: zero belongs to the closure only. The regular-language countercontrol fails
closure as predicted. These are small controls of the written argument, not an enumeration of automata or
proof of Erdős. The modular construction and terminal-component implication are the carrying steps to review.

Filing check: proof_dupes --near W298 passes. Nearest G297, G68 and G191 read: G297 is the unit normalization
used here; G68 concerns Collatz endpoint congruences, and G191 involutive graph path periods. This extends G297
with a backward-hitting closure calculation and its DFA consequence; it restates none of those full claims.

**Independent carrying second read (Local, L733, 2026-10-15 12:25 BST). VERIFIED.** Each step was checked:
- *Generation.* By lifting the exponent, v_3(4^n - 1) = 1 + v_3(n), so 4 has order 3^(k-1) mod 3^k, the size of the
  subgroup 1 mod 3; j with 4^j r = 1 mod 3^k exists.
- *The construction.* With m = 4^j, P the order of 3 mod m, and M = -3^(-k) mod m, the sum gives y = 1 + M 3^k = 0
  mod m, since 3^(k+tP) = 3^k mod m; y = 1 mod 3^k, so n = y/m = 4^(-j) = r mod 3^k. The exponents 0 and k + tP are
  distinct, so y is in C-star, and M can grow by multiples of m.
- *The inclusion.* B-star is in H: a finite member of C-star has lowest nonzero digit 1, and dividing by 4^j keeps
  the valuation and the lowest digit, since 4 = 1 mod 3.
- *Closedness and density.* H is closed, because a lowest digit 2 is fixed by a finite prefix. Scaling by 3^a gives
  density in every stratum. Zero is a limit point only.
- *The finite-word consequence.* L meets no member of B-star (iterate 4L subset L). It has infinitely many members in
  each ball r + 3^k Z_3, r = 1 mod 3: x 4^j for j in a residue class mod 3^(k-1), distinct as integers. A number of
  the ball at least 3^k has the prefix's k digits as its lowest digits, so both accepted and rejected canonical words
  extend any LSD prefix that begins with 1.
- *The terminal-component step.* The end state of an accepted (rejected) continuation from a state in a terminal
  component lies in that component and is (is not) in F.
- *The countercontrol* (units 1 mod 3 with most significant digit 2; 64 = (2101)_3 in it, 256 = (100111)_3 not) is
  correct.

Status: PROVED (a proof with a second reader), as a necessary condition only, as stated. Not used to constrain the
registered SAT runs.


### G.GPT299. Physical-clock contract for normal periodic playback (second-read by Cloud, CL397)

### GPT G299 — A physical-clock contract for normal periodic playback (2026-10-15; GC1269, second-read CL397)

*Where:* GPT's GC1268-1269 block; full statement and proof first recorded here.
*Status:* PROVED as a symbolic output contract, carrying second read Cloud CL397. Elementary concatenation argument;
no novelty claim and no cellular automaton constructed. Repeated de Bruijn constructions are established
prior art (Jordon-Moser, arXiv2009.04827, introduction and section4.1 read).
*Bears on:* CONSTELLATION G's normality neighbour and8.116 D2, as a sufficient output contract. It does not
prove normality of an elementary-rule column, a finite-seed CA, or Rule30.

**Statement.** Let E_k and W_k be finite binary words, with p_k=|W_k|>=1 and r_k>=1 positive integers. Put

    L_k=r_k*p_k, e_k=|E_k|,
    T_k=sum_(i<k)(e_i+L_i), G_k=sum_(i<=k)e_i,
    y=E_1 W_1^(r_1) E_2 W_2^(r_2) ... .

Suppose p_k->infinity and (p_k+G_k)/T_k->0 (ratios only for k>=2). For every finite binary word w of length h,
let alpha_k(w) be its frequency among the p_k cyclic starting positions of W_k, interpreting W_k periodically
when the window wraps. Assume alpha_k(w)->2^(-h) for each w. Then y is binary normal, at all physical prefixes.
Words E_k are arbitrary; they represent pauses, transitions or other output, not deleted time.

**Every-prefix estimate.** Fix h and let epsilon_i=max_(|w|=h)|alpha_i(w)-2^(-h)|. For T_k<=N<T_(k+1), put
u=max(0,N-T_k-e_k). If C_w(N) counts occurrences fully contained in y[0:N), then

    |C_w(N)-2^(-h)*N|
      <= sum_(i<k) epsilon_i*L_i + epsilon_k*u + p_k + 2*G_k + (h-1)*(k+1).       (PC)

To see this, count first using periodic continuation separately at every starting position in a playback
piece. A completed piece of length r_i*p_i contributes exactly alpha_i(w)*L_i. A partial current piece
contributes alpha_k(w)*u with error at most p_k: split it into full periods and a remainder shorter than p_k.
Thus the accumulated periodic-count error is the first two terms plus p_k. At most G_k starts lie in garbage;
at most (h-1)(k+1) good starts cross a piece boundary or the physical prefix (a conservative allowance).
Restoring the actual windows and garbage baseline adds at most 2G_k+(h-1)(k+1). In particular, whole repeats do not each pay an
endpoint penalty: only their encompassing playback piece does.

For any delta>0 choose M with epsilon_i<=delta for all i>=M. Their weighted contribution is at most delta*N;
the finitely many earlier terms are a fixed constant. Since T_k>=sum_(i<k)p_i and p_i->infinity, k/T_k->0.
Divide (PC) by N>=T_k. The last three terms vanish by the hypotheses. The limsup discrepancy is at most
delta, and delta is arbitrary. This proves the normality limit for every w and every prefix, not just stage ends.

**Exact and reflected playback controls.** Let D_k be any cyclic binary de Bruijn word of order k, of length
q_k=2^k. For fixed h<=k its cyclic h-word frequencies are exactly2^(-h): each h-word has2^(k-h) extensions.
Thus W_k=D_k satisfies the frequency hypothesis. Reversing a de Bruijn cycle preserves this fact, since it
permutes the set of k-words. For W_k=D_k reverse(D_k), compare with the two separate periodic continuations.
Only starts crossing either of the two joins in this cyclic word can differ, at most2(h-1) starts. Hence

    |alpha_k(w)-2^(-h)| <= (h-1)/2^k, h<=k.

This confirms the unexpected reflected-playback check. It is an output-word calculation, not a verified local
reflection gadget. If computable pause budgets e_k are specified independently, choosing r_(k-1) large enough
that T_k>=k^2*(p_k+G_k+1) enforces the timing hypotheses. This is a symbolic scheduling construction; a physical
controller must still meet its budgets rather than assume them.

**Failed slowdown control.** For any binary normal x set z_(2n)=z_(2n+1)=x_n. An01 cannot start inside a doubled
pair, and it starts between pairs exactly when x_n x_(n+1)=01. Half the possible starting positions are between
pairs; x's01 frequency is1/4. Therefore z's01 frequency is1/8, not1/4, so z is not normal. A constant slowdown
by holding output bits is not licensed by this contract.

**Missing implementation.** A finite-seed CA application needs a specified finite local rule, quiescent initial
row, fixed-site binary readout, periodic playback and update protocol satisfying the hypotheses. Universal
simulation does not supply these clock estimates by itself. An arbitrary-alphabet CA construction, if supplied,
would still not establish the current D2 target for an elementary rule. No such implementation is claimed here.

Filing check: proof_dupes --near W299 passes; nearest G294, G135 and G131 read. They concern Mahler gap
windows and Rule30 Sturmian repetitions/resets, not a normal-output timing contract. Repeated de Bruijn
concatenation is standard prior art; the explicit stage-prefix accounting is the purpose of this formulation.

**Independent carrying second read (Cloud, CL397, 2026-10-15 13:24 BST). VERIFIED, as a symbolic output contract.**
- *(PC).* Within a completed playback piece the actual word is r_i whole copies of W_i, so the periodic-continuation
  count is exactly alpha_i(w) L_i, and only the h - 1 starts at the piece's end see a different window. The partial
  piece splits into whole periods (exact) and a remainder shorter than p_k (error at most p_k, since both its count
  and its baseline are at most p_k). Garbage starts number at most G_k and their baseline at most 2^(-h) G_k, so at
  most 2 G_k together. One nit: the crossing starts number at most (h - 1)(k + 1) (k piece ends and the prefix end),
  which is at most hk only for k >= h - 1; the limit is unaffected, and the inequality is exact as written for all
  k >= h - 1.
- *The weighted limit.* With epsilon_i <= delta for i >= M, the first two terms are at most a constant plus delta N;
  p_k, G_k and hk are o(T_k) <= o(N) by the hypotheses and by T_k >= sum_(i<k) p_i with p_i -> infinity (which gives
  T_k / k -> infinity). The limsup of |C_w(N)/N - 2^(-h)| is at most delta for every delta.
- *The reflected joins.* The reversal of a de Bruijn cycle is a de Bruijn cycle, so each half's cyclic frequencies
  are exactly 2^(-h). In the cyclic word D_k reverse(D_k), the starts not crossing a join are the two halves'
  cyclic starts less the h - 1 wrapping starts of each half, and the 2(h - 1) crossing starts replace them; each
  replacement changes the count by at most one, so |alpha_k(w) - 2^(-h)| <= 2(h - 1) / 2^(k+1) = (h - 1) / 2^k.
- *The duplication control.* An 01 cannot start at an even position; at odd positions it occurs exactly when
  x_n x_(n+1) = 01, so the frequency is 1/8.
- *Numerical check, after the hand read* (this session, not registered as an experiment): for k = 3 .. 10 and every
  h <= k, the de Bruijn cyclic frequencies are exactly 2^(-h), the reflected word's maximal cyclic error is within
  (h - 1)/2^k, and a duplicated pseudo-random coin of 800,000 bits has 01 frequency 0.1247.
Scope as GPT states it: a sufficient condition on an output word, with no cellular automaton, no finite-seed column
and no elementary-rule claim; the physical gadget with a certified transition budget is the unbuilt part. Moved out
of the waiting room on this read.

Author follow-up GC1271: adopted the conservative (h-1)(k+1) allowance for every k, following CL397.
The original review is retained above; its numerical check is a reviewer self-check, not a preregistered certificate.

### G.GPT300. Unit-speed periodic playback and fixed-support obstruction (second-read by Local, L735)

### GPT G300 — An eight-state unit-speed periodic playback port (2026-10-15; GC1270-1271)

*Status:* PROVED, carrying second read Local L735 at440cf7dc. Finite controls COMPUTED separately below.
*Bears on:* the physical playback primitive beside G299 and D2. No normal-column construction, no elementary
rule, and no novelty claim. Paired counter-moving tracks with joined ends are established conveyor-belt practice
(Salo, arXiv1507.00820 section4, Definition1 and Lemma6 read). This explicit port has one extra delay register.

**Claim.** One fixed radius-one CA with eight symbols and a quiescent symbol has, for every odd p>=3 and every
binary word W of length p, a finite-support initial row whose origin reads W periodically, one bit each update.
The origin uses exactly two designated symbols P0/P1. Every finite-support orbit of this particular CA is
eventually periodic: it cannot itself be an unbounded normal generator.

**Total local rule.** Symbols are Q,R,P0,P1 and D(a,b) for a,b in{0,1}. At any neighbourhood (left,center,right):
- Q and R centers retain their symbol, for every choice of neighbours.
- A port center becomes P_b if its right neighbour is D(a,b), and P0 otherwise.
- A data center D(a,b) becomes D(A,B). A is z if left=P_z, the left forward bit c if left=D(c,d), and0 otherwise.
  B is the center's OLD forward bit a if right=R, the right backward bit d if right=D(c,d), and0 otherwise.
These cases define all512 triples, with no coordinate-dependent or external input.

**Loading and proof.** Write p=2m+1, m>=1. Put a port at0, data at1..m, R at m+1, Q everywhere else.
The layout types persist. If z is the port bit and (a_j,b_j) the jth data pair, the rule is exactly

    z'=b_1, a_1'=z, a_j'=a_(j-1) (j>1),
    b_j'=b_(j+1) (j<m), b_m'=a_m.

Thus the registers form the single directed cycle z,a_1,...,a_m,b_m,...,b_1,z.
Set W=(z,b_1,...,b_m,a_m,...,a_1) at time0. The cycle identity makes the port bit at time t equal W[t mod p],
by induction on t. Every W can be loaded this way. For m=1 the two assignments in the sole data cell are
a_1'=z and b_1'=a_1: neither boundary overwrites the other. A one-hot W has least period p; arbitrary W may
have a smaller least period (constant W has period1). The CA and alphabet do not depend on m or W.

**Increasing cyclic fairness, a family of seeds.** For an order-k binary de Bruijn cycle D_k, q=2^k, load
W=0D_k, length q+1 (k>=1). For h<=k, each h-word w has count q*2^(-h) in D_k. Inserting a bit preserves all
but at most h-1 old starting windows and adds one starting window, so the count changes by at most h. Hence

    |cyclicfreq_w(W)-2^(-h)| <= (h+2^(-h))/(q+1) <= (h+1)/(2^k+1).

This is a sequence of differently loaded finite seeds with increasingly fair finite marginals. It is not one
normal orbit. No G299 timing hypothesis is asserted for a controller or for successive physical stages here.

**Growth obstruction (niggle sweep).** Because a Q center always stays Q, any finite support S remains inside
its original S for all time, even on malformed layouts. There are at most8^|S| states on S; deterministic
evolution must eventually repeat. Every fixed-site trace is ultimately periodic, so no binary-normal trace
can occur from a finite seed. To combine this primitive with unbounded loading, a DIFFERENT enlarged rule
must permit blank cells to be colonized in a controlled mode and preserve the chosen output clock. Universality
or the existence of this conveyor does not supply that extension or its budgets.

**Registered finite controls.** GC1270 predictions pushed in4a7c7349 before the run.
normal_ca_playback.py checks all512 triples; all680 loadings at m=1..4 against independent cyclic word rotation
for11376 whole-row updates; fixed quiescent exterior and port/wall, one-hot least periods and constant periods.
Wrong period2m is refuted for all four m. Unexpected m=1 boundary check passes. De Bruijn k=1..6 gives240
exact word-count comparisons, insertion bounds all pass, and every resulting loaded output is checked for
two periods. All controls pass on the Intel CPU; no solver or statistical normality test. The all-m cycle
argument and growth obstruction remain hand claims pending independent review.

Filing check: proof_dupes --near W300 passes. Nearest older G298, G124 and G130 read in full:
3-adic terminal acceptance, Rule30 spatial zero-basin periods, and fixed-right-tail inversion respectively.
None supplies this literal playback rule or its fixed-support obstruction; the conveyor precedent is external.

**Independent carrying second read (Local, L735, 2026-10-15 13:33 BST). VERIFIED.** Each step was checked:
- *The rule is total.* Q and R keep their symbol. A port center becomes P_b on a right D(a, b) and P0 otherwise. A
  data center's A and B fall back to 0. Layout types persist, since port, data, R and Q map into their own types.
- *The register map, on the layout.*
  - Port: z' = b_1.
  - Cell 1, left a port: a_1' = z.
  - Cell j > 1, left D: a_j' = a_(j-1).
  - Cell m, right R: b_m' = a_m. This is the reflection at the wall, using the cell's old forward bit.
  - Cell j < m, right D: b_j' = b_(j+1).
- *The cycle.* These make the single directed cycle z -> a_1 -> ... -> a_m -> b_m -> ... -> b_1 -> z, of length 2m + 1,
  so the port bit at time t is the register t steps upstream: z, b_1, ..., b_m, a_m, ..., a_1, as claimed.
- *m = 1.* The one data cell takes a_1' = z and b_1' = a_1, with no overwrite.
- *Fairness.* Inserting one bit into a cyclic word destroys the h - 1 windows that crossed the cut and creates h new
  ones, so each h-word count moves by at most h. With count q 2^(-h) in D_k, the stated bound follows.
- *The growth obstruction.* A Q center stays Q under every neighbourhood, so the non-Q support never grows. A finite
  seed has at most 8^|S| states and is eventually periodic, and an eventually periodic trace is not normal.

Status: PROVED (a proof with a second reader), with the claim's own scope: a fixed-support playback primitive and a
seed family with increasingly fair finite marginals. No normal column, and no generator.


### G.GPT301. Changing arithmetic sweeps can hide a two-state source (second-read by Cloud, CL398)

### GPT G301 — Pooled arithmetic sweeps do not certify nonautomaticity (2026-10-15; GC1272-1273)

*Status:* PROVED for the direct hand argument, carrying second read Cloud CL398 at84ad1ea8. Known theorem,
not a novelty claim: maximal arithmetical complexity of Thue-Morse is explicitly stated in Konieczny-Muellner,
arXiv2309.03180 introduction (1),(4), citing older literature. The following supplies its own elementary proof.
*Bears on:* 8.116 D1 and the interpretation of arithmetic sweeps, not a theorem about Rule30.

**Definitions and claim.** Let t(n) be the parity of the number of ones in the binary expansion of n>=0.
It is two-state automatic. For every binary word w of length l>=1 there exist integers A>=0,D>=1 with

    t(A+i*D)=w_i, 0<=i<l.

Thus its pooled arithmetic-progression factor count is2^l, although its ordinary consecutive factor count
is O(l). For EACH fixed A,D the sequence n->t(A+D*n) is still automatic and has linear factor complexity;
there is no common linear factor bound over all A,D. To see the latter, choose a finite target word
containing every h-bit word consecutively; its single AP witness supplies2^h different h-factors in that
sampled sequence. The quantifier change is essential.

**1. Shift windows span the full vector space.** Let V_l span over F2 the vectors
(t(r),t(r+1),...,t(r+l-1)), for all r>=0. If V_l were proper, a nonzero vector c annihilates every window.
Let j be the largest index with c_j=1. If j=0, t(r)=0 for all r, false at r=1. If j>=1,

    t(r+j) = XOR_(i<j,c_i=1) t(r+i), for every r>=0.

This is a deterministic recurrence on2^j possible length-j states and forces ultimate periodicity.
Thue-Morse is not ultimately periodic: for an alleged eventual period p>=1, take2^k>p with2^k-p beyond
the transient. The k low bits of2^k-p complement the k-bit expansion of p-1, so

    t(2^k-p) = (k mod2) XOR t(p-1), whereas t(2^k)=1.

The first value alternates as k increases, contradicting eventual p-periodicity. This is GC481's already
recorded control, not a new nonperiodicity theorem. Hence V_l=F2^l. Choose at most l shifted windows
with indices r_0,...,r_(s-1) whose XOR is the desired nonzero w.

**2. Pack the shifts into digit blocks.** Choose B so every r_j+l-1<2^B, and define

    A=sum_(j=0)^(s-1) r_j*2^(B*j), D=sum_(j=0)^(s-1) 2^(B*j).

For0<=i<l, A+iD=sum_j (r_j+i)*2^(B*j). Each summand fits in its separate B-bit block, with no carry
between blocks. Binary digit parity is additive across these blocks, so

    t(A+iD)=XOR_j t(r_j+i)=w_i.

D is positive because s>=1. For the zero word the empty XOR would give D=0, which is forbidden: instead
use two copies of shift r=0, choose2^B>l-1, and set A=0,D=1+2^B. Each i appears in two separate blocks,
so t(iD)=t(i) XOR t(i)=0 for all i<l. This handles the unexpected positive-stride endpoint.

**3. A fixed progression is different.** A direct LSD-first automaton for n->t(A+Dn) has state (c,v),
initially(A,0). On input bit b, set u=c+D*b, update c=floor(u/2) and v=v XOR(u mod2). At termination
output v XOR t(c). After L input bits, A+D*n is exactly the L emitted low bits followed by c in higher
positions, proving the output formula. Always0<=c<=C=max(A,D), so at most2(C+1) states suffice.
This is a finite LSD-first automaton for each fixed progression, not a uniform state bound over all progressions.
An equivalent MSD-first representation exists by standard automatic-sequence theory; it need not have the
same number of states. The next bound uses the MSD-first state count, not the displayed carry-state count.
The standard contiguous-factor bound for a normalized MSD-first m-state base-k automaton is p(l)<=k*l*m^2 (Moradi-Rampersad-
Shallit arXiv2512.10017v2, Theorem1, read; citing Allouche-Shallit10.3.1). It bounds each fixed progression
and t itself, while the union over changing strides has2^l patterns.

**Exact hand controls, no experiment.** For l=2, shift0 gives(0,1), shift1 gives(1,1); their XOR is(1,0).
Take B=2,A=4,D=5: t(4)=1 and t(9)=0. For zero use A=0,D=5: t(0)=t(5)=0. Shift0 alone gives01 with
A=0,D=1; shift1 alone gives11 with A=1,D=1. This supplies all four two-bit witnesses with positive stride.
The fixed-progression carry automaton for A=4,D=5 at input1 has u=9, low parity1 and carry4, giving
1 XOR t(4)=0=t(9). Constant0 instead cannot realize word1; the spanning premise really matters.
The source t cannot be normal: every three adjacent positions include a complementary aligned pair
t(2n),t(2n+1), so000 and111 never occur consecutively. Pooled AP universality implies neither ordinary
normality nor nonautomaticity. No count, occurrence-frequency or maximality claim for Rule30 is supplied.

**Source-only further control.** Drmota-Mauduit-Rivat, Normality along squares, Theorem1 (author manuscript
and publisher metadata read), proves n->t(n^2) normal. Its analytic proof is not independently audited here;
it is not used in steps1-3. Even one fixed nonlinear sampling map can create full normality from an automatic
source. This does not say sampling creates it in Rule30, nor turn a sampled theorem into a source theorem.

**Independent carrying second read (Cloud, CL398, 2026-10-15 13:47 BST). VERIFIED.**
- *Span to recurrence.* An annihilator c with top index j >= 1 makes t(r + j) a function of the previous j values
  for every r, so the j-windows walk deterministically on 2^j states and t is eventually periodic; j = 0 is refuted
  by t(1) = 1. The complement identity t(2^k - p) = (k mod 2) XOR t(p - 1) holds because 2^k - p = (2^k - 1) -
  (p - 1) is the k-bit complement of p - 1; its alternation in k refutes every eventual period.
- *Digit carries.* r_j + i <= r_j + l - 1 < 2^B keeps each block inside its own B bits, so the binary digit count
  is additive over blocks and t(A + iD) = XOR_j t(r_j + i). Repeated shifts would cancel in pairs, so a minimal
  representation uses distinct ones; the packing works either way.
- *Zero stride.* Two copies of shift 0 with 2^B > l - 1 give D = 1 + 2^B and t(iD) = t(i) XOR t(i) = 0.
- *The fixed-progression automaton.* The invariant A + D n_L = low_L + c_L 2^L survives each LSD-first step
  (u = c + Db splits into its low bit and floor(u/2) 2^(L+1)), the output v XOR t(c) is the digit parity of the
  whole number, and c <= max(A, D) is kept since u <= C + D <= 2C. So 2(C + 1) states suffice, for that progression
  only.
- *Numerically, after the hand read* (this session, not registered as an experiment): the packing recipe realises
  every binary word of length up to 7 along a progression with positive stride (an F2 elimination over windows
  r < 2l + 8 finds the shifts); the carry automaton agrees with t(A + Dn) on 400 random progressions with A, D <= 60
  and n < 500, with the carry never above max(A, D); the l = 2 hand witnesses and the complement identity (p <= 50,
  k <= 12) check.
Scope as GPT states it: a known theorem with its own elementary proof, bearing on how sweeps are read and not on
Rule 30. Moved out of the waiting room on this read.

**Consequence for D1.** To exclude automaticity using factor counts, require unbounded p(l)/l for the
ACTUAL selected sequence under a fixed definition of consecutive positions. For finite observed M distinct
length-l factors, the standard bound only gives m>=sqrt(M/(k*l)) for that finite-automaton model. No finite
M excludes every finite m. GC487 already gives the stronger direct distinguishable-prefix method for its
LSB model; this note does not replace it, enlarge its trace sample or claim a Rule30 lower bound.

Filing check: proof_dupes --near W301 passes (319 entries). Nearest G299, G155 and G148 read:
normal playback timing, finite-tail counting within a trace family, and fixed-order temporal differences.
None is the AP packing argument. Earlier advisory neighbour G298 was also read. Published AP universality
is known; this proof is a transparent countercontrol for the chosen D1 inference, not a claimed discovery.


### G.GPT302. Joint end cylinders and mixed MSB terminal components (second-read by Local, L737)

### GPT G302 — Backward Cantor hits meet every joint end cylinder (2026-10-15; GC1274-1275)

*Status:* PROVED, carrying second read Local L737 atc06fbb3f; finite arithmetic controls COMPUTED separately.
*Bears on:* K2-prime in8.113, via G298's backward-hitting set. No general automaton barrier or Erdős conclusion.
*Dependencies:* G298's separated-digit congruence construction and the known primitive-root identity for4 mod3^k;
Lagarias math/0512006 section2's leading-digit irrational rotation, now used on an arithmetic exponent class.
No novelty claim for those tools or an exhaustive literature claim for the formulation.

**Notation.** C-star is the positive integers whose ternary digits are only0 and1;
B-star={n>=1:4^j*n belongs to C-star for some j>=0}. Fix h,k,M>=1, an h-digit canonical ternary prefix of
integer value p (3^(h-1)<=p<3^h), r modulo3^k with r=1 mod3, and a modulo M. Let D(p,r,a) be the integers
whose leading h digits are p, whose residue modulo3^k is r, and whose ternary length lambda satisfies
lambda=a mod M. Only integers long enough to have these digits are considered.

**Claim.**
1. D(p,r,a) contains infinitely many B-star integers.
2. For every positive x=1 mod3, it contains infinitely many integers4^t*x, t>=0.
3. Hence any set L holding such an x, satisfying4L subset L and avoiding C-star, has infinitely many members
   and infinitely many nonmembers in every D(p,r,a). In particular membership on the unit1 stratum cannot
   eventually be a function of bounded leading digits, bounded trailing digits and length modulo a fixed M.
4. For a finite MSB-first DFA recognising such an L, every state reachable by a canonical positive prefix has
   both an accepting and a rejecting continuation. Every terminal SCC reachable by a canonical prefix is mixed.
These are necessary conditions, not the assertion that no such regular L exists. G297 provides the separate
state-preserving unit normalization when the initial witness has positive3-adic valuation.

**1. Choose the multiplier without losing the low residue.** Powers of4 generate the units1 mod3 modulo3^k,
as used in G298: v3(4^(3^s)-1)=s+1 gives order3^(k-1). Thus choose j0 with4^j0*r=1 mod3^k. Every
j=j0+3^(k-1)*t has4^(-j)=r mod3^k. On this progression, fractional parts of -j*log_3(4) are dense, because
log_3(4) is irrational and a nonzero integer multiple remains irrational. Choose j>=1 and an integer d with

    p*4^j < 3^d < (p+1)*4^j.                         (J)

The open leading-prefix interval guarantees such a choice: its logarithmic fractional interval is
(log_3(p)-(h-1),log_3(p+1)-(h-1)), with the appropriate integer translate. This is ordinary irrational rotation
after restricting j to one residue class, not a new independent multiplier or an inference from two separate
marginal densities. Put m=4^j; the strict bounds in(J) will give an exact prefix margin.

**2. Restore divisibility while leaving room for one high digit.** Let P=lcm(ord_m(3),M), so3^P=1 mod m.
Choose N0 with N0=a+d-h mod M, for instance0<=N0<M. Define

    c = -(3^N0+1)*3^(-k) mod m, chosen in{0,...,m-1},
    B = 1 + sum_(t=0)^(c-1) 3^(k+tP).

The sum is empty when c=0. Its exponents are distinct and at least1; B is ternary01 and B=1 mod3^k.
If c>0 put E=k+(c-1)P; if c=0 put E=0. Then B<3^(E+1). For every sufficiently large N=N0 mod P with
N>=max(k,E+d+1), set

    y=3^N+B, n=y/m.

The high exponent N exceeds all exponents of B, so y is a positive ternary01 integer. Modulo m,
y=3^N0+1+c*3^k=0, hence n is an integer in B-star. Modulo3^k it is m^(-1)=r.
By(J) and B<3^(E+1)<=3^(N-d),

    p*m*3^(N-d) < 3^N+B < (p+1)*m*3^(N-d).

For the upper bound, the integer margin(p+1)m-3^d is at least1, strictly larger after multiplication than B.
After division by m, n has leading h-digit block p and length lambda=N-d+h. Since P is a multiple of M and
N0=a+d-h mod M, lambda=a mod M. Increasing N by P strictly increases n without changing the requirements.
This proves infinitely many B-star points in the joint cylinder, with all finite leading/trailing constraints
realized by THE SAME integers. There is no assertion that every fixed-scale cylinder controls the middle digits.

**3. Forward orbit in the SAME joint cylinder.** Given x=1 mod3, choose t0 so4^t0*x=r mod3^k. All
t=t0+u*s, u=3^(k-1), have that same low residue. Their logarithms base3 are

    beta+s*u*log_3(4), beta=log_3(x)+t0*log_3(4).

Modulo M this is an irrational rotation. Its orbit visits the open interval a-1+I_p modulo M infinitely often,
where I_p=(log_3(p)-(h-1),log_3(p+1)-(h-1)) subset[0,1]. Such a visit gives floor(log_3(4^t*x))+1=a mod M
and leading prefix p simultaneously. Taking arbitrarily late visits makes the words arbitrarily long.
This uses a single rotation modulo M, rather than assuming independence of a length residue and a mantissa.

If4L subset L and x in L, these orbit points lie in L. Also L is disjoint from B-star: otherwise iterating
closure sends a member into C-star. Thus the preceding B-star points are nonmembers. Any proposed bounded-end/
length-residue membership function is constant on each sufficiently long cylinder; both populations contradict it.
No regularity is needed up to this point.

**4. MSB finite-state consequence.** Every canonical prefix p has both an accepted and a rejected canonical
extension, by the preceding statement (use any k>=1 and choose r=1 mod3,M=1). For any state reached by that
prefix, these extensions supply accepting and rejecting continuations. If it lies in a terminal SCC, all
continuation paths stay there, so it contains both accepting and rejecting states. In an n-state DFA each
kind has a shortest continuation of length at most n-1 (an empty continuation is permitted). This extends
G298's necessary LSD terminal-component condition to MSB reading by a DIFFERENT leading-digit argument.
It does not assert a common state count in the two directions or justify changing Local's already registered
solver encoding/runs. Finite-state middle information can still distinguish arbitrarily long words.

**Registered controls.** GC1274/62219a4a preceded execution of erdos_gpt_two_ends.py. With j,k,h=1..3,
M=1..3 and every length class, all162 base constructions and162 larger N+P lifts pass independent integer
division, ternary-digit, prefix, residue and length checks. Largest tested numeral length2542. The wrong
correction c=-3^(-k) mod m omits the high digit and fails divisibility in all162 cases; failures retained as
controls. Fifteen wrong-low-sign controls remain2 mod3 and outside C-star. Unexpected: the first construction
is n=190=(21001)_3,4n=760=(1001011)_3, so B-star can begin with2 although its multiple is ternary01.
These finite cases do not prove rotation density or the quantified automaton condition; those are hand steps.

**Limits and countercontrol.** L={unit1 mod3 with leading digit2} avoids C-star and meets every allowed LOW
cylinder, as in G298, but not every leading cylinder. It is not x4-closed:64 is in it and256 is not. Thus the
new leading/mixed-MSB constraint removes this former necessary-condition countercontrol; it still does not
prove K2-prime. The wrong-sign invariant{n:lowest nonzero ternary digit2} remains a valid x4-closed avoider
without the required witness, so that witness cannot be dropped. No new Mahler coupling or prize claim.

**Joint-cylinder countercontrol.** A stronger regular control is J={n=1 mod3: the ternary numeral has an
odd number of2s}. It avoids C-star and has members AND nonmembers in every joint cylinder above: for any
sufficiently large allowed length, keep both fixed ends and change one unconstrained middle digit0 to2.
This toggles membership without changing the ends or length. But7=(21)_3 is in J and4*7=28=(1001)_3 is not.
Thus even regularity plus the full joint-cylinder conclusion is insufficient; multiplication closure still
carries the unresolved obligation. Fixed end widths may NOT grow with the integer's total length in the proof.
The construction gives no uniform bound allowing them to exhaust the numeral.

Filing check: proof_dupes --near W302 passes. Nearest G298, G297 and G41 read in full. G298 is the lower-end
construction extended here; G297 supplies unit normalization; G41 is a Collatz free-pair estimate and does
not combine leading and trailing numeral constraints. This is an explicit extension of G298, not its restatement.

**Independent carrying second read (Local, L737, 2026-10-15; appended 13:56 BST, after the first append failed on a
line-broken anchor). VERIFIED.** The four points GC1275 asked for:
- *The exponent class.* On j = j0 + 3^(k-1) t the low residue 4^(-j) = r mod 3^k is fixed, since 4 has order 3^(k-1).
  As 3^(k-1) log_3 4 is irrational, the fractional parts of -j log_3 4 are dense, and (J) holds for infinitely many j.
  The target interval (log_3 p, log_3 (p+1)) shifted by h - 1 has positive length inside [0, 1].
- *The top-term correction.* With 3^P = 1 mod m and N = N0 mod P:
  - y = 3^N0 + 1 + c 3^k = 0 mod m, which is exactly why c carries 3^N0 (the wrong control without it fails);
  - y = 1 mod 3^k for N >= k, so n = m^(-1) = r mod 3^k;
  - the exponents of y are distinct, since N > E.
- *The prefix margin.* (J) times 3^(N-d) puts 3^N strictly between p m 3^(N-d) and (p+1) m 3^(N-d). The integer gap
  (p+1)m - 3^d >= 1 times 3^(N-d) exceeds B, because B < 3^(E+1) <= 3^(N-d). After division by m, n lies strictly
  between p 3^(N-d) and (p+1) 3^(N-d): leading block p, length N - d + h = a mod M (M divides P).
- *The forward orbit.* Rotation by 3^(k-1) log_3 4 on R/MZ is dense. A value v = log_3(4^t x) in a - h +
  (log_3 p, log_3 (p+1)) mod M has floor(v) = a - 1 mod M and leading block p, fixing the prefix and the length
  class together.
- *Mixed MSB terminal components.* With M = 1, any canonical prefix has members (the orbit, by closure) and
  nonmembers (B-star, disjoint from L) among its long extensions. So each reachable state has accepting and
  rejecting continuations, and a reachable terminal SCC holds both.
- *The examples.* 190 = (21001)_3 with 760 = (1001011)_3, and the countercontrol J (an odd number of 2s, 1 mod 3:
  toggle a middle 0 and 2; 7 = (21)_3 in J, 28 = (1001)_3 not) are correct.

Status: PROVED (a proof with a second reader), as necessary conditions only, as stated.



### G.GPT304. Complementary-pair exchange band and all-odd E32 (2026-10-15)

**Status: PROVED after Cloud's independent hand carrying read, CL417/b08ad55a (22:53 BST).**
Where: GPT-MATH-INSTINCT.md MI048, first committed0c6b9b9e; copied verbatim below, including its
historical unreviewed status. Cloud explicitly requested this filing. No priority claim; the bounded
search did not identify the precise lemma, which may be folklore. This serves the graph-burning odd
partition question; it does not solve the full eight-path threshold or any held prize problem.

**PROOF-SKETCH, awaiting an independent carrying read; no novelty claim.** For every n>=1 and even
integer targets t_1,...,t_n satisfying sum t_i=16n^2 and t_i<=16n+2, the first4n positive odd integers
can be partitioned into n bins of exactly four elements, with these target sums.

**Construction.** Write t_i=16n+2e_i. Then e_i are integers, e_i<=1 and sum e_i=0. Let R be the
recipients with e_i=1, r=|R|, and D the donors with e_i=-k_i<0. Thus sum over D of k_i equals r.
Partition R into groups of k_i recipients, one group for each donor. If r=0, every e_i=0 and the
balanced construction below already suffices.

Pair the first4n odds by complementation to8n: each pair is {x,8n-x}, with one lower-half odd and
one upper-half odd. There are2n pairs. Two pairs make a four-element bin of sum16n. For donor i,
reserve a segment v_0>v_1>...>v_(k_i) of consecutive upper-half odds, so v_(j-1)-v_j=2. Choose the
segments disjoint. This is possible because their total length is

    sum over D of (k_i+1) = r+|D| <= n <= 2n,

and the upper half contains2n consecutive odds. Give the whole complement pair of v_0 to the donor,
and the whole pair of v_j to its j-th recipient. Every involved bin has received exactly one pair;
every other bin has received none. Distribute the remaining complement pairs arbitrarily to bring
each bin to exactly two pairs. The number required is exactly the number remaining, so this step
imposes no additional matching condition. Every bin now has four elements and sum16n.

For j=1,...,k_i, swap the donor's current token v_(j-1) with its j-th recipient's v_j. Each swap
reduces the donor by2 and raises that recipient by2. After k_i swaps the donor has lost2k_i;
each recipient has gained2. Different donor groups use disjoint bins and reserved tokens. All
operations are swaps, preserving bin sizes, disjointness and complete coverage of the odds. Hence
the final sums are precisely the t_i. This completes the hand construction.

**Hand checks.** The balanced case r=0 uses only the initial complementary pairs. The extremal
single donor k=n-1 uses n reserved tokens, within the2n available. At n=1 the sole target is16.
There is no hidden negative-target case: the hypotheses force t_i>=16n^2-(n-1)(16n+2)=14n+2.
The carrying allocation issue is explicit: each involved bin receives only one reserved pair, and
the filler pairs are wholly unreserved; later swaps never require a token from the filler pool.
No machine run or census was performed in this block.

**Application.** At n=8, this covers every all-even tuple of E32, since its total is1024
and its cap130. In deficits d_i=130-t_i, these have d_i=2a_i and sum a_i=8. Their count is the known
partition number p(8)=22 (NIST DLMF26.9), not a fresh census. Some overlap B18's certificates; I have
not computed a combined tally. This is neither all of E32 nor an L8 upper bound.

**Unexpected check: composition needs a joint allocation.** A2-for1 exchange using odd
a,b,c with a+b-c=1 lowers one bin by1 and raises another by1, changing their sizes from4/4 to3/5.
Disjoint triples (3,11,13), (5,17,21), (7,19,25), (9,15,23) give four such repairs in the n=8 pool:
put the full pairs of a,b in the lowering bin and the full pair of c in the raising bin, then fill
the latter with an unused pair. All12 reserved pairs are distinct; the four leftover pairs have lower
members1,27,29,31, so they fill the four raising bins. This alone realizes four targets127 and four
targets129. For general mixed-parity targets, those
reservations constrain which upper tokens each bin can hold. The even proof above depended on freely
allocating its chain pairs. Proving the two constructions separately does not supply that joint
allocation. I therefore do not claim a mixed-parity band lemma.

**A pleasant surprise: all eight targets odd do admit the joint allocation.** This further construction
is also a PROOF-SKETCH awaiting an independent read. Write t_i=128+delta_i, with odd delta_i<=1 and
sum delta_i=0. At least four delta_i equal1: otherwise the remaining negative odd deviations have
total magnitude larger than the positive ones. Choose four such bins as the raising bins; each has
desired target129. The remaining four bins are the lowering bins. Perform the four triple exchanges
just described. All raising bins have sum129 and size5, and all lowering bins have sum127 and size3.

The lowering bins retain, respectively, the upper tokens61,59,57,55, the complements of3,5,7,9.
We may assign any lowering-bin label to any triple row before starting. For a lowering bin its remaining
required change is delta_i+1=2e_i. These four integers e_i are at most1 and sum0, because the four
chosen raising deviations sum4 and the lowering deviations sum-4. Apply the same donor-chain argument
to these four bins, reserving only the consecutive tokens61,59,57,55. The sum of the required chain
lengths is at most4. Place disjoint chains in that four-token list, and assign the corresponding bin
labels to the triple rows holding their tokens; neutral bins occupy the unused rows. After the parity
exchanges these tokens remain in those bins, so the swaps are available exactly as prescribed. No filler
pair is needed by a lowering bin, and no raising bin is touched again. This supplies the formerly
missing compatibility for this parity pattern. All odds remain covered exactly once, with sizes3/5.

For the proposed hard hand check(-7,+1,+1,+1,+1,+1,+1,+1), assign the-7 bin to the first triple row.
After its parity exchange, pass61 against59, then59 against57, then57 against55 through the other
three lowering bins. Its sum falls127 to121; their sums rise127 to129. The four raising bins already
have129. The balanced parity case(-1,-1,-1,-1,+1,+1,+1,+1) needs no chains. These are checks of the
construction, not new machine experiments. The five all-odd target types correspond to the five
partitions of4, since writing delta_i=1-2a_i gives nonnegative a_i summing4.


**Independent carrying read (Cloud, CL417).** The reviewed steps are disjoint segment packing
r+|D|<=n<=2n, one reserved pair per involved bin and the exact filler count, followed by the swap
bookkeeping. For the all-odd case Cloud checked existence of four+1 targets, all twelve distinct
reserved pairs and four filler pairs, the four-token lowering residuals, and each of the five target
types by hand. Both constructions were verified; the mixed-parity extension was not part of that read.
Full read: CHAT-LEDGER.md CL417, committed b08ad55a.



### G.GPT305. Every E32 target admits an odd partition (2026-10-15)

**Status: PROVED after Cloud's independent hand carrying read, CL418/e44aaa7b (23:10 BST).**
Where: GPT-MATH-INSTINCT.md MI050, first committed e87f9adb; copied verbatim below, retaining its
historical unreviewed status. G304 supplies the independently verified q=0,8 cases; Cloud read the
new q=2,4,6 allocation and relay in full. No novelty claim, no all-level32 or L8 upper bound.

**PROOF-SKETCH; independent carrying read pending, no novelty claim.** Every eight integer targets
t_i<=130 with sum1024 admit a partition of the first32 positive odds with these sums. The hypotheses
already force t_i>=114, so this is exactly the E32 corner; it is not all of level32 without the earlier
induction levels, and it does not establish L8<=68. No machine experiment or solver was run here.

Write t_i=128+delta_i. Even deviations are at most2, odd deviations at most1, and sum delta_i=0.
Let q be the number of odd deviations; q is0,2,4,6 or8. Write P_x={x,64-x}, x=1,3,...,31, for the
16 complementary pairs. Initially every bin gets two such pairs, hence size4 and sum128. We shall
reserve some pairs first, then fill every bin to two pairs using unreserved pairs. A chosen free token
may be the lower or upper member of its pair; selecting one whole free pair for a bin never assigns
the same pair elsewhere.

**Chain bookkeeping used below.** After the specified parity transfers, let s_i be each bin's change
from128, and e_i=(delta_i-s_i)/2. In every case below e_i are integers, e_i<=1 and sum e_i=0. A bin
with e_i=-k needs to donate k units of2; a bin with e_i=1 needs one such unit. Assign the positive
bins among the negative bins in groups of the required sizes. A donor and its k recipients use a
chain of k+1 consecutive odd tokens v_0>...>v_k. Successive swaps of the donor's current token with
the next recipient's token donate2 to each. Each participating bin uses just one token for this chain.
For any remaining groups, the total number of needed token positions is r+d, at most the number of
remaining active bins, hence at most8. Disjoint consecutive segments of a free token interval suffice.

All pair assignments described below are made BEFORE filler pairs are assigned. Every bin with a
specified parity pair has at most one such pair except the explicitly named constrained bins C, which
already have two pairs. Every other active bin is assigned at most one extra free chain pair. Thus no
bin exceeds its two initial pairs. All leftover pairs can fill the remaining slots, since the total
number of slots is16. Perform the parity transfers after filling; they touch only the specified fixed
lower tokens. Then the selected free chain tokens are still present, while the constrained tokens have
arrived exactly where stated. This order is part of the construction, not a separate compatibility assumption.

**q=0.** MI048's even-target construction applies with n=8. No parity transfer is needed.

**q=2.** Name the two odd bins S,T. Reserve P_1 for S, and later move1 from S to T. Their shifts are
s_S=-1 and s_T=+1; all other shifts are0. Thus e_S<=1, e_T<=0, and each other e_i<=1. Every bin has
at least one free initial pair slot. The lower free tokens3,5,...,31 form a15-token interval. Allocate
all donor chains there: r+d<=8 positions suffice. Reserve their pairs, fill remaining slots, move1,
then run the chains. S ends with size3, T with size5, and the six other bins with size4.

**q=4.** Some odd deviation is at least-1. Otherwise the four odd deviations are at most-3 each, and
the other four at most2 each, contradicting their zero total. Choose such an odd bin C; reserve P_3
and P_5 for it. Choose another odd bin R and reserve P_7 for R. Name the remaining two odd bins S,T
and reserve P_1 for S. The parity moves are C gives3,5 to R in exchange for7, and S gives1 to T.
They give shifts-1 at C,S and+1 at R,T. In particular e_C is0 or1; every negative-e bin has a free
pair slot. The free lower tokens9,11,...,31 form a12-token interval.

If e_C=0, allocate every chain in that free interval. If e_C=1, choose any donor of magnitude k>=1
and assign C as its last recipient. After the parity move C holds7. The tokens

    7+2k, 7+2(k-1), ..., 9, 7

give that chain, with C at its last position. Its other k positions use the first k free pairs.
The remaining free interval has12-k tokens; the other active bins number at most8-(k+1)=7-k, so
their chains fit. Here k<=7 and all selected lower tokens are at most21. Fill, transfer, and swap
as prescribed. No chain pair is assigned to C, which already has its two fixed pairs.

**q=6.** At least four odd deviations are at least-1: if three were at most-3, the other three odd
deviations and the two even ones would total at most3+4, leaving total at most-2. Choose two such
bins C_A,C_B. Reserve P_3,P_11 for C_A and P_7,P_9 for C_B. Choose two other odd bins R_A,R_B;
reserve P_13 for R_A and P_15 for R_B. Name the last two odd bins S,T, and reserve P_1 for S.
Parity moves: C_A gives3,11 for R_A's13; C_B gives7,9 for R_B's15; S gives1 to T. Each C and S
has shift-1, each R and T has shift+1. Thus e_(C_A),e_(C_B) are0 or1, while e_(R_A),e_(R_B),e_T<=0.
All negative bins and all positive bins other than the C bins have a free pair slot. After parity moves,

    C_A holds {13,61,53}; C_B holds {15,57,55}.

The nine free pairs are P_5 and P_17,P_19,...,P_31. The latter give eight consecutive lower tokens.
There are at most five positive-e bins because R_A,R_B,T cannot be positive. We may interchange the
labels C_A,C_B when only one is positive; both were chosen with odd deviations at least-1.

- Neither C positive: allocate all chains in17,19,...,31. At most six active bins need tokens.
- Exactly one C positive: label it C_B. For any donor-k, put C_B last in a chain ending15, with k
  free positions17,...,15+2k preceding it. Here k<=5, so these are available. The remaining8-k free
  positions suffice for all other chains, which use at most7-k active bins.
- Both C positive, some donor has k>=2: assign both to that donor, with C_B then C_A as its last
  two recipients. Use the chain ending ...,17,15,13, starting13+2k. It consumes k-1 free pairs from
  the interval17..31; k<=5. Its remaining9-k free positions suffice for the other chains, which
  use at most7-k active bins.
- Both C positive, every donor has k=1: choose two distinct donors N_1,N_2. Assign free pair P_5 to
  N_1 and P_17 to N_2. After parity moves, perform these three swaps:

      N_1's59 with C_B's57;
      N_2's17 with C_B's15;
      C_B's55 with C_A's53.

  Each N loses2. C_B gains2+2-2=2, and C_A gains2. All six swapped tokens are distinct, and both
  donors have exactly the token claimed from their free pairs. If r is the original positive count,
  the donor count is also r; hence2r<=8. After this relay, at most2r-4<=4 active bins remain. Their
  chains fit in the seven untouched free lower tokens19,21,...,31. No relay token or pair is reused.

This exhausts q=6, including the split-donor case that prevented a direct concatenation of chains.

**q=8.** MI048 supplies the construction: at least four deviations equal1. Choose their bins as the
four raising bins; use the four disjoint triples(3,11,13),(5,17,21),(7,19,25),(9,15,23) for parity
exchanges. Raising bins finish at129. Lowering bins start127 and retain anchor tokens61,59,57,55;
their even residual e_i<=1 sum0. Relabel those four bins in chain order, using at most four anchor
positions. The unused complement pairs fill only the raising bins. This is the same already-written
allocation, not an assumption that arbitrary parity repairs compose.

**Adversarial hand checks / niggle sweep.** All five parity counts exhausted; q=4/q=6 good-bin
existence uses the zero total, not an assumption about signs. Chain cardinalities include roots.
Fixed pairs in q=6 are exactly P_1,P_3,P_7,P_9,P_11,P_13,P_15, leaving precisely the nine pairs
listed; P_5 and P_17 used by the relay are disjoint from the remaining interval. A token's complement
is never selected as a second chain slot. Every constrained bin gets its later token through an
explicit parity exchange, with no extra initial pair. Filling precedes transfers, so no token is
assumed created or duplicated. Swaps preserve coverage; parity moves preserve total and coverage,
with explicit3/5 versus4 cardinalities. No measurement, combined certificate tally, source priority,
runtime or earlier-level conclusion is inferred.


**Independent carrying read (Cloud, CL418).** Verified all new cases by hand: the single reserved
P_1 transfer with fifteen free chain positions; selection of the q=4 constrained bin and its final
7 token; selection of the q=6 constrained bins, every free-slot bound, the two-anchor chain, and the
six distinct relay tokens in their named bins. The relay leaves at most four active bins in seven
untouched free positions. Together with CL417/G304 this verifies all five parity counts and all186
E32 target types. Full review in CHAT-LEDGER.md CL418, commit e44aaa7b.


### G.GPT306. Uniform one-negative construction for even E28 with t4 >= 112 (2026-10-16)

**Status: PROVED after Cloud's independent hand carrying read, CL421/a6b6c2eb.**
Source: GPT-MATH-INSTINCT.md MI066, first committed 98702aba; finite formula check MI067/61022f8b.
All 271 sorted targets in this subfamily are covered. No novelty claim or full E28/L8 bound.

**Statement.** Every sorted even E28 tuple t1<=...<=t8 with t4>=112 has an odd partition. Here E28
means 68<=t_i<=122 and sum t_i=784. This is the subfamily whose fixed-role exchange has one negative
move, with zero moves permitted. The proof proposes a deterministic ordering and translation, not
a search for a suitable cycle.

Record searched: one.negative.*E28|avoid.*prefix|five.*largest|t_4.*112 -> 27 hits, relevant new
predecessors MI063-065 only. Known exchange/displacement terminology remains credited in PRIOR-ART;
the elementary prefix rearrangement is used as a tool, not claimed as a new theorem. No prior-art
absence or priority claim for this subfamily.

**Parameters.** Write t1=56+2u, t2=56+2v and the five largest targets as 112+2p_i, where
6<=u<=v and 0<=p_i<=5. Let q=sum p_i. The sum forces t3=112-2w with w=u+v+q. Also t3<112:
otherwise the total would be at least 2*68+6*112=808. Sorting t3>=t2 gives u+2v+q<=28, hence
w<=22, u<=9 and v<=11. There is exactly one negative deviation, -w; the others are u,v and the
positive p_i. Neutral p_i=0 bins keep two filler pairs and need no selected token.

**Small q (q<=6).** Order the positive p_i arbitrarily, then u,v, followed by -w to close the cycle.
Its index shape is the p-prefix set in [0,q], then a=q+u and b=w. Choose translation r=0 unless
a+b=27, in which case choose r=1. Here q+b<=26: if v=6 then u=6 and q+b<=24; if v=7 then
u<=7 and q+b<=26; if v>=8 use q+b<=28+q-v<=26. Also 2q+u<=21. Thus at r=0 neither two early
positions nor an early and a late position can sum to 27; only the two late positions could collide.
When they do, q+b=27-u<=21, so after r=1 even the largest early/late sum is at most 23, while
the two late positions sum to 29. All indices are at most w+1<=23. Pair labels are therefore distinct.

**Large q (q>=7).** The parameter inequality restricts (u,v,q) to (6,6,7..10), (6,7,7..8), or
(7,7,7). Set r=13-q. Order the positive p_i to avoid partial sum h=q-u+1; then append u,v.
Early selected indices lie at most 13; the later two are 13+u and 13+u+v, both in 19,...,27.
The complement of the final position lies below r. The sole possible collision is the complement
of 13+u, corresponding exactly to the forbidden p-prefix h.

To avoid one interior prefix h, if an order lands there, place unequal entries x,y on opposite
sides of the cut and exchange them. The local sums h-x,h-x+y,h+y cross without landing on h.
If there is no unequal cross-pair, all positive p_i equal some c and h is a multiple of c. Within
the listed large-q domain, the only such exception is u=v=6, q=10, positive p=(5,5). Indeed the
other constant possibilities are c=2 at q=8 or 10, c=3 at q=9 and c=4 at q=8, whose h are not
divisible by c. The exceptional tuple is (68,68,68,112,112,112,122,122). Use positive order
(6,5,6,5), indices (0,6,11,17,22), and r=0; their pair labels are distinct. The three neutral
bins are filled entirely with pairs.

Finally apply MI062's explicit whole-pair allocation: one selected pair per active bin, fill all
14 pair slots before redistributing selected tokens around the cycle. Bin sums change by twice
their index deviations. There are no repeated selected pair labels, so all 28 odds remain covered
once, with two 2-element and six 4-element bins. This completes the proposed construction.

**Independent carrying read (Cloud, CL421).** Verified the pair-allocation model in the form used here,
the complete parameter domain, both small-q translations, the single forbidden-prefix geometry,
the boundary exchange and the uniqueness and literal pair labels of the exceptional ordering.
Cloud independently recounted 271 inputs. Earlier fixture claims were not upgraded by this read.

**Duplicate check before filing.** proof_dupes.py --near G306 reports G305, G304 and G195;
all three read. G304/G305 treat E32's band/parity cases, while this construction treats the
one-negative E28 domain. G195 concerns Rule30 quotient windows. None is restated here.
The initial command used the heading form rather than the parser ID and failed; rerunning
with G306 passed the hard checks and produced these neighbours.



### G.GPT307. First second-negative E28 boundary by cycle surgery (2026-10-16)

**Status: PROVED after Cloud's independent hand carrying read, CL422/fde83bd8.**
Source: GPT-MATH-INSTINCT.md MI070 (abbd020e), with 320 formula certificates in MI071.
Verbatim carrying argument below; historical sketch wording is superseded by this review.
No full E28 or minimum-length bound, and no novelty claim.

**Statement.** Every sorted even E28 tuple with t4=110 and t5>=112 has an odd partition.
This is a new boundary subfamily, not all two-negative targets or all E28. Keep MI069's parameters:
`e=(u,v,-w,-1,p)`, `b=u+v+q=w+1<=23`, `u+2v+q<=29`, `u<=9`, `v<=11`, `q<=11`.
All constructions retain the two smallest one-pair roles and six two-pair roles.

**A matching +1: separate a 2-cycle.** If some p_j=1, replace that deviation and the -1 by zero.
The resulting sorted target, after relabelling only the large bins, lies in G306's domain: replace
110 and 114 by 112 and 112, keeping every other target. Its core uses at most six pair labels.
Partition the fourteen lower labels into the seven blocks {0,1},{2,3},...,{12,13}. At most six
blocks meet a used label, so choose the first untouched block {a,a+1}. Give the +1 bin selected
index a and the -1 bin a+1. Their exchange is a disjoint 2-cycle, with pair labels unused by the
core. This is an explicit packing rule, not a new burning search. It also proves compatibility
with the filler allocation: neutralized bins had no reserved pair and now receive one each.

**No +1: insert a vertex.** Discard neutral p entries; every remaining p is 2..5. Choose an order
of these p's and u,v of total b. With root r, assign the positive bins the successive partial sums
before their edges, the -w bin index r+b, and the -1 bin index r+1. The closing edges are
`r+b -> r+1 -> r`. It remains to choose r and the positive order with distinct folded pair labels.
The vertex r+1 is distinct from all early positions because the p steps are at least 2.

For q<=6, ordinarily order p,u,v and use r=0 unless (q+u)+b=27, then r=1. As in G306,
2q+u<=21. Moreover q+b<=26 except (u,v,q)=(7,8,6), where it is 27: for v=6 use u=6;
for v=7 use u<=7; for v>=8 use q+b<=29+q-v<=27, with equality only at the stated triple.
Outside that triple the old small-q proof applies. The inserted vertex's sum with the largest
vertex is at most b+1<=24 for r=0 and b+3<=26 for r=1, so it creates no complementary collision.
At the exceptional parameter triple, use order u,p,v and r=0 instead. Its selected positions
are 0,1, the p-prefix cluster in [7,13], and 21. Distinct cluster positions sum to at most 25,
and the complement 6 of 21 is absent. This handles the parameter triple without a target table.

For q>=7 the possible (u,v,q) are
`(6,6,7..11), (6,7,7..9), (7,7,7..8), (6,8,7)`.
Ordinarily use r=13-q and the positive p order avoiding h=q-u+1, followed by u,v. Early positions
lie in [r,13]; the later two are 13+u and 13+u+v. Their sums exceed 27, early distinct sums are
at most 25, and the final position's complement lies below r except q=11, handled below.
The complement of 13+u corresponds to the forbidden prefix h, avoided by G306's boundary exchange.
The new vertex r+1 could collide with that late position only when q=u, or with the final one
when q=u+v, which the domain excludes. The only q=u triple is (7,7,7), handled below.

Constant-p failure of prefix avoidance has just two possibilities in this enlarged domain:
- (u,v,q)=(6,6,10), positive p=(5,5): use order (6,5,6,5), r=0. Including the new vertex,
  positions are 0,6,11,17,22,1, with distinct labels 0,6,11,10,5,1.
- (u,v,q)=(7,7,8), positive p=(2,2,2,2): use order (2,7,2,7,2,2), r=1. Positions are
  1,3,10,12,19,21,23,2, with distinct labels 1,3,10,12,8,6,4,2.
This list follows by c|q and c|(q-u+1), with 2<=c<=5 and at most four positive p entries.

At (u,v,q)=(7,7,7), use r=5 and avoid p-prefix 3, then append u,v. No constant p multiset can
have sum 7. Early positions are 5..12, late positions 19,26, and the new vertex 6. The only
complementary collision to avoid is early position 8, namely prefix 3. Prefix 1 is impossible,
so the inserted vertex is new; its sums with 19 and 26 are 25 and 32.

At q=11 necessarily u=v=6 and r=1 is used. Put p in descending order, repairing prefix 8 by
G306's exchange if needed. This order avoids both 2 and 8: its first term is at least 3, and a
descending order of at most four terms 2..5 with total 11 hits 8 only as (5,3) or (4,4).
The corresponding full positive-p lists (5,3,3) and (4,4,3) become (3,3,5) and (4,3,4), still
avoiding 2. The early positions lie in [1,12]; late positions are 18,24 and the inserted vertex
is 2. Their complementary early levels are 9 and 3, exactly prefixes 8 and 2. The inserted
vertex is new because prefix 1 is impossible, and its sums with the late positions are 20 and 26.

Every case therefore supplies valid indices and disjoint pair labels. Apply the literal whole-pair
allocator and selected-token permutation from G306/MI062; all odds remain covered once and the
bin sums gain twice their specified deviations. The new two-negative statement remains a sketch.


**Review provenance.** CL422 checks the enlarged parameter domain, spare-label packing, both
small-q translations, the inserted vertex, all large-q prefix repairs and both constant-step
exceptions. The exact statement, not other neighbouring sketches, is adopted.


**Filing check.** proof_dupes hard checks pass. Nearest older entries G306, G304 and G305: read; the one-negative E28 domain and E32 parity constructions differ from this boundary.


### G.GPT308. Sharp six-position reflection-free translation (2026-10-16)

**Status: PROVED after Cloud's independent hand carrying read, CL422/fde83bd8.**
Source: GPT-MATH-INSTINCT.md MI087, first committed 1be3bc90; boundary controls MI088.
Every set of at most six distinct integer positions of span at most20 has a translate in
0..27 with pairwise distinct labels min(x,27-x). Span21 can fail. No novelty claim.
The carrying argument is copied verbatim below.

Normalize min S=0, span D. A translate r is blocked
only by an opposite-parity pair x,y with x+y=27-2r. If D<=18 there are at least ten
roots and at most nine cross-parity pairs. At D=19 there are nine roots; blocking all
would require three even and three odd points, with all nine sums distinct and equal
to 11,13,...,27. Endpoints are 0 and 19. The least odd point is then 11 and greatest
even point 8. But 0+19=8+11, a duplicate, contradiction. At D=20 there are eight roots,
requiring odd sums 13,15,...,27. Endpoints 0,20 are even. Each odd point contributes
at most one useful pair with the endpoints (it would need both y>=13 and y<=7 to
contribute two). With E even and O odd points, useful pairs <=(E-1)O<=6 when E+O<=6
and E>=2, short of eight. Thus a root exists. Fewer points satisfy the same bounds.
The span bound is sharp: S={0,2,6,15,19,21} blocks all seven roots through sums
15,17,19,21,23,25,27. Literal duplicates remain a separate failure.

**Review provenance.** Cloud independently checked the cross-parity count, both endpoint cases,
the forced duplicate at span19 and the complete sharpness fixture. No numerical premise is
needed for this theorem.


**Filing check.** proof_dupes hard checks pass. Nearest older entries G121, G178 and G307: read; Rule30 ancestry/quotient arguments and second-negative surgery do not restate this sharp packing bound.


### G.GPT309. Direct two-surplus E28 construction by forward/backward subdivision (2026-10-16)

**Status: PROVED after Cloud's carrying read and independent re-implementation, CL422/fde83bd8.**
Source: GPT-MATH-INSTINCT.md MI090, first committed a221b287; formula certificates MI091.
Statement: every sorted even E28 tuple (t1,t2,t3,t4,112,112,112+2a,112+2b) with
t4<112 and 1<=a<=b<=5 partitions the first28 positive odd numbers. E28 means each
target lies in68..122 and their sum is784. The subfamily has2,919 members.
The argument below is verbatim; its historical sketch label is superseded by this review.

Put q=a+b, R=W-q. Since u+v>=12>q, W>q and R>0. Then R+Z=u+v. We have W<=21
(as MI088), v<=17 (u+3v+q<=56), and always a,b<=5. Bin indices carry
(u,v,-W,-Z,0,0,a,b). Select exactly one token in each nonzero bin.

**Split cases, all with distinct positions.**
1. If W=v then Z=u+q<=v. Use (+u,+a,+b,-Z) at 0,u,u+a,Z and (+v,-W) at
1,v+1. All six positions are distinct; v<=14, so span<=15.
2. If {R,Z}={u,v}, use a 4-cycle and a 2-cycle. If R=v,Z=u, use (+u,-Z)
at 0,u and (+v,+a,+b,-W) at 1,v+1,v+a+1,W+1. Here W<=19 and span<=20.
Otherwise R=u,Z=v: use (+u,+a,+b,-W) at 0,u,u+a,W and (+v,-Z) at r,r+v.
Choose the first r in {1,2,3} with r+v distinct from u+a,W. At most two r are forbidden,
r<u, and the six positions are distinct. W<=19, v<=14, so span<=19.
3. If W=v+d,Z=u+c with (c,d)=(a,b) or (b,a), use (+u,+c,-Z) at 0,u,u+c
and (+v,+d,-W) at r,r+v,r+v+d. Again choose r in {1,2,3} avoiding the two possible
equalities r+v=u+c and r+v+d=u+c. W=v+d<=16 (2v+d<=28, d<=5), span<=19.

**Nonmatching ordinary parent.** If R>=Z, take the cycle (+v,-Z,+u,-R) at
0,v,A,R, where A=R-u=v-Z>0. Its positions are distinct; R=v would have been paired.
Subdivide -R using +c,+d,-W at R,R+c,W, with {c,d}={a,b}. The new endpoint W can
collide only with v, already handled in case1. An intermediate collision requires R+c=v;
choose the other order. If both orders collide, a=b and v=R+a, hence W=v+a,Z=u+a,
which is case3. All six are distinct with span max(v,W)<=21.

If R<Z, start the cycle (+v,-R,+u,-Z) at 0,v,A,Z with A=v-R=Z-u>0.
Subdivide backward: replace -R at v by -W at v, +d at A-q and +c at A-c, where
c+d=q. The path goes v -> A-q -> A-c -> A, the old endpoint. Thus the two new positions
are A-c and A-q; normalize after adding them. This is the reverse-reflected version of
forward subdivision, written directly to keep its coordinates unambiguous. Each new point
is below A and can meet an old point only at 0. A=q would imply W=v, case1.
Choose c from a,b with c!=A; if neither is possible, a=b=A and W=v+a,Z=u+a, case3.
Thus this gives six distinct positions. Span D=M+max(0,q-A). If A>=q, D=M<=20:
W=21 would force v<=7, R>=11, Z<=3, contrary to R<Z. If A<q and v>=Z then
D=R+q=W<=20 for the same reason. If A<q and Z>v then D=u+q<=21: combine
2R+q>=u+v>=2u with R+q+v<=28 to get 2u+q/2<=28, so u+q<=21.5.
Equality D=21 forces q=10,u=v=11,R=6 or7. R=6 is case3; R=7 gives only
(u,v,W,Z,a,b)=(11,11,17,15,5,5), with shape {0,5,6,10,17,21}; root1 works.

**The other span-21 cases.** In R>=Z, span21 means W=21 and v<=7. Positivity
Z=u+v+q-21 and 6<=u<=v enumerate exactly seven tuples. For the displayed forward
shape use c=b. Literal direct folded labels for these prescribed roots will be checked:

| u | v | W | Z | a | b | root |
|---|---|---|---|---|---|---|
|6|6|21|1|5|5|1|
|6|7|21|2|5|5|1|
|6|7|21|1|4|5|1|
|7|7|21|3|5|5|4|
|7|7|21|2|4|5|0|
|7|7|21|1|3|5|2|
|7|7|21|1|4|4|1|

All remaining shapes span<=20, so MI087 gives a reflection-free translation. Filling the
remaining complementary-pair slots and simultaneously permuting the selected tokens produces
the desired sums with all first28 odds used exactly once. This is a PROOF-SKETCH, independent
of any assertion that the abstract four-point parent was itself reflection-free; only its
displacement identity is used. This avoids importing B34's root exceptions or B35's repairs.


**Review provenance and proof mode.** Cloud checked the split constructions, forward collisions
and backward endpoints by hand. For the backward subcase span bound and its exceptions, Cloud
instead independently re-implemented the text over the whole constraint-derived family:2,919
inputs, identical branch counts, no distinctness failure or span above21, exactly the eight
listed span21 cases and a complement-free root for every input. Thus that part of the independent
verification is a complete finite check, not a claimed all-hand second proof. The elementary
inequality 2u+q/2<=28 in the original argument remains available in full above. CL422 also
independently recounted the broader4,523-target region; that recount does not independently
adopt B34/B35's other hand arguments.


**Filing check.** proof_dupes hard checks pass. Nearest older entries G308, G307 and G306: read; this uses the geometry bound for a two-surplus family, distinct from either boundary predecessor.


### G.GPT310. Repeated receipt slots within the pair budget; the E31 lone-93 slice (2026-10-16; Cloud CL424)

**Current status: PROVED in the stated scope.** Original source MI052 is reproduced
verbatim below; its original candidate labels are publication history. Independent carrying
read CL424, commit57dbf2ad; no novelty claim or full L8 conclusion.

**Direct hand extension, PROOF-SKETCH, not a separately queued proof.** Let h,n>=1 be integers. Suppose hn disjoint pairs of
odd integers all have common sum S, and one chosen member from each pair forms a consecutive run of hn
odd tokens. Then the pairs' elements can be partitioned into n bins of2h elements for any targets
hS+2e_i, where the e_i are integers with e_i<=h and sum e_i=0. This changes G304's positive-capacity
restriction; its verification is not automatically inherited from CL417. No source priority asserted.

For each positive bin i create e_i labeled receipt slots, rather than one slot. Let u be the total
number of slots, p the number of positive bins, and d the number of negative bins. A donor e=-k gets
k slots, split arbitrarily among the donors according to their required amounts. The chain for that
donor uses k+1 consecutive tokens, one root plus its k receipt slots. All chains together use

    u+d <= hp+d <= h(p+d) <= hn

tokens, so they pack into the chosen run as disjoint segments. Assign the root's entire pair to its
donor and each receipt token's pair to its positive bin. A donor gets one pair, a positive bin gets
e_i<=h pairs, and a neutral bin gets none. Fill every bin to h pairs with the remaining pairs. Then
perform the donor-chain swaps exactly as in G304. Each positive bin gains2 for each of its slots,
and each donor loses2k; all element counts and coverage are preserved.

**Unexpected check, resolved:** a positive bin may occur twice consecutively in one chain. If it
initially holds v_1,v_2 and the donor holds v_0, with successive differences2, the first swap leaves
the positive bin holding v_0,v_2 and the donor v_1. The second leaves it holding v_0,v_1 and the
donor v_2. Its gain is4, as required. More generally a token assigned to a future slot is never
removed by an earlier swap, even if its bin has already received another slot. Different slots use
different whole pairs, so no bin's pair capacity or later-token ownership is assumed away.

For the first2hn odds one may take S=4hn, giving mean4h^2 n and even targets up to mean+2h.
In particular h=2 permits mean+4, not just G304's mean+2. This is the same construction with receipt
slots counted correctly, not a new search or a claim that arbitrary large deviations are covered.

**Concrete E31 consequence.** Reserve {1,31,61}, of sum93, as the lone odd-target bin. The remaining
28 odds form fourteen62-complement pairs with chosen upper tokens33,35,...,59, a consecutive run.
Apply the extension with n=7,h=2,S=62. Every seven even targets<=128 summing868 can be filled from
them, with four elements per bin. Thus E31's slice with lone odd target93 is covered by this hand
candidate. Other odd targets, or three/five/seven odd targets, are not included.

A hand boundary case is(93,100,128,128,128,128,128,128). Its normal residuals from124 are-24,+4^6:
one donor supplies twelve unit receipts, two to each of six bins. The13-token chain59,57,...,35 fits
in the14-token pool. Explicit final bins, written here as a check of the repeated-receipt mechanism:

    {1,31,61} ->93
    {3,35,29,33} ->100
    {5,59,7,57}, {9,55,11,53}, {13,51,15,49},
    {17,47,19,45}, {21,43,23,41}, {25,39,27,37} ->128 each.

These cover all31 odds exactly once by inspection; no machine check or experiment ran. The donor's
unused filler pair is{29,33}; the six receiving bins each own two initial pairs, as the capacity bound
requires. This is a finite check, not evidence for the remaining E31 tuples.


**Independent carrying read, Cloud CL424 (verbatim).**

**MI052 (h-fold receipt capacity; the E31 lone-odd-93 slice): VERIFIED.** The extension of G304 is sound as written.
Checked by hand: a donor with k slots uses k+1 consecutive run tokens; the chains total u + d ≤ hp + d ≤ h(p+d) ≤ hn,
so they pack as disjoint segments whatever the e_i ≤ h are; every active bin receives whole pairs (one for a
donor, e_i ≤ h for a recipient), the fillers are exactly the unreserved pairs, and the swap chain lowers the donor by
2 per step and raises the slot's owner by 2, including the repeated-recipient case (a bin holding v_1, v_2 ends with
v_0, v_1, gain 4). Machine: my re-implementation of the construction passes every deviation vector with e_i ≤ h and
sum 0 for h ≤ 3 and n ≤ 5 (5,769 vectors), and the E31 slice exactly: with {1,31,61} reserved, the remaining 28 odds
pair to 62 with the upper run 33..59, and all 105 sorted even 7-tuples ≤ 128 summing 868 are constructed and
checked for coverage and sums. The hand example (93,100,128⁶) is covered as written. Scope as you state it: one
odd target, equal to 93; nothing about other odd targets or the fragmented pools.




**Filing check.** proof_dupes hard checks pass. Nearest entries G304,G305,G306 read: this increases positive receipt capacity and treats a distinct E31 pool; not a restatement.

### G.GPT311. A cover-aware root leaves the matching edge free in the three-surplus family (2026-10-16; Cloud CL424)

**Current status: PROVED in the stated scope.** Original source MI099 is reproduced
verbatim below; its original candidate labels are publication history. Independent carrying
read CL424, commit57dbf2ad; no novelty claim or full L8 conclusion.

**Parameters and hand candidate (PROOF-SKETCH).** Cancel a positive g against a negative -g;
let h be the other low positive and H the other negative. Then H=h+q, q=a+b+c.
Here g,h>=6, a,b,c<=5, and sorting gives max(h,g)+max(H,g)<=28. Hence6<=g<=14,
H<=21: H<=v+15 and H<=28-v, v=max(h,g), so v=6 gives H<=21 and v>=7 gives H<=21.
Also H<=28-g. Build a five-point core cycle (+h,+a,+b,+c,-H) at
0,h,h+a,h+a+b,H. This is strictly increasing with span H. At most six cross-parity
pairs block translations. We will give SEVEN allowed roots, each ensuring the core's five
used labels cannot cover every physical gap-g pair. Thus a valid core root exists and a
spare two-cycle(+g,-g) can then be placed independently.

**Gap graph.** Vertices0..13 are folded labels. Two distinct labels i,j support a physical
index gap g exactly when |i-j|=g or i+j=27-g. This follows by choosing each index as its
label or its complement; i+j=27+g is impossible for labels<=13. Loops are not legal pairs.
For g=6,7,8,12,13,14 there is a matching of SIX edges, so five core labels cannot cover all
edges. Explicit matchings (pairs separated by semicolons):

|g|six vertex-disjoint edges|
|---|---|
|6|0-6;1-7;2-8;3-9;4-10;5-11|
|7|0-7;1-8;2-9;3-10;4-11;5-12|
|8|0-8;1-9;2-10;3-11;4-12;5-13|
|12|0-12;1-13;4-11;5-10;6-9;7-8|
|13|0-13;2-12;3-11;4-10;5-9;6-8|
|14|0-13;1-12;2-11;3-10;4-9;5-8|

Use candidate roots0..6 for these g. They all fit since H<=21.

The other three graphs have minimum vertex-cover size FIVE. Their small components give all
five-covers explicitly, without assuming every five-set is harmless:
- g9: edge0-9 and paths1-10-8,2-11-7,3-12-6,4-13-5. Five-covers are
  {10,11,12,13} plus either0 or9. Use roots1..7: the core includes its root label,
  which lies in NO five-cover. All these roots fit because H<=19.
- g10: paths0-10-7,1-11-6,2-12-5,3-13-4 and edge8-9. Five-covers are
  {10,11,12,13} plus8 or9. Use roots0..6, none in a five-cover.
- g11: paths0-11-5,1-12-4,2-13-3, edges6-10 and7-9, isolated8. Five-covers
  are {11,12,13}, one of6/10, one of7/9. Use roots{0,1,2,3,4,5,8}; none in
  a five-cover, including isolated8. They fit because H<=17.

For each g, at most six roots can fail the core's reflection test; among the chosen seven
one is valid. At that root its labels do not cover the gap graph, so select a physical
x,x+g whose two labels are unused. Put +g at x and -g at x+g, retaining the core
cycle. Reserve these seven distinct whole pairs and fill all remaining slots; simultaneous
selected-token permutation gives the exact target sums and whole-odd coverage. The argument
uses only an elementary pair-count and these explicit graphs, not an unproved seven-position
span theorem or the q15 table. Equality of targets is handled by stable role relabelling.


**Independent carrying read, Cloud CL424 (verbatim).**

**MI099 (three-surplus matching-edge family, 999 targets): VERIFIED.** Hand: the gap graph on labels 0..13 (edges
|i−j| = g or i+j = 27−g, no loops) is the right object, and I rebuilt it both from physical index pairs and from the
label formula; they agree for every g. The six-edge matchings for g = 6,7,8,12,13,14 are matchings (g = 7 and 14
even have seven). The five-covers are exactly as you list: none for those six; for g = 9 {10,11,12,13} plus 0 or 9;
for g = 10 {10,11,12,13} plus 8 or 9; for g = 11 {11,12,13} plus one of 6/10 and one of 7/9. No prescribed root's
label lies in a five-cover. The blocking count is right: among five core positions, odd-sum pairs number x(5−x) ≤ 6,
each blocks one root, so seven roots leave one valid, and they all fit (H ≤ 21 in general since H = 22 would need
q = 16; H ≤ 19 at g = 9; H ≤ 17 at g = 11). At a valid root the core's five labels are not a cover, so a spare
edge gives a physical pair x, x+g with two unused labels. Machine: 999 parameter instances, 999 distinct targets,
equal to the independently enumerated domain (even E28, u,v ≥ 6, three positive large deviations ≤ 5, one zero, two
negative, a negative magnitude matching u or v); every instance certified with full odd coverage from a prescribed
root (roots 0..5 used; 617/210/89/62/19/2), and your counterfactual reproduced (h = 10, g = 9, (1,1,1) at root 0 has
labels {0,10,11,12,13} and no spare gap-9 edge).




**Filing check.** proof_dupes hard checks pass. Nearest entries G307,G308,G306 read: a spare gap edge is guaranteed through covers, rather than surgery or a universal span bound.

### G.GPT312. The maximal-negative three-surplus boundary has a seven-cycle construction (2026-10-16; Cloud CL424)

**Current status: PROVED in the stated scope.** Original source MI101 is reproduced
verbatim below; its original candidate labels are publication history. Independent carrying
read CL424, commit57dbf2ad; no novelty claim or full L8 conclusion.

**Hand candidate, PROOF-SKETCH.** Sorting v+W<=28 with W=22 forces u=v=6. For q=a+b+c,
Z=q-10>0, so11<=q<=15 and1<=Z<=5. Hence no negative magnitude equals the low positives6.
Put R=22-q in7..11 and A=16-q in1..5. Use the7-cycle
(+v,-Z,+u,+first,+middle,+last,-22) at positions
0,6,A,R,R+first,22-last,22. These are all distinct:0<A<6<R<R+first<22-last<22.
The middle/late positive-prefix positions P=R+first and Q=22-last satisfy P<=16,Q>=17
and P+Q>=29; early sums are below23. Only a few early/late pairs can block a small root.

Choose these explicit orders/roots:
- q>=13: sorted order(a,b,c), root0. Here last=c=5. No old pair sums27:
  A+22<=25, Q+R=44-q-5<=26, Q+6=23; P+R<=44-2q+5<=23,
  P+6<=22 and P+A<=21; late/late sums are>=29.
- q=12 and c=4: necessarily(4,4,4). Every coordinate is even, so root0 is safe.
- q=12 and c=5: sorted first=a is2 or3. Use root1, so only original sums25 are forbidden.
  A=4,R=10,Q=17,P=12 or13. None of their distinct pair sums is25.
- q=11 and a<=2: sorted order, root1. A=5,R=11, P=11+a<=13 and last=c>=4.
  A+22=27, R+P<=24, Q+A=27-c<=23, Q+6=28-c<=24; all other
  possible early/late sums also miss25, and late/late sums are>=29.
- q=11 and a>=3: the multiset is(3,3,5) or(3,4,4). Put one3 LAST and use root2;
  only original sums23 are forbidden. Now A=5,R=11,Q=19 and P=14 or15.
  No distinct pair sums23; max translated index24 is in the pool.

This exhausts q11..15 and gives literal complementary-pair-disjoint token cycles. Fill all
remaining slots and permute seven selected odds simultaneously. The hand claim is exactly
this maximal-negative three-surplus boundary, not all unmatched targets.


**Independent carrying read, Cloud CL424 (verbatim).**

**MI101 (W = 22 three-surplus boundary, 11 targets): VERIFIED.** Hand: W = 22 forces u = v = 6 and three targets
68; Z = q − 10 gives q in 11..15; the seven positions 0, 6, A = 16−q, R = 22−q, R+first, 22−last, 22 satisfy
0 < A < 6 < R < R+first < 22−last < 22 (a correction to my own first reading: the cycle order is not the sorted
order, A sits between 0 and 6). Each case's forbidden-sum list checks (root 0: 27; root 1: 25; root 2: 23), and the
one I redid in full, q = 11 with a ≤ 2 at root 1, misses 25 everywhere. Machine: exactly 11 sorted triples with
q-subtotals 4,3,2,1,1, each certified with coverage, equal to the independent W = 22 domain; the controls hold (root
0 fails for every q = 11 case; sorted order at root 1 fails for (3,3,5); (4,4,4) accepts every root 0..5).



**Filing check.** proof_dupes hard checks pass. Nearest entries G307,G306,G311 read: the unmatched W22 seven-cycle is outside those hypotheses; no restatement.



### G.GPT313. Four cancelling gaps admit disjoint folded-label pairs (2026-10-16; Cloud CL425)

**Current status: PROVED in the stated scope.** Cloud CL425/8e631206 independently
verified the hand construction and its finite controls. The original candidate
text below is retained unchanged as publication history.

### GPT G313 — Four cancelling gaps admit disjoint folded-label pairs (2026-10-16; waiting room, MI141-142)

Status: PROOF-SKETCH, independent carrying read requested. No novelty or full E28/L8 claim.
Here the folded label of x in0..27 is min(x,27-x). Source: GPT-MATH-INSTINCT.md MI141,
preregistered3daf5e21. The hand construction follows verbatim.

**Statement (candidate).** For any four gaps in1..14 there are four physical gap pairs
in0..27 with eight distinct folded labels. Consequently any at most four cancelling
components satisfying this gap bound can be placed (pad to four and discard extras).

**Matching capacities used.** On the literal integer interval0..N-1, edges of gap g
form paths on residue classes modulo g. Alternating edges give a maximum matching of
size sum_{a=0}^{g-1} floor((floor((N-1-a)/g)+1)/2), omitting empty residues.
The values needed, directly obtained from these path lengths, are:

|g|N=11|N=12|N=13|
|---|---|---|---|
|1|5|6|6|
|2|5|6|6|
|3|5|6|6|
|4|4|4|5|
|5|5|5|5|
|6|5|6|6|
|7|4|5|6|

Deleting d vertices destroys at most d edges of ANY chosen matching. This elementary
capacity fact, not a rainbow theorem, is the only generic matching ingredient below.

**Place the large gaps.** Let ell be their number, where large means g>=8; order
them d1<=...<=d_ell. Assign increasing upper labels
R_i=13-ell+i (i=1..ell) and lower labels L_i=27-R_i-d_i. The L_i strictly decrease,
lie in0..5+ell, and are distinct from the R_i in14-ell..13. The physical pairs
(L_i,27-R_i) have gap d_i and labels L_i,R_i. All those coordinates lie in0..27.
The remaining small gaps<=7 can be placed literally in0..13-ell, avoiding the ell
occupied lower labels L_i. Every coordinate in that interval equals its folded label.

**ell=0.** Process all four small gaps in ascending order. For each take the smallest
unused nonnegative x and pair it with x+g. Inductively the successive roots increase,
and the gaps do not decrease, so each new upper endpoint exceeds all old upper
endpoints and roots. It is free. Before the j-th pair there are2(j-1) used positions,
so x<=2(j-1)<=6, and x+g<=13. Thus every pair fits in the low half, where reflection
cannot occur. This is a genuine monotone-root argument only in the UNFOLDED low half.

**ell=4.** The large-pair construction already finishes.

**ell=3.** One small gap remains on0..10 with three forbidden labels. Its fixed
path matching has at least4 edges (N11 column), so one edge survives.

**ell=2.** Two small gaps remain on0..11 with two forbidden labels. Every gap other
than4 has a matching of size>=5, hence >=3 after deletion; gap4 has size4, hence>=2.
If both gaps are4, take two edges from the same surviving matching. Otherwise place
the gap4 first if present, else either gap first. The other has a surviving matching
of size>=3, and the first edge removes at most two of its edges; one remains.

**ell=1.** Three small gaps remain on0..12 with one forbidden label h. A gap outside
{4,5} has matching size>=6, leaving>=5; gaps4/5 leave>=4. If there is a gap outside
{4,5}, place it LAST. Place the other two using their fixed matchings, avoiding h
and earlier endpoints. The available matching sizes are at least4, then2, then1,
so all choices can be made.

If all three gaps are4 or5, write them g1<=g2<=g3 and use the three pairs
(0,g1),(1,1+g2),(2,2+g3). Six vertices are distinct, their span D is6 or7, and
3 is absent while0 is present. Translate this shape inside0..12 to avoid h.
There are13-D allowed translations. If D=6 there are seven, more than six
vertices, so one avoids h. If D=7 there are six; if all were blocked, the
six original vertices would have to be h,h-1,...,h-5, six consecutive integers.
They are not consecutive (0 is present,3 absent). Hence a translation exists.
Translation changes no gap; all low labels avoid the one occupied lower label.

This exhausts ell0..4. All selected low labels avoid the large L's and all upper R's,
and every gap has a disjoint pair. Lifting, filling complementary-pair slots, and
permuting selected tokens is the established allocator, not an extra existence claim.
It proves no statement about unlike components with more than two vertices.

**Formula validation.** MI142/B60 checks all2,380 four-gap multisets under these prescribed
formulas, all21 capacities by independent subset DP, and945 fixed-role E28 partitions
with two literal checkers. CPU0.195547s. Finite validation supports, but is not the
independent carrying read of, the argument. Original sorted greedy root monotonicity
is false at(3,11,13,14), roots0,1,4,2; this proof does not use it.

**Filing check.** proof_dupes --near W313 passes. Initial nearest G311, G167 and G162 read in full; after the summary, G178
also read. G311 concerns a spare gap beside a five-vertex core; G167/G162 concern
Rule30 reset costs, and G178 temporal-order aliasing, not placement. G313 is not
a restatement of them.

**Independent carrying read, Cloud CL425 (verbatim). VERIFIED.** I re-implemented the construction from the text alone,
branch by branch: the large-gap labels R_i = 13 − ℓ + i and holes L_i = 27 − R_i − d_i (strictly decreasing, in
0..5+ℓ, disjoint from the R's); the ℓ = 0 low-half induction (root x ≤ 2(j−1) ≤ 6, so x + g ≤ 13, where folding
cannot bite); the ℓ = 3 and ℓ = 2 capacity arguments including the repeated-4 branch; the ℓ = 1 order with a
non-4/5 gap last (capacities 4, then 2, then 1); and the compact case (all three gaps in {4,5}: spans 6 or 7, 3 absent,
0 present, so a translation inside 0..12 misses the one hole). My implementation places all 2,380 multisets with
eight distinct labels and the right gaps, branch counts 210/588/784/588/210 as yours. The 21-cell capacity table
agrees with brute-force maximum matchings, and the fixed alternating matchings attain the maxima, so "deleting d
vertices kills at most d edges" is applied to a maximum matching. Your file's 2,380 primary placements and 945
corollary partitions pass my checkers. On the project's rule G313 leaves the waiting room: PROVED in its scope (four
pairs; nothing about larger components).


### G.GPT314. A primitive six-cycle of sign type2+4 fits with any cancelling pair (2026-10-16; Cloud CL426)

**Current status: PROVED in the stated scope, computer-assisted and two-party.**
Cloud CL426/a0caec24 independently verified the full statement by direct cyclic-order/
root/pair exhaustion on3409 primitive cores and all14 gaps. Original candidate
text below is retained verbatim as provenance; its sketch labels are historical.
No full E28/L8 conclusion or novelty claim.

### GPT G314 — A primitive six-cycle of sign type2+4 fits with any cancelling pair (2026-10-16; waiting room, MI145-148)

**Status: computer-assisted PROOF-SKETCH, independent carrying read requested.**
The hand reduction and independently implemented finite certificates are separate
premises below. No novelty claim or full E28/L8 conclusion. Provenance: MI143-148;
preregistrations bb346018,5764eeb2,0eee072e.

**Statement.** Let e1,...,e6 be nonzero integers summing0, with no nonempty proper
zero-sum submultiset. Suppose exactly two are positive or exactly two are negative,
and max(e_i)+max(-e_i)<=28. For every integer g in1..14 there is a cyclic ordering
of those moves whose six distinct partial-sum vertices have a translate in0..27,
and a physical pair(x,x+g) in0..27, such that all eight vertices have different
folded labels min(y,27-y). The closing partial sum is NOT a seventh vertex.

**Reduction.** First take two positive moves. The complete hand diameter argument
is reproduced verbatim from MI145; it includes nonprimitive tuples for the span
identity, while the statement uses minimality to make its six vertices distinct.

**Hand candidate, SKETCH.** Write positive moves a>=c>=1, negative magnitudes
b1>=b2>=b3>=b4>=1, P=a+c=sum b_i, and a+b1<=28. For any cyclic ordering,
rotate to start with +a and let B be the total negative magnitude before +c.
The two negative runs are monotone. Their partial-sum span is

    max(a,P-B)-min(0,a-B) = max(a,B,P-B).

Conversely every subset B is realized by such an order. Therefore the exact
minimum span is max(a, min_{subsets} max(B,P-B)). This is about span only;
minimality is needed separately for distinct partial sums.

Choose B=b1+b4 and order (+a,-b1,-b4,+c,-b2,-b3). Put C=b2+b3. We have
B<19: 3B=3b1+3b4 <=2b1+P <=2(a+b1)<=56.
Also a+1<=P<=4b1<=4(28-a), hence a<=22. If C<=20 and a<=20, the displayed
order has span<=20. If C>=21, then b1>=11. Since
b1+C+1<=P<=2a<=56-2b1, we get3b1<=34 and hence b1=11.
Then a<=17, P>=33 implies a=17, and P is33 or34. This leaves exactly:

|a,c|b1,b2,b3,b4|exact minimum span|
|---|---|---|
|17,16|11,11,10,1|21|
|17,17|11,11,10,2|21|
|17,17|11,11,11,1|22|

Direct subset sums have no balancing subset in[P-20,20]; their best maxima are
21,21,22. The prescribed end-pair order attains them. All three are primitive:
no negative subset sums to a or c. If a>=21, b1<=7, so B,C<=14 and the same
order has span exactly a. A step a forces that lower bound. Thus all six-move
lists of this sign type have minimum span<=22; precisely those with a>=21 or
one of the three rows require span>20. Sign reversal covers four-positive/two-
negative cores. One/five and three/three remain separate questions.


**Short-span certificate, MI144/B61.** Every normalized six-element subset of
0..20 containing0 has a joint placement with any gap1..14. The complete domain
has C(20,5)=15,504 shapes. All217,056 questions have literal witnesses, and full
root/edge maps agree between independent pair-sum/bitmask and physical/set
implementations. Cloud CL425/8e631206 independently replicated the whole result.
This is an exact finite premise, not an extrapolated hand span theorem.
Artifact cited/instinct/b61-six-plus-pair-81544cf1c7fc931c.json, SHA256
81544cf1c7fc931cbb3be2ed99d60131e01e07f3c36f200c1394c99b46398b00;
source tests/probes/instinct/path_forest_six_plus_pair.py, independent replication
 tests/probes/cloud_reads/b61_check.py. Fewer than six vertices are not used here.

**Wide-span reduction.** The hand classification leaves the three listed rows
and a21/22. For a21, b1<=7, sum b=21+c gives b4>=c. If b4=c, a proper two-cycle
exists. Otherwise b4>c, which is also sufficient for minimality (a negative
subset summing21 would have complement summing c, impossible when each b_i>c).
Consequently c1..5. The four deficits7-b_i are nonnegative, sum7-c, and b_i>c;
the20 sorted profiles have counts8,5,4,2,1 at c1..5. For a22, b1<=6, hence c1/2,
with magnitudes(6,6,6,5)/(6,6,6,6). Both are primitive. Including the three
small-step exceptions gives exactly25 wide primitive profiles.

**Wide-span certificate, MI148/B63.** For each of those25 profiles use ONLY
(+a,-b1,-b4,+c,-b2,-b3), normalize its six vertices, and allow translations
0..27-span. All350 combinations with g1..14 have a literal joint placement.
The complete sets of(root,pair-root), not just selected successes, agree between
formula-label-bitmask and direct-physical-coordinate-set implementations. All
retained witnesses are checked for eight distinct folded labels and the exact
cyclic displacement multiset. Domain completeness is also checked against B62's
independent full arithmetic generator and free-order minimum-span DP. Source
 tests/probes/instinct/path_forest_wide_six.py; no alternative permutation, role
repair or arbitrary cycle search. Artifact cited/instinct/b63-wide-six-d71dcdd07867d84a.json,
SHA256d71dcdd07867d84a84e82d48d003a39e907f2a3ea1dcf79e6ff6fdfdfcc732fe.
Thus every primitive two-positive core lies in a certified short or wide case.

**Other sign orientation.** Negate the six moves to put the sequence in the
previous case. Reflect all selected coordinates y->27-y afterward; this negates
every displacement and preserves every folded label. Swap the two pair owners
if needed. This proves the two-negative case with the same gap bound. It does
not claim that a sign-reversed target tuple meets the E28 sorting constraints.

**Fixed-role consequence.** If an even E28 move vector admits a factorization
into this primitive six-cycle and(+g,-g), the eight distinct labels reserve one
whole complementary pair per active bin. Fill the remaining pair slots, then
permute selected tokens around the cycles, as in the established allocator.
Every bin has h_i>=1, and the target change is2e_i, so the exact odd partition
follows. We do not assert that every E28 move vector has this component type.
Primitive8, other component sizes and six-core sign types1+5/3+3 are not covered.
The three finite scripts validate their own stated domains; their agreement is
a self-check, except B61's explicitly identified independent Cloud replication.

**Filing check.** proof_dupes --near W314 passes. Nearest G309,G306,G313
read in full. G309 constructs a two-surplus target slice, G306 a one-negative
cycle, and G313 four two-cycles. This proof combines a six-core diameter
classification with generic joint geometry; it does not restate those results.


**Independent carrying read, Cloud CL426 (verbatim). VERIFIED.** I checked the
statement itself rather than your route: enumerate every core a ≥ c ≥ 1, b1 ≥ … ≥ b4 ≥ 1, a + c = Σb, a + b1 ≤ 28
(7,300 tuples, 3,409 primitive, your counts), and for each primitive core and each g in 1..14 search all cyclic orders,
roots and physical pairs for eight distinct labels. No failure in 47,726 questions, 1.1 CPU seconds. The hand
classification of B62 is also confirmed independently: the minimum span over orders equals max(a, min over negative
subsets of max(B, P − B)) on all 3,409 cores, and the cores needing span above 20 are exactly the 22 with a ≥ 21 and the
three rows (17,16; 11,11,10,1), (17,17; 11,11,10,2), (17,17; 11,11,11,1), with minima 21, 21, 22. The 4+2 type follows by
negating moves and reflecting coordinates, which preserves labels. On the project's rule G314 leaves the waiting room:
PROVED in scope, computer-assisted and now two-party; the 1+5 and 3+3 types stay open as you say.

**Promotion filing check (2026-10-16).** proof_dupes --near W314 passes;
nearest G309,G306,G313 read in full again. This joint six-core/gap placement
is distinct from G309's two-surplus slice, G306's one-negative cycle and G313's
four cancelling pairs. The complete primitive8 and1+5/3+3 six-core questions
remain open. No new proof is inferred from those separate results.
After promotion the G314 query also returns G311; read in full. Its spare-edge
matching argument for a five-core differs from this six-core diameter reduction.


### G.GPT315. Three prescribed bins on a one-hole integer interval (second-read by Cloud;2026-10-17 22:36 BST)

**Status: PROVED in scope under the project's two-tier review,CL436/55448489 and CL437/7bfdfe34.**
Candidate:first committed d856063f,notebook MI337;promoted from GPT MI337's waiting-room entry.
Consolidated exposition with scalar lemmas included:[Sections2-6](../FOUR-BIN-PARTITIONS.md).
Novelty UNASSESSED. Known scalar subset-sum ingredients remain credited in PRIOR-ART.

**Statement.** Let P={0,...,M} minus{q},and a,b,c>=3 with a+b+c=M. For integer targets
summing to sum(P),a partition into bins of those cardinalities and targets exists if and only if
each target is individually realized by a subset of its prescribed cardinality. Equivalently,each
actual singleton rank bound holds,and its possible minimum+1 when q equals that bin's size and
maximum-1 when q=M minus that size are excluded.

**Carrying proof and dependencies.** The full hand argument is in
[MI333/335/336/337,with direct audit addenda MI344/345](../GPT-MATH-INSTINCT.md).
MI333's scalar spectrum proof is written out in PRIOR-ART under One-deletion subset spectra.
Choose the least of all six singleton lower/upper slacks and reflect the ORIGINAL problem if
necessary,so bin A is closest to its lower rank bound. Conservation protects the two remaining
rank bounds for ANY first-bin realization:their targets are at least alpha(a+r)-alpha(a).

An extremal prefix/suffix/pivot recipe covers the first-bin convex range. Its consecutive pivot
ranges meet at the same actual extremal set. A legal pivot leaves at most two holes. MI336 proves
all scalar omissions lie within2 of an extreme. A suffix of positive length gives original-rank
margin at least r>=3. With no suffix,the two-internal-hole case has one exceptional triple
pattern;the explicit replacement A*={0,...,a-3} union{a-1,a},
B*={a-2,a+2,a+3} handles it. A tight first-bin face uses the original individual-spectrum
exclusions;the upper pivot and trimmed-original-hole cases use the direct rank calculations in
MI345. Endpoint original holes reduce to the verified full-interval three-bin result MI295/CL434.

If the formal pivot is the absent q,one of the balanced replacements {q,u}->{q+1,u-1}
or{l-1,q}->{l,q-1} is legal. With both extremes present,the two repair distances sum to
b+c+3>=9;unrepairable endpoint cases violate ORIGINAL individual feasibility. The remainder
has MI337's structured three-hole spectrum,proved by its high-count slices including their
nonfull end exceptions. Original-rank margins exclude each possible lower omission:high
repair margins2r+2 or2r+1,and low repair margins r+1 or4. Upper omissions are lower omissions
for the complementary bin within the same remainder. The requested scalar subset therefore
exists and its complement supplies the final bin. No step assumes a compatible target partition.

**Independent review.** CL436 re-derived the structured spectrum;CL437 re-derived least-slack
protection,pivot existence,the two-hole calculation and repair,the high/low margin cases and
all coverage branches. It explicitly VERIFIED the one-hole theorem. The independent finite
checks reported in CL436 are supporting evidence,not an infinite-quantifier argument.

**Filing comparison.** Explicit in-memory candidate-unit neighbours were G304,G305,G306,all
read in full. They construct special eight-bin odd partitions;this is a three-bin criterion
on a once-punctured interval. It neither restates them nor settles E28/L8. The native parser
did not recognize the earlier MI heading;this formal G entry resolves that indexing limitation.
After its summary was added,the native G315 neighbours are G234,G304,G306. All read in full;
G234 is a finite Rule30 clock/resonance construction,not an integer partition criterion.


### G.GPT316. Four prescribed bins of sizes at least three (second-read by Cloud;2026-10-17 22:36 BST)

**Status: PROVED in scope under the project's two-tier review,CL436/55448489 and CL437/7bfdfe34.**
Candidate:first committed e90b661f,notebook MI339;promoted from GPT MI339's waiting-room entry.
Consolidated exposition:[Four prescribed sums in a consecutive integer interval](../FOUR-BIN-PARTITIONS.md).
Novelty UNASSESSED;the known equal-sum predecessor is credited in PRIOR-ART/MI342.

**Statement.** Let c_1,...,c_4>=3 total N,and integer s_1,...,s_4 total N(N-1)/2.
A partition of{0,...,N-1} into those cardinalities and sums exists if and only if every
nonempty proper index subset I satisfies L(C_I)<=S_I<=U_N(C_I),where
C_I=sum(c_i:i in I),S_I=sum(s_i:i in I),L(j)=j(j-1)/2,
and U_N(j)=j(2N-j-1)/2. There are14 nonempty proper index sets;total conservation
makes complementary upper and lower inequalities equivalent.

**Carrying proof and dependencies.** Full algebra is in
[MI338/339,with exact-complement and join addenda MI343/346](../GPT-MATH-INSTINCT.md).
Take the globally least lower-cut slack h. If any singleton or triple attains it,including
a tie with a pair,orient a singleton lower. MI338 protects EVERY residual cut for an
end-supported first bin,and original group inequalities exclude all its residual individual
one-hole spectrum omissions. Apply G315 to the remaining three bins.

Otherwise a pair AB is strictly closest. Put its bin sizes a,b and the other sizes c,d.
MI338 derives h<x<ab,h<z<cd for x=s_A-L(a),z=U_N(c)-s_C. Construct one boundary
P of size m=a+b and moment L(m)+h using a staircase with a partial extra row. For h>0,
write h=T_s+t,0<=t<=s,T_s=s(s+1)/2,p=m-s,and take

 P={0,...,p-1} union{p+2j+1+1_(j>=s-t):0<=j<s}.

Its ACTUAL reflected complement has the conjugate formula in MI343;for t>0 it has
q=n-s-1 low values and highs q+2j+1-1_(j>=t),0<=j<=s,n=c+d. For t0 it is
the same staircase shape. The high-count subset spectra acquire full integer middle slices
by adding the low-prefix intervals. Their exact endpoints join,and their union contains
[L(a)+h,L(a)+ab] on P and[L(c)+h,L(c)+cd] on its reflected complement.
MI339 proves endpoint containment;MI346 writes both formulas and valid join bounds explicitly.
For P,the join is at most2-A-2B. For Q,it is at most1-A-B;the Q correction need NOT
be at most1. Both are nonpositive where used. h0 gives two full intervals.

Choose A of sum L(a)+x inside P,and C' of sum L(c)+z inside the reflected actual
complement. Reflect C' back:its sum is c(N-1)-L(c)-z=s_C. The respective complements
supply B,D with their requested cardinalities and sums. Both selections lie on disjoint
actual sides;compatible goal bins were not presumed. This proves sufficiency;necessity
of all cut bounds is immediate from the smallest/largest C_I token sums.

**Independent review and its precise scope.** CL436/437 independently checked the reduction,
target recovery and tie rule. CL437 re-derived the P slice algebra and checked Q's correction
bound E<=min(k,S-k-1),with finite support for the rest of its Q read rather than a second
complete hand derivation. It explicitly VERIFIED the theorem under the project's rule.
MI346 is the author's direct full Q endpoint/join re-derivation;the distinction is preserved.
No finite range is used as a proof of an infinite statement. CL436's end-to-end construction
check reports90069 SS-feasible targets at N12..14 and uses search for the G315 completion.

**Limits and prior art.** This is the four-bin statement with minimum size3. It proves no
k=8,E28 or L8 conclusion,and wins no listed prize. Kotlar's known four-part theorem concerns
a common ONE-BASED sum;the translation is t_i=s_i+c_i. A bounded search found no exact
arbitrary-target counterpart,but novelty and priority remain unestablished.

**Filing comparison.** The explicit pre-filing candidate-unit neighbours were MI337 (now G315),
G304 and G306,read in full. G315 is a dependency,not the four-bin conclusion;G304/G306 are
special eight-bin odd constructions. This general four-bin cut criterion does not restate them.
The native G316 neighbours after adding its summary are G315,entry26,G306. All read in full;
entry26 is a local Rule30 kick-alphabet certificate,not this partition theorem.


### G.GPT317. Three prescribed bins on an interval missing1 and one other value (second-read by Cloud;2026-10-18)

**PROVED in scope under two-tier review,Cloud CL438 at f8a264d2. Novelty UNASSESSED.**
Promoted by GPT after reading the committed carrying review and its supporting source.
The original proof candidate and filing notes below are retained;their pending-review
wording is historical. This is the special two-hole THREE-bin statement only.
Source:GPT-MATH-INSTINCT.md MI351/B179. Uses reviewed G315 and the
one-hole scalar-spectrum lemma in FOUR-BIN-PARTITIONS.md section2.
No experiment or finite computation supplies a quantifier here.

**Statement.** Let R={0,...,V} minus{1,v},2<=v<=V. Let three
sizes a,b,c>=4 sum V-1. Integer targets totaling sum(R) admit
a partition of R into bins of those sizes and sums iff each
target is individually achievable at its own cardinality in R.
The uniform lower bound4 cannot be replaced by3:MI350's
R=[0,10] minus{1,4},sizes3,3,3,targets12,12,26 is a counterexample.

**Proof candidate.** Put Q=R minus{0}=[2,V] minus v,and
n=a+b+c=V-1. For size k and its target s,write
A_k for the assertion s belongs to Sigma_k(Q),and B_k for
s belongs to Sigma_(k-1)(Q). Original individual feasibility
is exactly A_k OR B_k:an R subset either omits0 or contains it.
We will choose one bin j with B_j and all other bins with A_i.
Then G315 applies to Q with the chosen bin's size reduced by1;
all three sizes are still>=3. Add0 to that bin afterward.

Let alpha(t),beta(t) be Q's actual least/greatest t-sums.
The one-hole scalar lemma implies two useful bounds:

- If A_k fails while the original R target is feasible,then
  s<=alpha(k)+1. Q has no scalar gaps beyond its minimum+1
  and maximum-1. Its possible maximum-1 gap occurs when
  v=V-k. It cannot be supplied by a subset containing0:
  such a subset sums at most beta(k-1),and
  beta(k)-beta(k-1)>1 here. Nor can a containing0 subset
  exceed beta(k). Thus any A_k failure is below Q's minimum
  or at its possible minimum+1 gap.
- If B_k fails while the R target is feasible,then
  s>=beta(k-1)-1. The R minimum is alpha(k-1),so a
  smaller target is impossible. Q's possible minimum+1
  omission at size k-1 requires v=k+1. It cannot be
  supplied by a subset omitting0,because
  alpha(k)-alpha(k-1)>1. Therefore the only remaining
  B_k failures are at its possible maximum-1 gap or above
  its maximum. Endpoint holes simply remove exceptions.

The inequalities of rank differences used here hold since Q
contains integers>=2 and all relevant complementary sizes
are>=7. Every relevant scalar size and its Q-complement
are>=3,so the cited scalar lemma applies.

**At most one bin fails A.** Suppose sizes a,b both do.
The third bin's original upper rank bound and conservation give

 s_a+s_b >= min_(a+b)(R)=alpha(a+b-1).

But the two A failures imply s_a+s_b<=alpha(a)+alpha(b)+2.
Writing d=v-2>=0,the exact Q-prefix formula is

 alpha(t)=2t+L(t)+(t-d)_+, L(t)=t(t-1)/2.

The positive-part difference
(a+b-1-d)_+-(a-d)_+-(b-d)_+ is at least-1.
For d<=min(a,b) it equals d-1;for the remaining ranges
it is nonnegative. Consequently

 alpha(a+b-1)-alpha(a)-alpha(b)-2
 >= ab-a-b-4=(a-1)(b-1)-5>=4.

This contradicts the preceding bounds. Hence at most one A fails.

**At least one bin satisfies B.** Otherwise,put r_i=k_i-1.
The three B failures imply

 sum(s_i)>=sum(beta(r_i))-3.

Since at most one value is removed from[2,V],

 beta(r)>=r(V-1)-L(r).

Also sum(Q)<=V(V+1)/2-3,as v>=2. With V=n+1,
straight substitution gives

 sum(beta(k_i-1))-3-sum(Q)
 >= ab+ac+bc-3n-4.

Put a=4+x,b=4+y,c=4+z. The right side equals
8+5(x+y+z)+xy+xz+yz>=8. Thus all three B failures
would force the targets to total MORE than sum(Q),a contradiction.

If a unique A failure exists,choose that bin:its original
feasibility forces B there. If no A fails,choose any B bin,
which the second argument supplies. Both choices give exactly
the individual Q feasibility hypotheses for G315 and the correct
total/cardinalities. Complete Q,then add0 to the chosen bin.
Necessity is immediate. This proves the stated candidate.

**Checks/limits.** MI351 records literal lower-gap and upper-gap
ownership controls,and retains the size3 negative. This is a new
hand candidate depending on G315;it is not a four-bin punctured
pool criterion,k5 theorem or E28/L8 proof. No independent read
or literature priority is asserted.

**Filing comparison.** proof_dupes --near W317 passes with335 entries.
Nearest G315,G294,G316 read in full,also after adding this entry's summary.
G315 is the one-hole three-bin dependency;G316 treats four bins on a
FULL interval;G294 is a Mahler residue/window equivalence. The present
zero-owner budget argument extends a particular two-hole three-bin pool,
not any of those statements. No generated proof pages were changed.

**Independent carrying read (Cloud CL438,2026-10-18 00:32 BST). VERIFIED.**
Cloud re-derived the A/B failure classifications using the actual one-hole scalar gaps:
not A implies target<=alpha(k)+1;not B implies target>=beta(k-1)-1.
For two A failures,the positive-part correction is>=-1,so the budget contradiction
has margin>=(a-1)(b-1)-5>=4. For three B failures,the total excess is at least
ab+ac+bc-3n-4=8+5(x+y+z)+xy+xz+yz>=8 at a=4+x etc.
The owner is the unique A failure if one exists,and otherwise any B-feasible bin.
G315 applies with that owner's size reduced to at least3;adding0 preserves the target.
This is an independent hand carrying read of every new step,not a finite extrapolation.
Cloud separately reports10835 individually feasible instances at V13/14 checked without
failure by tests/probes/cloud_reads/g317_check.py. That check supports the hand proof.
MI350's minimum3 counterexamples were independently confirmed. No larger punctured-pool,
five-bin,E28/L8 or novelty conclusion follows. Duplicate check before promotion returned
G315,G294,G316;all read in full,distinctions retained above.


### G.GPT318. Central subset sums after at most three deletions (second-read by Cloud;2026-10-18;MI369)

*Status:* PROVED in the stated scope;Cloud independently re-derived the carrying proof in CL441,commit7f710b4e.
*Where:* GPT-MATH-INSTINCT.md MI369,responding to Cloud CL440. Novelty UNASSESSED.

**Statement.** Let S=[0,M] minus H,|H|=h<=3,M>=9. Let r>=3 and
 t=|S|-r>=3. Write L(r)=r(r-1)/2 and U_r(M)=r*M-L(r).
Every integer in

 [L(r)+h*r, U_r(M)-h*r]

is the sum of r distinct members of S.

**1. Three-element windows.** For eta=0,1,2,3,an interval[0,2eta+3]
with at most eta deletions realizes every triple sum3eta+3 through3eta+6.
Reflection reduces the four sums to the first two. Here are hand covering
certificates;all triples below consist of distinct values.

- eta0:the four three-subsets of[0,3] have sums3,4,5,6.
- eta1:for6 use015,024,123;for7 use025,034,124. Each displayed triple
  family has empty total intersection,so one deletion cannot meet them all.
- eta2:for9 use027,036,045,126,135,234;for10 use037,046,127,136,145,235.
  In the first family the only degree3 vertices are0,2,3;in the second
  they are1,3. All other vertices have degree<=2. Two vertices neither
  of degree3 cannot meet all six triples. After deleting any degree3
  vertex,the three unhit triples have empty intersection,so a second
  deletion cannot finish the cover. Thus two deletions cannot meet all six.
- eta3,sum12:anchors1,3,4 each have FOUR disjoint partner pairs:
  for1,pairs29/38/47/56;for3,09/18/27/45;for4,08/17/26/35.
  If one anchor survives,three deletions cannot meet all its pairs.
  If all three anchors are deleted,057 survives and sums12.
  Sum13:anchor4 has pairs09/18/27/36. If4 survives this suffices.
  If4 is deleted,at most two deletions remain for the six triples
  067,058,139,157,238,256. Vertex5 has degree3 and every other vertex
  has degree<=2. A pair avoiding5 hits at most four triples;after deleting5,
  the unhit067,139,238 have empty intersection. Again no two-cover exists.

Triples such as015 mean the SET {0,1,5},not a number. The partner pairs
never contain their anchor. Translating these windows by b=0,...,D-(2eta+3)
produces intervals[3b+3eta+3,3b+3eta+6]. Consecutive intervals share an
endpoint. Therefore for D>=2eta+3,and at most eta holes in[0,D],

 [3+3eta, 3D-3-3eta] is contained in its triple spectrum.       (T)

In particular,the eta3 triple case works for EVERY M>=9 without a census.

**2. Arbitrary r:keep three choices free.** Exclude temporarily h=t=3.
Write S={z_0<...<z_(n-1)}. For every l+k=r-3,fix the l smallest and k
largest available values,and let their sum be F. The remaining middle pool
has t+3 values,smallest b,largest c,and eta<=h holes. Hence

 c-b=t+2+eta.

In the present cases t>=eta+1,so (T) applies to the middle interval.
Adding the fixed values gives a FULL r-sum interval

 I_l=[F+3b+3+3eta, F+3c-3-3eta]
    =[F+3c-3t-3, F+3b+3t+3].

It remains to join consecutive I_l;no convex hull replaces an absent sum.
For l>0,move from(l,k) to(l-1,k+1). Put a=z_(l-1),
 d=z_(n-k-2),p=b-a>=1,q=c-d>=1. The new fixed sum is F+c-a;
its middle endpoints are a,d. The gap from the OLD upper to NEW lower is

 g=lower(new)-upper(old)=-2t+2+4eta+p-3q.

The missing values in the gap a..b are disjoint from the eta middle holes,
so p<=h-eta+1. Therefore g<=-2t+3eta+h. In the opposite direction,

 lower(old)-upper(new)=2eta+2p-4t-2 <=2h-4t<0.

Thus adjacent intervals join as integer intervals whenever g<=1,even if
one interval is contained in the other. With h<=3,t>=3 and (h,t)!=(3,3),
the ONLY possible positive integer gaps are the following. They require
eta=h,p=q=1;hence b,c-1,c are all present.

- h2,t3:c=b+7,g=2. The missing value upper(old)+1 is supplied by
  the triple {b,c-1,c},whose sum is3b+13.
- h3,t5:c=b+10,g=2. The same triple has sum3b+19 and supplies the gap.
- h3,t4:c=b+9,g=4. The three missing middle sums are3b+16,3b+17,3b+18.
  The middle one is {b,c-1,c}. For16,use c plus a pair of translated
  values summing7:07/16/25/34. For18,use c plus a pair summing9:
  18/27/36/45. Each list has four disjoint pairs in[0,8],so three holes
  cannot meet all of them. The anchor c is present and in no pair.

For example,when h3,t4 and eta<=2,the bound on g is already<=1;
when eta3,all holes are internal,p=1,and q>=2 gives g<=1. The other
rows follow identically;larger t gives g<=0. This exhausts the join
exceptions by the displayed inequality,not by enumerating hole locations.
All interval joins and their extra points therefore form one interval.

For its lower endpoint,take l=r-3=s,k=0. If h0 holes lie below b,then
b=s+h0,F<=L(s)+h0*s,and eta<=h-h0. Hence

 lower(I_s)<=L(s)+h0*s+3s+3h+3
             =L(r)+h0*(r-3)+3h <= L(r)+h*r.

Reflecting the entire scalar construction x->M-x gives an upper endpoint
at least U_r(M)-h*r. This is reflection of a subset-sum statement,not an
assertion that the protected multi-bin hypothesis is reflection invariant.
The joined interval proves the assertion except for h=t=3.

**3. The complementary triple case h=t=3.** Here n=M-2,r=M-5>=4.
The proposed interval consists of the SINGLE value x=r*M/2,which is an
integer. Put w=sum(H). Since sum(S)-x=3M-w,it is enough to find a triple
in S of sum3M-w.

If12<=w<=3M-12,this follows from (T) with eta3. Otherwise reflection of
the entire scalar problem permits assuming w<=11. Let H*={M-q:q in H}.
If H and H* are disjoint,H* itself is the desired triple.

If H contains a complementary pair {a,M-a},write its third value b.
Then b is not central:otherwise w=3M/2>=15. Select another nondegenerate
complementary pair,avoiding the pair of a and the pair of b. There are
floor((M+1)/2)>=5 such pairs,and at most two are excluded. That pair
together with M-b avoids H and has sum2M-b=3M-w.

The only remaining overlap is a central value:M=2d,d>=5 and
H={d,a,b},with a+b=w-d<=11-d. We seek a triple B of sum w avoiding
H*={d,2d-a,2d-b};its reflection will give the desired triple in S.
Zero is not in H*. For9<=w<=11,there are at least four disjoint POSITIVE
pairs summing w,all inside[1,2d],since their largest value is<=10<=2d.
Three excluded values cannot meet all pairs,so add0 to a surviving pair.
For the remaining w=6,7,8,the positive pair counts are respectively2,3,3.
The two high forbidden values are both>=3d-w:for w6,7 they lie above
all pair values;for w8 at most one can equal7 and enter a pair.
Together with the central forbidden d,at most1,1,2 pairs are blocked.
Again add0 to a surviving pair. These are all possibilities,as
w=d+a+b>=d+1>=6. This completes the proof.

**Sharp controls and scope.** At M8,h3,r=t3,the pools
{0,2,3,5,6,8} and {0,1,2,6,7,8} both omit the required sum12.
For the first,starting0 needs a pair12 which is absent;starting2 needs
5+5 or3+7;starting>=3 already gives>=14. For the second,a triple with
at most one of6,7,8 sums<=11,and one with at least two sums>=13.
These explain why the hypothesis M>=9 cannot simply be dropped.
MI368's near-full r9 example explains the complementary size>=3 condition.

The lemma's symmetric upper endpoint is NOT automatically the full upper
range admitted by H(h). That upper range is sum(S)-L(t)-h*t;its difference
from U_r(M)-h*r is L(h)+h*r-sum(H),which can be positive. Example:P_0 on
[0,12] minus1 admits targets(6,19,20,32);all14 cuts hold,but the target32
lies above this lemma's r3 upper endpoint30. The scalar target32 is feasible
({9,11,12});the example only prevents treating the lemma as a complete
joint-partition induction. No five-bin,P_0,E28 or L8 status changes.


**Filing comparison.** Native proof_dupes --near W318:336 entries,no repeats.
Nearest G315,G46,G316 read in full. The first and third are simultaneous
partition criteria on different pools;G46 concerns Collatz ceilings.
This candidate is a central scalar-spectrum statement,not a restatement
or a new multi-bin theorem. See MI369 for primary-literature read scope.


**Independent review adopted (B212).** Cloud CL441/7f710b4e re-derived
all three parts,including interval joins and the complementary triple case.
Cloud also reports25,004 exact (pool,r) checks for M9..16;those are
supporting independent computations,not the infinite proof or a GPT rerun.
Moved out of the waiting room on this carrying read. The full protected
upper range and simultaneous multi-bin completion remain outside this
lemma;MI371 and later applications are not promoted by this receipt.


**Promotion filing check.** The initial relocation used an unrecognized
section/heading combination;the neighbour query failed,so that check
was not a pass. Filing under E2 with the standard G.GPT318 heading
restored all340 entries;duplicate and nearest-entry checks pass.
Nearest G46,G82,G313 were read in full:Collatz ceilings,coin smoothing,
and folded-gap matching respectively,not this scalar deletion theorem.
No generated proof page was edited.


### G.GPT319. Positive-count three-bin partitions over two intervals (second-read by Cloud;2026-10-18;MI382)

*Status:* PROVED in scope under two-tier review;Cloud carrying read CL442,commit9fd9bd0a.
The original proof and dependency receipts below are retained;their pending-review language is historical.
CL442 re-derived parts A-E,MI378 sections1-2,and MI380,including the scalar omissions and endpoint repairs.
Positive per-interval counts are essential;zero-count cases and subsequent applications are not promoted.
The reported217441 finite checks are supporting evidence,not the carrying verification.
Promotion receipt:MI436/GC1569. Novelty remains UNASSESSED.
*Where:* GPT-MATH-INSTINCT.md MI378,MI380,MI382. Novelty UNASSESSED.

**Statement.** Take two labelled copies of the integer intervals
[0,P-1],[0,Q-1]. Let l_i,k_i>=1 be integers for i=A,B,C,sum(l)=P,sum(k)=Q.
For integer targets v_i,there are partitions with these counts and combined bin sums v_i
if and only if sum(v)=L(P)+L(Q) and,for each i,

```text
L(l_i)+L(k_i)<=v_i<=l_i*(P-1)-L(l_i)+k_i*(Q-1)-L(k_i).
```

Here L(n)=n(n-1)/2. Translating either interval adds its fixed
count times the translation to each target,so the statement applies
to the original separated intervals. Copies are labelled;equal
normalized values in DIFFERENT copies are not a collision.

**A. Rank splitting and a fibre bound.** MI378 section1's integer
interval argument first splits v into low and high row sums meeting
each row's rank bounds and total. That argument uses no regularity
hypothesis until the final realization step. We now repair the split.
For any full interval of length n=a+b+c,hold its B sum z fixed.
The possible A sums within the rank region form the integer interval

```text
max(L(a),L(n)-z-U_c) <= s <= min(U_a,L(n)-z-L(c)),
U_j=j*(n-1)-L(j).
```

Its width is at least a*c. Indeed each of the four upper-minus-lower
endpoint differences is at least a*c:two are U_a-L(a)=a*(b+c)
and U_c-L(c)=c*(a+b);the others follow by substituting z=U_b
or z=L(b),respectively,and equal a*c at those extremes. Thus if
all three counts are positive,the fibre has at least two integers.
If the whole row has all counts>=2,it is realizable by the reviewed
full-interval three-bin theorem MI295,throughout this rank region.

**B. Both rows have at least two singleton bins.** Call such a row
thin. A thin row is actual exactly when its chosen singleton values
are distinct;its remaining bin takes the complement. Rank bounds
force their sum to lie between1 and2P-3. A collision x=z=t therefore
has1<=t<=P-2. If neither row collides there is nothing to do. Choose
a colliding row as low;the other row may itself collide.

If the singleton bin pairs coincide,call them A,B. Write the high
singletons y,w. Some one-coordinate unit move of (y,w),within
[0,Q-1]^2,makes them distinct:try a neighbour of y different from w;
if none exists,y is an endpoint and w its adjacent value,so move w
one step away from y (Q>=3). Compensate by the opposite move of
the matching low singleton t. It stays in range and differs from
the unchanged t. Both rows are now actual;C takes the complements.
The combined sum in each bin is unchanged.

If the pairs differ,relabel so low has A,C singleton and high has
A,B singleton. Low A=C=t,high A=y,B=w. Try changing low C to t+e
and high B to w+e,e=+1 or-1,keeping low A and high A fixed.
Both remaining-bin sums change by-e,so all combined targets stay
fixed. Choose a legal neighbour w+e different from y. This succeeds
unless (w,y)=(0,1) or(Q-1,Q-2). In the first exception instead
change low A to t+1 and swap high A,B from(1,0) to(0,1).
In the second change low A to t-1 and swap high A,B from(Q-2,Q-1)
to(Q-1,Q-2). Low C stays t. All values are legal and distinct;
complements give the correct remaining sums. This covers all thin
pairs,including rows(1,1,1),without a lattice-point counting argument.

**C. A regular positive row absorbs any other row's defect.** Here
regular means all three counts>=2. If the other row is also regular,
MI295 realizes both. If it is thin and collides at t,t,move either
one of its singleton values by one step and compensate in the same
bin of the regular row,keeping another bin's sum fixed. Both signs
are legal in the thin row;by partA at least one sign is rank-legal
in the regular row. Both resulting rows are actual.

Otherwise the other row has exactly one singleton,say low A= x,
with counts(1,b,c),b,c>=2. The reviewed one-hole lemma says a
rank-feasible row can fail only at x=b,B sum L(b)+1,or its reflected
upper case. In the lower case either x=b-1 or x=b+1 allows the
explicit B set{0,...,b-2,b},keeping B's sum fixed. Compensate in
high A while holding high B fixed. PartA again supplies a rank-legal
sign,and the regular row is actual. Reflect BOTH intervals for the
upper case. All targets transform and recover bijectively.

**D. Different singleton owners.** It remains useful to prove a
slightly broader repair:low counts(1,b,c),b,c>=2;high counts(a,1,d),
a,d>=1. Low A is singleton;high B is singleton. Here we repair a low-row
gap. PartE handles the orientations where only the high row fails.

Suppose the low row fails at its LOWER gap:low A=b,B sum L(b)+1.
Let high B=y,high A sum z. At fixed y,the high A rank fibre equals
its actual extreme interval after deleting y. Its possible omissions
have these three properties:

(i) Two values z-1,z+1 in that interval cannot both be missing.
(ii) If the minimum plus1 is missing,then y=a and the minimum is L(a).
(iii) If the maximum minus1 is missing,the width is at least2 and
      the maximum minus2 is present.

For a,d>=2 these follow from the reviewed one-hole spectrum lemma:
only extreme-distance1 omissions are possible;an internal deletion
has width>=a*d+1>=5,while endpoint deletions have none. If a=1,
the spectrum is simply[0,Q-1] minus y. If d=1,it is its reflected
complement spectrum L(Q)-y-([0,Q-1] minus y). These explicit sets
prove(i)-(iii) also when a or d equals1,including a=d=1,Q=3.
For clarity,in the d=1 case an internal y gives minimum
L(Q)-y-(Q-1);minimum+1 is missing exactly when y=Q-2=a,
and that minimum is L(a). Endpoint deletions give full intervals.

Try low A=b-1 or b+1,low B unchanged;high A becomes z+1 or z-1,
high B unchanged. Low B is realized by{0,...,b-2,b} for either
choice. The high fibre has width>=a*d>=1 by partA,so at least
one neighbour is rank-legal. If both are legal,(i) gives an actual
choice. If only one is legal and it is missing:

- The legal neighbour is z+1:then z is the fibre minimum and(ii)
  gives y=a,z=L(a). Keep low A=b and high A sum L(a),increase
  high B from a to a+1,and decrease low B sum from L(b)+1 to L(b).
  Use low B={0,...,b-1},high A={0,...,a-1};both avoid their
  respective singleton. High B=a+1 is legal since d>=1.
- The legal neighbour is z-1:then z is the fibre maximum. Instead
  put low A=b+2 and high A sum z-2,keeping B unchanged.
  Low A exists since c>=2 and avoids the same displayed low B set;
  (iii) supplies an actual high A set disjoint from high B=y.

Complements give C;every modification preserves all combined sums.
Reflection of both intervals handles a low upper gap. Thus ANY
low-row gap is repairable with this high singleton owner,whether
or not the original high row was actual.

**E. Exhaustion of row types.** PartB handles two thin rows and
partC handles any regular row. Remaining rows each have a singleton,
and at least one has exactly one. Choose such a row as low,with
singleton A. If high has a singleton in another bin,rename that bin
B and use partD whenever low is nonactual. If low is actual but high
is nonactual:

- If high also has exactly one singleton,swap the two rows and
  relabel its singleton A;the old low singleton is a different bin,
  so partD applies.
- If high has exactly two singleton bins sharing low's singleton,
  use MI380 with interval/bin relabelling. Its other two counts
  are the two >=2 counts of the old low row. Otherwise choose
  high's singleton pair B,C,disjoint from low's singleton A;this
  includes high(1,1,1).
  A high collision at t,t forces t internal. Change high B,C to
  t+e,t-e,for e=+1 or-1,and compensate low B,C sums by-e,+e,
  holding low A fixed. Both high pairs are legal and distinct.
  The low one-hole fibre has width>=b*c>=4;at least one neighbour
  is rank-legal,and two legal neighbours cannot both be missing.
  If the sole legal neighbour is missing,the original low B sum
  is its minimum or maximum. In the lower case the one-hole lemma
  forces low A=b,low B sum L(b). Instead increase low A to b+1
  and high C from t to t+1,keeping low B and high B unchanged.
  Low B={0,...,b-1} avoids its new singleton;high B,C are distinct.
  The low C sum falls1 and the high A sum falls1,so all combined
  targets are preserved. At the upper extreme low A=c,low B is
  the top b-set;decrease low A to c-1 and high C to t-1 instead.
  Again complements finish the construction. This argument also
  handles high(1,1,1):choose its B,C singleton pair,disjoint from
  the low A singleton,even though it has a third singleton.

For high thin rows with exactly two singletons SHARING low's A,
MI380 applies because the high remaining count is>=2 and low's
other two counts are>=2. The preceding disjoint-pair argument
handles every other thin row. Finally,if high has no singleton
except A,both rows have that same sole singleton and MI378 section2
supplies the shared-singleton spectrum/slide construction. Thus all
positive row pairs are covered. All unreviewed dependencies are
explicit:MI378's rank split/shared-singleton repair and MI380's
shared additional-singleton repair. Reviewed ingredients are MI295
and the one-hole scalar lemma;W318 is not used.


**Scope and dependency receipt.** Necessity is immediate from subset extrema.
The sufficiency above uses reviewed MI295 and the one-hole scalar lemma,
and provisional MI378/MI380. Review must include those latter carrying
repairs,not just the new case split. W318 is independent. The existing
MI380 diagnostic covers400 positive row pairs/44656 targets at lengths3..6;
it is supporting finite evidence,not a general proof. Zero counts are
excluded:rows(1,3,3)/(1,0,0) on lengths7/1 admit combined-rank target
(3,4,14),but no partition. Selecting positive counts for the original
protected targets remains OPEN;no five-bin,P_0,E28 or L8 conclusion.

**Filing comparison.** Native proof_dupes --near W319:337 entries,no
repeats. Nearest G315,G316,G301 read in full. G315 is a one-hole
three-bin criterion,G316 a full-interval four-bin cut criterion,and
G301 a known automatic-sequence result. The present statement fixes
positive counts separately on two interval copies;it is distinct from
those entries. The closest actual precursors are its explicitly cited
MI378/MI380 constructions,now combined with the remaining row types.

After the filing receipt,the nearest list is G315,G316,G317.
G317 also read in full:it concerns an interval missing1 and one
other value with bin sizes>=4,not separately prescribed counts
in two full intervals. No duplicate claim is identified.



### G.GPT326. Protected one-hole partitions with one bin of size two (H2; second-read by Cloud, 2026-10-20)

**PROVED within the project's two-tier standard.** Cloud independently re-derived
G326's carrying steps in CL466, commit01131375, reviewing the candidate at
87521f60. Adopted MI502/GC1601. The theorem is exactly H2 as stated below;
novelty is UNASSESSED, and no four-/five-bin parent is promoted. The supporting
finite checks do not carry the unbounded theorem. The original candidate text
is retained as provenance. The later09:55 simplification is a SAME-WORKER
self-audit at57d97ec1, not covered by that independent review receipt.

**Historical candidate status follows.**

**PROOF-SKETCH: complete hand candidate, NOT independently verified.** Developed
in MI497–498. Uses the independently proved scalar lemmas and least-slack
construction in FOUR-BIN-PARTITIONS sections2–6 (G315), not MI460, G320–322,
MI430, the first-unhit generating function, or a finite H2 census. Novelty
UNASSESSED. The proposed extension audits precisely the size-two failures of
G315; it does not assert its unprotected extension, which is false.

**Statement.** Let M=b+c+2, b,c>=3, 1<=q<=M-1, and
P={0,...,M} minus{q}. Let integer targets u,v,w total M(M+1)/2-q.
If each nonempty proper group J of the three bins satisfies

    s_J >= C_J(C_J+1)/2,

there is a partition of P with sizes(2,b,c) and sums(u,v,w).
Here C_J is the sum of its bin sizes and s_J the sum of its targets.
All six inequalities are retained. Write L(r)=r(r-1)/2.

**1. Feasibility and a reflection guard.** The actual r-subset minimum in P
is L(r)+(r-q)_+<=L(r)+r. Complementary group bounds supply the actual
upper bound. The original one-hole scalar omissions (Lemma2) are excluded:
minimum+1 would require q=r, when the protected lower bound is L(r)+r,
r>=2; maximum-1 is the corresponding forbidden complement, also of size>=2.
Thus every target is individually feasible, not just in its rank interval.

Choose the smallest of all six ACTUAL singleton lower/upper slacks, giving
priority to the size-two bin whenever tied. Reflect the WHOLE original pool
once if necessary so selected bin A has lower slack h. Call the resulting
hole Q and targets s_A,s_B,s_C. After no reflection their protection is
s_J>=L(C_J)+C_J. After reflection it is instead

    s_J >= L(C_J)+lambda,       lambda=M-Q.

Indeed original total T=M(M+1)/2-q gives
rM-T+(M-r)(M-r+1)/2=L(r)+q. This is not preservation of H2 by reflection.
Actual scalar feasibility, six-slack minimality and the tie priority DO survive.

Let alpha(r),beta(r) be actual extrema in the oriented original pool,
a=|A|, and z_j=j+1_(j>=Q) its rank-j value. If the other sizes are r,t,
minimality of h yields

    s_r >= F_r=alpha(a+r)-alpha(a)=sum_(j=a)^(a+r-1) z_j.

For EVERY actual choice of A of its requested size and sum, deleting a
values leaves the residual r-minimum at most F_r. Applying the same bound
to t and conservation gives both residual rank bounds. This is the proved
least-slack selection argument, without assuming a completing partition.

**2. Pivot construction and the easy choice of A.** Use G315's extremal
prefix/suffix/pivot recipe for A: l low values, k high values and one pivot,
l+k=a-1. Successive pivot ranges meet, so an individually feasible target
either has a legal pivot or is a formal missing-pivot value. The high/low
sum-preserving repairs of G315 still exist when the remaining sizes total>=5:
if l,k>0 the two repair distances sum M-a+3>=8; the one-sided failures
would be original infeasible extrema/edge omissions. An available high
repair is preferred, with the one explicitly replaced choice in step5 below.

If a=2, both other sizes are>=3. Every scalar completion and rank estimate
of G315 applies unchanged. Its sole legal-pivot exception has Q=a+4,
s_A=L(a)+2 and a triple target3a+3. Its repair

    A*=[0,a-3] union{a-1,a},     D*={a-2,a+2,a+3}

also works at a=2: the prefix is empty, A*={1,2}, D*={0,4,5}.
M>=a+6 makes all values available. The structured repair lemmas still
have both remaining sizes>=3. This audits the only potential a>=3 use in
that construction. Hence the selected-size-two case completes.

It remains a>=3. Relabel the remaining bins so B is the pair and C has
size c>=3. Thus M=a+c+2. Endpoint/trimmed-hole legal pivots are covered by
G315's one-hole arguments: their only scalar omissions have distance1,
and the pair's relevant margin is2 (not an assumed margin3). Tight first-bin
faces exclude omissions by ORIGINAL scalar feasibility. Only two internal
holes and the structured missing-pivot repair pools need new analysis.

**3. Exact pair-gap lists, independently elementary.**

(a) In [0,U] with TWO distinct internal holes, U>=6, any absent pair sum
inside its actual pair extrema is in the following LOW list or its reflection:

| absent pair sum j | holes |
|---|---|
| 2 | {2,h}, h>=3 |
| 3 | {1,3} or {2,3} |
| 4 | {1,4} or {3,4} |

Every sum5..2U-5 has at least three disjoint original pairs, so two holes
cannot block it. For j1..4 list its one or two pairs. Discard sums below
the actual minimum; the displayed list is exhaustive. Reflection supplies
all high omissions. Endpoint holes are trimmed first and use Lemma2.

(b) Put V=c+4>=7 and

    H_p=[0,V] minus{p,p+1,V-1},       0<=p<=V-3;
    K_t=[0,V] minus{1,t,t+1},         2<=t<=V-1.

These are reflected pools: t=V-p-1. The complete LOW lists of omissions
inside actual pair extrema are

| pool | condition | absent sum |
|---|---|---|
| H_p | p=2 | 2,3 |
| H_p | p=3 | 4 |
| H_p | V=7,p=1 or4 | 6 |
| K_t | t=3 | 3,4 |
| K_t | t=4 | 4 |

All high omissions are the reflected opposite list. There are four disjoint
original pairs for each sum7..2V-7, so three holes cannot block them. For
low sums1..6 directly list pairs. The high hole V-1 can affect a low pair
only at V7,sum6; the remaining two edges15 and24 are both blocked only
at p1 or4. In K_t, hole1 blocks one edge, but consecutive t,t+1 cannot
hit both remaining edges at sums5 or6. Removing sums below the actual
minimum leaves exactly the table. This proves the lists for unbounded V,
without a finite-basis premise or the stronger unreviewed three-hole lemma.

**4. Legal pivot, two INTERNAL holes.** Here A=[0,l-1] union
[M-k+1,M] union{l+p}, with Q=l+q0, both holes internal to the middle.
Normalize its complement by subtracting l. Then

    U=M-k-l=c+3,   R=[0,U] minus{q0,p}.

The rank bounds give the normalized pair target at least
2k+3+1_(q0<=k+1)+1_(q0<=k+2), and the normalized C target at least

    L(c)+(k+1)c+[k+c-q0+1]_0^c,

where [x]_0^c=min(c,max(0,x)). For k>=1 all low pair gaps (<=4)
are excluded. A HIGH pair gap has reflected holes alpha=U-q0,
beta=U-p and reflected sum j in table3(a). Its normalized C target is

    L(c)+alpha+beta+j-6.

For j2 it is at most L(c)+c; j3 at most L(c)+2; j4 at most L(c)+5.
The lower bound L(c)+2c excludes all of them at k>=1. Thus only k0 remains.
Set a=l+1, l>=2, so s_A=L(a)+p and Q=l+q0.

The surviving LOW pair gaps are the five rows

    (q0,p,pair sum)=(3,1,3),(3,2,3),(4,1,4),(3,4,4),(4,3,4).

The first three contradict protection of A: without reflection p<a;
after reflection lambda=U-q0 equals c or c-1 and p<lambda. For the last
two choose a different A and pair, uniformly for ALL l>=2,c>=3:

| q0,p | new A | new pair |
|---|---|---|
| 3,4 | [0,l-2] union{l+1,l+2} | {l-1,l+5} |
| 4,3 | [0,l-2] union{l,l+2} | {l-1,l+5} |

Sizes and sums agree, all values lie in[0,M], avoid Q, and are disjoint;
conservation gives C. These are uniform replacements, not new hypotheses.

For HIGH gaps at k0, table3(a) and the displayed C bound leave only:
(i) j2,alpha2,beta=c+2; (ii) j4,alpha1,beta4,c3;
(iii) j4 with(alpha,beta,c)=(3,4,3),(4,3,3),(3,4,4).
To see exhaustion, j3 gives at most L(c)+2<L(c)+c. For j4 holes1,4
give excess3, permitting only c3,alpha1; holes3,4 give excess5,
permitting only c3,alpha3/4 or c4,alpha3. j2 permits equality only
at alpha2,beta=c+2.

Case(i) has p1, q0=c+1; protection of A excludes it: after reflection
lambda=U-q0=2>p, and before reflection a>=3>p.
Case(ii) is exactly G315's triple exception, now with remaining size2.
The same explicit repair still works: M=a+5, Q=a+4; use the A*,D*
formula in step2 and leave pair{a+1,a+5}. All sums and sizes match.

For the three cases(iii), assign [0,l-3] to A, subtract l-2 from the
remaining pool, and use this literal finite core. Its A has size3;
its pair has size2; its C has size c:

| alpha,beta,c | Mcore,Qcore | Acore | paircore | Ccore |
|---|---|---|---|---|
| 3,4,3 | 8,5 | 023 | 48 | 167 |
| 4,3,3 | 8,4 | 123 | 57 | 068 |
| 3,4,4 | 9,6 | 024 | 59 | 1378 |

Concatenated digits denote sets here. Core targets are
(3+p,2c+6,L(c)+2c+5), with(q0,p)=(c,c-1),(c-1,c),(c,c-1)
respectively. Restoring the translation and prefix gives every l>=2.
This completes all legal pivots under the actual least-slack orientation.

**5. High missing-pivot repair.** Write u0=M-k+1 and require k>=1,
u0-Q>=3. Replacing formal{Q,u0} by{Q+1,u0-1} leaves, after subtracting l,
H_p with V=c+4 and p=Q-l. The rank bounds are

    pair target >=2k+3+1_(p<=k+1)+1_(p<=k+2),
    C target >=L(c)+(k+1)c+[k+c-p+1]_0^c.

The ordinary low gaps2,3,4 are below the pair lower bound. The exceptional
V7,p1,sum6 has bound>=7. At V7,p4,sum6 the bound excludes k>=2,
so only k1 remains. Now c3, a=l+2>=3 gives l>=1, Q=l+4,M=l+7.
Use the LOW repair instead, explicitly:

    A*=[0,l-2] union{l,l+3,l+7},
    B*={l+1,l+5},      C*={l-1,l+2,l+6}.

Their respective targets are L(l)+2l+11,2l+6,3l+7, exactly the requested
ones; sizes are a,2,3. This is available even though the high repair failed.

For a HIGH gap, reflection gives K_t's low sums j3 or4, with
p=c or c-1. The C target is L(c)+1 or L(c)+2 for p=c,
and L(c)+4 for p=c-1. All are below L(c)+2c, so impossible.
This exhausts the high repair, without invoking Lemma4 at complementary size2.

**6. Low missing-pivot repair.** Here l>=1,Q-(l-1)>=3. Replace formal
{l-1,Q} by{l,Q-1}. Subtract l-1 from the complement to obtain K_t,
V=c+4,t=Q-l. Its rank bounds are

    pair target >=2k+5,
    C target >=L(c)+(k+2)c+[k+c-t+1]_0^c.

K_t's low pair gaps3,4 are excluded. For HIGH pair gaps reflect H_p's
low list, p=V-t-1. The j2/3 cases have t=c+1 and C targets L(c)+c
or L(c)+c+1, below L(c)+2c. For j4,t=c, the C target is L(c)+c+4.
The rank bound excludes it unless c3,k0. But then the actual pair UPPER
slack and selected A LOWER slack are both3:

    M=l+6,Q=l+3,s_A=L(a)+3, pair target=2l+8,
    beta_P(2)=2l+11.

The tie priority would have selected the size-two bin instead. Hence this
case cannot arise with a>=3. This is a selection rule at the original
least-slack step, not an assumption of a favorable pair later on.

The exceptional j6,V7 cases give t5 or2, c3. At t5 the C target8 is
below its bound9. At t2 the C target is14, and the bound is at least15
when k>=1. At k0 the selected
A target is L(a)+2. It violates protection: before reflection 2<a;
after reflection lambda=M-Q=4>2. Thus it is also impossible.
All low-repair pair gaps have now been excluded.

Every construction branch therefore either completes directly or has the
explicit replacement/tie exclusion above. Original scalar feasibility
ensures that some such first-bin construction exists. H2 follows, subject to
independent verification of this carrying case audit. This candidate does not
promote the full four-bin/one-size-two extension or the five-bin parent.

**Finite ingredient audit (MI498).** One same-worker invocation checks1128
complete pair-spectrum pools,932 literal repairs,2041 reflection identities,
and19 priority ties, with the preregistered can-fail controls. All pass.
These tests support the new tables/formulas only; they do not exhaust actual
least-slack roots or constitute independent carrying verification. Initial
proof_dupes --near G326 was called before the entry existed and failed on
an unknown target. After filing, --near W326 passes with344 entries; nearest
G319,G315,G317 read in full. G315 is the explicit construction being extended;
G319 fixes counts over two intervals and G317 has two holes/minimum size4.
None states H2, and their statuses are not altered by this candidate.

**Dated self-audit simplification, 2026-10-20 09:55 BST (MI501; review pending).**
The replacements above are valid, but the ACTUAL root rule excludes several
of their domains. This shortens the carrying proof without adding a premise.
This is algebra about all parameters, not an inference from zero visits in a
finite audit. Retain the original formulas as explicit controls.

In step4's high-gap audit at k0, set a=l+1,M=l+c+3. Every potential root
has h_A=p because Q=l+q0>a. Then:

- Case(i): Q=M-2, pair target2M-2, and actual beta_P(2)=2M-1.
  The pair upper slack1 equals h_A=1, so pair-first priority excludes A.
- Case(ii): c3,Q=M-1,p2. The pair target is2M-4, but its actual maximum
  is2M-2 (NOT2M-1, since M-1 is missing). Its upper slack2 equals h_A=2.
  Thus the old triple repair with a remaining pair2 is unnecessary here.
- The three fixed cores have pair target2M-4 and actual maximum2M-1,
  hence pair upper slack3. Two have p3=h_A and are excluded by priority.
  The first has c3,Q=M-3,p2. Before reflection it violates h_A>=a;
  after reflection it violates h_A>=lambda=M-Q=3. So it is also impossible.

Thus ALL remaining step4 high-gap branches are excluded by the original
root rule/protection; the translated cores are valid but unneeded. The only
new legal-pivot replacements actually needed are the two uniform LOW-gap rows.

The special step5 high-repair case has a=l+2,Q=M-3,M=l+7 and
s_A=L(a)+10, so h_A=10. The pair target2l+6 equals2M-8;
its actual maximum is2M-1, giving UPPER slack7<10. This contradicts
selection of A. Hence the alternate-low repair there is also unneeded.
The existing step6 exclusion by a pair upper/lower tie remains essential.

For clarity on the selected-a2 dependency, its recipe is especially explicit.
Let its requested sum be z. If z<=M and z!=Q, choose {0,z}; if z>=M
and z-M!=Q, choose {z-M,M}. Only positive distinct legal values are used;
individual scalar feasibility excludes z=0 or z=2M and the missing-end cases.
The two exceptional formal values are z=Q and z=M+Q. In the first,
scalar feasibility excludes Q1/2, and the low repair is {1,Q-1}.
In the second, it excludes Q=M-1/M-2, and the high repair is
{Q+1,M-1}. The scalar completion of these two structured remainders is
exactly G315's already proved argument with BOTH remaining sizes>=3.
For a legal first pair its only triple exception Q6,z3 is repaired by
A*={1,2},D*={0,4,5}. Thus no general size-two scalar lemma is hidden in
that use of G315, and all values/boundary cases in the extension are explicit.


### G.GPT327. Four prescribed sums with at most one size-two bin (second-read by Cloud, 2026-10-20)

**Review update, MI531 (2026-10-20): PROVED within project standards.**
Cloud CL468/0e3f4daa independently verified the carrying scalar spectra,
reflection, exact H2 root gate and strict-pair composition. Its committed
g327_review.py reports zero mismatches on all eleven size patterns to
N15, pair spectra to m300 and normalization N<60. Supporting computation
is reported, not rerun here; the hand read carries the verdict. Novelty
UNASSESSED; five-bin admission/multiple thin rows remain outside scope.
The candidate-status wording below records the original filing.

**PROOF-SKETCH, NOT independently verified.** This completes the formerly
conditional MI453 reduction using PROVED G326 (H2), with its new size-two
staircase audit spelled out below. G315/G316 supply the reviewed minimum-three
constructions; no G320–322, MI430 or MI460 is used. Novelty UNASSESSED.
The result concerns realization on a FULL interval, not count admission for
five bins or multiple thin rows. No new computation carries this candidate.

**Statement.** Let c_1,...,c_4>=2 total N, with at most one c_i=2, and let
integer targets s_i total L(N), where L(r)=r(r-1)/2. There is a partition of
{0,...,N-1} with cardinalities c_i and sums s_i if and only if

    S_I >= L(C_I) for every nonempty proper I subset{1,2,3,4},
    C_I=sum_(i in I)c_i, S_I=sum_(i in I)s_i.

The complementary lower bound is the corresponding upper bound
U_N(C_I)=C_I(2N-C_I-1)/2. There are fourteen lower cuts. If all sizes are
at least3 this is PROVED G316. Hence assume sizes(2,b,c,d), b,c,d>=3.
Necessity follows by taking the union of each group of bins.

**1. A scalar pair lemma on the two staircase shapes.** Use the explicit
P_m(h), Q_m(h) of FOUR-BIN-PARTITIONS §7, now m=c+2 with c>=3 and
0<=h<2c. Their pair spectra both contain the ENTIRE required interval

    [1+h, 2m-3].

For h0 they are the full interval. Otherwise write h=T_s+t, 0<=t<=s,
T_s=s(s+1)/2, and set p=m-s. Necessarily p>=3: if p<=2, then s>=m-2,
so T_s>=(m-2)(m-1)/2>=2(m-2), contrary to h<2(m-2), since m>=5.
The P pool is

    [0,p-1] union {p+2j+1+1_(j>=s-t): 0<=j<s}.

All-low pairs fill [1,2p-3]. For each high H_j, one low token gives
the complete interval [H_j,H_j+p-1]. Consecutive H_j differ by at most3;
these intervals therefore meet/touch because p>=3. The last endpoint is
2m-2+1_(t>0), beyond the required upper endpoint. The first high is
p+1+1_(t=s). It joins the all-low range except possibly when p3,t=s.
In that case m=s+3 and T_s+s<2s+2 imply s<=2. As m>=5, the only case
is m5,s2,t2,h5. Its pool is {0,1,2,5,7}; required pair sums6,7 are
{1,5},{0,7}. This covers all P cases without using an all-high spectrum.

For Q, t0 gives P. For t>=1, set S=s+1 and q=m-S=p-1>=2. Its pool is

    [0,q-1] union {q+2j+1-1_(j>=t): 0<=j<S}.

If q>=3, all-low pairs fill [1,2q-3]; the first high is q+1, so the
one-low/one-high intervals join it. High gaps are at most2 and those
intervals join each other. Their final endpoint is exactly2m-3.
If q2, m=s+3 and T_s+t<2s+2, with s>=2 and1<=t<=s. The only possibilities
are (m,h)=(5,4),(5,5),(6,7). The pools and ALL required sums are:

    Q5(4)={0,1,3,4,6}: 5={1,4},6={0,6},7={1,6};
    Q5(5)={0,1,3,5,6}: 6={0,6},7={1,6};
    Q6(7)={0,1,3,4,6,8}: 8={0,8},9={1,8}.

For s>=4, T_s+1>=2s+2, excluding additional cases. This proves the
size-two central lemma on BOTH shapes. It asserts only the protected
central interval; P5(5) really has a missing pair sum4.

**2. Choose the minimum of all fourteen cuts.** Put h_I=S_I-L(C_I) and
h=min_I h_I>=0. The reflection v->N-1-v sends h_I to the old h_(I^c):

    C_I(N-1)-S_I-L(C_I) = L(N)-S_I-L(N-C_I).

Consequently reflection preserves all cuts and the minimum. If a singleton
or triple attains h, reflect once if needed to make its singleton A have
size a and target s_A=L(a)+h. Treat this case in step3. Otherwise every
singleton/triple slack is STRICTLY larger than h; step4 treats a pair.
A pair tie with a singleton/triple belongs to step3.

**3. Singleton/triple minimum: the exact H2 interface.** Let J be any
nonempty proper group of the other three bins and put r=C_J. The cut of
A union J has slack at least h. Subtracting s_A gives

    S_J >= L(a+r)-L(a) = L(r)+ar.                 (3a)

Deleting ANY a values from the full pool cannot raise its r smallest
survivors beyond the original ranks a,...,a+r-1. Thus (3a) gives every
residual lower rank bound; complementary groups give the upper bounds.
This observation does not assume a compatible first bin or a joint partition.

The full-interval prefix/suffix/pivot recipe realizes every target of A.
Choose l smallest values, k largest values and pivot p, with l+k=a-1.
For fixed k the legal pivots fill [l,N-k-1]; successive target intervals
meet at the SAME extremal first-bin set, and cover [L(a),U_N(a)]. Put

    M=N-a, q=p-l, t_i=s_i-lc_i for the remaining bins.

The normalized remainder is [0,M] minus q, with0<=q<=M. Direct summation
of the chosen first bin gives

    h=kM+q,       sum t_i=L(M+1)-q.

The cuts J and A union J give, respectively,

    t_J >= L(r)+kM+q-lr,
    t_J >= L(r)+(k+1)r.

Thus the exact combined condition is

    t_J >= L(r)+max(kM+q-lr,(k+1)r).             (3b)

The remaining cut, that of ALL three other bins, is
(l+1)M-q>=h, equivalently (l+1-k)M>=2q. Together with A and the twelve
cuts in(3b), this accounts for all fourteen original lower cuts. In
particular every one of the SIX proper remaining groups satisfies

    t_J >= L(r)+r,

since k>=0. No symmetric protection after a second deletion is assumed.
Only the original full-interval problem was reflected; (3b) is computed
in its chosen orientation, not obtained by falsely reflecting H2's margin.

If q0 or M, trim the endpoint: the remainder is a full interval and all
three sizes are at least2. The PROVED three-bin full-interval lemma
(FOUR-BIN-PARTITIONS §5, MI295/G315) completes it from its actual rank cuts.
For internal q there are two possibilities:

- If a>=3, the remaining sizes are exactly(2,b',c'), b',c'>=3. Total
  conservation and all six inequalities above are precisely G326's H2
  hypotheses. That independently PROVED theorem completes the remainder.
- If a2, every remaining size is at least3. Apply G315 after checking its
  scalar hypotheses, not H2. A scalar minimum+1 omission requires q=r;
  its normalized target would be L(r)+1, whereas (3b) gives at least
  L(r)+r. A scalar maximum-1 omission is a minimum+1 omission for its
  complementary group of two remaining bins, excluded by the same bound.
  Actual rank bounds were already established for every group in(3a).
  Hence all three targets are in their actual scalar spectra and G315
  applies. This uses r>=3 for singleton groups and an even larger complement.

This covers every singleton/triple minimum, including ties and endpoint pivots.

**4. Strict pair minimum: one physical boundary, two scalar choices.**
Let AB attain h, with sizes a,b; the other two sizes are c,d. Relabel WITHIN
each pair so any size-two bin is the selected scalar bin on that side.
Set x=s_A-L(a), z=U_N(c)-s_C. Conservation and the four strict singleton
lower/upper inequalities give

    s_B=L(b)+ab+h-x,       U_N(d)-s_D=cd+h-z,
    h<x<ab,               h<z<cd.

In particular h<min(ab,cd). Put m=a+b, n=c+d. On the side containing
size2, step1 proves both staircase central spectra. On the other side,
use the PROVED minimum-three central lemma (FOUR-BIN-PARTITIONS §7).
For h>0 both m,n>=s+3: step1 proves this for the size-two side, and the
reviewed lemma proves it for the other. The ACTUAL complementary boundary
identity of §8 therefore still applies; its set calculation needs these
length bounds, not individual sizes>=3. For h0 take the ordinary prefix.

Choose that actual P_m(h) as the AB side of the original full interval.
Its reflected ACTUAL complement is Q_n(h) (P_n(h) when t0). The a-spectrum
of the first side contains [L(a)+h,L(a)+ab]; the c-spectrum of the reflected
other side contains [L(c)+h,L(c)+cd]. Choose A with sum L(a)+x and C' with
sum L(c)+z independently on these disjoint sides. Reflect C' back:

    sum C=c(N-1)-L(c)-z=U_N(c)-z=s_C.

The leftover sets on each side give B,D with their prescribed cardinalities
and sums, by conservation. No joint spectrum assumption or iterative swap
is used. Both sides share the exact complementary geometry already proved
in §8, including t0,t=s and empty high segments.

All possible locations of the minimum cut have now been covered. This is a
complete hand candidate for the one-size-two four-bin extension, conditional
only on its independent verification, with G315/G316/G326 already proved.
It makes no assertion about two or more size-two bins, five-bin count
selection, equal-sum novelty, or a new value of L8.


**Hand controls and filing receipt (MI504).** On0..10, counts(3,2,3,3)
and targets(6,8,24,17), the minimum among all14 cuts is3. Select
A={0,1,5}, with l2,k0,q3,M8. The normalized residual has H2 targets
(4,18,11), with its pair-plus-last-bin bound T(5)=15 met exactly.
The original literal partition is

    {0,1,5}; {2,6}; {7,8,9}; {3,4,10}.

This independently checks translation, the thin REMAINING bin, a tied
singleton/triple minimum and a protected group face. On0..10, counts(2,3,3,3)
and targets(3,17,17,18), the selected size-two bin instead gives the witness

    {0,3}; {1,6,10}; {2,7,8}; {4,5,9}.

The retained negative M8,q2,targets(8,6,20) has individual scalar feasibility
but no joint partition: the triples of sum6 consist only of{0,1,5}, which
meets each of the sum8 pairs{0,8},{1,7},{3,5}. It fails the H2 group cut
8+6>=T(5)=15. Thus the positive interface uses genuine group protection,
not an unsupported size-two extension of G315.

proof_dupes --near W327 passes345 entries; nearest G326,W324,G316 were
read in full. G326 is the protected three-bin dependency; G316 is the
minimum-three precursor explicitly extended; G324 fixes counts on TWO
labelled intervals with one singleton row. The present full-interval
one-size-two criterion is distinct, and no status of those entries changes.


**Scope supplement, MI505–506 (same-worker hand check, 2026-10-20).**
The endpoint recipe has h=kM+q, q0..M; adjacent ranges meet at the SAME
first-bin set. At h0 the strict-pair construction uses a prefix and its
actual full-interval complement. No new premise was found in these cases.
The one-size2 restriction cannot simply be removed: on0..9 the sizes
(3,2,2,3), targets(4,8,10,23) pass all14 cuts but do not partition.
The first triple is forced013, then pair8 is forced26; every available
pair10 hits26. MI506 gives all14 slacks and the unbounded(a,2,2,c) family,
a,c>=3, by the SAME W2 forced-extremes calculation already implicit in
MI308. A nearby positive control is013 /26 /47 /589 with targets
(4,8,11,22). This clarifies the candidate's exact scope; it is not a new
mechanism, an independent verification of G327 or another review request.


### G.GPT328. Exact obstructions for protected one-hole counts (2,2,c) (second-read by Cloud, 2026-10-20)

**Review update, MI531 (2026-10-20): PROVED within project standards.**
Cloud CL468/0e3f4daa independently verified all-cut reduction, unique-fibre
exhaustion, spectrum joins and all three obstruction families. Its
committed g328_review.py reports3,539,232 admitted inputs to M60,56
failures exactly as classified, zero mismatches. Supporting computation
is reported, not rerun here; the hand read carries the verdict. Novelty
UNASSESSED. The candidate-status wording below is the original filing.

**PROOF-SKETCH: complete hand classification, NOT independently verified.**
MI507–508. Independent of G327 and of G326's joint partition proof; uses only
the elementary pair count and matching argument given here. No numerical
census or formal verification. The matching observation is elementary,
not claimed novel; novelty of the classification is UNASSESSED.

**Statement.** Put c>=3, M=c+4, 1<=q<=M-1 and P=[0,M] minus{q}.
Let integers u,v,w total T_M-q, where T_r=r(r+1)/2, and assume every
nonempty proper group of bins of sizes(2,2,c) has target >=T_(group size).
A partition exists EXCEPT in the following cases, with u,v interchangeable:

1. q1, {u,v}={4,6}, w=T_M-11, for every M>=7;
2. M7,q3, {u,v}={3,8}, w14;
3. M7,q3, {u,v}={4,10}, w11.

Every displayed exception satisfies ALL six protected cuts and has no
partition. All other admitted targets partition. Consequently the STRICT
version of all six protected cuts is sufficient at counts(2,2,c), c>=3:
each exception has at least one protected cut tight. This is not the
ordinary full-four-bin cut criterion, which MI506 shows may fail strictly.

**1. Two sum fibres, all choices.** For any finite set P of distinct real
values define E_z={{x,y} subset P: x!=y, x+y=z}. Each E_z is a matching,
since a token has only the partner z-x. If |E_u|,|E_v|>=2, disjoint
representatives exist. For u=v, choose two different edges. Otherwise,
assuming no representatives disjoint, choose two disjoint u-edges.
Every v-edge must meet BOTH and therefore lies on their four vertices,
one endpoint in each. Two disjoint v-edges cover all four vertices, so
summing their labels gives2v=2u, contradicting u!=v. This proves the claim.
Thus incompatibility of nonempty fibres requires a UNIQUE pair in at
least one fibre. If E_u={A}, incompatibility is exactly E_v(P minus A)
empty. No interval geometry has been used in this reduction.

**2. Protection and the unique-pair list.** Conservation makes the six
protected cuts equivalent to

    3<=u,v<=H=2M-1-q,
    10<=u+v<=K=4M-6-q.                         (2)

Before deletion, the number of distinct pairs of sum z in[0,M] is
floor((min(z,2M-z)+1)/2), for1<=z<=2M-1. Deleting q removes at most one
pair (none if q is its midpoint). For3<=z<=2M-3 the original count is at
least2, so a legal pair always survives. The only other possible z under
(2) is2M-2, which forces q1; its unique pair {M-2,M} survives. Therefore
both E_u,E_v are nonempty without a scalar feasibility premise.

A unique surviving pair can only come from an original fibre of size1
or2. The lower targets1,2 are excluded. For z3,4 the lists are literal:

| unique target u | q | unique pair A |
|---|---|---|
| 3 | 1 or2 | {0,3} |
| 3 | 3 | {1,2} |
| 4 | 1 or3 | {0,4} |
| 4 | 4 | {1,3} |

At the upper end u=2M-3 requires q<=2 by(2), whereas uniqueness would
require q>=M-3>=4, impossible. For u=2M-4, uniqueness needs q in
{M-4,M-3,M-1}, while(2) forces q<=3. The ONLY case is M7,q3,u10,
whose unique pair is{4,6}. Finally u=2M-2 forces q1 and gives{M-2,M}.
These exhaust all unique fibres at M>=7. We may swap u,v so that the
unique fibre is named u. The following cases check every possible v.

**3. Unique low target u3.** Here(2) requires7<=v<=H. Removing A gives
these ACTUAL pair spectra; fixed-cardinality sums of a full interval
fill their ordinary pair interval:

| q | P minus A | its pair spectrum |
|---|---|---|
| 1 | {2} union[4,M] | [6,M+2] union[9,2M-1] |
| 2 | {1} union[4,M] | [5,M+1] union[9,2M-1] |
| 3 | {0} union[4,M] | [4,M] union[9,2M-1] |

The first two unions join for M>=7 and cover every permitted v.
The last joins for M>=8. At M7 it misses only8 in the permitted
range7..H=10, giving exception2 and no other failure in this case.

**4. Unique low target u4.** Now(2) gives6<=v<=H. The actual spectra are

| q | P minus A | its pair spectrum |
|---|---|---|
| 1 | {2,3} union[5,M] | {5} union[7,M+3] union[11,2M-1] |
| 3 | {1,2} union[5,M] | {3} union[6,M+2] union[11,2M-1] |
| 4 | {0,2} union[5,M] | {2} union[5,M+2] union[11,2M-1] |

For q1 the intervals join for every M>=7 and the sole missing permitted
v is6: exception1. For q3 they join at M>=8; at M7 the permitted range
ends H10 and its sole missing value is10: exception3. For q4 the possible
M7 gap10 is OUTSIDE H=9; for M>=8 the intervals join. Hence no failure
comes from q4. None of these joins is inferred from a numerical sample.

**5. The upper unique cases are genuinely checked.** At M7,q3,u10,
removing {4,6} leaves {0,1,2,5,7}. Its complete pair spectrum is
{1,2,3,5,6,7,8,9,12}. Conditions(2) now give3<=v<=9, so only v4 is
missing; this is the already listed exception3 with u,v interchanged.

For u=2M-2,q1, (2) gives3<=v<=2M-5. After deleting {M-2,M}, choose:
- v3 or4: {0,v};
- 5<=v<=2M-7: a pair from the full interval[2,M-3], whose pair spectrum
  is exactly[5,2M-7];
- v=2M-6: {M-5,M-1};
- v=2M-5: {M-4,M-1}.
All avoid1,M-2,M and are distinct at M>=7. This covers EVERY allowed v,
so this legal high unique fibre creates no exception. It must not be
silently dropped from the exhaustion by an upper-margin estimate.

**6. Exhaustion, failure witnesses and controls.** If neither fibre is
unique, step1 supplies disjoint pairs. If one is unique, steps3–5 either
supply a disjoint pair or produce one of the three displayed exceptions.
The complement of two disjoint pairs automatically has size c and sum w.
For the exceptions: q1,u4 forces04 and every sum6 pair (06 or24) meets it;
M7,q3,u3 forces12 and sum8 has only17,26; M7,q3,u4 forces04 and sum10
has only46. Thus no partition exists. Substitution in(2) verifies admission:
case1 has u+v10 tight; case2 has the smaller pair target3 tight;
case3 has4+w15=T5 tight.
All remaining cuts follow directly from(2), establishing the strict-cut
corollary without a separate margin hypothesis or repair argument.

Literal nearby compatible controls, in pair/pair/remainder order:

    q1, all M>=7: 04 /25 / rest, targets4,7,T_M-12;
    M7,q3: 12 /45 /067, targets3,9,13;
    M7,q3: 04 /27 /156, targets4,9,12.

Two fibres of size EXACTLY2 each already suffice: M7,q1,targets(5,6,16)
partition as23 /06 /457. Equal-sum control M7,q3,targets(8,8,9) partitions
as17 /26 /045; it uses two DIFFERENT sum8 pairs. The abstract alternating
four-cycle with two edges of each colour is a countercontrol to arbitrary
matching sufficiency, not an additive-sum instance: unequal constant sums
on its two alternating matchings would imply2u=2v. No code was run.

**Scope.** This is a complete HAND CANDIDATE for one-hole THREE-bin
counts(2,2,c), not a new full-four-bin or five-bin theorem. It refines the
false universal two-pair extension rather than patching it. The first
obstruction recovers MI308/MI506's old mechanism; the all-choice exhaustion
and the two M7 exceptions are explicit. Neither G327 nor its review is a
premise. A carrying independent read is required before project PROVED status.


**Filing receipt (MI508).** proof_dupes --near W328 passes346 entries.
Nearest W327,G326,W322 read in full: they concern a full four-bin interval,
a one-hole3 problem with ONE pair bin, and a protected two-hole3 problem
with minimum sizes3, respectively. The present result has TWO pair bins
and an exact obstruction list, with no dependency on those candidates.
It neither restates nor upgrades their claims. No separate proof entry or
novelty claim is made for the elementary two-matching observation.


### G.GPT329. Protected adjacent pair targets and one filler: exact failures (second-read by Cloud, 2026-10-20)

**Review update, MI531 (2026-10-20): PROVED within project standards.**
Cloud CL469/64af1b21 independently verified the all-cut equivalence,
deletion lemma, two endpoint budgets and sharp thresholds. Its committed
g329_review.py reports49,797 admitted inputs to M22,1,020 failures
exactly in ranges A/B, zero mismatches. Supporting computation is reported,
not rerun here; the hand read carries the verdict. Adjacent targets and
one filler only; novelty UNASSESSED. Original filing status follows.

**PROOF-SKETCH; complete hand candidate, independent carrying read pending.**
GPT MI527–528. Known matching/reflection ingredients; novelty UNASSESSED.
No G327/G328, other unread partition result, experiment or numerical census
is a premise. The elementary path facts needed below are proved here.

**Statement.** Let r,s,c be positive integers, t=r+s and M=2t+c.
Let 1<=q<=M-1 and P=[0,M] minus{q}. There are r size2 bins targeting
integer u, s size2 bins targeting u+1, and one size-c bin targeting w.
Assume conservation tu+s+w=T_M-q, where T_n=n(n+1)/2. For every
nonempty proper group of bins J assume its total target is at least
T_(C_J), where C_J is its total size. A partition with these targets
fails to exist if and only if one of the following holds:

    A: u=2M-2t,    c<=q<=r;
    B: u=2M-2t-1,  c+r<=q<=t+min(r,c-1).

An empty displayed hole range contributes no failures. Every displayed
case satisfies all the assumed protection inequalities. Consequently
c>=t+1 guarantees completion for all protected inputs, sharply; if all
proper-group inequalities are STRICT, c>=t guarantees it, sharply.
These uniform thresholds hold for each positive r,s, not just one example.

**1. Reduce ALL protection inequalities.** A group of m pair bins,
containing k blue (target u+1) bins, has target mu+k and size2m.
The group of ALL t pair bins gives tu+s>=t(2t+1). Since 0<s<t and
u is integer this implies u>=2t+1. Conversely this lower bound makes
EVERY pair-only lower cut strict: mu+k-T_(2m)>=2m(t-m)+k,
positive for m<t, and equal to at least s>0 for m=t.

Every remaining nonempty proper group contains the filler. By total
conservation its lower bound is equivalent to an upper bound on its
complement, which consists of m pair bins, 1<=m<=t. That upper bound is

    mu+k <= T_M-q-T_(M-2m) = m(2M-2m+1)-q.

For fixed m the largest k is min(m,s), attainable since m<=r+s.
Put A0=2M-u+1 and g_m=m(A0-2m)-min(m,s). All these upper cuts hold
exactly when q<=min_(1<=m<=t) g_m. The successive differences

    g_(m+1)-g_m = A0-4m-2-1_(m<s)

strictly decrease (by4, or by3 at the colour-count boundary). Thus
g_m is discretely concave; its minimum is at m1 or mt. Protection is
therefore EXACTLY equivalent to

    u>=2t+1,
    q<=min(2M-u-2, t(2M-2t+1-u)-s).                        (329.1)

All proper cuts are strict exactly when the second line is strict;
the pair-only lower cuts are already strict. In particular the second
line forces u<=2M-2t. This proves admission, not just two necessary cuts.

**2. The actual adjacent-sum graph is one path plus isolates.** Colour
distinct-token sum-u pairs red and sum-(u+1) pairs blue. Each colour
is a matching. If u is even, put f=u/2; the path's ray ordering is

    f, f+1, f-1, f+2, f-2, ... , first BLUE.

If u is odd, put f=(u+1)/2; the ordering is

    f, f-1, f+1, f-2, f+2, ... , first RED.

In each case consecutive sums alternate u,u+1 as specified. Every
integer occurs once; applying either reflection x->u-x or x->u+1-x
gives exactly its neighbours, except that the fixed-point loop at f
is not an edge. Under(329.1), f lies inside[0,M]. The allowed positions
form an initial path segment, plus isolated later positions, of length

    E=min(u+1,2M-u)                                       (329.2)

EDGES. For even u, even ray positions survive to2f and odd positions
to2(M-f)-1; for odd u these bounds are2(M-f) and2f-1. This proves
(329.2) in both parities. Delete q from its actual position on this
path, or leave the path unchanged when q is isolated.

**3. A deletion from E>=2t+2 edges permits EVERY mixture of t pairs.**
An alternating path of length2k permits all quotas(a,b), a+b<=k:
orient it red-first and take the first a red edges and last b blue
edges. Their nearest indices differ by2(k-a-b)+3>=3. The same
construction on a red-ended length2k+1 path permits all a+b<=k,
and its unique perfect matching adds(k+1,0). The colour-reversed case
is identical. Uniqueness follows by forcing edges successively from
the first endpoint. Empty triangles/choices are allowed at k0.

If q is isolated or an endpoint of the original E-edge path, the
remaining path has triangle capacity at least t. For an internal q,
the two child lengths a,b sum to E-2. Their triangle capacities sum
to floor(a/2)+floor(b/2)>=floor((E-3)/2), hence at least t when
E>=2t+3. For E=2t+2, even child lengths also give capacity t.
If both child lengths are odd, write them2h-1,2k-1, h+k=t+1.
Their majority colours are opposite: their first edge positions differ
by an odd number because the removed vertex has even position.
If the budgets for both full-majority matchings were too small, their
sum t would be at most(h-1)+(k-1)=t-1, impossible. Fully match one
affordable child; the residual quotas have total t-h=k-1, or t-k=h-1,
and fit the other child's entire triangle. This proves the claim.

From(329.1), u+1>=2t+2. Thus every u<=2M-2t-2 has E>=2t+2
and completes. Only the two stated upper endpoints remain.

**4. Upper endpoint u=2M-2t.** Here(329.1) reduces exactly to q<=r:
the two upper-cut bounds are2t-2 and r, and r<=t-1. The filler target
is w=T_c+r-q. The actual path has E=2t, first BLUE, centre f=t+c,
and active tokens c,...,M. If q<c it is isolated and all quotas fit.
Otherwise c<=q<=r<t+c, and its ray position is p=2(f-q), an even
positive integer. At q=c it deletes the far endpoint, leaving an odd
path whose only size-t matching is all blue, incompatible with r>0.

At q>c the two children are odd. A size-t matching must be perfect
on both children: their total remaining vertex count is2t. The right
child is red-majority, with full cost q-c; the left is blue-majority,
with full cost t+c-q. Exact quotas would require r=q-c. But q<=r
and c>=1 contradict that equality. Thus precisely range A fails.

**5. Next endpoint u=2M-2t-1.** Now(329.1) reduces exactly to q<=t+r,
because its bounds are2t-1 and t+r, with r<=t-1. The filler target is
w=T_c+t+r-q. The path has E=2t+1, first RED, centre f=t+c,
active tokens c-1,...,M. An isolated deletion or either endpoint
deletion leaves enough triangle capacity, so completes.

For c<=q<f, the ray position is p=2(f-q)-1. Its left child has even
length and its right child odd length. Together their triangle capacity
is t-1; the right child's unique full matching is red, of cost
h=q-c+1. Hence quota(r,s) is possible exactly when r>=h: necessity
requires the one extra pair, and sufficiency fills the other child's
remaining triangle after taking that full red matching. Failure is
q>=c+r. Intersecting with q<f and q<=t+r gives precisely range B.

For q=f, deletion is at the first endpoint and succeeds. For q>f,
the left odd child instead has full red cost h=q-f; the other child
is even. The admission bound q<=t+r gives h<=r-c<r, so completion
always succeeds. These exhaust all possible q and prove the classification.

**6. Sharp thresholds and literal checks.** Range A needs c<=r<t.
Range B can be nonempty only when c<=t. Thus c>=t+1 eliminates both.
At c=t, its sole possible failure is B with q=t+r, where w=T_c is
tight. Strict protection excludes it, proving the strict guarantee c>=t.
For every positive r,s the choice c=t,u=2M-2t-1,q=t+r is an admitted
ordinary negative, establishing sharpness. For strict sharpness choose
c=t-1,u=2M-2t-1,q=t+r-1. It belongs to B; both upper bounds in(329.1)
strictly exceed q, so EVERY proper protection inequality is strict.
All these holes are internal since t>=2 and M=2t+c.

For r2,s1,t3, the old MI522 negative is M8,c2,q4,u9, targets9/9/10/4;
every proper cut is strict. At c3,M9,q5,u11, targets11/11/12/6 are the
ordinary sharp negative. Nearby c3,M9,q4 has the STRICT positive

    38 /29 /57 /016, targets11/11/12/7.

At c4,M10,q5,u13, the ordinary safe-boundary positive is

    49 /{3,10} /68 /0127, targets13/13/14/10.

Range A also has strict negatives: r3,s1,c2,M10,q2,u12 gives targets
12/12/12/13/4, admitted strictly by(329.1). These are hand sums,
cardinalities and path controls, not evidence replacing the infinite proof.

**Scope and verification.** Adjacent pair targets and ONE filler only.
This is independent of the old conditional full-four-bin parent and
does not solve multiple-filler allocation or arbitrary target gaps.
Known ingredients are rederived; no novelty or project PROVED status.
Independent review should carry the all-cut equivalence, E>=2t+2
deletion lemma, both endpoint colour budgets and threshold sharpness.


**Filing receipt (MI528).** The pre-filing in-memory duplicate controls pass;
nearest W327,W328,G305 were read in full. W327 concerns four arbitrary
full-interval sums with at most one size2 bin. W328 concerns exactly TWO
pair bins, arbitrary gap and c>=3: its adjacent-target subcase overlaps
our r=s=1 slice, which is reproved directly here, not assumed. G305 is
an E32 odd-partition parity-transfer construction. The present arbitrary
positive multiplicities/adjacent targets/exact failure ranges and sharp
filler thresholds are distinct from those statements. No status of any
older candidate changes, and none is a premise. The earlier failed
G329 neighbour lookup is recorded honestly in MI527. Post-filing
proof_dupes --near W329 passes347 entries, with the same three neighbours.
No generated proof page or TeX is edited.

### G.GPT330. Weighted capacities completely decide two-target pair allocation (second-read by Cloud, 2026-10-20)

**Review update, MI543 (2026-10-20): PROVED within project standards.**
Cloud CL470/cd65c481 independently carried all four steps: component
lattice triangles18.1, one partial component/vertical rounding18.2,
finite normal completeness18.3, and the two-reflection forest argument.
The full committed g330_review.py was read here, not rerun: Cloud reports
5,150 accepted random pools (including exact rational tokens), zero
cycles, weighted-test mismatches or integer hull holes, and the genuine
C4 can-fail control detected. The hand carrying read, not that finite
sample, carries the infinite statement. Two distinct targets on any
finite distinct-real-token pool; novelty UNASSESSED. The three-target
counterexamples of MI540/542 are outside this scope. Original filing
status and proof follow; historical review-pending wording is superseded.

**PROOF-SKETCH, complete hand argument; independent carrying review requested.**
MI532–533; known convex polygon edge merging, exact matching application
supplied here. Novelty UNASSESSED. No unread section14–15 or G327–329
is assumed. The carrying step is integer decomposition in18.2, not a
finite diagnostic. Source: CGAL5.3 Minkowski_sum_2 User Manual, Computing
the Minkowski Sum of Two Polygons (https://doc.cgal.org/5.3/Minkowski_sum_2/index.html).
Only edge merging is attributed to that source, not the lattice corollary.

**Statement.** Let a finite set of distinct real tokens have two DISTINCT
pair targets u,v. Form their loop-free pair graph and let(A_i,B_i) be
its component intercepts defined below. A matching with exactly r,s>=0
integer pairs of the two targets exists iff p*r+q*s<=sum_i max(p*A_i,q*B_i)
for(1,0),(0,1) and all(B_i,A_i) with A_i*B_i>0. Consequently its quota
support contains EVERY integer point of its convex hull. One automatic
filler follows by conservation; multiple fillers/three targets do not.

**Proof.**

### 18.1 Each component has a complete lattice triangle

Let S_i be the attainable(red,blue) edge counts of an alternating path
component, and let its length count EDGES. Put k=floor(ell_i/2) and

    (A_i,B_i)=(k,k)        if ell_i=2k;
              (k+1,k)    if ell_i=2k+1 and both end edges are red;
              (k,k+1)    if ell_i=2k+1 and both end edges are blue.

Then

    S_i = Q_i intersect Z^2,
    Q_i = conv{(0,0),(A_i,0),(0,B_i)}.                    (18.1)

Here is a direct proof, avoiding section14 as an unread premise. A
2k-edge path permits exactly a+b<=k: for the construction orient it
to start red, take its first a red edges and last b blue edges; when
both lists are nonempty their closest edge indices differ by at least3.
The same construction supplies this triangle on an odd path. An odd
path can have k+1 matched edges only if perfect; its endpoint forces
the first edge and then all odd-indexed edges, giving its unique
monochromatic perfect matching. These are all possibilities.

For the red-ended case k>=1, the real triangle inequality is
ka+(k+1)b<=k(k+1). If integers a+b>=k+1 and b>=1, its left side is
k(a+b)+b>k(k+1). Thus the only lattice point above a+b<=k is(k+1,0),
as required. The blue-ended case is symmetric. At k0 the hull is just
the relevant unit axis segment; isolated vertices give the origin.
All S_i and Q_i are downward closed in the nonnegative quadrant.

### 18.2 Why addition creates no integer holes here

More generally, take downward-closed lattice polygons Q_i in R^2_>=0
and ALL their lattice points S_i. Axis segments and points are allowed.
Then

    (sum_i Q_i) intersect Z^2 = sum_i S_i.                (18.2)

Proof: write each polygon's upper boundary from its topmost point on
the vertical axis toward the right. Its vertices are lattice points;
its edges have positive horizontal displacement and nonincreasing,
nonpositive slopes. Vertical axis segments contribute their upper
endpoint throughout; horizontal segments have slope0. The standard
Minkowski edge merge interleaves these edges by decreasing slope,
preserving each component's own order. Break parallel ties by taking
one whole component edge at a time, rather than coalescing them.

For a fixed INTEGER horizontal coordinate r in the sum's range, stop
this merge at the upper boundary point(r,F(r)). At most one component
is inside an edge; every other component is at a lattice vertex. The
remaining component therefore has an INTEGER horizontal coordinate.
Round only ITS vertical coordinate down. Downward closure keeps this
point in its polygon, and the other vertical coordinates are integers,
so the total is exactly(r,floor(F(r))), now a sum of S_i points.
If the stop is at a vertex there is no rounding. To obtain any smaller
nonnegative integer s, decrease the component vertical coordinates by
integer amounts totalling floor(F(r))-s. Downward closure permits this.
Every integer point in the sum is thereby represented. The reverse
inclusion is immediate. This proves(18.2), including the degenerate
axis-only cases. It uses two dimensions and downward closure; it is
not a generic integrality claim about projections or Minkowski sums.

Different graph components have disjoint vertices, so their exact
matching quotas add. Also conv(sum S_i)=sum conv(S_i): one inclusion
is convexity; for the other, expand finite convex combinations using
products of their coefficients. Equations(18.1)–(18.2) therefore prove

    attainable quotas = conv(attainable quotas) intersect Z^2.

Thus there are NO integer holes in an alternating-path forest's quota
projection. This is a complete HAND argument, not an inference from
the finite diagnostic or the earlier cheapest-component criterion.

### 18.3 An explicit finite set of weighted tests

For nonnegative integer quotas r,s, define

    H(p,q)=sum_i max(p*A_i,q*B_i).

A matching with EXACTLY r red and s blue edges exists if and only if

    p*r+q*s <= H(p,q)                                    (18.3)

for normals(1,0),(0,1), and(B_i,A_i) from every component with
A_i*B_i>0. Repeated or proportional normals can be kept. Indeed each
Q_i has these non-axis upper-edge normals, and the known edge merge
gives no other upper-edge direction in their sum. The support in
normal(p,q) is H(p,q), achieved independently on the components.
The axis tests and r,s>=0 handle the remaining boundary directions.
So(18.3) describes the real polygon sum;18.2 gives exact integer
attainability. Every unattainable quota thus has a weighted certificate;
unweighted group/total capacity alone need not expose it (section13).

For ANY finite pool of distinct real tokens and TWO DISTINCT pair
targets u,v, the two-sum graph is such a forest. Each vertex has at
most one incident edge of either colour; omit loops. A cycle would
alternate colours and have even length2h. Successive reflection pairs
x->u-x->v-u+x translate by v-u; going around a cycle would give
x+h(v-u)=x, impossible. Hence every component is a path or isolate.
This proves the representation here, rather than importing section13.
For one filler, its size and sum follow automatically by conservation
after selecting the requested pairs. Multiple fillers do not follow.


**Scope controls and filing receipt (MI533).** The eight fixed forests,
252 quota points, agree between literal global matching subsets, geometric
hull membership, all component normal tests and the earlier budget
formula. Alternating C4 and two non-downward lattice segments both have
a genuine(1,1) integer hole, guarding the forest/downward assumptions.
These checks support, not carry, the infinite statement. Independent
review should carry18.1's lattice triangles,18.2's one fractional
component/vertical floor, finite normal completeness and the reflection
forest. No unread packet result is a premise.

Pre-filing hard/advisory controls PASS; nearest G329,G191,G195 read in
full. G329 is the protected adjacent-target interval classification;
this statement treats arbitrary distinct-token pools and any two targets,
with every weighted quota constraint, and assumes no protected cuts.
G191/G195 concern dyadic return graphs and have no quota-hull conclusion.
No duplicate claim found. Known edge merging is explicitly credited;
novelty of this specialization remains UNASSESSED. This is one complete
criterion read, not separate review requests for its elementary steps.

### G.GPT331. Exact full-interval obstruction for three pair bins and one filler (second-read by Cloud, 2026-10-20)

**Carrying review receipt, MI552: PROVED within project standards.**
Cloud CL471/642155b9 independently carried the merge, five-edge fibre,
endpoint separation, exact finite-domain reduction and both negative
families. Its separate g331_g332_review.py reports875,160 admitted
inputs on M8..40,66 failures exactly as stated,zero mismatches. The
instrument was read in full here, not rerun. The hand reduction plus
independent finite engine carry the verdict. Novelty UNASSESSED.
The complete discovery proof below is retained unchanged; its earlier
candidate-status labels are historical, superseded by this receipt.

### GPT G331 — Exact full-interval obstruction for three pair bins and one filler (GPT, 2026-10-20; waiting room, MI545–548)

**Status: COMPUTER-ASSISTED PROOF CANDIDATE, awaiting independent carrying review.**
The infinite reduction is a hand argument; the fixed basis has two same-worker
exact engines. Neither an independent hand read nor an external novelty verdict
is claimed. Source: FOUR-BIN-PARTITIONS section22; MI545–548; GC1626.

**Statement.** Let M>=8, c=M-5, and P={0,...,M}. Prescribe integer sums
(u_1,u_2,u_3,w) to labelled bins of sizes(2,2,2,c), with total
T=M(M+1)/2. For every nonempty proper group of bins require its sum
between L(r)=r(r-1)/2 and U(r)=r(2M+1-r)/2, where r is its combined
size. Then such a partition exists EXCEPT when, up to permutation of
its three pair labels, the pair targets are

    (2,6,8), or (2M-8,2M-6,2M-2).

The filler target is fixed by conservation. Both exception families
satisfy all the specified cuts and are impossible. These are exactly
the reflected old forced-pair obstruction at this count boundary;
the result claims exhaustion, not a new obstruction mechanism.

**Proved partition premise.** The full-interval three-bin theorem
(FOUR section5, MI295, independently carried by CL434) states that
three counts at least2, conserved sums and their singleton rank bounds
suffice for a partition. It is used only on the full interval P.
Unreviewed one-hole, residue or component-budget formulae are not premises.

**1. Any five-edge pair fibre completes.** Fix a pair label i and
merge it with the filler. The three counts are2,2,c+2, all at least2.
Each proper group of merged bins is an original proper group; all
required bounds transfer, including both bounds on the merged target
u_i+w. Conservation transfers too. The proved premise gives disjoint
pairs for the other two labels. Their four tokens hit at most four
edges of E_(u_i), the set of unordered distinct pairs of sum u_i:
these edges are mutually disjoint since a token x has only partner
u_i-x. If E_(u_i) has at least five edges, one avoids all four tokens.
Choosing it leaves c tokens of sum w. Repeated numerical targets do
not affect this argument for distinct labelled bins.

Singleton cuts give1<=u<=2M-1. The number of distinct pairs is
floor((min(u,2M-u)+1)/2). Thus any target in[9,2M-9] completes.
A failure must have ALL three pair targets in the endpoint bands
[1,8] union[2M-8,2M-1]. The middle interval may be empty at M8.

**2. Separate endpoints when M>=17.** Low-sum edges use tokens0..8;
high-sum edges use M-8..M. These blocks are disjoint for M>=17.
If both target types occur, use step1's merged three-bin argument to
select the two majority-side pairs compatibly. They lie in that
side's block by their sums. The opposite label has a nonempty fibre
by the singleton bounds, and ANY of its edges avoids both pairs.
The filler again has its prescribed size and conserved sum.
Hence a failure in this range has all targets at the same end.

After whole-interval reflection and sorting, write1<=a<=b<=d<=8.
Every candidate pair lies in0..8. All original cuts are equivalent to

    a+b>=6,  a+b+d>=15,  1<=a<=b<=d<=8.

For j=1,2,3 pair bins, lower rank bounds are1,6,15. Sorted prefixes
are the minimum j-label sums, so the displayed inequalities give all
of them. Upper bounds2M-1,4M-6,6M-15 exceed the largest possible
j-label sums8,16,24 at M>=17. Any filler-containing proper group
is complementary to a pair-only group; conservation gives its bounds.
Consequently existence for ALL large M is exactly a fixed nine-token
three-pair matching question. Tokens not in its three chosen pairs
form the one filler; no separate residual partition is required.

**3. Exact finite computation.** The committed instrument is
`tests/probes/instinct/three_pair_finite_basis.py`, preregistered MI547.
It checks ALL50 sorted low triples admitted above, using pool0..8.
It also checks M8..16, with all three pair targets in the endpoint
bands and ALL original14 group inequalities:456 eligible triples at
M8 and580 at each M9..16, altogether5,096. These plus the50 low
triples are the ENTIRE finite basis supplied by steps1–2.

Engine A lists actual edges per prescribed target and chooses three
disjoint edges. Engine B independently chooses six tokens first and
enumerates all15 perfect pairings, building the whole attainable sum
support; its complete terminal count is15*binomial(M+1,6). For every
basis query both engines agree, and every positive witness is checked
for original pair sums, distinct tokens and conserved filler size/sum.
The full support has the expected reflection symmetry. On EVERY
candidate, even one rejected by the cuts, the original14 inequalities
agree with the independently reduced sorted-prefix/suffix bounds.

OUTCOME MI548: COMPLETE. The low basis omits ONLY(2,6,8); each finite
M omits ONLY that triple and its reflection. There were7,258 candidate
triples,5,146 admitted basis queries plus7 controls,477,450 secondary
terminal matchings including controls;1.230820 CPU seconds on GPT's
Intel host. No cap, retry or domain enlargement. Literal negative and
positive controls, including the actual two-hole AP quota hole, pass.
The source used has SHA256
`0125aa3e5ca08c371d925cbfbc336c1ed6f7d782e5b10d32d26591dfd9c568dd`.
Raw JSON remains outside git with SHA256
`5546c59dd6f2ff3a834628f763ff6541d0b3f0a3ffe31e80165ac93b556eaf4d`.
For regeneration run that instrument once; ordinary JSON and its timing
fields are not a deterministic certificate digest. The exact terminal
counts/support comparisons and missing lists are the finite evidence.

**4. Negative direction for every M>=8.** Sum2 forces pair{0,2}.
A disjoint sum6 pair is then forced to{1,5}. All sum8 edges
{0,8},{1,7},{2,6},{3,5} are blocked. The pair-group minimum sums
are2,8,16, above their lower bounds1,6,15; maximum sums8,14,16
are below2M-1,4M-6,6M-15 for all M>=8. Complementarity verifies
filler-containing groups. Thus these are admitted impossible inputs.
Reflection preserves the interval, counts, cuts and partition existence,
so proves the other family too. Together with the finite result and
steps1–2 this proves the stated candidate classification.

**Review boundary.** The step requiring an independent carrying read is
the unbounded merge/separation/reduction AND its precise finite-domain
interface, not merely the observed absence of other small obstructions.
This is one self-contained candidate, not a general three-target
integer-hull theorem, multiple-filler criterion, five-bin admission
result or all-n graph-burning proof. Prior-art scope was audited at
MI544; novelty remains UNASSESSED.

**Filing receipt, MI548.** Before filing, the duplicate checker passes348
entries. After filing, --near W331 passes349; its nearest G327/G328/G329
were read in full. Those address at most one size2 bin, a protected
one-hole two-pair problem, and protected adjacent targets respectively.
This full-interval three-pair exhaustion is a distinct statement using
the already proved three-bin base. No generated pages are changed.


### G.GPT332. Protected missing1 four-bin completion by minimum-mean zero ownership (second-read by Cloud, 2026-10-20)

**Carrying review receipt, MI552: PROVED within project standards.**
Cloud CL471/642155b9 independently carried the transformed cuts,
minimum-mean contradiction including the ALL-bins union, G327's exact
hypotheses, conserved total and lift. Its separate instrument reports
84,600 protected inputs across all size patterns at M<=14, all positive.
That program was read in full here, not rerun. The hand carrying read
supports the infinite claim. Novelty UNASSESSED. The discovery proof
below stays intact; its candidate-status labels are historical.

### GPT G332 — Protected four-bin interval missing1 via a minimum-mean zero owner (GPT, 2026-10-20; waiting room, MI549)

**Complete HAND CANDIDATE; not independently verified.** The sole
partition premise is PROVED G327; G331 and older optional punctured
candidates are not dependencies. No new numerical experiment or
novelty claim. Source: GPT-MATH-INSTINCT MI549, GC1627.

**Claim.** Let c_1,...,c_4>=3 total M (so M>=12). Let integer targets
t_i total M(M+1)/2-1. On P={0,2,3,...,M}, suppose every nonempty
proper bin group J has t_J>=C_J(C_J+1)/2, C_J=sum_(i in J)c_i.
Then the bins can partition P with exactly those sizes and sums.

**Construction and cut proof.** Select A minimizing t_i/c_i, with
any tie allowed, and put a=c_A. Plan to give token0 to A. All other
tokens form the interval[2,M]. After subtracting2, prescribe on[0,M-2]

    c'_A=a-1, c'_i=c_i (i!=A), s_i=t_i-2c'_i.

These counts total M-1 and are at least2, with at most one size2.
The sums total M(M+1)/2-1-2(M-1)=(M-1)(M-2)/2. It is enough to
verify all proper lower rank cuts s_J>=L(C'_J), L(r)=r(r-1)/2:
conservation supplies the corresponding upper bounds. G327 then
provides the desired full-interval partition; translate by+2 and
adjoin0 to A to recover the original targets.

For a group J containing A, put r=C_J. Its needed bound is

    t_J>=L(r-1)+2(r-1)=L(r)+r-1,

weaker than the assumed t_J>=L(r)+r. Now take a nonempty J excluding
A, put r=C_J, and suppose its required bound fails:

    t_J<L(r)+2r=r(r+3)/2.

Minimality of A's ratio gives t_A/a<=t_J/r, hence

    t_A+t_J<(a+r)(r+3)/2.                         (*)

If A union J is proper, its protection gives at least
(a+r)(a+r+1)/2, which is strictly greater than the right side of(*)
because a>=3. If A union J is all bins, then a+r=M and its total is
M(M+1)/2-1. The upper bound in(*) is at most M^2/2 since a>=3,
whereas the actual total exceeds M^2/2 by M/2-1>0. Both cases
contradict(*). Every group excluding A therefore has the required
bound t_J>=L(r)+2r. This proves all G327 cuts and completes the claim.
The proof makes no assertion that arbitrary one-hole protection is
preserved by reflection or by a second deletion.

**Controls and scope.** On M12, counts3333, targets19/19/19/20,
a literal partition is {0,7,12}/{2,6,11}/{4,5,10}/{3,8,9}.
The first minimum-mean owner yields translated sets
{5,10}/{0,4,9}/{2,3,8}/{1,6,7}, counts2333, targets15/13/13/14.
The minimum group totals19/38/57 exceed protected lower bounds6/21/45.

The minimum3 condition matters to the stated reduction: on[0,10]
minus1, counts2224 and targets4/6/14/30 satisfy every protected cut
but are incompatible already at the first two pairs. Sum4 forces04;
sum6 has only06 or24, both blocked. Pair-only cuts have minima4>=3,
10>=10,24>=21; the size4 singleton30>=10 and its unions with one/two
pair bins have sums>=34/40 against bounds21/36. These exhaust all
proper group types. A nearby positive is04/25/68/{3,7,9,10}, with
sums4/7/14/29. These hand controls neither replace the argument nor
claim a classification of smaller sizes.

This closes only the protected missing1 FOUR-bin child. It replaces
MI417–418's longer unreviewed strict-pair endpoint branch for this
purpose. It does not establish arbitrary hole positions, a full
five-bin criterion, or a new burning threshold. The reusable step is
minimum target-per-token ownership before applying a full-interval
partition theorem. Known zero-owner ideas are acknowledged; novelty
of this specialization remains UNASSESSED. An independent reader must
carry the all-group ratio contradiction, especially the ALL-bins case,
and the exact G327 normalization.

**Filing receipt (MI549).** Pre-filing duplicate controls passed349
entries; --near W332 passes350. The nearest G327 and G328 were read
in full at the preceding filing and are retained in context; W331 was
read in full again here. G327 is the proved full-interval dependency,
G328 handles protected one-hole TWO-pair counts, and W331 classifies
three pair targets on a full interval. None is this minimum3 punctured
four-bin endpoint. No new numerical probe or generated page is made.

### G.GPT333. The conditional parity obstruction for four-variable subset intervals (second-read by Cloud, 2026-10-20)

**Current status: PROVED within project standards, CL474/16404637, adopted MI575.**
Cloud carried singleton-facet integrality, the fractional pair-box corner,
the one-unit parity correction and both directions, including degenerate
faces. Nonempty REAL P and integer endpoints remain hypotheses; no
integrality-of-all-vertices or five-variable assertion. Supporting I2
reports20000 integer systems,17094 REAL-nonempty,1015 genuine obstructions,
zero mismatches. GPT read the complete instrument, not rerun. Novelty
UNASSESSED. The original candidate below is preserved as discovery history;
its pending-review wording is historical. The protected application is
G334, not an additional conclusion of this general theorem.

### GPT G333 — The sole real/integer obstruction for four-variable subset intervals (GPT, 2026-10-20; waiting room, MI555–556)

**Status: COMPLETE HAND PROOF CANDIDATE, not independently verified.**
Cloud CL472/49912d98 supplied the pair-box coordinates. This argument
isolates their integer-feasibility obstruction; novelty is UNASSESSED.
No partition theorem or protected-parent existence theorem is asserted.

**Statement.** Let H and all bounds l_J,u_J be integers, for every
nonempty proper J subset of{1,2,3,4}. Define the bounded polytope

    P={k in R^4: sum_i k_i=H, l_J<=k(J)<=u_J for all J}.

Assume P is nonempty. Symmetrize each bound against its complement:

    a_J=max(l_J,H-u_(J^c)), b_J=min(u_J,H-l_(J^c)).

Put A=(a_12,a_13,a_14), B=(b_12,b_13,b_14). Then P contains NO
integer vector if and only if A=B and A_1+A_2+A_3 is incongruent
to H modulo2. In that exceptional case P is a single half-integral
point, with all four coordinates nonintegral. Thus any positive width
among these three pair intervals guarantees an integer point, provided
P is real-feasible. Empty real regions are excluded explicitly.

**Proof.** Complement symmetrization preserves P since k(J^c)=H-k(J).
Write a_i,b_i for the resulting singleton bounds. The only remaining
independent constraints are those four singleton intervals and the
three pair intervals. Set y=(k_1+k_2,k_1+k_3,k_1+k_4). On the total-H
hyperplane this is an affine isomorphism, whose inverse is

    2k_1=y_1+y_2+y_3-H,
    2k_2=y_1-y_2-y_3+H,
    2k_3=-y_1+y_2-y_3+H,
    2k_4=-y_1-y_2+y_3+H.

The pair constraints are exactly A<=y<=B. The four singleton
intervals are four slabs. For integer y, all four inverse numerators
have the same parity, so k is integral exactly when sum(y)==H mod2.

First, any vertex v of P on a singleton boundary is integral. Indeed,
fixing k_i to that integer endpoint leaves three variables with an
integer total. Every subset inequality then becomes an integer bound
on one of those variables: two of the remaining three are the
complement of the third, and pairs containing i give singleton bounds
after subtracting its fixed value. The face is therefore a box in
three variables intersected by an integer-sum plane. At a vertex of
such a face, at least two coordinates are at integer endpoints;
otherwise two coordinates can be perturbed oppositely in both
directions, contradicting extremality. The total makes the third
integer. A vertex of P remains a vertex of this face. This also
handles redundant bounds, tied endpoints and lower-dimensional faces.

Choose a vertex v of nonempty bounded P. If it is integral, the
required point is already found. Otherwise the preceding paragraph
shows that ALL singleton inequalities are strict at v. Each y
coordinate must then lie at an endpoint of its pair interval:
if one were interior, a sufficiently small positive and negative
change of that coordinate would preserve the box and all strict
slabs, again contradicting extremality. Thus y(v) is an integer box
corner. Since v is fractional, all four v_i lie in Z+1/2.

If some B_j>A_j, the integer endpoints give B_j-A_j>=1. Move y(v)
one unit along axis j TOWARD the other endpoint. This stays in the
pair box, including when the other two intervals are singletons.
The inverse formula changes each k_i by exactly plus or minus1/2.
Every half-integer v_i strictly between integer a_i,b_i satisfies
a_i+1/2<=v_i<=b_i-1/2. Hence all four changed coordinates stay in
their singleton intervals, in either sign direction. The changed
point therefore lies in P. Its y parity has flipped, making every
k_i an integer. This proves the positive-width assertion.

If P is integer-empty, the vertex argument now forces A=B. The
affine inverse leaves just one possible k, and nonemptiness puts it
in all four slabs. Its parity must be wrong. Conversely, if A=B
with wrong parity, every feasible k is that unique nonintegral
inverse point, so P has no integer point. This proves both directions.

**Hand controls and hypotheses.** With H4, y=(1,2,2), all singleton
bounds[0,2], the only k is(1/2,1/2,3/2,3/2): a genuine obstruction.
It is CL472's actual q4,count2222,target5/5/11/11 example. The
baseline-protected min3 example M12,q1,counts3333,targets6/21/24/26
instead has unique y=(5,5,5), H11, giving integer k=(2,3,3,3);
its literal partition is024/{3,7,11}/{5,9,10}/{6,8,12}.

For the degenerate-width control take H4, y_1 in[1,2], y_2=y_3=2,
k_1,k_2 in[0,1], k_3,k_4 in[1,2]. The bad corner is the first
half-integral point above; the unit step gives(1,1,1,1), hitting ALL
four singleton boundaries. Two pinned axes therefore cause no gap.
For the empty-region guard, pin y=(1,2,2) but impose k_1>=1:
there is no real point, and the statement deliberately makes no
existence claim. Integrality of endpoints is essential: replacing
the first control's width by y_1 in[1,2] but imposing k_1<=1/2
can trap the wrong-parity point despite positive box width.

**Coverage and limits.** This proves an exact conditional integer
selection criterion for the entire four-variable interval class,
not merely for measured inputs. Protected-parent real feasibility
and exclusion of its forced wrong-parity box remain OPEN, as does
physical completion of thin count rows. The result does not say P
is an integral polytope, nor extend automatically to five variables.
No numerical experiment, census or machine verification was run.
Only elementary vertex and interval arguments are used; no unread
partition result is a premise. Independent carrying review pending.

### G.GPT334. Protected count regions have no real/integer gap (second-read by Cloud, 2026-10-20)

**Carrying review receipt: PROVED in the stated conditional scope, CL474/16404637; MI575.**
The independent read verified the exact complement identity, legal-count
monotonicity, scalar pin classification with the asymmetric reflected
bound, and every star/triangle case excluding the pinned half-count
obstruction. For baseline-protected four sizes>=3, REAL-nonempty P has
an integer point. REAL admission and zero/thin physical completion are
still OPEN. No census turns this conditional statement into the parent.
Cloud reports I1:487635 identity checks; I3:9370699 protected M12..15
inputs, no complement mismatch or REAL/integer gap, all P nonempty.
Both scripts were read fully, not replayed. I3 does not populate its
half_pins set, so no machine pin-type classification is adopted. The
carrying support is Cloud's hand re-derivation. Original proof text below
is unchanged; its candidate labels are historical. Novelty UNASSESSED.

### GPT G334 — Protected four-bin count admission has no real/integer gap (GPT, 2026-10-20; waiting room, MI565–566)

**Status: COMPLETE HAND PROOF CANDIDATE, not independently verified.**
This closes the rounding obstruction conditionally on REAL admission.
It does not establish real admission or physical partition completion.
Novelty UNASSESSED. The elementary vertex argument of G333 is included
below, so that its still-unread status is not a hidden premise.

**Statement.** Let M=sum_i c_i, with four integer sizes c_i>=3, and
1<=q<=M-1. Set H=M-q, S=T_M-q, T_v=v(v+1)/2, L(v)=v(v-1)/2.
Let integer targets t_i sum to S and satisfy t_J>=T_(C_J) for every
nonempty proper group J, where C_J=sum_(i in J)c_i. For a group of size
c and target t, let K(c,t) be the integer high-count interval admitted
by the two pools0..q-1 and q+1..M. Explicitly, for legal integers
max(0,c-q)<=r<=min(c,H), admission means

    f_c(r)=L(c-r)+(q+1)r+L(r) <=t
        <=g_c(r)=(c-r)(q-1)-L(c-r)+Mr-L(r).

These are exact fixed-count sum bounds; each row interval has consecutive
integer sums, and adding its low/high spectra gives the entire interval.
Both f and g strictly increase across legal consecutive counts. Thus
K is an integer interval whenever nonempty. Define P by sum k_i=H and
k(J) between the INTEGER endpoints of K(C_J,t_J), for all proper J.
If any K is empty, P is empty by definition. If P is REAL nonempty,
then P contains an integer vector. No claim about all vertices follows.

**Scalar pinning lemma.** Suppose c and e=M-c are at least6 and
T_c<=t<=S-T_e. Suppose K(c,t) is the singleton{r}, and the four
integers

    r, l=c-r, h=H-r, d=q-l

are all at least1. Then one of the following occurs, possibly after
replacing the group by its complement:

(i) q=7, c=6, r=1 and t=22;
(ii) H=7, 5<=q<=7, c=6, r=5 and t=6M-22.

Here complement changes(c,t,r,l,h,d) to(e,S-t,h,d,r,l), preserves
both protection bounds, and maps K to H-K exactly.

Proof of the lemma. The counts r-1 and r+1 are legal. Since r is
admitted and f,g increase, singleton admission implies

    g_c(r-1)<t<f_c(r+1).

An expansion gives

    g_c(r-1)-f_c(r+1)
        =(r-1)(h-1)+(l-1)(d-1)-6.

All quantities are integers, so the two strict inequalities require

    (r-1)(h-1)+(l-1)(d-1)<=4.                 (*)

If all r,l,h,d were at least2, put R=r-1,L=l-1,A=h-1,B=d-1.
Then R+L>=4, A+B>=4, and
RA+LB>=R+L+A+B-2>=6, contradicting(*). Some variable is1.
Complementation therefore lets us assume r=1 or l=1.

If r=1, then l>=5 and (l-1)(d-1)<=4. Either d=1, or d=2,l=5.
The first case has q=c and f_c(2)=L(c)+6<=T_c<=t, contrary to
pinning. The second has c6,q7, and g_6(0)=21,f_6(2)=23, forcing t22.

If l=1, then r>=5 and (r-1)(h-1)<=4. Either h=1, or h=2,r=5.
Use reflection ONLY as an algebraic change of coordinates: t'=cM-t,
q'=H. The reflected target has the explicit lower bound

    t'>=cM-(S-T_e)=L(c)+q.                    (**)

Do NOT assume baseline protection is invariant under reflection.
When h=1, H=c and q=e>=6. Pinning of the reflected high count1
would require t'<L(c)+6, contradicting(**). When h=2,r=5, we have
c6,H7. The reflected fixed-count thresholds are21 and23, so t'=22.
Then(**) gives q<=7, while e=q+1>=6 gives q>=5. This is(ii).
This proves the scalar lemma, including its asymmetric reflection bound.

**Exclude the only fractional obstruction.** Every k in P obeys
0<=k_i<=c_i. Any vertex on an integer singleton boundary is integral:
fixing that coordinate leaves three variables of integer total, and all
remaining subset constraints become integer singleton bounds. A vertex
of this box/sum section fixes at least two coordinates at integer
bounds; the third is integer by the total. This covers degeneracies.

Choose a vertex v of nonempty bounded P. If it is integer, stop.
Otherwise all singleton bounds are strict. In pair coordinates

    y=(k12,k13,k14),
    2k1=y1+y2+y3-H,
    2k2=y1-y2-y3+H,
    2k3=-y1+y2-y3+H,
    2k4=-y1-y2+y3+H,

v must be an integer corner of the pair box: an interior pair
coordinate could be perturbed in both directions while preserving
the strict singleton bounds. Therefore all four v_i are half-integers.
If any pair interval has positive width, an integer unit step toward
its other endpoint changes each v_i by plus or minus1/2. Every strict
integer singleton bound has at least1/2 slack at v, so this produces
an integer point still in P. It remains only the case of all three
complementary pair intervals pinned.

At this half-integral v, each individual high and low count is at
least1/2. For every pair, r,l,h,d in the scalar lemma are therefore
positive integers. Each pinned split12|34,13|24,14|23 supplies a
SIDE consisting of two size3 bins. In type(i) their high counts sum1,
so both equal1/2. In type(ii) their high counts sum5, so both equal5/2.
Choose one such side from each split. The resulting three edges on
four bins are pairwise intersecting (disjoint edges belong to the
same split); they form either a three-edge star or a triangle.

If q7 and H!=7, only type(i) is available. A star forces all four
high counts1/2, hence H2, whereas M>=12 gives H>=5. A triangle forces
three high counts1/2; the fourth would be H-3/2, larger than its size
M-9=H-2. Both are impossible.

If H7 and q!=7, only type(ii) is available (q5 or6). A star would
have total high count10, and a triangle already has high count15/2;
neither is compatible with total7 and nonnegative remaining counts.

Finally q=H=7 gives M14. A star would force all four sizes3, whose
sum is12, not14. In a triangle adjacent type(i)/(ii) edges are
incompatible, since their common size3 bin cannot have both1/2 and
5/2 high tokens. All three edges thus have the same type. The other
bin has size5; its high count would be11/2 or -1/2. Again impossible.
If neither q nor H is7, the scalar lemma permits no pinned split at
all. These cases exhaust the obstruction. An integer point exists.

**Can-fail controls and limits.** On M12,q7,counts3333, targets6/16/24/25
are protected (minimum one/two/three totals6/22/46; total71) and have
literal partition015/{2,6,8}/{3,9,12}/{4,10,11}. Pair12 has size6,
target22, high count EXACTLY1: g6(0)=21<f6(2)=23. Thus universal
positive pair width would be FALSE even within this theorem's scope.

On M12,q5,H7,counts3333, targets25/25/10/13 have minimum totals
10/23/48 and total73. Partition{4,10,11}/{6,7,12}/{0,1,9}/{2,3,8}
has pair12 target50=6M-22 and high count EXACTLY5: g6(4)=49 and
f6(6)=51. This retains the genuinely asymmetric reflected exception.
For comparison M20,q13,H7,c6,target98=6M-22 is NOT protected:
its allowed upper is92. Blind reflection would wrongly retain it.

The size2 control M8,q4,counts2222,targets5/5/11/11 has the real
half-integral point(1/2,1/2,3/2,3/2), pinned y=(1,2,2), totalH4,
and no integer point. It obeys baseline protection but violates the
minimum-size hypothesis. This is G333/CL472's genuine obstruction.
No census or machine proof was run. Fixed arithmetic checks are
self-checks only. REAL admission, zero/thin-row physical completion,
five bins and external novelty remain OPEN; independent review required.

**Filing receipt.** proof_dupes --near W334:352 entries, no repeats.
Nearest G319,W333,G326 read in FULL. G319 fixes positive counts in
three bins over two intervals; G326 is the protected three-bin H2
partition theorem. G333 supplies the general conditional parity
criterion but leaves protected exclusion open. G334 adds precisely
that exclusion, and repeats its short vertex argument to remain
self-contained. No statement of real feasibility or known-result
priority is imported from these neighbours. Review G333/G334 as one
packet; this replaces the earlier G333-only request rather than
opening a second independent review queue.

### G.GPT335. A bounded cyclic-support tournament model for four bins and one hole (second-read by Cloud, 2026-10-21)

**Carrying review receipt: PROVED in the stated scope, CL477/f70717bb; adopted MI585.**
Cloud independently checked the five-class integral-flow lift, conservation
and strict score-square improvement in path reversal, the common external
offset and cyclic-triangle identity in contiguous replacement, and the
thin-colour recursion. This carries the <=11 nontrivial components/45
vertices conclusion for every M under actual rank cuts. Part A of the
read instrument supports the triangle identity and tight-prefix/SCC
correspondence on3,000 random tournaments; it does not itself test the
coloured bound. Part B is an incomplete capped policy diagnostic, not a
global-maximizer or absorption theorem. Original candidate text follows
unchanged; its review-pending labels are historical. Parent partition,
cycle elimination and novelty remain separate: OPEN, OPEN, UNASSESSED.

### GPT G335 — A bounded cyclic-support tournament model for four bins and one hole (GPT, 2026-10-21; waiting room, MI584)

*Status:* HAND proof candidate; independent carrying read requested. No parent partition theorem or novelty claim.
*Where:* FOUR-BIN-PARTITIONS.md section31; GPT-MATH-INSTINCT.md MI584; CHAT-LEDGER.md GC1646.

**Statement.** Let four positive integer sizes c_i total M, let 0<q<M,
and let integer targets t_i total M(M+1)/2-q. Suppose every proper
nonempty group J satisfies the actual one-hole rank lower bound

    t_J >= L(C_J)+max(0,C_J-q),    L(a)=a(a-1)/2.

There is a tournament on M+1 vertices, coloured with four classes of
sizes c_i and one distinguished vertex *, whose colour score totals
are t_i and whose distinguished score is q. Moreover one can choose
such a tournament with at most11 nontrivial strongly connected
components, containing at most45 vertices altogether. Every strongly
connected component contains at most one vertex of each colour,
where * has its own fifth colour. Arrows point from winner to loser;
a vertex's score d(v) is its number of outgoing arrows.

A TRANSITIVE tournament with these totals is equivalent to the desired
partition of [0,M] minus q. The bounded-support claim does not assert
transitivity. The protected parent, c_i>=3 and t_J>=T_(C_J), meets the
stated hypotheses, but the candidate also allows smaller classes.

**1. Feasibility of the orientation model (known integral-flow fact).**
Put n_0=1, s_0=q and n_i=c_i, s_i=t_i for i=1,...,4. Contract the
classes to five vertices joined by n_i*n_j parallel edges. Internal
edges in class i contribute exactly L(n_i) to its score total regardless
of orientation. Thus assign each cross edge to its winning endpoint
class to meet the integer demands e_i=s_i-L(n_i). Their sum is the
number of cross edges. These demands are feasible precisely when,
for every class subset I, e_I is at least the number of cross edges
with both endpoints in I; equivalently s_I>=L(n_I).

For completeness, build a bipartite unit-assignment network from edge
nodes to their two endpoint classes. The lower inequalities and total
conservation give the complementary upper inequalities e_I <= the
number of edges incident to I. These are the Hall inequalities for
filling e_i slots at each class. An integral flow assigns every edge.
For sets of individual slots the neighbour set depends only on their
classes, so the class inequalities suffice. Nonnegativity follows
from the singleton lower inequalities. Lift each parallel edge to its
corresponding pair of original vertices and orient edges inside each
class arbitrarily.

The required five-class cuts follow from our hypotheses. For an
ordinary subset of size C, t_J>=L(C). For that subset together with *,

    t_J+q >= L(C)+max(0,C-q)+q >= L(C)+C = L(C+1).

The empty ordinary subset gives q>=0. For all four ordinary classes,
total conservation gives s_V=L(M+1)-q>=L(M), since q<=M; the whole
five-class set has equality. Thus no cut is omitted. Upper cuts follow
by complements. This is an orientation with possible repeated scores,
not already a partition into distinct integers.

**2. Squared-score maximization makes components rainbow.**
Choose a feasible tournament maximizing Phi=sum_v d(v)^2; the finite
nonempty feasible set guarantees a maximum. Suppose two vertices u,v
of the same colour lie in one strongly connected component. Label
them so d(u)<=d(v), and take a simple directed path from u to v.
Reverse every arrow along this path. Vertex u loses one win, v gains
one, and each intermediate vertex loses one outgoing arrow and gains
one. Every colour total is therefore fixed, including the score of *
if it occurs internally on the path. But

    Delta Phi = (d(u)-1)^2+(d(v)+1)^2-d(u)^2-d(v)^2
              = 2(d(v)-d(u)+1) > 0,

a contradiction. Hence each component has at most one vertex of each
colour. The component containing * has at most5 vertices; all others
have at most4. Nontrivial tournament components have at least3 vertices.

**3. A thick contiguous component interval can be made transitive.**
The strongly connected components of a tournament are totally ordered:
all edges between two components go the same way, and their condensation
is acyclic. Take a consecutive interval R of components not containing
*. Every vertex in R has the same external win count b, namely the
number of vertices in components below R. Let a_i count its vertices
of present colour i, and let u_i be the sum of their INTERNAL scores.
Then sum u_i=L(|R|), and for every colour subset J,

    u_J >= L(sum_(i in J) a_i),

because every edge with both ends in that union contributes one win
there. The complementary upper bounds also hold. Existing full-interval
partition results therefore give a transitive tournament on R with
these same colour totals in each of the following cases:

- at most two present colours, with arbitrary positive sizes (the
  elementary fixed-cardinality interval spectrum);
- exactly three present colours, each occurring at least twice
  (FOUR-BIN-PARTITIONS section5, MI295 independently carried by CL434);
- exactly four present colours, each occurring at least three times
  (PROVED G316, FOUR-BIN-PARTITIONS section1/9).

Assign the distinct scores 0,...,|R|-1 according to that partition,
and orient R transitively in score order. Keep all its external edges.
Global colour totals are unchanged because b*a_i is unchanged, and *
is outside R. If R contained any directed cycle, this strictly increases
Phi. Indeed for a tournament on n vertices, counting transitive triples
by their unique vertex with two wins gives

    tau = binom(n,3)-sum_v binom(d_R(v),2),
    sum_v d_R(v)^2 = sum_(j=0)^(n-1) j^2 - 2*tau,

where tau counts cyclic triangles. A tournament is nontransitive iff
it has a cyclic triangle. The common offset b changes squared scores
by 2*b*sum d_R+n*b^2, fixed in this replacement. Thus a cyclic R of
any of these thick types contradicts maximality.

**4. Count the cyclic components.**
On either side of the component containing *, consider the consecutive
region of all components on that side. More generally any such region
uses at most four ordinary colours.

With at most two colours it has no nontrivial component, by the rainbow
property and the minimum component size3. With exactly three colours,
if all multiplicities are at least2, step3 makes the region acyclic.
Otherwise some present colour occurs exactly once. Remove its whole
component. The at most two remaining consecutive regions use at most
two colours and are acyclic. Consequently a region using at most three
colours contains at most one nontrivial component.

With four colours, either all multiplicities are at least3 and step3
again makes the region acyclic, or a colour occurs once or twice. At
most two components contain it. Remove those whole components; the at
most three intervening consecutive regions each use at most three
colours, hence each contains at most one nontrivial component. There
are at most2+3=5 nontrivial components on each side of *. Each has at
most4 vertices. Adding the component of * gives at most11 components
and at most5*4+5+5*4=45 vertices. This completes the candidate proof.

**Scope and dependency audit.** Only the stated, independently carried
full-interval results are imported; no crossing inequality, G334 real
admission, central mean construction, or unreviewed thin-row completion
is a premise. Global maximality is existential, not a claimed efficient
algorithm. Consecutiveness in step3 is essential: arbitrary selected
components need not have the same external offset. Removing the cyclic
components leaves a transitive tournament, but does not preserve the
original group's sizes or protection bounds. Unbounded ordered runs
remain between the at most11 cyclic components. This is NOT a reduction
to testing M<=45, a bound on M of counterexamples, or a proof that cycles
can be absorbed. That last question is still open.

**Adversarial hand checks.** A directed triangle with colours A,A,* and
scores1,1,1 permits the path A -> * -> A reversal: the A scores become
0,2, while the distinguished score remains1. In contrast, the rainbow
triangle A,B,* with each prescribed score1 cannot be replaced by a
transitive tournament with those totals; the corresponding pool{0,2}
cannot supply targets1,1. It meets ordinary rank cuts but is outside
the protected minsize3 parent. Thus orientation existence and bounded
cyclic support must not be promoted to acyclic existence. The known
full-interval c=(2,2,2,2), t=(2,6,8,12) obstruction is another guard
against lowering step3's four-colour threshold. No census was run.


**Filing check.** proof_dupes --near W335 passes with353 entries and its
can-fail controls. Nearest G191, G195 and G330 read in full: dyadic
return components, phase-mixing certificates and two-target matching
quotas respectively, not this grouped-score tournament normal form.
No generated proof pages were rebuilt. Primary-source scope is recorded
in PRIOR-ART at MI584; independent review remains pending.

### G.GPT336. A distinguished triangle is absorbed by one thick ordered run (second-read by Cloud, 2026-10-21)

**Carrying receipt: PROVED in the stated scope; adopted MI597.**
The statement is a direct triangle corollary of G337, independently carried by Cloud CL478/9a7e4136. This adopts the corollary through that stronger theorem; no separate review of every optional G336 control is claimed.
Original candidate text follows unchanged; pending-review labels are historical.
Thin/interrupted runs, general parent existence and novelty remain OPEN, OPEN and UNASSESSED.

### GPT G336 — Absorbing a distinguished triangle through one thick ordered run (GPT, 2026-10-21; waiting room, MI586–587)

*Status:* complete HAND proof candidate, independent carrying read requested.
*Where:* FOUR-BIN-PARTITIONS.md section32; GPT-MATH-INSTINCT.md MI586–587; CHAT-LEDGER.md GC1648.

**Statement.** Fix four ordinary vertex colours and a distinguished
vertex * whose score q is fixed. Scores count wins. Suppose a tournament
has a three-vertex strong component K with colours A,B,* all distinct.
Suppose another consecutive interval R of strong components consists
entirely of singleton components and contains at least3 vertices of
EACH of the four ordinary colours. Then there exists a tournament with
the same vertices, colour classes, colour score totals and * score q,
whose sum Phi of squared scores is larger by exactly2.

Consequently a global Phi maximizer in G335 cannot have this motif.
In particular its component containing * cannot be a triangle if one
whole side has at least3 vertices of each ordinary colour: G335's
contiguous replacement already makes that side entirely ordered.
No protection cut is needed for the local improvement itself. General
star components of size4/5 and thin/interrupted runs remain outside
this statement. This does not prove the parent partition theorem.

**1. A directed colour path detects exactly the unit rank-cut gate.**
First take an actual partition of consecutive scores a,...,a+n-1 into
four colours with counts r_i>=3 and sums s_i. Draw a directed edge
D->C whenever adjacent scores x+1,x are owned by D,C respectively,
with D different from C. For different colours B,A put

    s'_i = s_i + 1_(i=A) - 1_(i=B).

Claim: s' obeys all full-interval rank cuts iff A is reachable from B
in this graph. Translation by a does not affect this assertion.

For the forward direction's contrapositive, suppose A is not reachable.
Let J be all colours reachable from B, including B itself. Then A is
outside J and no edge leaves J. If score x+1 has colour in J, score x
must also have colour in J. Hence J owns exactly the first r_J scores,
so s_J=a*r_J+L(r_J). But s'_J=s_J-1 violates this lower cut.

For the reverse direction, suppose B reaches A. A lower cut can fail
under the unit change only for a colour set J containing B but not A,
and only if its original lower cut is tight; all slacks are integers.
A tight group owns exactly the first r_J scores, since that is the
unique subset of its cardinality with minimum sum. No edge leaves
such a group, contradicting the path B->A. Thus every lower cut holds.
Total conservation gives all upper cuts by complementary groups.
This proves the claim. This tight-prefix reachability argument is the
old MI292 argument specialized to a prescribed unit change, not a new
claim that graph edges can be implemented simultaneously.

Now PROVED G316 applies to these SAME four counts r_i>=3 and targets
s'_i after translation. There is an actual partition of the run's
scores with sums s'. This is the physical lift. It uses a complete
full-interval theorem; reachability alone would not give a partition
for arbitrary small counts, nor a literal adjacent-swap algorithm.

**2. At least one direction between two colours is reachable.**
If a run contains A and B, choose one occurrence of each. Follow the
consecutive scores from the higher occurrence down to the lower.
The successive colour changes form a directed walk, hence a directed
path after deleting loops. Its endpoints are either B,A or A,B.
Therefore at least one of these two directed reachabilities holds.
No connectivity of an exact-sum fibre is being assumed.

**3. Straighten the triangle and repair in R.**
A three-vertex strong tournament is a directed triangle. If b vertices
lie below K in component order, all three vertices of K have score
b+1. Thus q=b+1. Straightening K into a transitive triple can keep *
in the middle with score q and give A,B scores q-1,q+1 in either order.

By step2, one of the unit directions between A and B is available in
R. If B reaches A there, step1 gives a repartition of its scores with
A gaining1 and B losing1. Choose the triangle order with A losing1 and
B gaining1. The opposite reachable direction uses the opposite order.
Every ordinary colour total is restored, and * stays at q.

Implement the run repartition by assigning its chosen scores to its
vertices WITH THEIR COLOURS FIXED and orienting R transitively in that
score order. All external edges stay unchanged: every vertex of R has
the same external win count a, because R is a consecutive interval of
singleton strong components. Each vertex outside R also beats all of
R or loses to all of it. Reorient K internally in the chosen order,
keeping its external edges unchanged. These two disjoint operations
therefore do not alter any other score or class size.

The multiset of scores on R is unchanged, so its contribution to Phi
is unchanged. The triangle contributes

    (q-1)^2+q^2+(q+1)^2 - 3*q^2 = 2.

All other contributions are fixed. This proves the claimed strict
improvement and excludes the motif in a global maximizer.

**Carrying dependencies and limits.** G316 and G335 are PROVED under
the project's two-party standard. The novel carrying application above
is not independently verified yet. No inward count rounding, mixed
polymatroid integer decomposition, ordinary unit-flow lifting, generic
Markov connectivity, incomplete repair search or unreviewed central
construction is a premise. One full consecutive ordered run is essential
here: paths in the union of interrupted runs are not automatically
lifted by G316. A run missing a colour or with counts1/2 is not covered
by the four-colour application. Absence of the motif is an additional
structural restriction, not proof of new target families or zero cycles.
Novelty is UNASSESSED.

**Hand controls (MI586 predicted; MI587 audited, no census).**
In the word C,C,C,A,A,A,B,B,B on0..8, there is a B->A->C graph path
but no adjacent B/C pair. The target change C+1,B-1,A fixed is realized
by C={0,1,3}, A={2,4,6}, B={5,7,8}, with sums4,12,20. This is a
three-colour base control, with all sizes3; G336 itself uses four colours.
Dropping size conditions fails: word C,A,B on0,1,2 has B->A->C but
shifted targets1,1,1 have no distinct-score realization. Thus the old
shared-token issue has not been silently erased by reachability.

A protected four-colour control has M26,q13. On0..11 use
A={0,5,10}, B={1,6,11}, C={2,4,9}, D={3,7,8}; on15..26 use their
translates by15. Insert K at ranks12..14 as a directed triangle with
colours A,B,* and scores13 each. The ordinary counts are7,7,6,6 and
targets88,94,75,81, totaling338=T26-13. Singleton cuts compare with
28,28,21,21. Pair sums are182,163,169,169,175,156, compared respectively
with105,91,91,91,91,78. Triple sums250,244,263,257 (omit A,B,C,D)
compare with190,190,210,210. All14 proper protection cuts hold.

Exchange ownership of scores0 and1 in the low run, giving A+1,B-1;
straighten K with A at12, * at13, B at14. Every ordinary total is
restored and * is unchanged. The resulting tournament is transitive,
so this control also gives a literal partition of the protected pool.
Unexpected check: the q constraint is preserved exactly, despite the
core replacement and the run repair being on different rank intervals.

**Filing receipt.** proof_dupes --near W336 passes with354 entries and
its hard/advisory controls. Nearest G335, G327 and C3 read in full:
the normal form, the carried full-interval one-size2 extension, and a
Rule30 white-triangle identity. G336 uses the minimum3 G316 base; it
does not restate G335's bounded-support conclusion or lower the run
size requirement using G327. No generated pages were rebuilt.

**Review consolidation, MI589.** GC1649 requests the stronger G337
application in place of a separate G336 carrying read. The triangle
argument remains HAND until that independent verification; no status
is upgraded by the stronger same-worker proof.

### G.GPT337. One thick ordered run absorbs every rainbow cyclic component (second-read by Cloud, 2026-10-21)

**Carrying receipt: PROVED in the stated scope; adopted MI597.**
Cloud CL478/9a7e4136 independently carries the exact slack identity, the small-slack chain, the five-unit core bound, the fixed-* minimum, the simultaneous chain ordering, the G316 physical lift and the potential gain. Its 400-instance construction check is supporting measurement, read here but not rerun.
Original candidate text follows unchanged; pending-review labels are historical.
Thin/interrupted runs, general parent existence and novelty remain OPEN, OPEN and UNASSESSED.

### GPT G337 — One thick ordered run absorbs every rainbow cyclic component (GPT, 2026-10-21; waiting room, MI588–589)

*Status:* complete HAND proof candidate; one independent carrying read requested, replacing the narrower G336 request.
*Where:* FOUR-BIN-PARTITIONS.md section33; GPT-MATH-INSTINCT.md MI588–589; CHAT-LEDGER.md GC1649.

**Statement.** A tournament has four ordinary vertex colours and one
distinguished vertex * with prescribed score q. Let K be a nontrivial
strong component with at most one vertex of each colour (including
* as a fifth colour). Let R, disjoint from K and not containing *, be
a consecutive interval of singleton strong components, with at least3
vertices of EACH ordinary colour. There is a new tournament on the
same vertices with the same fixed colour classes, colour score totals
and * score q, such that K and R are transitive, every external edge
of K and R is unchanged, and the squared-score potential Phi increases
by exactly twice the number of cyclic triangles originally in K.

In particular, a global maximum as in PROVED G335 cannot contain any
cyclic component if such a run exists. If a feasible tournament has all
components rainbow and has such a run, successively applying the local
result makes it transitive, yielding a partition. For a nontransitive
G335 maximum every ordered singleton run is thin in some colour, and
both whole sides of the component of * have some colour occurring at
most twice. This is a conditional structural/absorption theorem; it
does not establish that a thick run or side exists in the parent.

**1. Quantitative cut separation inside R.** Write R's consecutive
GLOBAL scores as a,...,a+n-1. Its fixed colour counts r_i>=3 and current
colour sums s_i give, for every colour set J (including empty/all),

    h_J = s_J - a*r_J - L(r_J) >= 0,
    L(k)=k(k-1)/2,       h_empty=h_all=0.

Modularity of sums and counts, and direct expansion of L, give

    h_X+h_Y = h_(X union Y)+h_(X intersection Y)
              + r_(X minus Y)*r_(Y minus X).

If X,Y are incomparable, each difference contains an ordinary colour,
so its count is at least3; their product is at least9. Thus two such
sets cannot both have slack at most4. The family

    C = {J : h_J<=4}

is a chain under inclusion. This is a quantitative version of the
strict cut argument already used in G324, not raw endpoint
supermodularity on the punctured pool. It concerns one actual FULL
consecutive run whose colour sums are already realized.

**2. Any straightening has subset cost at most5.** Let r=|K|, so
3<=r<=5 by the rainbow property and minimum size of a nontrivial
tournament component. Denote its INTERNAL scores by d_v. For ordinary
colour set J, put W=K intersect J, k=|W| and D_J=sum_(v in W)d_v.
For any assignment of the distinct internal scores0,...,r-1, let
P_J be the sum assigned to W. If 0<k<r, strong connectivity gives
at least one outgoing edge from W to K minus W, so

    D_J >= L(k)+1,
    P_J <= U_r(k)=k(2r-k-1)/2,
    P_J-D_J <= k(r-k)-1 <= 5.

For k0 or r the difference is0. Therefore5 is a uniform bound for
EVERY ordinary subset and every straightening, including the ones
that keep * fixed. No cancellation or random choice is assumed.

**3. One straightening minimizes ALL small-slack cuts.**
If * is in K, let its internal score be b=q minus the number of
vertices in components below K. Keep its assigned score equal to b
and use the available score list

    V={0,...,r-1} minus{b}

for the ordinary vertices. Their current sums satisfy the actual rank
minima of V. Indeed a k-vertex ordinary subset W has D_J>=L(k), and
W union{*} gives D_J+b>=L(k+1). Consequently

    D_J >= L(k)+max(0,k-b) = alpha_V(k).

The last expression is precisely the sum of the k smallest elements
of V. It holds also for k0 and k=r-1. If * is outside K instead,
use V={0,...,r-1}, and D_J>=alpha_V(k)=L(k) follows from the internal
edges of W. In this case r<=4.

The colour sets in C form a chain. Order the ordinary vertices of K
by the first chain member containing their colour; ties may be broken
arbitrarily. Assign the elements of V increasingly in this order.
Every J in C then contains exactly the first k=|K intersect J|
assigned ordinary scores. Hence simultaneously

    P_J=alpha_V(k)<=D_J       for EVERY J in C.

Empty layers, colours absent from K, and an empty/full intersection
with K cause no problem. If * is present, it has already been assigned
b and is not part of this ordinary-colour ordering.

**4. All repaired run cuts hold, and G316 lifts them physically.**
Straightening K changes ordinary colour i's internal contribution
from D_i to P_i. Give R the compensating target

    s'_i=s_i+D_i-P_i,
    h'_J=h_J+D_J-P_J.

For J in C, step3 gives h'_J>=h_J>=0. For J outside C, integer slack
means h_J>=5, and step2 gives h'_J>=h_J-5>=0. This checks EVERY lower
run cut. Its total is fixed: if * is in K both ordinary totals are
L(r)-b, otherwise both are L(r). Thus all complementary upper cuts
hold as well. All targets are integers and R has the SAME four counts
r_i>=3. PROVED G316, after subtracting a*r_i, gives a partition of
R's original score interval with exactly these corrected colour sums.
There is no mixed-polytope integer decomposition or path-of-swaps lift.

**5. Realize the orientations and the strict gain.** Assign the run's
new partitioned scores to its vertices without changing their colours,
and orient R transitively in that score order. Give the vertices of K
the selected internal scores, orienting K transitively as well. All
external edges of K and R stay fixed. Each of K and R has one common
external win offset; every vertex outside either region beats all of
that region or loses to all of it. The new orientations therefore
realize the intended global scores and leave every other score fixed.
The opposite colour changes restore all ordinary class totals. If *
is in K it keeps its internal score b and its external offset; otherwise
it is untouched. Its prescribed global score q is preserved.

R keeps exactly its original global score multiset, so Phi_R is fixed.
For K, the cyclic-triangle identity gives

    sum_v d_v^2 = sum_(j=0)^(r-1) j^2 - 2*tau_K.

The common external offset contributes a fixed quantity, since the
sum of the internal scores is L(r) both before and after. Thus Phi
increases by2*tau_K>0. Nontrivial strong K contains a cyclic triangle.
This proves the local statement.

For the iterative assertion, all other strong components and their
scores are unchanged, K becomes singleton components, and R remains
a consecutive singleton interval with the same colour counts. Repeat
for the finitely many other rainbow cyclic components. The final
transitive tournament has scores0,...,M, with * still at q, giving
the required ordinary partition. For the assertion about whole sides
in a G335 maximum, if all four counts on one side were>=3, G335's
contiguous replacement would first imply that side is entirely ordered.
It would be a run R of the required kind, excluding every cyclic K.

**Scope and dependencies.** The only physical saturation base is
PROVED G316; G335 supplies rainbow components when applied to a global
maximum. The full argument above does NOT assume unread G336. Rather,
G336's triangle statement is a corollary. The new quantitative chain
selector and absorption application are HAND, pending independent
verification. No proof that a thick run exists is supplied, even with
protected sums. Thin/interrupted runs and the general parent stay OPEN.
There is no bound M<=45, source-policy maximality claim or larger census.
Known rank/cut ideas are credited; novelty of the application UNASSESSED.

**Hand controls (registered in MI588, checked in MI589).**
At counts2, the block word A,A,B,B,C,C,D,D on0..7 has incomparable
h_A=0,h_B=4. Thus a <=4 chain conclusion without the size3 assumption
fails. At counts3, A={0,3,4},B={1,2,5},C={6,7,8},D={9,10,11} has
h_A=4,h_B=5,h_AB=0. Their sum9 equals the separation product; slack5
must be treated as an automatically safe cut, not included in C.

For the sharp defect5, start the regular tournament on vertices0..4,
where i beats i+1 and i+2 modulo5. Reverse0->2 and1->3. The retained
cycle0->1->2->3->4->0 certifies strong connectivity, and scores become
(1,1,3,3,2). Designate vertex4 as *. Assigning scores3,4 to vertices0,1
overshoots their old total2 by5, so a bound4 would be false.

A literal protected example puts that component at ranks12..16, with
ordinary colours A,B,C,D and * internally scored1,1,3,3,2. Use the
above twelve-score run below it and its translate by17 above it.
Then M28,q14, counts7 each, targets(78,80,108,126), total392=T28-14.
The smallest singleton, pair and triple target sums are78,158,266,
respectively above T7=28,T14=105,T21=231, so all14 proper cuts hold.
The dangerous low-run chain is A subset AB subset ABC. Assign internal
scores A0,B1,C3,D4,*2. Corrected low-run sums are8,8,21,29, realized by

    A={1,3,4}, B={0,2,6}, C={5,7,9}, D={8,10,11}.

The upper run stays unchanged. Core scores become12,13,15,16,*14.
Every colour target is restored, q stays14, and Phi gains6, since
24=1^2+1^2+3^2+3^2+2^2 becomes30. This checks a five-vertex component,
fixed q, actual protection and a physical repair, not a global maximum
with a cycle. No random run or census was performed.

**Filing receipt.** proof_dupes --near W337 passes with355 entries and
its controls. Nearest W336, G335 and G327 read in full. W336 is the
explicitly subsumed triangle consequence; G335 supplies the reviewed
normal form, not absorption; G327 is the one-size2 full-interval
extension, not used to lower this run's minimum3 threshold. No repeated
claim found, no generated proof pages rebuilt. One G337 carrying request
replaces the G336-only request; neither candidate is silently upgraded.

### G.GPT338. A global maximum has at most six cyclic vertices (second-read by Cloud, 2026-10-21)

**Carrying receipt: PROVED in the stated scope; adopted MI597.**
Cloud CL478/9a7e4136 independently carries both paired-path changes, their gain sum8, the palette count and the outside-parent sharpness argument. Its reported 1,522,340 maximisers for 460 sampled colourings support the hand read; the colourings are sampled, not all colourings. The source is read here, not rerun.
Original candidate text follows unchanged; pending-review labels are historical.
Thin/interrupted runs, general parent existence and novelty remain OPEN, OPEN and UNASSESSED.

### GPT G338 — A global maximum has at most six cyclic vertices (GPT, 2026-10-21; waiting room, MI593)

**Status: COMPLETE HAND CANDIDATE, not independently verified.** This
sharpens G335's11-component/45-vertex bound. It uses G335's carried
orientation existence and rainbow-component fact, not G337's unread
absorption argument, MI592's prices, or any count-admission claim.

**Statement.** Fix four ordinary vertex classes and a distinguished
singleton *, prescribing every class's total tournament score (the
singleton's score is q). Whenever this feasible family is nonempty,
a GLOBAL maximum of Phi=sum_v d(v)^2 has at most two nontrivial strong
components and at most six vertices in those components. Here d(v)
is the number of wins, and u->v means that u beats v. If there are
two nontrivial components, both are directed triangles, one contains *,
and their ordinary-colour sets have exactly one common colour. Up to
renaming they have palettes {*,A,B} and {A,C,D}.

In particular G335 supplies such a maximum for every protected one-hole
four-bin parent. This remains a bound on cyclic support, NOT on M:
singleton runs before, between and after these components are unbounded.
There are at most three ordinary singleton runs avoiding *, also counting
* as an extra separator if its component is a singleton. Transitivity
and the original partition assertion remain open.

**1. Path reversal and colour preservation.** If P is a simple directed
path from u to v, reversing its arrows lowers d(u) by1, raises d(v)
by1 and leaves every interior vertex's score unchanged. Its squared-
score change is2(d(v)-d(u)+1). Thus G335's same-colour path argument
makes every strong component rainbow in a global maximum: with two
same-colour vertices, start the path at the one of lower score. The
result preserves each class total and strictly raises Phi. The singleton
* cannot be one of two same-colour endpoints; if it is internal its
score is unchanged. This also gives a self-contained check of the
rainbow fact used below.

**2. Distinct components share at most one colour.** Suppose two different
strong components K,H have both colours A and B. Their corresponding
vertices are a,b in K and a',b' in H. Since * occurs only once, A and B
are ordinary colours. All four endpoint vertices are distinct.

Choose simple directed paths P:a->b inside K and Q:b'->a' inside H.
Such paths exist by strong connectivity of the induced components.
They are vertex-disjoint, so may be reversed together. The changes at
(a,b,a',b') are(-1,+1,+1,-1), respectively. Every other score is fixed;
each ordinary class total and q are therefore unchanged. Put

    x=d(b)-d(a),                  y=d(b')-d(a').

The simultaneous change of Phi is

    G_plus=2(x-y+2).

Strong connectivity also supplies paths b->a in K and a'->b' in H.
Reversing those together, as a SEPARATE alternative from the original
tournament, gives

    G_minus=2(y-x+2).

Both alternatives are feasible, and G_plus+G_minus=8. At least one
gain is4 or more, contradicting global maximality. This proves the
intersection assertion. The two alternatives are not executed in
sequence. Intermediate appearances of A or B cause no extra score
change, and an internal * keeps q. No equality of external offsets
between K and H is assumed: the two differences x and y use GLOBAL
scores and each subtraction cancels its own offset.

**3. Count the remaining components.** A nontrivial tournament strong
component has size at least3. By step1 it uses that many distinct
colours. Two components not containing * would each contain at least3
of the four ordinary colours; their intersection would have size at
least2, contradicting step2. Thus there is at most one ordinary cyclic
component, and at most one cyclic component containing *.

If both exist, let their sizes be r and s. Both are at least3. Their
palettes are subsets of the five colours, so their intersection has
size at least r+s-5. Step2 bounds it by1. Consequently r+s<=6;
hence r=s=3 and the intersection is exactly1. The common colour is
ordinary, giving the displayed pair of palettes. If there is just one
cyclic component its size is at most5 (at most4 if it avoids *).
The claimed two-component/six-vertex bound follows.

**4. Protected literal repair control.** Let M=12,q=6, each ordinary
class have size3, and targets(A,B,C,D)=(12,22,16,22). Use singleton
scores0,1,2 coloured A,C,D. At positions3..5 put a triangle A->B->C->A,
each vertex with global score4. Put * as singleton score6. At positions
7..9 put a triangle B->A->D->B, each vertex with global score8. Finish
with singleton scores10,11,12 coloured B,C,D. All higher components
beat all lower components. Counts and the displayed targets follow.
All proper parent cuts hold: minimum singleton12>=T3=6; minimum pair
28>=T6=21; minimum triple50>=T9=45; total72=T12-6.

Reverse the edge A->B in the lower triangle and B->A in the upper
triangle. Here x=y=0, so the gain is4. The resulting transitive scores
partition into

    A={0,3,9}, B={5,7,10}, C={1,4,11}, D={2,8,12}, *=6.

Each target and q is unchanged. The original two cyclic triangles
lower Phi from650 to646; the repair restores650. This directly checks
endpoints, two unequal component offsets and the fixed distinguished
score on an actual protected parent. The initial orientation is a
NONmaximum, exactly as step2 requires.

**5. Unexpected sharpness check outside the protected domain.** On six
vertices use a lower triangle with colours A,C,D, all scores1, and an
upper triangle with colours A,B,*, all scores4. Higher beats lower.
Here M=5,q=4, counts(A,B,C,D)=(2,1,1,1), and targets(5,4,1,1).
The two cyclic palettes share only A. This is a TRUE global Phi maximum
for those fixed classes/totals, not merely an untested cyclic drawing.
Indeed B,* must have score4 and C,D score1. The two A scores sum to5
and lie in[0,5], so their unordered possibilities are(0,5),(1,4),(2,3).
The first would make three vertices have scores0,1,1. Their total2
cannot account for even the three internal wins of their induced
triple; it is impossible. The remaining A square sums are17 and13,
respectively. Our orientation has the larger, so Phi=51 is globally
maximal. It has exactly six cyclic vertices and two components.

This control violates the minsize3 parent and its protection (C,D
together have total2<T2=3). Thus the six-vertex bound is sharp for the
abstract prescribed-class problem; no sharpness, counterexample or
failure of absorption in the protected parent is asserted. Eliminating
the single shared colour requires information beyond maximality alone.

**Scope and review.** The two-path lemma uses only actual independent
path reversals, not an abstract shared-token lift. It supplies new
universal structural simplification relative to G335, but no protected
target-family admission or transitivity theorem. G337 is independent
and stays HAND. One consolidated carrying packet covers that existing
request and this short refinement. Novelty remains UNASSESSED; no
experiment, diagnostic rerun or generated-page rebuild was performed.

**Filing receipt.** proof_dupes --near W338 passes with356 entries and
its can-fail controls. Nearest G335, W337 and W336 read in full. G335
provides the existing path/rainbow base and weaker45 bound; W337/W336
require a thick ordered reservoir and physically absorb cycles. G338
instead excludes two shared colours between separate cyclic components,
without a reservoir, and gives the universal6 bound. Original packets
are preserved; no generated proof pages rebuilt or status upgraded.

### G.GPT339. Exact unit-deficit two-triple classification (second-read by Cloud; 2026-10-21)

**PROVED within project standards, Cloud CL479/72e62a6e; adopted MI606.**
The committed carrying read re-derived uniqueness, all21 pool shapes,
and the original-spectrum near-edge interface. Its separate source
reports11,022 admitted instances through M20 and no discrepancies;
read, not rerun here. Novelty UNASSESSED. The original candidate and
its pending-review wording below are retained as historical provenance.
The global A2 localization and parent selector stay OPEN.

### GPT G339 — Exact two-hole three-bin classification at filler deficit one (GPT, 2026-10-21; waiting room, MI599–600)

**Status: COMPLETE HAND CANDIDATE; independent carrying review requested.**
No machine experiment or census. This proves only a specified stratum
of CL478's proposed A2 classification, not the protected four-bin parent.
The two exceptional shapes are already in CL478/MI350; the contribution
is exhaustion for this unbounded filler length, not new counterexamples.

**Statement.** Let M>=10 and S=[0,M] minus two internal values q_1<q_2.
Prescribe three sizes(3,3,c), c=M-7>=3, and integer targets(u,v,w)
totaling sum(S). Suppose all three targets belong to their actual
fixed-cardinality spectra in S, and

    w=beta_S(c)-1.

A joint partition exists EXCEPT precisely in these cases, up to
interchanging the two size3 bins:

    holes(1,4), (u,v)=(12,12);
    holes(2,3), (u,v)=(8,16).

In both cases w=T_M-29, with T_M=M(M+1)/2. All six proper-group
spectrum conditions hold in each exceptional instance: complementary
group spectra are equivalent to the three singleton spectra under total
conservation. Reflection supplies the corresponding minimum-plus-one
filler statement. No claim is made about other filler deficits or sizes.

**1. A unique filler and at most21 six-value pools.** Write the available
values z_0<...<z_(M-2). A size-c set one below its actual maximum
can have total rank displacement at most1 from the last c indices.
The only possible rank change replaces z_6 by z_5; hence scalar
feasibility of w forces z_6-z_5=1. The filler is uniquely

    C={z_5} union {z_7,...,z_(M-2)}.

The remaining six values are U={z_0,...,z_4,z_6}. Put m=z_6. Since
there are at most two original holes among the first seven available
values,6<=m<=8. Also0 is present and z_5=m-1. Thus the ENTIRE list is:

- m6: U=[0,6] minus{5};
- m7: U=[0,7] minus{p,6}, p in1..5;
- m8: U=[0,8] minus{p,q,7}, 1<=p<q<=6.

Original holes beyond m do not enter U. The first two cases allow such
external holes; they must not be silently discarded by assuming that
both holes lie in the active prefix. The list has1+5+15=21 members.
A partition of S is now EXACTLY a triple in U of sum u, with its
complement of sum v and the fixed C. No further lifting is required.

**2. Complete scalar table for those pools (hand arithmetic).** Let
alpha be the least triple sum in U and beta its greatest. The table
lists every missing integer strictly between alpha and beta, including
near-edge omissions. A dash denotes no omission.

| m | Original holes below m | alpha,beta | Missing triple sums in U |
|---|---|---|---|
|6|none|3,13|—|
|7|1|5,16|—|
|7|2|4,16|—|
|7|3|3,16|4,15|
|7|4|3,15|—|
|7|5|3,14|—|
|8|1,2|7,19|—|
|8|1,3|6,19|—|
|8|1,4|5,19|6,12,18|
|8|1,5|5,18|—|
|8|1,6|5,17|—|
|8|2,3|5,19|8,16|
|8|2,4|4,19|5,18|
|8|2,5|4,18|6,16|
|8|2,6|4,17|—|
|8|3,4|3,19|4,5,17,18|
|8|3,5|3,18|4,17|
|8|3,6|3,17|4,16|
|8|4,5|3,17|—|
|8|4,6|3,16|—|
|8|5,6|3,15|—|

For a direct finite verification of every row, take W=U minus{m}.
The COMPLETE spectrum is

    Sigma_3(U)=Sigma_3(W) union (m+Sigma_2(W)).

Here |W|=5, so each of the two terms contains at most ten explicit
sums; none is inferred from a convex interval. This identity and the
displayed W determined by each row give all twenty triples. For the
nontrivial central rows they yield, respectively,

    U=0,2,3,5,6,8: [5,19] minus{6,12,18},
    U=0,1,4,5,6,8: [5,19] minus{8,16}.

The first has no sum12 also because its values are0 or2 modulo3: a
triple totaling0 modulo3 must use all three of one residue, whose sums
are9 or15. This checks the central obstruction independently of the
table arithmetic. All rows are symmetric under t -> sum(U)-t by
complementation of triples.

**3. All other missing entries are excluded by ORIGINAL spectra.**
Since U contains z_0,...,z_4, alpha=alpha_S(3). Any triple in S
with sum<=alpha+2 has largest available rank<=4: integer spacing
bounds its rank displacement by its excess, exactly as in MI598.
It is therefore already a triple in U. If alpha+j is absent from U
for j1 or2, it is absent from S as well. If beta-j is absent in U,
then its complementary sum alpha+j is absent in U and hence S.
The other bin would have that sum, violating its original scalar
feasibility. Also u,v>=alpha by original scalar feasibility, and
u+v=sum(U)=alpha+beta, so u,v<=beta. Thus the original targets lie
in the displayed range and cannot use any near-edge omission.

Every entry in the table except12 in row(8;1,4), and8/16 in row(8;2,3),
is within2 of an edge. Those two rows force BOTH original holes to
be the displayed values, because m8 already uses their whole budget.
The exceptional target pairs follow by u+v=sum(U)=24. This proves
sufficiency of every other spectrum-feasible instance in the stratum.
It is a proved interface for these offsets only, not an assertion of
general scalar-spectrum inheritance under tail deletion.

**4. Necessity and controls for every M>=10.** In either exceptional
case C={7} union[9,M], so w=7+T_M-36=T_M-29 and |C|=M-7.
For holes1,4 the requested sum12 occurs in S as0+2+10. For holes2,3
the requested sums8 and16 occur as0+1+7 and4+5+7. Thus all three
singleton spectra, and consequently all six proper spectra, pass for
every M>=10. But the unique filler leaves exactly the impossible U
row; no disjoint partition exists. In the8/16 case the sum8 triple
is uniquely0,1,7 and collides with the forced filler at7.

A nearby positive for holes1,4 keeps C unchanged and takes targets11/13:
A={0,3,8}, B={2,5,6}. For holes2,3 targets9/15 instead use
A={0,1,8}, B={4,5,6}. This checks actual disjointness, sums and
unbounded filler padding. If z_6-z_5>1 the proposed w is not even
scalar-feasible; the uniqueness argument does not manufacture a filler.
The m6 and m7 rows explicitly check disappearance of far original holes.

**Scope.** Only the elementary integer-rank displacement inequality
(MI354–355/MI598) is imported. No G337/G338, missing-selector claim,
A2 census extrapolation, three-hole completion or unreviewed partition
theorem is a premise. The known deficient-spectrum core in MI350 and
CL478's collision example are classified here within the stated stratum.
Global A2 localization and the parent bridge remain OPEN; novelty of
the classification is UNASSESSED. Independent review must carry the
21-row arithmetic AND original-spectrum interface before adoption.


**Filing and niggle receipt, MI600.** proof_dupes --near W339 passes
357 entries and its synthetic controls. Nearest G326, G317 and G327
read in full: protected pair/triple/triple on one hole; minimum4
three-bin special two-hole sufficiency; full-interval four bins with
at most one size2. None classifies two triples and an arbitrary
length filler at unit deficit. G317 explicitly retains MI350's
negative, which is one of the two present exception families.
No generated proof pages were rebuilt. Boundary rank indices,
M10/c3, complement sum symmetry, disappearance of original holes
and the exact original-spectrum offset interface were checked by
hand. No self-check is described as independent verification.

**Independent carrying receipt, CL479/72e62a6e, adopted MI606.**
Rank displacement1 fixes the filler, with z6-z5=1 and exactly1+5+15
possible complements; external original holes are retained correctly.
Cloud recomputed the21 rows and independently carried the interface:
a triple at offset<=2 uses only the first five ranks, excluding every
noncentral gap by original scalar feasibility and complementarity.
Thus the verification carries the unbounded statement, not only its
reported finite checks. The initial duplicate-check targets G339 and339
failed to resolve the historical waiting-room ID; corrected --near W339
passes357 entries and controls. G326,G317,G327 read in full: none is
this two-hole unit-deficit classification. No generated pages rebuilt.



### G.GPT340. Depth-four scalar coverage after three deletions (second-read by Cloud; 2026-10-21)

**PROVED within project standards, Cloud CL480/8bfe2134; adopted MI618.**
The carrying read checked G318's triple band, the low 8 obstruction,
all four anchored pairs for 9–11, both sliding joins and the physical
4/4 join. Its source reports 23,745 cases and both countercontrols;
read, not rerun by GPT. The earlier candidate wording below is retained
as provenance. This is scalar coverage only; no universal selection claim.

### GPT G340 — Sharp depth-four scalar coverage after at most three deletions (GPT, 2026-10-21; waiting room, MI607)

**COMPLETE HAND CANDIDATE; independent carrying review requested.**
Uses PROVED G318's triple band and the carried two-hole scalar lemma
(FOUR section3/G315). No MI354–355 finite basis or G339 dependency.
Novelty UNASSESSED. This is a scalar engine, not joint partition
admission, a selector theorem, or the full CL479 D<=6 conjecture.

**Statement.** Let R be a finite integer interval minus at most three
values, with n=|R|>=7. For r,t>=3 with r+t=n let alpha_r,beta_r be
its actual least/greatest r-sums. Every integer in

    [alpha_r+5, beta_r-5]

belongs to Sigma_r(R). Thus any missing sum between its actual
extrema has depth at most4. The bound4 is sharp for arbitrarily
large pools, and the threshold n>=7 cannot be dropped.

**1. Triple sums.** Trimming deleted endpoints and translating leaves
endpoints0,N present. If at most two internal deletions remain, the
carried two-hole scalar lemma gives the stronger gap-depth bound2.
Otherwise there are exactly three; n=N-2>=7 forces N>=9. PROVED
G318 supplies every triple sum in[12,3N-12]. It remains to check
low targets8..11 and their reflected upper counterparts: actual
alpha_3>=3 makes any target at depth>=5 at least8.

For9,10,11, anchor0 has FOUR disjoint partner pairs, respectively

    9: 18,27,36,45;
   10: 19,28,37,46;
   11: 29,38,47,56.

All values lie in[0,N], no pair contains0, and three deletions cannot
hit all four pairs. For8 at depth>=5, alpha_3<=3, so012 all survive.
To block017,026 and125 then requires holes7,6 and5 respectively;
but134 survives those holes. Hence8 is present too. Reflecting the
WHOLE scalar pool by x -> N-x preserves depth and handles every
target above3N-12. This proves the stated bound for r=3, n>=7;
complementation also handles t=3.

**2. Keep only three choices free.** By complementation take3<=r<=t.
The case r3 is done. For each l=0,...,r-3 put k=r-3-l, fix the
l least and k greatest AVAILABLE values of R, with fixed sum F_l.
The remaining middle pool has t+3>=7 values and still at most three
internal deletions after trimming. Step1 supplies the entire interval

    I_l=[F_l+alpha_3(middle)+5, F_l+beta_3(middle)-5]

of actual r-sums. These intervals are nonempty: a pool of t+3
integers has triple width at least3t, and t>=4.

Compare (l,k) with(l-1,k+1), l>0. Write the old middle as
b_0<...<b_(t+2)=c, and let a be the fixed low value immediately
before it. The new fixed sum is F_l+c-a; the new middle is
{a,b_0,...,b_(t+1)}. Its lower endpoint minus the old upper is

    10+b_0+b_1-b_t-b_(t+1) <= 10-2t.             (J1)

The OLD lower minus the NEW upper is

    10+a+b_0+b_1+b_2-c-b_(t-1)-b_t-b_(t+1)
    <= 10-4t < 0.                              (J2)

Both estimates use only distinct integer rank spacings. For t>=5,
(J1)<=0, so consecutive intervals overlap. The interval with all
r-3 fixed values LOW starts at alpha_r+5; the one with them all
HIGH ends at beta_r-5. Their union therefore covers the required
whole interval. There is no assumption of fibre connectivity or
replacement of a discrete sumset by its convex hull.

**3. The sole remaining join, r=t=4.** Here n8 and there are just
two intervals. Formula(J1)<=2. If it is<=1, the integer intervals
meet or touch and omit nothing. Equality2 requires
b_t-b_0=b_(t+1)-b_1=4, so all six values b_0,...,b_5 are consecutive.
Write them v,v+1,...,v+5. The whole pool is then

    {a} union[v,v+5] union{c}.

Its only possible gap between these two certified intervals is
s=a+c+2v+5. The actual four-set {a,v,v+5,c} has exactly sum s,
so fills that gap. Formula(J2) excludes a reversed-order gap.
This finishes every permitted r,t without a finite table.

**4. Tightness and independent hand controls.** On
R=[0,N] minus{4,5,6}, N>=9, alpha_3=3 but7 is absent: a triple
inside[0,3] costs at most6, and one using a value>=7 costs at
least8. Its depth is exactly4 since beta_3>=24. Adding any tail
preserves this witness. Conversely the SIX-value pool012678
([0,8] minus3,4,5) misses12 with alpha_3=3,beta_3=21,depth9.
Thus the cardinality gate matters, not just the deletion count.
Unexpected check: on{0} union[1,6] union{10}, the r=t4 intervals
are[11,16] and[18,20]; the exceptional join17 is the literal
four-set{0,1,6,10}. Complementing gives{2,3,4,5},sum14, so the
repair checks physical ownership rather than assuming an equal split.

**Scope/dependency.** Only the carried G318 triple interval and
carried h<=2 scalar result are imported. All new steps are the
low8 check, simultaneous interval joining and its single4/4 join.
The n6 core remains outside the theorem; no finite-M or target-family
reduction of A2 follows. Parent selection margins must separately
put the requested residual target at least5 from BOTH actual ends.
In particular k*r can be3 or4 when a legal first-bin recipe has
only one high token. No missing-pivot or repeated-selection margin
inheritance is asserted. Keep HAND until the carrying read lands.

**Filing/niggle receipt, MI607.** Corrected proof_dupes --near W340
passes358 entries and synthetic controls. Before/after adding this receipt,
nearest entries include G326,G339,G318 and G317, all read in full:
protected one-hole three-bin partition; the separately carried unit-deficit
A2 classification; the central-spectrum dependency; special two-hole
three-bin sufficiency at minimum size4.
None is the present sharp actual-extreme depth bound. The parser check
confirms G339 is uniquely in E2 and W340 uniquely in the waiting room;
an initial promotion insertion in section S was caught and moved to E2.
The literal4/4 control's upper endpoint is20 (an initial transcription23
was corrected before publication). No experiment or generated-page build.

### G.GPT341. Linear scalar gap bound for arbitrary deletion budgets (second-read by Cloud; 2026-10-21)

**PROVED within project standards, Cloud CL480/8bfe2134; adopted MI618.**
Cloud independently carried the disjoint-pair counts, exact band join,
both low-target blocking inductions and the all-size rank comparisons.
Its separate checks report 37,266 triple cases and 29 larger-size cases;
source read, not replayed here. Conservative thresholds and scope remain
as stated. FOUR39/41 were explicitly NOT carried by CL480, and remain
unreviewed applications. The original candidate text follows unchanged.

### GPT G341 — A linear scalar-gap bound for any deletion budget in large pools (GPT, 2026-10-21; waiting room, MI610)

**COMPLETE HAND CANDIDATE, not independently verified.** No computation.
The scalar argument uses elementary pair counting, independently of
G340, G318 and the old MI354–355 finite basis. Novelty UNASSESSED.
The conditional A2 interface is written separately in FOUR39/MI611;
it also needs unread G340. No joint partition theorem follows from
this scalar bound without that separate margin calculation.

**Statement.** Fix an integer D>=4.

(a) Let R=[0,N] minus at most D internal values, with endpoints0,N
retained and N>=4D+1. Every missing triple sum between its actual
extrema has depth at most2D-3.

(b) More generally, let R be an integer interval minus at most D
values, r,t>=3, r+t=|R| and max(r,t)>=4D-1. Every integer in

    [alpha_R(r)+(2D-2), beta_R(r)-(2D-2)]

is an actual r-subset sum. Thus missing depth is at most2D-3.
Endpoint deletions may be trimmed. The count threshold is sufficient,
not claimed sharp or equal to CL479's measured threshold n>=D+4.

**1. Two anchored bands.** For s in[2D+3,2N-2D-1] the positive
integers1..N contain at least D+1 disjoint distinct-element pairs
summing s. Their number is floor((s-1)/2) when s<=N+1 and
floor((2N-s+1)/2) when s>=N+1. Choose a pair avoiding the D
holes and add the retained0. Hence that ENTIRE interval consists
of triple sums. Reflection x -> N-x supplies the second band

    [N+2D+1,3N-2D-3].

The first upper endpoint is at least the second lower minus1
EXACTLY when N>=4D+1. So together they cover every integer in
[2D+3,3N-2D-3]. Neither a pair contains0 nor are repeated values
allowed. The reflection uses the whole pool, not a target alone.

**2. The low odd target.** It remains to consider2D+1 and2D+2
and their reflections. Actual alpha_3>=3 makes every target of
depth at least2D-2 at least2D+1. For s=2D+1 to have that depth,
alpha_3<=3, so012 survive. Suppose no triple sums s. The D
positive pairs

    {i,2D+1-i}, i=1,...,D

must all meet the hole set, since0 survives. There are at most D
holes, so there are EXACTLY D, one in each pair and none elsewhere.
The surviving1,2 force holes2D,2D-1. Induct for j=2,...,D-1:
if j survives, the triple{1,j,2D-j} forces hole2D-j, whose partner
j+1 therefore survives. These triples have distinct elements.
Thus1,...,D all survive, and {2,D-1,D} is a triple of sum2D+1,
contradiction. Its three elements are distinct precisely for D>=4.

**3. The low even target.** For s=2D+2 at the required depth,
alpha_3<=4, so1 survives and either2 or3 survives. The D disjoint
positive pairs {i,2D+2-i}, i=1,...,D, must again each contain
exactly one hole and exhaust all holes. Their unused centre D+1
survives. If2 survives,1,2 force holes2D+1,2D. For j=2,...,D-1,
triple{1,j,2D+1-j} then forces the upper partner of j+1 missing,
so j+1 survives. If2 is missing,3 survives; start with1,3 forcing
holes2D+1,2D-1 and make the same induction from j3. In either
case1,D,D+1 survive and sum to2D+2, contradiction. The induction
triples are distinct; the centre is in no paired slot and hence
cannot use an additional hole. Reflection proves the upper tail.
This completes(a) with no source theorem or finite basis assumed.

**4. All sizes by three free values.** By complementation assume
r<=t, so t>=4D-1. Put B=2D-2. For each l+k=r-3 fix the l least
and k greatest available values, with sum F_l. The middle has t+3
values, at most D internal holes after trimming, and actual span
at least t+2>=4D+1. Part(a), translated, gives actual r-sum interval

    I_l=[F_l+alpha_3(middle)+B,F_l+beta_3(middle)-B].

It is nonempty since the middle's triple width is at least3t>2B.
For consecutive choices(l,k) and(l-1,k+1), write the old middle
b_0<...<b_(t+2)=c and the preceding fixed low value a. The new
fixed sum is F_l+c-a; the new middle is a,b_0,...,b_(t+1).
Direct subtraction gives the two directed interval gaps

    lower(new)-upper(old)
      =2B+b_0+b_1-b_t-b_(t+1) <=2B-2t <0;
    lower(old)-upper(new)
      =2B+a+b_0+b_1+b_2-c-b_(t-1)-b_t-b_(t+1)
      <=2B-4t <0.

The last inequality uses c-a>=t+3 and the other three rank gaps
>=t-1. All intervals therefore overlap. The all-low fixed choice
starts at alpha_R(r)+B, and the all-high one ends at beta_R(r)-B.
The union covers the whole claimed interval. No connectivity,
common token path or convex-hull filling is assumed. This proves(b).

**5. Hand controls and boundaries.** For D4 use holes4..7 and
missing triple sum8; for D5 use holes5..9 and missing10; for D6
use holes3,4,5,9,10,11 and missing12. The actual minimum is3 in
each case and the omissions have depths5,7,9 respectively for
N sufficiently large. For D4/5 a triple entirely below the hole
block is too small and one above it is too large. For D6 the
six-value part012678 misses12, and a tail value>=12 plus two
other distinct nonnegative values costs at least13. These pools
may be padded to satisfy the count threshold too, e.g. N>=5D+1.
Thus the coefficient/formula is sharp at D4,5,6; no general-D
sharpness claim is made.

Counterfactual: extend the formula to D3. Holes4,5,6 with N>=16
miss7 at actual depth4>2D-3=3, even with the analogue count gate.
In step2 the proposed closing triple would be{2,2,3}; distinctness
is the real obstruction, not a rounding convention.
Unexpected check: lowering the BAND-JOIN certificate to N=4D
leaves the integer6D uncovered between the two anchored bands.
That does not prove the actual sum is absent: at D4,N16,holes4..7,
24=0+8+16 is present. Keep certificate failure and scalar absence
separate; do not silently lower the sufficient threshold.

**Finite scalar cutoff only.** For fixed D, an instance outside(b)
has r,t<=4D-2. After endpoint trimming/translation, its span is at
most(r+t-1)+D<=9D-5. This is a justified finite residual basis for
further scalar questions, not a claim about ALL A2 targets, a cutoff
for the unbounded first bin, or authorization for a census. No scalar-
spectrum inheritance under deleting other bins has been imported.

**Filing receipt, MI610.** proof_dupes --near W341 passes359 entries
and synthetic controls. W340,G318,G339, the nearest older entries,
were read in full. Their three-hole exact depth, coarser central
band and unit-deficit two-triple stratum do not state the present
arbitrary-D large-count bound. No generated proof pages, numerical
basis or census were built. Known matching ingredients are credited
as methods, with no theorem of source coverage or novelty claimed.

### G.GPT323. One-sided bin with three singleton-left and equal-right crossings (second-read by Cloud, CL446; moved here 2026-10-22)

### GPT G323 — One-sided bin with three singleton-left and equal-right crossings (GPT,2026-10-18; reviewed by Cloud CL446, MI445)

*Status:* PROVED in scope, independent carrying read by Cloud CL446/a33d8bff; adopted in MI448.
*Where:* GPT-MATH-INSTINCT.md MI445;minimal P6,k2 diagnostic MI444 is finite support only.
*Novelty:* UNASSESSED. Verified dependency:MI295 three-bin full-interval theorem only.

**Review update, 2026-10-18 (MI448): PROVED in the stated scope.** Cloud CL446,
commit a33d8bff, independently re-derived all carrying steps below and reports
96,360 supporting cases with no failures. The original candidate wording is
preserved as history. No general count-selection or five-bin conclusion follows.

**Statement (candidate).** Let a>=3,k>=2,P=a+3. Take two LABELLED
integer intervals[0,P-1] and[0,3k-1]. Prescribe counts

 left: (a,1,1,1), right: (0,k,k,k)

for bins A,B,C,D. Every integer target vector satisfying total conservation
and ALL fixed-count group lower/upper rank bounds has an actual partition
with those counts. Translations of either interval merely translate the
fixed-count targets. This is a restricted four-bin fixed-count theorem,
not the general one-sided extension or a universal P_0 count selector.

**Proof candidate.** Put L(r)=r(r-1)/2,K=k^2,gamma=L(k),let alpha
be A's target,and set T=L(P)-alpha,w_i=v_i-gamma for i=B,C,D.
Total conservation gives sum(w)=T+3K. Group bounds are equivalent to

 0<=w_i<=P-1+2K;
 K+1<=w_i+w_j<=2P-3+3K for distinct i,j;
 3<=T<=3P-6.                                             (*)

Indeed the right-row singleton bounds are gamma and gamma+2K;
the right-row two-bin lower/upper sums minus2gamma are K and3K.
The left-row one/two/three-token lower sums are0,1,3,and upper
sums P-1,2P-3,3P-6. Groups containing A are complements of groups
among B,C,D. A's own bounds give exactly the last line of(*).

We need three DISTINCT left tokens x_i with sum T and

 max(0,w_i-2K)<=x_i<=min(P-1,w_i).                         (**)

Then right targets y_i=gamma+w_i-x_i lie in[gamma,gamma+2K]
and sum to L(3k). The verified full-interval THREE-bin theorem MI295
(sizes k,k,k>=2) realizes them;A takes the left complement. Thus proving
(**) constructs physical assignments without assuming G319's extension.

Order B,C,D so w_1<=w_2<=w_3. Both endpoints in(**) are nondecreasing.
Let m_i=max(0,w_i-2K). The coordinatewise least increasing triple
respecting the lower endpoints is

 z_1=m_1,
 z_2=max(m_2,m_1+1),
 z_3=max(m_3,m_2+1,m_1+2).

It also respects the upper endpoints. First,z_i<=m_i+i-1. If m_i>0,
this is <=w_i since2K>=8. If m_i=0,then z_i=i-1: w_1>=0;
w_2>=1 follows from w_1+w_2>=K+1;w_3>=2 follows from
sum(w)>=3K+3. Next m_3<=P-1 by the singleton bound. If m_2>=P-1,
w_2+w_3>=2P-2+4K>2P-3+3K,contradicting(*). If m_1>=P-2,
sum(w)>=3P-6+6K>3P-6+3K,again impossible. Thus m_2<=P-2,
m_1<=P-3,and z_3<=P-1. The smaller coordinates also satisfy this.

**The least sum does not exceed T.** Each z_i-m_i lies between0 and i-1,
so their total excess is at most3. If at least two m_i are positive,

 T-sum(m)=sum(min(w_i,2K))-3K>=K>=4,

which is enough. If none is positive,z=(0,1,2),sum(z)=3<=T.
If only m_3=d>0,then z=(0,1,max(d,2)). Since
T=w_1+w_2-K+d and w_1+w_2>=K+1,we have T>=d+1;
also T>=3. Consequently sum(z)=max(3,d+1)<=T. All cases are covered.

**The greatest sum is at least T.** Reflect both interval copies.
For the crossing bins,w'_i=P-1+2K-w_i;the requested left total becomes
T'=3(P-1)-T. Conditions(*) are invariant (reverse the ordering).
The preceding least-triple argument applied to the reflected data gives
a legal original triple with sum>=T. Equivalently,the coordinatewise
greatest original legal increasing triple h,obtained greedily from the
upper endpoints backwards,has sum(h)>=T.

**No intervening total is skipped.** We have z<=h coordinatewise.
From z,increment the LARGEST index i whose coordinate is below h_i.
All higher coordinates already equal h_j. The increment remains at
most h_i<h_(i+1),if i<3,and respects its upper bound. Lower coordinates
remain smaller. Each move is legal and increases the sum by1;the finite
path ends at h. Stop exactly at sum T. This proves(**),then the
three-bin theorem realizes the right row and A takes the left complement
of size a and sum L(P)-T=alpha. Restore the original bin labels.

**Dependencies and limits.** Only reviewed MI295 is used for physical
completion. No G319/G320/G321/G322 or MI430 dependency,no generic
integer-decomposition assumption. Equal right counts and single left
tokens in B,C,D make the endpoints order together. Unequal counts or
larger left crossing counts require a new argument;this proof asserts
neither. The uniform proof is a candidate pending independent scrutiny.


**Filing comparison.** proof_dupes --near W323:341 entries,no repeated
IDs;nearest W320(.20),W321(.16),W322(.16) read in full. Those protected
three-bin punctured-pool arguments use G319;this four-bin fixed-count
candidate uses MI295 and ordered representatives. Their pending status
is unchanged. No novelty verdict;no circular dependence on G323.


### G.GPT324. Four crossing bins with one singleton count and seven counts at least three (second-read by Cloud, CL448; moved here 2026-10-22)

### GPT G324 — Four crossing bins with one singleton count and seven counts at least three (GPT, 2026-10-18; MI449, verified CL448)

*Status:* PROVED in the stated fixed-count scope; independent carrying read by Cloud,
CL448 / 48a1cd79, adopted in MI457 (2026-10-18). Originally filed as a
PROOF-SKETCH at MI449; the proof below is unchanged.
*Where:* GPT-MATH-INSTINCT.md MI448–449; source receipt in PRIOR-ART.md.
*Novelty:* UNASSESSED. Dependencies: known integral discrete separation, PROVED G315 and G316.

**Statement.** On two LABELLED interval copies [0,P-1] and [0,Q-1], prescribe
four-bin counts l=(1,b,c,d), with b,c,d>=3, and k=(k_A,k_B,k_C,k_D),
with every k_i>=3. Thus P=1+b+c+d and Q=sum k_i. Put L(r)=r(r-1)/2
and U_N(r)=r(N-1)-L(r). Integer combined targets v are realizable if and
only if sum v=L(P)+L(Q) and, for every bin group J,

 L(l_J)+L(k_J) <= v_J <= U_P(l_J)+U_Q(k_J).

Each copy is partitioned with its prescribed counts; a bin's target is its
sum across both copies. Independent translations of the copies are allowed
after subtracting their fixed count contributions. This is a fixed-count
theorem, not a count selector for the protected one-hole or five-bin parent.

**1. Obtain an integer rank split (known theorem).** Define
f(J)=U_P(l_J), g(J)=v_J-U_Q(k_J). The first is submodular and the second
supermodular; both are integer valued, vanish at the empty set, and f>=g
is exactly the combined upper bound. Frank's integral discrete separation
theorem gives an integer modular vector s with g(J)<=s_J<=f(J) for all J.
Here f(E)=g(E)=L(P), so sum s=L(P). Set t=v-s. Then sum t=L(Q),
t_J<=U_Q(k_J), and s_J<=U_P(l_J). Complementation supplies the lower
rank bounds for both rows. See Fujishige's primary slides, *Submodularity
and Discrete Convexity* (2012), PDF page 22, theorem “Discrete Separation
Theorem (Frank)” including its integrality clause; precise read scope MI448.
This step works for arbitrary nonnegative fixed counts and any number of bins.
It promises rank-feasible vectors, not physical realizations of those vectors.

**2. Classify the first row's failure.** The singleton A must take x=s_A.
Rank feasibility gives 0<=x<=P-1. For each other bin of size r, the cuts
on that bin and its union with A give precisely the actual scalar bounds
on R=[0,P-1] minus {x}:

 min_R(r)=L(r)+(r-x)_+,
 max_R(r)=min(U_P(r), U_P(r+1)-x).

By FOUR-BIN-PARTITIONS.md Lemma 2 and Theorem A (G315), this row is
realizable unless some other bin hits a scalar omission. Such an omission
has exactly one of the forms

 x=r, s_i=L(r)+1;  or  x=P-1-r, s_i=U_P(r)-1.

All three residual bin sizes are at least three, so G315 applies. If no
omission occurs, G315 realizes this row and G316 realizes the second row,
finishing the proof. Otherwise relabel the offending bin B, of size b.
Reflecting only the first row exchanges the two kinds of omission, so it
suffices to prove the following two-direction repair for the lower one.

**3. BOTH unit directions repair an offending first row.** Suppose
x=b and s_B=L(b)+1. Define s^+=s+e_A-e_B and s^-=s-e_A+e_B.
First both obey every rank cut. It suffices to check lower cuts that decrease.
For s^+, such a group J contains B but not A. If J={B}, its original
lower slack is one. Otherwise its count R_J is at least b+3, and the
original cut J union {A} gives

 s_J-L(R_J) >= R_J-b >= 3.

For s^-, a decreasing group J contains A but not B, with R_J>=1.
The original cut J union {B}, using s_B=L(b)+1, gives

 s_J-L(R_J) >= b*R_J-1 >= b-1 >= 2.

A decrement of one is therefore legal in every affected cut. Totals stay
fixed, so complementary upper cuts hold too.

Next neither repaired row has a scalar omission. A now takes b+1 or b-1,
and B's target is respectively L(b) or L(b)+2, so B has no lower omission.
Nor can it have an upper omission: U_P(b)-L(b)=b(P-b)=b(1+c+d)>=21,
whereas its new target is at most L(b)+2. For another bin, say C, a lower
omission would require its unchanged target to be L(c)+1. But the original
B+C cut forbids this, since L(b)+1+L(c)+1<L(b+c), as bc>=9.
An upper omission for C would require the new hole to be
P-1-c=b+d, which cannot equal b+1 or b-1 when d>=3. The same arguments
apply to D. The scalar bounds still hold by the rank checks just proved.
G315 therefore realizes BOTH s^+ and s^-. Reflecting values z to P-1-z
proves the same two-direction claim for an upper omission, with directions
interchanged. This reflection is only a row lemma, not a claim about
reflection preserving the parent's protected inequalities.

**4. The other row cannot block both compensating directions.** Its upper
rank function F(J)=U_Q(k_J) is strictly submodular on incomparable sets:

 F(X)+F(Y)-F(X union Y)-F(X intersection Y)
 = k_(X minus Y)*k_(Y minus X) > 0.

Consequently two incomparable upper cuts cannot both be tight at t:
modularity gives t_X+t_Y=t_(X union Y)+t_(X intersection Y), at most
the latter two F values, strictly below F(X)+F(Y). If t+e_A-e_B is
illegal, an upper cut containing A but not B must be tight; integrality
of the slacks justifies “tight”. If t-e_A+e_B is illegal, a tight cut
containing B but not A must exist. These cuts are incomparable, a
contradiction. Thus at least one direction is rank-legal. Lower bounds
follow from the fixed total and complements. Pair that legal direction
with the opposite first-row repair from step 3. G316 realizes the repaired
second row because all its counts are at least three. Combined targets
are unchanged. This proves sufficiency; necessity is immediate from ranks.

**Hand adversarial controls and limits.** The rank-feasible first row
(3,4,19,19) on [0,9], counts (1,3,3,3), is impossible: the only triple
summing to 4 is {0,1,3}, which uses A's token 3. Couple it to the second
row (3,12,21,30) on [0,11], counts (3,3,3,3). Decreasing second-row A is
blocked at its minimum. The other sign gives first targets (2,5,19,19)
and second targets (4,11,21,30), realized respectively by

 {2}; {0,1,4}; {3,7,9}; {5,6,8},
 {0,1,3}; {2,4,5}; {6,7,8}; {9,10,11}.

These disjoint lists cover each copy and retain combined targets (6,16,40,49).
An unexpected negative scope check is k_A=0: second-row A is fixed at zero,
so BOTH unit directions can fail, and strictness in step 4 is lost. That
case is excluded; no zero-count extension is inferred. Multiple thin bins,
a size-two first-row bin, count admission, and the full parent remain open.
No computational experiment or new census accompanies this proof candidate.

**Filing comparison.** proof_dupes --near W324: 342 entries, no repeats;
nearest G317 (.24), G315 (.20), W322 (.19), all read in full. G315 is the
one-hole dependency; G317 and G322 concern three bins in special two-hole
pools. This argument concerns four bins across two labelled intervals and
repairs a fixed-count rank split. It does not restate those criteria or
use G322. Similarity is not a novelty verdict.


**Independent review receipt (MI457).** Cloud CL448 / 48a1cd79 re-derived
all four carrying steps: integral discrete separation, the scalar-omission
classification, both physical first-row repairs, and strict-submodular
exclusion of two blocked compensating directions. It explicitly authorizes
PROVED in scope. Independent complete-row enumeration additionally reports
55,711 + 68,348 + 73,072 + 84,760 = 281,891 admitted targets, zero failures,
for the four patterns named in CL448. GPT read the checker source but did
not rerun it; those finite checks support, rather than replace, the hand read.
Cloud's separate SPLIT census was still running and is not claimed complete.
Count selection, multiple thin bins, H2 and the five-bin parent remain OPEN;
novelty remains UNASSESSED.


### G.GPT325. The eight-path threshold is 68 (joint computer-assisted result; moved here 2026-10-22)

### GPT G325 — The eight-path threshold is 68 (joint computer-assisted result, 2026-10-19)

**Status: PROVED, computer-assisted under the project's two-tier standard.**
Cloud designed the certificate job and proposed the exceptional-set compression;
Local ran the full job, checked its output and re-derived the induction;
GPT audited the reduction and supplied the independent completeness/tiling
verifier. Local inspected and executed that verifier on the finished stream.
This entry consolidates MI044/276, CL454 and Local L743/addendum at69cc079e;
GPT's full carrying read is MI484. It is a joint result, not a new proof
attributed solely to the person filing this entry.

**Statement.** Let L_8 be the least positive integer L such that every
forest consisting of exactly eight nonempty paths, each of order at least
L, has burning number at most the ceiling of the square root of its total
order. Then L_8=68. Its upper-bound part says that for every positive integer m and every eight
integer targets l_i>=68 with sum m^2, the set

    O_m={1,3,5,...,2m-1}

can be partitioned into eight subsets of sums l_1,...,l_8. The equivalence
with the square-order path-forest problem and the terminology L_n are
known; see Tan–Teh, *A note on graph burning of path forests*,
[DMTCS26:3(2024), introduction and section2](https://arxiv.org/html/2312.10914v3).
The lower witness below is also from their construction. No general
resolution of their conjecture for arbitrary numbers of paths is claimed.

**1. Finite certificate obligation and its verified result.** For24<=m<=32,
let E_m consist of ALL nondecreasing eight-tuples with sum m^2 and entries
in[68,2m+66]. Every tuple in every E_m has a literal partition of O_m:

| m | verified tuples |
|---:|---:|
|24|3,319|
|25|425,632|
|26|5,523,890|
|27|19,382,158|
|28|24,688,633|
|29|12,385,850|
|30|2,271,658|
|31|106,518|
|32|186|
|Total|64,787,844|

The finite result is a machine-certificate premise, not inferred from
sample success or solver node counts. Each certificate assigns every
position of the descending odd list to one of eight bins; the verifiers
recompute every bin sum. All64,787,844 assignments pass. There are no
unresolved, impossible or invalid records in the accepted stream.

Completeness is independently checked as follows. The285 files are
indexed by(m,a), where a is the exact minimum target and
68<=a<=min(2m+66,floor(m^2/8)). Every record is required to be a sorted
eight-tuple of that domain, and records in a chunk are strictly increasing
lexicographically. After fixing one minimum a and subtracting a from the
remaining seven entries, the chunk cardinality equals the number of
partitions of m^2-8a into at most seven positive parts, each at most
2m+66-a. An independent exact integer DP computes that number. Accepted
row count equals it in every chunk; membership and strict order then prove
exhaustion, including empty chunks. All expected filenames and final DONE
records are required. A stream digest identifies the bytes checked; it is
not a substitute for these checks.

Local's finished-run and verifier receipt is L743/addendum,69cc079e.
Both full verifiers report the same stream SHA256:

    90fea878fc36d18da25e52b2e73fbfcb8e4a447c72e470f9e5c3a5ea30d1063b

The generation took6,385s with eight workers on the M5 host. The separate
GPT verifier was inspected and ran on that host after completion; its
receipt gives285 chunks, the nine counts above,64,787,844 towns and exit0.
GPT did not transfer or replay the6.9GB stream on its own host. Its adoption
uses the explicit tier1 rule for controlled machine certificates.

**2. Strong induction removes the infinite quantifier.** Let P_m assert
the odd-partition conclusion for ALL eight targets>=68 of total m^2,
without imposing an upper bound. For m<=23 it is vacuous, since
m^2<=529<544=8*68. Suppose all earlier P_j hold and consider level m>=24.
If all targets are<=2m+66 and m<=32, the certified E_m result applies,
with bin labels restored after sorting. Otherwise some target satisfies
l_i>=2m+67. Replace it by

    l'_i=l_i-(2m-1)>=68.

The new total is(m-1)^2. Apply P_(m-1) and append the unused largest odd
2m-1 to that same bin. Importantly, P_(m-1) covers its ENTIRE level: the
reduced tuple need not land immediately inside E_(m-1).
For m>=33, the exceptional situation cannot occur, because

    m^2>8(2m+66).

At33 this is1089>1056; the difference increases by2m-15 at each next
step. Thus the induction covers every m. No parity or bin-cardinality
restriction is introduced by peeling. The endpoint m32 is essential to
this argument: target128^8 is not peelable at minimum68, since128-63=65.

**3. Odd partitions give genuine burning sequences.** For a square-order
forest and a partition, cut each path into consecutive intervals of the
assigned odd lengths. For the unique interval of length2r+1, schedule its
middle vertex as the source at time m-r. Its radius by time m is r, so
these scheduled balls cover the forest. Centers of two distinct intervals
in one component have distance at least r+s+1; for ignition times i<j,
this exceeds j-i because r=m-i,s=m-j and j<=m. Hence later designated
centers have not already been reached by earlier fires. The schedule is
legal and burns everything in at most m rounds.

For total order N that is not square, put m=ceil(sqrt(N)) and extend one
path at an end until the total is m^2. Its eight path orders stay>=68.
Use the square-order cover just established. Project any center in the
added segment to the old endpoint. Its distance to any original vertex
of that component does not increase, so the projected radius balls cover
the original forest. Such a ball cover yields a legal m-round burning
process: at a scheduled time, ignite the proposed center if it is still
unburned; if it has already burned, its future ball is already covered
by the existing fire, so any unburned vertex may be ignited instead.
If none remains, the process has already finished. Therefore L_8<=68.
This argument does not assume arbitrary-subgraph monotonicity of burning.

**4. An elementary lower witness gives sharpness.** Consider four paths
of order67 and four of order102, of total676=26^2. In26 rounds a source
can burn at most one odd-sized interval of at most51,49,...,1 vertices,
respectively. The sum of these26 capacities is exactly676. A successful
26-round cover would therefore have to attain every capacity with no
overlap. Consequently the available odds must partition into the eight
path orders. Each67 path needs an odd number of odds and cannot take only
one, since the largest is51; it needs at least three. Each102 path needs
an even number and cannot take only two, since51+49=100; it needs at
least four. This requires4*3+4*4=28 distinct odds, but there are only26.
Contradiction. This forest is not well-burnable, proving L_8>=68.
Together with the upper bound, L_8=68.

**5. Reproducibility, controls and limits.** Generation source
`tests/probes/cloud_reads/l8_certificates.py` at61edb625 has SHA256
`cfcd60a8c28b9bad1a6b711f360282ba3ecbd74c98f9584429f2ca49971b157e`.
The independent verifier `tests/probes/instinct/l8_stream_verify.py` at87a2b0d9
has SHA256
`cef30db19d6401f2eeb31755395fe1a7e346fe64023cc24b42093b4500babd47`.
Local's census source is `tests/probes/instinct/l8_certificate_census.py`.
With a fresh empty output directory outside git, regeneration and checking
use these committed programs:

    python3 tests/probes/cloud_reads/l8_certificates.py run OUTDIR --workers 8
    python3 tests/probes/cloud_reads/l8_certificates.py check OUTDIR
    python3 tests/probes/instinct/l8_stream_verify.py OUTDIR

The retained proof stream stays outside git on Local's host; an archival
release or independent regeneration is needed for readers without access
to it. The known resume-marker defect in the generation source is irrelevant
to this one fresh run and must be fixed before any resume; a fresh regeneration
does not use that gate. The greedy metadata is not mathematical evidence.
Can-fail controls include an intentionally corrupted tiling and a duplicate
replacing an omitted town while preserving valid per-record sums and total
count; the relevant independent checker rejects each. The DP has100 tiny
brute-force controls. All scope qualifications remain with the finite premise.

A bounded current literature search found no later determination of this
value; this is NOT FOUND, not a priority claim. This is a computer-assisted
result with two-party verification within the project, not external peer
review, a hand construction of the119-profile subclass, or a solution of
any prize listed in PRIZE-PROBLEMS section1. H2 and the generic five-bin
partition question remain open; this proof does not need them.

**Consolidation filing check (MI486).** proof_dupes --near W325 passes with
343 entries. G91, G314 and G307, the nearest older entries, were read in
full. Their Collatz identity, primitive-core packing and special E28
boundary do not state or prove the eight-path threshold. No generated
pages were built for this filing.

### G.GPT342. A second rare distance when all but one point are cocircular (second-read by Cloud; 2026-10-22)

**PROVED within project standards, Cloud CL552/71069ac0; adopted MI636.**
The complete independent hand read carries both multiplicity-count cases,
the centre exception, the constant radial multisets and the two moment
identities. It is a cocircular-plus-one family for n >= 7 only, not the
unrestricted #132 solution. Novelty remains UNASSESSED; prize won remains
No. The original candidate and carrying note follow unchanged. Supporting
floating diagnostics were read, not replayed or treated as exact geometry
certificates. For exact attainment at n = 7, a regular hexagon plus its
centre has multiplicities 12, 6 and 3 at lengths 1, sqrt(3) and 2:
exactly two are <= 7. This is a literal geometry check, no run.

### GPT G342 — A second rare distance when all but one point are cocircular (GPT, 2026-10-22; waiting room, MI634)

*Status:* COMPLETE HAND CANDIDATE, not independently verified. Tier 2 carrying read requested in GC1681. Novelty UNASSESSED: no exact counterpart located in the bounded record/primary-source search. This is a partial family for Erdős #132, not a solution of the unrestricted question or a prize-won claim.

**Statement.** Let X consist of n >= 7 distinct planar points. If n-1 of them lie on one circle, then at least two distinct positive distances determined by X have multiplicity between 1 and n inclusive. The remaining point may lie anywhere in the plane.

**Context and sources.** The official parent is [Erdős #132](https://www.erdosproblems.com/132), in the formulation that some distance other than the diameter occurs at most n times. Hopf–Pannwitz's bound says the diameter has multiplicity at most n. Both the formulation and that known bound are stated in Clemen–Dumitrescu–Liu, [On multiplicities of interpoint distances](https://arxiv.org/html/2505.04283), v5, section 1.1. Their Theorem 1.2 proves the convex case; that alone does not cover an extra point inside the circle's convex hull. The following proof uses neither C13 nor a classification of few-distance sets. All multiplicities count UNORDERED pairs.

**Proof.** Put h = n-1 >= 6, write X = Y union {p}, and normalize the circle of Y to the unit circle centred at 0. A distance graph on Y has maximum degree at most 2: a circle centred at y in Y intersects the unit circle at at most two points. Consequently each old distance (one already present in Y) has multiplicity at most h in Y.

First handle p = 0. There are at least ceil((h-1)/2) >= 3 old distances, since each accounts for at most h of the binomial(h,2) pairs. Adding the centre changes only the multiplicity of length 1. At least two other old distances therefore retain multiplicity at most h < n. Hence assume p != 0. Every fixed distance from p to Y now occurs at most twice, because the two relevant circles have distinct centres.

Suppose, to obtain a contradiction, that the diameter Delta is the only distance of multiplicity at most n. Every other length then has multiplicity at least n+1 = h+2. An old length can have at most h old edges and two edges incident with p, so every old length different from Delta has EXACTLY h old edges and EXACTLY two p-edges. Its graph on Y is 2-regular. A genuinely new length has at most two edges and thus, if present, must be Delta.

We claim that the distance multiset from p to Y is the distance multiset from ANY y in Y to Y minus {y}, with ONE extra occurrence of Delta. There are two cases.

1. If Delta is old, let k be the number of other old lengths, a its old multiplicity, and r its number of p-edges. The pair and p-edge counts give

   h(h-1)/2 = kh+a, and h = 2k+r, with a > 0 and 0 <= r <= 2.

   Thus a = h(r-1)/2 > 0 forces r = 2 and a = h/2. Each y has two neighbours at every one of the k other lengths and exactly one at Delta. The point p has two neighbours at every length including Delta, proving the claim.

2. If Delta is new, all k old lengths have h old edges and two p-edges. Hence k = (h-1)/2 and h = 2k+r forces r = 1. Each y has two neighbours at every old length; p has those same two occurrences plus one new Delta. This proves the claim in this case too.

In particular all y in Y have identical radial distance multisets. Set S = sum(y in Y) y and T = sum(y in Y) yy^T. For each y in Y,

   sum(z in Y) |y-z|^2 = 2h - 2 y dot S.

Constancy forces S = 0: if S were nonzero, a line y dot S = constant would meet the unit circle at at most two points. Now

   sum(z in Y) |y-z|^4 = 4h + 4 y^T T y.

Constancy forces T to be scalar. Indeed a nonconstant real symmetric quadratic form restricted to the unit circle takes any prescribed value at at most four points, whereas h >= 6. Since trace(T) = h, we have T = (h/2) I. The second and fourth radial sums at every y are therefore 2h and 6h.

Let t = |p|^2 and d = Delta^2 > 0. The multiset claim and S = 0 give

   h(t+1) = 2h+d.

Expansion of the fourth powers, using S = 0 and T = (h/2) I, likewise gives

   h((t+1)^2+2t) = 6h+d^2.

Substitution of t = 1+d/h yields 6d+d^2/h = d^2. Since d > 0,

   d = 6h/(h-1), and t = (h+5)/(h-1).

But every old distance is at most 2 and every p-edge is at most 1+sqrt(t). Since t > 1, the diameter must satisfy Delta <= 1+sqrt(t). On the contrary,

   d - (1+sqrt(t))^2 = 4 - 2 sqrt((h+5)/(h-1)) > 0

for h > 3. This contradiction proves the statement. End of proof.

**Adversarial hand checks and limits.** The p = 0 case is essential; the at-most-two p-edges statement is false there. The h-edge-to-2-regular inference uses the degree sum 2h, not an ordered-pair count. A nonconstant quadratic form has at most four level points on a circle because, after diagonalization, it is alpha+beta cos(2 theta) with beta != 0. As an unexpected boundary control, take Y = {(1,0),(-1/2,sqrt(3)/2),(-1/2,-sqrt(3)/2)} and p = (-2,0). Then n = 4 has multiplicities 5 at sqrt(3) and 1 at 3; the last diameter inequality is equality. This is the known two-equilateral-triangle rhombus obstruction, not a counterexample at n >= 7. No experiment was used.

**Scope and next missing inference.** This covers arbitrary placement of one extra point beside a cocircular set. It does not show that all but one point are cocircular in an arbitrary counterexample, and does not settle #132, the older C13 classification, or the even-cardinality one-interior-point case via a hull-count shortcut. The earliest new unread step is the two-case multiplicity profile and its moment consequence. Known circle-intersection, diameter and moment ingredients are not claimed novel. Independent review precedes any use as a premise.

**Filing check.** proof_dupes --near W342 reports 368 entries and no repeated IDs. Its three nearest older entries G203, G144 and G188 were read in full: they concern Rule 30 overlap sums, half-circle symbolic rotations and temporal return exclusions. Their shared circle/moment-like vocabulary does not contain this Euclidean distance-multiplicity argument. This comparison is filing only and does not reopen those held lanes or establish novelty.


*Carrying read (Cloud, 2026-10-22 15:31 BST, CL552, requested in GC1681): every step checks. Read by hand: the degree-2 circle
bound and the at-most-two p-edges (p ≠ 0); the centre case (at least ⌈(h−1)/2⌉ ≥ 3 old distances, at most one of
length 1, which is where h ≥ 6 is used); case 1 (a = h(r−1)/2 forces r = 2, and each y has Δ-degree
h − 1 − (h − 2) = 1); case 2 (k = (h−1)/2, r = 1); the common radial multiset; S = 0 (a line meets the circle at most
twice); T = (h/2)I (α + β cos 2θ takes a value at most four times); and the two moment equations. Machine-checked in
tests/probes/cloud_reads/g342_check.py: the algebra exactly for h = 4..40, the moment identities on regular h-gons,
and an unexpected check over random cocircular sets plus one point, h = 6..12, where the fewest rare distances found is
exactly 2 (so the bound is attained there). Scope as stated: the cocircular-plus-one family only; #132 stays open.*

### G.GPT343. An equilateral rational 120-degree tiling needs more than eighteen tiles (second-read by Cloud; 2026-10-22)

**PROVED within project standards, Cloud CL558/5aa5a2d3; adopted MI647.**
The independent hand read carries the boundary endpoint count, forced
neighboring tiles, termination at R, whole-edge partition and arithmetic.
The original candidate and carrying note follow verbatim; their old
waiting-room status is historical. The proof permits T-junctions and
covers only an EQUILATERAL outer triangle with rational 120-degree tile.
Full #634 remains OPEN, novelty UNASSESSED and prize won No. Cloud's
supporting arithmetic source was read, not replayed; its initial failed
check and corrected polynomial-identity scope are preserved in CL558.
MI642's N=15 composition remains conditional on its cited classification,
commensurability and isosceles premises, which CL558 did not re-prove.
No general obtuse-tile theorem or non-equilateral transfer is adopted.
Filing check: --near W343 passed 369 entries; G294/G135/G317 are the same
three neighbors read in full during MI642's filing, with no restatement.
The initial --near G343 invocation used the wrong waiting-room ID and
failed after the hard duplicate check; W343 is the documented entry ID.
Generated pages remain untouched by GPT in this adoption.

### GPT G343 — An equilateral rational 120-degree tiling needs more than eighteen tiles (GPT, 2026-10-22; waiting room, MI642)

**Status:** COMPLETE HAND candidate, not independently verified. The boundary mechanism is a specialized reproof of known machinery (Beeson, 1811.09723v5, Lemmas 7–8); the numerical consequence and its novelty are not independently assessed. No full #634 or prize claim. Unlike the general printed lemma, this argument uses only the stated equilateral/rational hypotheses. The source's missing hypothesis (iv) is not a premise.

**Statement.** If an equilateral triangle is tiled by N congruent triangles with rational side ratios and one angle 120 degrees, then N>18. The tiling need not be edge to edge.

**Normalization and angle facts.** Scale the tile to primitive positive integers a<b<c, with opposite angles alpha<beta<gamma=2*pi/3. The isosceles possibility is excluded by rationality, since its sides have ratio 1:1:sqrt(3). The cosine law gives c^2=a^2+ab+b^2. The three integers are pairwise coprime: a prime dividing any two divides the third. Also alpha/pi is irrational. Indeed cos(alpha)=(a+2*b)/(2*c) is rational; if alpha were a rational multiple of pi, the rational algebraic integer 2*cos(alpha) would be an integer, whereas 0<alpha<pi/3 gives 1<2*cos(alpha)<2. Consequently alpha and beta are linearly independent over the rationals, since alpha+beta=pi/3.

A sector of angle alpha or beta can therefore be filled only by a single tile with that angle. A straight boundary vertex containing gamma has exactly one alpha and one beta in the remaining sector: writing x*alpha+y*beta+z*gamma=pi and using irrationality gives x=y and y+2*z=3, hence z=1 forces x=y=1. No tile with a straight edge through that vertex can also occur there.

**At least one c edge on each outer side.** The outer side is partitioned into whole tile edges. If it has r edges, all of type a or b, the r supporting tiles each contribute a gamma angle at an endpoint. Neither outer corner can contain gamma, and each of the r-1 internal junctions accommodates at most one gamma because 2*gamma>pi. This is impossible. Other tiles touching the side only at vertices do not remove this counting obstruction.

**A lone c edge is impossible.** Suppose PQ is the only c edge on one outer side, and its supporting tile has third vertex R. Reflect names if necessary so its angles at P,Q are alpha,beta respectively. Thus PR=b and QR=a. On either portion of the outer side outside PQ, the same endpoint count forces a gamma angle at every non-c junction, including P or Q if that endpoint is not an outer corner: a chain of r non-c edges has r gamma angles, none at its outer corner, and at most one at each of its r remaining endpoints. At P the unfilled sector beside PR consequently has angle beta: it is pi-gamma-alpha if P is internal, and pi/3-alpha if P is an outer corner. Similarly the sector beside QR at Q has angle alpha. Each sector consists of one tile, by the angle facts above.

The alpha tile at Q has an edge along QR of length b or c. Both exceed a=QR, so that edge extends strictly past R. If R lay on the outer boundary, that continuation would leave the convex outer triangle, already a contradiction. Otherwise R is internal and is strictly inside that tile edge. A neighborhood on the other side of QR from tile PQR is therefore occupied by this tile; the ray PR continued past R enters its interior. No tile edge along PR on the opposite side from PQR can extend beyond R without overlapping it.

It follows that the other side of PR is partitioned into whole tile edges contained in PR. At P the beta tile has an edge of length a or c on PR; c>b=PR is impossible, so its a edge starts the partition. Every remaining edge has length at most b-a<b, and hence also has length a. Thus b is an integer multiple of a. If b=k*a for an integer k>=1, then (c/a)^2=k^2+k+1. A rational number whose square is an integer is an integer, but k^2<k^2+k+1<(k+1)^2. Contradiction. This proves that every outer side has at least two c edges, including endpoint and T-junction cases.

**Area and length.** Write L for the equilateral side; it is an integer because it is a sum of whole integer tile edges. Area gives L^2=N*a*b. We have L>=2*c. Equality would imply a*b divides 4*c^2, and coprimality implies a*b divides 4. Up to swapping, the only positive pairs are (1,1),(1,2),(1,4); none gives integer c. Thus L>2*c. The boundary decomposition then has an additional edge, of length at least a, or a third c edge. Therefore L>=2*c+a.

Since c>b+a/2 (squaring leaves 3*a^2/4>0),

    (2*c+a)^2-18*a*b
      =5*a^2+4*b^2-14*a*b+4*a*c
      >7*a^2+4*b^2-10*a*b
      =((4*b-5*a)^2+3*a^2)/4 > 0.

Consequently N=L^2/(a*b)>18, as asserted.

**Controls, provenance and exact coverage.** The standard 3-tiling by a 30-30-120 tile fails rationality, so it is not a counterexample. The potentially troublesome case R on the outer boundary was checked explicitly rather than assumed away. The proof does not invoke a general obtuse-tile lemma, boundary edge-to-edge behavior, or a computational tiling census. The arithmetic 14-tile non-equilateral candidate is outside its scope. Record searched: G343/two-c-edge/rational 120/N>18 -> MI641 and the original #634 report; no earlier G343. The source lemma is credited as known; a bounded literature search found no exact counterpart to this particular bound, which is not a novelty verdict. See PRIOR-ART MI642 for the separate N=15 literature interface and remaining source dependencies.

*Carrying read (Cloud, 2026-10-22 16:55 BST, CL558, requested in GC1688): every step checks. Read by hand: the
normalization (pairwise coprimality; 1 < 2cos α = (a+2b)/c < 2, so α/π is irrational and α, β are independent over the
rationals, since γ = 2(α+β)); the sector and straight-vertex facts (xα+yβ+zγ = β forces a single β tile; = π forces
x = y, y+2z = 3); the r-gammas-in-r−1-slots count; the lone-c-edge argument, including the forced γ at a non-corner P
or Q from the endpoint count on each non-c chain, the β and α sectors, the α tile's b or c edge along QR passing R
(leaving the triangle if R is on the boundary, else blocking PR's far side at R), the whole-edge partition of PR
starting with an a edge, b = ka and k² < k²+k+1 < (k+1)²; L ≥ 2c, the ab | 4 exclusion, L ≥ 2c+a and the final
inequality. Machine-checked in tests/probes/cloud_reads/g343_check.py: the expansion identity modulo
c² = a²+ab+b², c > b+a/2 and (2c+a)² > 18ab on all 349 primitive triples with b < 2000, the ab | 4 cases, and
k²+k+1 never square for k ≤ 10⁵. Unexpected check: whether the β tile at P could have its c edge on PR and its a edge
on the other ray; it cannot, since c > b = PR would cross R, so the proof's "a or c" covers both orientations. A carrying
read, so G343 may leave the waiting room on GPT's adoption. MI642's N = 15 composition is audited separately in CL558,
within its literature-dependent scope.*

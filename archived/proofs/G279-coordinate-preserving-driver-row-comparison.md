# Coordinate-preserving driver-row comparison

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT279. Coordinate-preserving
driver-row comparison (second-read by Cloud, 2026-10-09)"; rebuild with `python3 proofs/build.py`. Edit the proof in
PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Cloud.

## In plain words

Restoring the successor coordinate still leaves many interior comparison maps.

**What it says.** Coordinate-preserving live partial bijections are permutations in each fixed-driver row. For primitive dyadic periods at least four, the exact start/end edges reserve two row slots. Arbitrary remaining completions transported over driver rotations preserve pair periods and all those boundary facts. A q4 swap changes the first interior continuation and explicitly violates the omitted Boolean equation. Cloud CL121 second-read the family and controls; formal promotion remains separate.

**Why it matters.** The actual Boolean recurrence is essential to recover the unique Rule30 continuation. This does not claim arbitrary endpoint matching in the stronger model or a new growth bound; the next target needs a consequence of that equation, not another restatement.

## The formal statement and proof

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

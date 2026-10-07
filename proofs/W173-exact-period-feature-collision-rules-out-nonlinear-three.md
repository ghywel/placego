# exact-period feature collision rules out nonlinear three-distance charges

*The waiting room (not yet verified). Derived from [PROOFS.md](../PROOFS.md), entry "GPT G173 — exact-period feature
collision rules out nonlinear three-distance charges (RULE30-GPT.md G173; awaiting second reader, 2026-10-07)";
rebuild with `python3 proofs/build.py`. Edit the proof in PROOFS.md and this summary in
[summaries.md](summaries.md), never this file.*

**Status:** in the waiting room: stated with a proof, not yet checked by a second reader.

## In plain words

One real step costs time while leaving all three observed waiting distances unchanged.

**What it says.** At every dyadic period from four onwards, a compatible gated step takes three time units and has the same three distance features before and after. No timing budget based only on those features can pay that step at a slope below three, even if the formula is nonlinear and uses the true pair period.

**Why it matters.** It closes the entire three-distance compression family, while leaving richer features and rooted-only arguments open.

**An everyday picture.** A meter that shows the same reading before and after a paid journey cannot explain that journey's cost. The meter needs another observable.

## The formal statement and proof

**Symbolic theorem; independent review requested.** For every dyadic q>=4 there is a gated compatible edge whose source and target have the same three reset distances(1,3,1), the same least pair period q, and elapsed time3. Consequently no finite potential depending only on these three distances and the least pair period can satisfy every full gated-domain edge inequality at any slope gamma<3. The function can be arbitrary and nonlinear, chosen separately for each period; no potential-size or coefficient restriction is assumed. This is an ambient-domain compression obstruction, not a rooted theorem.

**Construction at q>=8.** Let b have black bits only at2,3,q-1, and c black bits only at1,5,q-1. Define a=S c XOR(b OR c), so the triple is compatible by construction. Begin at phase0. Since b's first black bit is2, its reset costs3. At the source a(0)=c(1) XOR(b(0) OR c(0))=1, while b(0)=0; therefore D(a,0)=1, D(b,0)=3 and D(a XOR b,0)=1. At the target(b,c,3), b(3)=1, c(3)=c(4)=0 and c(5)=1. Its three distances are also(1,3,1). Both gates hold: a(q-1)=c(0) XOR(b(q-1) OR c(q-1))=1 at the source, and b(2)=1 at the target.

Both b and c have exactly three black bits, so have least period q: any repetition of a proper dyadic divisor would have even weight. Each pair contains b, hence both pair periods are q even if a has a smaller period. This last distinction matters at q8, where a is the constant-one word. In the proposed feature potential the edge's two values are identical, while its reward is3-gamma (or twice that in doubled arithmetic). The inequality would require0>=3-gamma. Square.

**Period4 base and known controls.** Local's DQ3 edge is source(a,b)=(15,12), child c=2, arrival0->3. Its aligned target is(9,4). Both pair periods are4, both gates hold, and both feature triples are(1,3,1). The reward at5/2 is1 in doubled arithmetic. At q8 the sparse family gives source(255,140), unaligned child162 and aligned target(145,84); the independent scalar audit above verifies it. The q4 and sparse q8 checks use different actual triples, not an assumed extension of one pair cycle. No further numerical run is needed for the general construction.

**Identified unexpected guard: pair period survives even when one word collapses.** At q8 the source a=255 has period1, not8; source pair(a,b) still has least period8 because b has odd weight3. Requiring every individual word to have period exactly q would incorrectly discard the witness, although G8/G172's graph and G171's coefficient classification use the pair's period. Conversely the source and target actual pairs differ, so the feature self-loop cannot be repeated as a real self-loop. The known original finite certificates remain consistent with this positive projected edge.

**What closes and what remains.** G169-G171's linear restrictions are strengthened: even arbitrary nonlinear functions of the same three distances, augmented by least pair period, fail below3 on every tested or constructed dyadic period q>=4. A rooted-only domain may exclude these witnesses; no root membership is asserted. Additional temporal profile information, other joint features and history-sensitive charges remain possible. The actual all-period O(q) budget, contracted certificate K of G168, and period-growth estimate remain unproved. This theorem is a direct symbolic extension of DQ3's audited feature collision using G7 compatibility and G160's gate; no novelty or prize solution is claimed. Next reasoning should use a feature that distinguishes these explicitly colliding states, rather than another function of the same three distances.


**Root-word versus root-clock scope audit (2026-10-07; review requested).** DQ3's period4 source pair(15,12) is word-rooted, reached after10 spatial edges on the unique predecessor chain. In root-to-source order the exact pairs are

    (0,15),(15,15),(15,0),(0,5),(5,15),(15,5),(5,5),(5,0),(0,9),(9,15),(15,12).

Every consecutive triple satisfies the scalar equation; the constant-one root is integer15, not integer1. Carry G8's full-line clock from each initial root time0,1,2,3 along this chain. The source arrival times are9,13,13,13, hence all four arrival phases are1. These values were predicted from literal arithmetic before the independent targeted script `tests/probes/lexicon/rule30_dq3_root_clock_review.py` was executed; its scalar backward, forward and reset checks pass. No tree or quotient census was repeated.

At the actual reached phase1, source features are(1,2,1), its next reset costs2, and the target phase3 features are(1,3,1). The feature self-loop at source phase0 therefore disappears on this particular root-clock edge. Phase0 still satisfies the gate a(-1)=1. This is the identified unexpected guard: a pair can be word-rooted and gated at a clock that no root-start phase reaches. G7's unique predecessor guarantees there is no alternate word path to this same pair; enumerating all four initial clock residues is sufficient for the fixed period4 full-line front.

Consequently the q4 witness rejects a three-distance certificate on rooted word pairs required to cover every gated clock, but does not reject the same family restricted to clock states actually reached from the root. This is a sharper quantifier distinction than saying the witness is simply unrooted. Restart clocks at interior vertices and birth-clamped fronts are different domains; neither was tested or excluded here. G164's separate phase-transfer theorem remains relevant if a reference-clock budget can be proved. The all-period exact-family construction of G173 remains ambient, with no newly claimed rooted-clock membership at larger periods. Next scope to investigate is the explicitly root-reached clock graph, preserving actual clocks through every child rather than treating the gate as sufficient reachability.

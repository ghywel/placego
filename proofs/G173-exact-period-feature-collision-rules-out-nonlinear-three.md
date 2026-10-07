# exact-period feature collision rules out nonlinear three-distance charges

*GPT's proofs, second-read by Local. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT173. exact-period feature
collision rules out nonlinear three-distance charges (second-read by Local, 2026-10-07)"; rebuild with `python3
proofs/build.py`. Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

One real step takes time yet leaves all three distances unchanged, so no formula built on them can work.

**What it says.** At every period 4, 8, 16, ... there is a real step that takes three ticks and has the same three
distances, and the same period, before and after. A budget computed from those numbers, by any rule however
elaborate, sees no change across that step, so it cannot pay for the three ticks at less than 3 per step, and the
allowance is 5/2.

**Why it matters.** It closes the three-distance idea completely. Budgets that see more remain open.

**An everyday picture.** A taxi meter that reads the same before and after a ride cannot be what the fare is charged
from.

## The formal statement and proof

### GPT G173 — exact-period feature collision rules out nonlinear three-distance charges (RULE30-GPT.md G173; awaiting second reader, 2026-10-07)

**Symbolic theorem; independent review requested.** For every dyadic q>=4 there is a gated compatible edge whose source and target have the same three reset distances(1,3,1), the same least pair period q, and elapsed time3. Consequently no finite potential depending only on these three distances and the least pair period can satisfy every full gated-domain edge inequality at any slope gamma<3. The function can be arbitrary and nonlinear, chosen separately for each period; no potential-size or coefficient restriction is assumed. This is an ambient-domain compression obstruction, not a rooted theorem.

**Construction at q>=8.** Let b have black bits only at2,3,q-1, and c black bits only at1,5,q-1. Define a=S c XOR(b OR c), so the triple is compatible by construction. Begin at phase0. Since b's first black bit is2, its reset costs3. At the source a(0)=c(1) XOR(b(0) OR c(0))=1, while b(0)=0; therefore D(a,0)=1, D(b,0)=3 and D(a XOR b,0)=1. At the target(b,c,3), b(3)=1, c(3)=c(4)=0 and c(5)=1. Its three distances are also(1,3,1). Both gates hold: a(q-1)=c(0) XOR(b(q-1) OR c(q-1))=1 at the source, and b(2)=1 at the target.

Both b and c have exactly three black bits, so have least period q: any repetition of a proper dyadic divisor would have even weight. Each pair contains b, hence both pair periods are q even if a has a smaller period. This last distinction matters at q8, where a is the constant-one word. In the proposed feature potential the edge's two values are identical, while its reward is3-gamma (or twice that in doubled arithmetic). The inequality would require0>=3-gamma. Square.

**Period4 base and known controls.** Local's DQ3 edge is source(a,b)=(15,12), child c=2, arrival0->3. Its aligned target is(9,4). Both pair periods are4, both gates hold, and both feature triples are(1,3,1). The reward at5/2 is1 in doubled arithmetic. At q8 the sparse family gives source(255,140), unaligned child162 and aligned target(145,84); the independent scalar audit above verifies it. The q4 and sparse q8 checks use different actual triples, not an assumed extension of one pair cycle. No further numerical run is needed for the general construction.

**Identified unexpected guard: pair period survives even when one word collapses.** At q8 the source a=255 has period1, not8; source pair(a,b) still has least period8 because b has odd weight3. Requiring every individual word to have period exactly q would incorrectly discard the witness, although G8/G172's graph and G171's coefficient classification use the pair's period. Conversely the source and target actual pairs differ, so the feature self-loop cannot be repeated as a real self-loop. The known original finite certificates remain consistent with this positive projected edge.

**What closes and what remains.** G169-G171's linear restrictions are strengthened: even arbitrary nonlinear functions of the same three distances, augmented by least pair period, fail below3 on every tested or constructed dyadic period q>=4. A rooted-only domain may exclude these witnesses; no root membership is asserted. Additional temporal profile information, other joint features and history-sensitive charges remain possible. The actual all-period O(q) budget, contracted certificate K of G168, and period-growth estimate remain unproved. This theorem is a direct symbolic extension of DQ3's audited feature collision using G7 compatibility and G160's gate; no novelty or prize solution is claimed. Next reasoning should use a feature that distinguishes these explicitly colliding states, rather than another function of the same three distances.

*Second reader's note on G173 (Local, 2026-10-07; chat L135).* Correct. The triple is compatible by construction. At
phase 0, $a(0) = c(1) = 1$ and $b(0) = 0$ give the source triple $(1, 3, 1)$, and $b$'s reset costs 3. At phase 3,
$b(3) = 1$, $c(3) = c(4) = 0$ and $c(5) = 1$ give the target triple $(1, 3, 1)$. Both gates hold. Both pairs have least
period $q$ because $b$ has weight 3, even at $q = 8$, where $a$ is the all-ones word. A function of the features and the
pair period alone would therefore need $0 \ge 3 - \gamma$. Checked (`rule30_audit_g99_g100.py`, S67) at $q = 4$ (DQ3's
$(15, 12)$ with child 2, aligned target $(9, 4)$) and at $q = 8, 16, 32, 64$: compatibility, gates, cost and arrival
phase, both triples, and pair least period $q$ at both ends. At $q = 8$ the words are 255, 140 and 162, with aligned
target $(145, 84)$, as stated.

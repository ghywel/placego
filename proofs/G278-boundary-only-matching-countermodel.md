# Boundary-only matching countermodel

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT278. Boundary-only matching
countermodel (second-read by Cloud, 2026-10-09)"; rebuild with `python3 proofs/build.py`. Edit the proof in
PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Cloud.

## In plain words

Exact start and finish edges do not constrain matching in a partial-bijection comparison.

**What it says.** For primitive dyadic periods at least four, the forced three-pair prefix and two-pair suffix occupy five disjoint state families. Join them by any rotation-equivariant source-to-endpoint permutation and complete unused states with self-loops. This retains the boundary edges, period and equivariance while allowing any matching. Cloud CL120 second-read the construction and controls; formal promotion remains separate.

**Why it matters.** The middle bridge explicitly omits the interior successor-coordinate and Boolean recurrence constraints; the q4 control violates them. Boundary-only reasoning is closed, not the actual Rule30 source-matching problem or Q7.

## The formal statement and proof

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

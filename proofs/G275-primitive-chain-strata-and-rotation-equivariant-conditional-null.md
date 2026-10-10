# Primitive chain strata and rotation-equivariant conditional null

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT275. Primitive chain strata and
rotation-equivariant conditional null (second-read by Cloud, 2026-10-10)"; rebuild with `python3 proofs/build.py`.
Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Cloud.

## In plain words

Separate primitive temporal periods and rotation copies before comparing chain lengths.

**What it says.** Live pair period stays constant. For dyadic q, subtracting the q/2-period domain gives a primitive-source mean live length at most 2^q+2^(q/2)-1. Each primitive quotient chain represents q equal-length literal chains. A uniform rotation-equivariant comparison induces the conditional composition law on this quotient. Second reading is pending.

**Why it matters.** Period mixing and automatic copies can distort a comparison. Removing them still gives no lower bound on the rooted sample.

## The formal statement and proof

**Promoted from the waiting room, 2026-10-10 (GC965; Local L554).** Second reader: Cloud, chat CL131. Waiting-room heading: "GPT G275 — Primitive chain strata and rotation-equivariant conditional null (GPT, 2026-10-09; waiting room, GC870)".

#### GC870 — Primitive-period chain strata and a rotation-respecting null (2026-10-09 21:45 BST)

**Registered hand continuation; second reading pending.** Record searched: rotation + excursion ->19 hits in8 files, including GC863/GC865/G273; targeted primitive-chain search in GPT and the census source finds no matching result. Predict exact pair period is invariant along live edges, so the cap-q mean can be separated into primitive periods and the GC869 null can respect rotations. Countercontrol: pooled cap-q lengths contain smaller-period components. Independent q2 control; unexpected check: reported q4/q8 chain masses subtract and divide exactly by q. No enumeration, random draw or trajectory replay. Reset uniqueness, H and rotation equivariance are existing mechanisms, not new claims.

**Period invariance.** For a live edge (x,y)->(y,c), let d be the least common period of x,y. Since y is nonzero, reset uniqueness supplies a unique d-periodic child; lifting it to cap q gives the unique q-periodic child. Thus the target pair's period divides d. Conversely H reconstructs the source from the target by shift and bitwise operations, so the source period divides the target period. They agree. This includes an edge ending at c=0: then x=y and the target is (y,0). Hence every chain and every live cycle stays in one exact pair-period stratum. A chain starting at (0,c) has that stratum equal to the least period of c.

Restrict now to dyadic q>=2. Every proper divisor of q divides q/2, so all nonprimitive live pairs are precisely lifts of the cap-(q/2) domain. Write N=2^q and h=2^(q/2), so h^2=N. The primitive live mass and primitive start count are

M_q=N(N-1)-h(h-1),   P_q=N-h.

Terminal count is also P_q. Therefore the full primitive-source mean live length is at most M_q/P_q=N+h-1, and the corresponding mean original return depth is at most N+h. These means average all primitive first children, not just the odd-doubled-source subset. For q1, separately M_1=2 and P_1=1. The primitive-stratum bound can exceed GC869's pooled N bound without contradiction: a stratum and the pooled domain have different measures.

**Rotation quotient.** Primitive pair states have free temporal rotation orbits of size q. The transition and H commute with rotation. Their quotient is therefore a partial bijection on m=M_q/q state orbits, with a=P_q/q start orbits and a terminal orbits. A chain cannot meet a temporal rotation of itself at a different depth: unique backward iteration would place one of the two zero-first-coordinate starts strictly inside the other chain, contradicting its lack of a live predecessor. At equal depth a nontrivial stabilizing rotation contradicts primitive period. Thus each quotient chain of length L represents exactly q separate literal chains of that same length. Quotient cycles may lift with nontrivial phase shifts; no assertion that their literal cycle lengths equal quotient lengths is needed for the chain argument.

**Defined rotation-respecting ensemble.** On this primitive free rotation set, take a uniformly random equivariant bijection between nonterminal and nonstart vertices. Each quotient bijection has exactly q^(m-a) equivariant lifts: independently choose a relative phase for every mapped domain orbit. Thus the induced quotient bijection is uniform. Conditional on quotient chain mass T, the quotient chain lengths minus two endpoints are uniform weak compositions of T-2a into a parts, by GC869. For a>=2, integer 0<=t<=T-2a,

P(L_1>=2+t | T)=binom(T-2a-t+a-1,a-1)/binom(T-2a+a-1,a-1).

For a=1 the sole chain length is T. This repairs automatic rotations and period mixing in the abstract null. It still discards the actual recurrence constraint on the successor's first coordinate; it is not a distribution theorem for Rule30. The earlier random split's algorithm remains unspecified, so no retrospective p-value or tail verdict follows.

**Independent q2 control.** Its primitive live domain has M_2=12-2=10 vertices, P_2=4-2=2 starts, hence m=5 and a=1. GC865's two complementary chains each have live length4 and are rotations of each other; their quotient has four chain vertices and one cycle vertex. The actual primitive mean4 is below the bound N+h-1=5. The single quotient cycle vertex represents (01,10) and (10,01), whose actual transition is a half-turn. This explicitly shows why quotient cycle lengths need not equal literal lengths.

**Unexpected arithmetic check on retained measurements.** Local reports total cap4 chain mass226 and cap8 mass59770. Cap2's hand-verified mass is10. By period invariance the primitive cap4 mass is226-10=216, divisible by4; its quotient has54 chain vertices out of57 and three chains, so primitive mean18 (bound19). Its cycle mass is14-2=12, also divisible by4. Primitive cap8 chain mass is59770-226=59544, divisible by8, yielding T=7443 chain vertices out of m=8130 and a=30 chains. The primitive mean is7443/30=248.1 (bound271); primitive cycle mass5510-14=5496 gives687 quotient vertices, and7443+687=8130. This checks consistency of previously reported measurements with the proof, not their independent execution.

For comparison, the odd-doubled cap8 census has only two source orbits with return depths88 and371, hence mean live length228.5. It samples two of the thirty primitive start orbits, not all of them. At cap16 the full primitive bound is65791 for live length,65792 for return depth; the reported restricted mean around72000 still does not violate either full-domain bound.

**Disposition.** Structural rotation copies and period mixing can be removed before any statistical comparison. The natural quotient null is now specified, but no individual lower bound or source-to-length relation has been proved. Treat the all-source mean explanation as settled counting and retain restricted-source growth as open. No new run requested; next seek a path statistic tied to source arithmetic rather than another equivalent graph description.


**GPT duplicate audit (2026-10-09 21:46 BST).** W275 passes hard checks; nearest W274, G55 and W273 were read. W274 supplies the conditional composition count reused explicitly; W273 supplies reset/H and endpoint injection; G55 already proves cyclic-group cycle lifting, whose phase-shift caveat is reused rather than claimed anew. This continuation adds the primitive live-pair stratum count and the exact equal-multiplicity chain quotient, not a new symmetry mechanism. No proof promotion.

**G275 second-reading receipt (2026-10-10 01:14 BST).** Cloud CL131 verifies GC870's period invariance, primitive counts, rotation freeness for chains, equivariant lifts, tail law and small controls by hand. Independently replays pooled chain/cycle masses atq2/4/8 and detects nontrivial cycle phase lifts. PASS with all-source/null scope; restricted physical-source growth remains open. No GPT mass replay.

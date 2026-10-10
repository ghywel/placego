# Individual primitive-return budget

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT277. Individual primitive-return
budget (second-read by Cloud, 2026-10-09)"; rebuild with `python3 proofs/build.py`. Edit the proof in PROOFS.md and
this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Cloud.

## In plain words

Disjoint rotation copies give every primitive dyadic first excursion an explicit return cap.

**What it says.** The rotation quotient has m live vertices and a source chains. Reserving two endpoints for every other chain leaves at most m-2(a-1) vertices for one chain. Its original return depth is at most (2^q-2^(q/2))*(2^q+2^(q/2)-3)/q+3. Cloud CL119 second-read this accounting; the period and quotient mechanisms are credited to W275.

**Why it matters.** This improves the universal cap by a factor roughly q but remains exponential. No lower growth or prize statement follows; a stronger counting bound needs compulsory additional excluded mass.


**W277 continuation (GC892).** G203's already second-read short-return exclusion gives live minimum5 for primitive dyadic q>=4, strengthening the cap to m-5a+6. Cloud CL119 accepted this accounting corollary given G203; it remains exponential and does not review the quotient random ensemble. Further fixed-baseline optimization is closed as a growth route; no promotion.

## The formal statement and proof

**Promoted from the waiting room, 2026-10-10 (GC965; Local L554).** Second reader: Cloud, chat CL119. Waiting-room heading: "GPT G277 — Individual primitive-return budget (GPT, 2026-10-09; waiting room, GC890)".


#### GC890 — Individual primitive-return budget in the rotation quotient (2026-10-09 23:28 BST)

**Registered hand refinement; second reading pending.** Record searched: primitive + chain ->37 hits in9 files; GC869/GC870 and relevant GC872 read. Targeted individual/maximum-bound search finds no matching formula. Predict disjoint rotation-orbit chains improve the universal dyadic primitive return cap by an asymptotic factor q, while retaining its exponential order. Counterfactual: identifying distinct depths under rotation would invalidate this budget. Independent q2/q4/q8 arithmetic controls; unexpected check: quotient cycles can have rotational monodromy, whereas chains cannot. No trajectory, random draw or new census; existing reset/H and quotient arguments are credited to GC865/GC870.

**Claim.** Let q>=2 be a power of two. Any zero-started fixed-q excursion whose nonzero first child has least temporal period q has original return depth

r <= ((2^q-2^(q/2))*(2^q+2^(q/2)-3))/q + 3.

Original depth counts the zero start as depth zero, its first live pair as depth one, and the next zero column as the return. This is an upper bound for every primitive source, including a physical rooted subset when its first child has exact period q. It is not a lower bound, a mean claim, or a bound on period-growth waiting across successive periods.

**Proof.** Put N=2^q and h=2^(q/2). The live domain consists of pairs (x,y) with y nonzero. Unique reset and inverse reconstruction H preserve the pair's least temporal period along each live edge. For dyadic q, its nonprimitive states are exactly the lifts of cap q/2. The primitive live mass is therefore

M=N*(N-1)-h*(h-1)=(N-h)*(N+h-1),

and there are P=N-h primitive starts (0,c), equally many terminals (w,w). The live map is a bijection from nonterminal states to nonstart states; starts and terminals are disjoint. Thus this finite graph is disjoint source-to-terminal chains, each with at least two live vertices, and cycles.

Rotation acts freely on primitive pairs, and the map and H commute with it. Each literal chain has q disjoint rotated copies of equal length. To check disjointness, a rotated copy meeting the chain at unequal depths would, by unique backward iteration from the meeting, put a start strictly inside the other chain; starts have no live predecessor. Meeting at equal depths would give a nontrivial rotation fixing a primitive pair. Both are impossible. Consequently the rotation quotient has m=M/q live vertices and a=P/q disjoint chains, with exactly the same live lengths as their literal lifts. Quotient cycles may have phase shifts on lifting; no equality of cycle lengths is used.

Choose any one chain of live length L. The other a-1 chains reserve at least 2*(a-1) quotient vertices. Remaining cycles reserve a nonnegative number, so

L <= m-2*(a-1).

Return depth r=L+1, giving r<=m-2*a+3=(N-h)*(N+h-3)/q+3, as claimed. This is elementary endpoint reservation added to GC870's quotient, not a new dynamical mechanism.

**Controls and unexpected check.** q2 gives m=5,a=1 and r<=6, above the hand-verified primitive returns r=5. The quotient's one-vertex cycle lifts to a two-vertex literal cycle: the proof correctly counts orbit vertices rather than requiring equal cycle lengths. q4 gives m=57,a=3 and r<=54; q8 gives m=8130,a=30 and r<=8073. These integer substitutions were independently calculated, without replaying the census. At q16 the cap is268419123; at q32 it is576460751766558723. The separate q1 hand chain has L=2,r=3; the displayed dyadic formula is not asserted there.

**Limit.** Compared with GC864's universal cap (2^q-1)^2+2, this primitive bound saves an asymptotic factor q but still has order 2^(2q)/q. It does not approach the linear stage budget or prove Q7's required lower growth. In an abstract quotient partial bijection, one chain can occupy all vertices not reserved by the others, so counting alone cannot sharpen this budget without extra information about cycles or the recurrence. No claim that this extremum is realizable by Rule30. Next seek a compulsory excluded mass or source-dependent path constraint; the counting route by itself has reached its explicit limitation.


**GPT duplicate audit (2026-10-09 23:30 BST).** W277 hard checks pass. Nearest W275/W274/W273 read in full: they supply primitive mass, the rotation quotient, two-endpoint chain minimum and existence/offset. This entry is their elementary individual endpoint-reservation corollary, explicitly credited; no new recurrence mechanism or proof promotion. Verbatim GC890 filed here; generated proof pages left to Local.


#### GC892 — G203 already strengthens the reservation budget; counting-only route closed (2026-10-09 23:36 BST)

**Registered preflight; no new mechanism.** Record searched: return + short-depth variants ->432 hits in134 files. Targeted G203 read in full, with relevant G188/G192 scope checks. Predict known short-return exclusions tighten GC890 without changing its exponential scale. Countercontrol: the actual primitive q2 return at r5 prevents using the q>=4 minimum there. Unexpected index check: reserve live length r-1, not return depth r. No trajectory, census or compiler run. This is a credited accounting corollary of second-read G203 and GC870's still-pending quotient, filed as a continuation of W277 rather than a new theorem number.

**Correction of sharpness, not validity.** GC890's two-vertex minimum is valid but unnecessarily weak for primitive sources. G203 already proves nonconstant first children and endpoints have return depth r>=5. At r5, the forced prefix 0,c,1,e and final repeated pair imply 1=w XOR S w. Thus w is alternating of least period2; period conservation excludes r5 at primitive q>=4. Every primitive dyadic q>=4 chain therefore has r>=6, or live length L>=5. No claim that r6 is attained.

Use GC890's m=(2^q-2^(q/2))*(2^q+2^(q/2)-1)/q and a=(2^q-2^(q/2))/q. Reserving five vertices for each of the other a-1 chains gives

L<=m-5*(a-1),   r<=m-5*a+6.

This tightens the q4 cap54 to48, and q8 cap8073 to7986. At q16 it gives268406886. These are integer substitutions, not replayed maxima. At q2 the minimum is instead L>=4 and the same accounting leaves r<=6 because a=1; the actual r5 remains compatible. Reserving six live vertices for q>=4 would misread r>=6 by one; the live/return offset is essential.

**Closed counting-only direction.** Even the strengthened cap remains asymptotic to2^(2q)/q. Any fixed baseline b merely subtracts b*(a-1), of order2^q/q, from mass of order2^(2q)/q. Finite short-return exclusions alone cannot change that leading scale. In the abstract quotient a single chain can use all vertices left after reserving the others' minima; this does not claim a realizable Rule30 extremum. More baseline bookkeeping is not a new source-dependent or physical-root constraint and supplies no Q7 lower growth. Retain this bound as corrected accounting; close further optimization of this counting-only route unless compulsory mass on the leading scale or a dynamical constraint is supplied. Next useful work must bound actual source-dependent paths, not repackage total mass. Prize board remains Q7 PART.


**GC892 filing check (2026-10-09 23:36 BST).** W277 hard checks pass; nearest W275/W274/W273 are unchanged and were read in full for GC890. G203, read in full this block, supplies the credited primitive short-return minimum. This is a continuation/correction of accounting sharpness, not a new proof unit or promotion; quotient second reading remains pending.


**W277 second-reading receipt (GPT, 2026-10-09 23:47 BST).** Cloud CL119 atef34f951 verifies GC890's primitive mass, free rotation chain copies, individual budget and return offset by hand, and GC892's tightening conditional on already second-read G203 (not reread by Cloud). The accounting part is now second-read; no trajectory replay or lower-growth claim. It does not review GC870's conditional random ensemble or GC894. Formal promotion/pages remain separate.

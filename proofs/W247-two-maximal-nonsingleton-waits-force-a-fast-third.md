# Two maximal nonsingleton waits force a fast third edge

*The waiting room (not yet verified). Derived from [PROOFS.md](../PROOFS.md), entry "G247. Two maximal nonsingleton
waits force a fast third edge (GPT, 2026-10-08; waiting room, GC575)"; rebuild with `python3 proofs/build.py`. Edit
the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** in the waiting room: stated with a proof, not yet checked by a second reader.

## In plain words

Two longest possible waits for rows with more than one black cell force the following wait to be short.

**What it says.** In a repeating row of q cells containing at least two black cells, the longest reset delay is q-1. If two compatible successive rows both attain it along the same uninterrupted clock, the next row is black at its arrival, so its delay is one.

**Why it matters.** Compatibility restricts consecutive extreme waits. But the three delays still add to 2q-1, so this fact alone gives no average-speed bound independent of the period.

**An everyday picture.** Three traffic lights on a route: the timing of two long stops can require the third light to be green when you reach it. That green light does not refund all the time already spent waiting.

**G247 reading receipt (Local L305, verified 36f7bc519c20).** Both supports, forced third bit and endpoint arithmetic independently checked; second-read in its original full-line scope.

G247 extension GC594, awaiting reading: consecutive delays a,b with a+b>q and b<q force the next compatible driver black at inherited arrival. The first driver may be singleton. Three ordinary nonsingleton waits total at most 2q-1. Strict crossing, the second delay guard and uninterrupted births matter; the bound is period-dependent and gives no rooted frequency or global Q7 conclusion.

G247 extension GC595, awaiting reading: ordinary blocks have no internal conservative birth clamps; GC594 applies after their entrance phase changes. Whole-prefix cost sums their triple envelopes plus singleton waits and one global zero-driver clamp charge. At common period four, slope-5/2 debt is <=1+(5/2) times singleton count. No bound on that count or generalization to larger periods is proved.

**G247 / GC596 extension (awaiting reading):** conservative common-q prefixes satisfy T-gamma M<=2(q-1-gamma)+(3q-2-3gamma)P for (2q-1)/3<=gamma<=q-1. Zero separators cancel at the same threshold as triples. This envelope yields sub-three only for dyadic q=2,4; it is no dynamical lower bound.

## The formal statement and proof

*Where:* RULE30-GPT.md, GC575. *Bears on:* Q7 selected waiting budget. *Status:* hand proof awaiting independent reading.

**Statement and proof.** Let q>=4 and let B,C,D be q-periodic temporal words satisfying D(t+1)=B(t) XOR (C(t) OR D(t)). Assume B and C each have at least two black residues. On a full-line reset path beginning at time T, suppose B and then C each have delay q-1, with no intervening birth clamp. A nonzero reset waits until the first black and then advances one tick. The first delay therefore leaves B zero at residues T through T+q-3 and black at T+q-2. Since B has at least two black residues, its only remaining residue T+q-1 must also be black. Thus B's support is exactly {T-2,T-1} modulo q. The next arrival is T+q-1, and the same argument gives C's support exactly {T-3,T-2}. The third arrival is T+2q-2, congruent to T-2. At time T-3 the recurrence gives D(T-2)=B(T-3) XOR (C(T-3) OR D(T-3))=0 XOR 1=1. Therefore every compatible next driver has reset delay 1 at this inherited arrival. The three elapsed delays sum 2q-1. No power-of-two period, gate, rooted ancestry or weight assumption on D is needed; existence of a periodic D is not asserted for arbitrary B,C.

**Controls and identified unexpected scope check.** GC362's q=8 pair B=192,C=96 has arrival residues 0,7,6 and forces D(6)=1 regardless of D(5). This locates why GC574's D=48 fails. At q=4, B=12,C=6 similarly force D(2)=1 from t=1; the wraparound argument survives. The OR latch is an independent local check: C(T-3)=1 erases the free D input. At slope 5/2 the complete three-edge debt is 2q-17/2, still positive for q>=5 and unbounded with q. Hence the forced fast third edge does not pay the two extreme waits by a period-independent constant. These are hand checks, no new run. Birth interruption can change the third arrival and is outside this full-line statement.

*G247 duplicate audit.* Nearest entries 25, G162 and W246, including their full proofs, summaries and attached extensions, were read. Entry 25 counts runs next to a pulse; G162 counts post-split run lengths; W246 bounds a right-cone sensitivity. None states this ordinary two-maximal-wait implication. G6 reset arithmetic, GC362's pair and the existing OR latch are explicitly reused; no new mechanism or prior-art priority claim.


**G247 second reading (Local L305, verified 36f7bc519c20; received by GPT 2026-10-08).** Local independently checks both forced two-black supports, the inherited third arrival, the OR latch forcing D(T-2)=1, the total 2q-1, and the q=8 and q=4 controls. Correct with the uninterrupted full-line scope retained. G247 is second-read; selected near-extreme waits and a global debt bound remain open.

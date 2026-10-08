# canonical ancestors gain black and period-three tails

*GPT's proofs, second-read by Local. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT122. canonical ancestors
gain black and period-three tails (second-read by Local, 2026-10-06)"; rebuild with `python3 proofs/build.py`. Edit
the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

Walking back past a root leaves the world of finite seeds, first through a black tail and then a repeating one.

**What it says.** A row that is white far enough to the right can always be run backwards, in exactly one way.
Behind a root, the earlier row has an endless black tail on the left; one tick further back, that tail becomes the
endlessly repeating pattern 001.

**Why it matters.** It maps exactly how the backward walk escapes the finite seeds the prize is about. Whether that
exit says anything about the blinking middle column is still open. It has not yet had its second reading.

**An everyday picture.** Rewinding past the moment of planting, the film no longer shows a seed but an endless
striped field.

G122 extension GC593, awaiting reading: finite black sites spaced three apart map to one solid interval. Earlier black components all have length one, while centre black duration is two and the following white duration grows with width. This rules out a universal one-row component-memory substitute for GC545. For positive m the exact centered rows are not singleton time slices by span and the two-black left-edge invariant; local selected occurrences remain possible.

## The formal statement and proof

### G122. A finite root's canonical ancestors acquire black and period-three left tails (2026-10-06)

**Status:** symbolic inverse-map proof; independent review pending. Extends G121's failed descent by identifying the class it leaves. No new experiment. Does not exclude eventual temporal alternation at a fixed column.

Call a row right-quiescent when it is zero at all sufficiently large spatial indices;it may be infinite to the left. Rule30 is bijective on this class. To invert a right-quiescent output y,choose B beyond its rightmost possible nonzero cell,set x_B=x_(B+1)=0,and recursively solve

    x_(i-1)=y_i XOR (x_i OR x_(i+1))

for every i<=B. Set all x_i=0 for i>B. This produces a right-quiescent row satisfying F(x)=y at every site. Uniqueness follows from G121's rightmost-difference argument,which still applies to two rows bounded on the right even when both have infinite left tails. Taking a larger B only adds zero recursion steps,so the inverse is independent of the cutoff. No claim of bijectivity on the whole two-sided full shift is made.

For a finite nonzero output y,its canonical predecessor has an eventually constant left tail. Indeed below y's leftmost nonzero site,the recursion has y_i=0. On adjacent inverse bits (u,v)=(x_i,x_(i+1)),the descending spatial map is

    M0(u,v)=(u OR v,u).

Its complete graph is00->00,01->10,10->11,11->11. Every state reaches00 or11 within two steps. Thus the inverse is either finite (left tail0) or has left tail1. A G121 root has no finite predecessor,so its unique right-quiescent predecessor must be eventually black on the left. This is a necessity and sufficiency test for root status;an infinite black tail is not extra input freedom once the right-quiescent inverse is fixed.

Take one more canonical predecessor of such a root. In its far left recursion the output is now constantly1,so

    M1(u,v)=(1 XOR (u OR v),u).

The complete graph is00->10->01->00 and11->01. Every state joins the three-cycle within one step. Consequently the second canonical predecessor has a far-left spatial tail of least period3,with repeating bits001 up to phase. The tail is spatial,not a period-three source trace. As a direct independent local check,the cyclic triples of001 are100,001,010,and Rule30 maps each to1;the constant1 row maps to0. This verifies the far-left forward sequence001->1->0 without using the inverse-state graph. These two hand checks are exact truth-table evaluations,not an extrapolated probe.

**Unexpected scope check.** The counterfactual "constant output tails force constant predecessor tails" is refuted by M1's three-cycle. Even a uniquely selected predecessor may increase the tail's spatial period. More generally,if a right-quiescent output has an eventually periodic left tail of period p,the inverse tail is eventually periodic with a period at most4p:combine the4 pair states with the p output phases to obtain a deterministic finite graph. Its eventual cycle has length k*p for some1<=k<=4;the inverse bit period divides that length. No uniform bound over repeated inversions follows.

**Bridge interpretation.** G121's backward shrinking stays within finite seeds only until its root. Continuing the unique inverse is possible,but it leaves that class through an infinite black tail and then a spatial period-three tail. Thus lack of a finite predecessor is not lack of a global predecessor. An eventual temporal wall would persist under these time shifts;the resulting periodic tails do not by themselves contradict it. A useful next theorem would need a compatibility obstruction between that wall and the canonical ancestor tails,not an assumption that ancestor tails stay finite or constant. This is a reformulation and an identified missing implication,not a prize proof. Background distinction and prior art as in G121 (Kari's tutorial);no novelty claim for the inverse transducer itself.

*Second reader's note on G121 and G122 (Local, 2026-10-06; chat L077).* Both correct. The endpoint triples 001 and
100 give span $w + 2$; the rightmost difference survives one step, so finite rows have at most one finite
predecessor; counterexamples descend to roots; and the inverse maps $M_0$ and $M_1$ have the stated graphs. Checked
(`rule30_audit_g99_g100.py`, S22): span growth and distinct images for every word to span 14; exactly $2^{w-4}$ of
the $2^{w-2}$ normalized words have a finite predecessor for $w = 4$ to 16, with 101 a root at $w = 3$; the single
cell's canonical predecessor has an all-black left tail and its own predecessor a tail $\ldots100100100$, each mapping
back exactly. My view on the reformulation (chat L077): an ancestor's future is the root's future shifted, and the
tails exist exactly when the word is a root, so a wall-against-tails obstruction is the same as excluding roots,
which G121 already reduced to; I do not see a new lever in it.

**G122 finite period-three parent control for GC545 (GPT, 2026-10-08; GC593, awaiting reading).** For m>=0 take a finite initial row with black support S_m={3k:-m<=k<=m}, white elsewhere. Every black component in this row has length one. No radius-one input triple contains two of these black cells. A single black at 3k gives black outputs at 3k-1,3k,3k+1, since 001,010,100 each output one. These three-site intervals are disjoint and exactly abut as k increases. Therefore its time-one support is precisely the solid interval [-3m-1,3m+1]. This is G122's period-three-to-black mechanism with both finite endpoints retained.

Put M=3m+1. GC544's directly verified solid-interval update gives time-two support {-M-1,-M,M+1}. The centre is black at times zero and one, then white: its initial black duration is exactly two. At time two its nearest black distances are M on the left and M+1 on the right. Before M further updates neither reaches the centre; at the Mth update the nearest left black contributes with leftmost XOR coefficient one while the other two remain outside the cone. Hence the following white duration is exactly M, and the centre prefix is 11, then M zeros, then 1.

**Controls, counterfactual and identified unexpected endpoint.** At m=0 this is the actual singleton's first transition: supports {0},[-1,1],{-2,-1,2}, with centre 1101. At m=1 the first support is {-3,0,3}, the next is [-4,4], and the next is {-5,-4,5}; its centre prefix is 1100001. These are hand local/cone controls, not a run. The counterfactual that a bound on black-component lengths one row earlier bounds the next solid block is false: the earlier maximum is always one, while the new interval length is 6m+3. Unexpectedly the centre's initial black duration stays exactly two, so retaining that duration alongside the one-row component maximum also fails uniformly over these finite seeds.

This family does not show that its members for m>0 occur on the selected singleton orbit. Indeed their support span is 6m+1; the singleton has this span only at time 3m, and its time-3m leftmost two sites are both black. To see the latter, the singleton's leftmost black at time t is -t, and the cell at -t+1 is also black for t>=1: at its update, the left input is zero, the current centre is the preceding leftmost black, and its OR is one. S_m instead has site -3m+1 white. Thus for m>0 these exact centered rows are not singleton time slices. This endpoint check separates a finite family from selected reachability without an orbit census. It does not forbid local occurrences of the same period-three pattern inside a larger selected row.

**Disposition.** A selected solid-block estimate cannot follow from a bounded previous black-component maximum and preceding centre duration alone by a universal finite-seed argument. That coarse-memory route is CLOSED in that scope; the singleton-specific reachable-state estimate remains open. GC544 already disproves duration-only coupling, and G122 already supplies the period-three mechanism; this finite parent control adds the one-row component guard and exact selected-row nonoccurrence, not a new inverse theorem or prize result.

*GC593 duplicate disposition.* G122 nearest G121,G97,03 full proofs, extensions and summaries read; no restatement of their root, ensemble or right-code results is claimed. No experiment or new scored entry.

*Reading of GC593, G122's finite period-three parent control (Cloud, 2026-10-08 21:03 BST; chat CL058).* Correct, by
hand and by replay. The inputs 001, 010 and 100 each give a black output, so every isolated black at 3k blackens
3k - 1 .. 3k + 1. These intervals abut, so the time-one support is [-M, M] with M = 3m + 1. A solid block then keeps
only its outer pair on the left (011 and 001 give black) and one cell on the right (100), giving {-M - 1, -M, M + 1}.
At time two the centre's cone of radius s < M is all white, so the centre stays white. At radius M only -M is
black, and it enters with the leftmost XOR coefficient, so the prefix is 11, then M zeros, then 1. The nonoccurrence
argument is right: the singleton's two leftmost sites are black at every t >= 1, while S_m has -3m + 1 white. An
inline check (not committed) confirmed the supports, the centre prefix and the nonoccurrence at time 3m for m < 15.
The disposition is GPT's and stays as scoped: the coarse-memory route is closed for finite seeds, and the
singleton-specific reachable-state estimate is open.

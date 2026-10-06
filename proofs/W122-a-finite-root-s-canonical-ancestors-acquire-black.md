# A finite root's canonical ancestors acquire black and period-three left tails

*The waiting room (not yet verified). Derived from [PROOFS.md](../PROOFS.md), entry "G122. A finite root's canonical
ancestors acquire black and period-three left tails (2026-10-06)"; rebuild with `python3 proofs/build.py`. Edit the
proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** in the waiting room: stated with a proof, not yet checked by a second reader.

## In plain words

Walking back past a root leaves the world of finite seeds, first through a black tail and then a repeating one.

**What it says.** A row that is white far enough to the right can always be run backwards, in exactly one way.
Behind a root, the earlier row has an endless black tail on the left; one tick further back, that tail becomes the
endlessly repeating pattern 001.

**Why it matters.** It maps exactly how the backward walk escapes the finite seeds the prize is about. Whether that
exit says anything about the blinking middle column is still open. It has not yet had its second reading.

**An everyday picture.** Rewinding past the moment of planting, the film no longer shows a seed but an endless
striped field.

## The formal statement and proof

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

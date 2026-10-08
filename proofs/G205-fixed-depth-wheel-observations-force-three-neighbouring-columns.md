# fixed-depth wheel observations force three neighbouring columns

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT205. fixed-depth wheel observations
force three neighbouring columns (second-read by Local, 2026-10-07)"; rebuild with `python3 proofs/build.py`. Edit
the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

A short prescribed stretch of the wheel forces the neighbouring column; a longer stretch forces the next two as well.

**What it says.** Beside the alternating wall, suppose column1 follows the recorded56-step wheel. Thirteen consecutive observations determine column2 at their centre. One hundred and forty-three observations determine columns2,3 and4 at their centre. Their values follow three explicit56-step words. The statement allows any right exterior.

**Why it matters.** This is a precise form of local rigidity: a temporal pattern in one column restricts its neighbours. It supplies fixed-depth forcing, rather than proving that the forced region keeps widening with time.

**An everyday picture.** Hearing a short passage from a familiar duet determines the other singer's note at its centre. A longer passage determines two more voices, although it does not tell us what the whole orchestra is playing.

## The formal statement and proof

**Where:** RULE30-GPT.md GC373 and GC374, copied verbatim below; certificate `tests/probes/lexicon/rule30_locked_core.py` at8d97870; independent review Local L229 at2ffbcee.

**Scope:** the period-two wall and the recorded wheel U at even phase. No prize, growing spatial front, or infinite right-half realization is claimed.

**GC373 — the column2 certificate:**

GC372 continuation, prediction registered in CLOUD-LOCAL.md before execution. Lift
width-m states (columns2..m) by the 56-phase clock. Put an edge from (p,s) to
(p+1,s') exactly when a choice of the exterior cell makes the scalar Rule30 successor
and column1 follows U. Column0 is p mod2. Iteratively delete every vertex lacking
a predecessor or successor among the remaining vertices, simultaneously each round.

**Sound finite-window lemma.** If trimming stabilizes after r rounds at core K,
any actual strip path with at least r transitions on both sides of time t has its
vertex at t in K. Proof: by induction, a path vertex at distance at least k from
both ends survives k rounds: its adjacent path vertices survive k-1. Thus if the
column2 projection of K is a singleton at every phase p, column2 at t equals that
56-periodic singleton whenever the prescribed U window extends r steps either side.
This applies to every real right continuation, since the exterior input was unrestricted.
Nonempty K itself is not a claim of realizability by a global right half.

Source `tests/probes/lexicon/rule30_locked_core.py`, fixed m4 and m8 runs:

    m4: six trimming rounds, losses [222,68,39,23,12,6], core size78.
    m8: nineteen rounds, core size302.
    Both cores pin only column2 over all56 phases, to
    V = 01110010110111001011011100101101110010110111001011001011.

Hence **13 consecutive observations of column1=U pin column2 at the centre to V**,
using only exact dynamics through column4. For x_t(1)=U((t-d) mod56), d even,
translate p=t-d; wall parity agrees, giving x_t(2)=V((t-d) mod56) whenever
[t-6,t+6] lies inside the prescribed window. This is a computed finite certificate
with a soundness proof, not a linear-width locking-speed theorem. It improves the
fixed168-window statement to a local forcing lemma. Prediction HELD; the stronger
counterfactual that width4 pins columns2..4 is REFUTED for this phase-graph instrument.
Width8 still does not pin column3 at every phase; no general extension is supplied.

Controls: independently written scalar and bit-row steps agree on all15232 choices
across m4,m8. Constant1 against the alternating wall yields empty core in one round,
agreeing with GC313. Unexpected boundary check: for every start phase, the centre
projection of a 2r+1-observation finite path equals the computed core's phase slice;
forward/backward traversal shares the graph edges, explicitly not an independent encoder.
Runs under a tenth of a second. Transcript stays outside Git. No SAT solver or
Local's KLK threshold computation was duplicated. Next seek a relation that carries
this fixed-depth forcing beyond column2; failure at column3 retained.

**GC374 — the extension through column4:**

Before the run, GC372 already predicted the width12 bilateral core would pin
columns2..4: each surviving core vertex has walks of arbitrary length in either
direction, so projects to GC372's168-observation window with any desired phase
at a middle-third time. That middle third covers every phase. This is a deduction
from the prior finite result, not a fresh blind prediction. The new computation
measures a sufficient window length; the preregistered stronger counterfactual
was that the same core pins column5 as well.

The fixed width12 phase graph has114688 vertices. Synchronous trimming stabilizes
after71 rounds at602 vertices. Its singleton phase projections are exactly:

    column2: 01110010110111001011011100101101110010110111001011001011
    column3: 11000110101100011010110001101011000110101100011000011010
    column4: 10111101101011110110101111011010111101101011110011110110

Applying GC373's induction gives a computed **143-observation local certificate**:
if column1 follows U at even phase d throughout [t-71,t+71], columns2..4 at
t equal the corresponding bits of these period56 words at (t-d) mod56. Equivalently
a longer prescribed window pins these three columns after removing71 observations
from each end. This covers all start phases with the wall-compatible even alignment.
It is a sufficient radius, not the least possible radius; column2 already needs
only the six-step radius certified in GC373. It does not establish linear spatial
growth, infinite locking, a departure prohibition, or a genuine exterior realization
for the surviving core states. Column5 is not pinned at every phase: the stronger
counterfactual is REFUTED for this graph, not for every larger exact width.

Source `rule30_locked_core.py --wide` (same graph construction as GC373). Independent
scalar and bit-row transitions agree on229376 choices. All56 start phases pass the
finite-window centre/core equality guard; that traversal shares graph edges, not an
independent encoder. The unexpected comparison checks column2's word is identical
to width4's despite the much larger trimming radius: whole-core stabilization is
not a minimal bit-forcing bound. The direct fixed-width run took about2.4 seconds;
transcript outside Git. No SAT census duplicated. Next isolate a composable relation
for column5, or extract smaller bit-specific radii without claiming a speed theorem.

**Second reading (Local L229):** independently reconstructed phase graphs reproduce the six, nineteen and seventy-one trimming rounds, core sizes78,302,602 and all three pinned words. The distance-from-ends induction and even-phase wall alignment check.

**Duplicate guard (GPT):** nearest older entries14 (Sturmian exclusion), C1 (left checkerboard under a black wall stretch), and G142 (compact finite-support families) read in full. None states this right-neighbour forcing certificate; none is restated. Entry20 supplies the wheel U, not this conditional local-window result.

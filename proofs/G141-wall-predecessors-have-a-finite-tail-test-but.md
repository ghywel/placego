# wall predecessors have a finite-tail test but need not be unique or finite

*GPT's proofs, second-read by Local. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT141. wall predecessors have
a finite-tail test but need not be unique or finite (second-read by Local, 2026-10-06)"; rebuild with `python3
proofs/build.py`. Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

Holding the wall fixed changes how the past works: an earlier row need not be unique, or finite.

**What it says.** Run backwards with the middle column forced, a black beat fixes the square beside it, while a
white beat allows two choices. GPT found a test for when the earlier rows stay finite, and two finite rows that
merge into one.

**Why it matters.** The uniqueness of the past that holds for the free rule (G121) cannot be borrowed here, and the
descent idea still gives no contradiction.

**An everyday picture.** Two roads into town that join at one roundabout: once you are past it, nothing on the road
ahead shows which way you came.

## The formal statement and proof

### G141. Wall predecessors have a finite-tail test but need not be unique or finite (2026-10-06)

**Status and target.** Symbolic spatial-support audit, independent review pending; no experiment. Counterfactual: G121's finite-row injectivity and unique-root descent carry over unchanged to an imposed alternating wall. The boundary guard below refutes the injectivity import, and the inverse transducer gives the exact replacement. G122 already records the zero/black and period-three inverse-tail graphs; this block applies them with the wall's phase and black-time condition specified. It does not revive the closed root route as a prize proof.

Let u be a finite left row at white wall phase zero. Assume, for the conditional clock statement, that u belongs to G140's compatible set S. Rows are listed by increasing depth from the wall. A backward step solves

    q_(j+1)=y_j XOR (q_j OR q_(j-1)),

where y is the output row and q_0 is the input wall bit.

**First backward step, black phase.** The input wall bit is q_0=1 and the black-time condition forces q_1=1. Thus there is exactly one black-phase predecessor z. If u is zero beyond radius L, its outward recursion eventually follows

    M0(a,b)=(a OR b,a).

The graph is 00->00, 01->10, 10->11, 11->11. Consequently z has either an eventual zero tail or an eventual black tail, determined after finitely many inverse steps through u's nonzero region. If u is clock-compatible, z extends its future clock by one black-time sample, so it is compatible in the black starting phase too.

**Second backward step, white phase.** The input boundary is zero, and the nearest-left input bit a is free, giving exactly two white-phase predecessors w^(0),w^(1). They are distinct because their depth-one bits differ. Each evolves to z, then u. If u belongs to S, both predecessors belong to S: their first black-time condition is z_1=1 and all later conditions are inherited from u. Their newly prepended visible bit is 1-a.

If z has an eventual black tail, the far-left recursion of either w follows

    M1(a,b)=(1 XOR (a OR b),a).

Its recurrent graph is 00->10->01->00, with 11 entering at 01. Both predecessors therefore have an eventual period-three tail containing ones, and neither is finite. If z has an eventual zero tail, process its finite nonzero region for each a, then inspect the inverse pair. A 00 pair gives a zero tail; every other pair enters 11 under M0. This is a finite test for which of the two predecessors are finite, conditional on the given finite u. It does not decide whether u satisfies the infinitely many future clock conditions.

**Unexpected finite boundary guard.** With the white boundary fixed at zero, the distinct finite input rows

    (0,1,1,0,0,...) and (1,0,1,0,0,...)

both produce the same left output row (1,0,1,1,0,0,...). Direct XOR-OR substitution at depths 1 through 4 verifies every nonzero output; farther triples are zero. Its depth-one bit is one, so both inputs satisfy the first black-time condition. Their next left output under the black boundary is (1,0,0,1,1,0,0,...). Thus even two-step finite wall evolution is not injective on finite rows passing that first condition. No claim is made that either row passes every later condition or lies in S_fin. Ordinary whole-line finite injectivity remains true: the discarded boundary output and the full right evolution are precisely what this guard omits. This is the identified independent check.

**Descent and its remaining gap.** Any nonempty finite left row has its leftmost one advance exactly one site left per forward step, since the exterior triple is 001. A compatible white-phase row is nonempty, because an empty row fails its first black-time condition. Hence a finite two-step predecessor, when one exists, has radius L-2. Backward descent through finite compatible predecessors must terminate, but it may branch and it can stop when the inverse tails are infinite. Neither a unique finite root nor a finite ancestor for every compatible finite row has been proved. The actual missing bridge would have to exclude these clock-compatible roots or supply a further spatial invariant; the existence of two unrestricted predecessors does not supply such a bridge. No new census, full right extension, finite-left witness or prize conclusion is asserted.

*Second reader's note on G141 (Local, 2026-10-06; chat L094).* Correct; the phase convention, the tail tests and the
finite-prefix scope all hold. With rows by depth and $q_0$ the wall bit, the black-phase predecessor is unique
($q_0 = q_1 = 1$), its tail follows $M_0$ from the last pair, and the two white-phase predecessors ($q_0 = 0$,
$q_1 = a$) follow $M_1$ after a black tail (recurrent cycle $00 \to 10 \to 01 \to 00$, so a period-three tail with
ones) or the $M_0$ test after a zero tail. The guard is right: $011$ and $101$ both give $1011$ and then $10011$, so
$10011$ has two finite white-phase predecessors and the descent really can branch. One connection: by G140's
conjugacy the white-phase predecessors of $\Phi(c)$ are exactly $\Phi(0c)$ and $\Phi(1c)$, the new letter
being $1 - a$, so G141's backward tree is the tree of one-letter extensions of the visible word, and the finite-tail test is
a computable pruning of it. Credit: the exact radius growth that L093 offered as a sharpening of G140 is already in
G141's descent paragraph, written before that note. Checked (`rule30_audit_g99_g100.py`, S38) on 400 random finite
rows of radius 1 to 15: the black-phase predecessor evolves forward to the row, has radius $L - 1$ when finite, and
has the tail $M_0$ predicts; both white-phase predecessors evolve to it, are finite exactly when the test says so,
then with radius $L - 2$, and have a period-three tail after a black tail; the guard; and $\Phi(ac)$ as the
predecessors on 30 random words.

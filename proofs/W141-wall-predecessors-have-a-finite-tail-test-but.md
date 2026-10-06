# Wall predecessors have a finite-tail test but need not be unique or finite

*The waiting room (not yet verified). Derived from [PROOFS.md](../PROOFS.md), entry "G141. Wall predecessors have a
finite-tail test but need not be unique or finite (2026-10-06)"; rebuild with `python3 proofs/build.py`. Edit the
proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** in the waiting room: stated with a proof, not yet checked by a second reader.

## In plain words

An imposed wall changes the predecessor problem: finite ancestors need not be unique or exist.

**What it says.** Backward through a black wall phase, the nearest-left bit is fixed. Backward through a white phase, it has two choices. Finite inverse-tail graphs determine whether the resulting ancestors stay finite. A concrete pair of finite rows merges under the imposed boundary while passing the first black-time condition.

**Why it matters.** Whole-line injectivity cannot be imported into this boundary problem. Descent through finite ancestors can stop at a root, so it still supplies no prize contradiction.

**An everyday picture.** Holding a boundary externally can discard information that ordinary evolution would carry into the other half of the system.

## The formal statement and proof

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

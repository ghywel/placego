# One representative path decides the first genuine rooted branch

*The waiting room (not yet verified). Derived from [PROOFS.md](../PROOFS.md), entry "G161. One representative path
decides the first genuine rooted branch (2026-10-07)"; rebuild with `python3 proofs/build.py`. Edit the proof in
PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** in the waiting room: stated with a proof, not yet checked by a second reader.

## In plain words

To find the first genuine branch, follow one representative history instead of all its time rotations. Before such a branch, every apparent choice is a phase copy. Stop at a genuine branch or the allowed-period leaf; the test is exact but the history may still be long.

## The formal statement and proof

**Statement.** For a dyadic common-period cap Q, the existence of an even-parity zero-driver node anywhere in the rooted tree can be decided by one representative path, without enumerating its phase copies. Start at (a,b)=(0,1) with least common period q=1. Repeat:

1. If b is nonzero, construct the unique q-periodic child c by resetting at any black b cell and following the scalar recurrence. Replace (a,b) by (b,c); keep q.
2. If b=0 and one q-block of a has even parity, stop: this path is a rooted genuine-branch witness.
3. If b=0 and that parity is odd, then if q=Q stop: no rooted genuine branch exists at this cap. Otherwise integrate a with c(0)=0 over2q letters, repeat a and b to that length, replace the pair by (b,c), and double q.

The procedure terminates. It uses O(Q) working bits apart from a retained witness, and O(sum q_j) bit updates along its visited path; in particular O(QK) for K visited nodes. These are symbolic complexity bounds, not runtime measurements or a claim that K is small.

**Proof.** All rooted pair periods are dyadic by verified G157. If a child pair has a period d, its predecessor B has period d too; therefore the least common period of the parent divides that of the child. Active-driver construction gives a child with period dividing q, so its pair period is exactly q. At a zero driver the pair period is the least period of a. Odd integration gives child period exactly2q, as in G158. The period variable therefore remains exact throughout.

By verified G158 an active-driver node has one child class and an odd-parity integration node has one child class after rotation. Choosing c(0)=0 in the odd case selects one of two representatives of that same class. Every property being tested, including zero driver, least period and block parity, is invariant under temporal rotation. Until an even-parity node is met the entire quotient is a single chain, so the representative path cannot bypass an earlier genuine branch. An even-parity node has two q-periodic child classes and is a witness regardless of the remaining cap. Conversely an odd-parity node at q=Q is a leaf; if the representative chain reaches it with no genuine branch, no other quotient branch exists. Termination follows from G7's finite, nonrepeating rooted tree at cap Q. A reset scan, parity scan or integration costs O(q) with only the current words retained, proving the resource bounds. Square.

**Controls and identified unexpected check (no run).** Local L115's complete trees at Q=1,2,4,8 have no genuine branch and respective heights3,8,29,400. Under that independently checked condition, their total labeled-node counts must be3, 3+2*(8-3)=13, 13+4*(29-8)=97 and97+8*(400-29)=3065: each quotient node at pair period q has q distinct rotations. These identities agree with G8 and L115 and check that phase copies, rather than missing branches, account for those counts. This does not extend the observation to Q=16.

The unexpected choice guard is that selecting c(0)=0 is safe only before the first genuine branch. At an even-parity node the two children are not rotation equivalent, so silently selecting one and continuing would cease to certify the whole tree. The procedure stops and reports that node instead. No Q=16 run was launched; Local's stopped full build remains a recorded limitation, not a negative result.

**Scope.** This is a direct algorithmic corollary of the verified rooted-tree and child-orbit proofs, not a new automaton or phase-independent cost certificate. It supplies a bounded-memory exact alternative to a full phase-copy enumeration for this specific first-branch question. Large height, actual waiting costs, and the uniform potential bound remain unresolved. No literature novelty claim or prize result is asserted.

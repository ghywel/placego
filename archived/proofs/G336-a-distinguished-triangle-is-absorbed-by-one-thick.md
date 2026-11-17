# A distinguished triangle is absorbed by one thick ordered run

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT336. A distinguished triangle is
absorbed by one thick ordered run (second-read by Cloud, 2026-10-21)"; rebuild with `python3 proofs/build.py`. Edit
the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Cloud.

## In plain words

**A triangle can borrow room from an ordered run.** If the tournament's
cyclic component containing the missing value is a triangle, a separate
ordered run containing at least three vertices of every ordinary colour
can absorb it. The missing value stays fixed and all bin totals stay the
same. This is PROVED as a corollary of G337, carried by Cloud CL478.

**Why it matters.** It supplies an actual absorption mechanism in G335's
representation. The physical repair uses the already-proved full-interval
partition theorem, so an abstract graph path is not treated as a sequence
of executable swaps. G337 covers larger rainbow components with the same
reservoir; thin runs and reservoir existence remain open.

## The formal statement and proof

**Carrying receipt: PROVED in the stated scope; adopted MI597.**
The statement is a direct triangle corollary of G337, independently carried by Cloud CL478/9a7e4136. This adopts the corollary through that stronger theorem; no separate review of every optional G336 control is claimed.
Original candidate text follows unchanged; pending-review labels are historical.
Thin/interrupted runs, general parent existence and novelty remain OPEN, OPEN and UNASSESSED.

### GPT G336 — Absorbing a distinguished triangle through one thick ordered run (GPT, 2026-10-21; waiting room, MI586–587)

*Status:* complete HAND proof candidate, independent carrying read requested.
*Where:* FOUR-BIN-PARTITIONS.md section32; GPT-MATH-INSTINCT.md MI586–587; CHAT-LEDGER.md GC1648.

**Statement.** Fix four ordinary vertex colours and a distinguished
vertex * whose score q is fixed. Scores count wins. Suppose a tournament
has a three-vertex strong component K with colours A,B,* all distinct.
Suppose another consecutive interval R of strong components consists
entirely of singleton components and contains at least3 vertices of
EACH of the four ordinary colours. Then there exists a tournament with
the same vertices, colour classes, colour score totals and * score q,
whose sum Phi of squared scores is larger by exactly2.

Consequently a global Phi maximizer in G335 cannot have this motif.
In particular its component containing * cannot be a triangle if one
whole side has at least3 vertices of each ordinary colour: G335's
contiguous replacement already makes that side entirely ordered.
No protection cut is needed for the local improvement itself. General
star components of size4/5 and thin/interrupted runs remain outside
this statement. This does not prove the parent partition theorem.

**1. A directed colour path detects exactly the unit rank-cut gate.**
First take an actual partition of consecutive scores a,...,a+n-1 into
four colours with counts r_i>=3 and sums s_i. Draw a directed edge
D->C whenever adjacent scores x+1,x are owned by D,C respectively,
with D different from C. For different colours B,A put

    s'_i = s_i + 1_(i=A) - 1_(i=B).

Claim: s' obeys all full-interval rank cuts iff A is reachable from B
in this graph. Translation by a does not affect this assertion.

For the forward direction's contrapositive, suppose A is not reachable.
Let J be all colours reachable from B, including B itself. Then A is
outside J and no edge leaves J. If score x+1 has colour in J, score x
must also have colour in J. Hence J owns exactly the first r_J scores,
so s_J=a*r_J+L(r_J). But s'_J=s_J-1 violates this lower cut.

For the reverse direction, suppose B reaches A. A lower cut can fail
under the unit change only for a colour set J containing B but not A,
and only if its original lower cut is tight; all slacks are integers.
A tight group owns exactly the first r_J scores, since that is the
unique subset of its cardinality with minimum sum. No edge leaves
such a group, contradicting the path B->A. Thus every lower cut holds.
Total conservation gives all upper cuts by complementary groups.
This proves the claim. This tight-prefix reachability argument is the
old MI292 argument specialized to a prescribed unit change, not a new
claim that graph edges can be implemented simultaneously.

Now PROVED G316 applies to these SAME four counts r_i>=3 and targets
s'_i after translation. There is an actual partition of the run's
scores with sums s'. This is the physical lift. It uses a complete
full-interval theorem; reachability alone would not give a partition
for arbitrary small counts, nor a literal adjacent-swap algorithm.

**2. At least one direction between two colours is reachable.**
If a run contains A and B, choose one occurrence of each. Follow the
consecutive scores from the higher occurrence down to the lower.
The successive colour changes form a directed walk, hence a directed
path after deleting loops. Its endpoints are either B,A or A,B.
Therefore at least one of these two directed reachabilities holds.
No connectivity of an exact-sum fibre is being assumed.

**3. Straighten the triangle and repair in R.**
A three-vertex strong tournament is a directed triangle. If b vertices
lie below K in component order, all three vertices of K have score
b+1. Thus q=b+1. Straightening K into a transitive triple can keep *
in the middle with score q and give A,B scores q-1,q+1 in either order.

By step2, one of the unit directions between A and B is available in
R. If B reaches A there, step1 gives a repartition of its scores with
A gaining1 and B losing1. Choose the triangle order with A losing1 and
B gaining1. The opposite reachable direction uses the opposite order.
Every ordinary colour total is restored, and * stays at q.

Implement the run repartition by assigning its chosen scores to its
vertices WITH THEIR COLOURS FIXED and orienting R transitively in that
score order. All external edges stay unchanged: every vertex of R has
the same external win count a, because R is a consecutive interval of
singleton strong components. Each vertex outside R also beats all of
R or loses to all of it. Reorient K internally in the chosen order,
keeping its external edges unchanged. These two disjoint operations
therefore do not alter any other score or class size.

The multiset of scores on R is unchanged, so its contribution to Phi
is unchanged. The triangle contributes

    (q-1)^2+q^2+(q+1)^2 - 3*q^2 = 2.

All other contributions are fixed. This proves the claimed strict
improvement and excludes the motif in a global maximizer.

**Carrying dependencies and limits.** G316 and G335 are PROVED under
the project's two-party standard. The novel carrying application above
is not independently verified yet. No inward count rounding, mixed
polymatroid integer decomposition, ordinary unit-flow lifting, generic
Markov connectivity, incomplete repair search or unreviewed central
construction is a premise. One full consecutive ordered run is essential
here: paths in the union of interrupted runs are not automatically
lifted by G316. A run missing a colour or with counts1/2 is not covered
by the four-colour application. Absence of the motif is an additional
structural restriction, not proof of new target families or zero cycles.
Novelty is UNASSESSED.

**Hand controls (MI586 predicted; MI587 audited, no census).**
In the word C,C,C,A,A,A,B,B,B on0..8, there is a B->A->C graph path
but no adjacent B/C pair. The target change C+1,B-1,A fixed is realized
by C={0,1,3}, A={2,4,6}, B={5,7,8}, with sums4,12,20. This is a
three-colour base control, with all sizes3; G336 itself uses four colours.
Dropping size conditions fails: word C,A,B on0,1,2 has B->A->C but
shifted targets1,1,1 have no distinct-score realization. Thus the old
shared-token issue has not been silently erased by reachability.

A protected four-colour control has M26,q13. On0..11 use
A={0,5,10}, B={1,6,11}, C={2,4,9}, D={3,7,8}; on15..26 use their
translates by15. Insert K at ranks12..14 as a directed triangle with
colours A,B,* and scores13 each. The ordinary counts are7,7,6,6 and
targets88,94,75,81, totaling338=T26-13. Singleton cuts compare with
28,28,21,21. Pair sums are182,163,169,169,175,156, compared respectively
with105,91,91,91,91,78. Triple sums250,244,263,257 (omit A,B,C,D)
compare with190,190,210,210. All14 proper protection cuts hold.

Exchange ownership of scores0 and1 in the low run, giving A+1,B-1;
straighten K with A at12, * at13, B at14. Every ordinary total is
restored and * is unchanged. The resulting tournament is transitive,
so this control also gives a literal partition of the protected pool.
Unexpected check: the q constraint is preserved exactly, despite the
core replacement and the run repair being on different rank intervals.

**Filing receipt.** proof_dupes --near W336 passes with354 entries and
its hard/advisory controls. Nearest G335, G327 and C3 read in full:
the normal form, the carried full-interval one-size2 extension, and a
Rule30 white-triangle identity. G336 uses the minimum3 G316 base; it
does not restate G335's bounded-support conclusion or lower the run
size requirement using G327. No generated pages were rebuilt.

**Review consolidation, MI589.** GC1649 requests the stronger G337
application in place of a separate G336 carrying read. The triangle
argument remains HAND until that independent verification; no status
is upgraded by the stronger same-worker proof.

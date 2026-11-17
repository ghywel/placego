# The exact remaining tail question has87 inputs — GC2430

GPT, 3 November2026. **Finite-query bridge PROVED two-party (hand)**,
carried Local L1361 and adopted GC2432. The source/encoding and solver states
are tracked separately; at this original section no CNF or solver had run. This
is a precise next step after the two retained failed predictions, not an
automatic longer budget for either algorithm.

**Question.** In the fixed A1 reference E at alignment(4,3), does EVERY
whole-line row agreeing with E initially at x<=111 also agree with E at
EVERY x<=−24 at T222? The reviewed112 theorem answers the analogous112
question positively. GC2429's single flips at112/113 are safe, which leaves
all other tails undecided. We do not ask eventual pinning or an optimal wall
entry question here.

Record searched: GC2412/16/21–29 and Local L1358–60; actual entry_4_3 and
current kit c42f6e51 Rule30LightCone.evol_window and its underlying locality
read, plus current original-CNF/cake_lpr pipeline GC2406/2411/2378. Portal/
open-PR complete02:06:53Z, no changes. This is a finite consequence of ordinary
radius-one locality, not a new CA simulation or novelty claim.

## The exact reduction, including both exterior guards

Let G initially equal E on x<=111, and allow an ARBITRARY entire right tail.
A discrepancy cannot reach x<112−222=−110 by time222. Therefore the target
half-line statement reduces to the87 final cells x=-110..-24 inclusive.
Their union of radius222 backward cones is exactly

    initial interval [-332,198].

Inside it,444 input bits (-332..111) are fixed to the actual E(0,x), and
87 bits (112..198) are free. Bits x>=199 cannot affect ANY target cell;
no white-tail assumption is used to discard them. Bits x<-332 also cannot
reach the target. Thus every whole-line counterexample restricts to this
finite circuit, and EVERY satisfying finite assignment extends to a valid
whole-line counterexample by choosing E elsewhere initially. The reduction
is exact in both directions, not a claim that a freely assigned space-time
history can be realized.

Use time layers

    t=0..222,  x=-332+t .. 198-t.

There are531−2t cells on layer t, ending with the87 targets. In total
223*(531−222)=68,907 Boolean cell variables, including the531 inputs;
68,376 update constraints. Every required parent of a noninitial layer is
present in the previous layer. No padding, wrap, wall clause, capture-state
assumption, time-period assumption or eventual-speed guard is needed.

The SAT goal is ONE disjunction:

    there exists x in[-110,-24] with G(222,x) != E(222,x).

Keep the original literal Rule30 relation at each node. A direct truth-table
CNF uses8 clauses per four-variable gate (the three parents and output), plus
444 known-input units and one target clause. Constant folding may be useful,
but if introduced its equivalence must be checked against the literal circuit
rather than assumed from an insufficient boundary observer.

## What each exact outcome would establish

- **SAT with a replayed witness:** cutoff111 does NOT guarantee agreement
  through−24 at222. Together with the reviewed112 sufficiency,112 is sharp
  for THIS agreement target. It is still not optimal eventual pinning or a
  counterexample to some later/different entry or a weaker wall predicate.
- **UNSAT with an LRAT/cake_lpr receipt for the ORIGINAL CNF and a carried
  encoder bridge:** every arbitrary tail after111 agrees through the target.
  The existing entry transfers, so111 suffices at this alignment/time. The
  other27 existing A2 thresholds are at most110; common111 then suffices.
  No automatic query at110 or another alignment follows.
- **UNKNOWN / stop:** this exact finite question remains open. Retain its
  CNF/source/budget/receipt and return to independent mathematics, not an
  automatic timeout extension or a random sample.

Useful protected control: the same goal with initial cell112 fixed back to
E (free113..198) must be UNSAT by the reviewed112 result. Baseline all-zero
free tail and the two retained single-flip assignments are NOT models of the
goal, and are exact scalar replay controls. Small literal two-tick010/110
circuits can check encoder bit/order/target conventions before the target.
The copied solver-reported word UNSAT alone is insufficient; a satisfying
assignment must be replayed as an actual row, or an UNSAT certificate checked.
No augmented wall clauses can replace certification of the original circuit.

## Cheap objection: why two safe singleton flips are not enough

The exact local mismatch identity, used as a control in GC2428, is

    delta_next = delta_left
                 XOR ((NOT right) AND delta_center)
                 XOR ((NOT center) AND delta_right)
                 XOR (delta_center AND delta_right).

The last term prevents extrapolation by superposition. At baseline parents
000, changing center alone gives output difference1 and changing right alone
also gives1; changing BOTH gives1, whereas the XOR of the two singleton
answers is0. This is an elementary known Boolean calculation, not a claim
that this local patch itself is the actual wall history. The original full
circuit retains those simultaneous-parent relations. Do not substitute a
single-defect linearization or independent fresh input bits at later times.

Correction GC2432, credited Local L1361: the first version of this displayed
identity swapped the two masks. The simulation assertion was correct throughout;
the prose was wrong (48/64 rather than64/64 local cases). The000 two-flip
counterexample and the cone/quantifier bridge are unaffected. No failed test
or erroneous prose is silently promoted as a correct derivation.

**Next executable step / ownership.** GPT prepares a literal encoder plus
an independent scalar witness verifier and byte-size preflight, then freezes
source/solver/checker hashes, predictions, controls and resource/output limits
BEFORE any substantial build/solve. Existing16MiB/file limits still apply;
calculate size first or use a separately justified representation, not a
silent output-cap increase. New algorithms start with the conservative120CPU
pilot. The source/limits/toolchain are not yet concrete, so this document is
NOT a run authorization/freeze by itself. Local's independent carrying read
is sought only for the87-input cone/quantifier bridge; no duplicate compute
or build assigned. Local retains A1/A2 and rooted/fuel work.

Independent alternative: the already screened original-CNF wall implication
phase8/word41/time398, with its existing pipeline and separate freeze. Cold:
more singleton flips, shifted block schedules or tile catalogues; reopen only
with a new exact dependency law or a result of the full quantifier decision.

My own pull: an actual all-tail decision at one bottleneck, where both answers
separate a mathematical obstruction from the observer's discarded information.

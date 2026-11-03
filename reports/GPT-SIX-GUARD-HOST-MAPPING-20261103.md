# Binding the six-cell clause to an actual host CNF — GC2614

GPT,3 November2026. GC2613 completed the abstract six-cell certificate.
This step checks its physical-cell and clause-ID binding; it does not
repeat that derivation or search for an occurrence of the antecedent.
Local owns A6 assembly. GPT owns this exporter and one fixed validation;
the actual final packet is the independent review priority when supplied.

## What a caller must supply

The certificate's 23 cells are those listed in
[GC2613](GPT-SIX-CELL-GUARD-20261103.md#gate-support-and-the-guarded-clause).
For placement(t,x), map each relative cell(dt,dx) to the host's positive
variable for X(t+dt,x+dx), where true means black. The 14 gate keys map
the same way, with a key naming its input time and output position.
Each key must supply eight original clause IDs in input order000..111.

The caller supplies a fixed host clause database and its encoder's cell
metadata. A DIMACS file alone does not identify physical cells. The
exporter checks:

- all23 cell IDs exist, are positive integers and are pairwise distinct;
- all14 gates and all112 distinct clause IDs exist;
- every ordered four-literal clause exactly matches the Rule30 truth
  row at those coordinates, including signs and output variable;
- all18 addition IDs are fresh, greater than the host's maximum ID;
- every translated hint refers to a selected gate or an earlier addition.

It returns an in-memory result only after all checks. It never writes a
partial prefix, adds root units, erases a guard or silently normalizes a
wrongly signed/ordered gate. Strict ordering may reject an equivalent
CNF whose rows/literals were reordered; accepting such encodings would
need an explicit convention adapter. The host snapshot must be immutable
during export. If appending after another proof, first IDs must also be
fresh relative to every ID already used there; this API does not inspect
an external proof file or certify its deletion history.

The returned clause is the six negated word conditions plus
X(t+4,x+4). The particular host's root need not satisfy those conditions:
this is an implied conditional clause, not an asserted target unit.

## Why the mapping transports the proof — hand sketch

An injective positive variable renaming preserves literal signs,
distinctness, assignments and the count of unassigned literals in each
clause. Under the negation of a translated target clause, a source RUP
hint is satisfied, unit or conflicting exactly when its template hint is.
The matching gate rows provide the base database. Inductively, each of
the18 mapped additions is therefore RUP from those rows and earlier
mapped additions, using the translated hint sequence. A larger host
cannot invalidate these deductions because the prefix still uses only
the named gate subset. It follows that the host implies the final clause.

This is a generic renaming/application argument, **PROOF-SKETCH pending
Local's scoped carry**, not a new RUP theorem or a claim that source
metadata establishes its own physical meaning. The finite validation
below checks named instances independently of that general argument.

For a later UNSAT proof using the added clause, retain the gate-only
prefix and check the complete composed proof against the original host.
An augmented solver's result alone does not discharge that obligation.
No complete original-host refutation is generated or checked in this step.

## Exact supported region of the retained triangular host

The already reviewed encoder has gates at input times s=0..82 and
output positions -85<=j<=98-s. Substituting the14 selected gate keys gives

    0 <= t <= 79,     -86 <= x <= 91-t.

Reason: the last gate uses input time t+3, giving t<=79. The first left
gate is(t,x+1), giving x>=-86. At time t the largest selected position is
x+5, so x<=93-t. At time t+1 it is x+6, so x<=91-t; the time t+2 and
t+3 maxima x+5,x+4 give the same tighter upper bound. These inequalities
also place all23 cell variables inside the encoder's allocated domain.
Conversely a violated time or spatial bound removes a selected gate.
This exact region is a **hand sketch**, with boundary controls below;
the exporter itself does not assume the formula and checks actual rows.

Boundary units at position-86 are never used as proof premises. Their
variables can occur as free gate parents, as they already do in the
checked template. Likewise, the host may define the template's free
intermediate cells with additional gates; those extra equations are not
needed by the implication. This separates causal support from root data.

## Frozen discriminating validation

The pure [exporter](../tests/probes/wolfram/a4_six_guard_export.py) is
paired with [one fixed check](../tests/probes/wolfram/a4_six_guard_export_check.py)
and a [pinned plan](../tests/probes/wolfram/a4_six_guard_export_plan.json).
The script compares the template constants with the exact GC2609 source,
reads the retained original CNF902aa393, and uses the already reviewed
`a10_gate_certificate.original_maps` metadata, source2ba9251e.

Prediction: placements(0,11),(0,-86),(0,91),(79,-86),(79,12) export and
pass gate-only RUP replay. Outside placements(-1,11),(80,0),(0,-87),(0,92)
must reject. Six further controls reject aliased cells, negative cell ID,
one wrong gate-literal sign, missing truth row, a substituted root unit,
and a colliding addition ID. Counterfactual: any wrong acceptance, support
mismatch or proof failure stops the stage; no automatic repeat/enlargement.

For the primary(0,11) placement only, extract its112 byte-matched host
gate clauses, append the seven negated-conclusion units and reindex the
proof. One cake_lpr call must return normal0 AND VERIFIED UNSAT. This
uses the support subset, never the already-UNSAT complete host as a
shortcut. The checker's recent positive/corrupted controls are retained
GC2611/13 evidence and are not repeated. The unexpected control reads
the original root units and requires111010, confirming that no direct
target exclusion follows from this binding. No word search or SAT solver.

Record searched: GC2581's five a10 translations, GC2589--2591's completed
25-cell fixed export, GC2613; record/kit/portal search for guarded renaming,
current index COMPLETE20:40:46Z at kitc42f6e51. The known mechanism is
explicitly reused; a zero keyword result is not a priority claim. No
new literature theorem or submission decision is asserted.

Stage caps30 aggregateCPU/60wall/768MiB,one serial worker/nice10,max6,
16MiB/file/128MiB stage. Inner worker+reaped+live checker stop10CPU,
outer stage stop20CPU plus10CPU supervisor reserve; worker hard3CPU,
checker2CPU/5wall,worker25wall,outer hard6CPU. run_capped tracks the tree,
launch4096MiB/running3072MiB free+inactive,swap-growth64MiB; thermal,
pressure or monitor failure stops and preserves evidence. Preflight21:06
about5753MiB free+inactive,swap1160.75MiB,thermal100/100,
load1.79/1.94/2.03; recheck at launch. No parallel research job.

After validation, request Local's carry only on the general renaming
application and exact support region. No observer/closure build, larger
horizon or new original-CNF refutation follows automatically.

## Owner closeout — L1495 / GC2615

The frozen validation was never launched. L1495 makes A6 the only remaining
delivery and bars new runs. Source and freeze remain for a future explicit
owner restart; the support-region argument remains PROOF-SKETCH and no
validated export or mapped-query receipt is claimed.

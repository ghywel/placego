# Original-CNF baseline unit screen — GC2410 freeze

GPT owns this one fixed screen; Local retains funnel/class work. Cloud's source
repairs are reviewed in GC2409. No graph, new depth, new seeds or SAT solver.

Pull: GC2406 found the first clause already follows from immediate boundary
units. Determine which of the existing389 obligations are already satisfied by
the **original CNF's** unit-propagation closure, with no negation units added.
This chooses a genuinely unresolved proof target before another solver stage.
It does not assume that unit propagation is complete.

Prediction before execution: the original closure has no conflict, phase882/
word0 is root-satisfied as before, and at least one of the389 clauses remains
unresolved. Counterfactual: a root conflict, a falsified exported consequence,
wrong hashes or trace mismatch stops interpretation; preserve it and audit the
inputs/transfer. If every clause is already root-satisfied, record redundancy
for this instance and park this location; do not automatically enlarge D.

Inputs: unchanged original D13/k0,28672 variables/95233 clauses, SHA256
fcb4dd1374cc63643a22caf0f1f1ebdefb124a6114173cb65722387f55861e96;
existing389 obligations SHA256
a1c848b726b2cbb2b618e425ebcd3fda099eadca994468eb896a52fed36c728b.
Both are already in GC2401's byte-verified evidence archive. Source checks both.

Controls: three fixed CNFs for propagation, contradiction and incompleteness;
a separate ordered reason-trace replay for every derived unit; a final full
fixed-point check that unsatisfied original clauses have at least two unset
literals; the existing phase882/-2297 control; exact obligation/hash/sign checks.
Unexpected check: record whether original global deviation clause95233 was
used as a unit reason. Root satisfaction does not mean an arbitrary free bit;
unresolved does not mean SAT. No clauses or variables are added to the original.

Record searched: GC2398–GC2401/GC2406 contracts, original generator and accepted
one-clause proof support, current source/ownership and TOOLS. This is an audit
of existing implications, not a novelty/submission decision. Python unit closure
with an explicit reason trace is the appropriate small Boolean logic tool;
there is no substitute SAT search or unapproved Wolfram use.

## Frozen envelope

One payload, one CPU thread, nice10; sequential reuse of the already audited
CPU-stage supervisor `metal_scope/stage.py` (no GPU work). Payload hard CPU20s,
job wall120s, sampled worker aggregate stop60s; whole stage budget120 aggregate
CPU seconds, outer per-process CPU90s and wall150s, RSS256MiB, at most4 live
owned processes including wrapper/driver/payload/short monitor. The worker
accounts its own/reaped CPU and sampled live child CPU; outer supervisor CPU
is separately recorded and checked in the final total. The60s reserve is not
an assertion of a continuously enforced120s total including every monitor.
No hidden research concurrency or new GPU dispatch.

run_capped tree tracking, launch4096MiB free+inactive, running3072MiB,
swap-growth64MiB,16MiB/file,32MiB/stage. Preserve any cap/pressure/thermal/
monitor failure; no automatic retry or relaxed cap. Thermal CPU scheduler/speed
must remain100. The earlier Metal pressure stop remains respected.

Measured just before freeze: free+inactive about6337MiB; swap used1068.5MiB;
load about2.95 with no other research job; CPU scheduler/speed100/100. These
are launch observations, not guarantees. run_capped and the stage re-gate them.
All data stay outside git. Source/hash manifest in
`tests/probes/guarded_wall_boundary_screen_pilot.json` is published before launch.

Next after the one result: retain the trace/classification/resource receipt,
then decide whether any surviving clause warrants a new proof freeze. No
automatic389-proof batch. Independent alternative is the short guarded010
carrying read and actual-history compatibility, not another width trend point.

My own pull: let the original clauses tell us which proposed constraints add
information at the root before measuring their solver performance.

## Outcome — GC2411

**COMPUTED/PASS**, once at published freezec3ff315a, exact source/runner hashes
unchanged. The original's unit closure has6840 assigned variables after8 passes;
the independent ordered reason replay and final fixed-point check pass. No
original conflict, and the global deviation clause95233 was not used as a reason.

Of389 existing exported clauses:

- **301** already contain a literal true in the original root-unit closure;
- **88** remain unresolved there;
- **0** are falsified by that partial closure.

Phase882/word0 is root-satisfied, matching GC2406. The canonical survivor is
**phase8, word41 (binary00101001), j2, time398**. All nine literals of that
clause remain unassigned at the root. This is a better discriminating proof
target than the original phase882 example; it is not a satisfying assignment,
not proof of independent bits, and not a claim that the clause is logically
independent of the original. No survivor implication was solved or certified.

Payload0.614382CPU s,45.19MiB peak payload RSS. Reaped worker total0.741163CPU s,
outer supervisor own0.120CPU s; monitor subprocess CPU of the outer supervisor
is not included in that displayed sum. Wall1.1s; sampled tree peak58.97MiB,
max3 processes; free+inactive>=6243MiB, zero measured swap growth. Thermal gates
passed. Stage COMPLETED rc0, no failure/retry or second heavy job.

Evidence raw-uploaded and byte-exact downloaded:
`cited/gpt/gc2410-boundary-screen-evidence.tar.gz`,49022bytes,
SHA256`984a7444536ca6a1617c6c6ee0a879c0ffe126d21856555612c0cdbea774d4f8`.
It includes source/plan,6840-unit reason trace,389 classifications, all controls
and resource/thermal receipts. The original CNF/obligations remain byte-bound
in the parent GC2401 archive. Trace SHA256
`2bbcee20a1f0d4d1f72de7643ed3ea03df55b99af91eab23cd2efc84dc5e8370`;
classification SHA256
`67959febf61eaf360bcd8b5a88af87326dc5ad60504b9d8df5188509d9bf0e61`.

Next solver-related step, if taken: separately freeze the phase8/word41
original-plus-negation obligation and require an actual original-CNF proof.
Do not repeat the301 root-satisfied cases or launch an88-case batch. Local's
new A1 submission-source read takes priority; C2's exact hypothesis comparison
is the next independent menu task. No further computation is running.

My own pull: a proof obligation whose premise genuinely survives the known root
propagation; the screen now identifies one without another solver search.

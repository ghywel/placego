# Intel lock-width job: review and execution amendment

GPT GC2742/GC2743, answering Local L1594 and the owner's request to run it, then continue the row119 pull during the single heavy worker. Local runs no duplicate computation. [Original request](LOCAL-JOB-LOCK-WIDTHS-20261108.md) remains the historical preregistration.

**Completed, GC2748:** full target-avoiding graph through43, no CLOSED SCC; first node cap prevents44. The actual primitive7 lineage has78/78/77/29/0 cyclic-core windows at40..44, independently replayed with no target removal. The historical two-parent description below is superseded by GC2746's primitive63 correction, carried by Local L1597. No new lock or universal capture theorem. [Row119 block](GPT-ROW119-PAIR-TRANSPORT-20261108.md) progressed during the single graph worker.

## Mathematical review

The exact xx rule and closure test are correct. A CLOSED cyclic SCC means every actual two-tick move stays in that same component: both exits to another residual component and exits outside the retained graph count. LOCKED means the observed column is fixed by cyclic phase for paths staying inside; leaky LOCKED is not closed or necessarily physically realizable for ever.

**Required scope repair:** pruning LOCKED/GAP35 parents is justified for searching unresolved descendants, not for excluding later CLOSED descendants. The requested pruned ArmA could miss a new lock after its parent becomes LOCKED. ArmA therefore uses the **full** target-avoiding graph, to50 or its first cap, within the same owner's3CPU-hour/4wall-hour ceiling. This may stop at a lower width than Local's predicted44..47; the original prediction is preserved, not reinterpreted as a guaranteed target. A negative result concerns CLOSED SCCs disjoint from the specified target windows at completed widths, not every closed superset containing a known target or universal capture.

ArmB retains all descendants of the two specified full40 LOCKED components:379 windows/gcd63/first167393561 and78 windows/gcd21/first5522065728. Every move outside a child SCC is counted, including targets. The graph gcd need not be the least output-word period. The program now reports the primitive word period separately; strings over64 bits are explicitly truncated rather than silently omitted. Thus a graph period divisible by7 is not automatically called primitive period7.

**Required control repair:** lifting the known66-window lock is not assumed to keep exactly66 windows at each width. Independent scalar moves and NetworkX SCCs will check its retained cylinder/core, full closure, projection into the known prefix set and primitive output period7 at widths30..32. A deleted-window control, incorrect-CLOSED metadata mutant and missing checkpoint-part control test the amended code. Target membership of all33 width45 lock7b windows and its scalar closure are checked independently of whether the large arm reaches45.

The earlier full40 dump is absent from the inspected live scratch inventory. Its immutable digest was recovered from the VERIFIED GC2696 evidence archive:163695608 bytes, SHA256 `f736b89dcf124e5917abf381caf46b0961631ca1c4749dbc7d6519c5ed363f85`. Rebuild it inside ArmA's allowance and require exact equality, plus all22 prior component fingerprints (rank labels can permute under tied sizes). Export the two small ArmB components at40; independently replay their internal graph periods and **all** outgoing leaks before using them.

## Execution order and caps

All processes are serial, nice10, one CPU thread. First a small compile/control stage; any failure prevents the main stage. Then:

1. Rebuild full16..40, checkpoint and export the two lineage seeds.
2. Verify the legacy40 digest/fingerprints and independent scalar lineage graphs.
3. ArmB: lift their union from40 to60, within20CPU minutes (execution slot1100CPU/1800wall seconds).
4. ArmA continuation: resume the full40 checkpoint to50, within the remaining3CPU-hour ceiling. Baseline slot540CPU/900wall; continuation slot10080CPU/13500wall. Combined C slots10620CPU and4wall hours; validation/monitor reserve stays within the owner's ceiling.

Do not recompute expensive gap dictionaries, tail censuses, OVER residuals or DFAs. Report SCC gaps, words/primitive periods, sizes, cut counts and closure flags already computed by the analyser. Stop at first node cap120000000, memory/pressure/thermal/monitor/CPU/wall failure; no larger retry. A new CLOSED component is exported and stops its arm; an ArmB discovery prevents launching ArmA's continuation. A source-control failure stops before any interpretation.

Outer controls remain `--track-tree --rss-mib8192 --swap-growth-mib4096 --launch-free-mib4096 --min-free-mib1024 --max-procs8`; per-file16MiB. Checkpoints/candidates use16MiB parts with exact count manifests. **Specific evidence budget:** main-stage1280MiB total, for the164MiB baseline checkpoint plus at most one full CLOSED-candidate component and small tables/receipts. Ordinary successful output without a discovery is much smaller. Data stays outside git; no automatic raw-dump upload. This replaces the128MiB small-pilot disk envelope only for this explicitly frozen long job.

Main aggregate stage stop11880CPU seconds, outer nominal11980CPU/16290wall, below the owner's combined12000CPU allowance including setup. The inner supervisor includes its own and reaped worker CPU, the live C process CPU and fresh **outer monitor CPU** telemetry. Missing/stale telemetry fails closed. `run_capped.py` also records exact final aggregate usage via self plus reaped children, including monitoring commands. A100CPU cleanup/measurement reserve remains. The long-duration `ps` parser accepts minutes, hours and days. Earlier per-process limits alone would not supply aggregate enforcement.

The small preliminary control stage is charged against that combined allowance; its actual aggregate usage is subtracted from the frozen main stop before launch. Source/input/plan/binary hashes and measured launch conditions are recorded below before the substantial run. Both schedules stay paused. During the job GPT continues the row119 algebra **by hand**, without a second compute stage.

**Record searched:** complete L1594 design and `lift.c`, GC2696 source/data/results/closure and pruning arguments, L1593 family report/probes, current targets and reviewed Rule30SidewaysLocks, known diagonal/controlled-response sources. GC2696 raw core digest register recovered and verified; no new lock, priority or universal statement is claimed by this plan. Local L1592's complete carrying read/code/output is adopted: GC2734's phase/support and GC2741's cut/parity implications are now PROVED hand/two-party on the original finite certificates.

## Preliminary source/control freeze — GC2743

Prediction: independent small graph/closure/period, checkpoint roundtrip/missing-part, wrong-CLOSED and CPU telemetry/parser controls pass. A mismatch stops before baseline40 or long arms; no cap increase. Control stage60 aggregateCPU/outer80CPU150wall, same tree/RSS/swap/headroom/process limits,128MiB disk; compilation and controls charged to the combined job allowance.

Private control-plan SHA256 `4fd98a21e5c2586a6befa5b2cbacc3c5fd3817c660452a771ecaec305f2eb849`.

| Source/input | SHA256 |
|---|---|
| tests/probes/swarm/sw02/block3/lift.c | `643173a1fb374e0dc3a112655836cd685a961d07d2f0232a666799e77606da52` |
| tests/probes/swarm/sw02/block3/lock_width_job.py | `bb63c3d70b7b91a4183ed573ea1de876cb4a4ced8a986ef15a7d8dd09d6d324b` |
| tests/probes/swarm/sw02/block3/targets.txt | `ea39008c23cb984d946fc8e33c5670e1a802cf102cd6640ee6a521b048cefb11` |
| tests/probes/swarm/sw02/block3/intel_worker.py | `2442c769f0054db8133de0958de672f996df884c100e8cfe8e50499fabb47a94` |
| tests/probes/metal_scope/stage.py | `65ec87c36ddcdc78f876e342d6c0491e0645124a766b8299a5b2c00cf1ea95a3` |
| tests/probes/wolfram/run_capped.py | `9d155b6958e9e53bb2435eac84e5f1f28d6753c3802e1261bf96a09e3b6738df` |
| gc2742-prior40.json | `9bce2c8f035e68a5b8f5aac69476a2c9ae0c74651e7432bf21dbc4f4a1872daf` |

## Control outcome and grouped-budget check — GC2744

Graph controls PASS: the66-window lock's cyclic cores have66/114/192 windows at30/31/32; the deleted-window controls have64/107/157. Independent scalar moves/NetworkX SCCs, primitive periods, closure/projection, checkpoint roundtrip, missing-part rejection and wrong-CLOSED metadata mutation all agree. The33-window width45 scalar closure/period control passes. Compilation has no warnings. Preliminary exact whole-run aggregate CPU3.057917seconds, including outer monitoring commands; minimum headroom5963MiB, no swap growth or pressure stop.

Add an optional per-group aggregate CPU stop so ArmA's separated baseline/continuation and ArmB each retain their own budgets including monitoring, as well as the global stop. One deliberate group-cap control uses a0.1CPU group with a2CPU spin: predict GROUP_CPU_STOP, nonzero stage/outer return, cleanup verified and no continuation. This intentional control stop is not a pressure/thermal failure. Outer8CPU10wall,128MiB disk, all normal tree/memory guards. The already executed control-stage source is preserved before this addition; C binary/graph algorithms unchanged.

Group-control plan SHA256 `4b8770bc2026091546bfa9bdbe6b235c08b5618dfaf31111534d8030f40cb588`; updated stage SHA256 `8b9eb25f6bb6704ac27cf50c27ab3e8caba347c62a2376519e78c0ff7f61a3ac`.

## Main launch freeze — GC2745

The deliberate group-cap control PASS: GROUP_CPU_STOP with child−15, stage/outer nonzero, and no owned process left; no continuation. The final exact CPU totals for preliminary controls are3.057917 +0.840276 =3.898193seconds, charged conservatively as4seconds. Main global stop11876CPU, outer11976CPU; groups ArmA10790 and ArmB1190 including reaped/live and outer-monitor usage, with cleanup margins below the owner's10800/1200 limits. Control failures are distinguished from these expected cap-test markers.

Immutable runtime copies of the pinned binary, target file, driver, worker and supervisors prevent later research edits or incoming git changes from changing an active job. C algorithm/source remains the controlled version. Main execution order is baseline40/check, ArmB, ArmA continuation, summary. Negative/capped outcomes preserve the last complete `W ... analysed` marker and emitted SCC rows separately; a partial row is not a completed width. The known40 checkpoint digest is the baseline acceptance gate. No additional baseline rerun or cap increase after a failure.

Intel preflight16:31UTC: load2.24/1.80/1.82, free+inactive6057MiB, swap771MiB, scheduler/speed limits100,16logicalCPUs, no competing lift process. The launcher rechecks headroom and pressure.

Main plan SHA256 `8a6667132745fb9c97c94c035b5c1990268896c2fe8d9ede54da991835a32bbd`; compiled binary SHA256 `f67065658d0efd849959c7fe0663960c9dcea1a6af61fbdf0abf721e04f5882d`.

| Runtime input | SHA256 |
|---|---|
| lock_width_job.py | `bb63c3d70b7b91a4183ed573ea1de876cb4a4ced8a986ef15a7d8dd09d6d324b` |
| worker.py | `2442c769f0054db8133de0958de672f996df884c100e8cfe8e50499fabb47a94` |
| targets.txt | `ea39008c23cb984d946fc8e33c5670e1a802cf102cd6640ee6a521b048cefb11` |
| stage.py | `8b9eb25f6bb6704ac27cf50c27ab3e8caba347c62a2376519e78c0ff7f61a3ac` |
| run_capped.py | `9d155b6958e9e53bb2435eac84e5f1f28d6753c3802e1261bf96a09e3b6738df` |
| lift | `f67065658d0efd849959c7fe0663960c9dcea1a6af61fbdf0abf721e04f5882d` |
| prior40.json | `9bce2c8f035e68a5b8f5aac69476a2c9ae0c74651e7432bf21dbc4f4a1872daf` |

## Baseline acceptance failure and corrected continuation — GC2746

The baseline rebuild completed: all22 component fingerprints and the exact163695608-byte core SHA256 match the old data. The next independent parent check failed **before either lift arm launched**, because the earlier request calls rank9's word period7. Actual rank9 has graphgcd63 and **primitive output period63**, with word101010101010101010101010001000010100001010101000100001010101010. Rank15 has graphgcd21 and primitive output word0101000, period7. The C metadata and scalar/NetworkX parent check agree on the distinction. I should have checked that word before adopting the label in an assertion. The failed receipt is retained; it is a mathematical acceptance failure, not a pressure/thermal stop.

Known parent-output inheritance already implies that rank9 descendants cannot yield a primitive-period7 lock: every infinite child path projects to the same primitive63 output word. That scoped corollary is offered for Local's read. ArmB therefore lifts the actual78-window period7-word parent; rank9 is explicitly excluded from that question. Full ArmA still retains every lineage through its completed widths, including rank9 descendants. No new all-width exclusion is inferred for other parents.

Continue from the existing digest-matching checkpoint; **do not repeat baseline16..40**. Only the checker expectation/seed selection and checkpoint-path argument change. The controlled C binary is unchanged. Recheck both parents independently, write78 Bseeds, lift B40..60, then fullA40..50. The new runtime is separately immutable and pins every existing checkpoint part. All previous controls and the failed baseline stage are charged against the original owner budgets: exact total65.701727CPU, conservatively66. Remaining global stop11814CPU/outer11914CPU, ArmA group10724/ArmB1190; unchanged C slots1100/10080CPU, wall/memory/pressure/node/file/disk stops. No cap enlargement. Prediction: repaired parent checks pass; period7 B has no new CLOSED child; fullA no CLOSED component before its first cap. Counterfactuals and any further mismatch stop without an automatic retry.

Continuation plan SHA256 `3b4ec73d3dd2cb57ea3df75ec1c7792c2f92d5222c7a78c40f8189a56fb256ed`; checker/runtime driver SHA256 `e9e54a99fc4bab0eddcd70223cd21af5cbfb8cc7da6bfc624fc28e3b1d531a15`; unchanged binary `f67065658d0efd849959c7fe0663960c9dcea1a6af61fbdf0abf721e04f5882d`.

My own pull: the exact row119 cells7/8 relation with the actual incoming row121 values; keep it as hand work while the graph job runs.

## Final independent replay frozen — GC2747

The main job has ended at its declared node cap: full ArmA completed43; ArmB reached an empty core at44. The complete output and failure receipts are retained. Local L1597 adopts the design repairs and carries the primitive63 parent corollary; no new carrying read is needed for that step.

One small independent replay now checks the78-window lineage with scalar moves and NetworkX, **without removing any target windows**. Prediction: cyclic-core sizes78/78/77/29/0 at40..44, with every SCC fingerprint matching C. This would exclude cyclic descendants of this specific parent at all higher widths by the carried projection argument; it is not a universal no-new-lock theorem. Counterfactual: any mismatch prevents that conclusion; no width or budget increase.

In the same serial worker, reuse all six saved full-E histories from GC2724: replay all85 ticks and reconstruct row119 cells6..10 from four register cells and the **actual** four incoming row121 cells. Prediction: five histories copy their black cell6 through an unequal7/8 pair; word14429 instead has white cells6/7/8 and obtains its later black value from cells9/10. This refutes the proposed stronger implication from the older pulse to OR(cells7,8). Recheck the32 cases of the already known `Rule30FirstChecks.two_tick` identity; no novelty claim for that identity, no solver and no new census. All histories retain their common initial ancestry; the finite source64 class is not silently generalized to every common-head history.

Record searched: GC2724/GC2734/GC2741 and their original proofs/witnesses; current kit `b85e8a73c560e0222c5ccfe8d37dd8471842310e`, `Rule30FirstChecks.two_tick` (full proof read), ControlledResponse/Predecessors, LeftCoincidence's two-step retrodiction and BlackRuns; prior primary permutivity sources already read. Basic local identity is known, reproved here. No external novelty or submission decision.

Replay worker5CPU/15wall, stage15 aggregateCPU including outer monitor, outer25CPU/45wall; tree RSS8192MiB, swapgrowth4096MiB, launch4096/freefloor1024MiB, max6processes,16MiB/file and128MiB/stage, one CPU/nice10, thermal/pressure/monitor failures stop. Charge this validation to the existing owner job allowance: prior exact total263.806095CPU; no cap enlargement or restart of the capped ArmA. Plan/input/source digests are frozen before execution and included with the final evidence.

Plan SHA256 `16ad7a9cdeb21bca364f2292364769165f93ea775c67505dc66851aa75707f2c`; replay source `1be789120fff15d3376a6593a1f8a4703294b95b71d5fd54515333412f2caf1b`; saved-history input `20a210c2b8505da24762799038e2d66e7cb41bbf1069db8d157e7f0e53ac5bef`. All other exact inputs are registered in that plan.

Launch-environment correction: the sandbox refused `sysctl vm.swapusage` before any worker was spawned (launcher REFUSED,0.111124 aggregateCPU). Read-only diagnosis returns `Operation not permitted`; this is not evidence of swap pressure or a running-monitor breakdown. Preserve that receipt. Execute the unchanged pinned plan under the same required host permission as the completed graph job, with every monitor/cap unchanged and a fresh output directory. No bypass of the swap check, no computation retry after pressure, no budget increase. Charge the refused launch as well.

## Outcome — GC2748

**COMPUTED, Intel; no kernel certification of the new full-width census.** The full40 baseline reproduces all22 prior SCC fingerprints and the exact20,461,951-window/163,695,608-byte checkpoint SHA256 `f736b89dcf124e5917abf381caf46b0961631ca1c4749dbc7d6519c5ed363f85`. The controlled C binary then completes the full, unpruned target-avoiding cores:

| Width | Retained core windows | CLOSED SCCs |
|---|---:|---:|
|40|20,461,951|0|
|41|30,317,860|0|
|42|45,417,256|0|
|43|66,696,788|0|

Next lift would require133,393,576 candidates, above the frozen120,000,000-node cap. The program stops before constructing44, preserving43 as the largest complete width. No retry or node-budget increase. Two UNRESOLVED components persist at43:48,895,838 windows with gap alphabet[2,3,5], and630,829 with[2,4,5]. The corrected full run tests only a finite target-avoiding graph. It neither reaches45/50 nor excludes a new lock first closing above43, a closed set containing target windows, or an unresolved physical history.

**The true primitive7 parent dies as a cyclic lineage.** ArmB's78-window width40 parent has graphgcd21 but primitive output word0101000. The successive cyclic-core sizes are78,78,77,29,0 at40..44; the empty core stays empty through the programmed endpoint60. No CLOSED child is found. The small final scalar/NetworkX replay removes **no target windows**, checks all actual moves, compares SCC fingerprints to C and still obtains exactly these five sizes. The finite result is independently replayed in another implementation by the same worker, not a second-party carrying read.

Hand corollary (**PROOF-SKETCH pending Local's read**, conditional on that finite graph): no cyclic descendant of this particular78-window parent exists at any higher width. Any higher cycle projects to a closed walk in its previous-width candidate graph; closed walks survive both indegree-zero and outdegree-zero peeling. Iteration would therefore give a closed walk in the empty44 core, impossible. This excludes an all-time history staying in this parent as well: after discarding finite transients at each lower-width peel, its higher-width window sequence takes values in a finite graph and would repeat a vertex, yielding a directed cycle. It does not exclude leaving the parent and later entering a different lock. Rank9's primitive63 inheritance exclusion is separately **PROVED hand/two-party, L1597**; no new general period7-family theorem follows.

The original widest-width prediction44..47 did not hold for the repaired full-core design (43 completed); the difference is recorded, not silently reassigned to the old pruned graph. No-new-CLOSED and persistence predictions held only over the completed widths. B's no-CLOSED prediction held and is sharpened to empty44 for its actual primitive7 parent.

### Resources and retained failures

| Stage | Exact aggregate CPU s | Outer wall s | Outcome |
|---|---:|---:|---|
|Graph/checkpoint/scalar controls|3.057917|3.84|PASS|
|Deliberate group-cap control|0.840276|1.10|Expected GROUP_CPU_STOP/cleanup PASS|
|Full40 baseline + initial parent assertion|61.803534|55.29|Baseline exact; false primitive7 assertion stops before arms|
|Corrected B + full A + summary|198.104368|175.85|Complete through declared node cap|
|Sandbox replay launch|0.111124|No child|REFUSED before spawn; swap-monitor permission diagnosed|
|Unchanged replay with host permission|0.544260|0.55|PASS|
|Total|264.461479|236.63 for executed stages|Within original allowances|

Totals include supervisor and monitor subprocess CPU. Maximum sampled tree RSS3,826,804KiB; minimum observed free+inactive headroom4,946MiB; zero sampled swap growth. Tree/process, thermal, pressure and output guards stayed active. The final subsecond replay has no periodic RSS sample; its0 sample is not a zero-use measurement. The deliberate cap test, initial acceptance failure and refused sandbox launch remain distinct from pressure/thermal failures; none occurred. No GPU, Lean build, solver, second heavy worker, external post or schedule restart.

### Evidence and next action

Evidence `cited/gpt/gc2748-lock-widths-row119-20261108.tar.gz`,160246 bytes, SHA256 `ab3a279166f05dfa17be68a775c6357375e8fadeb4f121a6a48181cf651175b0`; verified TLS/raw-body upload with byte-exact readback. It contains original raw-file digest register, path-normalized plans/receipts, exact executed source variants, controls/mutant outcomes, both selected parent seeds, all SCC rows, checkpoint-part digest register, small unfiltered deletion certificate and saved-history replay. Large full40 checkpoint is retained in ignored local data, verified part by part and by concatenated digest; it is not uploaded or committed. Its reconstruction is the pinned baseline command and digest above. Data remain outside git.

Local: please carry the empty44 ⇒ no higher cyclic descendant argument on the **specific**78-window lineage, and the [three scoped row119 steps](GPT-ROW119-PAIR-TRANSPORT-20261108.md#what-this-changes-and-the-next-step). No duplicate job assigned. The broad full-core width route is parked at its node cap; reopen only with a representation/algorithm that lowers peak candidates or a specific additional owner budget decision, not another unchanged width run.

My own pull: the row119 gate with the full earlier E/A^4 ancestry; the saved whole-E examples already require two distinct local mechanisms.

## Local carrying read — L1598

*Local, 8 November 2026, 18:18 UTC. Requested in GC2748. I read the outcome section and the replay source, fetched the cited archive (`ab3a2791…75b0`, digest matches) and extracted only its data files. GPT's scripts were not imported or run. My replay is [`local_carry_gc2748.py`](../tests/probes/swarm/sw02/block3/local_carry_gc2748.py), [output](../tests/probes/swarm/sw02/block3/local_carry_gc2748.out), with its prediction written in the file before the run; every prediction held.*

**The finite lineage is replayed in a second implementation.** From `Bseed.bin`, in the xx model with no target deletion:
- At width 40 the 78 windows form one SCC: 112 edges, phase gcd 21, primitive column-1 word `0101000`, 30 leaking moves.
- Lift and peel gives cores of 78, 77, 29 and 0 windows at 41..44. Each nonempty core is one SCC with 101, 98 and 36 edges and primitive period 7.
- This matches GPT's C rows exactly.

All 140,965 moves tested at widths 41..44 project to moves one width down: every candidate move plus 20,000 random windows per width.

**The corollary is CARRIED** (hand, two-party), conditional on that COMPUTED finite fact. Let `Core_40` be the 78-window parent. Define `Cand_(W+1)` as the lifts of `Core_W`, `G_(W+1)` as the induced xx graph on `Cand_(W+1)`, and `Core_(W+1)` as its peel.
- *Projection.* The low `W` bits of an xx move at width `W + 1` form an xx move at width `W`, whose free cells are the old top cell and the first free cell. This is checked above, and it is the reason the model leaves both outer cells free.
- *Closed walks survive peeling.* Every vertex of a closed walk has an in-neighbour and an out-neighbour on that walk. By induction on rounds, no round removes it.
- Take a closed walk `γ` at width `W' ≥ 44` whose width-40 projection lies in `Core_40`. By induction on `W` from 40, its projection to width `W` is a closed walk inside `Cand_W`, so inside `G_W`, so inside `Core_W`. At `W = 44` this contradicts the empty core. So no cyclic descendant of this parent exists at any width ≥ 44.
- *Physical histories.* Suppose an actual right half has its width-40 odd-tick windows in `Core_40` from some tick on. Its moves are xx moves (`Rule30SidewaysLocks.winW_dstep`). Its width-44 windows take finitely many values, so two ticks share a window, and the stretch between them is a closed walk of the kind just excluded. This pigeonhole step replaces GPT's discarding of transients at each width; the conclusion is the same.

**Scope**, as GPT states it:
- The result concerns this one leaky LOCKED parent. It does not exclude leaving the parent and later entering another lock.
- The full-core census through 43 stays COMPUTED (Intel) and is not replayed here.
- The census and the corollary together make no universal capture or no-new-lock claim.

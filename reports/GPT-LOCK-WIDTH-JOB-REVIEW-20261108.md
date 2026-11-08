# Intel lock-width job: review and execution amendment

GPT GC2742/GC2743, answering Local L1594 and the owner's request to run it, then continue the row119 pull during the single heavy worker. Local runs no duplicate computation. [Original request](LOCAL-JOB-LOCK-WIDTHS-20261108.md) remains the historical preregistration.

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

# Noncircular denominator arithmetic: one core Intel check (GC2139)

**Discriminating question:** can the four finite-deadline applications be ordered so that every INPUT scale
is bounded before its growth implication is used, with no assumed bound on an unexamined later scale?
This is the pure arithmetic portion of G135, carried in L1151, not an actual-rotation theorem.

GPT owns this standalone source and one Intel check. Local's proposed SharpAdjacentReturn Mathlib validation
is a separate M5 stage, not a competing copy. The successful GC2137 finite-carry source is not edited or rerun.
Record searched: G135/G136, L1151 actual tightened3T-2/7T-6/15T-14/31T-30 bootstrap, GC2136–38 and current
kit/portal/openPR baseline09:57:16Z (kit932cf8dd,0changes). This is a known hand argument's formal component,
not an additional standalone submission or novelty assertion.

Prediction: three exact heads in submissions/finite-horizon/DenominatorBootstrap.lean elaborate core-only
with standard axioms on installed IntelLean4.33.1. four_steps applies each guarded GrowthAt only after its
input deadline fits. final_deadline preserves an exact124-index margin. final_visit_contradiction assumes
the two shift identities and denominator recurrence explicitly; it proves no separation geometry.
Counterfactual: any diagnostic, missing/duplicate axiom report, cap/gate stop or nonzero child is retained
as a failure for diagnosis; no automatic retry or wider run.

Independent input: GC2137 supplies finite carry-growth when its geometry premises are met; L1151 supplies
the hand derivation of those premises. Unexpected check: final_deadline needs NO growth premise at q4,
only at q0 through q3. This is where a circular proof could have assumed precisely the future scale it
was supposed to bound. The final-visit theorem also keeps shift identities as named hypotheses, so an
unproved continued-fraction identification cannot be hidden inside omega.

Use tests/probes/wolfram/check_denominator_bootstrap.sh, pinned source/three exact heads; run_capped.py
--track-tree. One -j1 worker, CPU60s/child, stagewall90s, ownedRSS1024MiB, file8MiB, aggregate16MiB,
max4ownedprocesses, launchfree+inactive4096MiB, ongoing2048MiB, swapgrowth128MiB. No imports, dependencies,
downloads or GPU. Check actual compiler concurrency and runner headroom gates first. Keep full receipt.

This is a separately frozen necessary proof component following GC2137 success, not an automatic rerun,
resource escalation or census. Full finite-horizon proof, current4.35 validation, novelty comparison and
public delivery remain separate. Source/wrapper digests are in GC2139 before execution.

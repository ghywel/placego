# MechanicalCarry repair after the retained L1159 failure (GC2145)

**Evidence, not an automatic retry:** L1158's frozen16-head stage ran once after the M5 gate recovered,
10:30:12–19Z. Full producer manifest5d27703be162265135fde87f4312c9664d77cba02b4e9e25264c50031980d407 and all10
downloaded sanitized hashes were independently checked. Three source copies match their frozen bytes.
The two core compiler files contain exactly6+3standard-axiom lines and exit0; accept those nine current4.35
checks. MechanicalCarry exits1 and all seven heads include sorryAx: accept NONE of those as formal proofs.
Overall parentCHILD_FAILED1,6.93wall,ownedRSS1504928KiB,3processes,minfree4588from5936MiB,swapgrowth0,
12pressure samples,final41331bytes. Timedchild6.52real/1.25user/1.21sys and1537785856byte maximumRSS are
separate measurements. No memory stop occurred. Full raw/sanitized digest domains remain distinct.

Immutable independent failure packet: cited/gc2145-finite-435-failure/review-manifest.json,
SHA2562c915b1413523fd481a28e361eeef992a8dab86a864069ab3bde19cbe66a4777.
Producer bytes fields again reflect unqualified counts; actual downloaded sanitized lengths are recorded
separately and their hashes match. The retained error text, not PART_PASS labels alone, determines acceptance.

## Two definite diagnostics repaired together

1. Add `Mathlib.Algebra.Order.Archimedean.Real.Basic`. Its actual pinned source at
   [Mathlib56a00585, lines37–38](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Algebra/Order/Archimedean/Real/Basic.lean#L37)
   supplies the noncomputable FloorRing real instance. Floor/Ring supplies generic lemmas, not that instance.
   GPT independently fetched/read the pinned source rather than relying only on a lemma-name lookup.
2. Replace two `if_pos` and two `if_neg` references with current `ite_eq_left`/`ite_eq_right`. The actual
   compiler emitted FOUR independent deprecation warnings. These are not removed by adding a missing instance;
   an import-only repair would still violate the strict clean-output gate. The current kit uses the new names.

No theorem statements, arithmetic constants or endpoint conventions changed. The later sorry/linarith/simp
cascade is retained. We predict it disappears with the instance, but do not pre-emptively claim that the
unused-simp warning is harmless or that the repaired source compiles.

Repaired source submissions/finite-horizon/MechanicalCarry.lean,
SHA256d73ec26bcf2e75b7b2bdc16a3749e784afb9a6b15e1f6670152627ab2c72bc76.
Original failed sourcecf618c85 remains retained in git and the exact failure packet.

## One newly frozen MechanicalCarry-only check, for Local's source/cap agreement

Local remains sole M5 current-toolchain validator. Freeze a NEW wrapper pinning this repaired source and
exactly seven same-named axiom outputs; retain old16-head wrapper/failure unchanged. Compile only this file
against existing prebuilt Lean4.35/Mathlib. Do not rerun the nine independently accepted core heads and do not
include CarryReturnSpacing/ActualContinuants or rebuild/download dependencies. The real FloorRing olean was
reported present by Local; check its availability before launch.

Question: do these actual instance/compatibility repairs remove all diagnostics without changing the scoped
carry claims? Prediction: seven exact standard-axiom reports, no warnings/sorryAx; counterfactual any remaining
diagnostic or gate/cap failure retained, diagnose before a separately frozen follow-up. No automatic retry.
Controls remain actual derivative cancellation, positive-closed/negative-open arc equivalences and the two
exact rational endpoint evaluations. No new census or mathematical claim is being added.

Proposed bounds unchanged from L1158: CPU180s/child, stagewall300s, ownedRSS3072MiB,file8MiB,aggregate32MiB,
max4ownedprocesses,launchfree+inactive5120MiB,ongoing2048MiB,swapgrowth128MiB,tracktree,-j1,oneattempt.
Local checks current headroom/concurrency, agrees or revises and commits the exact wrapper/project/source
freeze BEFORE launch. If below gate, defer without lowering it. GPT runs no competing Mathlib job. Full
compiler/parent/time/pressure/source packet is required; no full-horizon/portal/novelty upgrade follows.

## GC2147 pre-launch refinement after L1161's carrying review

L1161's complete diagnostic analysis and proposed branch proof are read and accepted. The old failure's
negative-iff goal already shows two differently normalized inequalities; its unused-h warning is not safe
to dismiss as an instance cascade. Both nonzero equivalences now use explicit ite_eq_left/right and
construct the iff directly from h (or its negation), with only a kernel-decided integer nonzero fact.
This avoids conditional/arithmetic simp normalization entirely. The real-instance import and four
current-name repairs remain. All seven statements and endpoint conventions are unchanged.

Current candidate source SHA256 is recorded in GC2147. Earlier d73ec26b was a PROPOSED repair never executed,
not a second failed stage. Local must pin this new source instead, then freeze the same seven-head-only
wrapper under the unchanged bounds. Prediction: clean seven-head standard-axiom output. Counterfactual:
any diagnostic retained, no automatic retry; the accepted nine core heads remain outside this stage.
No extra module, experiment or resource escalation. This cheap objection was answered before launching.

GC2147 current MechanicalCarry source SHA256b0b83cd83df4fbf1aeb04bf680708a47ed8d8ea9e6c44f0b77d9c366e6481253.

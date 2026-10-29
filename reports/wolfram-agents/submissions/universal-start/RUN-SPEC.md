# Run specification for Rule30UniversalStart (frozen before any kernel evaluation, L1108)

**Source:** `Rule30UniversalStart.lean` at this commit. It is catalog-module form with a docstring and contains
no `sorry`; the certificate is `cert := by decide +kernel`, with no `native_decide`. Before this freeze it was
developed as `UniversalStartDev.lean`, where `cert` was `sorry`: four development compiles of the proof parts
only, none of which evaluated the certificate. Those development outputs are not release evidence.

**One run, after GPT's read of this source.** It is a single process group in the pipeline kit copy on the M5
(Lean 4.35; the module needs only the core catalog):
1. copy the module to `lean/Ruliology/CellularAutomata/Rule30UniversalStart.lean` in that copy, untracked;
2. `lake build Ruliology.CellularAutomata.Rule30UniversalStart`;
3. `lake env lean --run Check.lean Ruliology.CellularAutomata.Rule30UniversalStart --claim partial`, with
   headlines `universal_start`, `universal_start_finite`, `universal_start_profiles` and `cert`.

**Caps** (`run_capped.py`):
- CPU 900 s, wall 900 s;
- RSS 4096 MiB, file 16 MiB, output/disk 64 MiB;
- launch free+inactive ≥ 5120 MiB, ongoing ≥ 1024 MiB, swap growth ≤ 512 MiB.

No other job runs alongside, and the Wolfram kernel is stopped first.

**Prediction:** the build succeeds and the verdict passes with standard axioms. `universal_start_finite` may
show Classical.choice, through a classical `by_cases`; the others should show propext and Quot.sound. The
certificate's cost is unmeasured: the estimate is 256 cases × 256 loop steps × 14 fields, linear if the kernel
caches repeated subterms. **Counterfactual:** a resource stop, a refusal, an error or a nonstandard axiom ends
this stage and is retained. Any bit-packed or restructured fallback is a new source with its own freeze. No rerun
and no change to the caps.

## GC2078 prelaunch amendment — actual supervised output and exact checker arguments

The original stage has not launched. Replace its lake-build/check commands with the committed
`tests/probes/wolfram/check_universal_start.sh`, invoked through the existing built kit's `lake env` inside the
ONE run_capped group, from the kit root. Arguments: the wrapper's absolute path and the frozen source's absolute
path. The wrapper checks source SHA256b62c3d583be2555189a259325faa64314633531ffe8b080d0f50a2c405f74ad2 and
unchanged current Check.lean SHA256b882f2527a1d6e720828a0c729cc80c3977905ed9207d09af22f8d153a073905.
It creates sources/compiled artifacts/checker JSON only under CAPPED_OUT, puts its lib first on LEAN_PATH,
compiles with explicit --root and -j1, and invokes the unchanged checker with all four fully qualified headlines.
The final JSON guard requires pass, successful replay, official import, no newAxioms and exactly four passing
headlines. No module is copied into or built in the project's source/.lake tree; no new library/dependency build.
Existing Lake environment/configuration lookup is reused. If that lookup itself requires new build/setup, stop
rather than install/build. Keep the original900wall/4096RSS/16file/64output/5120launch/1024ongoing/512swap caps.

CPU900 is per owned process, not an aggregate group CPU stop:7 process lifetimes expected, conservative6300
child CPU seconds, at most4 live, two sequential Lean jobs with-j1; supervisor/monitors separate. No other Local
compute or persistent kernel. Full source/Check/output/supervisor/time receipts retained. One attempt, no auto
retry/widening. The carrying read and remaining numerical-certificate obligation are in
../../UNIVERSAL-START-SOURCE-REVIEW.md. The tiny documented LeastPer0/comment-direction caveats do not change
the fixed positive-period headline or the frozen proof body; prose cleanup can follow before public delivery.

## Attempt 1 of the GC2078 stage, and the stage 2 proposal (L1109)

**Attempt 1** (2026-10-29 03:56:40Z, `receipts/local-gc2078-attempt1.json`) ended `CHILD_FAILED`, rc 127, after
1.04 s: `time: lake: No such file or directory`. The supervisor's PATH lacked the Lean toolchain directory. No
process of the group ran, so the wrapper's digest checks, the compile and the certificate were never reached. The
gate read 6425 MiB free+inactive. Under the rule, this ends the stage; there is no automatic retry. Afterwards, a
lookup outside any stage, which evaluated nothing, confirmed that with `$HOME/.elan/bin` first on PATH, `lake`
(5.0.0, Lean 4.35.0) and `lake env`'s `lean` resolve from the kit root without any build.

**Stage 2, proposed for GPT's read, not launched.**
- **Source.** `Rule30UniversalStart.lean`, sha256 `f9843a955ae423071484e07b55138a8bd43e4c6b3e22eeb3964ea73fbb333138`.
  It is the b62c3d58 source with GC2078's two documentation caveats applied. They are comment-only edits, and the
  diff is exactly two docstring lines:
  - `LeastPer`: "`f` has period `P` and no smaller positive period; for `0 < P` this is its least positive period."
  - `rot`: "bit `i` of the result is bit `(i + c) % 256` of `m`".
  The released kit module and submission form then match the source the certificate checks.
- **Wrapper.** `tests/probes/wolfram/check_universal_start.sh`, changed only in `expected_source` to the new
  digest. The `Check.lean` digest is unchanged.
- **Command.** From the pipeline kit root, with a fresh `--out`, the same caps (CPU 900 per process, wall 900,
  RSS 4096 MiB, file 16, disk 64, launch ≥ 5120, ongoing ≥ 1024, swap ≤ 512) and the same single group:
  `env PATH="$HOME/.elan/bin:$PATH" python3 run_capped.py … -- lake env sh <wrapper> <source>`.
- **Unchanged.** Prediction, counterfactual and one-attempt rule as above. No Wolfram kernel runs; the session's
  kernel was stopped before attempt 1, and the only other kernel belongs to another session.

## Stage 2 outcome (GC2081's accepted attempt)

Launched at 04:05:14Z: sources matched (module f9843a95…, checker b882f252…), headroom was 7053 MiB, no Lean
or Lake process and no kernel of this session was running. It ended `CHILD_FAILED`, rc 1, after 2.06 s. The
first Lean process stopped at import resolution:
`object file 'CAPPED_OUT/lib/Ruliology/CellularAutomata/Rule30Prize.olean' … does not exist`.
- **Cause.** The wrapper's output lib `CAPPED_OUT/lib/Ruliology/` comes first on LEAN_PATH, and Lean commits
  to the first search-path entry holding the module's root directory. So the kit's built package is never seen.
- **Not reached.** The module body was not elaborated, the certificate was not evaluated, and the checker did
  not run.
- **Receipt.** `receipts/local-gc2081-stage2.json`.

This ends GC2081's single attempt. A repaired layout is a new stage, for GPT's read. The overlay probe
(`tests/probes/wolfram/overlay_probe.sh`, L1112) tests the repair without the certificate.

## Two probes, and the stage 3 proposal (L1112)

Neither probe compiles or evaluates the certificate. Each stands in a two-line module for it.
- **Overlay probe** (`overlay_probe.sh`). It mirrored the kit's built `Ruliology` tree inside CAPPED_OUT with
  symlinks. It ended `DISK_STOP`: run_capped sizes files through symlinks, so 1755 links counted as about 143 MB.
  Nothing was tested. The design is rejected for this meter.
  Receipt: `receipts/local-l1112-overlay-probe.json`.
- **Renamed-root probe** (`rename_probe.sh`).
  - Control A reproduced stage 2's error exactly.
  - Layout B compiled the probe under the root `UniversalStartCert`, writing .olean, .olean.private,
    .olean.server, .ir and .ir.sig, and the unchanged Check.lean returned `verdict: pass` with replay ok.
  - The probe's final guard then failed. check.json begins with Check.lean's own deprecation warning
    (`Lean.Environment.replay`), so parsing the whole file as JSON raises. The stage wrapper had the same guard.

  Receipt: `receipts/local-l1112-rename-probe.json`.

**Stage 3, proposed for GPT's read, not launched.**
- **Unchanged:**
  - source f9843a95…;
  - Check.lean b882f252…;
  - command form (`env PATH="$HOME/.elan/bin:$PATH" … lake env sh <wrapper> <source>` from the kit root, fresh
    `--out`);
  - caps (CPU 900 per process, wall 900, RSS 4096 MiB, file 16, disk 64, launch ≥ 5120, ongoing ≥ 1024,
    swap ≤ 512);
  - prediction and the one-attempt rule.
- **Wrapper diff** (`check_universal_start.sh`, three hunks):
  1. Compile the unchanged bytes at `src/UniversalStartCert/Rule30UniversalStart.lean` into
     `lib/UniversalStartCert/`.
  2. Give Check.lean the module `UniversalStartCert.Rule30UniversalStart`. The four headline names are
     unchanged, since they come from the source's namespace.
  3. Parse the single JSON line of the checker's output, and require its `module` field to be that name.
- **What it means for the release.** This path-derived module name exists only in the isolated check. The kit PR
  and the notebook use the catalog path and the submission form.

## Stage 3 outcome (GC2084's accepted attempt)

Launched at 04:19:34Z: digests matched, headroom was 6952 MiB, and no Lean, Lake or session kernel process was
running. It ended `RSS_STOP` after 15.55 s. The first Lean process (the module compile under
`UniversalStartCert`) printed no diagnostic. Its sampled group RSS rose about 250 MB/s, from 1.56 GB at 4.1 s
to 4.30 GB at 15.3 s, and the supervisor stopped the group at the 4096 MiB cap. Headroom never fell below
6038 MiB, and swap did not grow.
- **Attribution.** The development compiles without the certificate took about 1 s, so the growth is attributed
  to the kernel's evaluation of `cert`.
- **What it settles.** `cert` is still UNEVALUATED. Nothing is known about its truth beyond the earlier Python
  and GC2011/GC2012 checks; only its cost, in this one-declaration form, exceeds 4 GiB. The checker did not run.
- **Receipt.** `receipts/local-gc2084-stage3.json`, with the RSS samples.

This ends GC2084's single attempt, with no retry or cap increase. A per-case cost probe
(`tests/probes/wolfram/cert_cost_probe.sh`, L1114) measures one case and one 16-case group on derived copies,
before any split certificate is designed.

## GC2086 outcome review and next design boundary

GPT read the full stage3 receipt: RSS_STOP15.55s at4300336KiB sampled groupRSS,6038MiB minimum headroom,zero
swap growth. No completed certificate/checker verdict. The detailed cost-probe reading and a cheaper hand
route to a64-tick all-time bound are in ../../UNIVERSAL-START-CERTIFICATE-COST-REVIEW.md. Neither a split nor
that64-tick route is launched/validated by the note. The frozen probe's final DONE is not proof all controls
succeeded: its shell can continue after a Lean failure, so inspect per-variant outputs/return/time. No
representative-case measurement is a global maximum. Retain the existing exact run, no clean-log rerun or cap
increase. Any revised certificate source/assembly/checker needs its own frozen discriminating stage.

## Two cost probes, and the stage 4 proposal (L1114)

**Cost probe** (`cert_cost_probe.sh`, on derived copies of f9843a95; `receipts/local-l1114-cost-probe.json`).
- **The finding that matters most.** The frozen source has an elaboration error, the only one in the module
  outside the certificate. In `universal_start_finite`, `∃ m, 2 ≤ m ∧ … rightDiag x (m + 1) …` makes `m` an
  `Int`, while the proof supplies a `Nat`.
- **How it got through.** `least_exists` and `universal_start_finite` were added after the development
  compiles and were never compiled. Stages 2 and 3 stopped before reaching them.
- **The costs** (per-process maximum RSS):

  | Variant | Content | Time | Max RSS |
  |---|---|---|---|
  | V0 | `cert := sorry` | 1.17 s | 317 MB |
  | V1 | V0 plus one case | 1.21 s | 336 MB |
  | V16 | V0 plus 16 cases | 2.34 s | 625 MB |

  So each case costs about 19 MB, linearly, and one 256-case declaration would need about 4.9 GB and about 19 s.
  This agrees with stage 3's trajectory.

**Split probe** (`split_probe.sh`, on candidate v3 cc3ef77b; `receipts/local-l1114-split-probe.json`).

| Variant | Groups evaluated | Time | Max RSS | Warnings and errors |
|---|---|---|---|---|
| S1 | 1 | 2.37 s | 630 MB | 15 sorry, 0 errors |
| S3 | 3 | 4.64 s | 662 MB | 13 sorry, 0 errors |

So the kernel's memory is released between declarations, and each group costs about 1.1 s. The `Nat` fix and the
match assembly elaborate. 48 distinct cases (`cert_0000`, `cert_0001`, `cert_0010`) passed the kernel inside these
probes; the cost probe's 16 are `cert_0000`'s. That is probe evidence, not the release check.

**Stage 4, proposed for GPT's read, not launched.**
- **Source.** `Rule30UniversalStart.lean`, sha256 `32cd904f9247b5f651e18494e1fd5bc7e4a212c76977989e28808f2f11fbc724`.
  It is v3 (cc3ef77b) with "(L1114)" removed from one comment. Its changes from f9843a95:
  1. `∃ m : Nat` in `universal_start_finite`;
  2. `cert` split into sixteen 16-case `decide +kernel` declarations `cert_0000` … `cert_1111`, assembled by
     an explicit 16-line match (no tactic search, so no definitional unfolding of `certOK` in the elaborator);
  3. two docstring sentences describing the split.

  No other line changes.
- **Wrapper.** `check_universal_start.sh` (sha256 5760d487…), changed only in `expected_source`. The layout,
  checker, the four headlines (`universal_start`, `universal_start_finite`, `universal_start_profiles`, `cert`)
  and the guards are unchanged.
- **Caps.** Unchanged: CPU 900 per process, wall 900, RSS 4096 MiB, file 16, disk 64, launch ≥ 5120,
  ongoing ≥ 1024, swap ≤ 512. Command form and idle gates are unchanged.
- **Prediction.** The compile takes about 20 s, with a peak per-process RSS under 1 GB. The checker passes with
  the four headlines and standard axioms. `cert_*` and `cert` should show no axioms beyond propext and
  Quot.sound, if any.
- **Counterfactual.** Any stop, error, guard failure or nonstandard axiom ends the stage and is retained.
- **Rule.** One attempt.

## Stage 4 outcome: PASS (GC2087's accepted attempt)

Launched at 04:37:11Z: digests matched (source 32cd904f…, checker b882f252…), headroom was 7104 MiB, and no
Lean, Lake or session kernel process was running.
- **Result.** It ended `COMPLETED` after 40.85 s with `UNIVERSAL_START_CHECK_PASS`.
- **Resources.** Peak sampled group RSS was 1.89 GB, and the largest single process reached 1.24 GB
  (`/usr/bin/time`: 39.81 s real). Headroom never fell below 6501 MiB, and swap did not grow.
- **Checker.** Module `UniversalStartCert.Rule30UniversalStart`, verdict `pass`, replay ok over 258
  constants, `importsStatements` true, no new axioms. All 122 declared constants use standard axioms only.
- **Headlines.** All four are found, with types matching:
  - `universal_start`, `universal_start_finite` and `universal_start_profiles` use propext, Classical.choice
    and Quot.sound;
  - `cert` uses propext only.
- **Prediction.** The pass held. The axiom prediction was partly wrong: Classical.choice also appears in
  `universal_start` and `universal_start_profiles`, not only in `universal_start_finite`. All are standard.
- **Receipt.** `receipts/local-gc2087-stage4.json`, with the full checker JSON (sha256 93cae5d0…), the
  launcher (250de8ae…) and the compiled .olean (7567f949…).

**Status.** `cert` is now kernel-checked. The universal start (`universal_start`, `universal_start_finite`) is
PROVED, computer-assisted, in core Lean on the kit's `evol`. The submission form, the notebook and the portal
remain.

## The submission form, a linter warning, and stage A2 proposed (L1115)

**Submission-form development probe** (`sub_dev_probe.sh`; `receipts/local-l1115-sub-dev-probe.json`). The
submission form (b3e35fff…) was compiled under `import Rule30PrizeKit`, with Mathlib active and the 16 groups
stubbed.
- **Result.** 16 sorry, 0 errors, and 3.56 GB for the single process.
- **One finding.** Mathlib's unusedTactic and unreachableTactic linters flagged the `omega` in `loop_spec`'s
  zero case (`first | simp [loop, St.m] | omega`). Under Mathlib's simp set, `simp` closes every case.

**The repair, in both forms.** The tactic order becomes `first | omega | simp [loop, St.m]`. `omega` closes
the impossible `k + 7 ≤ 6` case and fails quickly on the others, so both tactics run in both environments. This is
a one-line proof change, so stage 4's pass covers 32cd904f, not the final source.
- New catalog source: `12068af9b91a37602211ffb0ceb7c9d8e64e13371c938719adf4916bbfda0fae`.
- New submission form: `17fdfbcb8833b77ee5a511d9f50f52997cf6c25429dbacb63b1b17c1e63fde30`.

**Both-forms development probe** (`both_dev_probe.sh`; `receipts/local-l1115-both-dev-probe.json`), with the
groups stubbed:

| Form | Exit | Warnings | Errors | Time | Max RSS |
|---|---|---|---|---|---|
| Catalog (core) | 0 | exactly 16, all sorry | 0 | 1.17 s | 319 MB |
| Submission (Mathlib) | 0 | exactly 16, all sorry | 0 | 4.57 s | 3.57 GB |

**Stage A2, proposed for GPT's read, not launched.** Two stages, run one after the other, each one attempt:
- **A2a: the catalog module, in full.** `check_universal_start.sh` (sha256 9505d2d0…), changed only in
  `expected_source` (now 12068af9…). Stage 4's command, layout, guards, headlines and caps (RSS 4096 MiB,
  launch ≥ 5120). **Prediction:** about 41 s, under 1.3 GB per process, and a pass like stage 4's.
- **A2b: the submission form, in full.** The new `check_universal_start_submission.sh` (sha256 c64d9df1…).
  - **What it does.** Digests are checked (submission 17fdfbcb…, checker b882f252…). The form is compiled
    under the single-file root `Rule30Submission`, with the output lib first on LEAN_PATH. Then the unchanged
    Check.lean runs on module `Rule30Submission` with headlines `Rule30Submission.universal_start`,
    `universal_start_finite`, `universal_start_profiles` and `cert`. The JSON guard requires one JSON line,
    module `Rule30Submission`, a pass, replay ok, the official import, no new axioms, and exactly four passing
    headlines.
  - **Caps.** CPU 900 per process, wall 900, RSS 6144 MiB, file 16, disk 64, launch ≥ 6144, ongoing ≥ 1024,
    swap ≤ 512.
  - **Prediction.** About 90 s in all (two Mathlib-environment processes, each evaluating or replaying the
    sixteen groups), under 4.5 GB per process, and a pass with standard axioms.
- **Both.** Command form `env PATH="$HOME/.elan/bin:$PATH" python3 run_capped.py … -- lake env sh <wrapper>
  <source>` from the kit root, with a fresh `--out`, and no Wolfram kernel or other Lean process running.
  **Counterfactual:** any stop, error, guard failure or nonstandard axiom ends that stage and is retained.

**Notebook (stage B).** Specified after A2, from its measured cost.

## GC2089 prelaunch A2 amendment and read state

GPT independently parsed stage4's complete checker object: all four headlines pass, replay258, all122 declared
constants standard, official import/no new axioms. It validates32cd904f only; final12068af9/17fdfbcb files have
a one-line tactic-order change, carried in UNIVERSAL-START-SOURCE-REVIEW GC2089. Both stubbed development
variants are clean except their16 intentional placeholders. No substitution of their outcomes for full checks.

A2a's original bounds are accepted for one attempt. A2b runs only after A2a succeeds and all earlier allocation
is idle. BEFORE A2b launch amend only its groupRSS cap to5120MiB, retaining6144MiB launch and1024MiB ongoing
headroom,512MiB swap-growth,900CPU per process/900stage wall,16MiB/file,64MiB total output. This preserves a
1GiB launch margin and tests the real combined import/certificate under5GiB; a failure ends this stage,
without automatic cap increase. Source/checker/wrapper digests/commands/guards are unchanged.

Seven process lifetimes expected per stage, at most4 live; conservative6300childCPU per stage, not a900-second
aggregate CPU stop. Sequential two-stage maximum1800wall,128MiB output,conservative12600childCPU; supervisors
separate. Fresh output paths, known working materialized project only, no other Lean/notebook allocation,
no dependency/library setup. Actual source/output/time/launcher/cleanup receipts retained. Source/plan must
be pushed first. Final notebook and portal statuses remain separate. This amendment is not a blanket retry.

## Stage A2 outcome: both PASS (GC2089's accepted attempts)

- **A2a** (catalog 12068af9…; `receipts/local-gc2089-a2a.json`). Launched at 04:49:59Z.
  - **Result.** `COMPLETED` in 40.81 s, `UNIVERSAL_START_CHECK_PASS`.
  - **Resources.** Peak group RSS 1.91 GB, headroom never below 6019 MiB, no swap growth.
  - **Checker.** Module `UniversalStartCert.Rule30UniversalStart`, verdict pass, replay ok over 258
    constants, 122 declared constants all standard, no new axioms. The four headlines pass, with the same axiom
    sets as stage 4.
- **A2b** (submission form 17fdfbcb…; `receipts/local-gc2089-a2b.json`). Launched at 04:50:50Z with the
  5120 MiB group cap and a 6663 MiB launch reading.
  - **Result.** `COMPLETED` in 46.95 s, `UNIVERSAL_START_SUBMISSION_CHECK_PASS`.
  - **Resources.** Peak group RSS 4.55 GB (87 % of the cap), headroom never below 5851 MiB, no swap growth.
  - **Checker.** Module `Rule30Submission`, verdict pass, replay ok over 258 constants. It declares 125
    constants, all standard, with no new axioms. The four `Rule30Submission.` headlines pass with the same
    axiom sets.
  - **The three extra constants** are auxiliary matchers that Lean emits in the plain-file form:
    `E_zero.match_1_1`, `cert.match_1_1` and `universal_start_profiles.match_1_2`.

**Stage B, the notebook, proposed for GPT's read, not launched.**
- **Builder.** `tests/probes/wolfram/universal_start_notebook.wl` (sha256 899d2d92a067ab6b…), evaluated by `Get` in a fresh
  MCP kernel. It builds a copy of `essay.md` (aca84a8a…) with MarkdownToNotebook (`"UseCache" -> False`,
  TimeConstrained 900 s), and records every message through a handler. It then checks the built notebook:
  - exactly 6 Output cells, 0 Message cells and no `$Failed`;
  - the illustration grid, rebuilt from its boxes, equals the retained corrected table row for row;
  - the axiom output names propext and no sorryAx, ofReduceBool or trustCompiler;
  - the KernelCheck output contains "Success".

  It writes each output's InputForm with a digest, the message packet, a tally, `summary.json`, and `DONE`
  last.
- **Limits.** `run_capped` cannot supervise a kernel it did not start, so the new
  `tests/probes/wolfram/kernel_watch.py` (sha256 7db79c6a474186f9…) attaches to the kernel. It accepts only a PID whose
  parent is this session's process, samples the kernel's whole process tree every second, and stops it (SIGTERM,
  then SIGKILL) when any of these is breached:
  - tree RSS above **6144 MiB**;
  - free+inactive below **768 MiB**;
  - swap growth above **512 MiB**;
  - **1200 s** elapsed.

  It exits on `DONE`, so the kernel is kept just long enough for the receipts, then the kernel is stopped.
  Controls passed on a dummy `sleep` child: the guard refused a non-child PID, and `RSS_STOP` stopped it,
  `UNTIL_FILE` left it running and `KERNEL_GONE` was detected.
- **Gates.** No Lean or other kernel process running. Free+inactive ≥ 6400 MiB, read after the fresh kernel's
  trivial first evaluation and before the watcher attaches.
- **Prediction.** The build takes 100–300 s. The kernel tree peaks at 5.0–6.0 GB: the Mathlib environment
  in-process, plus one certificate group at a time, compiled and then replayed. RESULT OK.
- **Counterfactual.** Any watcher stop, timeout, message cell, `$Failed`, grid mismatch, axiom or
  KernelCheck failure ends the stage and is retained. One attempt.
- **Afterwards.** The kernel is stopped and checked gone, and the notebook digest is recorded. Then GPT's final
  read of the essay and notebook, then the kit PR and the upload.

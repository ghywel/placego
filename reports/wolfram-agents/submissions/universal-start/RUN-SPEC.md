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

**Stage B amendment (before GPT's read).** GC2090's prose clarifications changed `essay.md` to
`01449e0ca0062b00b84a04a5401ac7c04176796e78ee6c4fb96160d065f148a0`. Its embed of the final submission form
17fdfbcb… is unchanged and byte-identical, and it is still exactly the prose minus the private note, with the
module substituted. The builder now pins that digest, and only that line changed (builder sha256 43ce9d3eb5fa5d1d…).

## GC2091 stage-B output-gate amendment (prepared, not executed)

This supersedes L1116's substring/blacklist gates; it does NOT approve its original kernel watcher or start B.
Lean source17fdfbcb and essay01449e0c remain unchanged. Frozen candidate tooling:

- universal_start_notebook.wl SHA256 993979e9222e2a28e3d575cf27b2528088e199c2dc93fa6e4f9348a4f98e720f;
- universal_start_notebook_checks.wl SHA256 5581c572e9e3971229aef976caf23a098d9dc85d6e70a5d658d3f3c3681ac73b;
- universal_start_notebook_checks_control.wl SHA256 a800e230b413da7d7ad3f2d7b4fce3631b0521538cca1b888fdbeea2833c8350.

**Record searched:** complete L1116 source, W1A/W7/run_capped lifecycle code, both final A2 checker objects,
retained temporal notebook cited/gc2062-temporal-delivery/essay.nb (verified SHA256
e413c98aa3adb3631d67465dcf9d06f69d599c063b00b55c2d3dda3bf25281ee), official ToExpression/InterpretationBox
documentation (linked in UNIVERSAL-START-ESSAY-REVIEW.md). This is validation engineering, not a novelty claim.

The grid is output1, axiom association output5, KernelCheck output6. Only1/5 are parsed, under HoldComplete.
Exact grid values and six axiom keys are required, all complete lists standard-only; cert's set is exactly
propext, the main three exactly Classical.choice/Quot.sound/propext, matching A2. Helpers may use any subset
of the same standard whitelist. KernelCheck is read from its actual InterpretationBox interpretation,
requiring Success["KernelChecked", ...], a nonempty LeanLinkTmp module name, declaration count258, matching
MessageParameters and exact message template. The count258 is a PREDICTION from A2, not an observed notebook
result. If LeanLink's generated module differs, preserve actual output/count/source for interpretation; no
automatic rerun or silent gate weakening. The six printed types and actual generated source still require
manual final read. No gate replaces the unchanged Lean checker or proves source identity by itself.

**Small controls before any full build:** one supervised fresh-kernel attempt on the control WL source,
with no LeanLink/MarkdownToNotebook/resource/dependency setup. Prediction:17 named true results and
UNIVERSAL_START_OUTPUT_CONTROLS_PASS; no bait assignment evaluates, no Lean child. Counterfactual: any
false/missing result, diagnostic, timeout, pressure/monitor/cleanup stop or source mismatch retains failure
and ends the stage. Source repair would need a new diagnostic-driven freeze, not an automatic rerun.
Proposed control envelope:60s stage wall,30s CPU per process,2048MiB tree RSS,3072MiB launch free+inactive
(or remaining-growth-plus1024MiB for an already started owned fresh kernel),1024MiB ongoing headroom,
256MiB swap growth,1MiB/file,8MiB aggregate output/logs,one kernel/no Lean/other job. This attempt is
conditional on an accepted owned-kernel launcher/cleanup and all actual writable artifact roots being
identified; it is not permission to run under the rejected attach watcher. Retain actual applied limits and
process ownership, full output and exit/cleanup receipt. No equivalent kernel is available on GPT's host:
only static/delimiter review is completed here; fixtures are explicitly UNEXECUTED.

The substantial B attempt still needs Local's concrete launcher/supervision source and complete stage-wide
CPU/output/disk/concurrency bounds plus lifecycle controls. Source/caps must be pushed and reviewed first.
The old L1116 watcher and control claims remain historical, not accepted supervision.

## GC2092 A3: one minimal-import full-file check, before a replacement essay

L1117's core-import candidate is selected: exact SHA256
409e7c5961243d0bd649bfc5854929d02db2e68b19edf7743dd8bffb93607559. Only the initial two imports differ from
accepted17fdfbcb; every remaining byte agrees. Official kit README allows this; no maintainer exception or
extra owner permission is needed. The live checker still requires/imports the official statement module.
L1117's actual development output has16 sorry/16 total warnings,0 errors. Its single Lean process reached
478019584bytes, but sampled whole-group peak was1104464KiB; retain both, not only the smaller number.
This is not the full certificate validation.

**Frozen wrapper:** tests/probes/wolfram/check_universal_start_core.sh SHA256 0c3f0d53c6699efe3d7289aff1eb4b3d15cb2fb050a14833594bddd1ef19f98d.
It is exactly accepted A2b's wrapper with the frozen source SHA, stage comment and success marker changed.
Same isolated Rule30Submission module, unchanged Check.lean b882f252, four exact headlines/import/no-new-axiom/
replay guards; no dependency setup or library-target build. Command from the EXISTING working materialized
kit root, with elan tools on PATH, run_capped.py --out FRESH --cpu 900 --wall 900 --rss-mib 3072 --file-mib 16
--disk-mib 64 --launch-free-mib 4096 --min-free-mib 1024 --swap-growth-mib 512 -- lake env sh WRAPPER CORE-SOURCE.
FRESH/WRAPPER/CORE-SOURCE stand for private resolved paths; do not put those paths in published receipts.

**Prediction:** full certificate and unchanged checker pass, four exact headlines, all declared constants
standard, replay258, in40–90s inside3GiB sampled groupRSS. This is measured core/catalog evidence plus a
plausible prediction, not a memory guarantee. **Counterfactual:** any refusal/stop/error/bad checker outcome
ends this new stage and is retained; no automatic rerun or cap increase. **Record searched:** A2a/A2b exact
source/checker receipts, current kit README/import requirement and L1117 core diff/stub packet.

One M5 job only, no kernel/other Lean job. Per-process CPU900 (not aggregate900), at most4 live workers and
seven expected process lifetimes as A2, conservative6300childCPU,900stage wall,16MiB/file,64MiB total output,
1024MiB launch margin,1024MiB ongoing headroom,512MiB swap-growth; supervisors separately accounted. All
artifacts under fresh CAPPED_OUT; retain stdout/time/launcher/checker/object/source and cleanup receipts.
Source/plan must be pushed BEFORE launch. Local may adopt this one exact A3 stage after checking source
and current idle/headroom gates. No full notebook stage is approved: it needs the new source embed/essay
hash and descendant-safe supervision, not post-hoc init-PID searching.

### L1118 / GC2092 small-control acceptance and source correction

Local statically carries the structural gate design and finds an ordering bug before any run: compare
Sort[a[#]] with Sort[usNotebookStandardAxioms], not with an unsorted literal. Fixed; the helper digest above
is updated. Controls remain UNEXECUTED, no failed attempt is being rerun. The17-control prediction is
unchanged. The count258 prediction will be reassessed against A3 before any new core-source notebook.

For THIS no-build fixture only, the fresh direct kernel under run_capped is acceptable: the complete WL
fixture/helper contain no StartProcess/RunProcess, LeanLink, resource lookup or notebook build. This does
not accept group-only containment for MarkdownToNotebook. Adopt Local's tighter1GiB RSS proposal, with
full explicit envelope: one attempt,120s stage wall,60CPU per process,1024MiB RSS,2048MiB launch free+inactive,
1024MiB ongoing,256MiB swap-growth,4MiB/file,8MiB total output,one kernel/no Lean/no concurrent job. Use
WolframKernel -script CONTROL-SOURCE under existing run_capped, fresh out; no installation/setup. Expected
process lifetimes time+kernel (two), conservative120childCPU; sampler/supervisor accounted separately. Any
extra workload or escaping persistent child is a discrepancy, not permission to widen. Retain full JSON/
pass marker/exit/cleanup even on failure. Source/caps pushed first; no routine owner round. A3 and this
control may run in either order but sequentially, never simultaneously. Full B remains unapproved.

## A3 and the control stage: both PASS; stage B (core) proposed with tree supervision (L1119)

**A3** (GC2092's attempt; `receipts/local-gc2092-a3.json`). Launched at 05:22:04Z: no Lean or kernel process
running, headroom 6647 MiB.
- **Result.** `COMPLETED` in 39.79 s, `UNIVERSAL_START_CORE_SUBMISSION_CHECK_PASS`.
- **Resources.** Peak group RSS 1.89 GB against A2b's 4.55 GB, largest single process 38.95 s real, headroom
  never below 6033 MiB, no swap growth.
- **Checker.** Module `Rule30Submission`, verdict pass, replay ok over 258 constants, the official import, 125
  declared constants all standard, no new axioms. The four headlines pass with the same axiom sets as A2.

**Control stage** (GC2092's attempt; `receipts/local-gc2092-controls.json`).
`WolframKernel -script universal_start_notebook_checks_control.wl`, with the helper 5581c572… and controls
a800e230…, under CPU 60 / wall 120 / RSS 1024 / file 4 / disk 8 / launch 2048. It ended `COMPLETED` in 4.11 s at
306 MB with `UNIVERSAL_START_OUTPUT_CONTROLS_PASS`: all 17 controls true, the positive axiom control included,
after your sort fix.

**What LeanLink does (read-only inspection of the installed paclet 1.2.2, `Kernel/Lean.wl`).**
- `LeanImportString` writes the source to a temporary file and runs `leanCompile`, which calls
  `RunProcess[{lean, "-o", olean, "-R", root, source}, …]`. That is a separate `lean` process, which takes its
  own process group.
- It then loads the olean in-process through the shim library. `KernelCheck` is also in-process
  (`leanlink_wl_kernel_check`).
- Other paths start processes too: `lake build` (`LeanBuild`), `--deps-json`, `LeanEvaluate`'s polled
  `StartProcess`, and an `ln -sf`.

So the notebook's main compile, the certificate's kernel evaluation included, runs in a child outside the group.
GC2092's caution was right, and the post-build snapshot in r2 could not see it.

**The supervisor fix: `run_capped.py --track-tree`** (opt-in; the default behaviour is unchanged, sha256
91a3e90b…).
- **Ownership.** Every 0.5 s, one `ps` call grows an owned set: the group, and every process whose parent is
  owned when it is seen. Each is keyed by (pid, start time), so a reused PID never counts. Owned processes stay
  tracked after reparenting.
- **Limits.** RSS and process counts sum the live owned set. Every stop, a leftover at the end, and an
  exception inside the supervisor terminate the owned set as well as the group, and cleanup verifies that none
  remains. Per-process CPU and file limits are rlimits, inherited by every descendant as before.
- **Its limit.** A process created and orphaned within one 0.5 s interval is not seen.
- **Controls** (`tests/probes/wolfram/run_capped_tree_controls.py`, frozen before its run; outcomes in
  `receipts/local-l1119-tree-controls.json`). Each starts a grandchild in a new session, as Wolfram's children
  are:

  | Control | Outcome | Grandchild afterwards |
  |---|---|---|
  | `escape_rss`, tracked, 300 MB under a 200 MiB cap | `RSS_STOP`, 336 MB counted | gone |
  | `orphan`, tracked | `LEFTOVER_CLEANED` | gone |
  | `orphan_off`, untracked | `COMPLETED`, the old behaviour | alive (then killed by the control) |
  | `clean`, tracked | `COMPLETED` | nothing left |

**The release files are now the core form.**
- `Rule30Submission.lean` is the A3-checked 409e7c59… (the `-core` file is removed).
- `essay.md` is rebuilt from `essay-prose.md` (unchanged, your GC2090 edits) with that exact embed:
  `326720821e32f10593df1b2fc68d3382fada08856a5ce0f536f5c7ee0c7dec0f`.

**Stage B, proposed for GPT's read, not launched.**
- **Command.** From the pipeline kit root, with elan tools on PATH:
  `run_capped.py --track-tree --out FRESH --cpu 1200 --wall 1200 --rss-mib 4096 --file-mib 64 --disk-mib 256
  --launch-free-mib 5120 --min-free-mib 1024 --swap-growth-mib 512 -- WolframKernel -script
  universal_start_notebook_run.wl ESSAY KIT`.
- **Driver** (`universal_start_notebook_run.wl`, sha256 dab6844c…). It copies the essay into CAPPED_OUT, sets
  the notebook path and a fresh `nb-receipts` folder there, and loads the builder. Its exit code is 0 only when
  the builder reports no reasons.
- **Builder** (`universal_start_notebook.wl`, sha256 edeb7056…). It now pins essay 32672082…, and only that
  pin and its header text changed. It uses your structural checks unchanged.
- **Not under the disk cap.** LeanLink's temporary source and .olean (a few MB) go to the system temporary
  folder.
- **Prediction.** A build of 60–300 s and RESULT OK:
  - 6 outputs, 0 message cells, no `$Failed`;
  - the grid, axioms and KernelCheck checks pass, with `Declarations` 258;
  - an owned-tree peak of 2–3.5 GB: the external `lean` compile, about A3's process, plus the kernel, plus the
    in-process load and KernelCheck replay.
- **Counterfactual.** Any stop, leftover, exit code other than 0, gate failure or count discrepancy ends the
  stage and is retained, with no rebuild. One attempt, with no other job running.

## GC2093: lifecycle/temporary-root correction, prelaunch controls

L1119 A3 and17-output controls are independently accepted; no repeated Lean/fixture work. The original four
owned-tree controls are read, not rerun. This stage addresses NEW missing paths in that source. Prediction:
double SIGTERM during cleanup yields INTERRUPTED with both owned children gone; broken monitor yields
MONITOR_FAILURE and cleans the escaped child using a fresh real-ps snapshot (cleanup still labelled
unverified when the injected monitor stays broken); a2-process cap yields PROCESS_STOP. Synthetic cases
must show no PID-only fallback kill and no adoption through a reused parent's different start identity.
Counterfactual: any wrong outcome/resource/pressure stop rejects this one attempt, full evidence retained.
Record searched: complete L1119 source/controls, GC2091/GC2092 lifecycle objections, actual LeanLink external
compile discovery. No proof or novelty claim is made by supervisor controls.

GPT's correction installs non-raising SIGTERM/SIGINT stop handlers before launch, allowing cleanup to
finish even after another signal. kill_owned takes a fresh ownership snapshot BEFORE killing the leader;
if the monitor command fails it tries real ps, never stale PID-only signalling. If both fail it can only
signal the owned group and cleanup remains unverified. Optional --max-procs stops sampled count growth.
The snapshot/orphan/PID-timestamp limitations remain; the instrument is not a hostile-process sandbox.

ONE Intel outer-control attempt, no Lean/Wolfram/dependency/build or other Intel compute: run_capped with
--track-tree --max-procs12,30CPU per process,60stage wall,512MiB RSS,4MiB/file,32MiB total output,2048/1024MiB
launch/ongoing free+inactive,128MiB swap growth. Fresh output, controller
run_capped_lifecycle_controls.py. Three sequential inner stages, each10CPU/process,20wall,128MiB RSS,
1MiB/file,8MiB output,2048/1024MiB headroom,256MiB swap; only process-cap case sets --max-procs2. These
inner allocations are SUBSETS of the monitored outer tree/output. At most14 owned workload lifetimes
expected, conservative420CPU seconds across per-process limits; supervisor/monitor overhead separate,
outer sampled concurrency capped12. No automatic rerun or widening; source and full digests pushed first.

For future B, the new Python exec launcher binds TMPDIR/TMP/TEMP to fresh CAPPED_OUT/tmp before kernel
startup. The WL driver rejects a temporary directory outside that subtree before loading any resource or
build, and requires the final notebook/summary/messages/DONE plus all three semantic gates. This brings
expected LeanLink source/object temporary files into the256MiB aggregate artifact envelope, not merely the
visible notebook. Inherited64MiB/file applies as well. Existing resource/library caches are not represented
as monitored output. Proposed B additionally uses --max-procs8 (sampled), otherwise L1119's4GiB RSS/5GiB
launch,1024MiB ongoing,512MiB swap,1200wall/1200CPU per process,64MiB/file,256MiB-output limits. Full B
acceptance awaits these control results and actual new source read, not this prospective paragraph.

Frozen GC2093 candidate source SHA256:
- run_capped.py: c8c58b49e032fc4c20b61675adc4194646713e692a51815996791ac8943ffc56
- run_capped_lifecycle_controls.py: 3c67742af99257993ca5c86a054d37c68bdf504dd4e27969fe6ae07d899c6b1e
- universal_start_notebook_launch.py: 7fe5395978170ffc9de0cff993146282c3c8143ee9cb17c54c75963167187133
- universal_start_notebook_run.wl: 280fe22837201d9f401e024453d6c56288c16a2516543ba59f2c2d81b1628d47
- universal_start_notebook.wl: 903f0fb9819ccc781fb5f0a34112ff734a87984548f052e22943c62c5b36fce6

## GC2094: lifecycle results and one corrected B attempt ready

The single Intel GC2093 lifecycle stage PASS:14.58s,71516KiB sampled ownedRSS,7 processes peak,minimum
headroom5967MiB,swap growth0. Two SIGTERMs still give INTERRUPTED and cleanup TERM+KILL/0 owned left;
monitor failure cleans observed children using fresh real ps, while its intentionally broken cleanup
monitor stays labelled UNVERIFIED. Process-cap stop and both stale-identity models pass. No four-control
rerun or new fixture/Lean certificate repeat. Full raw/source/time/launcher/control packet:
cited/gc2094-lifecycle-intel/manifest.json SHA256 74a928f2324131b0de4e8f726b9086b67067468ebd9b49461f48eb6726472aa9.
Public compact receipt:receipts/intel-gc2093-lifecycle.json. This is Intel execution and self-check, not
Local's independent source read.

**B ready for ONE Local attempt after reading/adopting the actual50ec9b3d supervisor/launcher/driver delta,
with no material objection. No further GPT/owner permission round is needed.** If an actual source/cap
difference or safety objection remains, report it rather than substitute or automatically launch.
All five source hashes remain exactly the GC2093 list above. Essay32672082/core409e7c59/catalog12068af9
are unchanged. The17 gates and A3 passed, so do not rerun them.

Command from existing materialized kit root, with existing elan/kernel tools, private resolved arguments:
run_capped.py --track-tree --max-procs 8 --out FRESH --cpu 1200 --wall 1200 --rss-mib 4096
--file-mib 64 --disk-mib 256 --launch-free-mib 5120 --min-free-mib 1024 --swap-growth-mib 512 --
python3 -I universal_start_notebook_launch.py KERNEL universal_start_notebook_run.wl ESSAY KIT.
No other Local kernel/Lean/job; no dependency install, new project lookup or library-target build.
No extra Python wrapper child: the launcher execs the kernel, inheriting its actual limits and capped TMPDIR.
Driver rejects an out-of-root temporary directory BEFORE resource/Lean/build and requires all final files
plus structural gates. Source/olean temporary files and visible artifacts are included in the monitored
256MiB output root; resource/library caches elsewhere are not reported as monitored output.

CPU1200 is PER PROCESS, not an aggregate1200CPU cap. Sampled live ownership is capped8, with up to12
workload lifetimes predicted (nominal14400childCPU across their per-process limits, conditional on that
count); report actual accounting and any excess rather than infer it from the prediction. Monitor and
cleanup overhead are separate;1200s is the running-child wall guard, with sampling/cleanup overhead
reported. Preserve complete launcher/time/stdout/owning-process/receipt evidence on every outcome.

Prediction remains RESULT OK in60–300s,2–3.5GB owned-tree RSS,6 outputs/no Message cells, exact table,
complete standard axiom lists,KernelChecked258. Any refusal/stop/extra-process cap/message/output/source/
temporary-root/count/cleanup discrepancy ends this attempt and is retained, with no automatic retry or
scope/cap widening. A metadata count discrepancy does not by itself refute the theorem. Snapshot
ownership misses processes born AND orphaned inside a0.5s interval and uses ps timestamp resolution;
RSS/headroom are sampled proxies, not hard unified-memory/system peaks. Current source inspections and
controls support this cooperative bounded build; no hostile-process containment guarantee is claimed.

After the run: retain whole notebook, six native output cells, full message handler packet/tally, provenance,
exact embedded module, temp/build/output inventory and final cleanup; GPT performs the actual artifact
read before Local's sole-owner PR/upload. Fresh portal/kit/source checks and external verifier outcomes
remain separate. This read is launch readiness only, not final submission acceptance.

## Stage B attempt 1: CHILD_FAILED at the driver's argument binding; B2 proposed (L1121)

**Attempt 1** (GC2094's single attempt; `receipts/local-gc2094-stageB.json`). Launched at 05:48:23Z after a
read of GPT's actual 50ec9b3d delta, with no material objection. All five source hashes matched the GC2093
list, and no Lean, Lake or other kernel process was running.
- **Result.** `CHILD_FAILED`, rc 1, in 3.69 s: two processes, 291 MB sampled, no escaped or leftover process.
- **Cause.** The driver bound its arguments with `Take[$ScriptCommandLine, -2]`. Under the bare `WolframKernel
  -script`, `$ScriptCommandLine` is `{}` (it is a wolframscript feature), so the essay and kit paths were
  never set. The builder refused at its essay-digest check (`RESULT FAIL essay digest`).
- **Not reached.** No resource lookup, LeanLink call, compile or notebook.
- **Fault.** The driver is mine (L1119), and the binding was never exercised before the stage.

**The argument probe** (`tests/probes/wolfram/script_args_probe.wl`).
- **Attempt 1.** At a 1 MiB per-file cap it died of SIGXFSZ (rc -25) during kernel startup.
- **Attempt 2.** At 4/8 MiB it showed that `$ScriptCommandLine` is `{}`, and that `$CommandLine` ends with the
  script path and then its arguments.

**B2, proposed for GPT's read, not launched.** It is attempt 1's command, caps and sources, with one change:
`universal_start_notebook_run.wl` now reads `Take[$CommandLine, -2]` and refuses unless the essay file and kit
folder exist. Its sha256 is `1a91ee128a5fdceb570cad9dab033c887b3ad711d90a77833e7aac69b4d8163d`. The launcher,
builder, checks, run_capped, essay and caps are unchanged. The prediction and counterfactual are as in GC2094.
One attempt.

## GC2096 B2 prelaunch read

The actual diagnosed four-line change to driver1a91ee128a5fdceb570cad9dab033c887b3ad711d90a77833e7aac69b4d8163d
is accepted for one NEW B2 attempt. Its real argument probe confirms the bare kernel's CommandLine
semantics. All other GC2094 bounds/source/command/prediction/counterfactual unchanged; no gate relaxation
or automatic retry. B1 remains CHILD_FAILED before any build; no notebook validation is imputed to it.
Local may adopt/run B2 after current idle/headroom/source gates with no extra permission round.

## Stage B2 outcome: RESULT OK; the summary receipt failed to export (L1122)

Launched at 05:54:40Z with every hash matching GC2096's list (driver 1a91ee12…) and no Lean or kernel process
running.
- **Result.** `COMPLETED`, rc 0, in 66.95 s, with `RESULT OK`.
- **Resources.** Owned-tree peak RSS 1.84 GB, at most 5 live owned processes, headroom never below
  6050 MiB, no swap growth, no leftover and no stop signal.
- **Notebook.** `essay.nb` is 124,164 bytes, sha256 442525ee….
- **Receipt.** `receipts/local-gc2096-stageB2.json`. The packet (notebook, six output cells, sanitized
  message packet, launcher, stdout, reconstructed summary) is on the shared store at
  `workers/local/universal-start-stageB2/` (manifest 3bf2b014…).

**The builder's gates passed.** `RESULT OK` is printed only when its reason list is empty:
- 6 outputs, 0 message cells, no `$Failed`;
- the grid equal to the retained table;
- the complete standard axiom lists, `cert` with propext only;
- `Success["KernelChecked", …]` with `Declarations` 258, as predicted, and the exact template.

**Two discrepancies, retained, not repaired by a rerun.**
1. The builder printed two messages on the stage's stdout, outside the notebook:
   - `ResourceObject::unkpar`: `ReleaseDate` is not a property, in the builder's own provenance lookup;
   - `Export::jsonstrictencoding`: a `None` value.
2. Because of the second, `summary.json` is 0 bytes. The driver's exit guard checked only that it existed.

The summary's content was reconstructed from the retained files, read-only, and is labelled as such:
- **KernelCheck and notebook.** 258 declarations; 0 Message cells; 0 `$Failed`.
- **Handler.** 15,259 internal events, none printed (General::newsym 15,202, then LocalObject::nso 18,
  MIMETypeToFormatList::fmterr 12, DeleteFile::fdnfnd 12, …), the same pattern as the right-profiles build.

**Privacy.** The notebook and its six cells contain no private path or identifier. Its only temporary name is
the `LeanLinkTmp<session>x<random>` module. The raw message packet held private paths, one of them split
across an InputForm line continuation. The shared copy is sanitized (`messages.sanitized.m`), and the raw
digest is recorded.

## The prepared kit PR (local branch `universal-start`, commit 429d4f7, not pushed)

From kit main 932cf8dd. It adds `lean/Ruliology/CellularAutomata/Rule30UniversalStart.lean` (12068af9…, byte-identical to the
A2a-checked catalog module), `public import Ruliology.CellularAutomata.Rule30UniversalStart` after Rule30PrefixMerger in
`lean/Ruliology.lean`, and this row at the end of `lean/README.md`'s table of modules added in the kit:

| `Rule30UniversalStart` | 2026-10-29 | The universal start of the right diagonals: for a start whose rightmost black cell is at `0`, let `m ≥ 2` be the first index with `x (-m) = x (-(m - 1))`. Then the right diagonals `D (m+1), …, D (m+6)` of `Rule30Realization.evol` have least periods `4, 8, 8, 16, 32, 32`, and `D (m+7)` has least period `32` or `64`, whatever the other start bits (`universal_start`). Every finitely supported start has such an `m` (`universal_start_finite`). The `256` remaining cases, both feeder phases and seven free start bits, are a kernel-checked certificate in sixteen `decide +kernel` declarations (`cert`), which `universal_start_profiles` turns into the least periods. Contributed by Gareth Herbert with Claude (Anthropic) and GPT (OpenAI). | `universal_start`, `universal_start_finite`, `universal_start_profiles`, `cert` |

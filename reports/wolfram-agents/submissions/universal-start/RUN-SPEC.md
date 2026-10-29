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

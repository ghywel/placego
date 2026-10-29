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

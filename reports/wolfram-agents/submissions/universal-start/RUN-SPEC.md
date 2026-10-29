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

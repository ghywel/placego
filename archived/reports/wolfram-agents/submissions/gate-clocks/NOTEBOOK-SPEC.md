# L1221: the gate-clock notebook stage, frozen before its one run

Adapted from the ring-orbits stage (L1134, GC2112), the closest precedent: a core-only single file, built and checked
in a fresh bare kernel. Local is the sole notebook runner and poster. One run, no automatic retry.

**Question.** Does the officially checked source (`14372c1d`, L1221's rerun) run inside the executed essay? That means
its exact literal, the pinned illustration, five exact axiom sets, and a `KernelChecked` object, with a complete
parsed receipt.

**Prediction.** Six Output cells, zero Message cells, no `$Failed`; the computation, axiom and KernelCheck gates true,
with `KernelChecked` reporting 347 declarations. That is the official replay count: with internal names included, the
finite-horizon package matched 324 to 324. It takes 20 to 120 s, with peak tracked RSS below 4 GiB; ring-orbits peaked
at 2.0 GB. Both are hypotheses, not guarantees.

**Counterfactual.** Any stop, gate failure or mismatch, a count other than 347 included, ends the stage, with its
evidence retained. A repair would be a separate freeze, never an edit of this one or a relaxed gate.

Record searched: the ring-orbits, finite-horizon and universal-start stages' tooling and receipts (GC2112, L1187,
L1189), including LeanLink 1.2.2 hiding names containing `.rec` (L1187). This is an interface run, not a new
theorem or novelty search.

## Exact inputs

| File | SHA-256 |
|---|---|
| `Rule30Submission.lean` | `14372c1de82d95341d0d79d4101552683f8b24e9be332712da44600d8b262eb6` |
| `essay-prose.md` | `e92bf6adddd0153244910ad10284bfc6a12bce8bf3486f9e443595ee46aee3f2` |
| `essay.md` (bound by `assemble_gate_clocks_essay.py`) | `9db85853e896c17e31f18661b4190a63f2f88322877bc089a279ba6ef7ada1cd` |
| `assemble_gate_clocks_essay.py` | `f6aebd9b8206e642919524fc1356fbb4504c784633bf3b216f1278c8592eca33` |
| `gate_clocks_notebook_run.wl` | `be800ee8e687ef84beaca62b4fc37124756509946f9c1c1aaf11cc7f67f7ae5a` |
| `gate_clocks_notebook.wl` (pins essay.md) | `6c00c773ff2503a154e87c52e224dfe6aef4187110209f989390b6a3bee526a8` |
| `gate_clocks_notebook_checks.wl` | `3987d980868aa45f9023aa8faf6658e26d6cacbc70e22e549a9278b688d02707` |
| `gate_clocks_notebook_checks_control.wl` | `ae013cb6458c1e6e7023a05cde5da9a8943c358f38d93c1411b73c46bc772e8e` |
| `notebook_receipt.wl` (unchanged) | `4c6301c0d16cba03c03ba141da3afd827d1c5f777f4ea1cefbb8166e862b11e7` |
| `universal_start_notebook_launch.py` (unchanged) | `7fe5395978170ffc9de0cff993146282c3c8143ee9cb17c54c75963167187133` |

**Offline tests (bare kernel, no LeanLink, no build).** All 18 controls pass (`GATE_OUTPUT_CONTROLS_PASS`). The
actual illustration cell, evaluated and boxed as a notebook output, passes the computation gate, and its values equal
those of `gate_clock_control.py`'s independent simulator. The essay's literal decodes to the source byte for byte.

## The six outputs

1. The illustration Association, parsed held and compared with the pinned values.
2. `DirectoryQ` of the kit: `True`.
3. The `LeanEnvironment` object, held for the manual read and never evaluated.
4. The five headline types (`TypeForm`), for the manual read.
5. The five axiom sets, exactly those of the official check, with no missing, extra or duplicate key.
6. `Success["KernelChecked", …]` from its `InterpretationBox`, module `LeanLinkTmp…`, 347 declarations.

## Resources and launch

`run_capped.py --track-tree --max-procs 8 --cpu 1200 --wall 1200 --rss-mib 4096 --file-mib 64 --disk-mib 256
--launch-free-mib 5120 --min-free-mib 1024 --swap-growth-mib 256`, then `python3 -I universal_start_notebook_launch.py
KERNEL gate_clocks_notebook_run.wl ESSAY KIT`, from the pipeline kit. The kernel and kit paths are private. The build
fetches MarkdownToNotebook from the Wolfram Cloud, so it needs network access. No other Lean or Wolfram job runs.

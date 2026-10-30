# L1248: the nested gate-clock notebook stage, frozen before its one run

Adapted from Package A's stage (L1221, which passed at L1222), the closest precedent: the same tooling for a larger
core-only single file, built and checked in a fresh bare kernel. Local is the sole notebook runner and poster. One
run, no automatic retry.

**Question.** Does the officially checked source (`5c2e96a5`, checked first in this freeze) run inside the executed
essay? That means its exact literal, the pinned illustration, five exact axiom sets, and a `KernelChecked` object,
with a complete parsed receipt.

**Prediction.** Six Output cells, zero Message cells, no `$Failed`; the computation, axiom and KernelCheck gates
true, with `KernelChecked` reporting 507 declarations. That is the official replay count, if the official run that
comes first in this freeze reproduces it; the notebook stage runs only after that run passes with 507. With internal
names included, Package A matched 347 to 347. It takes 30 to 180 s, with peak tracked RSS below 4 GiB; Package A
peaked at 2.16 GiB. Both are hypotheses, not guarantees.

**Counterfactual.** Any stop, gate failure or mismatch, a count other than 507 included, ends the stage, with its
evidence retained. A repair would be a separate freeze, never an edit of this one or a relaxed gate.

Record searched: Package A's notebook stage tooling and receipts (L1221, L1222), and the finite-horizon and
universal-start stages behind it (L1187, L1189), including LeanLink 1.2.2 hiding names containing `.rec` (L1187). The
novelty search for the theorem is in L1248: on kit main `7beff71` and the portal (index refreshed 2026-10-30), the only
hits on excess thresholds are `Rule30RecordCharge` and our Package A.

## Exact inputs

| File | SHA-256 |
|---|---|
| `Rule30Submission.lean` | `5c2e96a50add3b75e45e677a7e5f4d6a51ae1822db34c124002499c0bc5f54d5` |
| `essay-prose.md` | `14c2cf375c777711c172a1c1ed960675ec2eaeb8da429155473827de21d44fb2` |
| `essay.md` (bound by `assemble_gate_clocks_nested_essay.py`) | `9d671428f97a2a9baa16e533ac68dbe0f60c3b4ee69530d7d6ba866e25710ba1` |
| `assemble_gate_clocks_nested_essay.py` | `84e3b06a7250e6a61eba19d2fc5a90d647d6f3cf26be9112aeb5e9e039a37819` |
| `gate_clocks_nested_notebook_run.wl` | `fe0969ab22a137426f33439910a875e272777e320d866adb84a3c2c8a31b1f1a` |
| `gate_clocks_nested_notebook.wl` (pins essay.md) | `020886f31b4a1e42e036ab171575287df73676bbbc2d00c63b5d771c049259f0` |
| `gate_clocks_nested_notebook_checks.wl` | `8660eea3e7ed4fa24f84851c61cd3b859cc5c0e0622fa8181c39179b7b540a60` |
| `gate_clocks_nested_notebook_checks_control.wl` | `5728d89cb282f02b39de38d4f40df7f096767e8660ad007ddb31e4a8e8374c1a` |
| `notebook_receipt.wl` (unchanged) | `4c6301c0d16cba03c03ba141da3afd827d1c5f777f4ea1cefbb8166e862b11e7` |
| `universal_start_notebook_launch.py` (unchanged) | `7fe5395978170ffc9de0cff993146282c3c8143ee9cb17c54c75963167187133` |

**Offline tests (bare kernel, no LeanLink, no build).** All 18 controls pass (`GATE_OUTPUT_CONTROLS_PASS`). The
actual illustration cell, evaluated and boxed as a notebook output, passes the computation gate, and its values equal
those of `gate_clock_beam2.py`'s independent bit-parallel simulator on the same twenty gates. The essay's literal
decodes to the source byte for byte.

## The six outputs

1. The illustration Association, parsed held and compared with the pinned values.
2. `DirectoryQ` of the kit: `True`.
3. The `LeanEnvironment` object, held for the manual read and never evaluated.
4. The five headline types (`TypeForm`), for the manual read.
5. The five axiom sets, exactly those of the official check, with no missing, extra or duplicate key.
6. `Success["KernelChecked", …]` from its `InterpretationBox`, module `LeanLinkTmp…`, 507 declarations.

## Resources and launch

`run_capped.py --track-tree --max-procs 8 --cpu 1200 --wall 1200 --rss-mib 4096 --file-mib 64 --disk-mib 256
--launch-free-mib 5120 --min-free-mib 1024 --swap-growth-mib 256`, then `python3 -I universal_start_notebook_launch.py
KERNEL gate_clocks_nested_notebook_run.wl ESSAY KIT`, from the pipeline kit. The kernel and kit paths are private. The
build fetches MarkdownToNotebook from the Wolfram Cloud, so it needs network access. No other Lean or Wolfram job runs.

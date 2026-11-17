# L1233: the finite-past notebook stage, frozen before its one run

Adapted from Package A's stage (gate-clocks NOTEBOOK-SPEC, L1221; PASS at L1222). Local is the sole notebook runner and
poster (GC2299). One run, no automatic retry.

**Question.** Does the officially checked plain source (`33c82f32`, L1233's official PASS) run inside the executed
essay? That means its exact literal, the pinned illustration data, seven exact axiom sets and a `KernelChecked`
object, with a complete parsed receipt.

**Prediction.** Eight Output cells, zero Message cells, no `$Failed`. The data, axiom and KernelCheck gates are true,
with `KernelChecked` reporting 196 declarations, the official replay count; A matched its count exactly, 347 to
347. 20 to 120 s, with peak tracked RSS below 4 GiB; A peaked at 2.2 GiB. Both are hypotheses, not guarantees.

**Counterfactual.** Any stop, gate failure or mismatch, including a count other than 196, ends the stage, with its
evidence retained. A repair would be a separate freeze.

Record searched: A's stage tooling and receipts (L1221, L1222), ring-orbits (GC2112), and LeanLink's `.rec` hiding
(L1187). This is an interface run, not a new theorem or novelty search.

## Exact inputs

| File | SHA-256 |
|---|---|
| `Rule30Submission.lean` (plain form) | `33c82f323c6629dce45206087bedac12f1fc69ca1e2c4a64f65332da8b525d99` |
| `essay-prose.md` | `6b3783f1a896f2dd97611f8c5adeef3e602a528f6afd5f06d77ae2d6a89f8dbe` |
| `essay.md` (bound by `assemble_finite_past_essay.py`) | `6e818ab162679a91ca490b02fbce215bbbbef1dee46b8d57a7e1b4477e25b41d` |
| `assemble_finite_past_essay.py` | `0abc63716559de4a66d99ee1868385e06a4713d8c604a2e6a3607f097a3b9e33` |
| `finite_past_notebook_run.wl` | `e8ad0827aae6e2f3a26630fbf2057d1663a08b51c4708e0aede99b3f01b2b7f8` |
| `finite_past_notebook.wl` (pins essay.md) | `ac45c4c2013ef1e6584c86a425cfdce4c69663c78889d2912aba9161de2490b3` |
| `finite_past_notebook_checks.wl` | `525f6171a7f6ce8fc9bdf3153e40f9e7673ae8fa71aab1a21357c2c1668b1a22` |
| `finite_past_notebook_checks_control.wl` | `645cc5cdb777d874ccf28658894f40ad5831af004b7b54bef5e64f2499cbd40e` |
| `notebook_receipt.wl` (unchanged) | `4c6301c0d16cba03c03ba141da3afd827d1c5f777f4ea1cefbb8166e862b11e7` |
| `universal_start_notebook_launch.py` (unchanged) | `7fe5395978170ffc9de0cff993146282c3c8143ee9cb17c54c75963167187133` |

**Offline tests (bare kernel, no LeanLink, no build).** All 18 controls pass (`FINITE_PAST_OUTPUT_CONTROLS_PASS`). The
actual data cell, evaluated and boxed, passes the data gate, and its values equal GPT's VALIDATION-SPEC expectations.
The essay's literal decodes to the source byte for byte.

## The eight outputs

1. The evolution picture and row table, for the manual read.
2. The count table and orientation check, for the manual read.
3. The same values as an Association, parsed held and compared with the pinned values.
4. `DirectoryQ` of the kit: `True`.
5. The `LeanEnvironment` object, held for the manual read, never evaluated.
6. The seven headline types (`TypeForm`), for the manual read.
7. The seven axiom sets, exactly those of L1229 and the official check.
8. `Success["KernelChecked", …]` from its `InterpretationBox`, module `LeanLinkTmp…`, 196 declarations.

## Resources and launch

`run_capped.py --track-tree --max-procs 8 --cpu 1200 --wall 1200 --rss-mib 4096 --file-mib 64 --disk-mib 256
--launch-free-mib 5120 --min-free-mib 1024 --swap-growth-mib 256`, then `python3 -I universal_start_notebook_launch.py
KERNEL finite_past_notebook_run.wl ESSAY KIT`, from the pipeline kit. The kernel and kit paths are private. The build
fetches MarkdownToNotebook from the Wolfram Cloud and needs network access. No other Lean or Wolfram job runs.

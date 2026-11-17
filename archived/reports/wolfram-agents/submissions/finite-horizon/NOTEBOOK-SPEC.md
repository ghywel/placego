# L1184: the horizon notebook build, frozen for GPT's read (not run)

**L1189 outcome:** the one repaired GC2188 stage PASSED: 20 controls, 5 outputs, 0 Message cells, eight exact standard axiom sets, KernelChecked 324, native source byte-equal to 791e45ed ([receipt](receipts/local-l1189-notebook.json)). GPT's artifact read precedes posting.

**L1187 outcome:** the one GC2182 stage FAILED at its axiom gate, because LeanLink hides names containing `.rec`. A repaired essay and its re-pinned driver and launcher are frozen in the last section, prepared and not run. The section below is the historical L1184 freeze.

One stage, adapted from the arc package's final five-output stage ([arc NOTEBOOK-SPEC](../arc-codes/NOTEBOOK-SPEC.md),
GC2115, completed in GC2117). Local is the sole notebook runner and poster. It runs only after GPT's read, with no
other Lean or Wolfram job, and no automatic retry.

**Question.** Does the officially checked single file (L1183) run inside the executed essay? That means its exact
source, the illustration grid, the eight standard axiom sets and a `KernelChecked` object of 324 declarations, with a
complete parsed receipt.

**Prediction.**
- All 20 controls pass, there are exactly 5 Output cells, 0 Message cells and no `$Failed`, the receipt parses, and
  `KernelChecked` reports 324 declarations.
- It takes 30 to 120 s, with peak owned RSS below 5120 MiB. The arc's stage peaked at 4.79 GB (4,790,384 KiB) on a
  169-declaration module; our official compile peaked lower than the arc's (2.72 against 3.38 GB). This is a
  hypothesis, not a resource guarantee.

**Counterfactual.** Any control, compile, output, receipt, resource, pressure or cleanup stop ends this one stage,
with its evidence retained. There is no rebuild, cap increase or weakened 324 gate. If memory stops it, the next
step is to inspect the actual cost; a restart of the host (offered by the owner) would be the way to more headroom,
since the 1024 MiB free floor binds before a larger RSS cap could.

Record searched: the arc stage's actual tooling, receipt and GC2114 RSS failure; the L1183 official receipt (324
replayed); the bound essay 4d24ea07. This is an interface run, not a new theorem or novelty search.

## Exact inputs

| File | SHA-256 |
|---|---|
| `Rule30Submission.lean` | 791e45ed1aef3955035989f1443f43a3427ea82b0cb01a8ad088bc221ec57110 |
| `essay.md` (bound by `assemble_horizon_submission.py`) | 4d24ea0712555cec4c8645a3055a369fc791891a68575ab68e05cd7904592355 |
| `horizon_notebook_launch.py` | d61faa2a7a0b6fa83ca556e70f3912da86712b9b91c1130a5ed7f673a0001535 |
| `horizon_notebook_run.wl` | 588f1cbda2794f6561e05d74d309a272bb437e3a7de92789cb1c0db59da4fa4e |
| `horizon_notebook_checks.wl` | 003aab35ce7760fcaac2ab4245901996ecc09a1fc24adc6e4d43f6cf20364c70 |
| `horizon_notebook_control.wl` | 0f066b3a5db550ce04f1de6fb8f66d0278e9e6b4585eda70985652f8c79e3fba |
| `notebook_receipt.wl` (unchanged from the arc) | 4c6301c0d16cba03c03ba141da3afd827d1c5f777f4ea1cefbb8166e862b11e7 |

The launcher checks the four tooling pins, the essay and the source. It decodes the essay's quoted source literal
with JSON and compares all its bytes with 791e45ed. It copies everything into a fresh `CAPPED_OUT`, points
TMPDIR, TMP and TEMP inside it, and execs the existing bare kernel. The driver, checks and receipt are the arc's,
renamed, with this package's pins.

## What changed from the arc

- **Headlines and count.** The eight agreed headlines, and the `KernelChecked` gate at 324 (from L1183).
- **The illustration grid is symbolic.** Its slopes are `GoldenRatio - 1`, `Sqrt[2] - 1`, `E - 2` and `Pi - 3`. A held
  comparison cannot equate a parsed `Sqrt[2]` with the evaluated `Power[2, 1/2]`. So the grid's data is parsed with
  `HoldComplete`, every symbol in it from level 2 down must be on a whitelist (List, Plus, Times, Power, Sqrt,
  Rational, GoldenRatio, E, Pi), and only then is it evaluated and compared with the L1177 values. `HoldComplete` is
  never whitelisted, since `ReleaseHold` would release an inner one.
- **Controls: 20, not 18.** The arc's 18 are adapted, plus `wrong_grid_slope` and `grid_code_is_held`.

**Offline tests (pure Wolfram Language, no LeanLink, no build, no stage).**
- All 20 controls pass in wolframscript.
- The actual illustration cell, evaluated and boxed as a notebook output, passes the grid check.
- Two further probes are refused, with the side effect still 0: a grid hiding code in an inner `HoldComplete`, and
  the pre-GC2173 header.
- The first attempt found two bugs, both now fixed. The level-1 scan saw the wrapper's own head, and the
  duplicate-key control evaluated its association.
- The launcher's pre-exec checks pass with a deliberately missing kernel name, and an altered essay is refused.

## The five outputs

1. The illustration grid, checked as above.
2. `DirectoryQ` of the kit: `True`.
3. The `LeanEnvironment` object, held for the manual read and never evaluated.
4. The eight axiom sets, each exactly propext, Classical.choice and Quot.sound, with no missing, extra or duplicate
   key, and no code evaluated.
5. `Success["KernelChecked", …]` from its `InterpretationBox`, with module `LeanLinkTmp…`, 324 declarations, and
   matching message parameters and template.

## Resources and launch

The arc's GC2115 envelope, unchanged:
- `run_capped.py --track-tree --max-procs 8 --cpu 1200 --wall 1200 --rss-mib 5120 --file-mib 64 --disk-mib 256
  --launch-free-mib 6144 --min-free-mib 1024 --swap-growth-mib 256`.
- CPU 1200 s is per process, not an aggregate. The arc saw at most 5 processes.
- Launch from the pipeline kit root, with the elan tools on PATH as in the arc run:
  `python3 -I horizon_notebook_launch.py KERNEL ESSAY KIT`. The kernel path and kit path are private and are not
  committed.

The parent must finish `COMPLETED` with child exit 0 and no stop. No child marker, JSON or post-stop artifact can
override the parent outcome.

## Retained evidence, and what follows

The following are retained:
- the pins and the launch command;
- the stdout, time and supervisor receipts;
- the actual notebook, all five exported cells, and the raw and parsed summary;
- the message packet and tally, and the 20 control outcomes.

Before posting, GPT reads the actual outputs, axioms, `KernelChecked` object and native source literal, and scans
for privacy. A local notebook pass is distinct from the portal's Lean Verified and Human Verified states.

## L1187: the first outcome (retained failure), and the repaired stage (prepared, not run)

**Outcome.** The stage ran from 15:29:50Z to 15:30:36Z on the restarted host, at 6791 MiB headroom.
- **Parent.** `CHILD_FAILED`, child exit 1, wall 45.9 s, peak owned RSS 4.60 GB, at most 5 processes, minimum free
  5497 MiB, no swap growth.
- **What passed.** The inputs and all 20 controls passed. The notebook built in 31.5 s, with 5 outputs and 0 Message
  cells. The grid matched, and `KernelChecked` reported 324 declarations of `LeanLinkTmp…`, with a matching template.
- **What failed.** Output 4 held the exact standard set for seven headlines, but for `RecodedHorizon.recoded_horizon`
  it held `Missing["KeyAbsent", …]["Axioms"]`.
- **Receipt:** [local-l1187-notebook-failed.json](receipts/local-l1187-notebook-failed.json). The full sanitized
  packet is workers/local/l1187-notebook-failed-packet/, MANIFEST d3152961.

**Cause, from LeanLink's source.** `Lean.wl` line 2985 defines `isInternalName` as `StringContainsQ` against
patterns that include `.rec` and `.inj`. `LeanImport` drops every such name unless `"IncludeInternal" -> True`, and
`LeanImportString` passes its options through. So `….recoded_horizon`, `….recode` and `….recurrence_one` are absent
from the environment. Of the checker's 155 declarations, these are the 3 user names missing among the 17 absent;
the other 14 are generated auxiliaries. The kernel replay is unaffected, since it covered all 324.

**Probe, frozen in de958989 and run once per mode.**
- It used a core-only module with `Probe.plain` and `Probe.recoded`, and `leanlink_rec_filter_probe.wl`.
- **Default import:** `Probe.recoded` is missing.
- **With `"IncludeInternal" -> True`:** both are present, with empty axiom sets.
- `KernelCheck` reports 2 declarations in both modes.
- Each run ended `LEFTOVER_CLEANED` with child exit 0: a process remained at the end, and the supervisor reaped it.

**Repair: one option in the essay, with no source, check or cap change.**
- The import cell becomes
  `LeanImportString["%%LEAN%%", "ProjectDir" -> $Rule30PrizeKit, "IncludeInternal" -> True]`.
- One sentence explains why.
- The prose is now 060de9b8, pinned in the assembler, and the bound essay is 203fd0a6.
- The driver and launcher change only their essay and driver pins. The checks, controls and receipt helper are
  byte-identical, and so are the grid, the axiom and `KernelChecked` 324 gates, the 20 controls and every cap.

| File | SHA-256 |
|---|---|
| `essay-prose.md` | 060de9b8c435cce923735f9c2ce81b0451592fd0e2dda6366f3ee7b9518d91ef |
| `essay.md` | 203fd0a6e9b43861e85b94fb62f5e257e9712a1235cd78a9c2e3e2a79c4e1def |
| `horizon_notebook_launch.py` | f7654266d10a4c657a50259ace6f6fb8718aa92ffcb08bd0d8b226f24d8692fb |
| `horizon_notebook_run.wl` | 154be32878d56869d5e317c0352226bf321733bfa9e81ad22651a77ed2ec125b |
| `horizon_notebook_checks.wl` | 003aab35ce7760fcaac2ab4245901996ecc09a1fc24adc6e4d43f6cf20364c70 (unchanged) |
| `horizon_notebook_control.wl` | 0f066b3a5db550ce04f1de6fb8f66d0278e9e6b4585eda70985652f8c79e3fba (unchanged) |
| `notebook_receipt.wl` | 4c6301c0d16cba03c03ba141da3afd827d1c5f777f4ea1cefbb8166e862b11e7 (unchanged) |
| `Rule30Submission.lean` | 791e45ed1aef3955035989f1443f43a3427ea82b0cb01a8ad088bc221ec57110 (unchanged) |

**Prediction for the repaired stage:** as in L1184, with output 4 now holding all eight exact standard sets.
`KernelChecked` stays 324, as the probe's equal counts and the failed stage's 324 indicate. Any stop ends the stage,
with its evidence retained.

# Run specification for the classic-ether front-speed entry (NIGHT-TASKS A1; Local, L1346)

**Sources.**
- **Catalog module.** `tests/probes/lean/EtherEdgeZero.lean`, sha256
  `005f5e3ec90bc26af48ec640a6d7943db505d0dbf7c45d20df1cc5e3b899dfe2` (L1345; GPT's source read requested).
- **Portal form.** `Rule30Submission.lean` (this folder), sha256
  `dc9ea874f8342ac7b900a63392f2750e7ad62f6e38a877cbae8b7b09725e99b3`, 360 lines.
  `tests/probes/wolfram/make_ether_zero_submission.py` generates it mechanically:
  - plain imports of `Rule30Prize` and `Rule30Ether`;
  - `namespace Rule30Submission` with `open Ruliology.CellularAutomata`;
  - no `module`, no `public import` and no `@[expose] public section`;
  - the module docstring in public wording.

  All 350 code lines are kept byte for byte. The script refuses internal references.
- **Check.** `tests/probes/wolfram/check_ether_zero.sh`, adapted from `check_ether_episode.sh`. It pins both sources and
  the kit's unchanged `Check.lean` (`b882f2527a1d6e72…`).
  - **Part c.** The catalog module is compiled under the root `EtherZeroCert`.
  - **Part s.** The portal form is compiled alone.
  - **Requirements for both parts.** Empty compiler output, one checker JSON line with a pass and replay ok, the
    official import, no new axioms, exactly the three headlines ok, and every declared constant standard.
- **Headlines.** `edge_pinned`, `trap_two_sided` and `wall_ne_ref_all`.
- **Kit.** The verifier's image 15 is kit `93d98bbe049177d2c1546b6b0714aa33703ae13d`, Lean 4.35.0 (portal
  `environment`, refreshed 23:37Z). `Rule30Ether`, `Rule30StripCertificates`, `Rule30Jen`, `Rule30MaskedJen`,
  `Rule30Diagonals`, `Rule30Prize` and `Check.lean` there are byte-identical to kit main c42f6e5. The closure of
  `Rule30Ether` is built in a fresh fetch of 93d98bbe (7 jobs).

**Command.** From `<kit 93d98bbe>/lean`:
`run_capped.py --track-tree --max-procs 10 --out FRESH --cpu 600 --wall 900 --rss-mib 6144 --file-mib 64 --disk-mib 512
-- lake env sh check_ether_zero.sh CATALOG SUBMISSION CHECKER`.

**Prediction.** `ETHER_ZERO_CHECK_PASS` for both parts, in under 3 minutes and under 3 GB per process (the kernel `decide`
of the 28 entries took 34 s and 2.6 GB in development). Each part has three ok headlines, replay ok and no new axioms.

**Counterfactual.** Any of the following ends the stage, and its output is kept: a stop, a diagnostic, a nonempty compiler
output, a name clash in `Rule30Submission`, a replay failure (for example a `decide` the replay cannot redo), or a guard
failure. One attempt, with no other job running.

**Record searched.** The precedents are ether-episode's RUN-SPEC (L1267–L1271) and `check_ether_episode.sh`. The kit's
`Check.lean` docstring was read.

## Results (written after the run)

**ETHER_ZERO_CHECK_PASS** (Local, M5, kit 93d98bbe, 3 November about 00:35Z). Under `run_capped.py --track-tree`:
COMPLETED, 175 s wall, peak RSS 3.22 GB.
- **Part c** (`EtherZeroCert.EtherEdgeZero`) and **part s** (`Rule30Submission`) both pass:
  - the compiler output is empty (0 bytes);
  - the checker's verdict is `pass`, with replay ok for 123 constants;
  - `importsStatements` is true and there are no new axioms;
  - the three headlines `edge_pinned`, `trap_two_sided` and `wall_ne_ref_all` are all ok;
  - every declared constant is standard (59 in part c, 62 in part s).
- The portal form's checker output has sha256 `aea15922153c332e…`. The kit's own `Check.lean` prints a deprecation
  warning (`Lean.Environment.replay`) before its JSON line; it is the checker's, not ours.
- **Prediction.** It held for the pass and for time (under 3 minutes). It narrowly **failed** for memory: 3.22 GB
  against "under 3 GB".

## Second run, after GPT's source read (L1351; prediction written before the run)

**What changed (GC2412).**
- **The credit.** Every docstring, the essay, the abstract and the README now credit `Rule30Ether` and its
  `trap_invariant` neutrally as the kit's (PR 65 added `Lock` and `Rule30EtherWallWitness` later), not to "Lowry, PR65".
- **The new theorem, GPT's 198-cell shield.** `agree_cone` (radius-one locality), `pinned_of_check_tail` and
  `edge_pinned_tail`: every evolution whose initial row agrees with the inserted edge's on x ≤ 198 is pinned the same way.
- **New sources.**
  - Catalog: `tests/probes/lean/EtherEdgeZero.lean`, sha256
    `4787092702a8744f3376c0fa074991f641df98fd3cf3ab7885536e508fd53773`; `edge_pinned_tail` is kernel-checked with
    standard axioms, 35 s.
  - Portal form: `4a2688b0c03fd1274aa0a2381f98b5405f7fb42ab0a1bde1c1472bcf6db07018`, 438 lines (428 code lines kept
    byte for byte).
- **Check.** `check_ether_zero.sh` is re-pinned, with four headlines: `edge_pinned`, `edge_pinned_tail`,
  `trap_two_sided` and `wall_ne_ref_all`.

**Prediction.** `ETHER_ZERO_CHECK_PASS` for both parts, under 4 minutes and under 3.5 GB. Four ok headlines per part,
replay ok, no new axioms. **Counterfactual.** Any guard failure ends the stage, and its output is kept. Same caps and
command as the first run.

**Second run: ETHER_ZERO_CHECK_PASS** (Local, M5, kit 93d98bbe, 3 November about 00:50Z). COMPLETED in 175 s, peak
3.22 GB.
- Both parts have empty compiler output, verdict `pass` and replay ok, now for 140 constants.
- There are no new axioms, and the four headlines `edge_pinned`, `edge_pinned_tail`, `trap_two_sided` and
  `wall_ne_ref_all` are all ok. Every declared constant is standard (62 in part c, 66 in part s).
- The portal form's checker output has sha256 `cac52618cd718a03…` (unscrubbed).
- The prediction (under 4 minutes, under 3.5 GB) held.
- **Raw receipts.** Those of both runs, and of A2's check, are on the shared store as
  `cited/local/l1351-a1-a2-check-receipts.tar.gz`, sha256 `61a326a5…4ff3`, 5,497 bytes. The home path is replaced by
  `~` in those copies, so their per-file digests differ from the unscrubbed ones quoted here.

## The release notebook (L1354; prediction written before the run)

- **Essay.** `essay.md` (sha256 `ee7aefd3f9b1de77…`) comes from `assemble_ether_zero_essay.py`, which pins
  `essay-prose.md` (`86068b39…`, after the GC2413/GC2416 prose corrections) and the checked portal form
  (`4a2688b0…`), and embeds the source verbatim as a multi-line string after `(*Iconize["Lean source"]*)`.
- **Driver.** `tests/probes/wolfram/ether_zero_notebook.wl` (`5fe368192f101a28…`), adapted from `ether_episode_notebook.wl`.
  It runs through `universal_start_notebook_launch.py` from a fresh worktree of the kit at 93d98bbe, with the prebuilt
  packages linked (Mathlib 56a00585, matching the verifier). The closure of `Rule30Ether` and `Rule30Prize` is built
  there.
- **Kernel.** Wolfram Engine 15.0, cloud-connected, LeanLink 1.2.2. The verifier lists LeanLink 1.2.1; noted.
- **Caps.** run_capped --track-tree, CPU 1,500 s, wall 1,500 s, RSS 8,192 MiB, 24 processes.
- **Prediction.** `RESULT OK`, in under 6 minutes and under 6 GB, with these gates:
  - 8 output cells, 0 message cells, no `$Failed`;
  - the source iconized;
  - the kit cell True and a `LeanEnvironment`;
  - the four axiom sets exactly {propext, Classical.choice, Quot.sound} ×2, {propext, Quot.sound}, {propext};
  - `KernelChecked` with 140 declarations.
- **Counterfactual.** Any failed gate ends the stage, and the notebook and receipts are kept. A failure of the two figure
  cells (wrap or size) or of the declaration count gets one corrected rebuild under a new prediction.

**Result: RESULT OK** (Local, M5, kit worktree at 93d98bbe, 3 November about 01:13Z). COMPLETED in 103 s wall (91 s
build), peak 3.43 GB, and no kernel or Lean process was left running. The prediction (under 6 minutes, under 6 GB, every
gate) held.
- **Every gate passed.**
  - The notebook has 8 output cells, 0 message cells and no `$Failed`.
  - The source is iconized, the kit cell is True, and the output is a `LeanEnvironment`.
  - The four axiom sets are exact.
  - `KernelChecked` reports 140 declarations, the official replay count.
- **Not a gate, recorded.** The message handler logged 18,918 events during MarkdownToNotebook. None became a message
  cell. Their kind was not recorded by this driver.
- **The notebook.** `essay.nb` is sha256 `c50e21cbc1740a8932f3ab8ae37079191e40defd9c93930d514524969a4c0c63`, 145,737
  bytes. `summary.json` gives the 8 output digests, and the driver is `5fe36819…`. The notebook and every cell receipt
  were checked for local paths: none.
- **Figures, inspected by eye.** The ether pattern; the difference at (4, 3), whose left edge drifts left to about −35
  and then runs straight down from about tick 220; and the four headline statements as Lean prints them. All three
  match the text.
- **Archive.** The notebook and its receipts (launcher output scrubbed of the home path) are on the shared store as
  `cited/local/l1354-ether-zero-release.tar.gz`, sha256 `da106492…a05f`, 47,469 bytes. They are kept outside git.

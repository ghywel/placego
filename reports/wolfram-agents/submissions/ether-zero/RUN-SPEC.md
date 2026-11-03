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

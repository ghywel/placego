# Run specification for Rule30RingOrbits (Lemma R)

**Sources.**
- **Catalog module.** `Rule30RingOrbits.lean`, sha256
  `15541031a3b309abc527155f2661fff85c2dc604ccefaa6788ba73abe1b6fe48`, core imports (`Rule30Prize`,
  `Rule30Realization`).
- **Submission form.** `Rule30Submission.lean`, sha256
  `e04eca51d9f3e912fa6939bfd5fd7c6d6b527036fae7ea28bc80ea7931458238`. It is generated mechanically: the same two
  imports, `namespace Rule30Submission` and `open Ruliology.CellularAutomata`. The diff from the catalog form is
  only the namespace and `open` lines. A clash scan finds none of its 22 names declared bare in
  `Ruliology.CellularAutomata`.

**Development compiles** (`tests/probes/wolfram/dev_compile.sh`; not release evidence). The catalog module
compiles with no diagnostics. A copy with `#print axioms` shows every headline standard:
- `ring_period_two` uses propext, Classical.choice and Quot.sound;
- `per_add_mul` uses propext; `decode_encode` uses Quot.sound;
- the rest use propext and Quot.sound.

The submission form shows the same sets.

**The full check, proposed for GPT's read, not launched.** `tests/probes/wolfram/check_ring_orbits.sh`, sha256
`6e5fa0cad3b23dad66c37dc68613a3e80585711c4fa2d9e39dd137b588a99297`.
- **Pins.** Both sources and the unchanged Check.lean (b882f252…).
- **Part c.** The catalog module is compiled under the root `RingOrbitsCert`, then checked as
  `RingOrbitsCert.Rule30RingOrbits` with the eight headlines `Ruliology.CellularAutomata.Rule30RingOrbits.`
  `orbit_eq_iff`, `encode_walk`, `decode_ring`, `decode_encode`, `encode_decode`, `ring_fixed`,
  `ring_period_two` and `alternating_even`.
- **Part s.** The submission form is compiled under its single-file root, then checked as `Rule30Submission` with
  the same eight names.
- **Guards for each part.**
  - empty compiler output;
  - one checker JSON line, with the exact module, a pass and replay ok;
  - the official import and no new axioms;
  - exactly the eight headlines, all ok;
  - every declared constant standard.
- **Command.** From the pipeline kit root, with elan tools on PATH: `run_capped.py --track-tree --max-procs 6
  --out FRESH --cpu 120 --wall 300 --rss-mib 2048 --file-mib 16 --disk-mib 64 --launch-free-mib 4096
  --min-free-mib 1024 --swap-growth-mib 256 -- lake env sh check_ring_orbits.sh CATALOG SUBMISSION`.
- **Prediction.** `RING_ORBITS_CHECK_PASS` in under 30 s, under 1.5 GB per process, with the headline axiom sets
  of the development compiles.
- **Counterfactual.** Any stop, diagnostic, guard failure or nonstandard axiom ends the stage and is retained.
  One attempt, with no other job running.

**Record searched** (`known_find`, kit 932cf8dd, portal 06:22Z). No matching result was found in the inspected
material, which is not a proof that none exists.
- "light-speed": 0 hits.
- "closed walk": the kit's ether-trap input graphs and `Rule30LocalConservation`.
- "spatially periodic": `PeriodicPoints` (velocity [−1, 1)) and `Rule30DelayedDefectPeriods`.

## GC2106 amendment: the positive-parameter wording, and the re-frozen sources

GPT's carrying read of the source (GC2106, LEMMA-R-SOURCE-REVIEW.md) accepted it, with one prose correction. The
encode/decode identities hold for every P and m, but reading them as closed walks in the finite graph of
P-periodic words, on a finite ring, needs 0 < P and 0 < m, because at 0 the periodicity condition is vacuous. The
module docstring now says so; no proof or type changed. The new sources and wrapper:
- `Rule30RingOrbits.lean`: `61fbff78da7c93e345d789a35396de373b42c25040eb66e227a5460af4a34e24`;
- `Rule30Submission.lean`: `23a3be9f7d008bcdeb0d9e4ffbc037d593457ad97e0064da35f323578d473a96`, regenerated
  mechanically;
- `check_ring_orbits.sh`: `e507784912374f54c01d937383bea3bdfbce6d06b8fe2ddc65dd6380a67ae321`, changed only in the
  two source pins.

Command, caps, guards and prediction are as above. One attempt.

## Stage B (the notebook), proposed for GPT's read, not launched (L1134)

**Essay.** `essay.md`, `0cefd19b86f2a8bcf700dfbdf50cad877bb78ce1d9c2696ed21f468dda5fdabe`. It is assembled from `essay-prose.md`,
minus the private note, with the checked submission form 23a3be9f… embedded byte for byte. Its computation cell now ends
in a plain Association (the counts for sizes 1 to 12, and the first return of 0001), so the gate can parse it held.

**Files** (sha256):
- `ring_orbits_notebook_checks.wl`: `530f48c666fec8e8344e10ccb3ff1d8747fa2ba60bc6f2bf98e8a0fc8ad977cd`
- `ring_orbits_notebook_checks_control.wl`: `27c23b324803c164ea2fc3d4fbd892443eab9edb78d85650309821bc1f5306d1`
- `ring_orbits_notebook.wl`: `cc637e2f320071fe007f427b684bb7bdb08052b1791c444b39c56569d250ed0c`
- `ring_orbits_notebook_run.wl`: `48b834b1b9a3dbb35d617a1d0a3d7848ad09d4c8fce6c9bd9a2386ee8a2198c0`
- `universal_start_notebook_launch.py`: `7fe5395978170ffc9de0cff993146282c3c8143ee9cb17c54c75963167187133`
- `notebook_receipt.wl`: `4c6301c0d16cba03c03ba141da3afd827d1c5f777f4ea1cefbb8166e862b11e7`
- `run_capped.py`: `c8c58b49e032fc4c20b61675adc4194646713e692a51815996791ac8943ffc56`

The launcher, the receipt helper and `run_capped` are the accepted, unchanged ones (B2, GC2107, GC2093).

**What the stage checks.** The builder and driver adapt B2 with GPT's receipt helper.
- **Notebook.** Exactly 6 outputs, 0 Message cells, no `$Failed`.
- **Computation.** The cell, held, equals the expected Association.
- **Axioms.** The eight exact keys, each with its exact standard set; both sides are sorted before comparing,
  which is the lesson of L1118.
- **KernelCheck.** `Success["KernelChecked", …]` with 59 declarations (predicted from the release replay) and a
  consistent module and template.
- **Receipt.** Provenance through `nrResourceMetadata`. The summary is written through `nrWriteReceipt`, and a
  `Failure` counts as a failure. The driver exits 0 only if `nrReceiptFileOK` accepts `summary.json` with its
  required keys, reasons are empty and every gate is true.

**The output-gate controls run first.** `ring_orbits_notebook_checks_control.wl` has 18 fixtures, 3 positive and 15
adversarial, with no build, LeanLink, network or process. It runs as `WolframKernel -script` under the controls'
caps (CPU 30, wall 60, RSS 1024, file 4, disk 8, launch 2048).

**Stage B command.** From the pipeline kit root, with elan tools on PATH:
`run_capped.py --track-tree --max-procs 8 --out FRESH --cpu 1200 --wall 1200 --rss-mib 4096 --file-mib 64
--disk-mib 256 --launch-free-mib 5120 --min-free-mib 1024 --swap-growth-mib 512 -- python3 -I
universal_start_notebook_launch.py WolframKernel ring_orbits_notebook_run.wl ESSAY KIT`.
These are B2's caps; B2 peaked at 1.84 GB, and this module is smaller.

**Prediction.** RESULT OK and exit 0 in 30–120 s, peaking under 2 GB, with the six outputs and gates as above.
**Counterfactual.** Any stop, gate, receipt or count discrepancy ends the attempt and is retained. One attempt.

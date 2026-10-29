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

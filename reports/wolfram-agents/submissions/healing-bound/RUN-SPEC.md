# Run specification for the universal healing bound (NIGHT-TASKS A2; Local, L1350)

**Sources.**
- **Catalog module.** `tests/probes/lean/HealingBound.lean`, sha256
  `90118b629613146a7269d3b74ffd094bbe289b25e8a12007a874bc221adce7d9` (L1349; GPT's read requested).
- **Portal form.** `Rule30Submission.lean` (this folder), sha256
  `f444ae698fa0de3fff978a5c41ea09aaebc91c80ce3da4ec668a6780c8d325b8`, 59 lines.
  `tests/probes/wolfram/make_healing_submission.py` generates it mechanically (plain imports of `Rule30Prize` and
  `Rule30Jen`, `namespace Rule30Submission`), keeping all 49 code lines byte for byte.
- **Check.** `tests/probes/wolfram/check_healing_bound.sh`, adapted from `check_ether_zero.sh`. Parts c and s, the same
  guards, and the headlines `healing_bound`, `front_ge` and `K_succ_bounds`. The kit's `Check.lean` is pinned
  (`b882f2527a1d6e72…`).
- **Kit.** The verifier's image 15 is kit 93d98bbe, the same fetch as A1's check.

**Command.** From `<kit 93d98bbe>/lean`:
`run_capped.py --track-tree --max-procs 10 --out FRESH --cpu 300 --wall 600 --rss-mib 2048 --file-mib 64 --disk-mib 256
-- lake env sh check_healing_bound.sh CATALOG SUBMISSION CHECKER`.

**Prediction.** `HEALING_BOUND_CHECK_PASS` for both parts, in under 60 s and under 1 GB. There are no `decide` steps and
only a short induction. Each part has three ok headlines, replay ok and no new axioms.

**Counterfactual.** A stop, a diagnostic, a nonempty compiler output, a name clash or a guard failure ends the stage, and
its output is kept. One attempt.

**Record searched.** A1's RUN-SPEC and `check_ether_zero.sh` (L1346).

## Results (written after the run)

**HEALING_BOUND_CHECK_PASS** (Local, M5, kit 93d98bbe, 3 November about 00:42Z). COMPLETED in 2.0 s, peak RSS 924 MB.
- Parts c (`HealingCert.HealingBound`) and s (`Rule30Submission`) both pass: empty compiler output, verdict `pass`,
  replay ok, official import, no new axioms, and the three headlines ok.
- The prediction (under 60 s, under 1 GB) held.

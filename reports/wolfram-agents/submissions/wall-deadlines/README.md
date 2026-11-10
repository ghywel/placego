# The wall deadlines of rules 90 and 150 (queue row S-18, Cloud's K-05)

**Full source/actual-nb1 read PASS GC2844; corrected-source Checks/nb2/pins/dry gates next; not posted.** [Complete review](../../../GPT-S18-RELEASE-REVIEW-20261110.md). Fixed only the module introduction's first-white terminology and the essay's count range (`2n<W`); declaration/proof body unchanged. Local reruns both source Checks, updates the kit branch, builds nb2 with the unchanged driver/original gates, updates notebook/source/essay pins and fresh dry check; these complete standing conditional posting/PR clearance without another permission round. Old nb1 and receipts below are historical. Built from BR-6.1 as Cloud carried it (CL773; the triage report `reports/CLOUD-SW02-CARRY-TRIAGE-20261110.md` §10 (a), (b)). Local wrote the module directly. Proof-size context is not formalised; Cloud's separate hardness3 addition remains its original PROOF-SKETCH.

## What the module proves

`Rule30WallDeadlines` is core Lean, 333 lines, and imports only `Rule30ZeroBoundary`. It has ten headlines: `zr_or_eq_zrow`, `fib2_mod`, `odd90`, `kstar_spec`, `deadline90`, `sharp90`, `two_step150`, `odd150`, `deadline150` and `sharp150`.

The sharpness statement for rule 90 uses `2 * s + 2 ≤ kstar W` rather than `2 * s ≤ kstar W - 2`. With natural subtraction the latter would be false at `W = 0`, where `kstar 0 = 1`.

| Form | File | sha256 | Check |
|---|---|---|---|
| Portal | [`Rule30Submission.lean`](Rule30Submission.lean), from [`kit_to_portal.py`](../../../../tests/probes/swarm/sw02/block11/kit_to_portal.py) | `6afbb54f…` | pass at `5fb59158`: 27 declared, 87 constants, 10 headlines, standard axioms ([receipt](check-5fb59158.json)) |
| Kit | [`Rule30WallDeadlines.lean`](Rule30WallDeadlines.lean) | see receipt | pass at main `03a19bf`: 26 declared, 87 constants ([receipt](check-kit-03a19bf.json)). The kit branch `wall-deadlines` at `eb5fd65` is local; [`kit-integration.patch`](kit-integration.patch) |

**Mutants.** All six were rejected ([output](../../../../tests/probes/swarm/sw02/block11/mutate_wall_deadlines.out)).

## Release artifacts

- **Texts:**
  - [`essay-prose.md`](essay-prose.md);
  - [`essay.md`](essay.md) (corrected `5d0d8cff…`, from [`assemble_wall_deadlines_essay.py`](../../../../tests/probes/wolfram/assemble_wall_deadlines_essay.py));
  - [`title.txt`](title.txt);
  - [`abstract.txt`](abstract.txt) (205 words);
  - [`headlines.txt`](headlines.txt) (10);
  - [`PR-BODY.md`](PR-BODY.md).
- **The worked numbers.** Python ([`wall_deadlines_replay.py`](../../../../tests/probes/wolfram/wall_deadlines_replay.py)) and Wolfram both give `{True, True, {4, 4, 4, 4, 6, 6, 10, 10, 10, 10, 12, 12}, {2, 2, 4, 4, 6, 6, 8, 8, 10, 10, 12, 12}, True}`, and the prediction held.
- **nb1** (`b2d00126c35e223b598c3029998cfb63783f242dcb78e40d5a4a81bc704cf6bf`, 96,736 bytes):
  - built from [`wall_deadlines_notebook.wl`](../../../../tests/probes/wolfram/wall_deadlines_notebook.wl);
  - RESULT OK in 16 s;
  - every gate passes;
  - KernelChecked 87;
  - evidence `cited/local/wall-deadlines-nb1-20261110.tar.gz`, 30,216 bytes, SHA256 `d5b7ed4f2ec6bc135af76efcb912ebf6b8d2d02f0b05d49b6f7f4ab20fdad5c0`, read back byte-exact.
- **Post script.** [`post.sh`](post.sh). The dry run passes.

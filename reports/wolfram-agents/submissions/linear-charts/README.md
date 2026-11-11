# Every linear chart of the constrained starts is the free-bit chart (queue row S-24, Cloud's K-10, Theorem D)

**Release packet built; REVIEW-REQUEST to GPT (L1662); not posted.**
- **Mandate.** The owner said "Build K-10" on 10 November.
- **Route.** The route is the group-law lemma of the [feasibility map](../../../LOCAL-S24-THEOREM-D-FEASIBILITY-20261110.md) (L1661), which GPT carried by hand (GC2894).
- **Who built it.** A Local sub-agent wrote the module. Local rebuilt and checked it and read its statements. That is a self-check; GPT's read is the second read.
- **The earlier proof.** The six-step proof of Theorem D (swarm XP-2, triage §9.1) is not used.

## What the module proves

`Rule30LinearCharts` is core Lean, 564 lines, and imports only `Rule30Prize` and `Rule30ZeroBoundary`. It has eighteen headlines:
- **The group-law lemma:** `groupLaw_eq_xor`, `fibre_form`, `involution_Q`, `flip_invariant`, `descent_step`, `window_zero`, `q_white`.
- **The free-bit side:** `kk_Theta`, `fb_Theta`, `Theta_fb`, `kk_two_step`, `fb_shift`, `uld_Theta`, `uld_fb`.
- **The theorem:** `linear_chart_is_free_bit_chart`, `free_bit_chart_affine`, `free_bit_chart_iso`, `free_bit_chart_is_chart`.

Continuity is represented as uniform finite dependence. The step from continuity on compact domains to that, and the closedness of A, are not formalized and not used.

| Form | File | sha256 | Check |
|---|---|---|---|
| Portal | [`Rule30Submission.lean`](Rule30Submission.lean), from [`kit_to_portal.py`](../../../../tests/probes/swarm/sw02/block11/kit_to_portal.py) | `30f09bdd…` | pass at `5fb59158`: 83 declared, 105 constants, 18 headlines, standard axioms ([receipt](check-5fb59158.json)) |
| Kit | [`Rule30LinearCharts.lean`](Rule30LinearCharts.lean) | `ff694db1…` | pass at main `03a19bf`: 82 declared, 105 constants ([receipt](check-kit-03a19bf.json)). The kit branch `linear-charts` at `0178971` is local; [`kit-integration.patch`](kit-integration.patch) |

**Mutants.** All six were rejected ([output](../../../../tests/probes/swarm/sw02/block11/mutate_linear_charts.out)).

## Release artifacts

- **Texts:**
  - [`essay-prose.md`](essay-prose.md);
  - [`essay.md`](essay.md) (`5dac2c18…`, from [`assemble_linear_charts_essay.py`](../../../../tests/probes/wolfram/assemble_linear_charts_essay.py));
  - [`title.txt`](title.txt);
  - [`abstract.txt`](abstract.txt) (236 words, no markdown markup);
  - [`headlines.txt`](headlines.txt) (18);
  - [`PR-BODY.md`](PR-BODY.md).
- **The worked numbers.** Python ([`linear_charts_replay.py`](../../../../tests/probes/wolfram/linear_charts_replay.py)) and Wolfram both give `{{2, 1}, {64, 1}, {4, 2}, {8, 2}}`, and the prediction held. The first Python draft built the symmetry control wrongly. It also forced `Q(0, w) = 0`, which follows from the neutral element only under symmetry, and so gave `{2, 1}`. I fixed the candidate set before the cell was written; it was an encoding fault, not a mismatch.
- **nb1** (`6d7ee261bc0e68a78a338ee3540c7d717ecb03d6ae70e7bfa7c2559ee5ce6232`, 156,205 bytes):
  - built from [`linear_charts_notebook.wl`](../../../../tests/probes/wolfram/linear_charts_notebook.wl);
  - RESULT OK in 16 s;
  - every gate passes;
  - KernelChecked 105;
  - evidence `cited/local/linear-charts-nb1-20261111.tar.gz`, 51,553 bytes, SHA256 `e5ffdcd4896323d6a11878586b4a124dd4520461395bc58bd260943396af6ee0`, read back byte-exact.
- **Post script.** [`post.sh`](post.sh). The dry run passes.

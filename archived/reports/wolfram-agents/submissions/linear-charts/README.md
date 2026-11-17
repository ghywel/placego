# Every linear chart of the constrained starts is the free-bit chart (queue row S-24, Cloud's K-10, Theorem D)

**POSTED, Lean Verified (L1663):** [R30-20261111-0121a4](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261111-0121a4), checked 2026-11-11 00:18:30Z with 105 constants, eighteen headlines and standard axioms. Kit PR [WolframInstitute/Rule30PrizeKit#279](https://github.com/WolframInstitute/Rule30PrizeKit/pull/279) from `aa25ef3`, whose catalogue row adds GC2900's Wibmer credit. Posted from nb2 (`bfc7217030b4f1dcaab99c0a64712fb9e7cab574fb4498230e1473a3aa859ef7`, 157,161 bytes, KernelChecked 105; evidence `cited/local/linear-charts-nb2-20261111.tar.gz`, 52,449 bytes, SHA256 `9ba6d64c59a0ae2cb23e55372de5bfaf1dba39ab0ba1a11aa0a5c7207253d055`, read back exact), with GC2900's title, abstract and scope fixes; nb1 is superseded.

**Independent release review PASS (GC2900). Exact public nb2, source, text and kit PR pass GC2903.** The kit PR awaits maintainer merge. [Public delivery read](../../../GPT-S24-RELEASE-REVIEW-20261111.md#public-delivery-read).
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
| Kit | [`Rule30LinearCharts.lean`](Rule30LinearCharts.lean) | `ff694db1…` | pass at main `03a19bf`: 82 declared, 105 constants ([receipt](check-kit-03a19bf.json)). The kit branch `linear-charts` at `aa25ef3` is pushed as PR #279; [`kit-integration.patch`](kit-integration.patch) |

**Mutants.** All six were rejected ([output](../../../../tests/probes/swarm/sw02/block11/mutate_linear_charts.out)).

## Release artifacts

- **Texts:**
  - [`essay-prose.md`](essay-prose.md);
  - [`essay.md`](essay.md) (`2a7e255f…`, from [`assemble_linear_charts_essay.py`](../../../../tests/probes/wolfram/assemble_linear_charts_essay.py));
  - [`title.txt`](title.txt);
  - [`abstract.txt`](abstract.txt) (231 words, no markdown markup);
  - [`headlines.txt`](headlines.txt) (18);
  - [`PR-BODY.md`](PR-BODY.md).
- **The worked numbers.** Python ([`linear_charts_replay.py`](../../../../tests/probes/wolfram/linear_charts_replay.py)) and Wolfram both give `{{2, 1}, {64, 1}, {4, 2}, {8, 2}}`, and the prediction held. The first Python draft built the symmetry control wrongly. It also forced `Q(0, w) = 0`, which follows from the neutral element only under symmetry, and so gave `{2, 1}`. I fixed the candidate set before the cell was written; it was an encoding fault, not a mismatch.
- **nb1** (`6d7ee261bc0e68a78a338ee3540c7d717ecb03d6ae70e7bfa7c2559ee5ce6232`, 156,205 bytes):
  - built from [`linear_charts_notebook.wl`](../../../../tests/probes/wolfram/linear_charts_notebook.wl);
  - RESULT OK in 16 s;
  - every gate passes;
  - KernelChecked 105;
  - evidence `cited/local/linear-charts-nb1-20261111.tar.gz`, 51,553 bytes, SHA256 `e5ffdcd4896323d6a11878586b4a124dd4520461395bc58bd260943396af6ee0`, read back byte-exact.
- **Post script.** [`post.sh`](post.sh). The nb1 dry run passed for its original text. The current text requires nb2 and the four updated pins. [Release review](../../../GPT-S24-RELEASE-REVIEW-20261111.md).

**Kit review edit (L1665, 11 November):** at the maintainer's request on PR #279, the contributor and portal credit moved out of the Lean docstring and stays in the README row; commit `3130483`, kit form now `a0a90bb8…`. Docstring only: the build and the kit Check pass unchanged. The portal entry keeps its posted source.

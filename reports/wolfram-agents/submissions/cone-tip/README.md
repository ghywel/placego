# The cone tip of the zero-boundary left half (queue row S-17, Cloud's K-03)

**POSTED, Lean Verified (L1645):** [R30-20261110-b07808](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261110-b07808), checked 2026-11-10 20:10:05Z with 55 constants, seven headlines and standard axioms. Kit PR [WolframInstitute/Rule30PrizeKit#272](https://github.com/WolframInstitute/Rule30PrizeKit/pull/272) from `b3810dc`. Posted from nb2 (`75f005fe448f042eca67770f4a00d38f66447422cb9d6c6c5d74cf41c45b7439`, 85,713 bytes, KernelChecked 55; evidence `cited/local/cone-tip-nb2-20261110.tar.gz`, 28,046 bytes, SHA256 `903bb0b6c5bce339db224f0da1a1852183767d6ae8576ef8adf4755ee913362e`, read back exact), with GC2841's counting text; nb1 is superseded.

**GPT source/actual-nb1 read PASS GC2841; corrected-text nb2/pin/dry gates next; not posted.** [Complete review](../../../GPT-S17-RELEASE-REVIEW-20261110.md). The wall/chain and both non-affinity questions are carried. GPT clarified the finite uniform input distribution and the absolute Walsh bound; proof/source/driver bytes are unchanged. Local builds nb2, verifies original gates, updates notebook/abstract/essay pins and runs the fresh dry check; these complete standing conditional post/PR clearance without another permission round. Old nb1 and pins below are historical, superseded for release. Built from LN-02.1 as Cloud carried it (CL773; the triage report `reports/CLOUD-SW02-CARRY-TRIAGE-20261110.md` §11.1). Local wrote the module directly, with no sub-agent.

## What the module proves

`Rule30ConeTip` is core Lean, 262 lines, and imports only `Rule30ZeroBoundary`. It has seven headlines:
- `level_aff`, `diag`, `chain_flip`;
- `cone_tip`: the second difference in depths `t - 1` and `t` is `t - 1 mod 2`;
- `face_disagree`, `affine_second`, `tip_not_affine`.

The correlation bound `1/2` at even `t` is stated in words, as a counting consequence of `face_disagree`, and checked numerically for `t ≤ 12`. It is not formalised.

| Form | File | sha256 | Check |
|---|---|---|---|
| Portal | [`Rule30Submission.lean`](Rule30Submission.lean), from [`kit_to_portal.py`](../../../../tests/probes/swarm/sw02/block11/kit_to_portal.py) | `2def43f5…` | pass at `5fb59158`: 19 declared, 55 constants, 7 headlines, standard axioms ([receipt](check-5fb59158.json)) |
| Kit | [`Rule30ConeTip.lean`](Rule30ConeTip.lean) | see receipt | pass at main `03a19bf`: 19 declared, 55 constants ([receipt](check-kit-03a19bf.json)). The kit branch `cone-tip` at `343bec9` is local; [`kit-integration.patch`](kit-integration.patch) |

**Mutants.** All five were rejected ([output](../../../../tests/probes/swarm/sw02/block11/mutate_cone_tip.out)).

## Release artifacts

- **Texts:**
  - [`essay-prose.md`](essay-prose.md);
  - [`essay.md`](essay.md) (corrected text `7e49ade9…`, from [`assemble_cone_tip_essay.py`](../../../../tests/probes/wolfram/assemble_cone_tip_essay.py));
  - [`title.txt`](title.txt);
  - [`abstract.txt`](abstract.txt) (corrected text225words, no markdown markup);
  - [`headlines.txt`](headlines.txt) (7);
  - [`PR-BODY.md`](PR-BODY.md).
- **The worked numbers.** Python ([`cone_tip_replay.py`](../../../../tests/probes/wolfram/cone_tip_replay.py)) and Wolfram both give `{True, True, {1/2, 1/2, 1/2, 3/8, 7/16, 9/32, 3/16, 21/128, 17/128, 65/512, 95/1024}}`, and the prediction held.
- **nb1** (`3a904618a72409d97541116f99187fe93130f3b6687c53a919bc2350d1f54097`, 84,444 bytes):
  - built from [`cone_tip_notebook.wl`](../../../../tests/probes/wolfram/cone_tip_notebook.wl);
  - RESULT OK in 17 s;
  - every gate passes;
  - KernelChecked 55;
  - evidence `cited/local/cone-tip-nb1-20261110.tar.gz`, 27,718 bytes, SHA256 `eebd8e9b0f656d6bf53dc11c5b66d769ff8075a9497382c4ec842310a34ede89`, read back byte-exact.
- **Post script.** [`post.sh`](post.sh). The dry run passes.

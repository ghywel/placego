# The cut ether is off the single cell's edge cycle (queue row S-11)

**GC2808: complete source/text/actual-nb1/current-verifier read PASS; CLEARED for posting and kit PR.** [Release review](../../../GPT-S11-RELEASE-REVIEW-20261110.md). Standing owner permission applies; no new consent round is needed. No public post/Lean Verified outcome is claimed yet. Built from HX-2.1 as GPT carried it in [GC2803](../../../GPT-S11-CARRY-REVIEW-20261110.md): the depth `8` with phase `16` of every `c7cut N`, its frozen-ruler corollary, the stronger all-phase non-agreement, and the sharp **flush** thirteen-cell ether exclusion. The negative control at row `204` is in Lean too. HX-2.2 and the past census stay out.

## What the module proves

`Rule30EtherCutEdge` (core Lean). It imports `Rule30FrozenRuler` and `Rule30ZeroBoundaryBarriers`; both, with `Rule30Realization`, are byte-identical at the verifier's kit `5fb59158`. Eleven headlines: `cycle9`, `cycle13`, `off9_closed`, `cut_code_prefix`, `c7cut_depth`, `c7cut_frozen`, `c7cut_off_seed`, `c7cut_not_seed_row`, `seed_no_flush_ether`, `seed_flush_ether_sharp`, `seed_offset_ether_204`. The finite facts are `decide +kernel` on `k`-bit codes (`Tm`, `enc_T`), not Python results taken as given.

| Form | File | sha256 | Check |
|---|---|---|---|
| Portal | [`Rule30Submission.lean`](Rule30Submission.lean), from [`kit_to_portal.py`](../../../../tests/probes/swarm/sw02/block11/kit_to_portal.py) | `cc9e2a11c7c7af4f…` | pass at `5fb59158`: 41 declared, 88 constants, 11 headlines, standard axioms ([receipt](check-5fb59158.json)) |
| Kit | [`Rule30EtherCutEdge.lean`](Rule30EtherCutEdge.lean) | see receipt | pass at main `03a19bf`: 36 declared, 88 constants ([receipt](check-kit-03a19bf.json)); kit branch `ether-cut-edge` at `9d230d4`, local; [`kit-integration.patch`](kit-integration.patch) |

**Mutants.** All six rejected ([output](../../../../tests/probes/swarm/sw02/block11/mutate_ether_cut_edge.out)):
- `129` placed on the cycle;
- depth `9`;
- twelve cells instead of thirteen (false by the sharp witness);
- a thirteen-bit cycle of `63`;
- row `204`'s word at phase `3`;
- the sharp witness at time `54`.

## Release artifacts

- **Texts:** [`essay-prose.md`](essay-prose.md), [`essay.md`](essay.md) (`380d2df9…`, from [`assemble_ether_cut_edge_essay.py`](../../../../tests/probes/wolfram/assemble_ether_cut_edge_essay.py)), [`title.txt`](title.txt), [`abstract.txt`](abstract.txt) (214 words), [`headlines.txt`](headlines.txt) (11), [`PR-BODY.md`](PR-BODY.md).
- **Worked numbers.** Computed on actual rule 30 rows, in Python ([`ether_cut_edge_replay.py`](../../../../tests/probes/wolfram/ether_cut_edge_replay.py), with its prediction header) and in Wolfram. Both give `{32, False, 64, {129, 129, 129, 129, 129, 129}, True, 12, 55, True}`, and the prediction held.
- **nb1** ([`ether_cut_edge_notebook.wl`](../../../../tests/probes/wolfram/ether_cut_edge_notebook.wl), at `5fb59158`):
  - SHA256 `167a9c37c09559460061bb186db1cfcf45614664c14d5f2af12fe7769e56bb3b`, 109,034 bytes.
  - RESULT OK in 15.8 s.
  - All gates pass, and the notebook kernel-checks all 88 declarations.
  - Evidence: `cited/local/ether-cut-edge-nb1-20261110.tar.gz`, 35,746 bytes, SHA256 `07b2b14bf65e2b4e3d7b7f044e09bc0138d7d7f669880c7ce27b9f221c37a914`, read back byte-exact.
- **Post script.** [`post.sh`](post.sh): the S-05 wrapper with new pins and 11 headlines. The dry run passes at `5fb59158`, image 18.

## Prior art

- **The kit's machinery.** `Rule30FrozenRuler` (the edge map of Coven, Pivato and Yassawi; the frozen ruler, from PR 42) and `Rule30ZeroBoundaryBarriers` (`c7`, `c7cut`) are used, not reproved.
- **rule30-open.** `lhallee/rule30-open`'s `SeedPastPeriods` has the single cell's nonfinite past, and it is not claimed here.
- **What is new.** The cut's depth and phase, the all-phase separation, and the sharp flush exclusion, which GC2803 searched for and did not find in the kit, on the portal or in the PRs.

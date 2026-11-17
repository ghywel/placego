# Zero-wall diagonals, bounded lag and the factor complexity of a surviving row's free word (queue row S-12)

**POSTED, Lean Verified (L1639):** [R30-20261110-144e6e](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261110-144e6e), checked 2026-11-10 15:24:15Z with 324 constants, twenty headlines and standard axioms. Kit PR [WolframInstitute/Rule30PrizeKit#269](https://github.com/WolframInstitute/Rule30PrizeKit/pull/269) from `1030f1e`. Posted from nb2 (`342100765d82656e6f35f78855311272f484975a3689aa187fa09201b648f0fa`, 238,925 bytes, KernelChecked 324; evidence `cited/local/zero-wall-diagonals-nb2-20261110.tar.gz`, 82,867 bytes, SHA256 `1e55c163930fe1169b926b893ec6f120105bfabeeae4237cfb72997cfc1d0b34`, read back exact), with GC2823's corrected wording; nb1 is superseded.

**GC2823 mathematical/source read PASS; corrected nb2 routine gates pending.** [Complete carrying/release review and exact next steps](../../../GPT-S12-RELEASE-REVIEW-20261110.md). All declaration/proof tokens unchanged; corrected nonzero/base-black/sufficient-guard/arbitrarily-large wording. The current corrected portal SHA256 is `2e88c60d653b267a26c12528f9f2a50d963f2baccf23bc1a415f950afd6d08f7`, abstract `61c841f78c87cf4e9f2da50c15ee7a7a433c8c9bfeb6bc13b5a5948bd7fd49ac`, essay `cc9d27f1f1c8858a5695dac54b2fd12de451149718d04341bd8150ac6ebb962c`. Local rebuilds/rechecks both forms, uses the unchanged driver for nb2, updates only notebook/source/abstract/essay wrapper pins and runs a current dry/pre-post source check. Those gates complete conditional posting/PR clearance under standing consent; no new owner or hand-proof approval needed. **The original nb1/Check record below is historical and is not permission to post nb1.**

**RELEASE PACKET BUILT (L1637), not posted: GPT's carrying read of the formal source and release read requested.** Built from CP-3.2 as GPT carried it ([GC2702](../../../GPT-BLOCK6-CARRY-REVIEW-20261106.md)). It follows GPT's tail-recurrence plan ([GC2817](../../../GPT-S12-DIAGONAL-PLAN-20261110.md)) and explicit word witnesses ([GC2819](../../../GPT-S12-WORD-WITNESSES-20261110.md)), whose four flagged steps Local carried (L1634, L1635). A Local sub-agent wrote the formal source, and Local read and checked it; GPT's read is the second read. The near-square side claim is excluded.

## What the module proves

`Rule30ZeroWallDiagonals` is core Lean, 1,242 lines, and imports `Rule30LeftUnbounded` and `Rule30ZeroBoundary`. It has twenty headlines; see [`headlines.txt`](headlines.txt) and the PR body. The main result is `freeWord_complexity`: for `FinSupp L` and `InX L`, every `K` has `N` with `n + K < factorCount (freeWord L) n` for all `n ≥ N`. It is conditional, since such rows exist only if `Q01` fails. The moving-edge diagonal package requires a nonzero finite row with a last black cell at positive depth; `E_entry` itself needs no support/nonzero hypothesis. The abstract `tail_*` lemmas require all of `TailLeft`, including both eventually black base coordinates.

| Form | File | sha256 | Check |
|---|---|---|---|
| Portal | [`Rule30Submission.lean`](Rule30Submission.lean), from [`kit_to_portal.py`](../../../../tests/probes/swarm/sw02/block11/kit_to_portal.py) | `3d36e906…` | pass at `5fb59158`: 106 declared, 324 constants, 20 headlines, standard axioms ([receipt](check-5fb59158.json)) |
| Kit | [`Rule30ZeroWallDiagonals.lean`](Rule30ZeroWallDiagonals.lean) | see receipt | pass at main `03a19bf`: 98 declared, 324 constants ([receipt](check-kit-03a19bf.json)). The kit branch `zero-wall-diagonals` at `e9acaba` is local; [`kit-integration.patch`](kit-integration.patch) |

**Mutants.** All six were rejected ([output](../../../../tests/probes/swarm/sw02/block11/mutate_zero_wall_diagonals.out)).

## Release artifacts

- **Texts:**
  - [`essay-prose.md`](essay-prose.md);
  - [`essay.md`](essay.md) (`fe17e5d4…`, from [`assemble_zero_wall_diagonals_essay.py`](../../../../tests/probes/wolfram/assemble_zero_wall_diagonals_essay.py));
  - [`title.txt`](title.txt);
  - [`abstract.txt`](abstract.txt) (205 words, no carets);
  - [`headlines.txt`](headlines.txt) (20);
  - [`PR-BODY.md`](PR-BODY.md).
- **The worked numbers.** Python ([`zero_wall_diagonals_replay.py`](../../../../tests/probes/wolfram/zero_wall_diagonals_replay.py)) and Wolfram both give `{True, True, True, {1, 1, 1, 2, 1, 2, 2, 1, 4, 1, 4}, True}`, and the prediction held.
- **nb1** (`921e668a8c44ed736286018eec1c7b29c26f564ab8133f87c65398463a5bed74`, 238,495 bytes):
  - built from [`zero_wall_diagonals_notebook.wl`](../../../../tests/probes/wolfram/zero_wall_diagonals_notebook.wl);
  - RESULT OK in 14 s;
  - every gate passes;
  - KernelChecked 324;
  - evidence `cited/local/zero-wall-diagonals-nb1-20261110.tar.gz`, 82,385 bytes, SHA256 `f70228dd87eb662fb6fcf99381426be36a939fba5a843b891a64776206888432`, read back byte-exact.
- **Post script.** [`post.sh`](post.sh). The dry run passes.

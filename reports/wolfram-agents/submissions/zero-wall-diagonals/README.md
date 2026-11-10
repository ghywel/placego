# Zero-wall diagonals, bounded lag and the factor complexity of a surviving row's free word (queue row S-12)

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

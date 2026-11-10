# The immortal rows of the alternating 90/150 hybrid with a white wall (queue row S-08, hybrid half)

**CLEARED for Local's single post and kit PR, GPT GC2822:** [complete independent carrying and actual-byte release read PASS](../../../GPT-S08-HYBRID-RELEASE-REVIEW-20261110.md). Use the unchanged nb1 below; all seven current dry pins pass, no rebuild or fresh owner consent required. Not yet posted; public status is a separate next check. **Original L1636 build record:** Built from BR-3.1 as GPT carried it ([GC2804](../../../GPT-S08-CARRY-REVIEW-20261110.md)), by the decimation-semiconjugacy route of L1632, which GPT carried in GC2815. The formal source was written by a Local sub-agent and then read and checked by Local; a sub-agent's check counts as a self-check, so GPT's read is the second read.

## What the module proves

`Rule30HybridWall` is core Lean, 1,827 lines, and imports only `Rule30Prize`. It has twenty headlines; see [`headlines.txt`](headlines.txt) and the PR body. The main results:
- the classification, in cells (`immortal_iff_bitFam_anyWall`, `immortal_iff_famRow`) and in coefficients (`immortal_real_iff`);
- the bijection count (`immortal_iff_param`);
- the small cases (`immortal_width_six`, `not_immortal_width_one`);
- aperiodicity (`col_not_eventually_periodic`, `immortal_odd_word_not_eventually_periodic`);
- the semiconjugacy (`D_P_P`, `psi_even_time`, `even_time_constant`).

The count `2^(W/2 - 1)` is formal as a bijection. Its value is formal only for `W ≤ 12`, by kernel evaluation.

**A repair to L1632, found in formalization.** `A^{4j} = S^{4j} + S^{-4j}` holds only when `j` is a power of 2; for example, `A^12` is the row `e4 + e12` (`real_A_pow_twelve`). The cell family and the coefficient family agree as sets, through the bijective change of parameters in `real_afam`, not term by term.

| Form | File | sha256 | Check |
|---|---|---|---|
| Portal | [`Rule30Submission.lean`](Rule30Submission.lean), from [`kit_to_portal.py`](../../../../tests/probes/swarm/sw02/block11/kit_to_portal.py) | `61278b18…` | pass at `5fb59158`: 195 declared, 445 constants, 20 headlines, standard axioms ([receipt](check-5fb59158.json)) |
| Kit | [`Rule30HybridWall.lean`](Rule30HybridWall.lean) | see receipt | pass at main `03a19bf`: 188 declared, 445 constants ([receipt](check-kit-03a19bf.json)). The kit branch `hybrid-wall` at `3f4aa00` is local; [`kit-integration.patch`](kit-integration.patch) |

**Mutants.** All six were rejected ([output](../../../../tests/probes/swarm/sw02/block11/mutate_hybrid_wall.out)).

## Release artifacts

- **Texts:**
  - [`essay-prose.md`](essay-prose.md);
  - [`essay.md`](essay.md) (`37abb1a4…`, from [`assemble_hybrid_wall_essay.py`](../../../../tests/probes/wolfram/assemble_hybrid_wall_essay.py));
  - [`title.txt`](title.txt);
  - [`abstract.txt`](abstract.txt) (213 words);
  - [`headlines.txt`](headlines.txt) (20);
  - [`PR-BODY.md`](PR-BODY.md).
- **Abstract.** The first notebook build failed its abstract gate. The markdown converter read the two carets in `A^2)p(A^4` as superscript delimiters, so the abstract now uses Unicode superscripts and no carets. That failed build is kept outside git.
- **The worked numbers.** Python ([`hybrid_wall_replay.py`](../../../../tests/probes/wolfram/hybrid_wall_replay.py)) and Wolfram both give `{{0, 1, 1, 2, 2, 4, 4, 8, 8, 16, 16, 32}, {3, 11, 53, 61}, True, True}`, and the prediction held.
- **nb1** (`3f5f04d90676f4fdd9746160356983f7e746785a14cf351ebf9018e162fd2ac8`, 268,770 bytes):
  - built from [`hybrid_wall_notebook.wl`](../../../../tests/probes/wolfram/hybrid_wall_notebook.wl);
  - RESULT OK in 43 s;
  - every gate passes (six outputs, no messages, icon, abstract, twenty axiom sets);
  - KernelChecked 445;
  - evidence `cited/local/hybrid-wall-nb1-20261110.tar.gz`, 90,927 bytes, SHA256 `872235b2570c9315970c4c8e1b3dfcdd34e1b71fab81c84643c7884423e2d568`, read back byte-exact.
- **Post script.** [`post.sh`](post.sh). The dry run passes.

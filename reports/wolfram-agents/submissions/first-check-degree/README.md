# The first check: weight n mod 2, degree n or n - 1, and the other phase always odd (queue row S-06)

**RELEASE PACKET BUILT (L1630), not posted: GPT's release read requested.** Built from XP-1.1 as GPT carried it ([GC2807](../../../GPT-S06-CARRY-REVIEW-20261110.md)), with the repaired guards: the Walsh exception at `n = 1`, and the second coefficient for the degree at even `n`. It reuses `Rule30FirstChecks.first_check_count` for the survivor congruence. GPT's one-slice proof for the other phase is added and formalized. The masking step to Berzai's alternating centre is a comparison in the essay only. No spectral or forgetting claims.

## What the module proves

`Rule30FirstCheckDegree` is core Lean and imports only `Rule30FirstChecks`. It has eleven headlines:
- `diag`, `top_succ`;
- `top_coefficient`, `omit_coefficient`;
- `anf_expansion`, `check_degree`;
- `ones_parity`, `first_check_parity`;
- `walsh_mod_four`, `walsh_one`;
- `other_phase_odd`.

| Form | File | sha256 | Check |
|---|---|---|---|
| Portal | [`Rule30Submission.lean`](Rule30Submission.lean), from [`gen_first_check_degree_portal.py`](../../../../tests/probes/swarm/sw02/block11/gen_first_check_degree_portal.py), with a byte copy of `Rule30FirstChecks`'s body, which the verifier's kit lacks | `9f6d9545…` | pass at `5fb59158`: 120 declared, 243 constants, 11 headlines, standard axioms ([receipt](check-5fb59158.json)) |
| Kit | [`Rule30FirstCheckDegree.lean`](Rule30FirstCheckDegree.lean), 622 lines | see receipt | pass at main `03a19bf`: 63 declared, 145 constants ([receipt](check-kit-03a19bf.json)). The kit branch `first-check-degree` at `d739f20` is local; [`kit-integration.patch`](kit-integration.patch) |

**Mutants.** All seven were rejected ([output](../../../../tests/probes/swarm/sw02/block11/mutate_first_check_degree.out)).

## Release artifacts

- **Texts:**
  - [`essay-prose.md`](essay-prose.md);
  - [`essay.md`](essay.md) (`843eb792…`, from [`assemble_first_check_degree_essay.py`](../../../../tests/probes/wolfram/assemble_first_check_degree_essay.py));
  - [`title.txt`](title.txt);
  - [`abstract.txt`](abstract.txt) (200 words);
  - [`headlines.txt`](headlines.txt) (11);
  - [`PR-BODY.md`](PR-BODY.md).
- **The worked numbers.** Python ([`first_check_degree_replay.py`](../../../../tests/probes/wolfram/first_check_degree_replay.py)) and Wolfram both give `{True, True, {1,1,3,3,5,5,7,7,9,9}, {1,2,3,4,17,38}, {0,0,2,0,2,0,2,0,2,0,2,0}, True}`, and the prediction held.
- **nb1** (`2a904097144b2f81b4fc5f7bd57a14cf69d1cff9f0d56e11728126d31e90ecbf`, 214,078 bytes):
  - built from [`first_check_degree_notebook.wl`](../../../../tests/probes/wolfram/first_check_degree_notebook.wl);
  - RESULT OK in 18.6 s;
  - every gate passes (six outputs, no messages, icon, abstract, eleven axiom sets);
  - KernelChecked 243;
  - evidence `cited/local/first-check-degree-nb1-20261110.tar.gz`, 70,235 bytes, SHA256 `2d5068a86fdc7be301e625f95f522cdbc398ed5f2081e7ba58fa27f7b2cab652`, read back byte-exact.
- **Post script.** [`post.sh`](post.sh). The dry run passes.

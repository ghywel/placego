# A binary radius-two left-permutive rule with an exactly alternating column (queue row S-07)

**RELEASE PACKET BUILT (L1626), not posted: GPT's release read requested.** Built from XP-4.1 as GPT carried it ([GC2804](../../../GPT-S07-CARRY-REVIEW-20261110.md)), using GPT's finite reflection proof, which Local carried in L1625. The scope is binary `N(p, q)`, the seed `{0, 2}`, the exact alternating columns `-2` and `-1`, and the column-0 translate. Extra seeds, chaos, the Galois sharpening and the radius-one census stay out.

## What the module proves

`Rule30RadiusTwoClock` is core Lean and imports only `Rule30Prize`. It has seven headlines:
- `rule_facts`;
- `z_frontier`;
- `row_formula`;
- `d_band`;
- `z_clock`;
- `clock`;
- `column0_alternates`.

| Form | File | sha256 | Check |
|---|---|---|---|
| Portal | [`Rule30Submission.lean`](Rule30Submission.lean), from [`kit_to_portal.py`](../../../../tests/probes/swarm/sw02/block11/kit_to_portal.py) | `3df4ff2995b5c21b…` | pass at `5fb59158`: 52 declared, 211 constants, 7 headlines, standard axioms ([receipt](check-5fb59158.json)) |
| Kit | [`Rule30RadiusTwoClock.lean`](Rule30RadiusTwoClock.lean) | see receipt | pass at main `03a19bf`: 46 declared, 211 constants ([receipt](check-kit-03a19bf.json)). The kit branch `radius-two-clock` at `9bcfee8` is local; [`kit-integration.patch`](kit-integration.patch) |

**Mutants.** All five were rejected ([output](../../../../tests/probes/swarm/sw02/block11/mutate_radius_two_clock.out)).

## Release artifacts

- **Texts:**
  - [`essay-prose.md`](essay-prose.md);
  - [`essay.md`](essay.md) (`ea020887…`, from [`assemble_radius_two_clock_essay.py`](../../../../tests/probes/wolfram/assemble_radius_two_clock_essay.py));
  - [`title.txt`](title.txt);
  - [`abstract.txt`](abstract.txt) (203 words);
  - [`headlines.txt`](headlines.txt) (7);
  - [`PR-BODY.md`](PR-BODY.md).
- **The worked numbers.** Python ([`radius_two_clock_replay.py`](../../../../tests/probes/wolfram/radius_two_clock_replay.py)) and Wolfram both give `{True, 14, 0, True, True}`, and the prediction held.
- **nb1** (`0b17cb6befd7e75c90c1d0230964a6e5e28fc4c06863f2668e6978a5da8e9628`, 116,857 bytes):
  - RESULT OK in 21.6 s;
  - every gate passes;
  - KernelChecked 211;
  - evidence `cited/local/radius-two-clock-nb1-20261110.tar.gz`, 35,574 bytes, SHA256 `9d2731a29f19f1d7d38f165aadeb9d9ff76e84954b71165aa3559cbf5fb460ae`, read back byte-exact.
- **Post script.** [`post.sh`](post.sh). The dry run passes.

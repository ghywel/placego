# A planted survivor: rule 30's survival table with one row added (queue row S-08, plant half)

**GC2812 actual public/gate follow-up PASS:** [Read](../../../GPT-S08-PUBLIC-READ-20261110.md). Corrected nb2/source match public R30-20261110-7a4a0d, actual Lean Verified13:17:45Z,266constants/tenheads; PR260 awaits maintainers. No repost.

**POSTED, Lean Verified (L1629):** [R30-20261110-7a4a0d](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261110-7a4a0d), checked 2026-11-10 13:17:45Z with 266 constants, ten headlines and standard axioms. Kit PR [WolframInstitute/Rule30PrizeKit#260](https://github.com/WolframInstitute/Rule30PrizeKit/pull/260) from `b51eb34`. Posted from nb2 (`a02333f1074dd7ed395f8c806e22c1465c0548abc44d19a704fbf0f5da7e430c`, 150,317 bytes, KernelChecked 266; evidence `cited/local/planted-survivor-nb2-20261110.tar.gz`, 51,272 bytes, SHA256 `7a0de61b4f027387d902dc73ba77ace12f2118ef2722f44c3d5ee6b8d0cd0935`, read back byte-exact), with GC2811's corrected comments, abstract and essay; nb1 is superseded. Both source forms passed Check again first (266 constants, ten headlines).

**GC2811: complete source/release read PASS, conditional on the routine corrected nb2 gates.** [Review](../../../GPT-S08-RELEASE-REVIEW-20261110.md). Declaration/proof code and ten headlines are unchanged. Corrected finite-table scope and nonincreasing-width wording change the source comments, abstract and essay; old nb1 is superseded. Local reruns both source Checks, builds corrected nb2 with the unchanged driver, refreshes only notebook/source/abstract/essay pins and passes the fresh verifier dry guard. Those routine gates complete conditional clearance under standing posting/PR consent, with no further owner or mathematical approval round.

**RELEASE PACKET BUILT (L1628), not posted: GPT's release read requested.** Built from BR-3.2 as GPT carried it ([GC2804](../../../GPT-S08-CARRY-REVIEW-20261110.md)), with GPT's two repairs: `psi` acts on rows and the stripe together, and survival is inclusive (every even check of depth `1` through `t`). The scope is the exact table identity and the finite-state witness. The hybrid half of S-08 (BR-3.1, the 90/150 classification) is not in this packet.

## What the module proves

`Rule30PlantedSurvivor` is core Lean and imports only `Rule30ZeroBoundaryBarriers`. It has ten headlines:
- `psi_psiInv`, `psiInv_psi`;
- `psi_stripe`;
- `psiInv_fin`;
- `Tn_eq`;
- `T_finite`, `T_zero`;
- `T_fixed`, `fixed_survives`;
- `survival_table`.

| Form | File | sha256 | Check |
|---|---|---|---|
| Portal | [`Rule30Submission.lean`](Rule30Submission.lean), from [`kit_to_portal.py`](../../../../tests/probes/swarm/sw02/block11/kit_to_portal.py) | `b6cf4a78…` | pass at `5fb59158`: 91 declared, 266 constants, 10 headlines, standard axioms ([receipt](check-5fb59158.json)) |
| Kit | [`Rule30PlantedSurvivor.lean`](Rule30PlantedSurvivor.lean) | see receipt | pass at main `03a19bf`: 79 declared, 266 constants ([receipt](check-kit-03a19bf.json)). The kit branch `planted-survivor` at `c500184` is local; [`kit-integration.patch`](kit-integration.patch) |

**Mutants.** All five were rejected ([output](../../../../tests/probes/swarm/sw02/block11/mutate_planted_survivor.out)).

## Release artifacts

- **Texts:**
  - [`essay-prose.md`](essay-prose.md);
  - [`essay.md`](essay.md) (`14b27c1a…`, from [`assemble_planted_survivor_essay.py`](../../../../tests/probes/wolfram/assemble_planted_survivor_essay.py));
  - [`title.txt`](title.txt);
  - [`abstract.txt`](abstract.txt) (206 words);
  - [`headlines.txt`](headlines.txt) (10);
  - [`PR-BODY.md`](PR-BODY.md).
- **The worked numbers.** Python ([`planted_survivor_replay.py`](../../../../tests/probes/wolfram/planted_survivor_replay.py)) and Wolfram both give `{True, 495, {0,0,0,1,1,1,1,1,1,0,0}, True, True}`, and the prediction held.
- **nb1** (`8670737a04fae33744eafe2d1712aa19187dcf244d9f8743f47c76beeb238db2`, 149,053 bytes):
  - RESULT OK in 14.6 s;
  - every gate passes (six outputs, no messages, icon, abstract, axioms);
  - KernelChecked 266;
  - evidence `cited/local/planted-survivor-nb1-20261110.tar.gz`, 50,565 bytes, SHA256 `f519baa08f79733d2e3ad3327a7af2a77b73ed69c383ad841a1a0ac151d405d3`, read back byte-exact.
- **Post script.** [`post.sh`](post.sh). The dry run passes.

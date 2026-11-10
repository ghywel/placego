# The wall deadlines of rules 90 and 150 (queue row S-18, Cloud's K-05)

**POSTED, Lean Verified (L1646):** [R30-20261110-c20b0a](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261110-c20b0a), checked 2026-11-10 20:32:22Z with 87 constants, ten headlines and standard axioms. Kit PR [WolframInstitute/Rule30PrizeKit#273](https://github.com/WolframInstitute/Rule30PrizeKit/pull/273) from `9168167`. Posted from nb2 (`986646fe7e2e8d4767342938b41c5ebcd1a45b5306f0bbfec32e5a5c7e91b939`, 98,121 bytes, KernelChecked 87; evidence `cited/local/wall-deadlines-nb2-20261110.tar.gz`, 30,199 bytes, SHA256 `e54adea3d716009e8ccc98295acbe424eb9482594fe4fef6b287cf07d97ccd73`, read back exact), with GC2844's comment and count-range fixes; nb1 is superseded.

**GPT exact public-byte follow-up PASS GC2849; delivery complete.** [Public read](../../../GPT-S18-PUBLIC-READ-20261110.md); [prepost carrying review](../../../GPT-S18-RELEASE-REVIEW-20261110.md). Fixed only the module introduction's first-white terminology and the essay's count range (`2n<W`); declaration/proof body unchanged. Local completed both corrected-source Checks, updated the kit branch, rebuilt nb2 with unchanged driver/original gates, updated three pins and passed current dry/old-nb1 rejection. GPT independently matched public nb2/source/title/abstract/headlines and PR273's head. Maintainers own merge; no release gate/repost remains. Old nb1 below is historical. BR-6.1/Cloud triage§10(a)/(b); Local wrote the module directly. Proof-size context is not formalised; Cloud's separate hardness3 addition remains its original PROOF-SKETCH.

## What the module proves

`Rule30WallDeadlines` is core Lean, 333 lines, and imports only `Rule30ZeroBoundary`. It has ten headlines: `zr_or_eq_zrow`, `fib2_mod`, `odd90`, `kstar_spec`, `deadline90`, `sharp90`, `two_step150`, `odd150`, `deadline150` and `sharp150`.

The sharpness statement for rule 90 uses `2 * s + 2 ≤ kstar W` rather than `2 * s ≤ kstar W - 2`. With natural subtraction the latter would be false at `W = 0`, where `kstar 0 = 1`.

| Form | File | sha256 | Check |
|---|---|---|---|
| Portal | [`Rule30Submission.lean`](Rule30Submission.lean), from [`kit_to_portal.py`](../../../../tests/probes/swarm/sw02/block11/kit_to_portal.py) | `6afbb54f…` | pass at `5fb59158`: 27 declared, 87 constants, 10 headlines, standard axioms ([receipt](check-5fb59158.json)) |
| Kit | [`Rule30WallDeadlines.lean`](Rule30WallDeadlines.lean) | see receipt | pass at main `03a19bf`: 26 declared, 87 constants ([receipt](check-kit-03a19bf.json)). The kit branch `wall-deadlines` at `9168167` is pushed as PR #273; [`kit-integration.patch`](kit-integration.patch) |

**Mutants.** All six were rejected ([output](../../../../tests/probes/swarm/sw02/block11/mutate_wall_deadlines.out)).

## Release artifacts

- **Texts:**
  - [`essay-prose.md`](essay-prose.md);
  - [`essay.md`](essay.md) (corrected `5d0d8cff…`, from [`assemble_wall_deadlines_essay.py`](../../../../tests/probes/wolfram/assemble_wall_deadlines_essay.py));
  - [`title.txt`](title.txt);
  - [`abstract.txt`](abstract.txt) (205 words);
  - [`headlines.txt`](headlines.txt) (10);
  - [`PR-BODY.md`](PR-BODY.md).
- **The worked numbers.** Python ([`wall_deadlines_replay.py`](../../../../tests/probes/wolfram/wall_deadlines_replay.py)) and Wolfram both give `{True, True, {4, 4, 4, 4, 6, 6, 10, 10, 10, 10, 12, 12}, {2, 2, 4, 4, 6, 6, 8, 8, 10, 10, 12, 12}, True}`, and the prediction held.
- **nb1** (`b2d00126c35e223b598c3029998cfb63783f242dcb78e40d5a4a81bc704cf6bf`, 96,736 bytes):
  - built from [`wall_deadlines_notebook.wl`](../../../../tests/probes/wolfram/wall_deadlines_notebook.wl);
  - RESULT OK in 16 s;
  - every gate passes;
  - KernelChecked 87;
  - evidence `cited/local/wall-deadlines-nb1-20261110.tar.gz`, 30,216 bytes, SHA256 `d5b7ed4f2ec6bc135af76efcb912ebf6b8d2d02f0b05d49b6f7f4ab20fdad5c0`, read back byte-exact.
- **Post script.** [`post.sh`](post.sh). The dry run passes.

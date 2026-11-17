# The free-middle theorem (queue row S-13)

**GC2808: exact public notebook/source/text and actual Lean Verified check confirmed.** [Public-byte review](../../../GPT-S13-S05-PUBLIC-READ-20261110.md). Kit PR integration awaits the maintainers; do not repost.

**POSTED and Lean Verified (L1624):** [R30-20261110-a6ada9](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261110-a6ada9). It was submitted at 11:55 UTC under the owner's standing permission, after GC2805's gates: Check was rerun at the corrected bytes (portal `fee006a2…`, kit `f0921510…`; 405 constants, 8 headlines), nb2 was built with the unchanged driver `ab07295c…` (`ee74b087a235974473567983498d07ebb5ab0715053dbb712c66c1213eb77147`, 238,909 bytes, RESULT OK, KernelChecked 405), exactly four pins were changed, the dry run passed, and a fresh `known_find --new` showed nothing added. The portal check passed: kernel replay, standard axioms only. Kit PR [WolframInstitute/Rule30PrizeKit#254](https://github.com/WolframInstitute/Rule30PrizeKit/pull/254): one commit (`b13d484`) on main `03a19bf`, three files; [`kit-integration-filled.patch`](kit-integration-filled.patch). Evidence: `cited/local/free-middle-nb2-20261110.tar.gz`, 83,913 bytes, SHA256 `910fc2c267cb48e4cb3b60927fa28192fb6a07f1baa38b38d81192e638a50d65`, read back byte-exact.


**GC2805: complete Lean read PASS; corrected text ready, nb2 refresh required.** [Full review and routine release gates](../../../GPT-S13-RELEASE-REVIEW-20261110.md). The old nb1 and old pins below are historical and must not be posted. Conditional clearance completes when Local reruns Check at corrected comment bytes, builds/pins coherent nb2 and passes the reviewed dry-run gates; standing owner authorization then covers posting/PR without another consent round.

**Historical L1621 packet:** Built under the owner's standing permission of 10 November (L1619) from XP-3.1 as GPT carried it in [GC2702 §2](../../../GPT-BLOCK6-CARRY-REVIEW-20261106.md#2-xp31-free-middle-survives-the-review), with its guards: integer densities, `u(W) → ∞`, the linear lower bound and fixed boundary windows. The B2+ claim stays out.

## What the module proves

`Rule30FreeMiddle` (core Lean; the kit form imports `Rule30ZeroBoundaryBarriers` and `Rule30LocalConservation`, both byte-identical at the verifier's kit `5fb59158`, so the portal form imports them too and carries nothing).
- `Late u s W`: a finite zero-wall row of width `W` whose double step survives and which passes every even check through `W - u W`. `ToInfty u`: `u` tends to infinity.
- `rank w e m β h s W = β W (wallW w s) (edgeW e s W) + dens m h s W`: any integer function of (width, wall window, edge window) plus an integer density of `m`-cell windows.
- `no_local_ranking_late`: the kit's B2 (`no_local_ranking`) for the late population: no function of (width, wall, edge) is nonnegative on it and strictly descends along its double steps.
- `free_middle`: a rank bounded below by `-K W` and nonincreasing along late double steps has `h` conserved on every closed walk (the kit's `CyclicConserved`); `free_middle_coboundary`: so `h` is a constant plus a shift coboundary.
- `rank_local`: then, for windows of at least `m - 1` cells, the rank is a function of (width, wall, edge).
- `no_additive_ranking_late`: no rank of this form is nonnegative and strictly descending on the late population.
- `lower_bound_needed`: popcount minus `W²` strictly descends on every surviving double step, and popcount is not a coboundary, so the lower bound cannot be dropped.
- Machinery: `wsum_rho` (balance: the four-step rise summed over all cyclic words of length `N ≥ m + 8` is zero), `cyclic_conserved_of_rho` (cyclic words to the kit's closed walks), `rise_mkRow` (the planted row), `rho_nonpos_of_descent` (the chain).

| Form | File | sha256 | Check |
|---|---|---|---|
| Portal | [`Rule30Submission.lean`](Rule30Submission.lean) (from the kit form by [`gen_free_middle_portal.py`](../../../../tests/probes/swarm/sw02/block11/gen_free_middle_portal.py)) | `fee006a2e070ae38…` (header-only correction; Check rerun pending) | historical pre-correction pass at the verifier's kit `5fb59158`: 129 declared, 405 constants replayed, 8 headlines, standard axioms, no new axioms; build plus Check 3.4 s, 0.97 GB ([receipt](check-5fb59158.json)) |
| Kit | [`Rule30FreeMiddle.lean`](Rule30FreeMiddle.lean), 1,327 lines | `f092151067a727e0…` (header-only correction; Check rerun pending) | historical pre-correction pass at kit main `03a19bf`: 128 declared, 405 constants, 8 headlines; module build 2.0 s, Check 5.0 s, 0.97 GB ([receipt](check-kit-03a19bf.json)); kit branch `free-middle` local, not pushed; [`kit-integration.patch`](kit-integration.patch) (the import and the catalogue row; `PORTAL-ID` to fill) |

**Mutants.** All eight proof/typing mutations were compiler-rejected; rejection alone does not refute every mutated mathematical statement. Local tested ([output](../../../../tests/probes/swarm/sw02/block11/mutate_free_middle.out), [script](../../../../tests/probes/swarm/sw02/block11/mutate_free_middle.py)): a quadratic lower bound (false, by the popcount example), balance from `N ≥ m + 7`, an image count of 255, a whole-row horizon, an all-black prefix, a linear `W` in the counterexample (false, by `free_middle`), windows of `m - 2` cells, and B2 without `u → ∞`.

## Prior art and scope

- Kit: `Rule30ZeroBoundaryBarriers.no_local_ranking` (B2 for all surviving double steps) and `Rule30LocalConservation.cyclic_conserved_iff_shift_coboundary` (the classification), both used, not reproved. `known_find` for `no_local_ranking`, `RankCert`, `CyclicConserved`, `free middle` (kit `03a19bf6`, portal 10:49:54Z, 20 open PRs): only those kit modules and `Rule30ProductParity.CyclicConserved`, a different notion. Cloud's CL752 comparison: the free-middle theorem CLEAR; `rule30-open`'s conservation-laws note and the kit's barriers PARTLY cover the object.
- Literature: balance for permutive cellular automata (Hedlund 1969) and absence of conservation laws (Hattori and Takesue 1991) are classical; the kit cites the latter.
- Not claimed: real or nonlinear densities, bounded margins `u`, rankings with memory, `Q01`, Problem 1. The late population includes rows that are not the left half of rule 30 under an alternating centre.

## Release artifacts (L1621)

**Historical nb1; superseded by GC2805 text corrections.**

- **Texts:**
  - [`essay-prose.md`](essay-prose.md);
  - [`essay.md`](essay.md) (`470c8e36…` after GC2805; oldnb1 used19007d84…), assembled by [`assemble_free_middle_essay.py`](../../../../tests/probes/wolfram/assemble_free_middle_essay.py) with the portal source embedded verbatim;
  - [`title.txt`](title.txt);
  - [`abstract.txt`](abstract.txt) (204 words after GC2805, one line; oldnb1 used201 words);
  - [`headlines.txt`](headlines.txt) (8);
  - [`PR-BODY.md`](PR-BODY.md).
- **The worked numbers.** Python ([`free_middle_replay.py`](../../../../tests/probes/wolfram/free_middle_replay.py), with its prediction header) and Wolfram Language give the same list: `{{0, 4, 180, 214}, {0, 6, 375, 381}, {1, 1, 0, 0, 0, 0, 0, 1, 0}, 4, {10, 14, 18, 22, 26, 30, 34}}`.
  - The balance totals are `0` for popcount at `N = 9` and for the count of `11` at `N = 10`.
  - The best popcount word has rise `4` read from its deep end.
  - The planted row's four-step change grows by exactly `4` per period.
  - The prediction held.
- **Notebook nb1.** Kept outside git, built by [`free_middle_notebook.wl`](../../../../tests/probes/wolfram/free_middle_notebook.wl) (`ab07295c…`) at the verifier's kit `5fb59158`, under `run_capped.py --track-tree`.
  - SHA256 `12c748474cfd1b17aeadec1b217ef335c45a0c64c3227a6b02e1ebc24cb14048`, 235,983 bytes.
  - RESULT OK in 20.3 s, 2.1 GB peak tree RSS.
  - Gates: 6 output cells and no message cells; the first cell equals the Python replay; the Abstract cell equals `abstract.txt`; the icon payload equals the portal source; the axiom sets match `Check`; KernelChecked at 405.
  - Evidence: `cited/local/free-middle-nb1-20261110.tar.gz`, 82,514 bytes, SHA256 `f57290fe7a18dd2e348d36ef898c7a5184ee4df6f4567a72dfd697b20b367f6a`, read back byte-exact.
- **Post script.** Current pins were refreshed coherently for nb2 (L1624/GC2808); the following oldnb1 receipt is historical. [`post.sh`](post.sh) is S-16's reviewed wrapper with only the pins and the headline count (8) changed. The dry run passes: seven pins, verifier `5fb59158`, image 18.

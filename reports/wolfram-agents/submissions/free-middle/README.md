# The free-middle theorem (queue row S-13)

**DRAFT (L1620): Lean built and checked; GPT's read of the Lean requested; essay, notebook and release artifacts not yet built.** Built under the owner's standing permission of 10 November (L1619) from XP-3.1 as GPT carried it in [GC2702 §2](../../../GPT-BLOCK6-CARRY-REVIEW-20261106.md#2-xp31-free-middle-survives-the-review), with its guards: integer densities, `u(W) → ∞`, the linear lower bound and fixed boundary windows. The B2+ claim stays out.

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
| Portal | [`Rule30Submission.lean`](Rule30Submission.lean) (from the kit form by [`gen_free_middle_portal.py`](../../../../tests/probes/swarm/sw02/block11/gen_free_middle_portal.py)) | `2cbe3701b2f2a244…` | pass at the verifier's kit `5fb59158`: 129 declared, 405 constants replayed, 8 headlines, standard axioms, no new axioms; build plus Check 3.4 s, 0.97 GB ([receipt](check-5fb59158.json)) |
| Kit | [`Rule30FreeMiddle.lean`](Rule30FreeMiddle.lean), 1,327 lines | `01a2bea3aad44ac4…` | pass at kit main `03a19bf`: 128 declared, 405 constants, 8 headlines; module build 2.0 s, Check 5.0 s, 0.97 GB ([receipt](check-kit-03a19bf.json)); kit branch `free-middle` local, not pushed |

**Mutants.** All eight must-fail mutants rejected ([output](../../../../tests/probes/swarm/sw02/block11/mutate_free_middle.out), [script](../../../../tests/probes/swarm/sw02/block11/mutate_free_middle.py)): a quadratic lower bound (false, by the popcount example), balance from `N ≥ m + 7`, an image count of 255, a whole-row horizon, an all-black prefix, a linear `W` in the counterexample (false, by `free_middle`), windows of `m - 2` cells, and B2 without `u → ∞`.

## Prior art and scope

- Kit: `Rule30ZeroBoundaryBarriers.no_local_ranking` (B2 for all surviving double steps) and `Rule30LocalConservation.cyclic_conserved_iff_shift_coboundary` (the classification), both used, not reproved. `known_find` for `no_local_ranking`, `RankCert`, `CyclicConserved`, `free middle` (kit `03a19bf6`, portal 10:49:54Z, 20 open PRs): only those kit modules and `Rule30ProductParity.CyclicConserved`, a different notion. Cloud's CL752 comparison: the free-middle theorem CLEAR; `rule30-open`'s conservation-laws note and the kit's barriers PARTLY cover the object.
- Literature: balance for permutive cellular automata (Hedlund 1969) and absence of conservation laws (Hattori and Takesue 1991) are classical; the kit cites the latter.
- Not claimed: real or nonlinear densities, bounded margins `u`, rankings with memory, `Q01`, Problem 1. The late population includes rows that are not the left half of rule 30 under an alternating centre.

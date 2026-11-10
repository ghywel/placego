Rule30FirstCheckDegree: the first check has degree n or n - 1, and its weight is n mod 2 (PORTAL-ID)

This adds `lean/Ruliology/CellularAutomata/Rule30FirstCheckDegree.lean`, with its `public import` line in `lean/Ruliology.lean` after `Rule30FirstChecks` and a row in *Added in the kit* after the same module. It imports only `Rule30FirstChecks`.

**What it proves.** It proves two algebraic normal form coefficient laws for `Rule30FirstChecks.check n`, and its exact degree for every positive `n`. The coefficient of a monomial is the exclusive-or over the subcube below its mask (`coeff`), and `anf_expansion` proves the Möbius inversion, so the degree is a formal statement (`IsDegree`).
- `top_coefficient`: for `n ≥ 1`, the coefficient of `f 0 ⋯ f (n - 1)` is `n mod 2`.
- `omit_coefficient`: for `n ≥ 2`, the coefficient of the monomial without `f 1` is `n + 1 mod 2`.
- `check_degree`: the check has degree `n` for odd `n` and `n - 1` for even `n`.
- `ones_parity`, `first_check_parity`: for `n ≥ 1`, `ones n ≡ n` and, with `first_check_count`, `firstCheck n ≡ n` modulo `2`.
- `walsh_mod_four`, `walsh_one`: `2 ^ n - 2 * ones n` is `2` modulo `4` exactly at odd `n ≥ 2`, and `0` at `n = 1`.
- `other_phase_odd`: with the free bits at the even steps and column `-1` black at the odd ones, the check at depth `2 n` has odd weight for every `n ≥ 1`.

**Method.** Flipping one entry of column `-1` flips every cell on the previous anti-diagonal (`Rule30ZeroBoundary.recon_aff`). So the top cell changes by the exclusive-or of the negated cells two anti-diagonals back (`diag`). Summing out `f 0` kills those cells at times `≥ 2`. Two survive in the kit phase, the previous check and `bcell` (`top_succ`, `bsum`); one survives in the other phase (`other_flip`). Fixing `f 1 = 0` first gives the second recurrence (`rsum_succ`, `tsum_succ`).

**Checks**, with Lean 4.35.0, at main `03a19bf`:
- `lake build Ruliology.CellularAutomata.Rule30FirstCheckDegree`: no warnings, under 1 s.
- The kit's own `Check.lean --claim partial` passes all 11 headlines, with 145 constants and no new axioms.
- The portal form passes `Check` at the verifier's kit `5fb59158`. That kit predates `Rule30FirstChecks`, so the portal form carries a byte copy of its body in a nested namespace.
- The compiler rejected all seven mutations tested:
  - the top coefficient `n + 1 mod 2`;
  - the second coefficient `n mod 2`;
  - the other-phase law claimed for the kit phase;
  - degree `n` at every `n`;
  - the Walsh law from `n = 1`;
  - the survivor parity at `n = 0`;
  - the derivative sum without its negation.
- The worked numbers agree in Python and Wolfram Language:
  - the parities for `n ≤ 12`;
  - the degrees `1, 1, 3, 3, …, 9, 9` for `n ≤ 10`, by Möbius transform;
  - the survivors `1, 2, 3, 4, 17, 38` for `n ≤ 6`, by direct simulation;
  - the Walsh sums;
  - the other phase.
- The full catalog was not validated. An uncapped `lake build Ruliology` attempt on Local's M5 was stopped before completion and supplies no receipt; `bash build_all.sh` was not run. The targeted module and official replays above passed.

**Prior art.**
- **Reused.** The check, `ones` and `first_check_count` are `Rule30FirstChecks`'s.
- **Method.** Differentiating along the newest, linearly entering variable is the method of `Rule30Equivalents.AlgebraicDegree`, which treats the unconstrained map. `Rule30WedgeParity` and `Rule30TopCoefficient` sum out variables after triangular substitutions, for other functions.
- **The other phase.** N. Berzai's paper (`nateberzai-svg/rule30-left-edge`) states odd check weights in the other phase without a parity proof there. `lhallee/rule30-open`'s `forced-bits-dense` computes full degree in that phase for twelve widths.
- **What is new.** The all-`n` kit-phase law and its corollaries, and an all-`n` proof in the other phase.

**What it does not do.** Nothing here bears on the single seed. The survivor statement is a congruence, not a count.

Portal entry: [PORTAL-ID](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/PORTAL-ID).

🤖 Generated with [Claude Code](https://claude.com/claude-code)

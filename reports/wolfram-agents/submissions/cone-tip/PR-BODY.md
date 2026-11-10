Rule30ConeTip: a second derivative of the zero-boundary column equal to t - 1 mod 2 on every row (PORTAL-ID)

This adds `lean/Ruliology/CellularAutomata/Rule30ConeTip.lean`, with its `public import` line in `lean/Ruliology.lean` after `Rule30PeriodTwoNoFloor` and a row in *Added in the kit* after the same module. It imports only `Rule30ZeroBoundary`.

**What it proves.** In the zero-boundary left half, with `flip L d` the row `L` with depth `d` flipped:
- `cone_tip`: for every `t ≥ 2` and every row `L`, `zrow L t 1 + zrow (flip L t) t 1 + zrow (flip L (t-1)) t 1 + zrow (flip (flip L (t-1)) t) t 1` is `1` exactly when `t` is even.
- `level_aff`: the cell at depth `k ≥ 1` and tick `s` reads depth `k + s` with coefficient `1`, and nothing deeper.
- `diag`, `chain_flip`: flipping depth `d` changes the cells of level `d + 1` by the negated cells of level `d - 1`; flipping depth `d - 1` flips each of those that is off the wall.
- `face_disagree`, `affine_second`, `tip_not_affine`: for even `t`, every affine function, and every function with vanishing second differences in those directions, misses the tip on each face of four rows, so the tip is not affine.

**Method.** The kit's `zrow_succ` and `zrow_light_cone` give `level_aff` by induction on the tick. Telescoping along the anti-diagonal gives `diag`. At the tip, the chain has `t - 1` real cells and one wall term.

**Checks**, with Lean 4.35.0, at main `03a19bf`:
- `lake build Ruliology.CellularAutomata.Rule30ConeTip`: no warnings.
- The kit's own `Check.lean --claim partial` passes all 7 headlines, with 55 constants and no new axioms.
- The portal form passes `Check` at the verifier's kit `5fb59158`.
- The compiler rejected all five mutations tested:
  - the law at odd `t`;
  - the newest depth one deeper;
  - the derivative without its flip hypothesis;
  - the chain without its negation;
  - the chain parity reversed.
- The worked numbers agree in Python and Wolfram Language: the law on every row of width at most `t + 1` for `t ≤ 14`, and the best affine correlation of the tip, at most `1/2` at every even `t ≤ 12`.
- Not run: the full catalog build (`bash build_all.sh`).

**Prior art.** The left-permutive derivative is `Rule30Equivalents.AlgebraicDegree.deriv_evol_diag_succ`, for the whole line. The same telescoping gives `Rule30FirstCheckDegree` for constrained rows. The row-frame constant is the corollary, and the mechanism is not claimed as new.

**What it does not do.** It says nothing about the single seed. The correlation bound `1/2` is a counting consequence of `face_disagree` that is not formalised here.

Portal entry: [PORTAL-ID](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/PORTAL-ID).

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Rule30RadiusTwoClock: a binary radius-two left-permutive rule with an exactly alternating column from a finite seed (PORTAL-ID)

This adds `lean/Ruliology/CellularAutomata/Rule30RadiusTwoClock.lean`, with its `public import` line in `lean/Ruliology.lean` and a row in *Added in the kit* after `Rule30FiniteConfigs`. It imports only `Rule30Prize`.

**What it proves.** For Booleans `p` and `q`, let `N p q` be `new x i = x (i - 2) xor g (x (i - 1)) (x i) (x (i + 1)) (x (i + 2))`. Here `g` is true unless its last three arguments are equal, except `g 1 1 0 1 = p` and `g 1 0 1 1 = q`.
- `rule_facts`: each rule is white-quiescent, not right-permutive and not affine over GF(2); it is left-permutive by its form.
- `clock`: from exactly the black cells `0` and `2`, columns `-2` and `-1` equal `t mod 2` at every time, for all four rules.
- `column0_alternates`: from `2` and `4`, column `0` alternates.

**Method.** The proof is finite, with no power series and no Mathlib.
- `row_formula`: the row is a doubled block field `z` up to the cell `2t - 1`, then black cells at `2t + 2` and, at even times, at `2t`.
- `step_doubled`: on doubled rows the rule never reads the two exceptional windows and acts as rule 150 on the blocks.
- `z_frontier`: the frontier sources give `z t (t - 1) = z t (t - 2) = (t odd)`.
- `band_step`, `d_band`: reflection about block `-1` commutes with rule 150, and the field minus its reflection is the even band `E n` at time `2n` and `E (n + 1)` at time `2n + 1`.
- `z_clock`: hence block `-1` flips at every step.

**Checks**, with Lean 4.35.0, at main `03a19bf`:
- `lake build Ruliology.CellularAutomata.Rule30RadiusTwoClock`: no warnings, about 2 s.
- The kit's own `Check.lean --claim partial` passes all 7 headlines, with 211 constants and no new axioms.
- The portal form passes `Check` at the verifier's kit `5fb59158`.
- The compiler rejected all five mutations tested: seed `{0, 3}`, block rule 90, the clock claimed for `t` even, the band on odd positions, and the rule claimed right-permutive.
- The worked numbers agree in Python and Wolfram Language. All four rules for 200 steps read 14 windows, none of them exceptional.
- Not run: the full catalog build (`bash build_all.sh`).

**Prior art.** Rule 126 emulating rule 90 on suitable blocks is classical (NKS, p. 270). Recoding the example to four states is a corollary of a known two-track control. What is new is the binary radius-two example and its finite proof.

**What it does not do.** The rules are not rule 30, and nothing here bears on rule 30's center column. Other seeds, chaos and radius one are not addressed.

Portal entry: [PORTAL-ID](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/PORTAL-ID).

🤖 Generated with [Claude Code](https://claude.com/claude-code)

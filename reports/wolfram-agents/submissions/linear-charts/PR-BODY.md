Rule30LinearCharts: every linear chart of the constrained zero-boundary starts is the free-bit chart (PORTAL-ID)

This adds `lean/Ruliology/CellularAutomata/Rule30LinearCharts.lean`, with its `public import` line in `lean/Ruliology.lean` after `Rule30Problem3` and a row in *Added in the kit*. It imports only `Rule30Prize` and `Rule30ZeroBoundary`.

**What it proves.** On `KK L := L 0 = false ∧ InX L`, `Theta` and the free-bit read-off are inverse bijections with all bit sequences, and they turn two steps into the one-sided shift.
- `linear_chart_is_free_bit_chart`, `free_bit_chart_affine`: let `A` be closed under `a + b + c` (pointwise xor), let `Lm` be affine on `A`, and let `Φ`, `Φ'` be mutually inverse between `KK` and `A`, uniformly finitely dependent, with `Φ (zrow L 2) = Lm (Φ L)`. Then `Φ ∘ Theta` is affine.
- `free_bit_chart_iso`: under the same hypotheses, `Φ ∘ Theta` is a bijection onto `A`, uniformly finitely dependent in both directions.
- `free_bit_chart_is_chart`: the free-bit chart itself satisfies the hypotheses.
- `groupLaw_eq_xor`: let an operation on one-sided bit sequences be commutative, have the white sequence as neutral element, satisfy `(x + y) + y = x`, commute with the shift, and have bit 0 fixed by a finite window. Then it is pointwise xor.

**Method.**
1. `fibre_form`: bit `n` of the law is `x n + y n + Q` of the tails.
2. `involution_Q`: `Q u w = Q (u + w) w`.
3. `descent_step`: flip bit `2 r + 1` to shrink the window of `Q`.
4. `window_zero` and `q_white`: then `Q = 0`.

The free-bit side uses the kit's `Theta_unique`, `Theta_dep`, `two_step_shift` and `zrow_light_cone`. Continuity is represented as uniform finite dependence (`ULD`). Its equivalence with continuity on compact domains is classical and is not formalized.

**Checks**, with Lean 4.35.0, at main `03a19bf`:
- `lake build Ruliology.CellularAutomata.Rule30LinearCharts`: no warnings, under 1 s.
- The kit's own `Check.lean --claim partial` passes all 18 headlines, with 105 constants and no new axioms. No headline uses `Classical.choice`.
- The portal form passes `Check` at the verifier's kit `5fb59158`.
- The compiler rejected all six mutations tested:
  - the lemma without the neutral element;
  - the lemma without commutativity;
  - the free bits shifted by two;
  - the white correction set to true;
  - a linear instead of an affine conclusion;
  - the inverse chart without finite dependence.
- The worked numbers agree in Python and Wolfram Language. Among the candidate correction terms of windows 1 and 2 on bit cycles of length 6, only `Q = 0` gives a law. Without symmetry or without the neutral element, a second law survives.
- Not run: the full catalog build (`bash build_all.sh`).

**Prior art.** The free-bit chart is the kit's (`Rule30ZeroBoundary`). The automorphism theorem of the one-sided full 2-shift is due to Hedlund (1969). The group-law lemma is probably known in the theory of one-sided group shifts and is not claimed as new.

**What it does not do.** It says nothing about the single seed, the finite starts or `Q01`.

Portal entry: [PORTAL-ID](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/PORTAL-ID).

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Rule30HybridWall: the immortal rows of the alternating 90/150 hybrid with a white wall (R30-20261110-41fdb3)

This adds `lean/Ruliology/CellularAutomata/Rule30HybridWall.lean`, with its `public import` line in `lean/Ruliology.lean` after `Rule30SparsePreimage` and a row in *Added in the kit* after the same module. It imports only `Rule30Prize`.

**What it proves.** It answers, for a linear relative of rule 30, the question the kit asks of rule 30 as `Q01`. The hybrid `H` applies rule 150 at odd depths and rule 90 at even depths, next to a white wall. A row is immortal when its depth-1 cell is black at every even time.
- `immortal_iff_bitFam_anyWall`, `immortal_iff_famRow`: a finite row is immortal iff `x 1 = 1`, `x (4 j + 3) = x (4 j + 5)` and `x (4 j + 2) = x (4 j + 1) + x (4 j + 3)` for every `j`.
- `immortal_real_iff`, `real_surj`, `real_inj`: in powers of `A = S + S⁻¹`, the immortal rows are exactly `(A + A²) p(A⁴) + r(A⁴)` with `p 0 = 1` and `r 0 = 0`.
- `immortal_iff_param`: for `W ≥ 2`, the immortal rows of width at most `W` are in bijection with the Boolean words supported below `W / 2 - 1`. The count `2 ^ (W / 2 - 1)` is checked by the kernel for `W ≤ 12`; counting the words in general is not formalised.
- `immortal_width_six`, `not_immortal_width_one`: the width-6 immortal rows are `3, 11, 53, 61`; none has width 1.
- `col_not_eventually_periodic`, `immortal_odd_word_not_eventually_periodic`: the column of every nonzero finite row is not eventually periodic.

**Method.** Writing `X = A a(T) + b(T)` with `T = A²`, the hybrid is the pair map `P (a, b) = (a + b, T a)`, and the depth-1 cell is `ψ a` with `ψ q = q 0 + ψ q_o`. The decimation `D (a, b) = (a_o, a_e + b_o)` satisfies `D (P (P x)) = P (D x)` (`D_P_P`). It is a semiconjugacy, since `D` is not injective. So the even-time column is a constant plus the column of `D x` (`psi_even_time`, `even_time_constant`, `colE_even`). The bridge to the physical hybrid realises coefficients by Horner's rule with rule 90 in mirror coordinates (`iter_H_real`, `col_real`). Injectivity is triangular (`col_inj`, `colE_inj`).

**Checks**, with Lean 4.35.0, at main `03a19bf`:
- `lake build Ruliology.CellularAutomata.Rule30HybridWall`: no warnings, about 2.5 s.
- The kit's own `Check.lean --claim partial` passes all 20 headlines, with 445 constants and no new axioms.
- The portal form passes `Check` at the verifier's kit `5fb59158`.
- The compiler rejected all six mutations tested:
  - the width-6 list without `61`;
  - the semiconjugacy with one step of `P`;
  - the coefficient family with `c (4 m + 1) = c (4 m + 3)`;
  - rule 150 at even depths;
  - no immortal row of width 2;
  - the even-time constant without `b 0`.
- The worked numbers agree in Python and Wolfram Language:
  - immortal counts `0, 1, 1, 2, 2, 4, 4, 8, 8, 16, 16, 32` for widths up to `12`, at horizon 400;
  - the cell family equal to the simulated set;
  - the semiconjugacy on all `4096` pairs of degree below `6`.
- Not run: the full catalog build (`bash build_all.sh`).

**Prior art.** Linear cellular automata over `GF(2)` and their polynomial treatment are classical (Martin, Odlyzko and Wolfram, *Algebraic properties of cellular automata*, 1984). The hybrid 90/150 rule and its null-boundary finite versions are standard objects. What is new is the exact immortality answer for this half-line with a white wall, and the decimation semiconjugacy that proves it.

**What it does not do.** The hybrid is linear and is not rule 30, and nothing here decides `Q01`.

Portal entry: [R30-20261110-41fdb3](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261110-41fdb3).

🤖 Generated with [Claude Code](https://claude.com/claude-code)

# The Survivors of a Linear Hybrid: Every Immortal Row of the Alternating 90/150 Rule with a White Wall

Gareth Herbert; Claude (Anthropic); GPT (OpenAI). 10 November 2026.

## 1. The statement

The kit's `Q01` asks whether every finite start of the zero-boundary left half of rule 30 eventually turns depth `1` white at an even time. This module answers the same question exactly for a linear relative of rule 30. That relative is the alternating 90/150 hybrid with a white wall.

Rows are finite, at depths `1, 2, …` next to a white wall at depth `0`. The hybrid `H` applies rule 150 (left, centre and right) at odd depths and rule 90 (left and right) at even depths. Over `GF(2)`:

`H x k = x (k + 1) + [k ≥ 2] x (k - 1) + [k odd] x k`.

A row is *immortal* when its depth-1 cell is black at every even time.
- `immortal_iff_bitFam_anyWall`: a finite row is immortal exactly when `x 1 = 1`, and, for every `j`, `x (4j+3) = x (4j+5)` and `x (4j+2) = x (4j+1) + x (4j+3)`.
- `immortal_iff_famRow`: equivalently, the row is `e1 + e2 + Σ_{j ≥ 1} p_j (e_{4j-2} + e_{4j-1} + e_{4j+1} + e_{4j+2}) + Σ_{j ≥ 1} r_j e_{4j}`.
- `immortal_real_iff`: in powers of `A = S + S⁻¹`, the immortal rows are exactly `(A + A²) p(A⁴) + r(A⁴)` with `p(0) = 1` and `r(0) = 0`. Coefficients exist (`real_surj`) and are unique (`real_inj`).
- `immortal_iff_param`: for `W ≥ 2`, the immortal rows of width at most `W` are in bijection with the Boolean words of length `W/2 - 1`. The count `2^(W/2 - 1)` itself is checked by the kernel for `W ≤ 12`. Counting the words in general is not formalised.
- `immortal_width_six`, `not_immortal_width_one`: the immortal rows of width at most `6` are `3, 11, 53` and `61` (depth `d` at bit `d - 1`); none has width `1`.
- `col_not_eventually_periodic`, `immortal_odd_word_not_eventually_periodic`: the depth-1 column of every nonzero finite row is not eventually periodic. In particular, the odd-time word of an immortal row is not.

## 2. Two steps become one

Write a row in powers of `A` as `X = A a(T) + b(T)` with `T = A²`. The hybrid becomes the pair map `P(a, b) = (a + b, T a)`. The depth-1 cell is `ψ(a)`, where `ψ(q) = q(0) + ψ(q_o)` and `q_o`, `q_e` are the odd and even decimations (`psi_mono`: on `T^m` this is `1` exactly when `m + 1` is a power of `2`).

The decimation `D(a, b) = (a_o, a_e + b_o)` turns two steps into one:

`D(P(P x)) = P(D x)` (`D_P_P`).

`D` is not invertible: it sends `(0, 1)` and `(0, 0)` to the same pair. So this is a semiconjugacy, not a conjugacy. Applying `ψ` gives the renormalisation (`psi_even_time`, `even_time_constant`). The even-time column of `x` is a constant plus the column of `D x`, and the constant is `a(0)` at time `0` and `a(0) + b(0)` afterwards. The second term matters: `D x` may have a constant coefficient, the wall cell, even when `x` does not.

## 3. From the renormalisation to the classification

For a row, `b(0) = 0`, so every even observation equals `a(0)` plus an observation of `D x`.
- If `a(0) = 1`, immortality says that `D x` has a white column at every time. The column determines a finite row with its wall cell (`colE_inj`), so `D x = 0`, which is the family.
- If `a(0) = 0`, `D x` would have a black column at every time. Then `L(D x) + D x` has a white column at every time, so `L(D x) = D x`. That is impossible for a nonzero finite object, since one step moves its deepest black cell one depth further from the wall.

Injectivity is triangular. If the black cell nearest the wall is at depth `n + 1`, the column is black at time `n` (`front`), so a row with a white column is white (`col_inj`). For an object with a wall cell, one step clears the wall, and the finite row is recovered from the top cell down (`colE_inj`).

The bridge to the physical hybrid realises a coefficient sequence by Horner's rule with rule 90 in mirror coordinates (`real`, `iter_H_real`). The depth-1 cell becomes `ψ` of the odd part through the squaring identity `A ↦ A²` on coefficients, which is `S ↦ S²` on rows (`col_real`).

The cell-by-cell family matches the coefficient family as a set, through a bijective change of parameters (`real_afam`), not term by term. `A^{4j}` is not `S^{4j} + S^{-4j}` unless `j` is a power of `2`; for example, `A^12` is the row `e4 + e12`.

## 4. Scope

The hybrid is linear and is not rule 30. The point is a contrast. For this relative of rule 30, under the same white wall and the same even checks of depth `1`, the immortal rows form an explicit self-similar family. A count of survivors per width is `2^(W/2 - 1)`, and the column of every survivor is aperiodic. Nothing here decides `Q01` or bears on rule 30's own survivors. The count is formal as a bijection; its numerical value is formal only for `W ≤ 12`.

## 5. Worked numbers

The cell below simulates the hybrid for 400 steps on every row of width at most `12`. It reports:
- the number of immortal rows for each width bound `W = 1, …, 12`;
- the immortal rows of width at most `6`;
- whether the simulated immortal set equals the cell-by-cell family for every `W ≤ 12`;
- whether `D(P(P x)) = P(D x)` on all `4096` pairs of polynomials of degree below `6`.

## 6. Prior art and scope

- **The objects.** Linear cellular automata over `GF(2)` and their polynomial treatment are classical (O. Martin, A. Odlyzko and S. Wolfram, *Algebraic properties of cellular automata*, Comm. Math. Phys. 93, 1984). The hybrid 90/150 rule is a standard object, and finite null-boundary 90/150 automata appear in the literature (for example [this 2022 paper](https://eprint.iacr.org/2022/041.pdf)). Those have two fixed finite endpoints, unlike this finite-support half-line whose width grows. The method and the hybrid are not claimed as new.
- **What is new.** The exact answer to the even-check immortality question for this hybrid with a white wall: the classification, the bijection with words of length `W/2 - 1`, and the aperiodicity of the column, with the decimation semiconjugacy that proves them.
- **The sibling result.** The plant half of the same queue item ([R30-20261110-7a4a0d](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261110-7a4a0d)) shows that a survival table alone cannot decide `Q01`. This module shows a linear relative where the survivors are fully known.
- **History.** It came from a sub-agent run of our programme. GPT carried the classification with the repair that the observation must be defined on all polynomial pairs, including a constant term. Local found the shorter route through the decimation semiconjugacy, which GPT carried. A Local sub-agent formalized it, and corrected one step in its brief: the family matches term by term only after a change of parameters.

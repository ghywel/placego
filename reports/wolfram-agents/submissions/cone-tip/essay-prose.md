# The Cone Tip of the Zero-Boundary Left Half: A Second Derivative of the Column Equal to t - 1 mod 2 on Every Row

Gareth Herbert; Claude (Anthropic); GPT (OpenAI). 10 November 2026.

## 1. The statement

In the zero-boundary left half of rule 30, the cell at depth `1` and tick `t` is a Boolean function `a_t` of the start's cells at depths `1, …, t + 1`. Write `flip L d` for the row `L` with depth `d` flipped. The second difference of `a_t` in the depths `t - 1` and `t` is

`D L = a_t(L) + a_t(flip L t) + a_t(flip L (t-1)) + a_t(flip (flip L (t-1)) t)`.

- `cone_tip`: for every `t ≥ 2` and every row `L`, `D L = (t - 1) mod 2`. It is the same constant on every row.
- `face_disagree`: so for even `t`, every function whose second difference in those two directions vanishes disagrees with `a_t` somewhere on each such face of four rows. Affine functions are such functions (`affine_second`).
- `tip_not_affine`: hence `a_t` is not affine for even `t ≥ 2`.

Each face of four rows therefore holds at least one disagreement. So at least a quarter of all rows disagree with any affine function, and the correlation of `a_t` with any affine function is at most `1/2`. That last counting step is elementary and is not formalised here; the worked numbers check it for `t ≤ 12`.

## 2. Two derivatives

Call depth plus tick the *level* of a cell.

- `level_aff`: a cell of level `L` reads the start only at depths up to `L`, and reads depth `L` with coefficient `1`. Rule 30 is left-permutive, and the left input of the cell at depth `k` is depth `k + 1`.
- `diag`: flip depth `d` alone. Every cell of level `d` flips, and cells of lower level do not. A cell of level `d + 1` is the cell of the same level one depth deeper and one tick earlier, exclusive-or `(y or z)`, with `y` of level `d` and `z` of level `d - 1`. Flipping `y` changes `y or z` by `not z`. So along level `d + 1` the change telescopes to the exclusive-or of the negated cells of level `d - 1` (`chain`).
- For the tip at level `t + 1`, flipping depth `t` therefore changes `a_t` by `t` negations of the cells of level `t - 1` at depths `t - 1, t - 2, …, 1, 0`. The last is the white wall.
- `chain_flip`: flip depth `t - 1` as well. Each of the `t - 1` real cells of level `t - 1` flips, by `level_aff`, while the wall stays white. So the second difference is `(t - 1) mod 2`.

## 3. Scope

These are exact statements about one Boolean function for every `t`. They do not bound how often the column is black, and nothing here bears on the single seed. For odd `t` the law gives a zero second difference in these directions and says nothing about affinity. The correlation corollary is stated in words, with its counting step unformalised.

## 4. Worked numbers

The cell below checks:
- the second difference on every row of width at most `t + 1`, for `t = 2, …, 14`;
- the largest normalised Walsh coefficient of `a_t` on those rows for `t = 2, …, 12`, which is its best correlation with an affine function, and whether it is at most `1/2` at every even `t`.

## 5. Prior art and scope

- **The mechanism.** The derivative along the newest, linearly entering cell is the kit's `Rule30Equivalents.AlgebraicDegree.deriv_evol_diag_succ`, for the whole line. The same telescoping gives the first-check laws of `Rule30FirstCheckDegree` for constrained rows. Here it is carried out in the row frame of the zero-boundary left half, with its white wall, and the constant `t - 1 mod 2` is the corollary. The mechanism is not claimed as new.
- **What is new.** The cone-tip law in this frame, its face and non-affinity corollaries, and their formal proof.
- **History.** It came from a sub-agent run of our programme. Cloud carried the hand proof, and Local formalized it.

# Two of Every Three First Checks Are Balanced: An Exact Pair Law on Free Words

Gareth Herbert; Claude (Anthropic); GPT (OpenAI). 6 November 2026.

## 1. The first check

`Q01` asks whether a finitely supported start of the zero-boundary left half can keep column `-1` black at every even tick. Such a start is a row of finite width, and each even tick is a check it must pass.

The checks are free at first. Every free word `f` has one row `Theta f` that passes them all, and depth `2 j + 2` flips exactly with the free bit `f j` (`tri_even`). The kit counts the consequence: exactly `2 ^ n` rows of width at most `2 n` pass every even tick below `2 n` (`count_constrained`). They are the rows `Theta f` cut off at depth `2 n`, for the `2 ^ n` free words of length `n`.

The check at tick `2 n` is the first that can fail. Cutting `Theta f` off at depth `2 n` turns its cell at depth `2 n + 1` white, and that cell is the only thing the check at tick `2 n` still depends on. So the check reads one cell. Write

- `check n l` for `Theta (word l) (2 n + 1)`, on a word `l` of length `n`;
- `ones n` for the number of words of length `n` on which it is black;
- `gap n` for the smaller of `ones n` and `2 ^ n - ones n`.

Then the rows that pass are exactly the words on which the cell is white (`first_check_count`):

```
firstCheck n + ones n = 2 ^ n
```

Everything below is exact counting over free words with all even pins black. Is this check close to a fair coin, or could it be nearly constant? A nearly constant check that passes would cost almost nothing.

## 2. Two ticks

Two ticks of a row with a white wall are one Boolean identity (`two_tick`). Write `a`, `b`, `c`, `d`, `e` for the cells at depths `j` to `j + 4`. Then the cell at depth `j + 2`, two ticks later, is

```
e  xor  ((b or a) and not (d xor c))
```

Two ticks of `Theta f` are `Theta` of the shifted word (`two_step_shift`). So the identity compares a check with the check of the shift (`check_xor`): they differ exactly when

```
(T(2m + 2) or T(2m + 1))  and  not (T(2m + 4) xor T(2m + 3))
```

where `T = Theta f`, the first check being at depth `2 m + 5` and the second at depth `2 m + 3` of the shifted row.

## 3. The pair law

Fix a word `p` of length `m` and add two bits `x`, `y`, newest last. The four cells above behave very simply (`four_sum`):

- `T(2m + 1)` is `check m p`, whatever `x` and `y` are (`tri_odd`).
- `T(2m + 2)` flips with `x` and does not see `y` (`tri_even`, `Theta_dep`).
- `T(2m + 3)` does not see `y` (`Theta_dep`).
- `T(2m + 4)` flips with `y` (`tri_even`).

So for each `x`, if `T(2m + 2) or T(2m + 1)` is black, the two values of `y` split evenly, and otherwise neither differs. Averaging over `x` as well, the four completions contain `1 + [check m p]` differences. Summing over `p` gives the pair law (`pair_count`):

```
flips (m + 1) = 2 ^ m + ones m
```

Here `flips (m + 1)` counts the words of length `m + 2` whose check differs from the check of their shift. With `p_n = ones n / 2 ^ n`, the probability of a difference is exactly `(1 + p_(n-2)) / 4`, and in signs `E[g_n(f) g_(n-1)(σ f)] = (1 + c_(n-2)) / 4`, where `g_n = (-1)^check` and `c_n = E g_n`.

This qualifies a random-function picture of the checks. Independence would give the product `c_n c_(n-1)`, so the exact covariance is `(1 + c_(n-2)) / 4 - c_n c_(n-1)`. In particular, when all three means are small, this covariance is close to `1/4`. The raw correlation alone does not establish dependence for every pair.

## 4. Two inequalities

A check and a shifted check are two subsets of the same cube, and `flips` is the size of their symmetric difference. So their sizes obey the elementary overlap bounds (`overlap`). Each shifted word comes from two words, so the shifted set has `2 * ones n` members.

Substituting the pair law turns these into linear inequalities between the numbers `ones n`. Two of them are worth naming. Divided by `2 ^ n`, with `ε_n = gap n / 2 ^ n`, they read:

- `adjacent`: `ε_n + ε_(n-1) ≥ (1 + p_(n-2)) / 4 ≥ 1/4`, for `n ≥ 2`.
- `distance_two`: `4 ε_n + 6 ε_(n-2) ≥ 1/4`, for `n ≥ 4`.

The second comes from using the pair law twice. Near-constant checks at `n` and `n - 2` pin `c_(n-1)` from both sides, and that forces the check at `n - 3` to be near constant too, against `adjacent`. In Lean both inequalities are `omega`, once the counts are named. So `ε` cannot be below `1/40` at two indices at distance one or two (`two_of_three`):

**Among any three consecutive `n ≥ 2`, at most one check is near constant.** For at least two of them `|c_n| ≤ 19/20`, and the share of rows that pass lies in `[1/40, 39/40]` (`first_check_balanced`).

These pair and marginal inequalities alone cannot ensure that every sufficiently late check is nondegenerate. The periodic pattern `c = 1, 1/3, 1/3` meets them and leaves room for a degenerate check at every third `n`. This limits the frequency conclusion; it does not assert that the constant `1/40` is optimal, or that this abstract pattern is realized by Rule 30.

## 5. Worked numbers

The cell below computes the check from the sideways recursion for every word of length at most 12, and counts rows directly for `n` up to 6. It returns `ones n`, `flips` for `n = 2` to `12`, the pair law's check, the row count's check, and the `n` at which a check is near constant.

The only such `n` is `0`, where the check is always black. The theorem is far weaker than the data: exact sums computed outside this module give `|c_n| ≤ 1/2` for `1 ≤ n ≤ 30`. Its point is that it holds for every `n`.

## 6. Prior art and scope

`Theta`, `two_step_shift`, `tri_odd`, `tri_even`, `Theta_dep`, `snoc_pivot`, `ok_snoc` and `count_constrained` are the kit's `Rule30ZeroBoundary`. The two-tick identity is two applications of the rule, and it appears in expanded polynomial form in this project's public record from 8 October 2026; what is new here is its consequence on free words. We found no bound on these checks in the kit, on the portal, in the open pull requests, or in `lhallee/rule30-open` at commit `f877f5af`.

This is a statement about the first check past the free range, under the uniform law on free words. It does not hold every `n`, only two of every three. It does not bound the second check: on rows that have passed the first, the fresh bits behind the pair law are pinned, so these bounds do not multiply along a row, and no decay of survivors follows. A uniform bound on checks conditioned on the earlier ones would imply `Q01`, and it is false as stated at small widths, where plateaus occur.

Nothing here proves `Q01`, and Problems 1 to 3 stay open.

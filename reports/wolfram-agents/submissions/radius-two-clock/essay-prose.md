# A Binary Radius-Two Left-Permutive Rule Whose Column Alternates Exactly from a Finite Seed

Gareth Herbert; Claude (Anthropic); GPT (OpenAI). 10 November 2026.

## 1. The statement

Rule 30 is left-permutive: each new cell is its left neighbour exclusive-or a function of the cells at and to the right of it. Problem 1 asks whether its center column, from the single black cell, can become periodic. This module shows that left permutivity alone does not forbid it once the radius is two, even with two states.

For Booleans `p` and `q`, the rule `N p q` is

`new x i = x (i - 2) xor g (x (i - 1)) (x i) (x (i + 1)) (x (i + 2))`,

where `g a b c d` is true unless `b`, `c` and `d` are all equal. The two exceptions are `g 1 1 0 1 = p` and `g 1 0 1 1 = q`.

- `clock`: from exactly the black cells `0` and `2`, the columns `-2` and `-1` equal `t mod 2` at every time `t`, for all four rules.
- `column0_alternates`: from the black cells `2` and `4`, column `0` alternates.
- `rule_facts`: each rule is white-quiescent, not right-permutive, and not affine over `GF(2)`. It is left-permutive by its form.

## 2. Doubled blocks

The row at time `t` is a *doubled* block field: cells `2j` and `2j + 1` both carry `z t j`, for every block `j ≤ t - 1`. Beyond that sit one black cell at `2t + 2` and, at even times, another at `2t` (`row_formula`).

On a doubled row:
- an even cell reads `(z (j-1), z j, z j, z (j+1))`;
- an odd cell reads `(z j, z j, z (j+1), z (j+1))`.

Neither window is exceptional, so `p` and `q` are never read. In both cases the new value is `z (j-1) xor z j xor z (j+1)`, which is rule 150 on the blocks (`step_doubled`).

The frontier adds sources:
- `z (t+1) = B (z t) + δ t + [t even] δ (t-1)`, where `B` is rule 150;
- its frontier is `z t (t-1) = z t (t-2) = (t odd)` (`z_frontier`);
- the eight cells from `2t - 2` to `2t + 5` follow by a finite check.

## 3. The clock by reflection

Let `J z j = z (-2 - j)` reflect about block `-1`, and `d t = z t + J (z t)`. Reflection commutes with rule 150. Let `E n` be the even positions `-2n, -2n + 2, …, 2n - 2`, so that `E 0` is empty. Then:
- `B (E n) = E n + δ (2n - 1) + δ (-2n - 1)` (`band_step`), even at `n = 0`, where the two deltas cancel.
- With the sources and their reflections, `d (2n) = E n` and `d (2n + 1) = E (n + 1)` (`d_band`).
- Block `-1` updates as `z (t+1) (-1) = z t (-1) + d t 0 + [t = 0]`. Since `d t 0 = [t ≥ 1]`, block `-1` flips at every step (`z_clock`).

The proof uses Booleans, integer bounds and two-step induction; no power series are needed.

## 4. Scope

The four rules are not rule 30, and nothing here bears on rule 30's center column. This example shows that, at radius two, left permutivity together with white quiescence, nonlinearity and a finite seed does not exclude an exactly periodic column. An argument for Problem 1 must use more of rule 30 than these properties.

Not claimed here:
- the behaviour of other seeds;
- any chaos of these rules;
- any classification of radius-one rules;
- any arithmetic sharpening of the clock.

## 5. Worked numbers

The cell below simulates all four rules for `200` steps from the black cells `0` and `2`. It reports:
- whether columns `-2` and `-1` are always `t mod 2`;
- how many distinct four-cell windows `g` reads on these orbits, and how many of them are exceptional;
- whether column `0` alternates from the black cells `2` and `4`;
- whether the black cells at time `t` lie in `[-2t, 2t + 2]`.

## 6. Prior art and scope

- **Block emulation.** That rule 126 behaves like rule 90 on suitable blocks is classical (S. Wolfram, *A New Kind of Science*, p. 270). Here the base `g` for `p = q = 1` is rule 126 on its last three arguments, and the doubled blocks follow rule 150.
- **Larger alphabets.** A four-state, two-track example with a period-two column from a finite seed was already in our record ([GC1165](https://github.com/ghywel/placego/blob/9d9de585fb2a3eeec2ccee7776a2db8d15af70ac/archive/gpt/RULE30-GPT.9.md#gc1165--injective-expanding-finite-orbits-can-share-a-periodic-column-2026-10-13), carried in L654). That establishes the larger-alphabet existence statement; the present result concerns a binary radius-two rule.
- **What is new.** The binary radius-two example, with its exact moving source, and a finite proof.
- **History.** It came from a sub-agent run of our programme. GPT carried the original generating-function proof and proposed the reflection proof, which Local carried and formalized.

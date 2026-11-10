# A Planted Survivor: Rule 30's Survival Table with One Row Added, by a Tree Automorphism of the Rows

Gareth Herbert; Claude (Anthropic); GPT (OpenAI). 10 November 2026.

## 1. The statement

The kit's `Q01` is the period-2 form of Problem 1 in the zero-boundary left half: every finite start eventually turns depth `1` white at an even time. A natural way to probe it is the survival table: for each width bound `W` and time `t`, count the rows of width at most `W` that pass every even check of depth `1` through `t`. This module shows that such a table cannot decide `Q01` by itself.

A different map of finite rows has an immortal row, and a survival table equal to rule 30's except for one extra row per width.

- `psi_psiInv`, `psiInv_psi`: for `L ≥ 1`, the map `psi L` flips the cell at each odd depth `k ≥ 2L + 1` at which the row agrees with the stripe `…10101` at every depth below `k`. It is a bijection of rows with inverse `psiInv L`.
- `psi_stripe`: `psi L` sends the stripe to the finite row `trunc (2L - 1)`.
- `psiInv_fin`: `psiInv L` keeps the width of every finite row except `trunc (2L - 1)`.
- `Tn_eq`: the map `T L = psi L ∘ (one step of rule 30) ∘ psiInv L`, iterated `n` times, is `psi L` of `n` steps of rule 30 from the inverse row.
- `T_finite`, `T_zero`: `T L` maps finite rows to finite rows and fixes the empty row.
- `T_fixed`, `fixed_survives`: `T L` fixes `trunc (2L - 1)`, whose depth `1` is therefore black at every time.
- `survival_table`: for every `W` and `t`, the count under `T L` equals the count under rule 30, plus one exactly when `2L - 1 ≤ W` and `2 ⌈W/2⌉ ≤ t`.

## 2. The automorphism

The flip at depth `k` reads only the depths below `k`. So `psi L` is a tree automorphism of the rows, and its inverse is computed depth by depth (`ipf`, `psiInv`).

The stripe agrees with itself everywhere, so every site flips, and its image is the stripe cut after depth `2L - 1`. A finite row disagrees with the stripe at its first white odd depth beyond its width, so only finitely many flips happen.

For the inverse the converse holds. If a flip happened beyond the width of a finite row, the row's inverse would agree with the stripe from then on, so the row would be `trunc (2L - 1)` (`psiInv_fin`).

## 3. The count

Depth `1` lies below every site, so survival under `T L` is survival under rule 30 of the inverse row (`survT_eq`). Inside the range `2L - 1 ≤ W`, `psiInv L` is injective from the rows of width at most `W` other than `trunc (2L - 1)` into those other than `trunc (2 ⌈W/2⌉ - 1)`:
- the image of `trunc (2m - 1)` under `psi L` has a black cell at depth `2m + 1` (`psi_trunc_top`), beyond the width bound;
- `trunc (2L - 1)` itself goes to the stripe, which survives for ever;
- `trunc (2 ⌈W/2⌉ - 1)` dies exactly at time `2 ⌈W/2⌉` (the kit's `trunc_survives`).

Counting along an injective self-map of a finite range (`cnt_perm`, with a pigeonhole lemma `pigeon`) gives the table identity. Outside that range, `psiInv L` is the identity on the rows that are counted.

## 4. Scope

`T L` is not a cellular automaton and not rule 30. `psi L` and `psiInv L` read a row depth by depth, with a counter up to `2L`, a parity bit and a prefix-match bit. So `T L` is rule 30's step between two finite-state transducers. The width-growth law of rule 30 is not claimed for `T L`.

The point is limited: a survival table of rule 30, however far it is computed, is also the survival table of a map with an immortal row, up to one row per width. Nothing here decides `Q01`, and nothing is claimed about tables restricted to physical left halves of rule 30.

## 5. Worked numbers

The cell below checks the table identity directly, for `L = 1, 2, 3`, every `W ≤ 10` and every `t ≤ 14`. It gives:
- whether the identity holds in every case, and the number of cases;
- the differences of the two counts for `L = 2` at `t = 8` and `W = 0, …, 10`;
- whether direct iteration of `T L` agrees with rule 30 on the inverse row, for every row below `2^8` and `12` steps;
- whether `T L` fixes the truncated stripe.

## 6. Prior art and scope

- **The kit's inputs.** The stripe, its truncations and `trunc_survives` are the kit's (`Rule30ZeroBoundary`, `Rule30ZeroBoundaryBarriers`), and the zero-boundary step is the kit's `zrow`.
- **The method.** Conjugating a dynamical system by a homeomorphism that moves a repelling point onto a finite configuration is a standard idea, and its use here is not claimed as new.
- **What is new.** The exact table identity, and this finite-state witness of it.
- **History.** It came from a sub-agent run of our programme. GPT carried it with the domain repair that `psi` acts on rows and the stripe together, and with the inclusive survival convention.

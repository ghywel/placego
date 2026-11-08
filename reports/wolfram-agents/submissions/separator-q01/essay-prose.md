# The Separator Is Q01 for Free Bits Without Two Adjacent Whites, and BWH Is a Death-Time Bound

Gareth Herbert; Claude (Anthropic); GPT (OpenAI). 8 November 2026.

## 1. The statements

The kit's zero-boundary left half runs rule 30 on the cells to the left of a white wall: `zrow L t k` is the cell at depth `k` and tick `t`, and the start `L` is read at depths `k ≥ 1`. A start is constrained when depth `1` is black at every even tick. The constrained starts are exactly the rows `Theta f`, where the free bits `f s` are depth `1` at the odd ticks `2 s + 1`. `Q01` says that no constrained start is finitely supported (`Rule30ZeroBoundary.Q01`, `Q01_iff_Theta`).

The kit also states two open hypotheses on streams over `Fin 4` (`Rule30WedgeBridge`). A stream is hard-core when every symbol is `1` or `2` and no two adjacent symbols are both `1`. The constant-tail separator `SEP` says that no hard-core stream has an inverse diagonal that is eventually constant `2` or eventually constant `3` (`ConstantTailSeparator`, equivalent to `OrbitSeparator`). The binary wedge hypothesis `BWH` says that for `n ≥ 7` no stream with a binary prefix of length `2 n + 2` has a constant wedge `2` or `3` of length `n + 2`. The kit proves `BWH ⇒ SEP` and that each excludes period two of the center column. Its docstrings record that no implication is proved, in either direction, between these hypotheses and `Q01`. This module proves where they sit.

Write `N` for the free bits with no two adjacent white bits, and `QN` for `Q01` restricted to them: `Theta f` is not finitely supported when `f` is in `N`.

**Theorem (`sep_iff_QN`).** `SEP` holds if and only if `QN` holds.

**Theorem (`Q01_iff_sep_and`).** `Q01` holds if and only if `SEP` holds and no finitely supported `Theta f` has free bits that meet two adjacent whites infinitely often.

**Theorem (`sep_Q01Gap`, `sep_iff_LR1`).** `SEP` implies the kit's `Q01Gap`, hence `CQ01Empty`. It is equivalent to `LR1`: no width-one layer beside the alternating column, with any start cell and any input from column `2`, has a finitely supported forced left row.

**Theorem (`bwh_iff_deathBounds`, `bwh_death`, `bwh_Q01`).** `BWH` holds if and only if every start of exact even width `W ≥ 16` dies by tick `2 W`, and every start of exact odd width `W ≥ 17` whose top two cells are black dies by tick `2 W - 2`. Under `BWH`, every start supported at depths `≤ W` with `W ≥ 16` dies by tick `2 W + 4`, and `Q01` follows.

Here a start dies at the first even tick at which depth `1` is white.

## 2. The chart

For a start `L`, let `zpair L t k` be the pair of depths `k` and `k + 1` at tick `t`, read as a symbol of `Fin 4` by the kit's `encodePair`. The endpoint stream of `L` is the pair of depths `1, 2` at the odd ticks: `zEnd L j = zpair L (2 j + 1) 1`.

**Chart (`cone_chart`, `peel_chart`).** If depth `1` is black at every even tick up to `2 S`, then for `j + n ≤ S` and `t + d ≤ S`,

`cone (zEnd L) n j = zpair L (2 j + n) (n + 2)`, and `peelPow d (inverse (zEnd L)) t = zpair L t (2 d + t + 2)`.

The inverse cone of the endpoint is the run of the start itself, read diagonally. Two facts carry it. The kit's `phi` steps one pair back in depth, from a pair and the pair below it one tick later (`zpair_back`, from `pair_inverse_table`). At an even tick depth `1` is black, so the boundary of the endpoint is the next pair down (`zEnd_boundary`). This is the kit's `actual_cone_chart` in zero-boundary coordinates. No right half enters, and the finite horizon is what the death bounds of section 5 need.

For a constrained start the endpoint is binary. At the odd tick `2 j + 1` depths `1` and `2` differ, because depth `1` is black one tick later. So `zEnd (Theta f) j` is `2` where `f j` is black and `1` where it is white (`zEnd_Theta`). It is hard-core exactly when `f` has no two adjacent white bits (`hardCore_endOf_iff`), and every hard-core stream arises this way (`hardCore_eq_endOf`).

## 3. SEP is Q01 on one class of free bits

Suppose `f` is in `N` and `Theta f` is white beyond depth `W`. By the chart, the `W`-th peel of the inverse of its endpoint is zero at every tick, because it reads depths beyond `W + t` at tick `t`. The kit's `separator_excludes_finite_peel_rank` says that under `SEP` no hard-core stream has a finite peel rank. So `SEP ⇒ QN`.

Conversely, suppose a hard-core stream has inverse eventually equal to `c ∈ {2, 3}` from index `m` on. The stream is the endpoint of some `Theta f` with `f` in `N`. Since `phi c c = 0` and `phi 0 0 = 0`, every further peel vanishes from `m` on (`peel_tail_zero`). Read through the chart at the even tick `2 m`, the row there is white from depth `2 m + 4` on. That row is `Theta` of the free bits shifted by `m` (`zrow_Theta_even`, from the kit's `two_step_shift`), and the shift stays in `N`. So `QN ⇒ SEP`, and `sep_iff_QN` holds. No rotation of the stream is needed.

The same shift shows that `QN` excludes every finite `Theta f` whose free bits are free of two adjacent whites from some index on (`QN_eventually`). So the only finite constrained starts that `SEP` leaves open have free bits meeting two adjacent whites infinitely often (`Q01_iff_sep_and`). In particular `Q01 ⇒ SEP` (`Q01_sep`). The class of `Q01Gap` gives free bits whose complement has no two adjacent black bits from some step on, so `SEP ⇒ Q01Gap` (`sep_Q01Gap`), and the kit's `CQ01Empty_of_Q01Gap` gives `CQ01Empty`.

## 4. Width-one layers

Put a single column beside the alternating center column, black at the even ticks: `layerCol x0 r` has start cell `x0` and arbitrary input `r t` from column `2`, and steps by rule 30. Its word `layerWord x0 r s` is its value at the white tick `2 s + 1`.

The layer words are exactly the words with no two adjacent black bits. If the column is black at a white tick, it is black at the next black tick, so it is white at the next white tick (`layerWord_no11`). Conversely every such word is a layer word: start white, and feed `r (2 s) = !w s` and `r (2 s + 1) = false` (`layerWord_realizes`). At the black ticks a layer is unconstrained (`black_tick_control`).

So `LR1`, which says that every layer's forced left row `Theta (fun s => !layerWord x0 r s)` is infinite, is `QN` (`LR1_iff_QN`), and `SEP ⇔ LR1`. The column `1` of a right half driven by the alternating column is a layer whose input is the right half's own column `2` (`u_eq_layerWord`). Hence, under `SEP`, the kit's sideways row `Psi R` is infinite for every right half `R` (`LR1_not_finSupp_Psi`), and `CQ01` follows (`sep_CQ01`). The kit already has this conclusion as `constant_separator_excludes_alternating`, in the coordinates of the whole configuration. What the layers add is the converse: `SEP` asks for nothing beyond a single column with free input, and it asks for all of that.

## 5. BWH is a death-time bound

The chart with a finite horizon gives a dictionary. For `n, ℓ ≥ 1` and `c ∈ {2, 3}`, a stream with a binary prefix of length `n + ℓ` and a constant wedge `c` of length `ℓ` at depth `n` exists exactly when some start survives to tick `2 (n + ℓ)` with its last black cell at depth `2 n + 2` (for `c = 2`), or at depth `2 n + 3` with the cell before it black (for `c = 3`).

From a row to a stream (`wedge_of_row_two`, `wedge_of_row_three`): survival makes the endpoint binary, and the top of the row moves out one depth per tick, so the pair the chart reads is the top pair, `2` or `3`. From a stream to a row (`row_of_wedge`): take `Theta f` with the stream's free bits. The constant wedge forces zero pairs from depth `2 n + 4` through depth `2 (n + ℓ) + 1`, because each further peel of a constant is zero. Truncate there; the last check, at tick `2 (n + ℓ)`, reads depths only up to `2 (n + ℓ) + 1`, so the truncation survives.

With `ℓ = n + 2` this turns `BWH` into the exact-width bounds of section 1 (`bwh_iff_deathBounds`). A start of odd width without its top two cells black has them black two ticks later, at width `W + 2`. So it dies by tick `2 + 2 (W + 2) - 2 = 2 W + 4`. Widths up to `16` die by tick `32` (the kit's `q01_width_le_16`). That gives `D(W) ≤ 2 W + 4` for `W ≥ 16` (`bwh_death`), and `BWH ⇒ Q01` (`bwh_Q01`).

Neither guard of the exact-width bounds can be dropped, and the module proves it by kernel checks on natural numbers. The start `272125`, binary `1000010011011111101`, has exact odd width `19`, a white cell at depth `18`, and survives to tick `36 = 2 · 19 - 2` (`odd_guard_control`, `odd_guard_needed`). The start `11083`, of exact width `14 = 2 · 6 + 2`, survives to tick `30`, past `2 · 14` (`even_threshold_control`, `even_threshold_needed`). The kit's `small_bwh_control` is the same threshold in stream form, at `n = 5`.

## 6. Worked numbers

The cell below recomputes the death ticks of the two control starts, checks the peel chart on the start `11083` at all `136` pairs `(d, t)` with `t + d ≤ 15` (the start survives to tick `30`), and counts the distinct layer words of lengths `1` to `6` over every start cell and every input.

## 7. Prior art and scope

The chart, `Q01 ⇒ SEP` and `BWH ⇒ Q01` are known. They are in the external Lean development [`lhallee/rule30-open`](https://github.com/lhallee/rule30-open/blob/f877f5afd5609373e2df1639e943d04e3a56e83b/Rule30Open/PeriodTwo/WedgeLadderQ01.lean), whose `zcone_chart` and `zpeel_chart` are the chart for a zero-driven start, and which proves that a binary constant-tail separator is equivalent to `Q01`, that `Q01` implies `ConstantTailSeparator`, and that `BWH` implies `Q01`. They are reproved here in the kit's coordinates. The kit's hypotheses and their period-two consequences are David Condrey's (`Rule30WedgeBridge`, `Rule30SeparatorEquivalences`, `Rule30SEPToPeriodTwo`), with additions by G.P.J.W. Quint; `Q01Gap` and `CQ01Empty_of_Q01Gap` are Renaud Bosdure's (`Rule30GateTrap`). The kit's own unconditional bound `q01_width_le_52_linear` gives `2 W + 8` up to width `52`.

What is new here is the exact class `N`, so `SEP ⇔ QN` and the description of `Q01` as `SEP` plus one class of free bits; `SEP ⇒ Q01Gap`; the width-one-layer form `LR1`; and `BWH` as an equivalence with exact-width death bounds, with the linear bound `2 W + 4` and the two controls. The statements were found in the project's swarm and carried by hand in the [project's record](https://github.com/ghywel/placego/blob/main/PROOFS.md); the width-`19` witness is the swarm skeptic's. The record's own version of `LR1` runs its clock from a white tick and needs a one-tick repair. The kit's sideways convention starts black, so it needs none.

Read through the dictionary, the wedge horizons `M(n, c)` of `BWH` are exact-width death times: `M = D / 2 - 1 - n`. An exhaustive search over exact widths reproduces the swarm's table for `n = 5` to `9`: `M(5, 3) = 8` and `M(6, 2) = 9` (why `n ≥ 7` is needed), then `7, 6`, `6, 7` and `5, 8`. That search is in the record, not in this notebook.

Nothing here proves `SEP`, `BWH` or `Q01`, or decides whether `SEP` implies `Q01`: that is exactly the question whether a finite constrained start can have free bits meeting two adjacent whites infinitely often. Problems 1 to 3 stay open.

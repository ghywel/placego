# The Cut Ether Is Off the Single Cell's Edge Cycle: Depth 8 with Phase 16, and No Flush Thirteen-Cell Ether Word on the Single Cell

Gareth Herbert; Claude (Anthropic); GPT (OpenAI). 10 November 2026.

## 1. The statement

The kit's `Rule30ZeroBoundaryBarriers` builds its two-sided barrier from the ether `c7`, the row black exactly at the positions `p ≡ 6 (mod 7)`. It is a rule 30 orbit of period `4`, and its truncations `c7cut N` keep the cells of `[-(7N + 1), 7N + 6]`. The kit's `Rule30FrozenRuler` reads a finite row from its rightmost black cell `e`: bit `k` of its *edge code* is the cell at distance `k` from `e`. The code evolves by the 2-adic right-edge map `T` of Coven, Pivato and Yassawi, with the edge moving one cell per step. A code has *depth `k`* with phase `s₀` when it agrees with the single cell's code at time `s₀` below bit `k`, and no code of the single cell's orbit agrees with it below bit `k + 1`. Then, by `frozen_ruler`, it follows the single cell's code at time `s₀ + t` below bit `k`, and differs from it at bit `k`, for ever.

This module places the cut ether in that picture.

- `cut_code_prefix`, `c7cut_depth`: for every `N`, the edge code of `c7cut N` begins `1 0 0 0 0 0 0 1 0`, and it has depth `8` with phase `16`.
- `c7cut_frozen`: at every time `t`, the code of `c7cut N` agrees with the single cell's code at time `16 + t` below bit `8` and differs from it at bit `8`. The white run behind its edge cell is never `8` or longer.
- `c7cut_off_seed`: more, at no time does it agree below bit `9` with the single cell's code at *any* time.
- `c7cut_not_seed_row`: so no row of the evolution of `c7cut N` is a translate of a row of the single cell.
- `seed_no_flush_ether`: conversely, at every time `s`, phase `a` and position `p`, one of the first thirteen cells of the single cell's row, counted from its rightmost black cell, differs from the ether.
- `seed_flush_ether_sharp`: the bound is sharp. At time `55`, twelve cells agree with the ether at phase `3`.
- `seed_offset_ether_204`: the flush condition is needed. At time `204`, the cells at distances `7` to `19` are the ether at phase `2`.

## 2. Codes as numbers

On the first `k` bits, the edge map is a map of numbers:

`T c = (c xor ((c << 1) or (c << 2))) mod 2^k` (`enc_T`).

Bit `k` of `T c` reads only bits `k - 2` to `k` of `c`, so the first `k` bits of a code evolve by themselves. The single cell starts at the code `1`. Its first nine bits run through a cycle of `32` distinct values that misses `129` (`cycle9`), and its first thirteen bits through a cycle of `64` distinct values (`cycle13`). Every time of the single cell lands on these cycles (`orbit9_mem`, `orbit13_mem`), by induction from the kernel-checked closure of each list under the map.

## 3. The proofs

- **The cut's code.** The edge code of `c7cut N` has bit `k` black exactly when `k` is a multiple of `7` and `k ≤ 14N + 7` (`code_cut`). Its first nine bits are therefore `129`, for every `N`, including `N = 0`, where bit `8` lies outside the cut.
- **Depth.** The single cell's code at time `16` has the same first eight bits (`c7cut_depth`), and no code of the single cell has first nine bits `129`. That is depth `8` with phase `16`, and the kit's `frozen_ruler` gives `c7cut_frozen`.
- **Off the cycle.** The edge map sends every odd nine-bit code off the cycle to an odd code off the cycle (`off9_closed`, checked over all `512` codes); it permutes the odd codes, so the cycle and its complement are both closed. The cut's code starts off the cycle and stays off it, whatever the time, which gives `c7cut_off_seed`.
- **Translates.** If a row of the cut were a translate of a row of the single cell, their rightmost black cells would correspond and their codes would be equal (`c7cut_not_seed_row`).
- **Flush ether words.** The ether has `4` phases and `7` positions. None of its `28` thirteen-cell words, read leftward from a position, lies on the thirteen-bit cycle (`ether_off_cycle13`). Since every flush window of the single cell does lie on it, `seed_no_flush_ether` follows. The white-ended words are excluded by the black edge cell itself.

## 4. Scope

- **The flush condition is part of the theorem.** At time `204`, the single cell does have thirteen ether cells at distances `7` to `19`, a black-ended window behind its edge.
- **The cheap version is weaker.** Whole-row non-equality for the unmodified cuts already follows from span parity: a cut's width stays even, while the single cell's rows have odd width. The depth and the flush exclusion say more. Removing the last black cell of `c7cut 1` gives an odd span with the same forbidden nine-bit prefix.
- **What it does not show.** The single cell's nonfinite past is known (below). Nothing here concerns the center column, the kit's ranking barrier for other finite rows, or Problem 1.

## 5. Worked numbers

The cell below replays the finite facts on actual rule 30 rows, not on the edge map:
- the lengths of the nine-bit and thirteen-bit cycles, and whether `129` is on the first;
- the first nine bits of the codes of `c7cut N` for `N = 0..5`;
- for `N = 0, 1, 2` and `t ≤ 32`, whether the edge code of the cut agrees with the single cell's at time `16 + t` below bit `8` and differs at bit `8`;
- over the single cell's rows up to time `300`, the longest flush agreement with the ether at any phase and position, and its first time;
- whether row `204` carries the ether at distances `7` to `19`.

## 6. Prior art and scope

- **The kit's machinery.** The edge code, its map, depth and the frozen ruler are the kit's `Rule30FrozenRuler`. The 2-adic right-edge map is that of E. Coven, M. Pivato and R. Yassawi, Proc. Amer. Math. Soc. 135 (2007). The cut ether and its period are the kit's `Rule30ZeroBoundaryBarriers`.
- **The single cell's past.** [`lhallee/rule30-open`'s `SeedPastPeriods`](https://github.com/lhallee/rule30-open/blob/1ddcd41186e245d6a001604e15b584981990591a/Rule30Open/Frames/SeedPastPeriods.lean) proves that the single cell has no finite past; we do not claim it.
- **What is new.** The depth and phase of the cut ether, its separation from every phase of the single cell's cycle, and the sharp flush ether exclusion, in Lean.
- **History.** These came from a sub-agent run of our programme. A skeptic's run corrected them to the flush form, and GPT carried the result with an independent finite replay.

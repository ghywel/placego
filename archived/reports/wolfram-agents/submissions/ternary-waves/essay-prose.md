# Free Ternary Codes of Rule 30 Travelling Waves: Three Freely Joining Tiles at Moving Period 12, and Three at Moving Period 15

Gareth Herbert; Claude (Anthropic); GPT (OpenAI). 10 November 2026.

## 1. The statement

Read rule 30 in the frame that moves one cell right per step, `Phi x i = x i xor (x (i+1) or x (i+2))` (the kit's `Rule30RingOrbits`). A row `x : Int → Bool` is a *travelling return* of period `P` when `orbit x P = x`. By the kit's `orbit_eq_iff`, this means that `P` ordinary updates of rule 30 bring the row back, moved `P` cells to the right.

The kit's `Rule30MovingWaves` shows that two 34-cell tiles at period 12 can be joined freely. Every bi-infinite binary code gives a travelling return of exact minimal period 12, so the spatial language at that period grows exponentially, and 12 is the least such period. This module gives a larger alphabet at period 12 and the same construction at period 15:
- **Period 12:** three 34-cell tiles (`tiles12`). Tiles 0 and 2 are the kit's two; tile 1 is new.
- **Period 15:** three 31-cell tiles (`tiles15`).

For each family:
- `free_ternary_period_twelve`, `free_ternary_period_fifteen`: an injective map from all bi-infinite ternary codes `Int → Fin 3` to rows of exact minimal moving return `P`.
- `ternary_marked_rings_twelve`, `ternary_marked_rings_fifteen`: for every `k > 0`, an injective family of `3^k` marked rings of size `L k`, each of exact minimal moving return `P`.
- `ternary_words_twelve`, `ternary_words_fifteen`: an injective map from ternary words of length `n / L` to binary words of length `n` that occur in rows with `orbit x P = x`.
- `ternary_wave_twelve`, `ternary_wave_fifteen`: the physical form, `evol (field code 0) P (i + P) = field code 0 i`.

So at least `3^⌊n/34⌋` words of length `n` occur in rows of moving period 12, and at least `3^⌊n/31⌋` in rows of moving period 15. That is at least `log₂3 / 34 ≈ 0.047` and `log₂3 / 31 ≈ 0.051` bits per cell, against the kit's `1/34 ≈ 0.029` at period 12.

## 2. Tiles and seams

A family `Tiles` has a length `L`, a period `P` and three tiles. Each tile lists, for each offset `r < L`, a time profile: bit `t` of it is the cell at offset `r` and phase `t`, read modulo `P`. The field of a code puts at site `i` the cell at offset `i mod L` of tile `code (i div L)`.

The moving frame updates a cell from itself and its two right neighbours. So the field obeys the rule everywhere as soon as every pair of tiles `a b` obeys it at every offset and phase across their seam (`Certificate`). The kernel checks this by `decide +kernel`:
- `tile_certificate12`: 9 seams × 34 offsets × 12 phases = 3672 identities;
- `tile_certificate15`: 9 seams × 31 offsets × 15 phases = 4185 identities.

Then `phi_field` and `orbit_field` identify the field at phase `t` with the `t`-th iterate of its phase-0 row, and `period` closes the loop at `P`. These are proved once, for every `L`, `P` and profile data, and instantiated twice.

## 3. Exact return and decoding

- `exact_period`: if a row returned at some `0 < d < P`, then the tile `code 0` would repeat its phase-0 row at phase `d`. The kernel checks that no tile of either family does that (`Exact`), so the least moving return is exactly `P` for every code.
- `decode12`, `decode15`: two phase-0 cells of each block read the code back. At period 12 the cells at offsets 20 and 23 are `(0,1)`, `(0,0)`, `(1,0)` for tiles 0, 1, 2. At period 15 the cells at offsets 6 and 23 are `(1,1)`, `(0,0)`, `(1,0)`. So the map from codes to rows is injective, and periodic codes give distinct marked rings.

## 4. Scope

These are explicit lower bounds on the travelling-wave language at two periods. They say nothing about other periods. In particular they say nothing about 13 and 14, or about whether 15 is the next period with positive spatial entropy. They do not determine the exact spatial entropy at period 12 or 15, and no statement about stationary periods. The rings counted are marked rings, not rotation classes. The single seed is not addressed.

## 5. Worked numbers

The cell below checks, independently of the Lean module:
- the seam identities of both families, in the moving frame;
- every ring made of one to three tiles, 39 per family, evolved by Wolfram Language's own `CellularAutomaton[30, …]` on a cycle. Each must come back moved `P` cells right after `P` ticks, and at no earlier tick `d` moved `d` cells;
- the decoder cells.

## 6. Prior art and scope

- **The method and two of the tiles** are those of the kit's `Rule30MovingWaves` (Emerson Villafuerte, portal entry R30-20261108-9933fc). Tiles 0 and 2 at period 12 are its `zeroProfiles` and `oneProfiles`, restated here because the verifier's kit does not yet contain that module.
- **The frame** is the kit's `Rule30RingOrbits`.
- **What is new:** the third freely joining 34-cell tile at period 12; the three 31-cell tiles at period 15; and the generic development, which certifies any such family by one finite check.
- **History.** GPT found the third period-12 tile in its analysis of the period-12 return state. Cloud found the period-15 tiles by a search of the profile graph. GPT checked both literal families independently, and a Local sub-agent formalized them under Local's direction. The profile-graph framework is the swarm's LN-12; Cloud carried the period-12 return construction in its [period-12 read](https://github.com/ghywel/placego/blob/main/reports/CLOUD-PERIOD12-CARRY-20261110.md), and the period-15 lists are in its [tile report](https://github.com/ghywel/placego/blob/main/reports/CLOUD-PERIOD15-TILES-20261110.md).

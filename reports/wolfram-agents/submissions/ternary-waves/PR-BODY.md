Rule30TernaryWaves: free ternary codes of travelling waves at moving periods 12 and 15 (PORTAL-ID)

This adds `lean/Ruliology/CellularAutomata/Rule30TernaryWaves.lean`, with its `public import` line in `lean/Ruliology.lean` after `Rule30MovingWaves` and a row in *Added in the kit*. It imports only `Rule30Prize` and `Rule30RingOrbits`.

**What it proves.** In the frame `Rule30RingOrbits.Phi`, a row is a travelling return of period `P` when `orbit x P = x`.
- `tile_certificate12`: three 34-cell tiles at period 12 join freely, with 3672 seam identities by `decide +kernel`. Tiles 0 and 2 are the two tiles of `Rule30MovingWaves`.
- `tile_certificate15`: three 31-cell tiles at period 15 join freely, with 4185 identities.
- `free_ternary_period_twelve`, `free_ternary_period_fifteen`: an injective map from all bi-infinite ternary codes to rows of exact minimal moving return `P`.
- `ternary_marked_rings_*` give `3^k` marked rings of size `L k`, and `ternary_words_*` give at least `3^(n / L)` words of length `n`. That is at least `log2(3)/34` and `log2(3)/31` bits per cell.
- `ternary_wave_*`: the physical form, `evol x P (i + P) = x i`.
- `decode12`, `decode15`: two phase-0 cells per block read the code back.

**Method.** That of `Rule30MovingWaves`, written once for any tile length, period and profile data (`Tiles`, `Certificate`, `Exact`, `Decoder`) and instantiated twice. Exactness is checked tile by tile: no tile repeats its phase-0 row at an earlier phase. The lists are restated rather than imported from `Rule30MovingWaves`, which the verifier's kit `5fb59158` does not yet contain.

**Checks**, with Lean 4.35.0, at main `03a19bf`:
- `lake build Ruliology.CellularAutomata.Rule30TernaryWaves`: no warnings, about 1 s.
- The kit's own `Check.lean --claim partial` passes all 12 headlines, with 157 constants and no new axioms.
- The portal form passes `Check` at the verifier's kit `5fb59158`.
- The compiler rejected all six mutations tested:
  - one bit flipped in the new period-12 tile;
  - one bit flipped in a period-15 tile;
  - tile length 33;
  - period 14;
  - each decoder altered.
- The worked numbers agree in Python and Wolfram Language. Every ring of one to three tiles, 39 per family, returns under ordinary rule 30 moved `P` cells right after exactly `P` ticks, and the decoder cells are as stated.
- Not run: the full catalog build (`bash build_all.sh`).

**Prior art.** The method, the frame and two of the period-12 tiles are those of `Rule30MovingWaves` (Emerson Villafuerte, R30-20261108-9933fc) and `Rule30RingOrbits`. New here: the third freely joining 34-cell tile, the three 31-cell tiles at period 15, and the generic development.

**What it does not do.** It claims nothing about other periods, nor that 15 is the next period with positive spatial entropy. It does not determine the exact spatial entropy at period 12 or 15, and no statement about stationary periods.

Portal entry: [PORTAL-ID](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/PORTAL-ID).

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Rule30PlantedSurvivor: rule 30's survival table with one row added, by a tree automorphism of the rows (PORTAL-ID)

This adds `lean/Ruliology/CellularAutomata/Rule30PlantedSurvivor.lean`, with its `public import` line in `lean/Ruliology.lean` after `Rule30ZeroBoundaryStripeCascade` and a row in *Added in the kit* after the same module. It imports only `Rule30ZeroBoundaryBarriers`.

**What it proves.** A survival table alone cannot decide `Q01`. For `L ≥ 1`, `psi L` flips the cell at every odd depth `k ≥ 2 L + 1` at which the row agrees with the stripe `…10101` at every depth below `k`.
- `psi_psiInv`, `psiInv_psi`: `psi L` is a bijection of rows, with inverse `psiInv L`.
- `psi_stripe`: `psi L` sends the stripe to the finite row `trunc (2 L - 1)`.
- `psiInv_fin`: `psiInv L` keeps the width of every finite row except `trunc (2 L - 1)`.
- `Tn_eq`, `T_finite`, `T_zero`: the map `T L y = psi L (zrow (psiInv L y) 1)` iterates as `psi L` of rule 30's iterates, maps finite rows to finite rows and fixes the empty row.
- `T_fixed`, `fixed_survives`: `T L` fixes `trunc (2 L - 1)`, whose depth `1` is black at every time.
- `survival_table`: for every width bound `W` and time `t`, the rows of width at most `W` that pass every even check of depth `1` through `t` number the same under `T L` as under rule 30, plus one exactly when `2 L - 1 ≤ W` and `2 ⌈W / 2⌉ ≤ t`.

**Method.** The flip at depth `k` reads only the depths below `k`, so `psi L` is a tree automorphism and its inverse is computed depth by depth (`ipf`, `psiInv`). Depth `1` lies below every flip site, so survival under `T L` is survival under rule 30 of the inverse row. Inside the range, `psiInv L` maps the rows of width at most `W` other than `trunc (2 L - 1)` injectively into those other than `trunc (2 ⌈W / 2⌉ - 1)`, which dies exactly at time `2 ⌈W / 2⌉` (the kit's `trunc_survives`). A pigeonhole lemma on a finite range (`pigeon`, `cnt_perm`) gives the count.

**Checks**, with Lean 4.35.0, at main `03a19bf`:
- `lake build Ruliology.CellularAutomata.Rule30PlantedSurvivor`: no warnings, under 1 s.
- The kit's own `Check.lean --claim partial` passes all 10 headlines, with 266 constants and no new axioms.
- The portal form passes `Check` at the verifier's kit `5fb59158`.
- The compiler rejected all five mutations tested: no extra row in the table, flip sites at even depths, the width lemma without its exception, the extra row from `2 L ≤ W`, and the fixed row `trunc (2 L + 1)`.
- The worked numbers agree in Python and Wolfram Language: the table identity for `L = 1, 2, 3`, every `W ≤ 10` and every `t ≤ 14` (495 cases), direct iteration of `T L` against rule 30 on the inverse row, and the fixed row.
- Not run: the full catalog build (`bash build_all.sh`).

**Prior art.** The stripe, its truncations, `trunc_survives` and `zrow` are the kit's (`Rule30ZeroBoundary`, `Rule30ZeroBoundaryBarriers`). Conjugating a system by a homeomorphism that moves a repelling point onto a finite configuration is a standard idea. What is new is the exact table identity and this finite-state witness of it.

**What it does not do.** `T L` is not a cellular automaton and not rule 30. Nothing here decides `Q01`, and nothing is claimed about tables restricted to physical left halves of rule 30.

Portal entry: [PORTAL-ID](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/PORTAL-ID).

🤖 Generated with [Claude Code](https://claude.com/claude-code)

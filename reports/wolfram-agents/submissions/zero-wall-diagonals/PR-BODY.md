Rule30ZeroWallDiagonals: zero-wall left diagonals, bounded lag and factor complexity of the free word (PORTAL-ID)

This adds `lean/Ruliology/CellularAutomata/Rule30ZeroWallDiagonals.lean`, with its `public import` line in `lean/Ruliology.lean` after `Rule30LeftAntiPeriod` and a row in *Added in the kit* after the same module. It imports `Rule30LeftUnbounded` and `Rule30ZeroBoundary`.

**What it proves.** It shows what a counterexample to `Q01` would have to look like.
- `E_entry`, `E_tailLeft`: for a finite row with last black cell at depth `m ≥ 1`, the diagonals measured from the moving edge, `E L m j t = zrow L t (m + t - j)`, obey the left-diagonal recurrence exactly from their entry time `j + 2 ≤ m + t`, equality included. This is `zrow_succ`; at equality the right input is the wall.
- **The `TailLeft` package**, for every array whose recurrence holds eventually at each index:
  - `tail_periodic`: eventual period `2 ^ j`;
  - `tail_profile_bound`: `M + 3 ≤ 2 ^ (2 Q)` for `Q`-periodic profiles;
  - `tail_white_unbounded`, `tail_no_two_white`, `tail_black_after_white`, `tail_black_unbounded`: eventually black coordinates at arbitrarily large index.

  `E_black_unbounded` instantiates this for the zero wall.
- `row_eq_Theta`, `rows_agree`, `freeWord_bounded_lag`, `freeWord_bounded_lag_of_finSupp`: for a finitely supported constrained row, bounded-slack repeats of the free word `freeWord L s = zrow L (2 s + 1) 1` have bounded lag.
- `le_factorCount`, `factorCount_le`, `factorCount_succ`, `rightSpecialCount_pos`, `two_run`: a core-Lean factor count, pinned as the number of distinct factors, with the binary special-factor identity, the Morse–Hedlund step, and an explicit two-run witness.
- `complexity_of_bounded_lag`, `freeWord_complexity`: such a free word has factor complexity above `n + K` eventually, for every `K`.

**Scope.** Finitely supported constrained rows exist only if `Q01` fails, so the free-word statements are conditional. The diagonal statements hold for every finite row. No rate is claimed for the complexity excess.

**Checks**, with Lean 4.35.0, at main `03a19bf`:
- `lake build Ruliology.CellularAutomata.Rule30ZeroWallDiagonals`: no warnings.
- The kit's own `Check.lean --claim partial` passes all 20 headlines, with 324 constants and no new axioms.
- The portal form passes `Check` at the verifier's kit `5fb59158`, where `Rule30ZeroBoundary` and `Rule30LeftReset` lack only later appended declarations, none of them used here.
- The compiler rejected all six mutations tested:
  - the entry guard one step early;
  - the second diagonal black from time 0;
  - the factor count rising by exactly 1;
  - the two-run lemma with `M ≥ L + q`;
  - right-special factors of every length for every word;
  - the complexity bound without aperiodicity.
- The worked numbers agree in Python and Wolfram Language:
  - the edge-diagonal recurrence holds inside the guard and fails just outside it;
  - late periods divide `2 ^ j`;
  - the Fibonacci word has `n + 1` factors and one right-special factor per length.
- Not run: the full catalog build (`bash build_all.sh`).

**Prior art.** The left-diagonal theory and profile bound are the kit's `Rule30Diagonals`, `Rule30LeftReset` and `Rule30LeftUnbounded`, for the single seed, ported here with entry-time guards. Morse–Hedlund's complexity bound and the binary special-factor count (Cassaigne, 1997) are classical and are reproved in core Lean; the kit's `ShiftOrbit` and `WordsAutomata` have Mathlib versions. Repetitions in low-complexity words are studied by Bugeaud and Kim (2019). No priority is claimed for the abstract word implication.

**What it does not do.** It does not decide `Q01`, gives no quantitative rate, and does not include the separate near-square claim.

Portal entry: [PORTAL-ID](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/PORTAL-ID).

🤖 Generated with [Claude Code](https://claude.com/claude-code)

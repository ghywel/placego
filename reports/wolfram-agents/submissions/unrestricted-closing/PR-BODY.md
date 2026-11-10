Rule30UnrestrictedClosing: unrestricted tail closing fails on the constrained class of the zero-boundary left half (PORTAL-ID)

This adds `lean/Ruliology/CellularAutomata/Rule30UnrestrictedClosing.lean`, with its `public import` line in `lean/Ruliology.lean` after `Rule30ZeroBoundaryStripeFour` and a row in *Added in the kit*. It imports only `Rule30Prize` and `Rule30ZeroBoundary`.

**What it proves.** Three eventually periodic starts of the zero-boundary left half, read from depth 1:
- `rowA` repeats `1011111`;
- `rowB` is `11` followed by repeats of `01001011001000`;
- `rowC` repeats `1100001`.

With `G` for two ticks:
- `two_A`, `two_B`, `two_C`, `two_cycle`: `G A = G B = C` and `G C = A`, at every depth.
- `inX_A`, `inX_B`, `inX_C`: all three are in `InX`.
- `free_A`, `free_B`, `free_C` give their free words; `theta_A`, `theta_B`, `theta_C` give each row as `Theta` of its free word.
- `differ_AB`: `A` and `B` differ at every depth `14 q + 3`. `differ_one_tick`: one tick later they differ at every depth `14 q + 4`.
- `not_unrestricted_closing`: two rows of `InX` with the same row after one double step need not agree on any tail.

**Method.** Two ticks at depth `k ≥ 3` read depths `k - 2 .. k + 2` only, so each identity is checked on one period of depths by `decide` and carried along the period. Membership and free words follow by induction along the cycle, and `Theta_unique` gives the identification.

**Checks**, with Lean 4.35.0, at main `03a19bf`:
- `lake build Ruliology.CellularAutomata.Rule30UnrestrictedClosing`: no warnings, under 1 s.
- The kit's own `Check.lean --claim partial` passes all 16 headlines, with 82 constants and no new axioms.
- The portal form passes `Check` at the verifier's kit `5fb59158`.
- The compiler rejected all six mutations tested:
  - one bit of `rowA` flipped;
  - one bit of `rowB`'s period flipped;
  - the fixed-point reading `G C = C`;
  - the mismatch at `14 q + 4` instead of `14 q + 3`;
  - `fB` without its two leading whites;
  - the one-tick values swapped.
- The worked numbers agree in Python and Wolfram Language. On the first 600 depths: the three identities, black even heads for 40 double steps, the free words, and the exact mismatch residues `0, 1, 3, 5, 6, 8, 9, 11, 12` modulo 14.
- Not run: the full catalog build (`bash build_all.sh`).

**Prior art.** The framework is `Rule30ZeroBoundary`. The closest statements are the guarded `HomoclinicClosing` and `AllPastClosing` of open PR #52 (`Rule30GateTailReduction`), which assume legal gate streams, and PR #47's synchronizing-carrier families. Neither is contradicted. In PR #52's convention the common future here begins with the window value `85`, outside its ten legal windows, so its legality guard cannot be dropped.

**What it does not do.** It says nothing about legal gate streams or finite rows, and nothing here decides `Q01` or period 2.

Portal entry: [PORTAL-ID](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/PORTAL-ID).

🤖 Generated with [Claude Code](https://claude.com/claude-code)

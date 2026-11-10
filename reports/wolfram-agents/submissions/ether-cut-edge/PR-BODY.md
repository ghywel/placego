Rule30EtherCutEdge: the cut ether is off the single cell's edge cycle (R30-20261110-1f7087)

This adds `lean/Ruliology/CellularAutomata/Rule30EtherCutEdge.lean`, with its `public import` line in `lean/Ruliology.lean` and a row in *Added in the kit* after `Rule30FrozenRuler`. It imports `Rule30FrozenRuler` and `Rule30ZeroBoundaryBarriers`.

**What it proves**, with `Rule30FrozenRuler`'s edge codes, map `T`, `HasDepth` and `frozen_ruler`, and the cut ether `c7cut` of `Rule30ZeroBoundaryBarriers`:
- `cut_code_prefix`, `c7cut_depth`: for every `N`, the edge code of `c7cut N` begins `1 0 0 0 0 0 0 1 0` and has depth `8` with phase `16`.
- `c7cut_frozen`: so at every time it agrees with the single cell's code at time `16 + t` below bit `8`, differs at bit `8`, and has no white run of `8` or more behind its edge cell.
- `c7cut_off_seed`: at no time does it agree below bit `9` with the single cell's code at any time.
- `c7cut_not_seed_row`: so no row of its evolution is a translate of a row of the single cell.
- `seed_no_flush_ether`: no row of the single cell has thirteen ether cells flush with its rightmost black cell, at any phase and position.
- `seed_flush_ether_sharp`: twelve occur at time `55`.
- `seed_offset_ether_204`: without the flush condition, thirteen occur at time `204`, at distances `7..19`.

**Method.**
- On `k`-bit codes the edge map is `c xor ((c << 1) or (c << 2))` modulo `2 ^ k` (`enc_T`).
- The first nine bits of the single cell's code run through a cycle of `32` values that misses `129` (`cycle9`). The odd codes off the cycle stay off it (`off9_closed`, all `512` codes).
- The first thirteen bits run through a cycle of `64` values (`cycle13`). None of the `28` thirteen-cell ether words is on it (`ether_off_cycle13`).
- All finite facts are `decide +kernel`.

**Checks**, with Lean 4.35.0, at main `03a19bf`:
- `lake build Ruliology.CellularAutomata.Rule30EtherCutEdge`: no warnings, about 1 s.
- The kit's own `Check.lean --claim partial` passes all 11 headlines, with 88 constants and no new axioms.
- The portal form passes `Check` at the verifier's kit `5fb59158`, where the three modules it uses are byte-identical.
- The compiler rejected all six mutations tested.
- The worked numbers, computed on actual rule 30 rows in Python and Wolfram Language, agree.
- Not run: the full catalog build (`bash build_all.sh`).

**Prior art.** The edge codes, depth and the frozen ruler are `Rule30FrozenRuler`, whose edge map is that of Coven, Pivato and Yassawi. The single cell's nonfinite past is the external `lhallee/rule30-open`'s `SeedPastPeriods`. Whole-row non-equality for the unmodified cuts already follows from span parity; the depth and the flush statements say more.

**What it does not do.** Nothing here concerns the center column, the ranking barrier for other finite rows, or Problem 1.

Portal entry: [R30-20261110-1f7087](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261110-1f7087).

🤖 Generated with [Claude Code](https://claude.com/claude-code)

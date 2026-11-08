Rule30PeriodThreeLanguage: the column-1 language beside a period-3 center, and left statements that still exclude period 3 (PORTAL-ID)

This adds `lean/Ruliology/CellularAutomata/Rule30PeriodThreeLanguage.lean`, with its `public import` line in `lean/Ruliology.lean` and a row in *Added in the kit*. It imports `Rule30PeriodTwoLanguage` and `Rule30EtherThreeSkeleton`.

**What it proves.** These are statements about the seed, as `Cert.sound_bad` is.
- `occurs3`, `no_pattern3`: `Rule30PeriodTwoLanguage`'s subset simulation of the bad class, extended to period 3. Each letter takes three ticks, and the path stays in the bad class at every tick.
- `col1_011` (certificate at strip width `7`): beside an eventual `011` center, column `1` at phase `0` eventually never spells `00`, `011110`, `111010`, `0101010`, `0101110`, `01011010`, `11101110` or `111011010`.
- `col1_001` (width `10`): beside `001`, column `1` at phase `1` eventually never spells `010`, `101`, `11111`, `000000`, `100111`, `111001`, `00000111`, `01110001`, `10011001` or `11100000`. So its black runs have length `2..4` and its white runs `2..5`.
- `free_bits_011`, `free_bits_001`: column `-1` never spells the complements (`col_m1_011`, `col_m1_001_skeleton`).
- `C3r011` and `C3g001` (open) restrict `C3w w011` and `C3s001` to left configurations whose free bits also avoid those complements.
  - `C3r011_of_C3w`, `C3g001_of_C3s`: the kit's statements imply them.
  - `not_eventually_011_of_C3r`, `not_eventually_001_of_C3g`: each still excludes its tail.
  - `no_eventual_period_three_of_C3g`: together they exclude an eventually 3-periodic center.

**Checks**, with Lean 4.35.0, at main `1487f31`:
- `lake build Ruliology.CellularAutomata.Rule30PeriodThreeLanguage`: no warnings, about 12 s on an M5 MacBook Pro.
- The kit's own `Check.lean --claim partial` passes all 10 headlines. It replays 142 constants and finds no new axioms; every headline's axioms are within `propext`, `Classical.choice`, `Quot.sound`.
- Positive controls by `decide`: the control words `11` and `0110111` (beside `011`) and `11`, `0011` and `110011` (beside `001`) occur in the bad classes. So the exclusions are not vacuous.
- The compiler rejected all nine mutations tested:
  - a control word added to each word list (`1001` beside `001` needs width `13`);
  - the wrong center word, the wrong bad rank, and one corrupted rank;
  - the wrong reading phase in `col1_001`, `C3r011` and `C3g001`;
  - the dropped complement in `C3r011`.
- The worked numbers agree in Python and Wolfram Language: the cyclic components of both strip graphs, and the occurrence of every listed word in the bad class.
- The portal form, with the same proofs, passes `Check` at the verifier's kit `5fb59158`.
- Not run: the full catalog build (`bash build_all.sh`).

**Prior art.** The external development [`lhallee/rule30-open`](https://github.com/lhallee/rule30-open/tree/f877f5afd5609373e2df1639e943d04e3a56e83b) treats period 3 as well.
- `ThreeRuns` proves that beside `001` column `1` at the second white step avoids `010`, `101` and `1001`, for every right half.
- `ConstrainedLeft001` reduces `001` to `C3r001`, `C3s001` restricted by that language. Our word list adds upper run bounds and longer exclusions, while the width-10 strip still admits `1001`. This comparison of word restrictions proves no logical independence of the open left statements.
- Beside `011`, `reading-constraints.md` computes `00`, `010`, `01110` and `011110`. The full list is not forced for every right half, but `011110` is already computed as unconditionally forbidden at width 7, and `00` is forced unless the readings are eventually white. These prior computational exclusions have no Lean there. The upper run bounds beside `001` appear as sampled, not forced.

What is new here is the period-3 path check, the `011` language and the `001` upper bounds in Lean, and the restricted statements `C3r011` and `C3g001` with their reductions. The method is the kit's: bad-class certificates with masked Jen (`Rule30PeriodFourSkeleton`) and `Rule30PeriodTwoLanguage`.

**What it does not do.** None of `C3r011`, `C3g001` or the absence of period 3 is proved. The separate finite-word growth estimates through width 22 are not certified entropy values, a positive infinite-width limit, or a proof that every finite left game survives.

Portal entry: [PORTAL-ID](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/PORTAL-ID).

🤖 Generated with [Claude Code](https://claude.com/claude-code)

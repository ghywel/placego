Rule30EtherThreeNotAbsorption: AbsorptionT t001 is false, after lhallee/rule30-open (PORTAL-ID)

This adds `lean/Ruliology/CellularAutomata/Rule30EtherThreeNotAbsorption.lean`, with its `public import` line in `lean/Ruliology.lean` and a row in *Added in the kit*. It imports only `Rule30EtherThreeTrap`. It also corrects two status lines of `lean/README.md` that call `AbsorptionT t001` open: the period-3 line of the status table and the `Rule30EtherThreeTrap` row.

**What it proves**, with the kit's own definitions (`PTrap`, `PTrap.check`, `PTrap.invariant`, `AbsorptionT`, `t001`):
- `trap001fifteen_check`: `trap001fifteen` is a checked `PTrap` for `001` of period `15`, with `52` cells and `153` states.
- `fifteen_apart_t001`: no state of it, cut to `47` cells, is a state of `t001` at a label of the same phase. The kernel compares all `124,695` pairs.
- `stays`: the right half given by its state `0` keeps its first `52` cells in the trap for ever.
- `not_absorptionT_t001`: `¬ AbsorptionT t001`.
- `rule30open_half`: the half named in `lhallee/rule30-open` is state `25` of the same table.

`not_eventually_001_of_absorption` stays true but its hypothesis is false. The empty right half still enters `t001` (`Rule30EtherThreeReach.absorbed_empty`, at step 1270).

**Credit.** The theorem and the trap are Logan Hallee's, in [`lhallee/rule30-open`, `Rule30Open.Columns.Traps001`](https://github.com/lhallee/rule30-open/blob/1ddcd41186e245d6a001604e15b584981990591a/Rule30Open/Columns/Traps001.md) (Apache-2.0). That module proves more: four pairwise apart traps for `001`, and entry into one of any three of them fails. Our agent found the period-15 table independently, and this file restates the first theorem with the kit's `PTrap` machinery; no code is copied. The header of `Rule30EtherThreeErosion` also calls the statement open; it is a docstring in another module, left unchanged here.

**Checks**, with Lean 4.35.0, at main `03a19bf`:
- `lake build Ruliology.CellularAutomata.Rule30EtherThreeNotAbsorption`: no warnings, 3.8 s, 1.1 GB.
- The kit's own `Check.lean --claim partial` passes all 5 headlines, with 34 constants and no new axioms.
- The portal form passes `Check` at the verifier's kit `5fb59158`, where `Rule30EtherThreeTrap` is byte-identical.
- The worked numbers agree in Python and Wolfram Language. Driven by `001`, neither witness enters `t001` within 3,000 steps, and the empty half enters at step 1270.
- Not run: the full catalog build (`bash build_all.sh`).

**What it does not do.** It does not decide whether the center column can be eventually `001`. `Q001`, `C3s001` and `C3w(011)` stay open.

Portal entry: [PORTAL-ID](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/PORTAL-ID).

🤖 Generated with [Claude Code](https://claude.com/claude-code)

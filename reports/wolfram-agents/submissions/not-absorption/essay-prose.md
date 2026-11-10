# AbsorptionT t001 Is False: a Period-15 Trap for 001, after lhallee/rule30-open

Gareth Herbert; Claude (Anthropic); GPT (OpenAI). 10 November 2026.

## 1. The statement

For the word `001` of least period three, the kit's `Rule30EtherThreeTrap` gives a trap: `t001` is a set of `815` states of the first `47` columns beside the center, each with a label modulo `21`, closed under both values of column `48`. If the right half of rule 30 enters it while the center column repeats `001`, column `1` becomes periodic at the white times, which masked Jen forbids. So the kit reduces `001` to an entry statement.

`AbsorptionT t001`: every finitely supported right half driven by `001`, from any phase, eventually has its first `47` cells in a state of `t001` at a label of the same phase. It implies that the center column is not eventually `001` repeated (`not_eventually_001_of_absorption`). The kit's status table, its `Rule30EtherThreeTrap` row and the header of `Rule30EtherThreeErosion` all list it as open.

It is false:

- `trap001fifteen_check`: `trap001fifteen` is a checked `PTrap` for `001`, with `52` cells, labels modulo `15` and `153` states, closed under both values of column `53`.
- `fifteen_apart_t001`: no state of `trap001fifteen`, cut to its first `47` cells, is a state of `t001` whose label has the same phase. The kernel compares all `153 × 815 = 124,695` pairs.
- `stays`: the right half whose cells `1..48` are the state `0` of `trap001fifteen`, white beyond, driven by `001` from phase `0`, keeps its first `52` cells in the trap at every step, with the label counting the time. This is the kit's own `PTrap.invariant`.
- `not_absorptionT_t001`: so that half never enters `t001`, and `¬ AbsorptionT t001`.
- `rule30open_half`: the right half that `lhallee/rule30-open` names as its witness is the state `25` of the same table, at label `3`, which has the same phase.

## 2. Why two traps cannot share an orbit

This explains why the two traps can be apart; the proof is the kernel check `fifteen_apart_t001`, state by state. Both traps are closed, so a half that entered `t001` from `trap001fifteen` would stay in both for ever. On each trap, column `1` at the white phases is a function of the label, with period `21` on `t001` and period `15` on `trap001fifteen`. In both at once, that column would repeat with period `3` at the white times, which the function for `t001` does not do.

## 3. What it changes in the kit

`not_eventually_001_of_absorption` stays true, but its hypothesis is false, so it gives nothing. The kit's route for `001` needs a weaker entry statement. A half that starts in one trap stays in it, so entry into one of a list of traps fails whenever some further trap is apart from every trap of the list; `rule30-open` shows this for any three of its four. What remains is entry into one of a longer list, or into some trap. The empty right half does enter `t001`, at step `1270` (`Rule30EtherThreeReach.absorbed_empty`). Whether the center column can be eventually `001` remains open.

## 4. Worked numbers

The cell below reads the kit's packed table for `t001` and runs three right halves for `3,000` steps, driven by `001` from phase `0`: the module's witness, the half named by `rule30-open`, and the empty half. For each it gives the first step at which cells `1..47` are a state of `t001` at a label of the same phase, or `-1` if there is none. For the two witnesses it also gives the number of distinct `52`-cell windows seen.

## 5. Prior art and credit

The theorem and the trap are Logan Hallee's: [`lhallee/rule30-open`, `Rule30Open.Columns.Traps001`](https://github.com/lhallee/rule30-open/blob/1ddcd41186e245d6a001604e15b584981990591a/Rule30Open/Columns/Traps001.lean), with its note [Traps001](https://github.com/lhallee/rule30-open/blob/1ddcd41186e245d6a001604e15b584981990591a/Rule30Open/Columns/Traps001.md). That module proves more:
- there are four traps for `001`, pairwise apart;
- entry into one of any three of them fails;
- entry into some trap of `001` would still exclude it.

Our agent PE-1 found the period-15 table independently while searching traps for `001`, and our replay BN-L1 checked the refutation with the kit's `PTrap` machinery before we saw that rule30-open already had it. This module is that replay, cleaned for the kit.

We submit it, with the owner's approval and full credit, because the kit and the portal still list the statement as open. What is ours is only the kit-form restatement and its check. Nothing here decides Problem 1 for period three.

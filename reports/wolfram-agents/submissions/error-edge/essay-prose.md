# The error edge of two rule 30 configurations never retreats, heals exactly at a black parent, and obeys six laws after a heal

Gareth Herbert; Claude (Anthropic); GPT (OpenAI). 5 November 2026.

## 1. The object

Take two configurations of rule 30, each with a leftmost black cell, and read each in the wall frame: wheel `j` at tick `t` is the cell at position `lo − t + j`, with `lo` the initial leftmost black cell (`Rule30FiniteDiagonals.Ld`). The wheels of a configuration satisfy the kit's left-diagonal recurrence (`Rule30AgedLeftDiagonals.Recurrence`): wheel 0 is constant, wheel 1 at tick `t + 1` is the or of wheels 0 and 1 at tick `t`, and wheel `i + 2` at tick `t + 1` is `xor (wheel i) (wheel (i + 1) || wheel (i + 2))` read at tick `t`. Everything below is proved for any two arrays `a`, `b` with this recurrence, so it holds for any two configurations with leftmost black cells, whatever lies to their right, and in particular for a configuration against a periodic strip.

Say that `a` and `b` **agree below `m`** at tick `t` when they are equal on every wheel `j < m` (`Agree a b m t`), and that their **error edge is at `m`** when they agree below `m` and differ at `m` (`Edge a b m t`). The edge is the left end of the difference pattern of the two configurations, the object whose average leftward speed in the ordinary frame Wolfram reports as about 0.2428 cells per step (Grassberger's measurement); in the wall frame the edge moves up at about 0.757 wheels per tick. The theorems here are its exact one-step laws; they say nothing about the speed.

## 2. The barrier and the heal

**The edge never retreats (`agree_step`, `agree_after`, `edge_le`).** A wheel reads only itself and the two wheels below it, so two arrays that agree below `m` at a tick agree below `m` at every later tick. Hence if the edge is at `m` at tick `t` and at `m′` at tick `t + n`, then `m ≤ m′`.

**The heal criterion (`heal_iff`).** Let the edge be at `m + 1` at tick `t`. Then `a` and `b` agree on wheel `m + 1` at tick `t + 1` if and only if wheel `m` of `a` (equally of `b`, since they agree there) is black at tick `t`. For `m = 0` this is the or of wheel 0 with the differing wheel 1; for `m ≥ 1` the differing wheel enters an or with the black parent, which absorbs it, or with a white parent, which exposes it. So with a white parent the edge is still at `m + 1` one tick later (`edge_stall`), and with a black parent the two arrays agree on every wheel through `m + 1` one tick later (`edge_heal`): the edge has moved up, by a jump of at least one.

## 3. Six laws after a heal

Let the edge be at `m + 2` at tick `t` with its parent, wheel `m + 1`, black. The wheels above the old edge at tick `t + 1` are then constrained, whatever the two arrays carried there at tick `t`.

**`white_above`.** If wheel `m + 3` agrees at tick `t + 1`, it is white there. **`black_two_above`.** If wheels `m + 3` and `m + 4` agree at tick `t + 1`, wheel `m + 4` is black there.

Write `d` for the jump, the new edge being at `m + 2 + d`, and the **new parent** for wheel `m + 1 + d`.

| jump | law | theorem |
|---|---|---|
| 2 | the new parent is white at `t + 1` | `jump_two` |
| 3 | the new parent is black at `t + 1` | `jump_three` |
| 4 | the new parent is black at `t + 2`, whatever it was at `t + 1` | `jump_four` |
| 5 | if the new parent is white at `t + 1`, it is black at `t + 2` | `jump_five` |
| 6 | if the new parent is white at `t + 1`, it is white at `t + 2` | `jump_six` |
| 7 | if the new parent is white at `t + 1`, it is white at `t + 2` | `jump_seven` |

So after a jump of 2 the edge must stall at least one tick, after a jump of 3 it heals again at once, after a jump of 4 it heals at the second opportunity at the latest, after a jump of 5 at the second opportunity if not the first, and after a jump of 6 or 7 a stall lasts at least two ticks. Jumps of 1 and of 8 or more carry no such constraint at these ticks: the enumeration behind the module shows both values occur for them.

## 4. The proofs

Each law is a Boolean identity in the values of the two arrays on a window of wheels at tick `t`. Unfolding the recurrence once or twice expresses every wheel at ticks `t + 1` and `t + 2` in those values; the edge hypothesis replaces the values of `b` below the edge by those of `a` and the value at the edge by its complement; and the identity is decided by Lean's `decide` over the remaining free Boolean variables, at most thirteen of them for `jump_seven`. The module has no literals, no computation beyond these decisions, and builds in about three seconds; the kit's `Check` replays its 56 constants with the standard axioms `propext` and `Quot.sound`.

## 5. What these laws are for

The error edge is the damage front of rule 30 seen from a single configuration: the lowest wheel on which a configuration differs from a reference, for instance from the periodic strip that every configuration with a leftmost black cell eventually carries on its first wheels (R30-20261104-309041, 458f3b, 9aa447). The heal criterion gives an exact accounting identity for its heal rate, and the six laws fix the first stall after a heal by the jump alone: after a jump of 2 the stall is forced, after 3 it is excluded, after 4 and 5 it ends at the second tick, after 6 and 7 it lasts two ticks at least. In measurements on the seed's strip and on random rows (our record, CL740–CL746) these laws hold on every one of about 300,000 heals, and the stall hazard after the first tick is close to one half.

## 6. Prior art and scope

The barrier and the heal criterion are the two-configuration form of the aligned-parent transport of `Rule30UniversalLeftSide` (`child_same`, `child_white`), where one array is a strip; here neither array is special. The left damage front of rule 30 and its speed are in Wolfram's *Random sequence generation by cellular automata* (1986) and *A New Kind of Science* (p. 949), and the heal identity in diagonal coordinates is in our record (§8.66, 6 October 2026). The six laws after a heal were found by exhaustive enumeration of the window (`jump_facts.py` in our record) and are proved here for the first time as far as we know. Nothing here concerns the center column or the Prize problems.

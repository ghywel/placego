# The error edge of two rule 30 configurations never retreats, heals exactly at a black parent, and obeys six laws after a heal

Gareth Herbert; Claude (Anthropic); GPT (OpenAI). 5 November 2026.

## 1. The object

Take two configurations of rule 30, each with a leftmost black cell, translate their leftmost cells into alignment, and read from that common left edge: wheel `j` at tick `t` is the cell at position `lo − t + j`, with `lo` the initial leftmost black cell (`Rule30FiniteDiagonals.Ld`). The wheels of a configuration satisfy the kit's left-diagonal recurrence (`Rule30AgedLeftDiagonals.Recurrence`): wheel 0 is constant, wheel 1 at tick `t + 1` is the or of wheels 0 and 1 at tick `t`, and wheel `i + 2` at tick `t + 1` is `xor (wheel i) (wheel (i + 1) || wheel (i + 2))` read at tick `t`. Everything below is proved for any two arrays `a`, `b` with this recurrence. `Rule30AgedLeftDiagonals.Ld_recurrence` gives the recurrence for a configuration that is white left of `lo`, so it holds for any two configurations with leftmost black cells, whatever lies to their right, and in particular for a configuration against a periodic strip.

Say that `a` and `b` **agree below `m`** at tick `t` when they are equal on every wheel `j < m` (`Agree a b m t`), and that their **error edge is at `m`** when they agree below `m` and differ at `m` (`Edge a b m t`). The edge is the left end of the difference pattern of the translated configurations. For difference patterns on random backgrounds, Wolfram reports an empirical average leftward speed of about 0.2428 cells per step (Grassberger's measurement), equivalent to about 0.7572 wheels per tick in this moving frame. This is not a speed assertion for every pair. The theorems here concern exact local laws, not a limiting speed.

## 2. The barrier and the heal

**The edge never retreats (`agree_step`, `agree_after`, `edge_le`).** A wheel reads only itself and the two wheels below it, so two arrays that agree below `m` at a tick agree below `m` at every later tick. Hence if the edge is at `m` at tick `t` and at `m′` at tick `t + n`, then `m ≤ m′`.

**The heal criterion (`heal_iff`).** Let the edge be at `m + 1` at tick `t`. Then `a` and `b` agree on wheel `m + 1` at tick `t + 1` if and only if wheel `m` of `a` (equally of `b`, since they agree there) is black at tick `t`. For `m = 0` this is the or of wheel 0 with the differing wheel 1; for `m ≥ 1` the differing wheel enters an or with the black parent, which absorbs it, or with a white parent, which exposes it. So with a white parent the edge is still at `m + 1` one tick later (`edge_stall`), and with a black parent the two arrays agree on every wheel through `m + 1` one tick later (`edge_heal`): if a later error edge exists, it lies strictly higher; the two arrays may instead become identical. For arbitrary recurrence arrays, a difference at wheel 0 is constant and is outside this heal criterion. For the physical anchored rows, wheel 0 is black in both, and wheel 1 is black in both from tick 1.

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

For these jumps, whose old edge is at least 2, the new edge stalls at least once after a jump of 2 and heals immediately after 3. After 4 or 5 it heals by the second opportunity: immediately if its new parent is black, otherwise one tick later. After 6 or 7, a white new parent forces at least two stalled updates; a black new parent instead gives an immediate heal. Here a heal may eliminate the difference entirely. Jumps of 1 and of 8 carry no such constraint at these ticks: the enumeration behind the module shows both values occur for them. It does not reach jumps above 8.

## 4. The proofs

Each law is a Boolean identity in the values of the two arrays on a window of wheels at tick `t`. Unfolding the recurrence once or twice expresses every wheel at ticks `t + 1` and `t + 2` in those values; the edge hypothesis replaces the values of `b` below the edge by those of `a` and the value at the edge by its complement; and the identity is decided by Lean's `decide` over the remaining free Boolean variables, at most thirteen of them for `jump_seven`. The module has no literals and no computation beyond these decisions, and it builds in about a second; the kit's `Check` replays its constants with the standard axioms `propext` and `Quot.sound`.

## 5. What these laws are for

The error edge is the damage front of rule 30 seen from a single configuration: the lowest wheel on which a configuration differs from a reference, for instance from the periodic strip that every configuration with a leftmost black cell eventually carries on its first wheels (R30-20261104-309041, 458f3b, 9aa447). The heal criterion underlies exact accounting of heals. The six laws constrain the first stall: after a jump of 2 a stall is forced; after 3 it is excluded; after 4 or 5 the new edge heals by its second opportunity; after 6 or 7 it stalls at least twice if its new parent is white. The jump alone does not determine every stall. In measurements on the seed's strip and on random rows (our record) these laws hold on every one of about 300,000 heals, and the stall hazard after the first tick is close to one half.

The cell below runs the laws on two actual configurations: the single black cell, and the same row with a second black cell 500 places to its right. In the tested offset-3 example, the edge becomes pinned at wheel 8 above a permanently white wheel; `edge_stall` then keeps it there. Offset 500 supplies varied jumps for this demonstration. Over 3,000 ticks the cell prints the final edge, the number of heals, the heals by jump, whether `heal_iff` held on the tested transitions `t = 0,…,2998`, and the number of heals that break a jump law.

## 6. Prior art and scope

The barrier and the heal criterion use the aligned-parent mechanism of `Rule30UniversalLeftSide` (`child_same`, `child_white`). Those theorems already allow abstract arrays and prove persistent transport under persistent parent alignment; their use against a strip is an application. Here agreement below the current error edge supplies the alignment, and `heal_iff` records the instantaneous equivalence. The black half of `heal_iff` is also the recruiting step of our `Rule30HealingBound` (R30-20261103-e660e4), in whole-line coordinates: a black newest known cell masks its unknown neighbour. The masking itself is classical (`Rule30MaskedJen.left_of_black`). The complementary white-parent memory rule is already used inside `child_white`. More directly, `Rule30LightCone.rule_flip_right_iff` (kit PR 98) proves that flipping the right input changes the output exactly when the center input is white; at an error edge of index at least 2 this is precisely the Boolean criterion used by `heal_iff`, in diagonal coordinates. The edge statement packages this known criterion and also handles wheel 1’s boundary rule. The left damage front of rule 30 and its speed are in Wolfram's *Random sequence generation by cellular automata* (1986) and *A New Kind of Science* (p. 949), and the heal identity in diagonal coordinates is in our record (§8.66, 6 October 2026). The six laws after a heal were found by exhaustive enumeration of the window (`jump_facts.py` in our record). We searched the kit at main `5fb59158`, the portal and the open kit PRs on 5 November 2026 for error edges, difference patterns, damage, two-array statements, heals, stalls and jumps, and found no matching statements of these six post-heal laws. This is the scope of the prior-art check, not an exhaustive novelty claim. Nothing here concerns the center column or the Prize problems.

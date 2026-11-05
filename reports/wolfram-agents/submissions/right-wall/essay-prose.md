# Locks at the wall of rule 30's rain-tailed rows: letters forced for ever, whatever lies below

Gareth Herbert; Claude (Anthropic); GPT (OpenAI). 5 November 2026.

## 1. The setting and the claim

Read a row of rule 30 from its rightmost black cell. Bit `k` of its edge code is the cell `k` places behind that cell, and one tick of rule 30 is the kit's edge map `T`:

`T c 0 = c 0`, `T c 1 = c 1 ⊕ c 0`, `T c (k + 2) = c (k + 2) ⊕ (c (k + 1) ∨ c k)`.

This is `Rule30FrozenRuler.edge_evol`, which needs only white to the right of the edge cell, so the row need not be finite. Below, a *row* is such a code. Every row has exactly one predecessor (`predecessor_unique`), so time can be run backward, and `previousN` does so. A statement about all `z` with `iter z n = x` is a statement about one row, the `n`-th predecessor of `x`. It holds whatever the lower cells of `x` are.

A row has a *rain tail* if its cells alternate from some index on. `T` keeps a rain tail and so does the predecessor (`step_rain_tail`, `back_rain_tail`). The rain pair `1010…`, `11010…` of `Rule30EdgeStaircases` is all tail. Any other row with a rain tail has a *wall*, the last equal pair below the tail (`Top`). This entry is about what stands at the wall. Words are written from low cell to high cell, with `#` black and `.` white.

**Letters.** Suppose the wall rises three cells on each of three backward ticks, at depth at least 5. Then the eleven cells ending at the wall read `A = ..####...##` or `B = .#.###...##` (`deep_words`). `BB` never occurs on successive ticks (`no_BB`), nor does `AAA` (`no_AAA`), and `ABA` occurs on an anchored row (`witness_ABA`).

**Locks.** Three sets of windows, each closed under the backward tick for every pair of lower cells:

| Lock | Cells | Windows | Phases | Letters, in backward time | Reset word |
|---|---|---|---|---|---|
| `LockAB` | 45 | 4 | 2 | `A`, `B` | at the foot of every window (`floor`) |
| `LockAAB` | 136 | 6 | 3 | `A`, `A`, `B` | at the foot of every window (`floor`) |
| `LockThird` | 175 | 40 | 6 | `B`, `A`, `A`, `B`, `A`, `A` | at no depth below the wall's own (`no_floor`) |

If a row shows a window of a lock at its wall, with rain above, then every predecessor does too, three cells higher each tick, and the letters follow the phases for ever, whatever lies below the window (`LockAB.letters`, `LockAAB.letters`, `LockThird.letters`). Each lock has a witness on an anchored row (`witness`).

**The cloud.** A set of 798 windows of 45 cells is closed too (`Cloud.closed`). None of them is a window of `LockAB` (`cloud_not_lock`), so a row in the cloud never reaches that lock (`avoids_lock`). Along any backward history in the cloud the letters cannot change on 17 ticks running (`no_long_alternation`).

**Entry.** One explicit anchored row passes from the cloud into the third lock (`Entry.entry`).

**Not periodic.** A row in any of these four sets is not periodic under `T` (`not_periodic`, from the general `held_not_periodic`).

Nothing here concerns the center column or the Prize problems.

## 2. The wall and its letters

The wall moves by an exact local rule under `T`. Say the wall is at `D`. If cell `D` is white it moves up two cells (`top_up`). If `D` is black and a cell of `D − 1`, `D − 2` is black, it stays (`top_stay`). If `D` is black and both are white, it falls by one, two or three cells, according to cells `D − 3` and `D − 4` (`top_minus_one`, `top_minus_two`, `top_minus_three`). So a backward advance of three is the last case read in reverse, and it fixes the six cells at the wall to `#...##` (`marker`).

Three such advances put that marker on three successive rows, and a finite check of the ten cells below the first marker leaves the two letters (`deep_words`). Eighteen windows of eleven cells are closed under the backward tick (`front_back`), and a row showing one is not periodic (`front_not_periodic`). So the open part of the question "is the rain pair the only periodic row with a rain tail?" is whether every other such row reaches those windows. We do not settle that here.

Once a row shows a letter, the two letters are themselves closed (`letters_closed`). The next letter has a simple rule. After `B` comes `A` for every pair of lower cells (`letter_after_B`). After `A` comes `A` exactly when the two cells of the predecessor just below the old window are white (`letter_after_A`). After `AA` comes `B`, by `no_AAA`. So every settled word is a string of blocks `BA` and `BAA`, and the only choice is the letter after `BA`.

## 3. The word that stops what comes from below

A backward tick is a sweep upward. Each new cell reads the old cell at its place and the two new cells below it. So the image of a window depends on what lies below only through two cells.

Take ten cells `F(b, u, v) = 0, b, ¬b, 1, u, 1, 0, v, 0, 1`.

- `Reset.reset`: under any two lower cells, the new cells on places 3 to 9 of the word are `0, b′, ¬b′, 1, ¬v, 1, 0`. Only the bit `b′` feels the lower cells, and only through whether both are white.
- `Reset.above`: the output above the word is one fixed function of the input above it, whatever `b`, `u`, `v` and the cells below.
- `Reset.again`: if the row reads `s, ¬s, s` just above the word, the predecessor has the same shape of word three cells higher, with `v` replaced by `¬s` and `u` by `¬v`.
- `Reset.letters`: `A` and `B` are `F(0, 1, 0)` and `F(1, 1, 0)` with one black cell above.

Rain supplies `s, ¬s, s` on every tick, which is why the wall rises by exactly three.

`Reset.above` is not new in kind. Each word `F(b, u, v)` contains a word `0 1^(3m + 1) 0` of Lowry's `Rule30ResetFreeCore` with a further cell above it, and such words reset the inverse sweep (`Rule30InverseCascade`, kit PR 60). What the theorems here add is the shape that comes back three cells higher.

## 4. Closed sets

Let `S` be a list of words of `W` cells. `S` is *closed* (`Closed`) if for every window in it and each of the four pairs of lower cells, the image window is in `S` and rain resumes above it. `Held W S x L` says that cells `L` to `L + W − 1` of `x` are a window of `S` and that the cells above alternate. Then:

- `held_back`: every predecessor is held three cells higher, whatever lies below the window.
- `held_forever`: every row `n` ticks back is held `3 n` cells higher.
- `held_not_periodic`: if every window ends in the wall's equal pair, a held row is not periodic. A period would put the same wall `3 P` cells higher on the same row, inside its rain.

The check on `S` is finite, and the theorem is general. A closed set of windows that ignores the cells on one side is the method of the kit's `Rule30GateTrap`, here on the wall of an edge code and in backward time.

## 5. Three locks

These are the four windows of `LockAB`. The last eleven cells are the letter.

```
..##.#...#.#..#..#........##....##..####...##    A
.#.#.#...#.#..#..#........##....##..####...##    A
..####.#.##.##.########......#.##..#.###...##    B
.#.###.#.##.##.########......#.##..#.###...##    B
```

The two windows of a phase differ only in cells 1 and 2, the bit `b` of the reset word at the foot of the window. That bit is all the lower cells can move. So a window of `LockAB` holds a second reset word, 34 cells below the wall's own, and the strip between the two cannot feel anything from below. The same holds for `LockAAB`, with the two words 125 cells apart.

`LockThird` shows that a lock needs no such word. No reset word stands at one depth in all forty windows, apart from the wall's own (`no_floor`), and the number of windows in a phase runs 5, 6, 7, 8, 7, 7. Lower states still merge before they reach the letters, but at places that move with the phase. So `AAB` repeated has two different locks.

A separate computation finds that these widths are the smallest. At 135 and 174 cells, a path of free lower cells leaves the letters (COMPUTED).

## 6. The cloud, and a row that enters a lock

Most rows do not lock at once. Of 100,000 rows with 40 random cells, 99,176 entered the 798 windows and 824 entered `LockAB`, all by tick 128 (MEASURED). The cloud explains why late rows never reached `LockAB`: `Cloud.closed` holds them, and `cloud_not_lock` keeps them apart. Its rank function, the longest alternating run from each window, gives `no_long_alternation`.

The cloud is coarse, though. The theorem `Entry.entry` is about one explicit row whose rain starts at cell 569. Its images under `T`, at ticks `k`, read letters for every `k ≤ 110` (`Entry.letters`). The image at tick 97 is held in the cloud, so the images at every tick below 97 are too. The image at tick 7 is outside the third lock, and the image at tick 6 is inside it, so the images at ticks 0 to 6 are as well. Read backward from tick 110, the letters run in a mix of `BA` and `BAA` down to tick 57, then `BAA` repeated, and the row is caught at tick 6.

So a row in the cloud can step into a lock: a window of 45 cells cannot see the third lock.

## 7. A computation

The first cell below checks `LockAB` outside Lean, with plain lists and the inverse rule cell by cell, then reads the letters of the entry row, tick 0 first, by forward ticks on one integer. The second cell draws the top 120 cells of that row in the frame of its wall, with tick 110 at the top, tick 0 at the bottom and the wall on the left.

## 8. How the kernel checks it

A window of `W` cells is a number. `load` puts the two lower cells under it and six cells of rain over it, `sw` is one cell of the sweep, and `run` is the whole sweep, on one number with one index. `run_back` proves this is `back` on words, `next_fast` that the image window is `nxt`, and `closed_fast` that a list of numbers passing `Fast` is `Closed`. The test inside `run` never changes the value, since `0` stays `0` (`run_succ`), but it forces each cell as the kernel reaches it. For the forward direction `fw` is one exclusive or and two shifts, and `iter_fw` proves it is `T` on all bits.

The record's first versions of these proofs used lists and took 57 s for the cloud alone. With numbers the three kit modules build in about 2, 2 and 10 s, at 2.7 GB at most, and the one-module portal form builds in 13 s at 3.0 GB. All the times here were measured on an M5 MacBook Pro.

We also ran two controls outside the Lean proof. Ten small mutations (a window of each lock, a rank, the rank bound, a window of the cloud, a bit of the row, a letter, the rule, the rain) were all rejected. A separate Python replay from the literals in the source, on plain lists, confirms all 3,392 image checks, the letters, the ranks, the reset depths and the entry row.

## 9. What is computed or open

These are not theorems of this entry.

- **COMPUTED.** Let `E(w)` be the windows of `w` cells that can follow arbitrarily many settled ticks with free lower cells. At every width from 45 to 92 the graph on `E(w)` has exactly two closed classes, the class of `LockAB` and a cloud, of 798 windows at width 45 and 920,783 at width 92.
- **COMPUTED.** A reset word below the wall leaves one free binary word in time. Among primitive words of period up to 13, exactly two reach rain going up, `10` and `110`, the words of `LockAB` and `LockAAB`. Through period 24 this holds within 20,000 columns.
- **MEASURED, on a surrogate.** In a chain on the top 256 cells with independent fair lower cells, no capture by the third lock was detected in about 1.2 · 10^11 ticks. Fair lower cells are an assumption, not a fact about real rows, and no rate is claimed.
- **Open.** Whether every row with a rain tail reaches the letters, whether every settled row ends in a lock, and whether there are other locks. A search by period found these three and no others, with caps, so this is a list of what was found.

## 10. Credits and prior art

The edge map is `Rule30FrozenRuler` (Coven, Pivato and Yassawi, Proc. AMS 135, 2007), and the rain pair is `Rule30EdgeStaircases` (R30-20261027-196370). Reset words `0 1^(3m + 1) 0` and their role in the inverse sweep are Troy Lowry's (`Rule30ResetFreeCore`, `Rule30ResetFreeThree`, kit PR 60). The closed-window method is in `Rule30GateTrap`. `Rule30UniversalStart` (R30-20261029-3ca86f) reads the first equal pair behind the edge on the right diagonals. The wall here is the last one. The word "lock" here is not the `Lock` of the kit's period-4 table, and "wall" is not the kit's zero wall.

We searched the kit at main `72253aea`, all portal entries and open kit PRs on 5 November 2026 for rain tails, walls of edge codes, closed windows under the backward tick and reset words, and found no earlier statement of these theorems.

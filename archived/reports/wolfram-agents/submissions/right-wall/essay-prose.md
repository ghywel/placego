# Locks at the wall of rule 30's rain-tailed rows: letters forced for ever, whatever lies below

Gareth Herbert; Claude (Anthropic); GPT (OpenAI). 5 November 2026.

## 1. The setting and the claim

Read a row of rule 30 from its rightmost black cell. Bit `k` of its edge code is the cell `k` places behind that cell, and one tick of rule 30 is the kit's edge map `T`:

`T c 0 = c 0`, `T c 1 = c 1 ⊕ c 0`, `T c (k + 2) = c (k + 2) ⊕ (c (k + 1) ∨ c k)`.

This is `Rule30FrozenRuler.edge_evol`, which needs only white to the right of the edge cell, so the row need not be finite. Below, a *row* is such a code, with bit 0 black; the Lean definitions also allow unanchored Boolean sequences. Every row has exactly one predecessor (`predecessor_unique`), so time can be run backward, and `previousN` does so. A statement about all `z` with `iter z n = x` is a statement about one row, the `n`-th predecessor of `x`. It holds whatever the lower cells of `x` are.

A row has a *rain tail* if its cells alternate from some index on. `T` keeps a rain tail and so does the predecessor (`step_rain_tail`, `back_rain_tail`). The rain pair of `Rule30EdgeStaircases` is `1010…`, which has no equal pair, and `11010…`, whose last equal pair starts at index 0. Any other anchored row with a rain tail has a *wall*, the last equal pair below the tail (`Top`). This entry is about what stands at the wall. Words are written from low cell to high cell, with `#` black and `.` white. In all window-transport, letter and nonperiodicity statements below, the window starts at an index `L ≥ 2`, leaving the two lower cells used by the sweep.

**Letters.** Suppose the wall rises three cells on each of three backward ticks, with the shallowest of the four walls at depth at least 5. Then the eleven cells ending at the wall read `A = ..####...##` or `B = .#.###...##` (`deep_words`). `BB` never occurs on successive ticks (`no_BB`), nor does `AAA` (`no_AAA`), and `ABA` occurs on an anchored row (`witness_ABA`).

**Locks.** Three sets of windows, each closed under the backward tick for every pair of lower cells:

| Lock | Cells | Windows | Phases | Letters, in backward time | Reset word |
|---|---|---|---|---|---|
| `LockAB` | 45 | 4 | 2 | `A`, `B` | at the foot of every window (`floor`) |
| `LockAAB` | 136 | 6 | 3 | `A`, `A`, `B` | at the foot of every window (`floor`) |
| `LockThird` | 175 | 40 | 6 | `B`, `A`, `A`, `B`, `A`, `A` | no common offset below the top letter has shape `F(b,u,v)` in all forty windows (`no_floor`) |

If a row shows a window of a lock at its wall, with rain above, then every predecessor does too, three cells higher each tick, and the letters follow the phases for ever, whatever lies below the window (`LockAB.letters`, `LockAAB.letters`, `LockThird.letters`). Each lock has a witness on an anchored row (`witness`).

**The cloud.** A set of 798 windows of 45 cells is closed too (`Cloud.closed`). None of them is a window of `LockAB` (`cloud_not_lock`), so a row in the cloud never reaches that lock (`avoids_lock`). Along any backward history in the cloud the letters cannot change on 17 ticks running (`no_long_alternation`).

**Entry.** One explicit anchored row passes from the cloud into the third lock (`Entry.entry`).

**Not periodic.** A row in any of these four sets is not periodic under `T` (`not_periodic`, from the general `held_not_periodic`).

Nothing here concerns the center column or the Prize problems.

## 2. The wall and its letters

The wall moves by an exact local rule under `T`. Say the wall is at `D ≥ 5`; shallower walls have boundary exceptions. If cell `D` is white it moves up two cells (`top_up`). If `D` is black and a cell of `D − 1`, `D − 2` is black, it stays (`top_stay`). If `D` is black and both are white, it falls by one, two or three cells, according to cells `D − 3` and `D − 4` (`top_minus_one`, `top_minus_two`, `top_minus_three`). So a backward advance of three is the last case read in reverse, and it fixes the six cells at the wall to `#...##` (`marker`).

Three such advances put that marker on three successive rows, and a finite check of the ten cells below the first marker leaves the two letters (`deep_words`). Eighteen windows of eleven cells are closed under the backward tick (`front_back`), and a row showing one is not periodic (`front_not_periodic`). A periodic orbit cannot meet those windows. Thus a sufficient route to proving that the rain pair is the only periodic anchored row with a rain tail would be to show that every other such row reaches the windows. That capture statement is open; no converse is claimed.

Once a row shows a letter, the two letters are themselves closed (`letters_closed`). The next letter has a simple rule. After `B` comes `A` for every pair of lower cells (`letter_after_B`). After `A` comes `A` exactly when the two cells of the predecessor just below the old window are white (`letter_after_A`). After `AA` comes `B`, by `no_AAA`. Thus an infinite settled history, after at most an initial `A` or `AA`, is a concatenation of `BA` and `BAA`; finite observed words may end partway through a block. The choice is the letter after `BA`.

## 3. The word that stops what comes from below

A backward tick is a sweep upward. Each new cell reads the old cell at its place and the two new cells below it. So the image of a window depends on what lies below only through two cells.

Take ten cells `F(b, u, v) = 0, b, ¬b, 1, u, 1, 0, v, 0, 1`.

- `Reset.reset`: under any two lower cells, the new cells on places 3 to 9 of the word are `0, b′, ¬b′, 1, ¬v, 1, 0`. Only the bit `b′` feels the lower cells, and only through whether both are white.
- `Reset.above`: the output above the word is one fixed function of the input above it, whatever `b`, `u`, `v` and the cells below.
- `Reset.again`: if the row reads `s, ¬s, s` just above the word, the predecessor has the same shape of word three cells higher, with `v` replaced by `¬s` and `u` by `¬v`.
- `Reset.letters`: `A` and `B` are `F(0, 1, 0)` and `F(1, 1, 0)` with one black cell above.

Rain supplies `s, ¬s, s` on every tick, which is why the wall rises by exactly three.

`Reset.above` uses a known reset mechanism. Each word `F(b, u, v)` contains `0 1^(3m + 1) 0` with a further cell above it. Troy Lowry's `Rule30InverseCascade.run_resets` in [kit PR 60](https://github.com/WolframInstitute/Rule30PrizeKit/pull/60) proves the corresponding inverse-sweep synchronization; `Rule30ResetFreeRuns.AvoidReset` records the forbidden-run family, and `Rule30ResetFreeCore` supplies the encoded graph framework. Here `Reset.again` identifies the particular ten-cell shape that returns three cells higher. The reviewed prior sources do not state that identity.

## 4. Closed sets

Let `S` be a list of words of `W` cells. `S` is *closed* (`Closed`) if for every window in it and each of the four pairs of lower cells, the image window is in `S` and rain resumes above it. `Held W S x L` says that cells `L` to `L + W − 1` of `x` are a window of `S` and that the cells above alternate. Assume `L ≥ 2` (and, for nonperiodicity, `W ≥ 2`). Then:

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

`LockThird` has no common location for the shape `F(b,u,v)` below its top letter: for each offset `0 ≤ d < 164`, at least one of the forty windows lacks that shape there (`no_floor`). This excludes neither other synchronizing words nor a floor outside the displayed window. The numbers of windows in its six phases are 5, 6, 7, 8, 7, 7. A separate computation finds that the four lower sweep states merge below the letters, at positions depending on the window and phase (COMPUTED). Thus `AAB` repeated has two different locks.

A separate computation finds that these widths are the smallest. At 135 and 174 cells, a path of free lower cells leaves the letters (COMPUTED).

## 6. The cloud, and a row that enters a lock

Most rows do not lock at once. Of 100,000 rows with 40 random cells, 99,176 entered the 798 windows and 824 entered `LockAB`, all by tick 128 (MEASURED). The cloud explains why late rows never reached `LockAB`: `Cloud.closed` holds them, and `cloud_not_lock` keeps them apart. A rank between 1 and 17 decreases whenever the letter changes, giving `no_long_alternation`: seventeen successive letter changes are impossible.

The cloud is coarse, though. The theorem `Entry.entry` is about one explicit row whose rain starts at cell 569. Its images under `T`, at ticks `k`, read letters for every `k ≤ 110` (`Entry.letters`). The image at tick 97 is held in the cloud, so the images at every tick below 97 are too. The image at tick 7 is outside the third lock, and the image at tick 6 is inside it, so the images at ticks 0 to 6 are as well. Read backward from tick 110, the letters run in a mix of `BA` and `BAA` down to tick 57, then `BAA` repeated, and the row is caught at tick 6.

Thus a backward orbit can enter the third lock while remaining in the cloud. Membership in the 45-cell cloud does not distinguish whether capture by the third lock has occurred. The two windows end at the same wall: their starting indices differ by `175 − 45 = 130`.

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
- **Open.** Whether every anchored row with a rain tail outside the rain pair reaches the letters, whether every settled row ends in a lock, and whether there are other locks. A search by period found these three and no others, with caps, so this is a list of what was found.

## 10. Credits and prior art

The edge-map formalization is the kit's `Rule30FrozenRuler`; Coven, Pivato and Yassawi, Proc. AMS 135 (2007), give the general permutive-automaton and odometer framework. The rain pair is in `Rule30EdgeStaircases` (R30-20261027-196370). Troy Lowry's `Rule30ResetFreeRuns` and `Rule30InverseCascade.run_resets` (kit PR 60) supply the reset-run family and inverse-sweep synchronization. The closed-window method is in `Rule30GateTrap`, contributed by Renaud Bosdure with Claude, Gemini and Grok. `Rule30UniversalStart` (R30-20261029-3ca86f) reads the first equal pair behind the edge on the right diagonals. The wall here is the last one. The word "lock" here is not the `Lock` of the kit's period-4 table, and "wall" is not the kit's zero wall.

The 5 November 2026 search was refreshed at kit `c63cde84`, with the portal and open PR sources, and included the relevant PR 60 discussion and linked proof archive. We found no earlier statement of these particular invariant window families and their letter laws. The reset mechanism and closed-window method are prior art, as credited above.

# From Tick 46 On, Every Row of Rule 30 Beside a Wall Has a Twin

Gareth Herbert; Claude (Anthropic); GPT (OpenAI). 8 November 2026.

## 1. The statement

Read a natural number `Y` as a row of rule 30 beside a white wall: bit `k` of `Y` is the cell at depth `k + 1`, and the wall is always white. One tick is `F(Y) = (Y >>> 1) XOR (Y OR (Y <<< 1))`, two ticks are `G = F∘F`, and `iter F t` is `t` ticks. These are the kit's `Rule30ZeroBoundary` definitions. In this frame `Q01` says that every natural reaches an even value under `G`, that is, a white cell beside the wall at some even tick (`Q01_iff_integer`).

**Theorem (`late_twin`).** For every nonzero natural `y` and every `t ≥ 46`, the row `x = iter F (t - 2) y` has a twin: a natural `x′ ≠ x` of the same width, with the same cell beside the wall, and with `F (F x′) = F (F x)`.

**Theorem (`late_twin_immortal`, `late_twin_off_orbit`).** If moreover `y` never reaches an even value under `G` and `t` is even, then `x′` never reaches an even value either, and `x′` is none of the rows `iter G j y`.

So an immortal natural, if one existed, would force another immortal natural of the same width at every even tick from `46` on, off its own orbit. The twin and `x` agree two ticks later, so they have one future: the twins add rows, not futures.

## 2. The top of a row moves on its own

Rule 30 reads a cell's left neighbour, so the cells above a cut never see the cells below it. In this frame that is one identity (`F_shiftRight`): for every row `Y` and every cut `m`,

`F Y >>> (m + 1) = R (Y >>> m)`, where `R u = (u >>> 2) XOR ((u >>> 1) OR u)`.

The cut moves out by one cell each tick, as the top of the row does. Iterating, `iter F t Y >>> (m + t) = R^t (Y >>> m)` (`iter_F_shiftRight`). Taking the cut twenty cells below the top, the top twenty cells of every row evolve by `R`, whatever lies beneath them and wherever the wall is.

## 3. The top twenty cells settle within 26 ticks

From any start whose top cell is the twentieth, `R^t` reaches one four-cycle `C20 = {820683, 822904, 911005, 912610}` by `t = 26` and stays there (`band_settles`). Every nonzero row reaches width `20` by tick `19`, so from tick `45` on every row's top twenty cells lie on `C20` (`band_late`).

The kernel checks this in two stages rather than all `2^19` starts at once. Because `R` commutes with shifting, the top thirteen cells evolve on their own too. All `4,096` starts of the top thirteen cells reach the four-cycle `C13 = {6411, 6428, 7117, 7129}` within `14` ticks (`stage13`). From `C13` with any seven cells below it, `512` states, the top twenty reach `C20` within `12` more (`stage20`). That gives `26`. The bound is sharp: among all `2^19` starts, `40,960` need all `26` ticks.

## 4. Reset words and the twin

A preimage of a row under `F` is fixed by the row and its cell beside the wall. The kit's backward transducer `back b y` builds it upward one depth at a time (`eq_back`, `zrow_back`). Two runs that read the same inputs forget their starting states once the input contains the word `0 1 0` or `0 1111 0` followed by one more cell (`reset0`, `reset1`, `sync`): from the depth of that extra cell on, the runs agree.

Every phase of `C20` carries such words, and in two consecutive rows they are stacked in the right order. With the band's bits counted upward from the cut, the four phases give:

| Band of `F x` | Band of `F (F x)` | Word in `F (F x)` | Word in `F x` |
|---|---|---|---|
| 820683 | 911005 | `0 1 0` at bit 6 | `0 1 0` at bit 14 |
| 822904 | 912610 | `0 1 0` at bit 0 | `0 1 0` at bit 14 |
| 911005 | 822904 | `0 1111 0` at bit 2 | `0 1111 0` at bit 12 |
| 912610 | 820683 | `0 1 0` at bit 2 | `0 1111 0` at bit 12 |

Now invert `F (F x)` twice, flipping the cell beside the wall at the middle step and keeping it at the first. The flipped run differs from `F x` only below the word in `F (F x)`. The next run reads the word in `F x`, which lies above that, and forgets the difference. So the result agrees with `x` above the second word, and it is a finite row: the twin (`twin_of_factors`). It differs from `x`, because its image one tick on has the other cell beside the wall. Its width is that of `x`, because both reach the same row two ticks later.

At an even tick the twin keeps the cell beside the wall that `x` has, and from two ticks on it is `x`'s future, so immortality passes to it. It is off the orbit because the orbit has exactly one row of each width, and that row is `x`.

## 5. Worked numbers

The cell below recomputes both stage maxima, then takes seven rows, among them the long survivors `1493` and `11083`. For each it checks that the band of `iter F 45 y` is on `C20`, and that `iter F 44 y` has a twin of equal width, the same cell beside the wall and the same image two ticks on, found by inverting `F` twice.

## 6. Prior art and scope

The reset words come from Feynman's theorem on predecessors: on a cyclic register, a configuration has exactly one predecessor under rule 30 if and only if some run of `1`s between consecutive `0`s has length `1` mod `3` (the kit's `Rule30Predecessors`, `predCount_eq_one_iff`, proved through the transfer map `T`). The words `0 1 0` and `0 1111 0` are such runs, read by the same map. Stacking such words across many rows gives the inverse-cascade staircase of Troy Lowry's kit pull request #60 (`scheduled_cascade_closes`), which assumes recurrent resets. What is new here is that every late row supplies them, from an explicit tick, in its own top. The kit's `Rule30PrefixMerger` gives a fixed seven-cell rewrite beside the wall that merges after two ticks for every tail, a twin for rows with that prefix. The settling of the top is a small explicit case of the left side's settling (`Rule30UniversalLeftSide`, `Rule30FourLeftSides`). The statement was found in the project's swarm and carried by hand in the [project's record](https://github.com/ghywel/placego/blob/main/PROOFS.md); this module is its formal proof.

Not formalized here: the larger family the same mechanism gives. On the four left strips through `87,866` wheels, reset chains reach `7,911` levels, so past an onset that was not computed every late row has `2^3955` guarded preimages at depth `7,910`. Nor is the general reset schedule.

The twins have the same future as `x`. They raise the number of immortal rows, not the number of immortal futures, and they bound no death time. Nothing here proves `Q01`, and Problems 1 to 3 stay open.

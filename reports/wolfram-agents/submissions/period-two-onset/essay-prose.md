# The Column-1 Words of Period Two from Two Ticks On: The Kit's Width-5 and Width-6 Constraints with an Explicit Onset, for Every History

Gareth Herbert; Claude (Anthropic); GPT (OpenAI). 10 November 2026.

## 1. The statement

Suppose the center column of rule 30 alternates white, black, white, … from a time `T`. The kit's `Rule30PeriodTwoWidth5.col1_constraints` and `Rule30PeriodTwoWidth6.col1_constraints` then show that from some later time `T'` on, column `1` read at consecutive white times never spells a word of their lists `col1Forbidden`:
- at width `5`: `11`, `00000`, `100101`, `10010001`;
- at width `6`: these and `101001`, `1010100001`, `1010001001`, `10010000101`, `1001000010001`.

They are stated for the single seed, and `T'` comes from a certificate of the strip's bad class, as an existence statement. This module makes `T' = T + 2` and drops the seed.

A *history* is any `H : Nat → Int → Bool`. `Obeys b H` says that it obeys rule 30 at the columns `1, …, b`, at every tick. Nothing is assumed about the other columns: column `0` may be anything, the columns beyond `b` may be anything, and the configuration need not be finite.

- `no_word5`, `no_word6`: if `Obeys b H` and column `0` alternates white, black on the `2 m` ticks `s, s + 1, …, s + 2 m - 1`, then column `1` at the ticks `s + 2, s + 4, …, s + 2 m` does not read a listed word of length `m`. At width `6` the same holds for `101010000`, the word `1010100001` without its last sample (`no_short6`).
- `onset5`, `onset6`: so if column `0` alternates from `T` on, no listed word is read from any white time `t ≥ T + 2`. For the single seed these are the kit's two statements with `T' = T + 2` (`col1_constraints5`, `col1_constraints6`).
- `free_bit5`, `free_bit6`: if the rule also holds at column `0`, then column `-1` at a white time followed by a black one is the complement of column `1`. So column `-1` never reads a complemented listed word, once the alternation lasts two ticks longer. `free_bit_constraints5` and `free_bit_constraints6` are the kit's free-bit statements with `T' = T + 2`.

## 2. Two ticks

Let `s` be a white tick of column `0`, with `s + 1` black. One tick moves the window of the columns `1, …, b` by rule 30, with column `0` on its left and column `b + 1` on its right (`seg_step`). Two ticks therefore move it by a fixed map. The left inputs are white, then black, and the only other inputs are the two cells of column `b + 1` at `s` and `s + 1` (`dstep`, `win_dstep`).

So the window at every white time after the first is one of the windows that a double step can produce from some window. That is the first image, `img b`, whatever the history did before.

## 3. A finite relation

The kernel computes the first images. One double step takes the `32` windows of width `5` onto `20` (`img5_length`) and the `64` windows of width `6` onto `38` (`img6_length`). The double step takes each of these sets back into itself, for every value of column `b + 1` (`img5_closed`, `img6_closed`). The stabilized image at width `6` has `36` windows, but the first image is already closed, so no later entry time is needed.

For a word `c₀ c₁ … c_{m-1}`, the first layer is the set of windows of `img b` whose column-`1` cell is `c₀`. Each later layer is the set of double-step images of the previous one whose column-`1` cell is the next sample (`run`). The kernel checks that the last layer is empty for every listed word (`excludes5`, `excludes6`, `excludes_short6`). Reading the word from `s + 2` uses the double steps from `s, s + 2, …, s + 2 m - 2`, which need column `0` at the ticks `s` to `s + 2 m - 1`. The tick of the last sample itself is not used (`mem_run`, `no_word`).

## 4. Scope

The relation forgets every column beyond `b + 1`. So `T + 2` is an onset that holds for every history, not the earliest onset for actual configurations. The finite certificate is a relaxation, and the words it excludes are the words this method can exclude. They do not exclude an eventual period `2`, and nothing here bears on `Q01` or the single seed's center column beyond the kit's own statements.

## 5. Worked numbers

The cell below computes, independently of the Lean module and with Wolfram Language's own rule 30 (`CellularAutomaton[30, …]`):
- the sizes of the first images at widths `5` and `6`, and whether each is closed under the double step;
- whether every listed word, and `101010000` at width `6`, is excluded;
- the minimal excluded words of length at most `13`: words whose two one-sample shortenings are both readable;
- the listed words that are excluded already from all windows, with no first double step.

Up to length `13`, the minimal excluded words are exactly the kit's lists, except that `1010100001` is replaced by its prefix `101010000` (COMPUTED). Only `11` and `00000`, and `101001` at width `6`, need no first double step (COMPUTED).

## 6. Prior art and scope

- **The words** are the kit's, from `Rule30PeriodTwoWidth5` and `Rule30PeriodTwoWidth6`, which prove them for the single seed from an existential onset. The portal entry R30-20261028-e34744 restates the width-`6` words for finite configurations with a leftmost black cell, again from an existential onset.
- **The method** is the kit's: windows driven by the alternating column and closed under the double step for every value of the next column, with layers of windows for each word (`Rule30GateTrap`, `Rule30GateTrapWords`). Our earlier submission R30-20261108-c1d531 has the same double step for windows (`winW_dstep`). In `Rule30GateTrapWords` the conclusions hold after the window enters the trap; here the first set is the image of all windows, so entry is automatic.
- **Sharper languages.** `Rule30PeriodTwoWidth13` (R30-20261109-62afca) forces the left trace into a nine-pair gap language, which the kit describes as sharper than the width-`5` and width-`6` words. It is stated for the single seed, from an existential onset.
- **What is new:** the explicit onset `T + 2`, for every history that obeys rule 30 at the columns `1, …, b`; the shortened word `101010000`; and the observation that the first images, with `20` and `38` windows, are already closed.
- **History.** Cloud carried the transfer from the swarm's run. GPT replayed the finite relation independently and sharpened the onset to two ticks at both widths. Local formalized it.

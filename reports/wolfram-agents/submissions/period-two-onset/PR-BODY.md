Rule30PeriodTwoOnset: the period-two column-1 words from two ticks on, for every history (PORTAL-ID)

This adds `lean/Ruliology/CellularAutomata/Rule30PeriodTwoOnset.lean`, with its `public import` line in `lean/Ruliology.lean` after `Rule30SEPToPeriodTwo` and a row in *Added in the kit*. It imports only `Rule30Prize` and `Rule30Jen`.

**What it proves.** A history is any `H : Nat → Int → Bool`; `Obeys b H` says it obeys rule 30 at the columns `1..b`, with nothing assumed beyond them.
- `no_word5`, `no_word6`: if column `0` alternates white, black on the `2 m` ticks `s, …, s + 2 m - 1`, then column `1` at the ticks `s + 2, …, s + 2 m` does not read a word of length `m` of the kit's `Rule30PeriodTwoWidth5.col1Forbidden` (resp. `Rule30PeriodTwoWidth6.col1Forbidden`). `no_short6`: nor, at width `6`, `101010000`, the listed `1010100001` without its last sample.
- `onset5`, `onset6`: so with an alternation from `T`, the words are excluded from every white time `t ≥ T + 2`. `col1_constraints5`, `col1_constraints6`, `free_bit_constraints5`, `free_bit_constraints6` are the kit's single-seed statements with `T' = T + 2` in place of `∃ T'`.
- `free_bit5`, `free_bit6`: column `-1`, complemented, with the rule at column `0` and two more ticks.

**Method.** Two ticks from a white time move the window of the columns `1..b` by a double step whose only other inputs are two cells of column `b + 1` (`win_dstep`). One double step takes the `32` windows of width `5` onto `20` and the `64` of width `6` onto `38`. Both sets are closed under the double step (`img5_length`, `img6_length`, `img5_closed`, `img6_closed`). The kernel checks layers of windows for each word, as in `Rule30GateTrapWords`, starting from these images, so no entry time is needed.

**Checks**, with Lean 4.35.0, at main `03a19bf`:
- `lake build Ruliology.CellularAutomata.Rule30PeriodTwoOnset`: no warnings, about 4 s.
- The kit's own `Check.lean --claim partial` passes all 16 headlines, with 136 constants and no new axioms.
- The portal form passes `Check` at the verifier's kit `5fb59158`.
- The compiler rejected all eight mutations tested:
  - the width-5 image with 19 windows;
  - the width-6 first image with 36 windows, the size it stabilizes at;
  - the shortened word at width 5;
  - a shortening that is not excluded;
  - the clock reversed;
  - the clock one tick short;
  - the free bits one tick short;
  - the rule at one column fewer.
- The worked numbers agree in Python and Wolfram Language. Up to length `13`, the minimal words this relaxation excludes are the kit's lists, with `1010100001` replaced by `101010000`.
- Not run: the full catalog build (`bash build_all.sh`).

**Prior art.** The words are the kit's (`Rule30PeriodTwoWidth5`, `Rule30PeriodTwoWidth6`), proved there for the single seed from an existential onset. The method is `Rule30GateTrapWords`'s, and our earlier `winW_dstep` (R30-20261108-c1d531) has the same double step. `Rule30PeriodTwoWidth13` gives a sharper language for the single seed, from an existential onset.

**What it does not do.** The relation forgets the columns beyond `b + 1`, so `T + 2` is not claimed to be the earliest onset for actual configurations. Nothing here excludes period 2.

Portal entry: [PORTAL-ID](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/PORTAL-ID).

🤖 Generated with [Claude Code](https://claude.com/claude-code)

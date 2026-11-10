Rule30WallDeadlines: the exact wall deadlines of rules 90 and 150 (R30-20261110-c20b0a)

This adds `lean/Ruliology/CellularAutomata/Rule30WallDeadlines.lean`, with its `public import` line in `lean/Ruliology.lean` after `Rule30ExactReturn` and a row in *Added in the kit* after the same module. It imports only `Rule30ZeroBoundary`.

**What it proves.** It answers `Q01` exactly for rules 90 and 150 in the zero-boundary frame. Every rule of the form `left xor h (centre, right)` has the frame `zr h` beside a white wall, and `zr_or_eq_zrow` shows that rule 30's is the kit's `zrow`.
- `odd90`, `fib2_mod`: for rule 90, if depth `1` is black at every even tick up to `T`, every cell with depth plus tick odd (and at most `T + 1`) is Fibonacci modulo `2` of its depth, which is white exactly at the multiples of `3`.
- `kstar_spec`, `deadline90`, `sharp90`: so every start of width at most `W` turns depth `1` white at some even tick at most `kstar W - 1`, where `kstar W` is the least odd number above `W` not divisible by `3`. Every start whose odd depths follow Fibonacci stays black at every earlier even tick.
- `two_step150`, `odd150`: two steps of rule 150 act on the odd depths at even ticks by `x (k + 2) + x k + x (k - 2)`, with `x 3` at the wall, so every odd depth is forced black.
- `deadline150`, `sharp150`: the rule 150 deadline is `2 * ((W + 1) / 2)`, attained by every start with all odd depths black.

**Checks**, with Lean 4.35.0, at main `03a19bf`:
- `lake build Ruliology.CellularAutomata.Rule30WallDeadlines`: no warnings.
- The kit's own `Check.lean --claim partial` passes all 10 headlines, with 87 constants and no new axioms.
- The portal form passes `Check` at the verifier's kit `5fb59158`.
- The compiler rejected all six mutations tested, each a false statement: either deadline two ticks earlier, either sharpness one tick longer, Fibonacci white at the even numbers, and the wall case reading depth 2.
- The worked numbers agree in Python and Wolfram Language, by brute force for widths `1` to `12`: both deadlines match their closed forms, and the starts attaining them are exactly the pattern rows, `2 ^ (W / 2)` of them.
- Not run: the full catalog build (`bash build_all.sh`).

**Prior art.** The family and its shared properties with rule 30 are the kit's `Rule30Realization` (`center90`, `center150`, `barrier`). Portal R30-20261023-1bf4dc proves that no finite configuration keeps rule 90's period-2 clock on the whole line (`no_finite_clock90`); the one-sided wall deadlines here are different statements. Fibonacci parity and the squaring of linear rules are classical.

**What it does not do.** Rules 90 and 150 are linear and are not rule 30. Nothing here decides `Q01`, and the proof-size remarks of the essay are not formalised.

Portal entry: [R30-20261110-c20b0a](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261110-c20b0a).

🤖 Generated with [Claude Code](https://claude.com/claude-code)

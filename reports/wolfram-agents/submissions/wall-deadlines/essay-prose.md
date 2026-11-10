# The Wall Deadlines of Rules 90 and 150: The Kit's Period-Two Question Answered Exactly for Two Linear Relatives of Rule 30

Gareth Herbert; Claude (Anthropic); GPT (OpenAI). 10 November 2026.

## 1. The statement

The kit's `Q01` asks whether every finite start of the zero-boundary left half of rule 30 eventually turns depth `1` white at an even tick. Every rule of the form `left xor h(centre, right)` has the same frame beside a white wall (`zr h`). For `h = or` this is rule 30's frame, the kit's `zrow` (`zr_or_eq_zrow`). This module answers the question exactly for rules 90 (`h(b, c) = c`) and 150 (`h(b, c) = b xor c`), with the latest possible deadline.

- `deadline90`, `sharp90`: a start of width at most `W` turns depth `1` white at some even tick at most `k* - 1`, where `k*` is the least odd number above `W` that is not a multiple of `3` (`kstar`, `kstar_spec`). Every start of width at most `W` whose odd depths follow Fibonacci modulo `2` stays black at depth `1` at every earlier even tick.
- `deadline150`, `sharp150`: for rule 150 the deadline is `2⌈W/2⌉`, and it is attained by every start whose odd depths are all black.

So the latest deadline is `k* - 1` for rule 90 and `2⌈W/2⌉` for rule 150, both linear in `W`. For comparison, rule 30's latest deadlines for widths `2` to `12` are `6, 6, 6, 8, 10, 12, 12, 18, 18, 30, 30` by direct computation (COMPUTED, not proved here).

## 2. Rule 90: a closed parity class

Read sideways, rule 90 says `x(k+1, t) = x(k, t+1) + x(k-1, t)`. All three cells have the same parity of depth plus tick. So the cells with depth plus tick odd form a closed system, bounded by the white wall and by the black column at even ticks; no free bit enters it.

- `odd90`: by induction on the depth, each such cell is `φ(k)`, Fibonacci modulo `2`, which is white exactly at the multiples of `3` (`fib2`, `fib2_mod`).
- At tick `0` this fixes every odd depth of the start. The least odd depth above the width that is not a multiple of `3` must be black, but the width makes it white. That gives `deadline90`.
- Conversely, `φ` on the odd class satisfies the forward rule (`fwd90`). The light cone of depth `1` at the even ticks before the deadline only reaches odd depths above `W` that are multiples of `3`, where `φ` is white anyway (`sharp90`).

## 3. Rule 150: two steps on the odd depths

Two steps of rule 150 act on the odd depths at even ticks by their own rule (`two_step150`):

`x(k, t+2) = x(k+2, t) + x(k, t) + x(k-2, t)`, and `x(1, t+2) = x(3, t)` at the wall.

- `odd150`: read backwards, this makes every odd depth black at every even tick inside the triangle, given the black column. At tick `0` the least odd depth above `W` would have to be black, which gives `deadline150`.
- Conversely, all-black odd depths stay black under the two-step rule (`fwd150`), which gives `sharp150`.

## 4. Scope

Rules 90 and 150 are linear and are not rule 30. They share rule 30's frame and its left permutivity, and, by the same sideways count as the kit's `count_constrained` (not formalised here for them), its number of surviving starts per tick before the deadline. Their deadlines are explicit and linear. Nothing here decides `Q01`.

A remark on proof size, not formalised here. Cloud's carried argument shows that these deadlines are found by unit propagation for rule 90, and by width-5 resolution for rule 150, on the natural SAT encoding. So no argument that only uses properties shared by the whole family can give a superpolynomial lower bound on refuting the rule 30 formulas.

## 5. Worked numbers

The cell below computes, by brute force over all starts of width at most `W` for `W = 1, …, 12`:
- the latest first white even tick for each rule, against `k* - 1` and `2⌈W/2⌉`;
- whether the starts attaining the deadline are exactly the pattern rows (odd depths Fibonacci for rule 90, all black for rule 150), `2^⌊W/2⌋` of them.

## 6. Prior art and scope

- **The family.** The kit's `Rule30Realization` (`center90`, `center150`, `barrier`) shows that rules 90, 150 and 210 share left permutivity and Jen's hypotheses with rule 30.
- **Related submissions.** Our earlier submission R30-20261023-1bf4dc proves the whole-line statement that no finite configuration keeps rule 90's period-2 clock (`no_finite_clock90`). The one-sided wall deadlines here are different statements. The plant half of S-08 and `Rule30HybridWall` treat other relatives of rule 30.
- **The methods.** Fibonacci parity and the squaring of linear rules over `GF(2)` are classical.
- **What is new.** The exact wall deadlines and the classes of starts attaining them, with formal proofs.
- **History.** It came from a sub-agent run of our programme. Cloud carried the hand proof, and Local formalized it.

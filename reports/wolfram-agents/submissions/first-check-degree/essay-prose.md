# The First Check of the Zero-Boundary Left Half: Its Weight Is n mod 2, Its Degree Is n or n - 1, and the Other Clock Phase Is Always Odd

Gareth Herbert; Claude (Anthropic); GPT (OpenAI). 10 November 2026.

## 1. The statement

In the zero-boundary left half, keep column `-1` black at every even step and let its values at the odd steps be free bits `f 0, f 1, …`. The kit reconstructs the whole row from that column (`Rule30ZeroBoundary.Theta`). The first cell past `n` free bits is the cell at depth `2n + 1`, the kit's first check `Rule30FirstChecks.check n`, a Boolean function of `f 0, …, f (n - 1)`.

This module fixes its algebraic normal form over `GF(2)` for every `n`. The coefficient of a monomial is the exclusive-or of the function over the points below its mask (`coeff`), and every function is the exclusive-or of the coefficients below its argument (`anf_expansion`).
- `top_coefficient`: for `n ≥ 1`, the coefficient of `f 0 ⋯ f (n - 1)` is `n mod 2`.
- `omit_coefficient`: for `n ≥ 2`, the coefficient of the monomial of every free bit except `f 1` is `n + 1 mod 2`.
- `check_degree`: so the check has degree `n` for odd `n` and `n - 1` for even `n`. At even `n` the top coefficient only bounds the degree; the second coefficient fixes it.
- `ones_parity`: for `n ≥ 1`, the number of words on which the check is black is congruent to `n` modulo `2`.
- `first_check_parity`: for `n ≥ 1`, the number of rows of width at most `2n` that are black at column `-1` at every even tick through `2n` is congruent to `n` modulo `2`. This uses the kit's count `first_check_count` and is a congruence, not a count.
- `walsh_mod_four`, `walsh_one`: the Walsh sum `2^n - 2 ones(n)` is `2` mod `4` exactly at odd `n ≥ 2`. At `n = 1` it is `0`, so the guard `n ≥ 2` is needed.
- `other_phase_odd`: in the other clock phase, with the free bits at the even steps and column `-1` black at the odd ones, the check at depth `2n` has top coefficient `1` for every `n ≥ 1`. Its weight is always odd, so the two phases differ at every even `n`.

## 2. The derivative along an anti-diagonal

The cell at depth `k` and time `t` reads column `-1` at times `t, …, t + k - 1`. Call `t + k - 1` its anti-diagonal. The kit's `recon_aff` says that the cell depends affinely on its newest entry, with coefficient `1`.

Flip one entry of column `-1`, at time `d - 1`, and keep the rest.
- Every cell on anti-diagonal `d - 1` flips.
- Cells on earlier anti-diagonals are unchanged.
- Each cell on anti-diagonal `d` is the cell one depth shallower and one step later, on the same anti-diagonal, exclusive-or `(y OR z)`, where `y` is on anti-diagonal `d - 1` and `z` on `d - 2`. Flipping `y` changes `y OR z` by `NOT z`.

So the top cell changes by the exclusive-or of the negated cells two anti-diagonals back (`diag`, with the sum `zs`).

## 3. The two recurrences

For the check, the newest entry, at time `2n`, is a fixed black cell, and the entry before it is the newest free bit `f (n - 1)`. Summing over `f (n - 1)` therefore leaves the derivative, and the remaining sum runs over `f 0, …, f (n - 2)`.

Every derivative cell at a time `≥ 2` does not read `f 0`, which sits at time `1`. Summing over `f 0` kills it, and so do the negations, which are constants summed over at least two points. Two cells survive:
- the previous check, at time `0`;
- the cell `bcell` at depth `2(n - 1)` and time `1`.

So the top sum changes by the top sum of `bcell` (`top_succ`). The same argument for `bcell` leaves only the previous `bcell` at time `1` (`bsum`), so that sum is `1` at every step. The top coefficient is `1` at `n = 1`, where the check is `f 0`, and it changes at every step after that.

For the coefficient without `f 1`, fix `f 1 = 0` before summing (`ins`). The same two cells survive, and the base cases move to `n = 2` and, for `bcell`, `n = 3` (`rsum_succ`, `tsum_succ`).

In the other phase, `g 0` sits at time `0`. So only the cell at time `0`, the previous check, survives (`other_flip`), and the top coefficient keeps its initial value `1`. This pinpoints the difference between the phases: two surviving time slices against one.

## 4. Scope

These are exact statements about one Boolean function for every `n`. They do not say how often a long run of checks passes, and nothing here bears on the single seed. The survivor statement is a congruence modulo `2`, not a count.

## 5. Worked numbers

The cell below computes, for the words of length `n`:
- whether `ones(n) ≡ n mod 2` for `n = 1, …, 12`, and whether the words with `f 1 = 0` give `n + 1 mod 2` for `n = 2, …, 12`;
- the algebraic degree of the check for `n = 1, …, 10`, by the Möbius transform of its truth table;
- the rows of width at most `2n` that pass every even check through `2n`, by direct simulation, for `n = 1, …, 6`;
- the Walsh sum modulo `4` for `n = 1, …, 12`;
- whether the other phase has odd weight for `n = 1, …, 12`.

## 6. Prior art and scope

- **The kit's inputs.** The reconstruction, `recon_aff` and `Theta` are the kit's (`Rule30ZeroBoundary`). The check, its weight `ones` and the count `first_check_count` are the kit's `Rule30FirstChecks`, which is reused, not reproved.
- **The method.** Differentiating along the newest variable, which left permutivity makes enter linearly, is the method of the kit's [`AlgebraicDegree`](https://github.com/WolframInstitute/Rule30PrizeKit/blob/03a19bf6240b63c6d15894c5f7552f3a6091d937/equivalents/Rule30Equivalents/AlgebraicDegree.lean), which finds the degree of the unconstrained `t`-step map. Summing out a variable after a triangular substitution is the method of the kit's `Rule30WedgeParity` and `Rule30TopCoefficient`. Those modules treat different functions, on free initial cells or free diagonals, and this module does not rely on them.
- **The other phase.**
  - N. Berzai's paper ([rule30-left-edge](https://github.com/nateberzai-svg/rule30-left-edge/tree/d9cb3d57b28f5a713a4ac28c11f5723cbe14d6a4), 8 October 2026), in the subsection on the left machine for the tail `01`, works in the other phase. It states that the weights of its checks are odd, labelled proved, without a parity proof in that subsection.
  - The code it cites ([rule30-prize](https://github.com/cochon123/rule30-prize/tree/0ff6930488bfa5e9c244b2caa05835907217077f)) computes the same reconstruction in that phase.
  - [`forced-bits-dense`](https://github.com/lhallee/rule30-open/blob/1ddcd41186e245d6a001604e15b584981990591a/negative-results/period-two/forced-bits-dense.md) in `rule30-open` computes the forced bits of that phase as polynomials of full degree for twelve widths, in row coordinates. Full degree is odd weight, which the triangular change between row bits and free bits keeps, so that table agrees with `other_phase_odd` up to `n = 12`.
  - Berzai's centre alternates rather than staying white. At the odd times, when it is black, the cell next to it is forced black, so its OR with the centre is unchanged if the centre is replaced by white. That comparison argument is ours and is not formalized here.
- **What is new.** The all-`n` law in the kit phase (top coefficient `n mod 2`, degree `n` or `n - 1`), its corollary for the survivors, the Walsh exception at `n = 1`, and an all-`n` formal proof of the odd weight in the other phase.
- **History.** It came from a sub-agent run of our programme. GPT carried the hand proof with its repairs: the guard `n ≥ 2` on the Walsh sum, and the second coefficient needed for the degree at even `n`. GPT also made the phase comparison. Local formalized it, adding the other phase.

# The Free-Middle Theorem: Late Survival Does Not Restrict Additive Ranks of Rule 30's Zero-Boundary Left Half

Gareth Herbert; Claude (Anthropic); GPT (OpenAI). 10 November 2026.

## 1. The statement

The kit's `Q01` is the period-2 form of Problem 1 in the zero-boundary left half. It says that every finite start eventually turns column `-1` white at an even time. A termination proof would be a rank: a natural number attached to each row that strictly decreases along every surviving double step. The kit's barrier `Rule30ZeroBoundaryBarriers.no_local_ranking` (B2) shows that no function of the width, a wall window of `w` cells and an edge window of `e` cells can be such a rank. This module strengthens B2 in two directions at once. The rank may contain an additive density, and it need only decrease on rows passing a width-dependent cutoff, with a margin tending to infinity.

Fix `u : Nat → Nat` with `u(W) → ∞`. A row of width `W` is *late* (`Late u s W`) if its double step survives and depth `1` is black at every even time up to `W - u(W)`. A *rank* is `β(W, wall window, edge window) + Σ h(window)`, where the sum runs over the `m`-cell windows of the row and `β` and `h` are arbitrary integer functions. Here `m ≥ 1` and `e ≥ 1`. The boundary reduction and additive-ranking obstruction use `w, e ≥ m - 1`; fixed shorter windows can be enlarged while ignoring the extra cells.

- `free_middle`: suppose the rank is at least `-K W` on late rows and never increases along their double steps. Then `h` is conserved on every closed walk of overlapping windows, in the sense of the kit's `Rule30LocalConservation.CyclicConserved`. By the kit's `cyclic_conserved_iff_shift_coboundary`, `h` is a constant plus a shift coboundary (`free_middle_coboundary`).
- `rank_local`: once both windows have at least `m - 1` cells, such a rank is a function of (width, wall window, edge window) alone.
- `no_local_ranking_late`: no function of (width, wall window, edge window) is nonnegative on late rows and strictly decreases along their double steps.
- `no_additive_ranking_late`: hence no rank of the additive form does either.
- `lower_bound_needed`: the lower bound cannot be dropped. Popcount minus `W²` strictly decreases along every surviving double step of every finite row, and popcount is not a constant plus a coboundary.

Survival short of the whole row therefore puts no constraint on additive potentials beyond the boundary windows.

## 2. Why the middle is free

Survival through time `T` reads only the depths `1, …, T + 1` of the start, because that is where the light cone of depth `1` at time `T` ends. The two baseline checks at times `0` and `2` are required as well. Thus all the check conditions of a late row lie inside the prefix of length `B(W) = max(3, max(W - u(W), 0) + 1)`. The number of depths beyond that sufficient prefix is `max(W - B(W), 0) = min(max(W - 3, 0), max(u(W) - 1, 0))`. It tends to infinity with `W`, even when `u(W)` exceeds `W`. Exact width fixes the top cell, and the boundary labels and interfaces use a fixed further number of cells; the remaining middle still grows without bound.

The proof plants a cyclic word `d` in that free part. Its row (`mkRow`) has three parts:
- the stripe `…10101` on the first `D` depths;
- `μ + 2` periods of `d`;
- an edge label of `e` cells on top.

The stripe is a fixed point of the zero-boundary dynamics (`zrow_stripe`), so a long enough stripe makes the row, and its double step, late. After four steps the windows inside the stripe are unchanged. Each period of `d` contributes exactly the four-step rise of `d` (`rho`), up to a bounded error from the two interfaces and the edge (`rise_mkRow`).

## 3. The proof

Suppose some cyclic word `d` of length `N ≥ m + 8` has a positive four-step rise `ρ`.
- **The rows.** Build planted rows of widths `W₀ + 4n` whose middles hold `μₙ + 2` periods of `d`, with `μₙ` chosen from `u` so that the rows stay late and `μₙ → ∞`.
- **The labels.** Each row's edge label is the edge window the previous row has four steps later (`labels`). Then `Bₙ = β(W₀ + 4n, stripe wall, label n)` is the same number at the end of one step and the start of the next.
- **Descent.** Descent along two double steps gives `Bₙ₊₁ ≤ Bₙ − μₙ ρ + C`, with `C` independent of `n`.
- **The lower bound.** It gives `Bₙ ≥ −(K + H)(W₀ + 4n)`, where `H` bounds `|h|`.
- **Contradiction.** Since `μₙ → ∞`, the descent eventually drives `Bₙ` down faster than the lower bound allows (`rho_nonpos_of_descent`).

So no cyclic word of length at least `m + 8` has a positive rise. Balance rules out negative rises too.
- **Balance.** Summed over all `2^N` cyclic words of a length `N ≥ m + 8`, the four-step rise is zero (`wsum_rho`). The four-step image of an `(m + 8)`-cell word is `2⁸`-to-one onto the `m`-cell words (`wsum_image`), and so is the crop to its middle `m` cells (`wsum_crop`). The image count is left permutivity: the leftmost cell enters each output by exclusive or.
- **Closed walks.** Every closed walk of the kit's form is, after repetition, a cyclic word of length at least `m + 8` (`closed_weight_eq_rho`). That gives `CyclicConserved` (`cyclic_conserved_of_rho`).

For the restricted B2 (`no_local_ranking_late`), the kit's own proof works after one change. It uses the truncated stripes `trunc n` and finitely many of their double steps, up to some `j₂`. Those rows are late once `u ≥ 4 j₂ + 2` at their widths, and long enough truncations ensure that.

## 4. Scope

- **Densities.** The densities are integer-valued; rational densities reduce to integer ones by clearing denominators.
- **The margin.** `u` must tend to infinity. A bounded margin is not covered: it leaves only a bounded reservoir by this construction. The case `u = 0` requires checks through the whole width. No claim about the bounded-margin case follows from this theorem.
- **Which rows.** As in the kit's barriers, the late population includes rows that are not the left half of rule 30 under an alternating centre.
- **Not claimed.** Nothing here bears on nonlinear or nonlocal rankings, decides `Q01`, or proves Problem 1.

## 5. Worked numbers

The cell below checks balance and the planted rise by direct computation.
- **Balance.** It takes popcount on cyclic words of length `9`, and the count of `11` on cyclic words of length `10`. For each it lists the total four-step rise over all words, the largest rise, and the numbers of words whose rise is positive and negative.
- **The planted rise.** It takes a cyclic word `d` of length `9` whose popcount rise, read from its deep end, is largest. It plants `μ + 2` periods of `d` after a stripe of `12` depths, under one black top cell, and reports the four-step popcount change of that row. The change grows by exactly the rise of `d` with each step of `μ`.

## 6. Prior art and scope

- **The kit.** The kit's B2 (`Rule30ZeroBoundaryBarriers.no_local_ranking`) and its classification of conserved densities (`Rule30LocalConservation`) are used, not reproved. The latter cites T. Hattori and S. Takesue, Physica D 49 (1991), 295–322. The balance of left-permutive maps is classical (G. A. Hedlund, Math. Systems Theory 3 (1969), 320–375).
- **rule30-open.** [`lhallee/rule30-open`'s note on conservation laws](https://github.com/lhallee/rule30-open/blob/1ddcd41186e245d6a001604e15b584981990591a/negative-results/structure/conservation-laws.md) finds no additive conservation law on the single cell's orbit or on block counts. Its orbit and finite-width searches remain computations; it also cites the kit's all-width classification of conserved densities. Neither those searches nor that classification supplies a nonincrease-to-conservation argument on the late population. We retain the late-population additive-rank theorem as the additional formal statement, without a broader priority claim.
- **Where it came from.** The statement and a first proof came from a sub-agent run of our programme. GPT carried it, with repairs to the balance step, to the restriction to the late population and to the role of the lower bound.

What is new here, in Lean, is the barrier for the late population, with additive densities and its necessary lower bound. Nothing here proves `Q01` or Problem 1.

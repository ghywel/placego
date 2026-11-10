# No Ranking Through a Recognizable Statistic: The Kit's Ranking Barriers for Period Two Extended to Finite-Monoid Images, and Two Rows That Defeat Every Width-Bounded Rank

Gareth Herbert; Claude (Anthropic); GPT (OpenAI). 10 November 2026.

## 1. The statement

The kit reduces an eventual period `2` of rule 30's center column to `Q01`, a question about the zero-boundary left half. A natural way to prove `Q01` would be a ranking function: a rank on finite rows that falls at every *surviving* double step, one that keeps depth `1` black at the two even ticks. The kit's `Rule30ZeroBoundaryBarriers` rules out two such shapes:
- `no_local_ranking` (`RankCert`): no natural-number rank of the width, a window at the wall and a window at the edge;
- `no_edge_dfa_ranking` (`CertE`): no rank given by the longest prefix of the row, read from its edge, that a finite automaton accepts.

The same module has a coupled two-sided version, `no_joint_local_ranking` (`JointCert`), over all finite configurations, with a strict fall at every flip of the center column.

A *recognizable statistic* of a row is its image under a morphism from Boolean words into a fixed finite monoid (`FinMonoid`, `FinMonoid.eval`). It is the classical notion behind regular languages: what a finite automaton remembers about a whole word. This module adds such a statistic to the arguments of the rank, and lets the rank take values in any well-founded order.

- `no_recognizable_ranking`, `no_recognizable_ranking_nat`: no rank of (width, image of the row read from its edge) falls at every surviving double step of every finitely supported row. `no_wall_recognizable_ranking`: the same with the row read from the wall. Reversing a word is reading it in the opposite monoid (`FinMonoid.op`, `FinMonoid.eval_reverse`).
- `no_windowed_recognizable_ranking`: the same with the kit's wall and edge windows added. For the one-element monoid it is the kit's `no_local_ranking` (`no_local_ranking_of_recognizable`).
- `no_joint_recognizable_ranking`, `no_joint_recognizable_ranking_nat`, `no_joint_windowed_recognizable_ranking`: the coupled frame. The statistic is the image of the whole configuration between its leftmost and rightmost black cells, read from left to right (`spanWord`). For the one-element monoid it is the kit's `no_joint_local_ranking` (`no_joint_local_ranking_of_recognizable`).
- `no_width_bounded_ranking`: no integer rank between `-1` and the width falls at every surviving double step. So `no_edge_automaton_ranking`: the kit's automaton barrier holds for every automaton with states in `Nat`, with no bound on their number.

## 2. The zero-boundary frame

The witnesses are the kit's truncated stripes `trunc n`, the stripe `…10101` cut off at an odd depth `n`, which survive for a long time.
- `edge_decomp`: for odd `n`, `j ≥ 1` and `4 j ≤ n`, the row after `j` double steps, read from its edge, is a word `Zw j` of length `4 j - 1` followed by `k = (n + 1 - 2 j) / 2` copies of `01`. The word `Zw j` does not depend on `n`.
- The images of the powers of `01` in the finite monoid are eventually periodic, with some period `π` from some index on.
- Along `j = 1 + i π`, two of the finitely many values of (image of `Zw j`, edge window) agree, at some `j₁ < j₂`, and `d = j₂ - j₁` is a multiple of `π`.
- Only then is the odd base depth `n₀` chosen, large enough for both times. Write `r m j` for the row after `j` double steps from `trunc (n₀ + 2 m)`. The rows `r m j₂` and `r (m + d) j₁` have the same width, the same windows and the same image, because their stripe exponents differ by `2 d`.
- A certificate would carry `r (m + d) j₁` down to `r m j₁` through the steps from `j₁` to `j₂`, for every `m`. That is an infinite descent in a well-founded order (`no_descent`).

## 3. The coupled frame

The witnesses are the truncations `c7cut N` of the spatially `7`-periodic orbit.
- `c7cut_span`: at a time `t = 28 c` with `2 t ≤ 14 N + 8`, the row between its ends is a left wedge of `2 t` cells, an ether word of length `14 N + 8 - 2 t`, and a right wedge of `2 t` cells.
- The wedges and the edge windows do not depend on `N` once `N` is large (`wedgeData_indep`). The center column flips at every tick in range, so a certificate falls at each of them (`jrank_step`, the kit's `jointRank_step` with the monoid image added).
- Pigeonhole both wedge images and both edge windows over the times `28 π i`, at some `i₁ < i₂`. Compare the rows `(N, t₂)` and `(N + ε, t₁)` with `7 ε = t₂ - t₁`. They have the same ends, the same center window and the same windows, and their ether lengths differ by `28 ε`, a multiple of `7 π`. So they have the same image, and the same descent follows.

## 4. Two sharp rows

`sharp_rows_check` is a kernel evaluation of the kit's integer form `G` of the double step. The rows `1493` and `1507`, of width `11`, keep depth `1` black at the even ticks `0, 2, …, 28` and turn it white at tick `30`. So they survive fourteen double steps (`sharp_rows_survive`, `sharp_rows_fourteen`). A rank between `-1` and the width that fell at each of them would go from at most `11` to below `-1` (`no_width_bounded_ranking`). The longest accepted prefix of a word lies between `-1` and its length, so `no_edge_automaton_ranking` follows for every automaton.

## 5. Worked numbers

The cell below computes, independently of the Lean module:
- the first even iterate of `G` from `1493` and from `1507`;
- for each bit length `L = 1, …, 12`, the largest first-even index over the odd rows of that length, and the rows attaining it at `L = 11`;
- the decomposition of `edge_decomp`, for every odd `n` from `5` to `41` and every `j` with `4 j ≤ n`: the width `n + 2 j`, the run of `01` pairs, and a prefix that depends only on `j`.

The largest first-even index by bit length is `1, 3, 2, 3, 4, 5, 6, 5, 9, 7, 15, 8`, so the bound "bit length plus four" is attained at length `11`, and there only by `1493` and `1507` (COMPUTED).

## 6. Prior art and scope

- **The barriers and the witnesses** are the kit's: `Rule30ZeroBoundaryBarriers` with `RankCert`, `CertE` and `JointCert`, the truncated stripes with `edge_split` and `Z_shift`, and `c7cut` with `jointRank_step`. This module adds the monoid image and general well-founded ranges; the kit's two-window theorems are its one-element-monoid cases.
- **Recognizable statistics** are classical: a language is regular exactly when it is recognized by a morphism into a finite monoid.
- **The two rows.** The portal entry R30-20261108-a0fd36, by a third party, observed that `1493` and `1507` are sharp for its bound, a first even iterate at most the bit length plus four. Here their survival is kernel-checked and turned into a barrier.
- **Scope.** The certificates quantify over all finite rows or configurations, and so do the witnesses. Nothing here covers ranks whose values do not factor through a finite monoid and the width, such as value-unbounded weighted automata, or obligations restricted to particular starts. As in the kit (`trunc_not_left_half`), the truncated stripes are never the left half of rule 30 at the start of an alternating tail. So these barriers concern arguments that use the zero-boundary dynamics alone. Nothing here decides `Q01` or period `2`.
- **History.** Cloud's swarm run proposed B2+ (BR-2.1) and the width-bounded rider (LN-06). GPT carried B2+ by hand in both frames. A Local sub-agent formalized both under Local's direction, and Local checked and packaged the module.

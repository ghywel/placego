# A Sharp Black-Count Bound on Five Adjacent Columns of Every Rule 30 Trajectory

Gareth Herbert; Claude (Anthropic); GPT (OpenAI). 10 November 2026.

## 1. The statement

Take any initial configuration on the integer line, evolve it by the official rule `new(i) = old(i-1) xor (old(i) or old(i+1))`, and fix any five adjacent physical columns. In any interval of `T` ticks they contain at most `3T + 2` black cells (`evol_five_column_bound`). The interval includes its first row and excludes its final endpoint. `T = 0` is allowed. The starting time is arbitrary.

The source also proves the bound for any array satisfying the Rule 30 recurrence (`five_column_bound`), and specializes it to the kit's official singleton diagram (`cell_five_column_bound`). No random-row, finite-support, periodicity or capture assumption occurs.

## 2. A short potential

For a five-cell word `u = (a,b,c,d,e)`, let `pop(u)` count black cells and put

`H(u) = max(0, 2 - (b+c+d+e))`.

The first cell is deliberately omitted from this potential. Its range is `0..2` (`potential_bounds`). On every seven-bit input word, let `u` be its middle five cells and `v` the five updated cells. Both exterior input bits are free. The local inequality is

`pop(u) - 3 <= H(v) - H(u)` (`local_potential`).

The proof checks all seven Boolean inputs in the Lean kernel. There is also a short case explanation. If the right four input cells contain zero or one black cell, the required lower bound on `H(v)` is nonpositive. With two or more, `H(u)=0`, and input population at most three is immediate. If the input has four black cells, at most one of the right four output cells is black; if all five inputs are black, those four outputs are all white. These give the required lower bounds one and two.

## 3. Telescope and sharpness

Along an actual trajectory the local inequalities telescope. Writing `C5` for the black count in the window gives

`C5 <= 3T + H(final) - H(initial)` (`telescope`).

The range of `H` then gives `C5 <= 3T + 2`. The module counts bits as integers, with black equal to one. Its separately defined white count plus black count is exactly `5T`, so the window contains at least `2T - 2` white cells (`white_column_bound`).

The additive constant two is necessary already at `T=1`: a real initial row can be all black in the five-cell window, giving count five (`sharp_constant`). The coefficient three is necessary too. The alternating row is fixed by Rule 30, and a window `10101` contains exactly three black cells at every time (`sharp_rate`, at every horizon). These are actual configurations, not just cycles of a relaxed window graph.

## 4. What the bound controls

The result is an upper bound on a sum over five columns. It proves no density limit, no positive lower density of black cells and no stronger conclusion for the singleton. In particular, the sharp alternating example has individual columns permanently black or permanently white, so the five-column statement supplies no individual-column ceiling. Neither of its sharpness examples is the finite singleton seed.

## 5. Worked numbers

The numerical cell checks all 128 seven-bit windows and counts the 70 tight inequalities. It also checks three deliberately wrong controls: the mirrored potential fails on 8 edges, replacing the potential at the all-white word by zero fails on 3 edges, and using rule 150 with the same certificate fails on 16 edges. These are illustrative checks of the finite certificate. The formal proof covers all trajectories and horizons without relying on the numerical cell.

## 6. Prior art and provenance

The method of summing local inequalities and telescoping a bounded potential is standard. Related results are the count-transfer bounds in [rule30-open's ColumnTransfer](https://github.com/lhallee/rule30-open/blob/1ddcd41186e245d6a001604e15b584981990591a/Rule30Open/Columns/ColumnTransfer.lean), and the source-dependent one-column bound in [kit PR253](https://github.com/WolframInstitute/Rule30PrizeKit/pull/253). They concern different observables and do not state this five-column ceiling. Earlier spin and finite-row population identities in our public record, and Cappallo's counting formula in [OEIS A070952](https://oeis.org/A070952), are context; no new version of those identities is claimed here.

The certificate came from our P2-3.1 swarm source, was independently carried by GPT, and was then formalized against the kit's actual rule/evolution definitions. The two source forms pass the official kernel replay with nine headlines and standard axioms. This is a partial result, with no claim of literature priority or prize solution.

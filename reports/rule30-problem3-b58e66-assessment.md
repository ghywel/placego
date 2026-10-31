# Assessment of R30-20261031-b58e66, the first Problem 3 entry (Local, L1254)

Owner's request, 31 October 2026: assess the new entry on Problem 3. The entry is
[R30-20261031-b58e66](https://www.wolframcloud.com/obj/rule-30-prize/Agents/status/R30-20261031-b58e66), "Head-Cone Locality,
2-Adic Transient Elimination, and Unconditional Step Lower Bounds for Prize Problem 3", by G.P.J.W. Quint and Gemini.
It was submitted at 10:00 UTC and is Lean Verified and Human Verified, with 14 headlines and standard axioms. It is also
kit PR [#68](https://github.com/WolframInstitute/Rule30PrizeKit/pull/68) (`Rule30Problem3Bounds`, open, no comments).
It replaces R30-20261031-0a5974, which Cloud saw Lean Unverified at 09:58Z (CL668). That page is no longer public and
b58e66 does not list it as superseded.

**Bottom line.** The entry is correct and honestly scoped. It is the first lower-bound machinery for the kit's Problem 3
model, and it complements the kit's upper-bound side. Its quantitative content is small:
- every unconditional bound is a constant, at most 5 steps;
- the logarithmic bound `log2 n + 2` is unconditional only for `n < 16`;
- the general form of that bound rests on a hypothesis that is at least as hard as the open period-2 case of Problem 1;
- even that bound is exponentially below what Problem 3 asks.

Two additions of ours follow below: one result machine-checked here, and one hand remark.

Record searched: the entry's complete source (424 lines, SHA256 prefix `3fd5cfe4`, read in full), its portal record and
verifier check, and kit main `842b756`. In the kit: `Rule30Problem3` (`dc117894`), `equivalents/Rule30Equivalents/ProblemThree`
(`918f53c3`), `Rule30FactorWindow`, the README's status-by-period table, and `known_find.py` (refreshed at 10:18Z) for
`Problem1`, `EvPer`, `two_pow`, eventual periods and small periods. On the portal: R30-20261023-603218 (Norris with
Jesse), whose headline 20 packages the kit's `Problem3 → Problem1` bridge.

## The model and the question

The kit's `Rule30Problem3` uses a deterministic one-tape Turing machine. Its input is `n` in binary, least significant
digit first, on cells `0, 1, …`; cell `i` holds a digit iff `2 ^ i ≤ n`, every other cell is blank, and the head
starts on cell 0. `Computes M f T` means that on every input `n` the machine halts within `T n` steps with `f n`.
The prize's formal `Problem3` says no machine computes `center` within `C · (n + 1)` steps. The input has about
`log2 n` digits, so this asks for time exponential in the length of the input. The kit also states `Problem3Verbal`
(no time `o(n)`) and `Problem3Robust` (no time `n^o(1)`).

The kit already has the other direction, in `Rule30Equivalents.ProblemThree`. A 2-automatic sequence is computed in
`|bin n| + 1` steps, so Problem 3 implies that the center column is not 2-automatic and implies Problem 1
(`problem1_of_problem3`, `not_isAutomatic_of_problem3Verbal`). Before b58e66 the kit had no lower bound of any kind
for its machine model.

## What the entry proves

Read in full against the kit's definitions.

1. **Locality** (`run_eq_of_init_eq_lt`). After `t` steps from head 0, the run depends only on cells `< t`. Negative
   cells are blank for every input.
2. **Residue collapse** (`init_tape_eq_of_mod_two_pow_eq`, `computes_eq_of_mod_two_pow_of_run_le`,
   `computes_const_on_dyadic_ray`). Inputs `m, n ≥ 2 ^ (k - 1)` with `m ≡ n (mod 2 ^ k)` have identical cells
   `0, …, k - 1`. So if the machine halts within `k` steps on one such `n`, then `f` takes the value `f n` on the
   whole class above `2 ^ (k - 1)`, below `n` as well as above it.
3. **Flip bounds** (`time_gt_of_mod_two_pow_ne`, `log2_succ_succ_le_time_of_ray_flip`). One pair in a class with
   different values forces `T ≥ k + 1` on the whole class. If `f (n + u · 2 ^ L) ≠ f n` for some `u`, where `L` is
   the digit length of `n`, then `T n ≥ log2 n + 2`: the machine must read past the last digit.
4. **The bridge** (`evPer_two_pow_of_eventually_time_le`, `time_unbounded_of_problem1`). Time at most `k` from `N` on
   makes `f` eventually `2 ^ k`-periodic. Hence Problem 1 implies that, for every `k`, the time exceeds `k`
   infinitely often.
5. **Uniform bounds** (`two_le_time` … `five_le_time`, `log2_succ_succ_le_time_lt_16`). Fourteen kernel-checked flip
   pairs, with center values up to time 99 (`decide +kernel`, which is allowed), give, for every machine computing
   `center`:
   - `T n ≥ k + 1` for all `n ≥ 2 ^ (k - 1)`, for `k = 1, …, 4`, so `T n ≥ 5` for every `n ≥ 8`;
   - `T n ≥ log2 n + 2` for `1 ≤ n < 16`.
   `center_eq_fastCenter` is a quadratic light-cone evaluator used to find those flips.

**Correctness.** The proofs are sound: the verifier replayed them and they are Human Verified, and my reading found no
gap. The statements say what the abstract says.

**Scope.** The abstract is accurate. The title's "Unconditional Step Lower Bounds for Prize Problem 3" is literally
true. A reader should know that the unconditional bounds are at most 5 steps, and that the only Rule 30-specific
input is the fourteen flip pairs. Items 1 to 3 hold for any function on this model: the standard indistinguishability
argument that a machine must read its input. Items 1–4 are new to the kit as Lean; the mathematics is textbook.

## Addition 1 (PROVED by machine): the bridge holds without Problem 1 for every k ≤ 13

The residue collapse gives more than item 4 uses. One input with time at most `k` fixes the answer on its whole class.
So time at most `k` from any `N` on gives period `2 ^ k` from `2 ^ (k - 1)` itself, whatever `N` is
(`period_of_eventually_time_le`). The kit's `Rule30FactorWindow.transient_add_period_ge` says an eventual period `P`
from `T` needs `T + P ≥ 16359`. Here `T + P = 3 · 2 ^ (k - 1)`, which is below 16359 for every `k ≤ 13`. Hence,
**unconditionally, every machine computing `center` takes at least 14 steps on infinitely many inputs**
(`time_unbounded_le_thirteen`, with `k ≤ 13` and any `N`). b58e66 states this only under Problem 1.

[`tests/probes/b58e66_unbounded13.lean`](../tests/probes/b58e66_unbounded13.lean) (SHA256 prefix `5dee68ac`) contains:
- the entry's sections 1–2, copied verbatim and credited;
- `period_of_eventually_time_le` and `time_unbounded_le_thirteen`.

It is a dev compile on Local's M5 with Lean 4.35.0, against the pipeline kit's core, which matches the verifier kit
`19540bf` (it has `Rule30Problem3` and `Rule30FactorWindow`). The run was under run_capped: 300 s CPU and 3 GiB caps,
1.7 s wall, 409 MiB, rc 0, compiled first time. Both theorems use only `propext`, `Classical.choice` and `Quot.sound`.
This is not the official checker; nothing is posted.

Prediction, stated before the compile: it compiles silently with standard axioms; any failure is a gap in the hand
argument. It held.

The gain is small: "infinitely often" up to 14 steps, against the entry's "always" up to 5. It shows that the bridge's
reach is set by the kit's period exclusions, not by Problem 1.

## Addition 2 (PROOF-SKETCH, Local solo; GPT halted, unread): why the logarithmic bound stops at 16

`log2_succ_succ_le_time_of_ray_flip` needs, for each `n`, a `u` with `center (n + u · 2 ^ L) ≠ center n`. Holding this
for every `n` would rule out every eventual period `2 ^ j`. Suppose `center (t + 2 ^ j) = center t` for all
`t ≥ T0`, and take `n ≥ max T0 (2 ^ j)`. Then `L > j`, so `n + u · 2 ^ L` lies in the class of `n` mod `2 ^ j`, beyond
`T0`, and carries the same value: there is no flip at `n`. In particular the uniform bound would settle period 2,
which the kit lists as **open** (reduced to Q01). So this route cannot reach `log2 n + 2` for all `n` without a
Problem-1-type result. Even with one, a bound of `log2 n` is exponentially below Problem 3's `n`. That is the gap the
entry's machinery does not touch.

What it does teach: in this model, lower bounds for fixed `k` are finite searches. "`T ≥ k + 1` on every `n ≥ 2 ^ (k - 1)`"
holds iff every class mod `2 ^ k` has a flip. Unboundedness up to `k` reduces exactly to period exclusions with
transient `2 ^ (k - 1)`.

## Relation to our work

Problem 3 is not our line, and nothing of ours is affected. The entry's bridge goes the other way from R30-20261023-603218's
headline 20, which repackages the kit's `Problem3 → Problem1`, so there is no duplication. A kit PR or a comment on
#68 with Addition 1 would be outward-facing and is the owner's call. It is offered, not done.

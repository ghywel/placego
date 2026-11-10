# If a Finite Row Survives, Its Free Word Is Not Sturmian-Like: Zero-Wall Diagonals, Bounded Lag and Rising Factor Complexity

Gareth Herbert; Claude (Anthropic); GPT (OpenAI). 10 November 2026.

## 1. The statement

The kit's `Q01` asks whether every finite start of the zero-boundary left half of rule 30 eventually turns depth `1` white at an even time. A start that never does is a finite constrained row: it is black at depth `1` at every even step, and its values at the odd steps form its free word `f` (`freeWord`). If `Q01` holds there are no such rows. This module proves what any such row would have to satisfy.

- `freeWord_complexity`: the free word `f` of a finitely supported constrained row satisfies, for every `K`, `n + K < p_f(n)` for all large `n`. Here `p_f(n)` is the number of distinct length-`n` factors (`factorCount`). So `p_f(n) - n` tends to infinity; such a word cannot have the bounded excess of Sturmian or quasi-Sturmian words.
- `freeWord_bounded_lag`, `freeWord_bounded_lag_of_finSupp`: for every slack `K` there is a bound `B` with the following property. Whenever the length-`n` blocks of `f` at `i < j` agree and `j ≤ n + K`, the lag `j - i` is at most `B`.

These are conditional theorems. They say something only if `Q01` fails, and nothing here proves or refutes `Q01`.

The route has two parts that hold unconditionally.
- **Zero-wall diagonals.** For any finite row with last black cell at depth `m ≥ 1`, measure diagonals from the moving edge: `E j t = zrow L t (m + t - j)`.
  - `E_entry`: the left-diagonal recurrence is guaranteed under the entry guard `j + 2 ≤ m + t`, equality included.
  - `E_tailLeft` packages the edge-measured diagonals as an array whose recurrence holds at each index from some time on (`TailLeft`).
  - For every such array: each coordinate is eventually periodic with period `2^j` (`tail_periodic`); finitely many `Q`-periodic coordinates obey `M + 3 ≤ 4^Q` (`tail_profile_bound`); eventually white coordinates are unbounded, never adjacent, and followed two later by an eventually black one (`tail_white_unbounded`, `tail_no_two_white`, `tail_black_after_white`).
  - So eventually black diagonals occur at arbitrarily large index (`tail_black_unbounded`, `E_black_unbounded`).
- **Words.**
  - `factorCount_succ`: the factor count rises by the number of right-special factors.
  - `rightSpecialCount_pos`: there is at least one right-special factor of every length unless the word is eventually periodic.
  - `two_run`: two long maximal runs of one period force two distinct right-special factors of one length.
  - `complexity_of_bounded_lag`: an aperiodic word whose bounded-slack repeats have bounded lag has `p(n) - n → ∞`.

## 2. Zero-wall diagonals

The recurrence `E (j+2) (t+1) = E j t xor (E (j+1) t or E (j+2) t)` is rule 30 solved for its left input, read along the diagonal at fixed distance `j` from the edge. It is the kit's `zrow_succ` at depth `m + t - (j + 2)`. At equality the right input is the wall at depth `0`, which is white, so the recurrence still holds there. One step earlier the updated cell would be the wall itself, so this derivation no longer applies. The recurrence can hold accidentally outside the guard; the worked numbers exhibit a point where it fails. The guard is a sufficient domain for the identity, not an if-and-only-if condition.

So a diagonal obeys the recurrence only from its entry time. The kit's single-seed left-diagonal theory (`Rule30Diagonals`, `Rule30LeftReset`, `Rule30LeftUnbounded`) assumes the recurrence from time `0`. Here every argument takes the maximum of finitely many entry and period thresholds, and never one threshold for infinitely many indices. The periodic-profile bound reuses the kit's array-free inverse map and its pigeonhole: the `M + 3` profile pairs, the ghost pairs before the edge included, are pairwise distinct, so `M + 3 ≤ 4^Q`.

## 3. From black diagonals to bounded lag, and from bounded lag to complexity

Two steps of the constrained row shift its free word by one place (`row_eq_Theta`). With the kit's `Theta_dep`, two equal length-`n` blocks of `f` at `i` and `j` make the rows at times `2i` and `2j` agree through depth `2n + 1` (`rows_agree`).

Take an eventually black diagonal `b ≥ m + 2K - 1` with black onset `T`, and suppose the lag `j - i` exceeds `max(b/2, (T+1)/2)`. Then the later row has a black cell at depth `m + 2j - b`. That depth lies beyond the earlier row's support but inside the agreed range, which is a contradiction (`lag_le_of_black`). This gives `freeWord_bounded_lag`.

For an aperiodic word, suppose `p(n) ≤ n + K` for arbitrarily large `n`. The excess `p(n) - n` never decreases, so it is eventually constant, and then there is exactly one right-special factor per length. By `two_run`, the `q`-periodic factors then have bounded length for each `q` (`perRun_bounded`). But two equal windows among the first `n + K + 1` positions have lag at most `B`, and their union is a periodic factor longer than any of those bounds. So `p(n) - n → ∞`.

## 4. Scope

- **Conditional.** The free-word theorems apply to finitely supported constrained rows, which exist only if `Q01` fails. If `Q01` holds they are vacuous. The moving-edge black/white diagonal theorems require a nonzero finite row with a last black cell at positive depth. The entry identity itself needs no support or nonzero hypothesis.
- **No rate.** `p(n) - n → ∞` is qualitative. No rate is claimed.
- **Excluded.** The queue's separate near-square claim is not part of this module.
- **The count.** `factorCount` counts factor codes below `2^n`. `le_factorCount` and `factorCount_le` show it is exactly the number of distinct factors.

## 5. Worked numbers

The cell below runs the zero-boundary left half from the single black cell at depth `1` for 600 steps. It reports:
- whether the edge-diagonal recurrence holds at every point inside the guard `j + 2 ≤ m + t`, for `j ≤ 12`;
- whether it fails somewhere just outside the guard;
- whether each of `E_0, …, E_10` is periodic on the window `400 ≤ t < 600` with a period dividing `2^j`, and those minimal periods;
- whether the displayed 20,000-bit Fibonacci prefix exhibits exactly `n + 1` factors and one right-special factor at each tested length `n ≤ 12`. This is a finite illustration; the infinite word is the standard Sturmian example.

That last line shows the boundary case `freeWord_complexity` excludes for free words.

## 6. Prior art and scope

- **Words.** Morse and Hedlund (1938) show that an aperiodic word has at least `n + 1` factors of each length, and the identity `p(n+1) - p(n) =` (number of right-special factors) for binary words is classical (Cassaigne, *Complexité et facteurs spéciaux*, 1997). Both are reproved here in core Lean. The kit's `ShiftOrbit` and `WordsAutomata` contain the Morse–Hedlund equivalences in Mathlib form. Repetitions in low-complexity words are studied by Bugeaud and Kim (Trans. AMS 371, 2019). We claim no priority for the abstract implication `complexity_of_bounded_lag`.
- **Diagonals.** The left-diagonal theory and the profile bound are the kit's `Rule30Diagonals`, `Rule30LeftReset` and `Rule30LeftUnbounded`, for the single seed. This module ports them to the zero wall with entry-time guards. `Theta`, `Theta_dep` and `free_not_eventuallyPeriodic` are the kit's `Rule30ZeroBoundary`.
- **What is new.** The guarded zero-wall diagonal package, and the conclusion that the free word of any surviving finite row has unbounded complexity excess.
- **History.** The statement came from a sub-agent run of our programme and was carried by GPT. GPT then proposed this tail-recurrence route and the explicit word witnesses, and Local carried both. A Local sub-agent formalized it; Local read and checked it.

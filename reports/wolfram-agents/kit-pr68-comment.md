<!-- Posted on kit PR #68 by the owner's account at 2026-10-31 10:37:32Z, on the owner's instruction (L1255): https://github.com/WolframInstitute/Rule30PrizeKit/pull/68#issuecomment-6542314565 . Byline removed at the owner's request; prose paragraphs unwrapped for GitHub. -->

Thanks for this. We read the submission's source against `Rule30Problem3`. One small strengthening falls straight out of your residue collapse.

`computes_eq_of_mod_two_pow_of_run_le` needs `T n ≤ k` on just one input of a class to fix `f` on the whole class above `2 ^ (k - 1)`. So if `T n ≤ k` from some `N` on, every class mod `2 ^ k` has such an input beyond `N`, and `f` has period `2 ^ k` from `2 ^ (k - 1)` itself, whatever `N` is. `evPer_two_pow_of_eventually_time_le` gives the transient `max N (2 ^ (k - 1))`. With the transient fixed at `2 ^ (k - 1)`, the kit's `Rule30FactorWindow.transient_add_period_ge` (`T + P ≥ 16359`) applies, because `2 ^ (k - 1) + 2 ^ k < 16359` for every `k ≤ 13`. So for `center` itself the step count is unbounded up to 14 without assuming Problem 1:

```lean
-- needs `public import Ruliology.CellularAutomata.Rule30FactorWindow`

/-- If `M` computes `f` and takes at most `k` steps from `N` on, then `f` has period `2 ^ k` from
`2 ^ (k - 1)` on, whatever `N` is. -/
theorem period_of_eventually_time_le {M : Machine} {f : Nat → Bool} {T : Nat → Nat}
    (hM : Computes M f T) {k N : Nat} (hT : ∀ n, N ≤ n → T n ≤ k) :
    ∀ m, 2 ^ (k - 1) ≤ m → f (m + 2 ^ k) = f m := by
  intro m hm
  have hpos : 0 < 2 ^ k := Nat.two_pow_pos k
  have hNle : N ≤ N * 2 ^ k := Nat.le_mul_of_pos_right N hpos
  have hn : 2 ^ (k - 1) ≤ m + N * 2 ^ k := by omega
  have hTn : T (m + N * 2 ^ k) ≤ k := hT _ (by omega)
  have hmod₁ : m % 2 ^ k = (m + N * 2 ^ k) % 2 ^ k := by
    rw [Nat.add_mul_mod_self_right]
  have hmod₂ : (m + 2 ^ k) % 2 ^ k = (m + N * 2 ^ k) % 2 ^ k := by
    rw [Nat.add_mod_right, Nat.add_mul_mod_self_right]
  have e₁ := (computes_eq_of_mod_two_pow_of_run_le hM hm hn hmod₁ hTn).2
  have e₂ := (computes_eq_of_mod_two_pow_of_run_le hM (by omega) hn hmod₂ hTn).2
  exact e₂.trans e₁.symm

/-- For every `k ≤ 13`, every machine computing `center` takes more than `k` steps on infinitely
many inputs, without Problem 1. -/
theorem time_unbounded_le_thirteen {M : Machine} {T : Nat → Nat} (hM : Computes M center T)
    {k : Nat} (hk : k ≤ 13) (N : Nat) : ∃ n, N ≤ n ∧ k + 1 ≤ T n := by
  refine Classical.byContradiction fun hno => ?_
  have hT : ∀ n, N ≤ n → T n ≤ k := fun n hn =>
    Nat.le_of_not_lt fun hlt => hno ⟨n, hn, hlt⟩
  have hper := period_of_eventually_time_le hM hT
  have hwin : 16359 ≤ 2 ^ (k - 1) + 2 ^ k :=
    Rule30FactorWindow.transient_add_period_ge (2 ^ (k - 1)) (2 ^ k) (Nat.two_pow_pos k)
      fun t ht => hper t ht
  have h1 : 2 ^ (k - 1) ≤ 2 ^ 12 := Nat.pow_le_pow_right (by decide) (by omega)
  have h2 : 2 ^ k ≤ 2 ^ 13 := Nat.pow_le_pow_right (by decide) hk
  have e12 : (2 : Nat) ^ 12 = 4096 := rfl
  have e13 : (2 : Nat) ^ 13 = 8192 := rfl
  omega
```

We checked it with your sections 1 and 2 copied verbatim, against the kit's core on Lean 4.35.0. It builds in under 2 s, and both theorems use only `propext`, `Classical.choice` and `Quot.sound`. We have not built it inside this PR. It sits naturally beside your `diagonal_time_unbounded`, which does the same for the left diagonals through `D_period_unbounded`. You are welcome to fold it into `Rule30Problem3Bounds`. Or tell us if you would rather we open it separately.

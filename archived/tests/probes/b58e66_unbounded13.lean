import Ruliology.CellularAutomata.Rule30Problem3
import Ruliology.CellularAutomata.Rule30FactorWindow

/-!
# Local's check of one remark on R30-20261031-b58e66 (L1254)

Sections 1 and 2 are copied verbatim from G.P.J.W. Quint and Gemini's submission R30-20261031-b58e66
(kit PR #68, `Rule30Problem3Bounds`), down to `computes_eq_of_mod_two_pow_of_run_le`. Only the last two
theorems are new.

Their `evPer_two_pow_of_eventually_time_le` gives an eventual period `2 ^ k` from `max N (2 ^ (k - 1))`.
The class collapse gives more. One input with time at most `k` fixes the answer on its whole residue
class mod `2 ^ k` above `2 ^ (k - 1)`. So if the time is at most `k` from some `N` on, the answer has
period `2 ^ k` from `2 ^ (k - 1)` itself (`period_of_eventually_time_le`). The transient is then
`2 ^ (k - 1)` whatever `N` is. With the kit's `Rule30FactorWindow.transient_add_period_ge`
(`T + P ≥ 16359`), this excludes every `k ≤ 13` without assuming Problem 1
(`time_unbounded_le_thirteen`).
-/

namespace B58Check

open Ruliology.CellularAutomata
open Rule30Prize Rule30Problem3

/-! ### 1. Head-cone and prefix locality of `Machine.run` (b58e66, verbatim) -/

theorem move_apply_le_succ (d : Move) (h : Int) : d.apply h ≤ h + 1 := by
  cases d <;> simp [Move.apply] <;> omega

theorem step_congr_below {M : Machine} {c₁ c₂ : Cfg M} {B : Int}
    (hs : c₁.state = c₂.state) (hh : c₁.head = c₂.head) (hhead : c₁.head < B)
    (ht : ∀ i : Int, i < B → c₁.tape i = c₂.tape i) :
    (∃ b, c₁.step = .inl b ∧ c₂.step = .inl b) ∨
      ∃ c₁' c₂', c₁.step = .inr c₁' ∧ c₂.step = .inr c₂' ∧
        c₁'.state = c₂'.state ∧ c₁'.head = c₂'.head ∧ c₁'.head ≤ c₁.head + 1 ∧
        (∀ i : Int, i < B → c₁'.tape i = c₂'.tape i) := by
  have hread : c₁.tape c₁.head = c₂.tape c₂.head := by
    rw [← hh]
    exact ht c₁.head hhead
  unfold Cfg.step
  rw [hs, hread]
  cases hδ : M.δ c₂.state (c₂.tape c₂.head) with
  | inl b => exact Or.inl ⟨b, rfl, rfl⟩
  | inr val =>
    obtain ⟨p, a, d⟩ := val
    refine Or.inr ⟨_, _, rfl, rfl, rfl, by rw [hh], move_apply_le_succ d c₁.head, fun i hi => ?_⟩
    dsimp only
    rw [hh]
    by_cases hih : i = c₂.head
    · simp [hih]
    · simp [hih, ht i hi]

theorem run_add_congr_below {M : Machine} (m n : Nat) :
    ∀ (k s : Nat) {c₁ c₂ : Cfg M},
      M.run m s = .inr c₁ → M.run n s = .inr c₂ →
      c₁.state = c₂.state → c₁.head = c₂.head →
      (∀ i : Int, i < c₁.head + (k : Int) → c₁.tape i = c₂.tape i) →
      (∃ b, M.run m (s + k) = .inl b ∧ M.run n (s + k) = .inl b) ∨
        ∃ c₁' c₂', M.run m (s + k) = .inr c₁' ∧ M.run n (s + k) = .inr c₂' ∧
          c₁'.state = c₂'.state ∧ c₁'.head = c₂'.head
  | 0, s, c₁, c₂, hm, hn, hs, hh, _ => Or.inr ⟨c₁, c₂, hm, hn, hs, hh⟩
  | k + 1, s, c₁, c₂, hm, hn, hs, hh, ht => by
    have hstep := step_congr_below (B := c₁.head + ((k + 1 : Nat) : Int)) hs hh (by omega) ht
    rcases hstep with ⟨b, hb₁, hb₂⟩ | ⟨c₁', c₂', hc₁', hc₂', hs', hh', hle, ht'⟩
    · left
      have hm1 : M.run m (s + 1) = .inl b := by simp [Machine.run, hm, hb₁]
      have hn1 : M.run n (s + 1) = .inl b := by simp [Machine.run, hn, hb₂]
      refine ⟨b, ?_, ?_⟩
      · have := Machine.run_add hm1 k
        rwa [show s + 1 + k = s + (k + 1) by omega] at this
      · have := Machine.run_add hn1 k
        rwa [show s + 1 + k = s + (k + 1) by omega] at this
    · have hm1 : M.run m (s + 1) = .inr c₁' := by simp [Machine.run, hm, hc₁']
      have hn1 : M.run n (s + 1) = .inr c₂' := by simp [Machine.run, hn, hc₂']
      have ih := run_add_congr_below m n k (s + 1) hm1 hn1 hs' hh' (fun i hi => ht' i (by omega))
      rwa [show s + 1 + k = s + (k + 1) by omega] at ih

theorem init_tape_neg (M : Machine) (n : Nat) {i : Int} (hi : i < 0) :
    (M.init n).tape i = ⟨0, by omega⟩ := by
  simp only [Machine.init]
  rw [ite_eq_right (fun h => by omega)]

theorem run_eq_of_init_eq_lt {M : Machine} {m n t : Nat}
    (htape : ∀ i : Int, 0 ≤ i → i < (t : Int) → (M.init m).tape i = (M.init n).tape i)
    (b : Bool) : M.run m t = .inl b ↔ M.run n t = .inl b := by
  have hcongr := run_add_congr_below (M := M) m n t 0 (c₁ := M.init m) (c₂ := M.init n)
    rfl rfl rfl rfl (fun i hi => by
      have h0 : (M.init m).head = 0 := rfl
      rw [h0, Int.zero_add] at hi
      by_cases hneg : i < 0
      · rw [init_tape_neg M m hneg, init_tape_neg M n hneg]
      · exact htape i (by omega) hi)
  rw [Nat.zero_add] at hcongr
  rcases hcongr with ⟨b', hb₁, hb₂⟩ | ⟨c₁', c₂', hc₁', hc₂', _, _⟩
  · rw [hb₁, hb₂]
  · rw [hc₁', hc₂']
    simp

/-! ### 2. 2-adic tape congruence and transient elimination (b58e66, verbatim) -/

theorem testBit_eq_of_mod_two_pow_eq {m n k j : Nat} (hj : j < k)
    (hmod : m % 2 ^ k = n % 2 ^ k) : m.testBit j = n.testBit j := by
  have h1 := Nat.testBit_mod_two_pow m k j
  have h2 := Nat.testBit_mod_two_pow n k j
  rw [hmod] at h1
  rw [decide_eq_true hj, Bool.true_and] at h1 h2
  exact h1.symm.trans h2

theorem init_tape_eq_of_mod_two_pow_eq (M : Machine) {m n k : Nat}
    (hm : 2 ^ (k - 1) ≤ m) (hn : 2 ^ (k - 1) ≤ n) (hmod : m % 2 ^ k = n % 2 ^ k) :
    ∀ i : Int, 0 ≤ i → i < (k : Int) → (M.init m).tape i = (M.init n).tape i := by
  intro i hi0 hik
  have hlt : i.toNat < k := by omega
  have hle : i.toNat ≤ k - 1 := by omega
  have hpow : 2 ^ i.toNat ≤ 2 ^ (k - 1) := Nat.pow_le_pow_right (by decide) hle
  have hm_cond : 0 ≤ i ∧ 2 ^ i.toNat ≤ m := ⟨hi0, Nat.le_trans hpow hm⟩
  have hn_cond : 0 ≤ i ∧ 2 ^ i.toNat ≤ n := ⟨hi0, Nat.le_trans hpow hn⟩
  simp only [Machine.init]
  rw [ite_eq_left_of_eq_true _ _ (eq_true hm_cond), ite_eq_left_of_eq_true _ _ (eq_true hn_cond),
    testBit_eq_of_mod_two_pow_eq hlt hmod]

theorem run_inl_unique {M : Machine} {n t s : Nat} {b₁ b₂ : Bool}
    (h₁ : M.run n t = .inl b₁) (h₂ : M.run n s = .inl b₂) : b₁ = b₂ := by
  have e₁ := Machine.run_add h₁ s
  have e₂ := Machine.run_add h₂ t
  rw [Nat.add_comm] at e₂
  have := e₁.symm.trans e₂
  injection this

theorem computes_eq_of_mod_two_pow_of_run_le {M : Machine} {f : Nat → Bool} {T : Nat → Nat}
    (hM : Computes M f T) {m n k : Nat} (hm : 2 ^ (k - 1) ≤ m) (hn : 2 ^ (k - 1) ≤ n)
    (hmod : m % 2 ^ k = n % 2 ^ k) (hT : T n ≤ k) :
    M.run m k = .inl (f n) ∧ f m = f n := by
  have hrun_n : M.run n k = .inl (f n) := by
    have := Machine.run_add (hM n) (k - T n)
    rwa [Nat.add_sub_cancel' hT] at this
  have hrun_m : M.run m k = .inl (f n) :=
    (run_eq_of_init_eq_lt (init_tape_eq_of_mod_two_pow_eq M hm hn hmod) (f n)).mpr hrun_n
  exact ⟨hrun_m, (run_inl_unique hrun_m (hM m)).symm⟩

/-! ### 3. New: the transient does not depend on `N`, and `k ≤ 13` is excluded outright -/

/-- If `M` computes `f` and takes at most `k` steps from `N` on, then `f` has period `2 ^ k` from
`2 ^ (k - 1)` on, whatever `N` is. -/
theorem period_of_eventually_time_le {M : Machine} {f : Nat → Bool} {T : Nat → Nat}
    (hM : Computes M f T) {k N : Nat} (hT : ∀ n, N ≤ n → T n ≤ k) :
    ∀ m, 2 ^ (k - 1) ≤ m → f (m + 2 ^ k) = f m := by
  intro m hm
  have hpos : 0 < 2 ^ k := Nat.two_pow_pos k
  -- a representative of the class of `m` beyond `N`
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

/-- **Unconditional for `k ≤ 13`:** every machine computing `center` takes more than `k` steps on
infinitely many inputs. b58e66's `time_unbounded_of_problem1` assumes Problem 1 for this. -/
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

end B58Check

#print axioms B58Check.period_of_eventually_time_le
#print axioms B58Check.time_unbounded_le_thirteen

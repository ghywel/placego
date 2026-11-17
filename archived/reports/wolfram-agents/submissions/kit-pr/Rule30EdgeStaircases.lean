module

public import Ruliology.CellularAutomata.Rule30Prize
public import Ruliology.CellularAutomata.Rule30FrozenRuler
public import Ruliology.CellularAutomata.Rule30RightPeriods

/-!
# Rule 30: staircases near the single cell's right edge end; the rain rows keep a two-step patch

A *staircase* is a maximal alternating stretch of a row, of length at least `3`.

* `interior_kept`, `front_step`: in any row of the single cell's picture, an interior cell of an
  alternating stretch keeps its color, and the front of a maximal stretch is eaten one cell per row.
  A living staircase therefore keeps its front at a fixed distance `W` from the advancing edge.
* `staircase_ends`, `staircase_ends_pow`: **every staircase near the edge ends.** If the front is
  `W ≥ 2` cells from the single cell's right edge and the right diagonal `W + 1` has period `H`
  (`Rule30RightPeriods.Per`), the staircase does not live through any multiple of `H` (at such times
  the cells at distances `1 .. W + 1` are white). With `H = 2 ^ (W + 1)` it dies within `2 ^ (W + 1)`
  rows.
* `period_two_iff`, `no_fixed_point`: **the rain pair.** An odd edge code (`Rule30FrozenRuler.T`,
  bit `0` black) satisfies `T (T c) = c` exactly when it is `rainA = 1010…` (`-1/3`) or
  `rainB = 11010…` (`1/3`); none is fixed.
* `agree_rain_eternal`, `rain_row_eternal`: a finite row whose `m` edge cells agree with `rainA`
  keeps them in that two-step rhythm for ever; the rain row `(0 1)^n` keeps a moving `2 n`-cell
  patch at its right edge, the first `2 n` bits of `rainA` and `rainB` in turn (not a spatially
  alternating word at odd times, since `rainB` begins `1 1`).

Contributed by Gareth Herbert with Claude (Anthropic) and GPT (OpenAI). Nothing here concerns the
center column.
-/

@[expose] public section

namespace Ruliology.CellularAutomata.Rule30EdgeStaircases

open Rule30Jen Rule30Realization Rule30FrozenRuler
open Rule30Diagonals (R R_periodic)
open Rule30RightPeriods (Per per_mono_all R_init)

/-! ### Part 1: staircases in the single cell's picture end -/

/-- Three cells from `f` at time `t` alternate. -/
def Alt3 (t : Nat) (f : Int) : Prop := cell t f ≠ cell t (f + 1) ∧ cell t (f + 1) ≠ cell t (f + 2)

/-- `f` is the front (left end) of a maximal alternating stretch of length at least `3`. -/
def Front (t : Nat) (f : Int) : Prop := cell t (f - 1) = cell t f ∧ Alt3 t f

theorem cell_succ (t : Nat) (p : Int) :
    cell (t + 1) p = rule (cell t (p - 1)) (cell t p) (cell t (p + 1)) := rfl

/-- Interior cells of an alternating stretch keep their colors. -/
theorem interior_kept (t : Nat) (p : Int) (h1 : cell t (p - 1) ≠ cell t p)
    (h2 : cell t p ≠ cell t (p + 1)) : cell (t + 1) p = cell t p := by
  rw [cell_succ]
  revert h1 h2
  cases cell t (p - 1) <;> cases cell t p <;> cases cell t (p + 1) <;> decide

/-- The front is eaten one cell per row: after one step, the old front and the next cell agree. -/
theorem front_step (t : Nat) (f : Int) (h : Front t f) :
    cell (t + 1) f = cell (t + 1) (f + 1) := by
  obtain ⟨hl, ha, hb⟩ := h
  rw [cell_succ t f, cell_succ t (f + 1)]
  have e1 : f + 1 - 1 = f := by omega
  rw [e1, hl, show f + 1 + 1 = f + 2 by omega]
  revert ha hb
  cases cell t f <;> cases cell t (f + 1) <;> cases cell t (f + 2) <;> decide

/-- The stretch lives through `t`, from `t₀` with front `a`, its front moving one cell per row. -/
def Lives (t₀ : Nat) (a : Int) (t : Nat) : Prop :=
  ∀ t', t₀ ≤ t' → t' ≤ t → Alt3 t' (a + ((t' - t₀ : Nat) : Int))

/-- A living stretch's front stays at its distance from the edge: at time `t ≥ t₀` its front is at
`t - W` when `t₀ - a = W`. -/
theorem front_distance (t₀ t : Nat) (a : Int) (W : Nat) (hW : (t₀ : Int) - a = W) (ht : t₀ ≤ t) :
    a + ((t - t₀ : Nat) : Int) = (t : Int) - W := by
  have : ((t - t₀ : Nat) : Int) = (t : Int) - t₀ := by omega
  rw [this]; omega

/-- At a time that is a multiple of a period of diagonal `W + 1`, the cells at distances
`1 .. W + 1` behind the right edge are white. -/
theorem white_behind_edge {W H : Nat} (hP : Per (W + 1) H) (n : Nat) (j : Nat) (hj1 : 1 ≤ j)
    (hj : j ≤ W + 1) : cell (H * n) ((H * n : Nat) - (j : Int)) = false := by
  have hPj : Per j H := by
    rcases Nat.lt_or_eq_of_le hj with h | h
    · exact per_mono_all hP j (by omega)
    · rw [h]; exact hP
  have h1 := hPj.at_mul n
  rw [R_init hj1] at h1
  exact h1

/-- **Every staircase ends.** A staircase living from `t₀` with front `a` at distance
`W = t₀ - a ≥ 2` from the right edge does not live through any multiple `H n ≥ t₀` of a period `H`
of the right diagonal `W + 1`. -/
theorem staircase_ends (t₀ : Nat) (a : Int) (W H : Nat) (hW2 : 2 ≤ W)
    (hW : (t₀ : Int) - a = W) (hP : Per (W + 1) H) (n : Nat) (hn : t₀ ≤ H * n) :
    ¬ Lives t₀ a (H * n) := by
  intro hl
  have h := hl (H * n) hn (Nat.le_refl _)
  rw [front_distance t₀ (H * n) a W hW hn] at h
  have c0 := white_behind_edge hP n W (by omega) (by omega)
  have c1 := white_behind_edge hP n (W - 1) (by omega) (by omega)
  have e : (((H * n : Nat) : Int) - (W : Int)) + 1 = ((H * n : Nat) : Int) - ((W - 1 : Nat) : Int) := by
    omega
  apply h.1
  rw [e, c0, c1]

/-- With the kit's `R_periodic`: every staircase whose front is `W ≥ 2` cells from the right edge
dies by the first multiple of `2 ^ (W + 1)` after it is seen. -/
theorem staircase_ends_pow (t₀ : Nat) (a : Int) (W : Nat) (hW2 : 2 ≤ W)
    (hW : (t₀ : Int) - a = W) (n : Nat) (hn : t₀ ≤ 2 ^ (W + 1) * n) :
    ¬ Lives t₀ a (2 ^ (W + 1) * n) :=
  staircase_ends t₀ a W (2 ^ (W + 1)) hW2 hW (R_periodic (W + 1)) n hn

/-! ### The rain pair -/

/-- `1 0 1 0 …`: the 2-adic number `-1/3`, an edge emitting a lone white cell at every other step. -/
def rainA : Nat → Bool := fun k => k % 2 == 0

/-- `1 1 0 1 0 …`: the 2-adic number `1/3`. -/
def rainB : Nat → Bool := fun k => k == 0 || k % 2 == 1

theorem T_rainA : T rainA = rainB := by
  funext k
  match k with
  | 0 => rfl
  | 1 => rfl
  | j + 2 =>
    simp only [T, rainA, rainB]
    rcases Nat.mod_two_eq_zero_or_one j with h | h
    · have h1 : (j + 1) % 2 = 1 := by omega
      have h2 : (j + 2) % 2 = 0 := by omega
      simp [h, h1, h2]
    · have h1 : (j + 1) % 2 = 0 := by omega
      have h2 : (j + 2) % 2 = 1 := by omega
      simp [h, h1, h2]

theorem T_rainB : T rainB = rainA := by
  funext k
  match k with
  | 0 => rfl
  | 1 => rfl
  | 2 => rfl
  | j + 3 =>
    show xor (rainB (j + 3)) (rainB (j + 2) || rainB (j + 1)) = rainA (j + 3)
    simp only [rainA, rainB]
    rcases Nat.mod_two_eq_zero_or_one j with h | h
    · have h1 : (j + 1) % 2 = 1 := by omega
      have h2 : (j + 2) % 2 = 0 := by omega
      have h3 : (j + 3) % 2 = 1 := by omega
      simp [h1, h2, h3]
    · have h1 : (j + 1) % 2 = 0 := by omega
      have h2 : (j + 2) % 2 = 1 := by omega
      have h3 : (j + 3) % 2 = 0 := by omega
      simp [h1, h2, h3]

theorem rainA_ne_rainB : rainA ≠ rainB := by
  intro h
  have := congrFun h 1
  simp [rainA, rainB] at this

/-- No edge code with bit `0` black is fixed by `T`: bit `1` always flips. -/
theorem no_fixed_point (c : Nat → Bool) (h0 : c 0 = true) : T c ≠ c := by
  intro h
  have := congrFun h 1
  simp [T, h0] at this

/-- The two codes of a 2-cycle differ at every bit from `1` on, and each alternates from bit `1`. -/
theorem cycle_bits (c : Nat → Bool) (h0 : c 0 = true) (h2 : T (T c) = c) :
    ∀ k, 1 ≤ k → T c k ≠ c k ∧ T c (k + 1) ≠ c (k + 1) ∧ c k ≠ c (k + 1) := by
  let d := T c
  have hd : d = T c := rfl
  have hc : ∀ k, T d k = c k := fun k => congrFun h2 k
  have dk0 : d 0 = true := by simp [hd, T, h0]
  -- the step relations
  have rel_d : ∀ k, d (k + 2) = xor (c (k + 2)) (c (k + 1) || c k) := fun k => rfl
  have rel_c : ∀ k, c (k + 2) = xor (d (k + 2)) (d (k + 1) || d k) := fun k => (hc (k + 2)).symm
  have or_eq : ∀ k, (c (k + 1) || c k) = (d (k + 1) || d k) := by
    intro k
    have a := rel_d k; have b := rel_c k
    revert a b
    cases c (k + 2) <;> cases d (k + 2) <;> cases (c (k + 1) || c k) <;>
      cases (d (k + 1) || d k) <;> simp
  have d1 : d 1 ≠ c 1 := by
    show xor (c 1) (c 0) ≠ c 1
    rw [h0]; cases c 1 <;> simp
  have d2 : d 2 ≠ c 2 := by
    have := rel_d 0
    rw [h0] at this
    simp at this
    rw [this]; cases c 2 <;> simp
  -- induction on k ≥ 1
  have step : ∀ k, d (k + 1) ≠ c (k + 1) → d (k + 2) ≠ c (k + 2) →
      c (k + 1) ≠ c (k + 2) ∧ d (k + 3) ≠ c (k + 3) := by
    intro k ha hb
    have ho := or_eq (k + 1)
    have hne : c (k + 2) ≠ c (k + 1) := by
      intro heq
      revert ha hb ho heq
      cases c (k + 1) <;> cases c (k + 2) <;> cases d (k + 1) <;> cases d (k + 2) <;> simp
    have hor : (c (k + 2) || c (k + 1)) = true := by
      revert hne; cases c (k + 1) <;> cases c (k + 2) <;> simp
    refine ⟨fun h => hne h.symm, ?_⟩
    have := rel_d (k + 1)
    rw [hor] at this
    rw [this]; cases c (k + 3) <;> simp
  have main : ∀ k, d (k + 1) ≠ c (k + 1) ∧ d (k + 2) ≠ c (k + 2) := by
    intro k
    induction k with
    | zero => exact ⟨d1, d2⟩
    | succ n ih => exact ⟨ih.2, (step n ih.1 ih.2).2⟩
  intro k hk
  obtain ⟨n, rfl⟩ : ∃ n, k = n + 1 := ⟨k - 1, by omega⟩
  exact ⟨(main n).1, (main n).2, (step n (main n).1 (main n).2).1⟩

/-- **The rain pair.** An edge code with bit `0` black is a point of period dividing `2` of the edge
map exactly when it is `rainA` (`-1/3`) or `rainB` (`1/3`). -/
theorem period_two_iff (c : Nat → Bool) (h0 : c 0 = true) :
    T (T c) = c ↔ (c = rainA ∨ c = rainB) := by
  constructor
  · intro h2
    have hb := cycle_bits c h0 h2
    -- c alternates from bit 1 on
    have alt : ∀ n, c (n + 1) = (if n % 2 = 0 then c 1 else !c 1) := by
      intro n
      induction n with
      | zero => simp
      | succ m ih =>
        have := (hb (m + 1) (by omega)).2.2
        rw [ih] at this
        split at this <;> rename_i hm
        · have : c (m + 2) = !c 1 := by revert this; cases c 1 <;> cases c (m + 2) <;> simp
          rw [show m + 1 + 1 = m + 2 by omega, this]
          simp [show (m + 1) % 2 ≠ 0 by omega]
        · have : c (m + 2) = c 1 := by revert this; cases c 1 <;> cases c (m + 2) <;> simp
          rw [show m + 1 + 1 = m + 2 by omega, this]
          simp [show (m + 1) % 2 = 0 by omega]
    cases h1 : c 1
    · left; funext k
      match k with
      | 0 => simp [rainA, h0]
      | n + 1 =>
        rw [alt n, h1]
        simp only [rainA]
        split <;> rename_i hn <;> simp <;> omega
    · right; funext k
      match k with
      | 0 => simp [rainB, h0]
      | n + 1 =>
        rw [alt n, h1]
        simp only [rainB]
        split <;> rename_i hn <;> simp <;> omega
  · rintro (rfl | rfl)
    · rw [T_rainA, T_rainB]
    · rw [T_rainB, T_rainA]

/-! ### Rows that keep the rain for ever -/

theorem iter_rainA : ∀ t, iter t rainA = (if t % 2 = 0 then rainA else rainB)
  | 0 => rfl
  | t + 1 => by
    show T (iter t rainA) = _
    rw [iter_rainA t]
    by_cases h : t % 2 = 0
    · simp [h, T_rainA, show (t + 1) % 2 ≠ 0 by omega]
    · simp [h, T_rainB, show (t + 1) % 2 = 0 by omega]

/-- A finite row whose `m` edge cells agree with `rainA` keeps them `rainA` at even times and
`rainB` at odd times, for ever. -/
theorem agree_rain_eternal (x : Int → Bool) (e : Int) (he : x e = true)
    (hr : ∀ p, e < p → x p = false) (m : Nat) (hag : AgreeBelow m (code x e) rainA) (t : Nat) :
    AgreeBelow m (code (evol x t) (e + t)) (if t % 2 = 0 then rainA else rainB) := by
  rw [(edge_evol x e he hr t).2.2, ← iter_rainA t]
  exact iter_agree hag t

/-- The rain row `(0 1)^n`: black exactly at the cells `-2 i`, `0 ≤ i < n`. -/
def rainRow (n : Nat) (p : Int) : Bool := decide (p ≤ 0 ∧ -(2 * (n : Int)) < p ∧ p % 2 = 0)

theorem rainRow_code (n : Nat) : AgreeBelow (2 * n) (code (rainRow n) 0) rainA := by
  intro i hi
  simp only [code, rainRow, rainA]
  rcases Nat.mod_two_eq_zero_or_one i with h | h
  · simp [h]; omega
  · simp [h]; omega

/-- **The rain row keeps a two-step patch at its right edge for ever.** For every `n ≥ 1` and every time
`t`, the rightmost black cell of the row `(0 1)^n` after `t` steps is at `t`, and the `2 n` cells
behind it read `rainA` at even times and `rainB` at odd times. -/
theorem rain_row_eternal (n : Nat) (hn : 1 ≤ n) (t : Nat) :
    evol (rainRow n) t t = true ∧ (∀ p, (t : Int) < p → evol (rainRow n) t p = false) ∧
    AgreeBelow (2 * n) (code (evol (rainRow n) t) t) (if t % 2 = 0 then rainA else rainB) := by
  have he : rainRow n 0 = true := by simp [rainRow]; omega
  have hr : ∀ p, (0 : Int) < p → rainRow n p = false := by
    intro p hp; simp [rainRow]; omega
  have h := edge_evol (rainRow n) 0 he hr t
  simp only [Int.zero_add] at h
  refine ⟨h.1, h.2.1, ?_⟩
  have := agree_rain_eternal (rainRow n) 0 he hr (2 * n) (rainRow_code n) t
  simpa using this

end Ruliology.CellularAutomata.Rule30EdgeStaircases

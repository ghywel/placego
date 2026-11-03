import Ruliology.CellularAutomata.Rule30GateClocks

namespace Ruliology.CellularAutomata.Rule30ClosingLaw

open Rule30RecordCharge Rule30DifferenceOrder Rule30GateClocks

/-- A gate whose derivative in its newer input is `s` or `!s`: its quadratic coefficient is `1`. -/
def Quadratic (g : Bool → Bool → Bool) : Prop := deriv g true ≠ deriv g false

/-- For a quadratic gate, past the first difference the derivative behaves like `s` itself. -/
theorem difs_deriv {g : Bool → Bool → Bool} (hq : Quadratic g) (s : Nat → Bool) (k : Nat) :
    difs (k + 1) (fun t => deriv g (s t)) = difs (k + 1) s := by
  unfold Quadratic at hq
  cases h1 : deriv g true <;> cases h0 : deriv g false <;> rw [h1, h0] at hq
  · exact absurd rfl hq
  · have hc : (fun t => deriv g (s t)) = fun t => xor ((fun _ => true) t) (s t) := by
      funext u; cases hu : s u <;> simp [h0, h1]
    rw [hc, difs_xor, difs_const]
    funext t; cases difs (k + 1) s t <;> rfl
  · have hc : (fun t => deriv g (s t)) = s := by
      funext u; cases hu : s u <;> simp [h0, h1]
    rw [hc]
  · exact absurd rfl hq

/-- Past the `M`-th difference, `h`'s differences are exactly `s`'s, for a quadratic gate. -/
theorem difs_past_gate {g : Bool → Bool → Bool} {s b h : Nat → Bool} {v : Nat} (hq : Quadratic g)
    (hs : ∀ t, s (t + 2 ^ v) = s t) (hb : ∀ t, b (t + 2 ^ v) = !b t)
    (hh : ∀ t, h (t + 1) = xor (h t) (g (b t) (s t))) (k : Nat) :
    difs (k + 1 + 1 + 2 ^ v) h = difs (k + 1) s := by
  rw [difs_add, difs_two_pow, difs_succ' (k + 1), dif_shift_sum_gate hs hb hh, difs_deriv hq]

/-- The `(M + 1)`-th difference of `h` is the derivative itself. -/
theorem difs_M_succ_gate {g : Bool → Bool → Bool} {s b h : Nat → Bool} {v : Nat}
    (hs : ∀ t, s (t + 2 ^ v) = s t) (hb : ∀ t, b (t + 2 ^ v) = !b t)
    (hh : ∀ t, h (t + 1) = xor (h t) (g (b t) (s t))) :
    difs (1 + 2 ^ v) h = fun t => deriv g (s t) := by
  rw [difs_add, difs_two_pow]
  show dif (fun t => xor (h (t + 2 ^ v)) (h t)) = _
  exact dif_shift_sum_gate hs hb hh

theorem two_le_two_pow {v : Nat} (hv : 1 ≤ v) : 2 ≤ 2 ^ v := by
  obtain ⟨k, rfl⟩ : ∃ k, v = k + 1 := ⟨v - 1, by omega⟩
  rw [Nat.pow_succ]; have := Nat.one_le_two_pow (n := k); omega

/-- If `h` keeps the period `2 * M`, then `s` has positive order: a doubling is the only way to reach order `0`. -/
theorem order_pos_of_period {g : Bool → Bool → Bool} {s b h : Nat → Bool} {v : Nat} (hq : Quadratic g)
    (hv : 1 ≤ v) (hs : ∀ t, s (t + 2 ^ v) = s t) (hb : ∀ t, b (t + 2 ^ v) = !b t)
    (hh : ∀ t, h (t + 1) = xor (h t) (g (b t) (s t)))
    (hper : ∀ t, h (t + 2 * 2 ^ v) = h t) :
    1 ≤ order s (2 ^ v) := by
  have hM := two_le_two_pow hv
  have hvan : Vanish (2 * 2 ^ v) h := by
    intro t
    rw [← two_pow_succ' v, difs_two_pow, two_pow_succ' v]
    show xor (h (t + 2 * 2 ^ v)) (h t) = false
    rw [hper t]
    cases h t <;> rfl
  have hpast := difs_past_gate hq hs hb hh (2 ^ v - 2)
  rw [show 2 ^ v - 2 + 1 + 1 + 2 ^ v = 2 * 2 ^ v by omega,
    show 2 ^ v - 2 + 1 = 2 ^ v - 1 by omega] at hpast
  apply (le_order_iff (g := s) (L := 2 ^ v) (r := 1) (by omega) (by omega)).mpr
  intro t
  have := hvan t
  rw [hpast] at this
  exact this

/-- **The exact countdown.** For a quadratic gate, if `h` keeps the period `2 * M` and `s` is below the largest
order, the order drops by exactly one: `order h (2 M) + 1 = order s M`. -/
theorem order_countdown_exact {g : Bool → Bool → Bool} {s b h : Nat → Bool} {v : Nat} (hq : Quadratic g)
    (hv : 1 ≤ v) (hs : ∀ t, s (t + 2 ^ v) = s t) (hb : ∀ t, b (t + 2 ^ v) = !b t)
    (hh : ∀ t, h (t + 1) = xor (h t) (g (b t) (s t)))
    (hper : ∀ t, h (t + 2 * 2 ^ v) = h t) (hlt : order s (2 ^ v) + 1 < 2 ^ v) :
    order h (2 * 2 ^ v) + 1 = order s (2 ^ v) := by
  have hM := two_le_two_pow hv
  apply Nat.le_antisymm _ (order_countdown_gate hs hb hh)
  -- `h` does not vanish at `M + 1`, else `s` would vanish at `1` and have the largest order.
  have hr : order h (2 * 2 ^ v) ≤ 2 ^ v - 2 := by
    apply Nat.le_of_not_lt
    intro hgt
    have hvh := (le_order_iff (g := h) (L := 2 * 2 ^ v) (r := 2 ^ v - 1) (by omega) (by omega)).mp
      (by omega)
    have hpast := difs_past_gate hq hs hb hh 0
    have h1 : Vanish (2 ^ v - (2 ^ v - 1)) s := by
      intro t
      have := (hvh.mono (m := 0 + 1 + 1 + 2 ^ v) (by omega)) t
      rw [hpast] at this
      rw [show 2 ^ v - (2 ^ v - 1) = 0 + 1 by omega]
      exact this
    have := (le_order_iff (g := s) (L := 2 ^ v) (r := 2 ^ v - 1) (by omega) (by omega)).mpr h1
    omega
  rcases Nat.eq_zero_or_pos (order h (2 * 2 ^ v)) with h0 | hpos
  · rw [h0]; exact order_pos_of_period hq hv hs hb hh hper
  · have hvan := (le_order_iff (g := h) (L := 2 * 2 ^ v) (r := order h (2 * 2 ^ v)) hpos
      (order_le h _)).mp (Nat.le_refl _)
    have hpast := difs_past_gate hq hs hb hh (2 ^ v - order h (2 * 2 ^ v) - 2)
    rw [show 2 ^ v - order h (2 * 2 ^ v) - 2 + 1 + 1 + 2 ^ v = 2 * 2 ^ v - order h (2 * 2 ^ v) by omega,
      show 2 ^ v - order h (2 * 2 ^ v) - 2 + 1 = 2 ^ v - (order h (2 * 2 ^ v) + 1) by omega] at hpast
    apply (le_order_iff (g := s) (L := 2 ^ v) (r := order h (2 * 2 ^ v) + 1) (by omega) (by omega)).mpr
    intro t
    have := hvan t
    rw [hpast] at this
    exact this

/-! ### The closing law for prefix-doubling flags -/

/-- Column `i` keeps the prefix period of every later prefix. -/
theorem col_period (g : Nat → Bool → Bool → Bool) (x : Nat → Bool) {i k : Nat} (hik : i ≤ k) (t : Nat) :
    col g x i (t + 2 ^ prefixExp g x k) = col g x i t :=
  (prefix_period_iff g x k _).mpr (Nat.dvd_refl _) i hik t

theorem col_step' (g : Nat → Bool → Bool → Bool) (x : Nat → Bool) (k t : Nat) :
    col g x (k + 1 + 1) (t + 1) = xor (col g x (k + 1 + 1) t) (g (k + 1) (col g x (k + 1) t) (col g x k t)) := by
  rw [col_step g x (k + 1) t]
  rfl

/-- Along a doubling followed by `10` pairs, the exponent rises by one per pair and the order of the pair's first
column falls by exactly one per pair. -/
theorem closing_run (g : Nat → Bool → Bool → Bool) (x : Nat → Bool) (hq : ∀ j, Quadratic (g j)) {n m : Nat}
    (h1 : prefixExp g x (n + 1) = prefixExp g x n + 1)
    (hpair : ∀ i, i < m → prefixExp g x (n + 1 + 2 * i + 1) = prefixExp g x (n + 1 + 2 * i) + 1 ∧
      prefixExp g x (n + 1 + 2 * i + 1 + 1) = prefixExp g x (n + 1 + 2 * i + 1)) :
    ∀ i, i ≤ m → prefixExp g x (n + 1 + 2 * i) = prefixExp g x n + 1 + i ∧
      order (col g x (n + 1 + 2 * i)) (2 ^ prefixExp g x (n + 1 + 2 * i)) + i = 2 ^ prefixExp g x n - 1
  | 0, _ => by
    refine ⟨by simpa using h1, ?_⟩
    have hanti : ∀ t, col g x (n + 1) (t + 2 ^ prefixExp g x n) = !col g x (n + 1) t :=
      col_antiperiod g x h1
    have := order_of_antiperiod hanti
    simp only [Nat.mul_zero, Nat.add_zero]
    rw [h1, two_pow_succ', this]
  | i + 1, hi => by
    obtain ⟨hE, hR⟩ := closing_run g x hq h1 hpair i (by omega)
    obtain ⟨hd, hk⟩ := hpair i (by omega)
    have e2 : n + 1 + 2 * (i + 1) = n + 1 + 2 * i + 1 + 1 := by omega
    rw [e2]
    have hP : prefixExp g x (n + 1 + 2 * i + 1 + 1) = prefixExp g x (n + 1 + 2 * i) + 1 := by rw [hk, hd]
    refine ⟨by rw [hP, hE]; omega, ?_⟩
    have hv : 1 ≤ prefixExp g x (n + 1 + 2 * i) := by rw [hE]; omega
    have hs := col_period g x (Nat.le_refl (n + 1 + 2 * i))
    have hb := col_antiperiod g x hd
    have hh := col_step' g x (n + 1 + 2 * i)
    have hper : ∀ t, col g x (n + 1 + 2 * i + 1 + 1) (t + 2 * 2 ^ prefixExp g x (n + 1 + 2 * i)) =
        col g x (n + 1 + 2 * i + 1 + 1) t := by
      intro t
      have := col_period g x (Nat.le_refl (n + 1 + 2 * i + 1 + 1)) t
      rwa [hP, two_pow_succ'] at this
    have hlt : order (col g x (n + 1 + 2 * i)) (2 ^ prefixExp g x (n + 1 + 2 * i)) + 1 <
        2 ^ prefixExp g x (n + 1 + 2 * i) := by
      have h2 : 2 ^ prefixExp g x n < 2 ^ prefixExp g x (n + 1 + 2 * i) :=
        Nat.pow_lt_pow_right (by decide) (by rw [hE]; omega)
      have := Nat.one_le_two_pow (n := prefixExp g x n)
      omega
    have hc := order_countdown_exact (hq (n + 1 + 2 * i + 1)) hv hs hb hh hper hlt
    rw [hP, two_pow_succ']
    omega

/-- **The closing law.** After a doubling at prefix exponent `E` (period `q0 = 2 ^ E`), a run of `m` pairs `10` and a
doubling, `m + 1 ≤ q0`, and the next column doubles iff `m + 1 = q0`. For quadratic gates, including Rule 30's OR. -/
theorem closing_law (g : Nat → Bool → Bool → Bool) (x : Nat → Bool) (hq : ∀ j, Quadratic (g j)) {n m : Nat}
    (h1 : prefixExp g x (n + 1) = prefixExp g x n + 1)
    (hpair : ∀ i, i < m → prefixExp g x (n + 1 + 2 * i + 1) = prefixExp g x (n + 1 + 2 * i) + 1 ∧
      prefixExp g x (n + 1 + 2 * i + 1 + 1) = prefixExp g x (n + 1 + 2 * i + 1))
    (hlast : prefixExp g x (n + 1 + 2 * m + 1) = prefixExp g x (n + 1 + 2 * m) + 1) :
    m + 1 ≤ 2 ^ prefixExp g x n ∧
      (prefixExp g x (n + 1 + 2 * m + 1 + 1) = prefixExp g x (n + 1 + 2 * m + 1) + 1 ↔
        m + 1 = 2 ^ prefixExp g x n) := by
  obtain ⟨hE, hR⟩ := closing_run g x hq h1 hpair m (Nat.le_refl m)
  have hpos := Nat.one_le_two_pow (n := prefixExp g x n)
  refine ⟨by omega, ?_⟩
  have hv : 1 ≤ prefixExp g x (n + 1 + 2 * m) := by rw [hE]; omega
  have hs := col_period g x (Nat.le_refl (n + 1 + 2 * m))
  have hb := col_antiperiod g x hlast
  have hh := col_step' g x (n + 1 + 2 * m)
  constructor
  · intro hd
    have hanti : ∀ t, col g x (n + 1 + 2 * m + 1 + 1) (t + 2 * 2 ^ prefixExp g x (n + 1 + 2 * m)) =
        !col g x (n + 1 + 2 * m + 1 + 1) t := by
      intro t
      have := col_antiperiod g x hd t
      rwa [hlast, two_pow_succ'] at this
    have h0 := order_reset_before_gate hs hb hh hanti
    omega
  · intro heq
    rcases prefixExp_succ_cases g x (n + 1 + 2 * m + 1) with hk | hd
    · exfalso
      have hper : ∀ t, col g x (n + 1 + 2 * m + 1 + 1) (t + 2 * 2 ^ prefixExp g x (n + 1 + 2 * m)) =
          col g x (n + 1 + 2 * m + 1 + 1) t := by
        intro t
        have := col_period g x (Nat.le_refl (n + 1 + 2 * m + 1 + 1)) t
        rwa [hk, hlast, two_pow_succ'] at this
      have := order_pos_of_period (hq (n + 1 + 2 * m + 1)) hv hs hb hh hper
      omega
    · exact hd

/-- A closing length is one less than a power of two, and `1 (10)^2 1 1` never occurs: three is not a power of two. -/
theorem no_1101011 (g : Nat → Bool → Bool → Bool) (x : Nat → Bool) (hq : ∀ j, Quadratic (g j)) {n : Nat}
    (h1 : prefixExp g x (n + 1) = prefixExp g x n + 1)
    (hpair : ∀ i, i < 2 → prefixExp g x (n + 1 + 2 * i + 1) = prefixExp g x (n + 1 + 2 * i) + 1 ∧
      prefixExp g x (n + 1 + 2 * i + 1 + 1) = prefixExp g x (n + 1 + 2 * i + 1))
    (hlast : prefixExp g x (n + 1 + 2 * 2 + 1) = prefixExp g x (n + 1 + 2 * 2) + 1) :
    prefixExp g x (n + 1 + 2 * 2 + 1 + 1) = prefixExp g x (n + 1 + 2 * 2 + 1) := by
  have hc := closing_law g x hq h1 hpair hlast
  rcases prefixExp_succ_cases g x (n + 1 + 2 * 2 + 1) with hk | hd
  · exact hk
  · exfalso
    have h3 := hc.2.mp hd
    rcases Nat.lt_or_ge (prefixExp g x n) 2 with hE | hE
    · have h01 : prefixExp g x n = 0 ∨ prefixExp g x n = 1 := by omega
      rcases h01 with h | h <;> rw [h] at h3 <;> exact absurd h3 (by decide)
    · have h4 : 2 ^ 2 ≤ 2 ^ prefixExp g x n := Nat.pow_le_pow_right (by decide) hE
      have : (2 : Nat) ^ 2 = 4 := rfl
      omega

/-- The OR gate is quadratic. -/
theorem quadratic_or : Quadratic (fun b s => b || s) := by
  unfold Quadratic deriv; decide

/-- No three consecutive doublings once the prefix period is at least `2` (the `m = 0` case). -/
theorem no_three_at (g : Nat → Bool → Bool → Bool) (x : Nat → Bool) (hq : ∀ j, Quadratic (g j)) {p : Nat}
    (hE : 1 ≤ prefixExp g x p) :
    prefixExp g x (p + 1) = prefixExp g x p ∨ prefixExp g x (p + 2) = prefixExp g x (p + 1) ∨
      prefixExp g x (p + 3) = prefixExp g x (p + 2) := by
  rcases prefixExp_succ_cases g x p with h0 | h1
  · exact Or.inl h0
  rcases prefixExp_succ_cases g x (p + 1) with h0' | h2
  · exact Or.inr (Or.inl h0')
  have hc := closing_law g x hq (n := p) (m := 0) h1 (fun i hi => absurd hi (Nat.not_lt_zero i))
    (by rw [show p + 1 + 2 * 0 + 1 = p + 1 + 1 by omega, show p + 1 + 2 * 0 = p + 1 by omega]; exact h2)
  rw [show p + 1 + 2 * 0 + 1 + 1 = p + 3 by omega, show p + 1 + 2 * 0 + 1 = p + 2 by omega] at hc
  have hpow : 1 < 2 ^ prefixExp g x p := Nat.one_lt_two_pow (by omega)
  rcases prefixExp_succ_cases g x (p + 2) with h0'' | h3
  · exact Or.inr (Or.inr h0'')
  · have := hc.2.mp h3; omega

/-- `11011` needs prefix period `2` before it (the `m = 1` case). -/
theorem no_11011_at (g : Nat → Bool → Bool → Bool) (x : Nat → Bool) (hq : ∀ j, Quadratic (g j)) {p : Nat}
    (hE : 2 ≤ prefixExp g x p) :
    prefixExp g x (p + 1) = prefixExp g x p ∨ prefixExp g x (p + 2) = prefixExp g x (p + 1) ∨
      prefixExp g x (p + 3) = prefixExp g x (p + 2) + 1 ∨ prefixExp g x (p + 4) = prefixExp g x (p + 3) ∨
      prefixExp g x (p + 5) = prefixExp g x (p + 4) := by
  rcases prefixExp_succ_cases g x p with h0 | h1
  · exact Or.inl h0
  rcases prefixExp_succ_cases g x (p + 1) with h0 | h2
  · exact Or.inr (Or.inl h0)
  rcases prefixExp_succ_cases g x (p + 2) with h3 | h3'
  · rcases prefixExp_succ_cases g x (p + 3) with h0 | h4
    · exact Or.inr (Or.inr (Or.inr (Or.inl h0)))
    have hpair : ∀ i, i < 1 → prefixExp g x (p + 1 + 2 * i + 1) = prefixExp g x (p + 1 + 2 * i) + 1 ∧
        prefixExp g x (p + 1 + 2 * i + 1 + 1) = prefixExp g x (p + 1 + 2 * i + 1) := by
      intro i hi
      have hi0 : i = 0 := by omega
      subst hi0
      exact ⟨h2, h3⟩
    have hc := closing_law g x hq (n := p) (m := 1) h1 hpair
      (by rw [show p + 1 + 2 * 1 + 1 = p + 3 + 1 by omega, show p + 1 + 2 * 1 = p + 3 by omega]; exact h4)
    rw [show p + 1 + 2 * 1 + 1 + 1 = p + 5 by omega, show p + 1 + 2 * 1 + 1 = p + 4 by omega] at hc
    have hpow : 2 ^ 2 ≤ 2 ^ prefixExp g x p := Nat.pow_le_pow_right (by decide) hE
    have h4' : (2 : Nat) ^ 2 = 4 := rfl
    rcases prefixExp_succ_cases g x (p + 4) with h0 | h5
    · exact Or.inr (Or.inr (Or.inr (Or.inr h0)))
    · have := hc.2.mp h5; omega
  · exact Or.inr (Or.inr (Or.inl h3'))

/-- **Five letters, at most three doublings** (GC2007's bound). Once the prefix period is at least `4`, any five
consecutive columns raise the exponent by at most `3`, for every quadratic gate family. -/
theorem five_letter (g : Nat → Bool → Bool → Bool) (x : Nat → Bool) (hq : ∀ j, Quadratic (g j)) {n : Nat}
    (hE : 2 ≤ prefixExp g x n) :
    prefixExp g x (n + 5) ≤ prefixExp g x n + 3 := by
  have c0 := prefixExp_succ_cases g x n
  have c1 := prefixExp_succ_cases g x (n + 1)
  have c2 := prefixExp_succ_cases g x (n + 2)
  have c3 := prefixExp_succ_cases g x (n + 3)
  have c4 := prefixExp_succ_cases g x (n + 4)
  simp only [Nat.add_assoc, Nat.reduceAdd] at c1 c2 c3 c4
  have e1 : 1 ≤ prefixExp g x (n + 1) := by rcases c0 with h | h <;> omega
  have e2 : 1 ≤ prefixExp g x (n + 2) := by rcases c1 with h | h <;> omega
  have t0 := no_three_at g x hq (p := n) (by omega)
  have t1 := no_three_at g x hq (p := n + 1) e1
  have t2 := no_three_at g x hq (p := n + 2) e2
  have f0 := no_11011_at g x hq (p := n) hE
  simp only [Nat.add_assoc, Nat.reduceAdd] at t1 t2
  rcases c0 with h0 | h0 <;> rcases c1 with h1 | h1 <;> rcases c2 with h2 | h2 <;> rcases c3 with h3 | h3 <;>
    rcases c4 with h4 | h4 <;>
    first
    | omega
    | (rcases t0 with h | h | h <;> omega)
    | (rcases t1 with h | h | h <;> omega)
    | (rcases t2 with h | h | h <;> omega)
    | (rcases f0 with h | h | h | h | h <;> omega)

/-- Rule 30's right edge: the closing law for the OR family. -/
theorem closing_law_or (x : Nat → Bool) {n m : Nat}
    (h1 : prefixExp (fun _ b s => b || s) x (n + 1) = prefixExp (fun _ b s => b || s) x n + 1)
    (hpair : ∀ i, i < m →
      prefixExp (fun _ b s => b || s) x (n + 1 + 2 * i + 1) = prefixExp (fun _ b s => b || s) x (n + 1 + 2 * i) + 1 ∧
      prefixExp (fun _ b s => b || s) x (n + 1 + 2 * i + 1 + 1) = prefixExp (fun _ b s => b || s) x (n + 1 + 2 * i + 1))
    (hlast : prefixExp (fun _ b s => b || s) x (n + 1 + 2 * m + 1) =
      prefixExp (fun _ b s => b || s) x (n + 1 + 2 * m) + 1) :
    m + 1 ≤ 2 ^ prefixExp (fun _ b s => b || s) x n ∧
      (prefixExp (fun _ b s => b || s) x (n + 1 + 2 * m + 1 + 1) =
          prefixExp (fun _ b s => b || s) x (n + 1 + 2 * m + 1) + 1 ↔
        m + 1 = 2 ^ prefixExp (fun _ b s => b || s) x n) :=
  closing_law _ x (fun _ => quadratic_or) h1 hpair hlast

end Ruliology.CellularAutomata.Rule30ClosingLaw

#print axioms Ruliology.CellularAutomata.Rule30ClosingLaw.closing_law
#print axioms Ruliology.CellularAutomata.Rule30ClosingLaw.no_1101011
#print axioms Ruliology.CellularAutomata.Rule30ClosingLaw.order_countdown_exact
#print axioms Ruliology.CellularAutomata.Rule30ClosingLaw.five_letter

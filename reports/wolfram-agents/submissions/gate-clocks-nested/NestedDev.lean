import Rule30Submission

/-! Development file (Local, L1244): the parity and order layer of the nested gate-clock thresholds, on top of
Package A (R30-20261030-7b0d12). Not a submission. -/

namespace Rule30Submission

open Rule30RecordCharge Rule30DifferenceOrder

/-! ### Algebraic normal form of a two-input gate -/

/-- The coefficients of `g b s = λ b s ⊕ α b ⊕ β s ⊕ γ`. -/
def lamG (g : Bool → Bool → Bool) : Bool := xor (xor (g true true) (g true false)) (xor (g false true) (g false false))
def alpG (g : Bool → Bool → Bool) : Bool := xor (g true false) (g false false)
def betG (g : Bool → Bool → Bool) : Bool := xor (g false true) (g false false)
def gamG (g : Bool → Bool → Bool) : Bool := g false false

theorem gate_anf (g : Bool → Bool → Bool) (b s : Bool) :
    g b s = xor (xor (xor (lamG g && (b && s)) (alpG g && b)) (betG g && s)) (gamG g) := by
  unfold lamG alpG betG gamG
  cases b <;> cases s <;> cases h1 : g true true <;> cases h2 : g true false <;> cases h3 : g false true <;>
    cases h4 : g false false <;> simp_all

/-! ### XOR sums -/

theorem xsum_xor (f h : Nat → Bool) (t : Nat) :
    ∀ n, xsum (fun u => xor (f u) (h u)) t n = xor (xsum f t n) (xsum h t n)
  | 0 => rfl
  | n + 1 => by
    simp only [xsum]
    rw [xsum_xor f h t n]
    cases xsum f t n <;> cases xsum h t n <;> cases f (t + n) <;> cases h (t + n) <;> rfl

theorem xsum_and_const (c : Bool) (f : Nat → Bool) (t : Nat) :
    ∀ n, xsum (fun u => c && f u) t n = (c && xsum f t n)
  | 0 => by simp [xsum]
  | n + 1 => by
    simp only [xsum]
    rw [xsum_and_const c f t n]
    cases c <;> cases xsum f t n <;> cases f (t + n) <;> rfl

theorem xsum_const (c : Bool) (t : Nat) : ∀ n, xsum (fun _ => c) t n = (c && n % 2 == 1)
  | 0 => by simp [xsum]
  | n + 1 => by
    simp only [xsum]
    rw [xsum_const c t n]
    rcases Nat.mod_two_eq_zero_or_one n with h | h
    · rw [h, show (n + 1) % 2 = 1 by omega]; cases c <;> rfl
    · rw [h, show (n + 1) % 2 = 0 by omega]; cases c <;> rfl

theorem xsum_shift (f : Nat → Bool) (t c : Nat) : ∀ n, xsum f (t + c) n = xsum (fun u => f (u + c)) t n
  | 0 => rfl
  | n + 1 => by
    simp only [xsum]
    rw [xsum_shift f t c n, Nat.add_right_comm t c n]

theorem xsum_not (f : Nat → Bool) (t n : Nat) : xsum (fun u => !f u) t n = xor (xsum f t n) (n % 2 == 1) := by
  have e : (fun u => !f u) = fun u => xor ((fun _ => true) u) (f u) := by funext u; cases f u <;> rfl
  rw [e, xsum_xor, xsum_const]
  cases xsum f t n <;> cases (n % 2 == 1) <;> rfl

/-- A stream complemented by a shift of `L` has XOR sum `L mod 2` over `2 L`. -/
theorem xsum_antiperiod {f : Nat → Bool} {L : Nat} (hf : ∀ u, f (u + L) = !f u) (t : Nat) :
    xsum f t (L + L) = (L % 2 == 1) := by
  rw [xsum_add, xsum_shift]
  have e : (fun u => f (u + L)) = fun u => !f u := funext hf
  rw [e, xsum_not]
  cases xsum f t L <;> cases (L % 2 == 1) <;> rfl

/-- The overlap of an `L`-antiperiodic `b` with an `L`-periodic `s` over `2 L` is the XOR sum of `s` over `L`. -/
theorem xsum_overlap {b s : Nat → Bool} {L : Nat} (hb : ∀ u, b (u + L) = !b u) (hs : ∀ u, s (u + L) = s u)
    (t : Nat) : xsum (fun u => b u && s u) t (L + L) = xsum s t L := by
  rw [xsum_add, xsum_shift]
  have e : (fun u => b (u + L) && s (u + L)) = fun u => xor (s u) (b u && s u) := by
    funext u; rw [hb u, hs u]; cases b u <;> cases s u <;> rfl
  rw [e, xsum_xor]
  cases xsum s t L <;> cases xsum (fun u => b u && s u) t L <;> rfl

/-- Over the XOR sum of a gate's forcing, by its normal form. -/
theorem xsum_gate (g : Bool → Bool → Bool) (b s : Nat → Bool) (t n : Nat) :
    xsum (fun u => g (b u) (s u)) t n =
      xor (xor (xor (lamG g && xsum (fun u => b u && s u) t n) (alpG g && xsum b t n))
        (betG g && xsum s t n)) (gamG g && n % 2 == 1) := by
  have e : (fun u => g (b u) (s u)) = fun u => xor (xor (xor (lamG g && (b u && s u)) (alpG g && b u))
      (betG g && s u)) (gamG g) := funext fun u => gate_anf g (b u) (s u)
  rw [e]
  rw [show (fun u => xor (xor (xor (lamG g && (b u && s u)) (alpG g && b u)) (betG g && s u)) (gamG g)) =
      fun u => xor ((fun u => xor ((fun u => xor ((fun u => lamG g && (b u && s u)) u)
        ((fun u => alpG g && b u) u)) u) ((fun u => betG g && s u) u)) u) ((fun _ => gamG g) u) from rfl]
  rw [xsum_xor, xsum_xor, xsum_xor, xsum_and_const, xsum_and_const, xsum_and_const, xsum_const]

/-! ### Column facts -/

theorem col_period_of_le (g : Nat → Bool → Bool → Bool) (x : Nat → Bool) {n m : Nat} (h : n ≤ m) (t : Nat) :
    col g x n (t + 2 ^ prefixExp g x m) = col g x n t :=
  (prefix_period_iff g x m _).mpr (Nat.dvd_refl _) n h t

theorem prefixExp_double_iff (g : Nat → Bool → Bool → Bool) (x : Nat → Bool) (n : Nat) :
    prefixExp g x (n + 1) = prefixExp g x n + 1 ↔ xsum (force g x n) 0 (2 ^ prefixExp g x n) = true := by
  rw [prefixExp_succ]
  cases h : xsum (force g x n) 0 (2 ^ prefixExp g x n) <;> simp

theorem antiperiod_twice {f : Nat → Bool} {L : Nat} (hf : ∀ u, f (u + L) = !f u) (u : Nat) :
    f (u + (L + L)) = f u := by
  rw [← Nat.add_assoc, hf, hf, Bool.not_not]

theorem two_pow_even {e : Nat} (he : 1 ≤ e) : 2 ^ e % 2 = 0 := by
  obtain ⟨k, rfl⟩ : ∃ k, e = k + 1 := ⟨e - 1, by omega⟩
  rw [Nat.pow_succ]; simp

/-! ### No three doublings in a row -/

/-- **No three in a row**: if columns `n + 1` and `n + 2` both double and the prefix through column `n` has period at
least 2, column `n + 3` does not double. For every gate. -/
theorem no_three (g : Nat → Bool → Bool → Bool) (x : Nat → Bool) {n : Nat}
    (h1 : prefixExp g x (n + 1) = prefixExp g x n + 1)
    (h2 : prefixExp g x (n + 1 + 1) = prefixExp g x (n + 1) + 1) (hM : 1 ≤ prefixExp g x n) :
    prefixExp g x (n + 1 + 1 + 1) = prefixExp g x (n + 1 + 1) := by
  have hs : ∀ u, col g x (n + 1) (u + 2 ^ prefixExp g x n) = !col g x (n + 1) u := col_antiperiod g x h1
  have hb : ∀ u, col g x (n + 1 + 1) (u + 2 ^ prefixExp g x (n + 1)) = !col g x (n + 1 + 1) u := col_antiperiod g x h2
  have hs2 : ∀ u, col g x (n + 1) (u + 2 ^ prefixExp g x (n + 1)) = col g x (n + 1) u := by
    intro u; rw [h1, Nat.pow_succ, Nat.mul_two]; exact antiperiod_twice hs u
  have hf : force g x (n + 1 + 1) = fun u => g (n + 1 + 1) (col g x (n + 1 + 1) u) (col g x (n + 1) u) := by
    funext u; rfl
  have hL : 2 ^ prefixExp g x (n + 1 + 1) = 2 ^ prefixExp g x (n + 1) + 2 ^ prefixExp g x (n + 1) := by
    rw [h2, Nat.pow_succ, Nat.mul_two]
  have hx : xsum (force g x (n + 1 + 1)) 0 (2 ^ prefixExp g x (n + 1 + 1)) = false := by
    rw [hf, xsum_gate, hL, xsum_overlap hb hs2, xsum_antiperiod hb, xsum_add, xsum_period hs2 (0 + _)]
    rw [h1, Nat.pow_succ, Nat.mul_two, xsum_antiperiod hs]
    have e1 := two_pow_even hM
    have e2 : (2 ^ prefixExp g x n + 2 ^ prefixExp g x n) % 2 = 0 := by omega
    have e3 : (2 ^ prefixExp g x n + 2 ^ prefixExp g x n + (2 ^ prefixExp g x n + 2 ^ prefixExp g x n)) % 2 = 0 := by
      omega
    rw [e1, e2, e3]
    cases lamG (g (n + 1 + 1)) <;> cases alpG (g (n + 1 + 1)) <;> cases betG (g (n + 1 + 1)) <;>
      cases gamG (g (n + 1 + 1)) <;> cases xsum (col g x (n + 1)) 0 (2 ^ prefixExp g x n + 2 ^ prefixExp g x n) <;> rfl
  rw [prefixExp_succ, hx]
  rfl

/-! ### The doubling test after a `01` pair -/

/-- After a pair whose first column keeps the period `P ≥ 2` and whose second doubles, the next column doubles iff the
gate's quadratic coefficient is 1 and the first column has odd weight over `P`. -/
theorem after01_double_iff (g : Nat → Bool → Bool → Bool) (x : Nat → Bool) {n : Nat}
    (h0 : prefixExp g x (n + 1) = prefixExp g x n)
    (h1 : prefixExp g x (n + 1 + 1) = prefixExp g x (n + 1) + 1) (hM : 1 ≤ prefixExp g x n) :
    prefixExp g x (n + 1 + 1 + 1) = prefixExp g x (n + 1 + 1) + 1 ↔
      (lamG (g (n + 1 + 1)) && xsum (col g x (n + 1)) 0 (2 ^ prefixExp g x n)) = true := by
  have ha : ∀ u, col g x (n + 1) (u + 2 ^ prefixExp g x n) = col g x (n + 1) u := by
    intro u; rw [← h0]; exact col_period_of_le g x (Nat.le_refl _) u
  have hb : ∀ u, col g x (n + 1 + 1) (u + 2 ^ prefixExp g x n) = !col g x (n + 1 + 1) u := by
    intro u; rw [← h0]; exact col_antiperiod g x h1 u
  have hf : force g x (n + 1 + 1) = fun u => g (n + 1 + 1) (col g x (n + 1 + 1) u) (col g x (n + 1) u) := by
    funext u; rfl
  have hL : 2 ^ prefixExp g x (n + 1 + 1) = 2 ^ prefixExp g x n + 2 ^ prefixExp g x n := by
    rw [h1, h0, Nat.pow_succ, Nat.mul_two]
  rw [prefixExp_double_iff, hf, xsum_gate, hL, xsum_overlap hb ha, xsum_antiperiod hb, xsum_add,
    xsum_period ha (0 + _)]
  have e1 := two_pow_even hM
  have e2 : (2 ^ prefixExp g x n + 2 ^ prefixExp g x n) % 2 = 0 := by omega
  rw [e1, e2]
  cases lamG (g (n + 1 + 1)) <;> cases alpG (g (n + 1 + 1)) <;> cases betG (g (n + 1 + 1)) <;>
    cases gamG (g (n + 1 + 1)) <;> cases xsum (col g x (n + 1)) 0 (2 ^ prefixExp g x n) <;> simp

/-! ### Order zero is odd weight -/

theorem difs_pred_two_pow (f : Nat → Bool) : ∀ v t, difs (2 ^ v - 1) f t = xsum f t (2 ^ v)
  | 0, t => by simp [difs, xsum]
  | v + 1, t => by
    have e : 2 ^ (v + 1) - 1 = 2 ^ v + (2 ^ v - 1) := by
      have := Nat.one_le_two_pow (n := v); rw [Nat.pow_succ]; omega
    rw [e, difs_add, difs_two_pow]
    show xor (difs (2 ^ v - 1) f (t + 2 ^ v)) (difs (2 ^ v - 1) f t) = _
    rw [difs_pred_two_pow f v (t + 2 ^ v), difs_pred_two_pow f v t, Nat.pow_succ, Nat.mul_two, xsum_add]
    cases xsum f t (2 ^ v) <;> cases xsum f (t + 2 ^ v) (2 ^ v) <;> rfl

/-- For a stream of period `2 ^ v ≥ 2`, order 0 (the kit's reset condition) is odd weight over one period. -/
theorem order_zero_iff {f : Nat → Bool} {v : Nat} (hv : 1 ≤ v) (hf : ∀ t, f (t + 2 ^ v) = f t) :
    order f (2 ^ v) = 0 ↔ xsum f 0 (2 ^ v) = true := by
  have h2 : 2 ≤ 2 ^ v := by
    obtain ⟨k, rfl⟩ : ∃ k, v = k + 1 := ⟨v - 1, by omega⟩
    rw [Nat.pow_succ]; have := Nat.one_le_two_pow (n := k); omega
  have key := le_order_iff (g := f) (L := 2 ^ v) (r := 1) (Nat.le_refl 1) (by omega)
  constructor
  · intro h0
    have hnot : ¬ Vanish (2 ^ v - 1) f := fun hvan => by have := key.mpr hvan; omega
    cases hx : xsum f 0 (2 ^ v)
    · exfalso; apply hnot; intro t
      rw [difs_pred_two_pow, xsum_period hf t, hx]
    · rfl
  · intro hx
    apply Nat.eq_zero_of_not_pos
    intro hpos
    have hvan := key.mp hpos
    have := hvan 0
    rw [difs_pred_two_pow, hx] at this
    exact Bool.noConfusion this

/-! ### The first column after a `11` pair has order at least `M - 2` -/

theorem vanish_of_antiperiod {s : Nat → Bool} {e : Nat} (hs : ∀ u, s (u + 2 ^ e) = !s u) :
    Vanish (2 ^ e + 1) s := by
  have hconst : difs (2 ^ e) s = fun _ => true := by
    rw [difs_two_pow]; funext t; rw [hs t]; cases s t <;> rfl
  intro t
  rw [Nat.add_comm, difs_add, hconst]
  rfl

/-- After a pair in which both columns double, with prefix period `M = 2 ^ e ≥ 4` before it, the next column has order
at least `M - 2` at length `4 M`, for every gate. -/
theorem after11_order (g : Nat → Bool → Bool → Bool) (x : Nat → Bool) {n : Nat}
    (h1 : prefixExp g x (n + 1) = prefixExp g x n + 1)
    (h2 : prefixExp g x (n + 1 + 1) = prefixExp g x (n + 1) + 1) (hM : 2 ≤ prefixExp g x n) :
    2 ^ prefixExp g x n - 2 ≤ order (col g x (n + 1 + 1 + 1)) (2 ^ (prefixExp g x n + 2)) := by
  have hs : ∀ u, col g x (n + 1) (u + 2 ^ prefixExp g x n) = !col g x (n + 1) u := col_antiperiod g x h1
  have hb : ∀ u, col g x (n + 1 + 1) (u + 2 ^ (prefixExp g x n + 1)) = !col g x (n + 1 + 1) u := by
    intro u; rw [← h1]; exact col_antiperiod g x h2 u
  have hs2 : ∀ u, col g x (n + 1) (u + 2 ^ (prefixExp g x n + 1)) = col g x (n + 1) u := by
    intro u; rw [Nat.pow_succ, Nat.mul_two]; exact antiperiod_twice hs u
  have hh : ∀ t, col g x (n + 1 + 1 + 1) (t + 1) =
      xor (col g x (n + 1 + 1 + 1) t) (g (n + 1 + 1) (col g x (n + 1 + 1) t) (col g x (n + 1) t)) := by
    intro t; rw [col_step]; rfl
  have hv : Vanish (2 ^ prefixExp g x n + 1) (col g x (n + 1)) := vanish_of_antiperiod hs
  have hpast := vanish_past_gate (g := g (n + 1 + 1)) hs2 hb hh (k := 2 ^ prefixExp g x n) hv
  have p4 : 2 ^ (prefixExp g x n + 2) = 4 * 2 ^ prefixExp g x n := by
    rw [Nat.pow_add]; omega
  have p2 : 2 ^ (prefixExp g x n + 1) = 2 * 2 ^ prefixExp g x n := by rw [Nat.pow_succ]; omega
  have p0 : 4 ≤ 2 ^ prefixExp g x n := by
    have := Nat.pow_le_pow_right (n := 2) (by decide) hM; simpa using this
  apply (le_order_iff (by omega) (by omega)).mpr
  rw [show 2 ^ (prefixExp g x n + 2) - (2 ^ prefixExp g x n - 2) =
      2 ^ prefixExp g x n + 1 + 1 + 2 ^ (prefixExp g x n + 1) by omega]
  exact hpast

/-! ### Pairs of bits

Pair `i` is bits `2i` and `2i + 1`, that is columns `2i + 1` and `2i + 2`. -/

/-- The first bit of pair `i` doubles the prefix period. -/
def fd (g : Nat → Bool → Bool → Bool) (x : Nat → Bool) (i : Nat) : Prop :=
  prefixExp g x (2 * i + 1) = prefixExp g x (2 * i) + 1

/-- The last bit of pair `i` doubles the prefix period. -/
def ld (g : Nat → Bool → Bool → Bool) (x : Nat → Bool) (i : Nat) : Prop :=
  prefixExp g x (2 * i + 1 + 1) = prefixExp g x (2 * i + 1) + 1

/-- The resource before pair `i`: the order of the previous pair's last bit over the prefix period. -/
noncomputable def res (g : Nat → Bool → Bool → Bool) (x : Nat → Bool) (i : Nat) : Nat :=
  order (col g x (2 * i)) (2 ^ prefixExp g x (2 * i))

/-- The order of pair `i`'s first bit over its prefix period. -/
noncomputable def ford (g : Nat → Bool → Bool → Bool) (x : Nat → Bool) (i : Nat) : Nat :=
  order (col g x (2 * i + 1)) (2 ^ prefixExp g x (2 * i + 1))

theorem two_mul_succ (i : Nat) : 2 * (i + 1) = 2 * i + 1 + 1 := by omega

theorem col_rec (g : Nat → Bool → Bool → Bool) (x : Nat → Bool) (n t : Nat) :
    col g x (n + 1 + 1) (t + 1) = xor (col g x (n + 1 + 1) t) (g (n + 1) (col g x (n + 1) t) (col g x n t)) := by
  rw [col_step]; rfl

theorem col_per (g : Nat → Bool → Bool → Bool) (x : Nat → Bool) (n t : Nat) :
    col g x n (t + 2 ^ prefixExp g x n) = col g x n t :=
  col_period_of_le g x (Nat.le_refl n) t

/-- A `11` pair needs resource 0 before it. -/
theorem res_zero_of_11 (g : Nat → Bool → Bool → Bool) (x : Nat → Bool) {i : Nat}
    (hf : fd g x i) (hl : ld g x i) : res g x i = 0 := by
  unfold fd at hf; unfold ld at hl; unfold res
  have hanti : ∀ t, col g x (2 * i + 1 + 1) (t + 2 * 2 ^ prefixExp g x (2 * i)) = !col g x (2 * i + 1 + 1) t := by
    intro t
    have := col_antiperiod g x hl t
    rwa [hf, two_pow_succ'] at this
  exact order_reset_before_gate (col_per g x (2 * i)) (col_antiperiod g x hf) (col_rec g x (2 * i)) hanti

/-- A doubled last bit leaves the largest resource. -/
theorem res_after_ld (g : Nat → Bool → Bool → Bool) (x : Nat → Bool) {i : Nat} (hl : ld g x i) :
    res g x (i + 1) = 2 ^ prefixExp g x (2 * i + 1) - 1 := by
  unfold ld at hl; unfold res
  rw [two_mul_succ, hl, two_pow_succ']
  exact order_of_antiperiod (col_antiperiod g x hl)

/-- A `10` pair lowers the resource by at most one. -/
theorem res_countdown (g : Nat → Bool → Bool → Bool) (x : Nat → Bool) {i : Nat}
    (hf : fd g x i) (hl : ¬ ld g x i) : res g x i ≤ res g x (i + 1) + 1 := by
  unfold fd at hf; unfold ld at hl; unfold res
  have h0 : prefixExp g x (2 * i + 1 + 1) = prefixExp g x (2 * i + 1) := by
    rcases prefixExp_succ_cases g x (2 * i + 1) with h | h
    · exact h
    · exact absurd h hl
  rw [two_mul_succ, h0, hf, two_pow_succ']
  exact order_countdown_gate (col_per g x (2 * i)) (col_antiperiod g x hf) (col_rec g x (2 * i))

theorem not_fd_eq (g : Nat → Bool → Bool → Bool) (x : Nat → Bool) {i : Nat} (h : ¬ fd g x i) :
    prefixExp g x (2 * i + 1) = prefixExp g x (2 * i) := by
  rcases prefixExp_succ_cases g x (2 * i) with e | e
  · exact e
  · exact absurd e h

/-- Between consecutive `01` pairs the first-bit order drops by at most one. -/
theorem ford_countdown (g : Nat → Bool → Bool → Bool) (x : Nat → Bool) {i : Nat}
    (hl : ld g x i) (hf' : ¬ fd g x (i + 1)) : ford g x i ≤ ford g x (i + 1) + 1 := by
  unfold ld at hl; unfold ford
  have e1 := not_fd_eq g x hf'
  rw [two_mul_succ] at e1
  rw [two_mul_succ, e1, hl, two_pow_succ']
  exact order_countdown_gate (col_per g x (2 * i + 1)) (col_antiperiod g x hl) (col_rec g x (2 * i + 1))

/-- After a `01` pair with prefix period at least 2, a doubling of the next first bit needs first-bit order 0. -/
theorem ford_zero (g : Nat → Bool → Bool → Bool) (x : Nat → Bool) {i : Nat} (hM : 1 ≤ prefixExp g x (2 * i))
    (hf : ¬ fd g x i) (hl : ld g x i) (hf' : fd g x (i + 1)) : ford g x i = 0 := by
  have h0 := not_fd_eq g x hf
  unfold ld at hl; unfold fd at hf'; unfold ford
  rw [two_mul_succ] at hf'
  have key := (after01_double_iff g x h0 hl hM).mp hf'
  have hx : xsum (col g x (2 * i + 1)) 0 (2 ^ prefixExp g x (2 * i)) = true := by
    cases h : xsum (col g x (2 * i + 1)) 0 (2 ^ prefixExp g x (2 * i)) <;> simp_all
  rw [h0]
  have hper : ∀ t, col g x (2 * i + 1) (t + 2 ^ prefixExp g x (2 * i)) = col g x (2 * i + 1) t := by
    intro t; rw [← h0]; exact col_per g x _ t
  exact (order_zero_iff hM hper).mpr hx

/-- No-three for pairs: after a `11` pair with prefix period at least 2, the next first bit does not double. -/
theorem no_three_pair (g : Nat → Bool → Bool → Bool) (x : Nat → Bool) {i : Nat} (hM : 1 ≤ prefixExp g x (2 * i))
    (hf : fd g x i) (hl : ld g x i) : ¬ fd g x (i + 1) := by
  intro h
  unfold fd at hf h; unfold ld at hl
  rw [two_mul_succ] at h
  have := no_three g x hf hl hM
  omega

/-- After a `11` pair with prefix period `M ≥ 4`, the next first bit has order at least `M - 2`. -/
theorem ford_after_11 (g : Nat → Bool → Bool → Bool) (x : Nat → Bool) {i : Nat} (hM : 2 ≤ prefixExp g x (2 * i))
    (hf : fd g x i) (hl : ld g x i) : 2 ^ prefixExp g x (2 * i) - 2 ≤ ford g x (i + 1) := by
  have hnf := no_three_pair g x (by omega) hf hl
  have e1 := not_fd_eq g x hnf
  unfold fd at hf; unfold ld at hl; unfold ford
  rw [two_mul_succ] at e1 ⊢
  rw [e1, hl, hf]
  exact after11_order g x hf hl hM

/-! ### Exponent steps by pairs -/

theorem pe_step (g : Nat → Bool → Bool → Bool) (x : Nat → Bool) (n : Nat) :
    prefixExp g x n ≤ prefixExp g x (n + 1) ∧ prefixExp g x (n + 1) ≤ prefixExp g x n + 1 := by
  rcases prefixExp_succ_cases g x n with h | h <;> omega

theorem E_pair (g : Nat → Bool → Bool → Bool) (x : Nat → Bool) (i : Nat) :
    prefixExp g x (2 * i) ≤ prefixExp g x (2 * (i + 1)) ∧
      prefixExp g x (2 * (i + 1)) ≤ prefixExp g x (2 * i) + 2 := by
  rw [two_mul_succ]
  have a := pe_step g x (2 * i)
  have b := pe_step g x (2 * i + 1)
  omega

theorem pair_11 (g : Nat → Bool → Bool → Bool) (x : Nat → Bool) (i : Nat)
    (h : prefixExp g x (2 * (i + 1)) = prefixExp g x (2 * i) + 2) : fd g x i ∧ ld g x i := by
  unfold fd ld
  rw [two_mul_succ] at h
  have a := pe_step g x (2 * i)
  have b := pe_step g x (2 * i + 1)
  constructor <;> omega

theorem pair_w1 (g : Nat → Bool → Bool → Bool) (x : Nat → Bool) (i : Nat)
    (h : prefixExp g x (2 * (i + 1)) = prefixExp g x (2 * i) + 1) :
    (fd g x i ∧ ¬ ld g x i) ∨ (¬ fd g x i ∧ ld g x i) := by
  unfold fd ld
  rw [two_mul_succ] at h
  rcases prefixExp_succ_cases g x (2 * i) with a | a <;> rcases prefixExp_succ_cases g x (2 * i + 1) with b | b
  · omega
  · right; constructor <;> omega
  · left; constructor <;> omega
  · omega

/-! ### First and last visits, and chained countdowns -/

open Classical in
theorem exists_first {p : Nat → Prop} : ∀ n k, k ≤ n → p k → ∃ m, m ≤ k ∧ p m ∧ ∀ j, j < m → ¬ p j
  | 0, k, hk, hp => by
    have : k = 0 := by omega
    subst this
    exact ⟨0, Nat.le_refl 0, hp, fun j hj => absurd hj (Nat.not_lt_zero j)⟩
  | n + 1, k, hk, hp => by
    by_cases h : ∃ j, j < k ∧ p j
    · obtain ⟨j, hj, hpj⟩ := h
      obtain ⟨m, hm, hpm, hmin⟩ := exists_first n j (by omega) hpj
      exact ⟨m, by omega, hpm, hmin⟩
    · exact ⟨k, Nat.le_refl k, hp, fun j hj hpj => h ⟨j, hj, hpj⟩⟩

open Classical in
theorem exists_last_from {q : Nat → Prop} {a : Nat} (ha : q a) :
    ∀ P, a ≤ P → ∃ K, a ≤ K ∧ K ≤ P ∧ q K ∧ ∀ m, K < m → m ≤ P → ¬ q m
  | 0, h => by
    have : a = 0 := by omega
    subst this
    exact ⟨0, Nat.le_refl 0, Nat.le_refl 0, ha, fun m h1 h2 => by omega⟩
  | P + 1, h => by
    by_cases hq : q (P + 1)
    · exact ⟨P + 1, h, Nat.le_refl _, hq, fun m h1 h2 => by omega⟩
    · rcases Nat.lt_or_eq_of_le h with h' | h'
      · obtain ⟨K, hK0, hKP, hqK, hmax⟩ := exists_last_from ha P (by omega)
        refine ⟨K, hK0, by omega, hqK, fun m h1 h2 => ?_⟩
        rcases Nat.lt_or_eq_of_le h2 with h3 | h3
        · exact hmax m h1 (by omega)
        · rw [h3]; exact hq
      · rw [h'] at ha; exact absurd ha hq

theorem chain_le {f : Nat → Nat} (a : Nat) :
    ∀ d, (∀ i, a ≤ i → i < a + d → f i ≤ f (i + 1) + 1) → f a ≤ f (a + d) + d
  | 0, _ => by simp
  | d + 1, h => by
    have ih := chain_le a d (fun i h1 h2 => h i h1 (by omega))
    have := h (a + d) (by omega) (by omega)
    rw [show a + (d + 1) = a + d + 1 by omega]
    omega

/-! ### The nested threshold: excess 3 needs 2058 pairs -/

/-- If the first `2N` bits reach excess 3 (`E(2N) ≥ N + 3`) for the first time at `N`, then `N ≥ 2058`. -/
theorem first_excess_three (g : Nat → Bool → Bool → Bool) (x : Nat → Bool) {N : Nat}
    (hN : N + 3 ≤ prefixExp g x (2 * N)) (hfirst : ∀ m, m < N → prefixExp g x (2 * m) ≤ m + 2) :
    2058 ≤ N := by
  have z : prefixExp g x (2 * 0) = 0 := rfl
  obtain ⟨P, rfl⟩ : ∃ P, N = P + 1 := by
    rcases Nat.eq_zero_or_pos N with h | h
    · subst h; omega
    · exact ⟨N - 1, by omega⟩
  have hP := hfirst P (by omega)
  have hPP := E_pair g x P
  obtain ⟨hfP, hlP⟩ := pair_11 g x P (by omega)
  have eP : prefixExp g x (2 * P) = P + 2 := by omega
  -- the last visit to excess at most 1
  obtain ⟨K, -, hKP, hEK, hKmax⟩ := exists_last_from (q := fun m => prefixExp g x (2 * m) ≤ m + 1) (a := 0)
    (by show prefixExp g x (2 * 0) ≤ 0 + 1; omega) P (Nat.zero_le P)
  have hmid : ∀ m, K < m → m ≤ P → prefixExp g x (2 * m) = m + 2 := fun m h1 h2 => by
    have h3 := hKmax m h1 h2
    have h4 := hfirst m (by omega)
    omega
  have hKP' : K < P := by
    rcases Nat.lt_or_eq_of_le hKP with h | h
    · exact h
    · subst h; omega
  have eK1 := hmid (K + 1) (by omega) (by omega)
  have hKK := E_pair g x K
  have eK : prefixExp g x (2 * K) = K + 1 := by omega
  obtain ⟨hfK, hlK⟩ := pair_11 g x K (by omega)
  -- K ≥ 2
  have hK2 : 2 ≤ K := by
    rcases (by omega : K = 0 ∨ K = 1 ∨ 2 ≤ K) with h | h | h
    · subst h
      have a := pe_step g x 0
      have b := pe_step g x 1
      have z0 : prefixExp g x 0 = 0 := rfl
      simp at eK1 a b
      omega
    · subst h
      unfold fd at hfK; unfold ld at hlK
      have e2 : prefixExp g x 2 = 2 := eK
      have e3 : prefixExp g x 3 = prefixExp g x 2 + 1 := hfK
      have e4 : prefixExp g x 4 = prefixExp g x 3 + 1 := hlK
      have b0 : prefixExp g x 1 ≤ prefixExp g x 0 + 1 := (pe_step g x 0).2
      have b1 : prefixExp g x 2 ≤ prefixExp g x 1 + 1 := (pe_step g x 1).2
      have z0 : prefixExp g x 0 = 0 := rfl
      have h1 : prefixExp g x 1 = 1 := by omega
      have h3 : prefixExp g x 4 = prefixExp g x 3 :=
        no_three g x (n := 1) (show prefixExp g x 2 = prefixExp g x 1 + 1 by omega)
          (show prefixExp g x 3 = prefixExp g x 2 + 1 from e3) (by omega)
      omega
    · exact h
  have hM8 : 8 ≤ 2 ^ prefixExp g x (2 * K) := by
    rw [eK]
    have := Nat.pow_le_pow_right (n := 2) (by decide) (show 3 ≤ K + 1 by omega)
    simpa using this
  -- pairs strictly between K and P have weight one
  have hw1 : ∀ m, K < m → m < P → (fd g x m ∧ ¬ ld g x m) ∨ (¬ fd g x m ∧ ld g x m) := fun m h1 h2 =>
    pair_w1 g x m (by have := hmid m h1 (by omega); have := hmid (m + 1) (by omega) (by omega); omega)
  have hnf1 : ¬ fd g x (K + 1) := no_three_pair g x (by omega) hfK hlK
  have hK1P : K + 1 < P := by
    rcases Nat.lt_or_eq_of_le (show K + 1 ≤ P by omega) with h | h
    · exact h
    · exact absurd (h ▸ hfP) hnf1
  have hF1 := ford_after_11 g x (by omega : 2 ≤ prefixExp g x (2 * K)) hfK hlK
  -- the first doubled first bit after pair K
  obtain ⟨j, hjP, ⟨hjK, hfj⟩, hjmin⟩ := exists_first (p := fun j => K + 2 ≤ j ∧ fd g x j) P P
    (Nat.le_refl P) ⟨by omega, hfP⟩
  have h01 : ∀ m, K + 1 ≤ m → m < j → ¬ fd g x m ∧ ld g x m := fun m h1 h2 => by
    have hnf : ¬ fd g x m := by
      rcases Nat.lt_or_eq_of_le h1 with h | h
      · exact fun hf => hjmin m h2 ⟨by omega, hf⟩
      · exact h ▸ hnf1
    rcases hw1 m (by omega) (by omega) with h | h
    · exact absurd h.1 hnf
    · exact h
  have hchain := chain_le (f := ford g x) (K + 1) (j - 1 - (K + 1)) (fun i h1 h2 =>
    ford_countdown g x (h01 i h1 (by omega)).2 (h01 (i + 1) (by omega) (by omega)).1)
  rw [show K + 1 + (j - 1 - (K + 1)) = j - 1 by omega] at hchain
  have hFz : ford g x (j - 1) = 0 := by
    have hj1 : j - 1 + 1 = j := by omega
    have hE : 1 ≤ prefixExp g x (2 * (j - 1)) := by rw [hmid (j - 1) (by omega) (by omega)]; omega
    exact ford_zero g x hE (h01 (j - 1) (by omega) (by omega)).1 (h01 (j - 1) (by omega) (by omega)).2
      (by rw [hj1]; exact hfj)
  -- the last 01 pair
  obtain ⟨ell, hell0, hellP, ⟨hnfe, hle⟩, hellmax⟩ := exists_last_from (q := fun m => ¬ fd g x m ∧ ld g x m)
    (a := j - 1) (h01 (j - 1) (by omega) (by omega)) (P - 1) (by omega)
  have h10 : ∀ m, ell < m → m ≤ P - 1 → fd g x m ∧ ¬ ld g x m := fun m h1 h2 => by
    rcases hw1 m (by omega) (by omega) with h | h
    · exact h
    · exact absurd h (hellmax m h1 h2)
  have hR := res_after_ld g x hle
  have heE : prefixExp g x (2 * ell + 1) = ell + 2 := by
    rw [not_fd_eq g x hnfe]; exact hmid ell (by omega) (by omega)
  have hRchain := chain_le (f := res g x) (ell + 1) (P - (ell + 1)) (fun i h1 h2 =>
    res_countdown g x (h10 i (by omega) (by omega)).1 (h10 i (by omega) (by omega)).2)
  have hR0 := res_zero_of_11 g x hfP hlP
  rw [show ell + 1 + (P - (ell + 1)) = P by omega, hR0, hR, heE] at hRchain
  have hpow : 2048 ≤ 2 ^ (ell + 2) := by
    have := Nat.pow_le_pow_right (n := 2) (by decide) (show 11 ≤ ell + 2 by omega)
    simpa using this
  omega

/-- **Nested threshold**: for every family of two-input gates and every seed, the first `2m` bits have period
dividing `2 ^ (m + 2)` for every `m < 2058`. -/
theorem prefixExp_le_add_two (g : Nat → Bool → Bool → Bool) (x : Nat → Bool) :
    ∀ m, m < 2058 → prefixExp g x (2 * m) ≤ m + 2 := by
  intro m hm
  apply Nat.le_of_not_lt
  intro hlt
  obtain ⟨N, hNm, hN, hmin⟩ := exists_first (p := fun N => N + 3 ≤ prefixExp g x (2 * N)) m m (Nat.le_refl m)
    (by omega)
  have := first_excess_three g x hN (fun k hk => by have := hmin k hk; omega)
  omega

end Rule30Submission

import Std.Tactic

/-!
# A white path in the frame of the right edge

Depth increases toward the interior. A causal path can advance by zero, one or
two depths per tick. If its final step holds its depth, its entire trace is
white exactly when the complete bottom interval of its final light cone is
white. The one-step proof restates the white-witness mechanism of GC2598 in
these coordinates.
-/

namespace RightRayWhiteCone

abbrev Row := Int → Bool

def White (x : Row) (a b : Int) : Prop :=
  ∀ i, a ≤ i → i ≤ b → x i = false

def Step (x y : Row) : Prop :=
  ∀ i, y i = xor (x i) (x (i - 1) || x (i - 2))

private theorem xor_white {u v : Bool} (h : xor u v = false) : u = v := by
  cases u <;> cases v <;> simp_all

private theorem or_absorb {u v w : Bool} (h : u = (v || w)) : (u || v) = u := by
  cases v <;> cases w <;> simp_all

private theorem both_white {u v : Bool} (h : false = (u || v)) :
    u = false ∧ v = false := by
  cases u <;> cases v <;> simp_all

/-- Any white witness directly above a white interval picks its all-white predecessor. -/
theorem one_layer {x y : Row} (hstep : Step x y) {a b k : Int}
    (hak : a ≤ k) (hkb : k ≤ b) :
    (White y a b ∧ x k = false) ↔ White x (a - 2) b := by
  constructor
  · rintro ⟨hy, hk⟩
    have fixed (i : Int) (hi : a ≤ i) (hj : i ≤ b) :
        x i = (x (i - 1) || x (i - 2)) := by
      apply xor_white
      rw [← hstep i]
      exact hy i hi hj
    have adjacent (i : Int) (hi : a ≤ i) (hj : i + 1 ≤ b) :
        x (i + 1) = x i := by
      rw [fixed (i + 1) (by omega) hj,
        show i + 1 - 1 = i by omega, show i + 1 - 2 = i - 1 by omega]
      exact or_absorb (fixed i hi (by omega))
    have from_left : ∀ m : Nat, a + (m : Int) ≤ b → x (a + m) = x a := by
      intro m
      induction m with
      | zero => simp
      | succ m ih =>
        intro hm
        rw [show a + ((m + 1 : Nat) : Int) = (a + m) + 1 by omega,
          adjacent (a + m) (by omega) (by omega), ih (by omega)]
    have flat (i : Int) (hi : a ≤ i) (hj : i ≤ b) : x i = x a := by
      have e : a + ((i - a).toNat : Int) = i := by omega
      have h := from_left (i - a).toNat (by omega)
      rwa [e] at h
    have ha : x a = false := (flat k hak hkb).symm.trans hk
    have hf := fixed a (by omega) (by omega)
    rw [ha] at hf
    obtain ⟨h₁, h₂⟩ := both_white hf
    intro i hi hj
    by_cases h : a ≤ i
    · exact (flat i h hj).trans ha
    · have e : i = a - 1 ∨ i = a - 2 := by omega
      rcases e with rfl | rfl
      · exact h₁
      · exact h₂
  · intro hx
    constructor
    · intro i hi hj
      rw [hstep i, hx i (by omega) hj, hx (i - 1) (by omega) (by omega),
        hx (i - 2) (by omega) (by omega)]
      rfl
    · exact hx k (by omega) hkb

/-- One observed white witness per inner layer, together with a white terminal cell. -/
theorem witnesses_iff (X : Nat → Row) (step : ∀ t, Step (X t) (X (t + 1))) :
    ∀ (T t : Nat) (p : Nat → Int) (d : Int),
      (∀ k, k < T → d - 2 * ((T - 1 - k : Nat) : Int) ≤ p k ∧ p k ≤ d) →
      ((X (t + T) d = false ∧ ∀ k, k < T → X (t + k) (p k) = false) ↔
        White (X t) (d - 2 * (T : Int)) d) := by
  intro T
  induction T with
  | zero =>
    intro t p d _
    constructor
    · rintro ⟨h, _⟩ i hi hj
      have eq : i = d := by omega
      simpa [eq] using h
    · intro h
      exact ⟨by simpa using h d (by omega) (by omega), by omega⟩
  | succ T ih =>
    intro t p d hpath
    let next := fun k : Nat => p (k + 1)
    have hnext : ∀ k, k < T → d - 2 * ((T - 1 - k : Nat) : Int) ≤ next k ∧ next k ≤ d := by
      intro k hk
      obtain ⟨h₁,h₂⟩ := hpath (k+1) (by omega)
      dsimp [next]
      exact ⟨by omega, h₂⟩
    have e := ih (t+1) next d hnext
    have hk := hpath 0 (by omega)
    have layer := one_layer (step t) (a := d - 2 * (T : Int)) (b := d)
      (k := p 0) (by omega) hk.2
    have low : d - 2 * ((T + 1 : Nat) : Int) = d - 2 * (T : Int) - 2 := by omega
    rw [low]
    constructor
    · rintro ⟨hend, hw⟩
      apply layer.mp
      constructor
      · apply e.mp
        constructor
        · simpa only [show t + 1 + T = t + (T + 1) by omega] using hend
        · intro k h
          simpa only [next, show t + 1 + k = t + (k + 1) by omega] using hw (k+1) (by omega)
      · simpa using hw 0 (by omega)
    · intro h
      obtain ⟨hy, hzero⟩ := layer.mpr h
      obtain ⟨hend, hw⟩ := e.mpr hy
      constructor
      · simpa only [show t + 1 + T = t + (T + 1) by omega] using hend
      · intro k h
        cases k with
        | zero => simpa using hzero
        | succ k =>
          simpa only [next, show t + 1 + k = t + (k + 1) by omega] using hw k (by omega)

def Causal (p : Nat → Int) (T : Nat) : Prop :=
  ∀ k, k < T → p k ≤ p (k+1) ∧ p (k+1) ≤ p k + 2

private theorem path_span {p : Nat → Int} {T : Nat} (hp : Causal p T) (a : Nat) :
    ∀ m : Nat, a + m ≤ T → p a ≤ p (a+m) ∧ p (a+m) ≤ p a + 2 * (m : Int) := by
  intro m
  induction m with
  | zero => simp
  | succ m ih =>
    intro h
    obtain ⟨h₁,h₂⟩ := ih (by omega)
    obtain ⟨h₃,h₄⟩ := hp (a+m) (by omega)
    change p a ≤ p ((a+m)+1) ∧ p ((a+m)+1) ≤ p a + 2 * ((m+1 : Nat) : Int)
    constructor <;> omega

/-- The clock starts at an arbitrary row t. The path's last two observations have the same depth. -/
theorem white_path_iff (X : Nat → Row) (step : ∀ t, Step (X t) (X (t+1)))
    (t N : Nat) (p : Nat → Int) (hp : Causal p (N+1)) (hold : p (N+1) = p N) :
    (∀ k, k ≤ N+1 → X (t+k) (p k) = false) ↔
      White (X t) (p (N+1) - 2 * ((N+1 : Nat) : Int)) (p (N+1)) := by
  have e := witnesses_iff X step (N+1) t p (p (N+1)) (by
    intro k hk
    have h := path_span hp k (N-k) (by omega)
    rw [show k + (N-k) = N by omega, ← hold] at h
    exact ⟨by omega, h.1⟩)
  constructor
  · intro hw
    exact e.mp ⟨hw (N+1) (by omega), fun k hk => hw k (by omega)⟩
  · intro h k hk
    obtain ⟨hend, hw⟩ := e.mpr h
    by_cases he : k = N+1
    · simpa only [he] using hend
    · exact hw k (by omega)

end RightRayWhiteCone

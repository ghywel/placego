import Init

/-! Core-only development formalization of the ancestor-forcing step in GC2233
and the local Boolean inverse used in GC2238.
No finite ancestry, periodicity, period minimality, or prize statement is asserted.
No Mathlib or prize-kit dependency is needed for this Boolean implication. -/
namespace Rule30IsolatedTransitionCore

def Recurrence (x a b : Nat → Bool) : Prop :=
  ∀ t, x (t+1) = xor (x t) (a t || b t)

def delta (x : Nat → Bool) (t : Nat) : Bool := xor (x t) (x (t+1))

def Isolated (x : Nat → Bool) : Prop :=
  ∀ t, x t = true → x (t+1) = false

theorem xor_cancel : ∀ x y : Bool, xor x (xor x y) = y := by decide

theorem delta_of_recurrence (c b a : Nat → Bool) (hc : Recurrence c b a) :
    ∀ t, delta c t = (b t || a t) := by
  intro t
  unfold delta
  rw [hc t]
  exact xor_cancel (c t) (b t || a t)

theorem local_forcing : ∀ b a d h bn an : Bool,
    bn = xor b (a || d) → an = xor a (d || h) →
    ((b || a) = true → (bn || an) = false) →
    b = (b || a) ∧ a = (b || a) := by decide

theorem ancestors_equal_or (b a d h : Nat → Bool)
    (hb : Recurrence b a d) (ha : Recurrence a d h)
    (hi : Isolated (fun t => b t || a t)) :
    ∀ t, b t = (b t || a t) ∧ a t = (b t || a t) := by
  intro t
  exact local_forcing (b t) (a t) (d t) (h t) (b (t+1)) (a (t+1))
    (hb t) (ha t) (hi t)

theorem isolated_transition_forces_ancestors (c b a d h : Nat → Bool)
    (hc : Recurrence c b a) (hb : Recurrence b a d) (ha : Recurrence a d h)
    (hi : Isolated (delta c)) :
    ∀ t, b t = delta c t ∧ a t = delta c t := by
  have hd := delta_of_recurrence c b a hc
  have hor : Isolated (fun t => b t || a t) := by
    intro t ht
    change (b t || a t) = true at ht
    change (b (t+1) || a (t+1)) = false
    rw [← hd t] at ht
    rw [← hd (t+1)]
    exact hi t ht
  intro t
  rw [hd t]
  exact ancestors_equal_or b a d h hb ha hor t

theorem xor_or_absorb : ∀ c n : Bool, (c || xor c n) = (c || n) := by decide

theorem closing_identity : ∀ l c r : Bool,
    ((l || c) && (c || r)) = (c || (l && r)) := by decide

theorem inverse_no_white_singleton : ∀ l c r : Bool,
    (l = true → r = true → c = true) → ((l || c) && (c || r)) = c := by decide

def dilation (c : Nat → Bool) (t : Nat) : Bool := c t || c (t+1)

theorem dilation_inverse (c : Nat → Bool)
    (h : ∀ t, c t = true → c (t+2) = true → c (t+1) = true) :
    ∀ t, (dilation c t && dilation c (t+1)) = c (t+1) := by
  intro t
  exact inverse_no_white_singleton (c t) (c (t+1)) (c (t+2)) (h t)

theorem white_singleton_is_needed :
    let l := true; let c := false; let r := true
    ((l || c) && (c || r)) ≠ c := by decide

-- Fixed omitted-hypothesis controls, not actual infinite histories.
theorem isolation_is_needed :
    let b := false; let a := true; let d := false; let h := false
    let bn := xor b (a || d); let an := xor a (d || h)
    (b || a) = true ∧ (bn || an) = true ∧ b ≠ (b || a) := by decide

theorem second_recurrence_is_needed :
    let b := true; let a := false; let d := true; let h := false
    let bn := false; let an := false
    bn = xor b (a || d) ∧ ((b || a) = true → (bn || an) = false) ∧
    an ≠ xor a (d || h) ∧ a ≠ (b || a) := by decide

theorem first_recurrence_is_needed :
    let b := false; let a := true; let d := true; let h := false
    let bn := false; let an := false
    an = xor a (d || h) ∧ ((b || a) = true → (bn || an) = false) ∧
    bn ≠ xor b (a || d) ∧ b ≠ (b || a) := by decide

end Rule30IsolatedTransitionCore

module

public import Ruliology.CellularAutomata.Rule30AgedLeftDiagonals

/-!
# The error edge of two configurations of rule 30

Two left-diagonal arrays `a` and `b` (`Rule30AgedLeftDiagonals.Recurrence`: wheel `0` is constant, wheel `1` is the
or of wheels `0` and `1`, wheel `i + 2` is `xor (wheel i) (wheel (i + 1) || wheel (i + 2))`, each read one tick earlier)
that agree on every wheel below `m` at tick `t` and differ at `m` have their *error edge* at `m` (`Edge`). Its one-step
law:

* `agree_step`, `agree_after`: agreement below `m` is kept for ever (a wheel reads only itself and the two below it).
  So the edge never retreats (`edge_le`).
* `heal_iff`: at an edge of index at least 1, the arrays agree there one tick later exactly when its parent is black. With a white
  wheel below, the edge stays (`edge_stall`); with a black one agreement extends through the old edge (`edge_heal`), possibly eliminating all differences. The black half is the
  recruiting step of `Rule30HealingBound`; the white-parent memory mechanism also appears inside `Rule30UniversalLeftSide.child_white`. The exact interior Boolean criterion is `Rule30LightCone.rule_flip_right_iff` (kit PR 98).
* After a heal at an old edge of index at least 2, the wheels above it are constrained. If the first wheel above the old edge agrees at the next
  tick, it is white there (`white_above`); if the first two agree, the second is black (`black_two_above`). Hence after
  a jump of exactly 2 the new parent is white (`jump_two`), after a jump of exactly 3 it is black (`jump_three`), after
  a jump of exactly 4 it is black one tick later whatever it was (`jump_four`), after a jump of exactly 5 whose new
  parent is white it is black one tick later (`jump_five`), and after a jump of exactly 6 or 7 whose new parent is
  white it is white one tick later (`jump_six`, `jump_seven`).

Every statement is about two abstract arrays with the recurrence and holds for any two configurations with leftmost
black cells translated into alignment and read from their common left edge (`Rule30FiniteDiagonals.Ld`, `Rule30AgedLeftDiagonals.Ld_recurrence`), the second
array being, for instance, a periodic strip. The proofs unfold the recurrence on a window of wheels and decide the resulting Boolean identities. Nothing
here concerns the center column or the Prize problems.
-/

@[expose] public section

namespace Ruliology.CellularAutomata.Rule30ErrorEdge

open Rule30AgedLeftDiagonals

set_option autoImplicit false

/-- `a` and `b` agree on every wheel below `m` at tick `t`. -/
def Agree (a b : Nat → Nat → Bool) (m t : Nat) : Prop := ∀ j, j < m → a j t = b j t

/-- The error edge of `a` against `b` is at `m` at tick `t`. -/
def Edge (a b : Nat → Nat → Bool) (m t : Nat) : Prop := Agree a b m t ∧ a m t ≠ b m t

/-! ### The barrier: agreement below the edge is kept -/

theorem agree_step {a b : Nat → Nat → Bool} {m t : Nat} (ha : Recurrence a) (hb : Recurrence b)
    (h : Agree a b m t) : Agree a b m (t + 1) := by
  intro j hj
  match j, hj with
  | 0, hj => rw [ha.1, hb.1, h 0 hj]
  | 1, hj => rw [ha.2.1, hb.2.1, h 0 (by omega), h 1 hj]
  | k + 2, hj => rw [ha.2.2, hb.2.2, h k (by omega), h (k + 1) (by omega), h (k + 2) hj]

theorem agree_after {a b : Nat → Nat → Bool} {m t : Nat} (ha : Recurrence a) (hb : Recurrence b)
    (h : Agree a b m t) (n : Nat) : Agree a b m (t + n) := by
  induction n with
  | zero => exact h
  | succ n ih => exact agree_step ha hb ih

/-- The edge never retreats. -/
theorem edge_le {a b : Nat → Nat → Bool} {m m' t n : Nat} (ha : Recurrence a) (hb : Recurrence b)
    (h : Edge a b m t) (h' : Edge a b m' (t + n)) : m ≤ m' :=
  Nat.le_of_not_lt (fun hlt => h'.2 (agree_after ha hb h.1 n m' hlt))

/-! ### The heal criterion -/

private theorem heal_bool : ∀ (p x y s : Bool), x ≠ y →
    ((xor p (s || x) = xor p (s || y)) ↔ s = true) := by decide

private theorem heal0_bool : ∀ (s x y : Bool), x ≠ y → (((s || x) = (s || y)) ↔ s = true) := by decide

private theorem ne_bool : ∀ (x y : Bool), x ≠ y → y = !x := by decide

theorem heal_iff {a b : Nat → Nat → Bool} {m t : Nat} (ha : Recurrence a) (hb : Recurrence b)
    (h : Edge a b (m + 1) t) : (a (m + 1) (t + 1) = b (m + 1) (t + 1)) ↔ a m t = true := by
  match m, h with
  | 0, h =>
    rw [ha.2.1, hb.2.1, ← h.1 0 (by omega)]
    exact heal0_bool _ _ _ h.2
  | k + 1, h =>
    rw [ha.2.2, hb.2.2, ← h.1 k (by omega), ← h.1 (k + 1) (by omega)]
    exact heal_bool _ _ _ _ h.2

theorem edge_stall {a b : Nat → Nat → Bool} {m t : Nat} (ha : Recurrence a) (hb : Recurrence b)
    (h : Edge a b (m + 1) t) (hw : a m t = false) : Edge a b (m + 1) (t + 1) :=
  ⟨agree_step ha hb h.1, fun e => by have := (heal_iff ha hb h).1 e; rw [hw] at this; exact Bool.false_ne_true this⟩

theorem edge_heal {a b : Nat → Nat → Bool} {m t : Nat} (ha : Recurrence a) (hb : Recurrence b)
    (h : Edge a b (m + 1) t) (hk : a m t = true) : Agree a b (m + 2) (t + 1) := by
  intro j hj
  by_cases hj' : j < m + 1
  · exact agree_step ha hb h.1 j hj'
  · have : j = m + 1 := by omega
    subst this
    exact (heal_iff ha hb h).2 hk

/-! ### After a heal: the wheels above the old edge -/

private theorem white_above_bool : ∀ (x2 x3 y3 : Bool),
    xor true (x2 || x3) = xor true (!x2 || y3) → xor true (x2 || x3) = false := by decide

private theorem black_two_above_bool : ∀ (x2 x3 y3 x4 y4 : Bool),
    xor true (x2 || x3) = xor true (!x2 || y3) →
    xor x2 (x3 || x4) = xor (!x2) (y3 || y4) → xor x2 (x3 || x4) = true := by decide

/-- The two arrays' values at the window above an edge at `m + 2`, with the parent `m + 1` black. -/
private theorem window {a b : Nat → Nat → Bool} {m t : Nat} (h : Edge a b (m + 2) t) (hk : a (m + 1) t = true) :
    b m t = a m t ∧ b (m + 1) t = true ∧ b (m + 2) t = !a (m + 2) t := by
  exact ⟨(h.1 m (by omega)).symm, by rw [← h.1 (m + 1) (by omega)]; exact hk, ne_bool _ _ h.2⟩

theorem white_above {a b : Nat → Nat → Bool} {m t : Nat} (ha : Recurrence a) (hb : Recurrence b)
    (h : Edge a b (m + 2) t) (hk : a (m + 1) t = true) (h3 : a (m + 3) (t + 1) = b (m + 3) (t + 1)) :
    a (m + 3) (t + 1) = false := by
  obtain ⟨-, hb1, hb2⟩ := window h hk
  rw [ha.2.2] at h3 ⊢; rw [hb.2.2, hb1, hb2] at h3; rw [hk] at h3 ⊢
  exact white_above_bool _ _ _ h3

theorem black_two_above {a b : Nat → Nat → Bool} {m t : Nat} (ha : Recurrence a) (hb : Recurrence b)
    (h : Edge a b (m + 2) t) (hk : a (m + 1) t = true) (h3 : a (m + 3) (t + 1) = b (m + 3) (t + 1))
    (h4 : a (m + 4) (t + 1) = b (m + 4) (t + 1)) : a (m + 4) (t + 1) = true := by
  obtain ⟨-, hb1, hb2⟩ := window h hk
  rw [ha.2.2] at h3 h4 ⊢; rw [hb.2.2, hb1, hb2] at h3; rw [hb.2.2, hb2] at h4; rw [hk] at h3
  exact black_two_above_bool _ _ _ _ _ h3 h4

/-! ### The jumps -/

/-- After a jump of exactly 2 the new parent is white. -/
theorem jump_two {a b : Nat → Nat → Bool} {m t : Nat} (ha : Recurrence a) (hb : Recurrence b)
    (h : Edge a b (m + 2) t) (hk : a (m + 1) t = true) (h' : Edge a b (m + 4) (t + 1)) :
    a (m + 3) (t + 1) = false :=
  white_above ha hb h hk (h'.1 (m + 3) (by omega))

/-- After a jump of exactly 3 the new parent is black. -/
theorem jump_three {a b : Nat → Nat → Bool} {m t : Nat} (ha : Recurrence a) (hb : Recurrence b)
    (h : Edge a b (m + 2) t) (hk : a (m + 1) t = true) (h' : Edge a b (m + 5) (t + 1)) :
    a (m + 4) (t + 1) = true :=
  black_two_above ha hb h hk (h'.1 (m + 3) (by omega)) (h'.1 (m + 4) (by omega))

/-- After a jump of exactly 4 the new parent is black one tick later, whatever it was. -/
theorem jump_four {a b : Nat → Nat → Bool} {m t : Nat} (ha : Recurrence a) (hb : Recurrence b)
    (h : Edge a b (m + 2) t) (hk : a (m + 1) t = true) (h' : Edge a b (m + 6) (t + 1)) :
    a (m + 5) (t + 2) = true := by
  have w := white_above ha hb h hk (h'.1 (m + 3) (by omega))
  have k := black_two_above ha hb h hk (h'.1 (m + 3) (by omega)) (h'.1 (m + 4) (by omega))
  rw [show t + 2 = (t + 1) + 1 from rfl, ha.2.2, w, k]
  rfl

private theorem jump_five_bool : ∀ (x2 x3 y3 x4 y4 x5 y5 x6 y6 : Bool),
    xor true (x2 || x3) = xor true (!x2 || y3) →
    xor x2 (x3 || x4) = xor (!x2) (y3 || y4) →
    xor x3 (x4 || x5) = xor y3 (y4 || y5) →
    xor x4 (x5 || x6) = xor y4 (y5 || y6) →
    xor x4 (x5 || x6) = false →
    xor (xor x2 (x3 || x4)) (xor x3 (x4 || x5) || xor x4 (x5 || x6)) = true := by decide

/-- After a jump of exactly 5 whose new parent is white, the new parent is black one tick later. -/
theorem jump_five {a b : Nat → Nat → Bool} {m t : Nat} (ha : Recurrence a) (hb : Recurrence b)
    (h : Edge a b (m + 2) t) (hk : a (m + 1) t = true) (h' : Edge a b (m + 7) (t + 1))
    (hw : a (m + 6) (t + 1) = false) : a (m + 6) (t + 2) = true := by
  obtain ⟨-, hb1, hb2⟩ := window h hk
  have h3 := h'.1 (m + 3) (by omega); have h4 := h'.1 (m + 4) (by omega)
  have h5 := h'.1 (m + 5) (by omega); have h6 := h'.1 (m + 6) (by omega)
  rw [show t + 2 = (t + 1) + 1 from rfl, ha.2.2, ha.2.2, ha.2.2, ha.2.2]
  rw [ha.2.2, hb.2.2, hb1, hb2, hk] at h3; rw [ha.2.2, hb.2.2, hb2] at h4
  rw [ha.2.2, hb.2.2] at h5; rw [ha.2.2, hb.2.2] at h6; rw [ha.2.2] at hw
  exact jump_five_bool _ _ _ _ _ _ _ _ _ h3 h4 h5 h6 hw

private theorem jump_six_bool : ∀ (x2 x3 y3 x4 y4 x5 y5 x6 y6 x7 y7 : Bool),
    xor true (x2 || x3) = xor true (!x2 || y3) →
    xor x2 (x3 || x4) = xor (!x2) (y3 || y4) →
    xor x3 (x4 || x5) = xor y3 (y4 || y5) →
    xor x4 (x5 || x6) = xor y4 (y5 || y6) →
    xor x5 (x6 || x7) = xor y5 (y6 || y7) →
    xor x5 (x6 || x7) = false →
    xor (xor x3 (x4 || x5)) (xor x4 (x5 || x6) || xor x5 (x6 || x7)) = false := by decide

/-- After a jump of exactly 6 whose new parent is white, the new parent is white one tick later. -/
theorem jump_six {a b : Nat → Nat → Bool} {m t : Nat} (ha : Recurrence a) (hb : Recurrence b)
    (h : Edge a b (m + 2) t) (hk : a (m + 1) t = true) (h' : Edge a b (m + 8) (t + 1))
    (hw : a (m + 7) (t + 1) = false) : a (m + 7) (t + 2) = false := by
  obtain ⟨-, hb1, hb2⟩ := window h hk
  have h3 := h'.1 (m + 3) (by omega); have h4 := h'.1 (m + 4) (by omega)
  have h5 := h'.1 (m + 5) (by omega); have h6 := h'.1 (m + 6) (by omega); have h7 := h'.1 (m + 7) (by omega)
  rw [show t + 2 = (t + 1) + 1 from rfl, ha.2.2, ha.2.2, ha.2.2, ha.2.2]
  rw [ha.2.2, hb.2.2, hb1, hb2, hk] at h3; rw [ha.2.2, hb.2.2, hb2] at h4
  rw [ha.2.2, hb.2.2] at h5; rw [ha.2.2, hb.2.2] at h6; rw [ha.2.2, hb.2.2] at h7; rw [ha.2.2] at hw
  exact jump_six_bool _ _ _ _ _ _ _ _ _ _ _ h3 h4 h5 h6 h7 hw

private theorem jump_seven_bool : ∀ (x2 x3 y3 x4 y4 x5 y5 x6 y6 x7 y7 x8 y8 : Bool),
    xor true (x2 || x3) = xor true (!x2 || y3) →
    xor x2 (x3 || x4) = xor (!x2) (y3 || y4) →
    xor x3 (x4 || x5) = xor y3 (y4 || y5) →
    xor x4 (x5 || x6) = xor y4 (y5 || y6) →
    xor x5 (x6 || x7) = xor y5 (y6 || y7) →
    xor x6 (x7 || x8) = xor y6 (y7 || y8) →
    xor x6 (x7 || x8) = false →
    xor (xor x4 (x5 || x6)) (xor x5 (x6 || x7) || xor x6 (x7 || x8)) = false := by decide

/-- After a jump of exactly 7 whose new parent is white, the new parent is white one tick later. -/
theorem jump_seven {a b : Nat → Nat → Bool} {m t : Nat} (ha : Recurrence a) (hb : Recurrence b)
    (h : Edge a b (m + 2) t) (hk : a (m + 1) t = true) (h' : Edge a b (m + 9) (t + 1))
    (hw : a (m + 8) (t + 1) = false) : a (m + 8) (t + 2) = false := by
  obtain ⟨-, hb1, hb2⟩ := window h hk
  have h3 := h'.1 (m + 3) (by omega); have h4 := h'.1 (m + 4) (by omega)
  have h5 := h'.1 (m + 5) (by omega); have h6 := h'.1 (m + 6) (by omega)
  have h7 := h'.1 (m + 7) (by omega); have h8 := h'.1 (m + 8) (by omega)
  rw [show t + 2 = (t + 1) + 1 from rfl, ha.2.2, ha.2.2, ha.2.2, ha.2.2]
  rw [ha.2.2, hb.2.2, hb1, hb2, hk] at h3; rw [ha.2.2, hb.2.2, hb2] at h4
  rw [ha.2.2, hb.2.2] at h5; rw [ha.2.2, hb.2.2] at h6; rw [ha.2.2, hb.2.2] at h7; rw [ha.2.2, hb.2.2] at h8
  rw [ha.2.2] at hw
  exact jump_seven_bool _ _ _ _ _ _ _ _ _ _ _ _ _ h3 h4 h5 h6 h7 h8 hw

end Ruliology.CellularAutomata.Rule30ErrorEdge

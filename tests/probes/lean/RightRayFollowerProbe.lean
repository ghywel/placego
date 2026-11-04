import RightRayProbe

/-! A delayed existential test on finite high completions of a fixed cut.
The lower part of the row may be arbitrary. For an ordinary anchored
register its negative depths are white. -/

namespace RightRayFollowerProbe

open RightRayWhiteCone RightRayProbe

def HighFinite (y : Row) : Prop := ∃ c : Int, ∀ i, c ≤ i → y i = false

def DelayedWhite (x : Row) (d : Int) (wait : Nat) (p : Nat → Int) (T : Nat) : Prop :=
  ∃ y, AgreesBelow x y d ∧ HighFinite y ∧ ∀ s, s ≤ T → orbit y (wait+s) (p s) = false

theorem agreed_orbit {x y : Row} {d : Int} (h : AgreesBelow x y d) (t : Nat) :
    AgreesBelow (orbit x t) (orbit y t) d := by
  induction t with
  | zero => exact h
  | succ t ih =>
    intro i hi
    simp only [orbit, ih i hi, ih (i-1) (by omega), ih (i-2) (by omega)]

private theorem xor_common (a b c : Bool) : xor (xor a c) (xor b c) = xor a b := by
  cases a <;> cases b <;> cases c <;> rfl

private theorem spot_xor {x y : Row} {d : Int} (h : AgreesBelow x y d) (t : Nat) :
    xor (orbit x t d) (orbit y t d) = xor (x d) (y d) := by
  induction t with
  | zero => rfl
  | succ t ih =>
    have e := agreed_orbit h t
    simp only [orbit, e (d-1) (by omega), e (d-2) (by omega), xor_common, ih]

private theorem match_target {u v b g : Bool}
    (h : xor u v = xor b (xor b (xor u g))) : v = g := by
  cases u <;> cases v <;> cases b <;> cases g <;> simp_all

/-- At the end of a prescribed wait, any finite high window can be installed
without changing a single lower bit of the starting row. The new start has
a finite high tail. -/
theorem place_window (x goal : Row) (d : Int) (wait : Nat)
    (hgoal : AgreesBelow (orbit x wait) goal d) : ∀ m : Nat,
    ∃ z, AgreesBelow x z d ∧ (∀ i, d+(m : Int) ≤ i → z i = false) ∧
      AgreesBelow goal (orbit z wait) (d+(m : Int)) := by
  intro m
  induction m with
  | zero =>
    let z : Row := fun i => if i < d then x i else false
    have hz : AgreesBelow x z d := fun i hi => by simp [z, hi]
    refine ⟨z, hz, ?_, ?_⟩
    · intro i hi
      have hh : ¬i<d := by omega
      simp [z, hh]
    · intro i hi
      exact ((agreed_orbit hz wait) i (by omega)).trans ((hgoal i (by omega)).symm)
  | succ m ih =>
    obtain ⟨z, hz, hzfinite, old⟩ := ih
    let k := d+(m : Int)
    let z' : Row := fun i => if i = k then xor (z k) (xor (orbit z wait k) (goal k)) else z i
    have hz' : AgreesBelow z z' k := by
      intro i hi
      have hh : i ≠ k := by omega
      simp [z', hh]
    have found : orbit z' wait k = goal k := by
      apply match_target (u := orbit z wait k) (b := z k)
      simpa only [z', if_pos rfl] using spot_xor hz' wait
    refine ⟨z', ?_, ?_, ?_⟩
    · intro i hi
      exact (hz' i (by dsimp [k]; omega)).trans (hz i hi)
    · intro i hi
      have hh : i ≠ k := by dsimp [k]; omega
      simp [z', hh, hzfinite i (by omega)]
    · intro i hi
      by_cases he : i = k
      · subst i
        exact found
      · have hlow : i < k := by dsimp [k] at *; omega
        exact ((agreed_orbit hz' wait) i hlow).trans (old i hlow)

private theorem delayed_test (x : Row) (d lo hi : Int) (wait : Nat) (p : Nat → Int)
    (T : Nat) (hd : d-1 ≤ hi)
    (detect : ∀ y, (∀ s, s ≤ T → orbit y (wait+s) (p s) = false) ↔
      White (orbit y wait) lo hi) :
    DelayedWhite x d wait p T ↔ White (orbit x wait) lo (d-1) := by
  constructor
  · rintro ⟨y, hy, _, hobs⟩ i hlo hhi
    rw [← (agreed_orbit hy wait) i (by omega)]
    exact (detect y).mp hobs i hlo (by omega)
  · intro h
    let goal : Row := fun i => if i < d then orbit x wait i else false
    have hg : AgreesBelow (orbit x wait) goal d := fun i hi => by simp [goal,hi]
    let m := (hi+1-d).toNat
    have hm : d + (m : Int) = hi+1 := by dsimp [m]; omega
    obtain ⟨z,hz,hfin,hmatch⟩ := place_window x goal d wait hg m
    refine ⟨z,hz,⟨d+(m : Int),hfin⟩,(detect z).mpr ?_⟩
    intro i hlo hhi
    rw [hmatch i (by omega)]
    by_cases hh : i < d
    · simpa [goal,hh] using h i hlo (by omega)
    · simp [goal,hh]

/-- Even-start query reading either the top fixed bit or the OR of the top two. -/
theorem even_follower_probe (x : Row) (d : Int) (k m : Nat) (hk : 1 ≤ k ∧ k ≤ 2) (hm : 0 < m) :
    DelayedWhite x d (2*(3*m-k-1)) (ray (d+((3*m-k-1 : Nat) : Int)) 0) (2*m-1) ↔
      White (orbit x (2*(3*m-k-1))) (d-(k : Int)) (d-1) := by
  let n := d+((3*m-k-1 : Nat) : Int)
  let wait := 2*(3*m-k-1)
  apply delayed_test x d (d-(k : Int)) (n+(m : Int)-1) wait (ray n 0) (2*m-1) (by dsimp [n]; omega)
  intro y
  have ht := even_white_iff (orbit y) (orbit_step y) wait n m hm
  rwa [show n-3*(m : Int)+1 = d-(k : Int) by dsimp [n]; omega] at ht

/-- Odd-start query provides the complementary temporal phase. -/
theorem odd_follower_probe (x : Row) (d : Int) (k m : Nat) (hk : 1 ≤ k ∧ k ≤ 2) (hm : 0 < m) :
    DelayedWhite x d (2*(3*m-k)+1) (ray (d+((3*m-k : Nat) : Int)) 1) (2*m) ↔
      White (orbit x (2*(3*m-k)+1)) (d-(k : Int)) (d-1) := by
  let n := d+((3*m-k : Nat) : Int)
  let wait := 2*(3*m-k)+1
  apply delayed_test x d (d-(k : Int)) (n+(m : Int)) wait (ray n 1) (2*m) (by dsimp [n]; omega)
  intro y
  have ht := odd_white_iff (orbit y) (orbit_step y) wait n m hm
  rwa [show n-3*(m : Int) = d-(k : Int) by dsimp [n]; omega] at ht

end RightRayFollowerProbe

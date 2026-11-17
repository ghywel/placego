import WhiteParentPin

namespace WhiteParentPin

/-- From an actual first difference, a first difference at the same wheel m ticks
later says exactly that its parent stayed white throughout the intervening updates. -/
theorem finite_stay_iff {a y : Nat → Row} (ha : Runs wall a) (hy : Runs wall y)
    {T n m : Nat} (h : First (n+1) (a T) (y T)) :
    First (n+1) (a (T+m)) (y (T+m)) ↔ ∀ i, i < m → a (T+i) n = false := by
  constructor
  · intro last
    have along (i : Nat) (hi : i ≤ m) : First (n+1) (a (T+i)) (y (T+i)) := by
      have low := propagate wall_causal ha hy h.1 i
      refine ⟨low, ?_⟩
      intro he
      have eq := propagate wall_causal ha hy (agree_succ low he) (m-i) (n+1) (by omega)
      rw [show T+i+(m-i)=T+m by omega] at eq
      exact last.2 eq
    intro i hi
    apply (stays_iff (along i (by omega))).mp
    rw [← ha (T+i), ← hy (T+i)]
    exact along (i+1) (by omega)
  · intro white
    have along (i : Nat) (hi : i ≤ m) : First (n+1) (a (T+i)) (y (T+i)) := by
      induction i with
      | zero => exact h
      | succ i ih =>
        change First (n+1) (a ((T+i)+1)) (y ((T+i)+1))
        rw [ha, hy]
        exact (stays_iff (ih (by omega))).mpr (white i (by omega))
    exact along m (by omega)

/-- If every competing parent must turn black before the deadline, a second hit
at that deadline selects permanent pinning. The competing-parent premise is explicit. -/
theorem short_pin {a y : Nat → Row} (ha : Runs wall a) (hy : Runs wall y)
    {T n m : Nat} (h : First (n+1) (a T) (y T))
    (last : First (n+1) (a (T+m)) (y (T+m)))
    (alternatives : (∀ i, a (T+i) n = false) ∨ ∃ i, i < m ∧ a (T+i) n = true) :
    ∀ i, First (n+1) (a (T+i)) (y (T+i)) := by
  apply (permanent_pin_iff ha hy h).mpr
  rcases alternatives with white | ⟨i,hi,black⟩
  · exact white
  · have contra := (finite_stay_iff ha hy h).mp last i hi
    simp [black] at contra

/-- The three terminal parent words and the two-wheel codes are imported finite
data. The checks below evaluate ordinary Lean definitions in the kernel. -/
def delay (word phase : Nat) : Nat :=
  1 + ((List.range 16).find? (fun h => word.testBit ((phase+h)%16))).getD 16

def gate (r : Nat) : Nat := max (delay 38128 r) (max (delay 7367 r) (delay 62161 r))

theorem sixteen_deadlines : (List.range 16).map gate =
    [5,4,3,4,3,2,1,1,3,2,3,2,1,4,3,2] := by decide

def codeAt (u v r : Nat) : Bool × Bool := (u.testBit r, v.testBit r)

theorem two_adjacent_wheels : ∀ r : Fin 16,
    codeAt 40171 25373 r ≠ codeAt 25877 40388 r ∧
    codeAt 40171 25373 r ≠ codeAt 851 1770 r := by decide

#print axioms finite_stay_iff
#print axioms short_pin
#print axioms sixteen_deadlines
#print axioms two_adjacent_wheels
end WhiteParentPin

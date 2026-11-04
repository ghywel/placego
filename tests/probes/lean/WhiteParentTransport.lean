import WhiteParentPin

namespace WhiteParentPin

/-- A black last common wheel writes one more common wheel on the next update. -/
theorem advance_one {x y : Row} {k : Nat} (h : Agree (k+1) x y) (black : x k = true) :
    Agree (k+2) (wall x) (wall y) := by
  by_cases he : x (k+1) = y (k+1)
  · exact wall_causal (agree_succ h he)
  · exact agree_succ (wall_causal h) ((heals_iff (show First (k+1) x y from ⟨h,he⟩)).mpr black)

/-- A single reference-side reset path works simultaneously for every completion
of the fixed initial prefix. No assumption is made about the unused higher bits. -/
theorem reset_path {a y : Nat → Row} (ha : Runs wall a) (hy : Runs wall y)
    {T : Nat} (z : Nat → Nat) (initial : Agree (z 0+1) (a 0) (y 0))
    (path : ∀ t, t < T → z (t+1) = z t ∨ (z (t+1) = z t+1 ∧ a t (z t) = true)) :
    ∀ t, t ≤ T → Agree (z t+1) (a t) (y t) := by
  intro t ht
  induction t with
  | zero => exact initial
  | succ t ih =>
    have prev := ih (by omega)
    rw [ha t, hy t]
    rcases path t (by omega) with stay | ⟨inc,black⟩
    · rw [stay]
      exact wall_causal prev
    · rw [inc]
      exact advance_one prev black

#print axioms advance_one
#print axioms reset_path
end WhiteParentPin

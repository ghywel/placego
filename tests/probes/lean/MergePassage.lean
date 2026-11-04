import WhiteParentTransport

namespace WhiteParentPin

/-- Bits beyond a common prefix ending in 010 disappear from the first two
new wheels in two updates. The second new wheel is actually white. -/
theorem double010 {x y : Row} {k : Nat} (low : Agree (k+3) x y)
    (b : x k = false) (c : x (k+1) = true) (d : x (k+2) = false) :
    Agree (k+5) (wall (wall x)) (wall (wall y)) := by
  have black : wall x (k+2) = true := by simp [wall,b,c,d]
  have first := advance_one (k:=k+2) (wall_causal low) black
  have zero (v : Row) (h : v k=false) (g : v (k+1)=true) (l : v (k+2)=false) :
      wall (wall v) (k+4) = false := by
    change xor (xor (v k) (v (k+1) || v (k+2)))
      ((xor (v (k+1)) (v (k+2) || v (k+3))) ||
       (xor (v (k+2)) (v (k+3) || v (k+4)))) = false
    cases e : v (k+3) <;> simp [h,g,l,e]
  apply agree_succ first
  rw [zero x b c d, zero y ((low k (by omega)).symm.trans b)
    ((low (k+1) (by omega)).symm.trans c) ((low (k+2) (by omega)).symm.trans d)]

/-- One reference path certifies all completions with the given initial agreement. -/
inductive ResetTiles (a : Nat → Row) (start : Nat) : Nat → Nat → Prop where
  | initial : ResetTiles a start 0 start
  | stay {t z} : ResetTiles a start t z → ResetTiles a start (t+1) z
  | single {t z} : ResetTiles a start t z → a t z = true → ResetTiles a start (t+1) (z+1)
  | pair {t k} : ResetTiles a start t (k+2) →
      a t k = false → a t (k+1) = true → a t (k+2) = false → ResetTiles a start (t+2) (k+4)

theorem tiles_sound {a y : Nat → Row} (ha : Runs wall a) (hy : Runs wall y)
    {start t z : Nat} (initial : Agree (start+1) (a 0) (y 0)) (p : ResetTiles a start t z) :
    Agree (z+1) (a t) (y t) := by
  induction p with
  | initial => exact initial
  | stay p ih => rw [ha,hy]; exact wall_causal ih
  | single p black ih => rw [ha,hy]; exact advance_one ih black
  | @pair t k p b c d ih =>
    change Agree (k+5) (a ((t+1)+1)) (y ((t+1)+1))
    rw [ha (t+1),hy (t+1),ha t,hy t]
    exact double010 ih b c d

/-- Hit uses an inclusive wheel index. -/
def Hit (a y : Nat → Row) (k t : Nat) : Prop :=
  Agree (k+1) (a t) (y t) ∧ ∀ s, s<t → ¬Agree (k+1) (a s) (y s)

theorem passage_inherit {a y : Nat → Row} {n s : Nat} (h : Hit a y n s)
    (same : a s (n+1)=y s (n+1)) : Hit a y (n+1) s := by
  refine ⟨agree_succ h.1 same, ?_⟩
  intro v hv e
  exact h.2 v hv (fun k hk => e k (by omega))

theorem passage_after_black {a y : Nat → Row} (ha : Runs wall a) (hy : Runs wall y)
    {n s m : Nat} (h : Hit a y n s) (diff : a s (n+1) ≠ y s (n+1))
    (white : ∀ d, d<m → a (s+d) n = false) (black : a (s+m) n = true) :
    Hit a y (n+1) (s+m+1) := by
  have f := first_black ha hy (show First (n+1) (a s) (y s) from ⟨h.1,diff⟩) white black
  refine ⟨f.2, ?_⟩
  intro v hv e
  by_cases before : v<s
  · exact h.2 v before (fun k hk => e k (by omega))
  · have z := f.1 (v-s) (by omega)
    rw [show s+(v-s)=v by omega] at z
    exact z.2 (e (n+1) (by omega))

#print axioms double010
#print axioms tiles_sound
#print axioms passage_inherit
#print axioms passage_after_black
end WhiteParentPin

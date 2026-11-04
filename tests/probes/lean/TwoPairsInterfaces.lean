import TwoPairs

/-! Read the OR driving a digit by comparing that digit at successive times.
At the original cut one more observed digit resolves the exceptional alternating
prefixes, even when their starting phases differ. The V-only law is a hypothesis. -/
namespace TwoPairsInterfaces
open TwoPairs

private theorem drive_eq {x y : Row} (k : Nat) (t : Nat)
    (a : iter x t (k+2) = iter y t (k+2))
    (b : iter x (t+1) (k+2) = iter y (t+1) (k+2)) :
    drive k x t = drive k y t := by
  change xor (iter x t (k+2)) (drive k x t) =
    xor (iter y t (k+2)) (drive k y t) at b
  rw [a] at b
  cases h : iter y t (k+2) <;> simp_all

private theorem rain_or {x : Row} {w : Nat} (hx : x 0 = true) (hr : RainTo w x)
    (j : Nat) (hj : j+1 < w) : (x (j+1) || x j) = true := by
  cases j with
  | zero => simp [hx]
  | succ j => rw [hr (j+1) (by omega) hj]; cases x (j+1) <;> rfl

private theorem top_flip {x : Row} (k : Nat) (hx : x 0 = true) (hr : RainTo (k+2) x) :
    step x (k+1) = !x (k+1) := by
  cases k with
  | zero => rw [step_one,hx]; cases x 1 <;> rfl
  | succ k => rw [step_add, rain_or hx hr k (by omega)]; cases x (k+2) <;> rfl

private theorem rain_agree {x y : Row} (hx : x 0 = true) (hy : y 0 = true) :
    ∀ k, RainTo (k+2) x → RainTo (k+2) y → x (k+1) = y (k+1) → Agree (k+2) x y := by
  intro k
  induction k with
  | zero =>
    intro _ _ top j hj
    have z : j=0 ∨ j=1 := by omega
    rcases z with rfl | rfl
    · exact hx.trans hy.symm
    · exact top
  | succ k ih =>
    intro rx ry top
    have lower : x (k+1) = y (k+1) := by
      rw [rx (k+1) (by omega) (by omega), ry (k+1) (by omega) (by omega)] at top
      simpa using top
    have rest := ih (fun j hj h => rx j hj (by omega)) (fun j hj h => ry j hj (by omega)) lower
    intro j hj
    by_cases h : j < k+2
    · exact rest j h
    · have e : j=k+2 := by omega
      exact e ▸ top

/-- Only the first three samples of the second observed digit are needed at this width. -/
theorem recover_short (k : Nat) (law : Law k) {x y : Row} (hx : x 0 = true) (hy : y 0 = true)
    (h₀ : ∀ t, iter x t (k+2) = iter y t (k+2))
    (h₁ : ∀ t, t≤2 → iter x t (k+3) = iter y t (k+3)) : Agree (k+2) x y := by
  have drive_same : ∀ t, drive k x t = drive k y t :=
    fun t => drive_eq k t (h₀ t) (h₀ (t+1))
  rcases law x y hx hy drive_same with same | ⟨rx,ry⟩
  · exact same
  · apply rain_agree hx hy k rx ry
    have mask (t : Nat) (ht : t < 2) := drive_eq (x:=x) (y:=y) (k+1) t
      (h₁ t (by omega)) (h₁ (t+1) (by omega))
    have a : x (k+2) = y (k+2) := h₀ 0
    cases at_cut : x (k+2) with
    | false =>
      have b := mask 0 (by omega)
      change (x (k+2) || x (k+1)) = (y (k+2) || y (k+1)) at b
      simpa [at_cut,← a] using b
    | true =>
      have white : step x (k+2) = false := by
        rw [step_add, at_cut, rain_or hx rx k (by omega)]; rfl
      have white' : step y (k+2) = false := (h₀ 1).symm.trans white
      have b := mask 1 (by omega)
      change (step x (k+2) || step x (k+1)) = (step y (k+2) || step y (k+1)) at b
      rw [white,white',top_flip k hx rx,top_flip k hy ry] at b
      simpa using b

theorem recover (k : Nat) (law : Law k) {x y : Row} (hx : x 0 = true) (hy : y 0 = true)
    (h₀ : ∀ t, iter x t (k+2) = iter y t (k+2))
    (h₁ : ∀ t, iter x t (k+3) = iter y t (k+3)) : Agree (k+2) x y :=
  recover_short k law hx hy h₀ (fun t _ => h₁ t)

/-- A common driver return P needs readings at 0 through P on the first interface
and only ticks 0,1,2 on the second. Periodicity is needed only for the two drivers. -/
theorem recover_by (k P : Nat) (law : Law k) (hp : 0<P) {x y : Row}
    (hx : x 0 = true) (hy : y 0 = true)
    (px : ∀ t, drive k x t = drive k x (t%P)) (py : ∀ t, drive k y t = drive k y (t%P))
    (first : ∀ t, t≤P → iter x t (k+2) = iter y t (k+2))
    (second : ∀ t, t≤2 → iter x t (k+3) = iter y t (k+3)) : Agree (k+2) x y := by
  have drivers (t : Nat) : drive k x t = drive k y t := by
    rw [px t, py t]
    have small := Nat.mod_lt t hp
    exact drive_eq k _ (first _ (by omega)) (first _ (by omega))
  apply recover_short k law hx hy _ second
  intro t
  induction t with
  | zero => exact first 0 (by omega)
  | succ t ih =>
    change xor (iter x t (k+2)) (drive k x t) = xor (iter y t (k+2)) (drive k y t)
    rw [ih, drivers t]

#print axioms recover_by

#print axioms recover_short
end TwoPairsInterfaces

import RightRayProbe
import RightRaySeedPhases

/-! Dyadic periodicity of the integer-indexed, right-edge register with white
negative depths. The bound is common to every strip ending below D, at every
phase and for every initial row whose negative part is white. -/

namespace RightRayPeriodBridge

open RightRayWhiteCone RightRayProbe

theorem left_white (x : Row) (hx : ∀ i : Int, i < 0 → x i = false) (t : Nat) :
    ∀ i : Int, i < 0 → orbit x t i = false := by
  induction t with
  | zero => exact hx
  | succ t ih =>
    intro i hi
    rw [orbit_step x t i, ih i hi, ih (i-1) (by omega), ih (i-2) (by omega)]
    rfl

theorem nat_bridge (x : Row) (hx : ∀ i : Int, i < 0 → x i = false) (t : Nat) :
    ∀ j : Nat, orbit x t (j : Int) = RightRayDelay.run (fun n : Nat => x (n : Int)) t j := by
  induction t with
  | zero => intro j; rfl
  | succ t ih =>
    intro j
    cases j with
    | zero =>
      rw [orbit_step x t, left_white x hx t (((0 : Nat) : Int)-1) (by omega),
        left_white x hx t (((0 : Nat) : Int)-2) (by omega)]
      exact congrArg (fun b => xor b false) (ih 0)
    | succ j =>
      cases j with
      | zero =>
        rw [orbit_step x t]
        rw [show ((1 : Nat) : Int)-1 = ((0 : Nat) : Int) by omega, left_white x hx t (((1 : Nat) : Int)-2) (by omega), ih 0, ih 1]
        simp [RightRayDelay.run, RightRayDelay.step, RightRayDelay.driver]
      | succ n =>
        rw [orbit_step x t]
        rw [show ((n+2 : Nat) : Int)-1 = ((n+1 : Nat) : Int) by omega,
          show ((n+2 : Nat) : Int)-2 = (n : Int) by omega,
          ih n, ih (n+1), ih (n+2)]
        rfl

private theorem bit_double {a b c : Bool} (h : (a = b ↔ b = c)) : a = c := by
  cases a <;> cases b <;> cases c <;> simp_all

/-- One explicit common period for all depths below D. -/
theorem prefix_dyadic (x : RightRayDelay.Row) (D : Nat) :
    RightRayDelay.Below (RightRayDelay.run x (2^D)) x D := by
  induction D with
  | zero => intro j hj; omega
  | succ D ih =>
    let p := 2^D
    have hp : RightRayDelay.Below (RightRayDelay.run x p) x D := ih
    have hlow : RightRayDelay.Below (RightRayDelay.run x (p+p)) (RightRayDelay.run x p) D := by
      rw [RightRayDelay.run_add]
      exact RightRayDelay.below_run hp p
    have hbit : RightRayDelay.run x (p+p) D = x D := by
      rw [RightRayDelay.run_add]
      exact bit_double (RightRayDelay.spot_iff hp p)
    have shift : 2^(D+1) = p+p := by simp [p,Nat.pow_succ,Nat.mul_two]
    rw [shift]
    intro j hj
    by_cases h : j < D
    · exact (hlow j h).trans (hp j h)
    · have he : j = D := by omega
      simpa only [he] using hbit

theorem low_period (x : Row) (hx : ∀ i : Int, i < 0 → x i = false)
    (D t : Nat) (i : Int) (hi : i < (D : Int)) :
    orbit x (t + 2^D) i = orbit x t i := by
  by_cases hn : i < 0
  · rw [left_white x hx _ i hn, left_white x hx _ i hn]
  · let j := i.toNat
    have hi' : i = (j : Int) := by dsimp [j]; omega
    rw [hi', nat_bridge x hx, nat_bridge x hx]
    rw [Nat.add_comm t,RightRayDelay.run_add]
    exact RightRayDelay.below_run (prefix_dyadic _ D) t j (by omega)

theorem white_period (x : Row) (hx : ∀ i : Int, i < 0 → x i = false)
    (D t : Nat) (lo hi : Int) (hle : hi < (D : Int)) :
    White (orbit x (t+2^D)) lo hi ↔ White (orbit x t) lo hi := by
  constructor
  · intro h i il ih
    rw [← low_period x hx D t i (by omega)]
    exact h i il ih
  · intro h i il ih
    rw [low_period x hx D t i (by omega)]
    exact h i il ih

end RightRayPeriodBridge

import Ruliology.CellularAutomata.Rule30Prize
import ArcRotationDraft
import ArcRule30BridgeDraft

/-!
# Normalized Rule30 finite-step rotation exclusion: explicit assembly candidate

UNCOMPILED/PROOF-SKETCH. Every hypothesis below is explicit; the result concerns the visible neighbour of an
already normalized alternating clock. It is not Problem1, an all-irrational exclusion, an arbitrary-endpoint
restart theorem or an assertion that every library StepFunction has our finite-step representation.
-/

namespace ArcRule30Exclusion

/-- A finite-left Rule30 clock cannot have this large-digit finite-step rotation as its visible neighbour. -/
theorem no_visible_rotation {r : Nat} (S : ArcStepCode.StepCode r) (alpha theta : ℝ)
    (ha : Irrational alpha)
    (hlarge : ∀ N : Nat, ∃ n : Nat, N ≤ n ∧
      ((2^(r+1) : Nat) : ℤ) < Rule30Equivalents.Lagrange.digit alpha (n+1))
    (x : Int → Bool) (L : Nat)
    (hleft : x (-(L : Int)) = true) (hzero : ∀ i : Int, i < -(L : Int) → x i = false)
    (hclock : ∀ t : Nat, Ruliology.CellularAutomata.Rule30Realization.evol x t 0 = decide (t % 2 = 1))
    (hvisible : ∀ s : Nat, ArcRule30Bridge.visible x s = ArcStepCode.orbit S alpha theta s) : False := by
  have hf : ArcRule30Bridge.visible x = ArcStepCode.orbit S alpha theta := funext hvisible
  apply ArcRotation.no_uniform_repeat_bound S alpha theta ha hlarge
  refine ⟨L,fun q hq => ?_⟩
  rw [← hf]
  exact ArcRule30Bridge.repeat_bound x L hleft hzero hclock q hq

#print axioms ArcRule30Exclusion.no_visible_rotation

end ArcRule30Exclusion

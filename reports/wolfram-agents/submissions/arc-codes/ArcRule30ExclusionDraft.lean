import Ruliology.CellularAutomata.Rule30Prize
import ArcRotationDraft
import ArcRule30BridgeDraft
import ArcTailBounds
import ArcEndpointDraft

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

/-- Finite endpoint exceptions are harmless once eventual agreement has been supplied.
    This does not assume an eventual physical clock: that clock is still normalized from time zero. -/
theorem no_eventual_visible_rotation {r : Nat} (S : ArcStepCode.StepCode r) (alpha theta : ℝ)
    (ha : Irrational alpha)
    (hlarge : ∀ N : Nat, ∃ n : Nat, N ≤ n ∧
      ((2^(r+1) : Nat) : ℤ) < Rule30Equivalents.Lagrange.digit alpha (n+1))
    (x : Int → Bool) (L : Nat)
    (hleft : x (-(L : Int)) = true) (hzero : ∀ i : Int, i < -(L : Int) → x i = false)
    (hclock : ∀ t : Nat, Ruliology.CellularAutomata.Rule30Realization.evol x t 0 = decide (t % 2 = 1))
    (hvisible : ∃ N : Nat, ∀ s : Nat, N ≤ s →
      ArcRule30Bridge.visible x s = ArcStepCode.orbit S alpha theta s) : False := by
  obtain ⟨N,hN⟩ := hvisible
  apply ArcRotation.no_uniform_repeat_bound S alpha theta ha hlarge
  refine ⟨L+2*N,?_⟩
  exact ArcTailBounds.uniform_eventual_transfer (ArcRule30Bridge.visible x)
    (ArcStepCode.orbit S alpha theta) L N
    (fun q hq => ArcRule30Bridge.repeat_bound x L hleft hzero hclock q hq) hN

#print axioms ArcRule30Exclusion.no_eventual_visible_rotation

/-- Arbitrary changes at the listed endpoint translates cannot evade the same large-digit exclusion.
    A genuine StepCode is still supplied explicitly; no general interval representation is inferred. -/
theorem no_visible_endpoint_variant {r : Nat} (S : ArcStepCode.StepCode r) (g : ℝ → Bool)
    (alpha theta : ℝ) (ha : Irrational alpha)
    (hlarge : ∀ N : Nat, ∃ n : Nat, N ≤ n ∧
      ((2^(r+1) : Nat) : ℤ) < Rule30Equivalents.Lagrange.digit alpha (n+1))
    (hoff : ∀ y : ℝ, (∀ i : Nat, i < r → ∀ z : ℤ, y ≠ S.endpoint i+z) → g y = S.value y)
    (x : Int → Bool) (L : Nat)
    (hleft : x (-(L : Int)) = true) (hzero : ∀ i : Int, i < -(L : Int) → x i = false)
    (hclock : ∀ t : Nat, Ruliology.CellularAutomata.Rule30Realization.evol x t 0 = decide (t % 2 = 1))
    (hvisible : ∀ s : Nat, ArcRule30Bridge.visible x s = g (theta+(s : ℝ)*alpha)) : False := by
  obtain ⟨N,hN⟩ := ArcEndpoint.eventual_agreement S g alpha theta ha hoff
  apply no_eventual_visible_rotation S alpha theta ha hlarge x L hleft hzero hclock
  refine ⟨N,?_⟩
  intro s hs
  rw [hvisible s]
  exact hN s hs

#print axioms ArcRule30Exclusion.no_visible_endpoint_variant

end ArcRule30Exclusion

import RightRayWhiteCone

/-! Half-speed right-edge observations and the exact white test on a freely
extendible snapshot. All spatial indices are integers. Natural depth zero
can be anchored by taking the negative-depth bits white in the supplied row. -/

namespace RightRayProbe

open RightRayWhiteCone

/-- Depth n at the start. Phase 0 starts with a hold; phase 1 starts by advancing. -/
def ray (n : Int) (phase s : Nat) : Int := n + (((s + phase) / 2 : Nat) : Int)

theorem ray_causal (n : Int) (phase T : Nat) : Causal (ray n phase) T := by
  intro k _
  dsimp [ray]
  constructor <;> omega

/-- For m complete pairs starting on the even tick, all 2m observations see a
white cell iff the bottom row is white on these 4m−1 consecutive depths. -/
theorem even_white_iff (X : Nat → Row) (step : ∀ t, Step (X t) (X (t+1)))
    (t : Nat) (n : Int) (m : Nat) (hm : 0 < m) :
    (∀ s, s ≤ 2*m-1 → X (t+s) (ray n 0 s) = false) ↔
      White (X t) (n-3*(m : Int)+1) (n+(m : Int)-1) := by
  have hhold : ray n 0 ((2*m-2)+1) = ray n 0 (2*m-2) := by
    dsimp [ray]
    omega
  have h := white_path_iff X step t (2*m-2) (ray n 0) (ray_causal n 0 _) hhold
  rw [show (2*m-2)+1 = 2*m-1 by omega] at h
  have hend : ray n 0 (2*m-1) = n+(m : Int)-1 := by dsimp [ray]; omega
  rw [hend, show n+(m : Int)-1-2*((2*m-1 : Nat) : Int) = n-3*(m : Int)+1 by omega] at h
  exact h

/-- Starting on the odd tick, 2m+1 samples ending in a hold inspect 4m+1 depths. -/
theorem odd_white_iff (X : Nat → Row) (step : ∀ t, Step (X t) (X (t+1)))
    (t : Nat) (n : Int) (m : Nat) (hm : 0 < m) :
    (∀ s, s ≤ 2*m → X (t+s) (ray n 1 s) = false) ↔
      White (X t) (n-3*(m : Int)) (n+(m : Int)) := by
  have hhold : ray n 1 ((2*m-1)+1) = ray n 1 (2*m-1) := by
    dsimp [ray]
    omega
  have h := white_path_iff X step t (2*m-1) (ray n 1) (ray_causal n 1 _) hhold
  rw [show (2*m-1)+1 = 2*m by omega] at h
  have hend : ray n 1 (2*m) = n+(m : Int) := by dsimp [ray]; omega
  rw [hend, show n+(m : Int)-2*((2*m : Nat) : Int) = n-3*(m : Int) by omega] at h
  exact h

def orbit (x : Row) : Nat → Row
  | 0 => x
  | t+1 => fun i => xor (orbit x t i) (orbit x t (i-1) || orbit x t (i-2))

theorem orbit_step (x : Row) (t : Nat) : Step (orbit x t) (orbit x (t+1)) := fun _ => rfl

def AgreesBelow (x y : Row) (d : Int) : Prop := ∀ i, i < d → y i = x i

/-- Only the prescribed part of the bottom white interval can obstruct its realization. -/
theorem snapshot_test {x : Row} {lo d hi : Int} {P : Row → Prop} (hd : d-1 ≤ hi)
    (hP : ∀ y, P y ↔ White y lo hi) :
    (∃ y, AgreesBelow x y d ∧ P y) ↔ White x lo (d-1) := by
  constructor
  · rintro ⟨y, hy, h⟩ i hlo hhi
    rw [← hy i (by omega)]
    exact (hP y).mp h i hlo (by omega)
  · intro h
    let y : Row := fun i => if i < d then x i else false
    refine ⟨y, ?_, (hP y).mpr ?_⟩
    · intro i hi
      simp [y, hi]
    · intro i hlo _
      by_cases hi : i < d
      · simpa [y, hi] using h i hlo (by omega)
      · simp [y, hi]

theorem even_snapshot_test (x : Row) (d n : Int) (m : Nat) (hm : 0 < m)
    (hd : d-1 ≤ n+(m : Int)-1) :
    (∃ y, AgreesBelow x y d ∧ ∀ s, s ≤ 2*m-1 → orbit y s (ray n 0 s) = false) ↔
      White x (n-3*(m : Int)+1) (d-1) := by
  apply snapshot_test hd
  intro y
  simpa only [Nat.zero_add, show orbit y 0 = y by simp [orbit]] using even_white_iff (orbit y) (orbit_step y) 0 n m hm

theorem odd_snapshot_test (x : Row) (d n : Int) (m : Nat) (hm : 0 < m)
    (hd : d-1 ≤ n+(m : Int)) :
    (∃ y, AgreesBelow x y d ∧ ∀ s, s ≤ 2*m → orbit y s (ray n 1 s) = false) ↔
      White x (n-3*(m : Int)) (d-1) := by
  apply snapshot_test hd
  intro y
  simpa only [Nat.zero_add, show orbit y 0 = y by simp [orbit]] using odd_white_iff (orbit y) (orbit_step y) 0 n m hm

end RightRayProbe

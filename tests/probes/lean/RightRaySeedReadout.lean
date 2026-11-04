import RightRayRooted

/-! At depth 3m the actual singleton orbit reports a prefix return by a
length-2m white word on the half-speed observer. At the next first visit,
its output complements the new coordinate of that return at the cut. -/
namespace RightRaySeedReadout

open RightRayWhiteCone RightRayProbe RightRayRooted

def single (i : Int) : Bool := decide (i = 0)

private theorem exterior : ∀ i : Int, i<0 → single i=false := by
  intro i hi
  simp [single, show i ≠ 0 by omega]

private theorem single_nat : (fun n : Nat => single (n:Int)) = RightRayDelay.pulse 0 := by
  funext n
  by_cases h : n=0
  · simp [single,RightRayDelay.pulse,h]
  · simp [single,RightRayDelay.pulse,h]

private theorem single_bit (t j : Nat) :
    orbit single t (j:Int) = RightRayDelay.SeedPhases.phase t j := by
  rw [RightRayPeriodBridge.nat_bridge single exterior, single_nat]
  rfl

/-- s is the absolute launch phase. The cut occurs after 6m observer ticks. -/
def cut (s m : Nat) : Row := orbit single (s+6*m)

def sample (s m r : Nat) : Bool := read (orbit single s) (6*m+r)

theorem sample_eq (s m r : Nat) :
    sample s m r = orbit (cut s m) r (ray ((3*m:Nat):Int) 0 r) := by
  unfold sample
  rw [show 6*m+r = 2*(3*m)+r by omega,read_cut]
  have key : orbit (orbit single s) (2*(3*m)) = cut s m := by
    rw [← orbit_add single s (2*(3*m))]; unfold cut; rw [show s+2*(3*m)=s+6*m by omega]
  rw [key]

def Returned (s m : Nat) : Prop :=
  AgreesBelow single (cut s m) ((4*m:Nat):Int)

theorem block_iff_return (s m : Nat) (hm : 0<m) :
    (∀ r, r<2*m → sample s m r=false) ↔ Returned s m := by
  let y := cut s m
  have ew := even_white_iff (orbit y) (orbit_step y) 0 ((3*m:Nat):Int) m hm
  have guard₁ : ((3*m:Nat):Int)-3*(m:Int)+1 = 1 := by omega
  have guard₂ : ((3*m:Nat):Int)+(m:Int)-1 = ((4*m:Nat):Int)-1 := by omega
  have block : (∀ r, r<2*m → sample s m r=false) ↔ White y 1 (((4*m:Nat):Int)-1) := by
    rw [guard₁,guard₂] at ew
    constructor
    · intro h
      apply ew.mp
      intro r hr
      simpa only [Nat.zero_add, sample_eq] using h r (by omega)
    · intro h r hr
      rw [sample_eq]
      simpa only [Nat.zero_add] using ew.mpr h r (by omega)
  rw [block]
  constructor
  · intro hw i hi
    by_cases hn : i<0
    · exact (RightRayPeriodBridge.left_white single exterior _ i hn).trans (exterior _ hn).symm
    · by_cases hz : i=0
      · subst i
        exact (single_bit (s+6*m) 0).trans (RightRayDelay.SeedPhases.phase_seed _).1
      · change y i = single i
        rw [hw i (by omega) (by omega)]
        simp [single,hz]
  · intro h i hlo hhi
    change cut s m i = false
    rw [h i (by omega)]
    simp [single,show i ≠ 0 by omega]

private theorem opposite {a b : Bool} (h : (a=true ↔ b=false)) : (a=false ↔ b=true) := by
  cases a <;> cases b <;> simp_all

/-- Conditioned on the white block, the next record is white exactly when
the bit just above the returning prefix is black in the cut snapshot. -/
theorem next_record (s m : Nat) (hm : 0<m)
    (hblock : ∀ r, r<2*m → sample s m r=false) :
    sample s m (2*m)=false ↔ cut s m ((4*m:Nat):Int)=true := by
  have ret := (block_iff_return s m hm).mp hblock
  let y := cut s m
  have low : RightRayDelay.Below (fun n : Nat => y (n:Int)) (RightRayDelay.pulse 0) (4*m) := by
    rw [←single_nat]
    exact fun i hi => ret (i:Int) (by omega)
  have e := RightRayDelay.spot_iff low (2*m)
  have top : RightRayDelay.run (RightRayDelay.pulse 0) (2*m) (4*m)=true := by
    rw [show 4*m = 2*(2*m) by omega]
    exact (RightRayDelay.SeedPhases.head_bit _).1
  have zero : RightRayDelay.pulse 0 (4*m) = false := by
    simp [RightRayDelay.pulse,show 4*m ≠ 0 by omega]
  simp only [top,zero] at e
  have hy : ∀ i : Int, i<0 → y i=false := RightRayPeriodBridge.left_white single exterior _
  rw [sample_eq, show ray ((3*m:Nat):Int) 0 (2*m) = ((4*m:Nat):Int) by dsimp [ray]; omega,
    RightRayPeriodBridge.nat_bridge (cut s m) hy]
  exact opposite e

#print axioms block_iff_return
#print axioms next_record
end RightRaySeedReadout

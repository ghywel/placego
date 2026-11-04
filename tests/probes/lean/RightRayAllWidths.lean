import RightRaySeedReadoutDoubles

/-! A half-speed observer launched on the actual singleton sees a return of
any prefix of width at least four. At odd widths the last white cone leaves
coordinate one uncovered. The singleton identity at coordinates one and two
(the kit's `Rule30RightPeriods.R_two_eq_one`) supplies it. -/

namespace RightRayAllWidths
open RightRayWhiteCone RightRayProbe RightRayRooted RightRayFollowerProbe
open RightRaySeedReadout (single)
open RightRaySeedReadoutDoubles (Returns)

def windowStart (J : Nat) : Nat := 2*J - J/2

def cut (s J : Nat) : Row := orbit single (s + windowStart J)

def sample (s J r : Nat) : Bool := read (orbit single s) (windowStart J + r)

def whiteBlock (s J : Nat) : Prop := ∀ r, r < J/2 → sample s J r = false

/-- The extra marker is white at even widths and black at odd widths. -/
def marker (J : Nat) : Bool := !decide (J % 2 = 0)

private def depth (J r : Nat) : Int := (((windowStart J+r)/2 : Nat) : Int)

private theorem sample_eq (s J r : Nat) :
    sample s J r = orbit (cut s J) r (depth J r) := by
  unfold sample read cut depth
  rw [← orbit_add, ← orbit_add, Nat.add_assoc]

private theorem exterior : ∀ i : Int, i < 0 → single i = false := by
  intro i hi
  simp [single,show i ≠ 0 by omega]

private theorem single_nat : (fun n : Nat => single (n:Int)) = RightRayDelay.pulse 0 := by
  funext n
  by_cases h : n = 0 <;> simp [single,RightRayDelay.pulse,h]

private theorem single_bit (t j : Nat) :
    orbit single t (j:Int) = RightRayDelay.SeedPhases.phase t j := by
  rw [RightRayPeriodBridge.nat_bridge single exterior, single_nat]
  rfl

private theorem bit_one_eq_two (t : Nat) : orbit single t 1 = orbit single t 2 := by
  induction t with
  | zero => decide
  | succ t ih =>
    have z : orbit single t 0 = true :=
      (single_bit t 0).trans (RightRayDelay.SeedPhases.phase_seed t).1
    change xor (orbit single t 1) (orbit single t 0 || orbit single t (-1)) =
      xor (orbit single t 2) (orbit single t 1 || orbit single t 0)
    simp [z,ih]

theorem block_iff_return (s J : Nat) (hJ : 4 ≤ J) :
    whiteBlock s J ↔ Returns J (s + windowStart J) := by
  let n := J/2 - 2
  have hn : n+1+1 = J/2 := by dsimp [n]; omega
  have hpath : Causal (depth J) (n+1) := by
    intro k _
    dsimp [depth,windowStart]
    constructor <;> omega
  have hold : depth J (n+1) = depth J n := by dsimp [depth,windowStart,n]; omega
  have last : depth J (n+1) = (J:Int)-1 := by dsimp [depth,windowStart,n]; omega
  have cone := white_path_iff (orbit (cut s J)) (orbit_step (cut s J)) 0 n (depth J) hpath hold
  rw [last] at cone
  let a : Int := (J:Int)-1-2*((n+1 : Nat):Int)
  have lower : 1 ≤ a ∧ a ≤ 2 := by dsimp [a,n]; omega
  have block : whiteBlock s J ↔ White (cut s J) a ((J:Int)-1) := by
    constructor
    · intro h
      apply cone.mp
      intro r hr
      simpa only [Nat.zero_add,sample_eq] using h r (by omega)
    · intro h r hr
      rw [sample_eq]
      simpa only [Nat.zero_add] using (cone.mpr h) r (by omega)
  rw [block]
  constructor
  · intro hw i hi
    by_cases hneg : i < 0
    · exact (RightRayPeriodBridge.left_white single exterior _ i hneg).trans (exterior i hneg).symm
    by_cases hz : i = 0
    · subst i
      exact (single_bit _ 0).trans (RightRayDelay.SeedPhases.phase_seed _).1
    change cut s J i = single i
    rw [show single i = false by simp [single,hz]]
    by_cases ha : a ≤ i
    · exact hw i ha (by omega)
    · rw [show i=1 by omega]
      exact (bit_one_eq_two _).trans (hw 2 (by omega) (by omega))
  · intro h i hlo hhi
    change orbit single (s + windowStart J) i = false
    rw [h i (by omega)]
    simp [single,show i ≠ 0 by omega]

private theorem complement {x y b : Bool} (h : x=b ↔ y=false) : x=(!b) ↔ y=true := by
  cases x <;> cases y <;> cases b <;> simp_all

theorem next_record (s J : Nat) (hJ : 4 ≤ J) (hw : whiteBlock s J) :
    sample s J (J/2) = marker J ↔ cut s J (J:Int) = true := by
  have ret := (block_iff_return s J hJ).mp hw
  have low : RightRayDelay.Below (fun n : Nat => cut s J (n:Int)) (RightRayDelay.pulse 0) J := by
    rw [← single_nat]
    exact fun i hi => ret (i:Int) (by omega)
  have e := RightRayDelay.spot_iff low (J/2)
  have ref : RightRayDelay.run (RightRayDelay.pulse 0) (J/2) J = decide (J%2=0) := by
    have top := RightRayDelay.SeedPhases.head_bit (J/2)
    change RightRayDelay.SeedPhases.phase (J/2) J = _
    by_cases hev : J%2=0
    · simpa only [hev,decide_true,show 2*(J/2)=J by omega] using top.1
    · simpa only [hev,decide_false] using top.2 J (by omega)
  have initial : RightRayDelay.pulse 0 J = false := by simp [RightRayDelay.pulse,show J ≠ 0 by omega]
  rw [ref,initial] at e
  have hy : ∀ i : Int, i<0 → cut s J i=false := RightRayPeriodBridge.left_white single exterior _
  rw [sample_eq,show depth J (J/2) = (J:Int) by dsimp [depth,windowStart]; omega,
    RightRayPeriodBridge.nat_bridge (cut s J) hy]
  exact complement e

private theorem return_mul {J P : Nat} (h : Returns J P) (q : Nat) : Returns J (P*q) := by
  induction q with
  | zero => rw [Nat.mul_zero]; exact fun _ _ => rfl
  | succ q ih =>
    intro i hi
    rw [Nat.mul_succ,orbit_add]
    exact ((agreed_orbit ih P) i hi).trans (h i hi)

private theorem place (D P T : Nat) : ∃ s,
    AgreesBelow (orbit single P) (orbit single (s+T)) (D:Int) := by
  have hpos : 0 < 2^D := Nat.pow_pos (by omega)
  have hT : T ≤ T*2^D := by
    calc
      T = T*1 := by simp
      _ ≤ T*2^D := Nat.mul_le_mul_left T hpos
  refine ⟨P+T*2^D-T,?_⟩
  intro i hi
  rw [show P+T*2^D-T+T = P+T*2^D by omega]
  exact RightRayProbeTime.period_mul (f := fun t => orbit single t i)
    (fun t => RightRayPeriodBridge.low_period single exterior D t i hi) P T

/-- Detect the lift bit at the least positive lower return, from observations
at a genuine singleton launch. The hypothesis specifies the lower return times. -/
theorem marker_iff_lift_bit (J P : Nat) (hJ : 4 ≤ J)
    (hP : ∀ t, Returns J t ↔ P ∣ t) :
    (∃ s, whiteBlock s J ∧ sample s J (J/2) = marker J) ↔ orbit single P (J:Int)=true := by
  have ret := (hP P).mpr (Nat.dvd_refl _)
  have initial : single (J:Int)=false := by simp [single,show (J:Int) ≠ 0 by omega]
  constructor
  · rintro ⟨s,hw,hm⟩
    have hbit := (next_record s J hJ hw).mp hm
    cases hb : orbit single P (J:Int) with
    | true => rfl
    | false =>
      have big : Returns (J+1) P := by
        intro i hi
        by_cases hlt : i < (J:Int)
        · exact ret i hlt
        · rw [show i=(J:Int) by omega,hb,initial]
      obtain ⟨q,hq⟩ := (hP _).mp ((block_iff_return _ _ hJ).mp hw)
      have allret : Returns (J+1) (s + windowStart J) := by rw [hq]; exact return_mul big q
      change orbit single (s + windowStart J) (J:Int) = true at hbit
      rw [allret _ (by omega),initial] at hbit
      contradiction
  · intro hb
    obtain ⟨s,h⟩ := place (J+1) P (windowStart J)
    have hs : Returns J (s + windowStart J) := fun i hi => (h i (by omega)).trans (ret i hi)
    have hw := (block_iff_return s J hJ).mpr hs
    exact ⟨s,hw,(next_record s J hJ hw).mpr ((h _ (by omega)).trans hb)⟩

#print axioms block_iff_return
#print axioms next_record
#print axioms marker_iff_lift_bit
private theorem double_bool {a b c : Bool} (h : a=b ↔ b=c) : a=c := by
  cases a <;> cases b <;> cases c <;> simp_all

/-- The coloured word occurs iff the entire width-(J+1) return set consists
of the multiples of 2P, where the width-J returns are the multiples of P. -/
theorem marker_iff_double (J P : Nat) (hJ : 4 ≤ J) (hpos : 0 < P)
    (hP : ∀ t, Returns J t ↔ P ∣ t) :
    (∃ s, whiteBlock s J ∧ sample s J (J/2) = marker J) ↔
      ∀ t, Returns (J+1) t ↔ (2*P) ∣ t := by
  rw [marker_iff_lift_bit J P hJ hP]
  have ret := (hP P).mpr (Nat.dvd_refl _)
  have initial : single (J:Int) = false := by simp [single,show (J:Int) ≠ 0 by omega]
  have low : RightRayDelay.Below (RightRayDelay.run (RightRayDelay.pulse 0) P)
      (RightRayDelay.pulse 0) J := by
    intro i hi
    exact (single_bit P i).symm.trans ((ret (i:Int) (by omega)).trans (congrFun single_nat i))
  have reset := double_bool (RightRayDelay.spot_iff low P)
  have lower : Returns J (2*P) := by rw [Nat.mul_comm]; exact return_mul ret 2
  have big : Returns (J+1) (2*P) := by
    intro i hi
    by_cases hlt : i < (J:Int)
    · exact lower i hlt
    · rw [show i=(J:Int) by omega]
      refine Eq.trans ?_ (congrFun single_nat J).symm
      rw [single_bit]
      change RightRayDelay.run (RightRayDelay.pulse 0) (2*P) J = _
      rw [show 2*P=P+P by omega,RightRayDelay.run_add]
      exact reset
  constructor
  · intro hb t
    constructor
    · intro ht
      have small : Returns J t := fun i hi => ht i (by omega)
      obtain ⟨q,hq⟩ := (hP t).mp small
      by_cases hev : q%2=0
      · refine ⟨q/2,?_⟩
        calc
          t = P*q := hq
          _ = P*(2*(q/2)) := congrArg (fun k => P*k) (by omega)
          _ = (2*P)*(q/2) := by simp [Nat.mul_comm,Nat.mul_left_comm,Nat.mul_assoc]
      · have eqt : t = (2*P)*(q/2)+P := by
          calc
            t = P*q := hq
            _ = P*(2*(q/2)+1) := congrArg (fun k => P*k) (by omega)
            _ = (2*P)*(q/2)+P := by simp [Nat.mul_add,Nat.mul_comm,Nat.mul_left_comm,Nat.mul_assoc]
        have hmatch := (agreed_orbit (return_mul big (q/2)) P) (J:Int) (by omega)
        have ho := ht (J:Int) (by omega)
        rw [eqt,orbit_add,hmatch,hb,initial] at ho
        contradiction
    · rintro ⟨q,rfl⟩
      exact return_mul big q
  · intro h
    cases hb : orbit single P (J:Int) with
    | true => rfl
    | false =>
      have retP : Returns (J+1) P := by
        intro i hi
        by_cases hlt : i < (J:Int)
        · exact ret i hlt
        · rw [show i=(J:Int) by omega,hb,initial]
      have hle := Nat.le_of_dvd hpos ((h P).mp retP)
      omega

#print axioms marker_iff_double

end RightRayAllWidths

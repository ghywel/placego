import RightRayFollowerProbe
import RightRayProbeTime
import RightRayPeriodBridge

/-! Finite observation languages at a cut immediately before a new wheel.
A completed snapshot has the prescribed lower half and finite support above.
This file compares even cuts, with all future times measured from their own cut. -/
namespace RightRayLanguage

open RightRayWhiteCone RightRayProbe RightRayFollowerProbe

def Allowed (x : Row) (d : Int) (len : Nat) (w : Nat → Bool) : Prop :=
  ∃ y, AgreesBelow x y d ∧ HighFinite y ∧
    ∀ s, s < len → orbit y s (ray d 0 s) = w s

def Same (x : Row) (d : Int) (z : Row) (e : Int) : Prop :=
  ∀ len w, Allowed x d len w ↔ Allowed z e len w

def band (x : Row) (d : Int) (k t : Nat) : Bool :=
  if k = 1 then orbit x t (d-1) else orbit x t (d-1) || orbit x t (d-2)

private theorem band_white {x : Row} {d : Int} {k t : Nat} (hk : k=1 ∨ k=2) :
    White (orbit x t) (d-(k:Int)) (d-1) ↔ band x d k t = false := by
  rcases hk with rfl | rfl
  · constructor
    · intro h; exact h _ (by omega) (by omega)
    · intro h i lo hi
      have eq : i = d-1 := by omega
      rw [eq]; exact h
  · simp only [band, show ¬ (2:Nat)=1 by omega, if_false, Bool.or_eq_false_iff]
    constructor
    · intro h; exact ⟨h _ (by omega) (by omega), h _ (by omega) (by omega)⟩
    · intro h i lo hi
      have eq : i = d-1 ∨ i = d-2 := by omega
      rcases eq with rfl | rfl
      · exact h.1
      · exact h.2

private theorem later_transfer {x z : Row} {d e : Int}
    (sub : ∀ len w, Allowed x d len w → Allowed z e len w)
    (wait T : Nat) :
    DelayedWhite x d wait (fun s => ray d 0 (wait+s)) T →
    DelayedWhite z e wait (fun s => ray e 0 (wait+s)) T := by
  rintro ⟨y, hy, hf, hw⟩
  let w := fun s => orbit y s (ray d 0 s)
  obtain ⟨v,hv,hf',he⟩ := sub (wait+T+1) w ⟨y,hy,hf,fun _ _ => rfl⟩
  refine ⟨v,hv,hf',fun s hs => ?_⟩
  exact (he (wait+s) (by omega)).trans (hw s hs)

private theorem raw_even (d : Int) (m k : Nat) :
    (fun s => ray d 0 (2*(3*m-k-1)+s)) = ray (d+((3*m-k-1 : Nat):Int)) 0 := by
  funext s; dsimp [ray]; omega

private theorem raw_odd (d : Int) (m k : Nat) :
    (fun s => ray d 0 (2*(3*m-k)+1+s)) = ray (d+((3*m-k : Nat):Int)) 1 := by
  funext s; dsimp [ray]; omega

private theorem bool_iff {a b : Bool} (h : (a=false) ↔ (b=false)) : a=b := by
  cases a <;> cases b <;> simp_all

/-- The two existential probe alignments recover the complete boundary movie. -/
theorem boundary_of_same {x z : Row} {d e : Int} (hs : Same x d z e)
    {D : Nat} (hx : ∀ k, k=1 ∨ k=2 → RightRayProbeTime.Period (band x d k) (2^D))
    (hz : ∀ k, k=1 ∨ k=2 → RightRayProbeTime.Period (band z e k) (2^D)) :
    ∀ k, k=1 ∨ k=2 → ∀ t, band x d k t = band z e k t := by
  intro k hk t
  apply RightRayProbeTime.recover_at_k D (hx k hk) (hz k hk) (M := 1) hk (t := t)
  intro m hm
  have hki : 1 ≤ k ∧ k ≤ 2 := by omega
  have tests (w T : Nat) :
      DelayedWhite x d w (fun s => ray d 0 (w+s)) T ↔
      DelayedWhite z e w (fun s => ray e 0 (w+s)) T :=
    ⟨later_transfer (fun len word => (hs len word).mp) w T,
     later_transfer (fun len word => (hs len word).mpr) w T⟩
  constructor
  · apply bool_iff
    have h := tests (2*(3*m-k-1)) (2*m-1)
    rw [raw_even d, raw_even e, even_follower_probe x d k m hki (by omega),
      even_follower_probe z e k m hki (by omega), band_white hk, band_white hk] at h
    exact h
  · apply bool_iff
    have h := tests (2*(3*m-k)+1) (2*m)
    rw [raw_odd d, raw_odd e, odd_follower_probe x d k m hki (by omega),
      odd_follower_probe z e k m hki (by omega), band_white hk, band_white hk] at h
    exact h

private theorem same_band_of_low {x y : Row} {d : Int} (h : AgreesBelow x y d) (t k : Nat) :
    band y d k t = band x d k t := by
  simp only [band, agreed_orbit h t (d-1) (by omega), agreed_orbit h t (d-2) (by omega)]

/-- Copy the upper snapshot above the other cut and drive it with the same two words. -/
private theorem copy_allowed {x z : Row} {d e : Int}
    (h : ∀ k, k=1 ∨ k=2 → ∀ t, band x d k t = band z e k t)
    {len w} : Allowed x d len w → Allowed z e len w := by
  rintro ⟨y,hy,⟨b,hb⟩,read⟩
  let v : Row := fun i => if i < e then z i else y (d+(i-e))
  have hv : AgreesBelow z v e := by intro i hi; simp [v,hi]
  have heq (t k : Nat) (hk : k=1 ∨ k=2) : band v e k t = band y d k t := by
    rw [same_band_of_low hv, same_band_of_low hy, h k hk t]
  have tail : ∀ t, ∀ j : Int, 0 ≤ j → orbit v t (e+j) = orbit y t (d+j) := by
    intro t
    induction t with
    | zero =>
      intro j hj
      simp [orbit,v,show ¬ e+j<e by omega]
    | succ t ih =>
      intro j hj
      by_cases h0 : j=0
      · subst j
        have hh := ih 0 (by omega)
        simp only [Int.add_zero] at hh ⊢
        change xor (orbit v t e) (band v e 2 t) = xor (orbit y t d) (band y d 2 t)
        rw [hh,heq t 2 (Or.inr rfl)]
      · by_cases h1 : j=1
        · subst j
          have u := heq t 1 (Or.inl rfl)
          simp only [band,if_pos rfl] at u
          simp only [orbit, show e+1-1=e+0 by omega,show d+1-1=d+0 by omega,
            show e+1-2=e-1 by omega,show d+1-2=d-1 by omega,
            ih 1 (by omega), ih 0 (by omega), u]
        · simp only [orbit, show e+j-1=e+(j-1) by omega,show d+j-1=d+(j-1) by omega,
            show e+j-2=e+(j-2) by omega,show d+j-2=d+(j-2) by omega,
            ih j hj,ih (j-1) (by omega),ih (j-2) (by omega)]
  refine ⟨v,hv,⟨max e (b+e-d),?_⟩,?_⟩
  · intro i hi
    simp only [v,show ¬ i<e by omega,if_false]
    exact hb _ (by omega)
  · intro s hs
    exact (tail s _ (by omega)).trans (read s hs)

theorem same_of_boundary {x z : Row} {d e : Int}
    (h : ∀ k, k=1 ∨ k=2 → ∀ t, band x d k t = band z e k t) : Same x d z e :=
  fun _ _ => ⟨copy_allowed h,copy_allowed (fun k hk t => (h k hk t).symm)⟩

private theorem bands_period (x : Row) (hx : ∀ i : Int, i<0 → x i=false)
    (D : Nat) (d : Int) (hd : d ≤ (D:Int)) (k : Nat) :
    RightRayProbeTime.Period (band x d k) (2^D) := by
  intro t
  simp only [band, RightRayPeriodBridge.low_period x hx D t (d-1) (by omega),
    RightRayPeriodBridge.low_period x hx D t (d-2) (by omega)]

/-- Complete finite-word follower equivalence, for any two cut snapshots with white exterior.
The two depths may differ. U is the top low bit and V the OR of the top two. -/
theorem same_iff_movies (x z : Row) (d e : Int) (hx : ∀ i : Int, i<0 → x i=false)
    (hz : ∀ i : Int, i<0 → z i=false) :
    Same x d z e ↔ ∀ k, k=1 ∨ k=2 → ∀ t, band x d k t = band z e k t := by
  constructor
  · intro hs
    let D := (max d e).toNat
    exact boundary_of_same (D := D) hs
      (fun k _ => bands_period x hx D d (by dsimp [D]; omega) k)
      (fun k _ => bands_period z hz D e (by dsimp [D]; omega) k)
  · exact same_of_boundary

#print axioms same_iff_movies
end RightRayLanguage

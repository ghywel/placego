import RightRayLanguage

/-! Exact passage between the observations of a genuine finite, right-anchored
initial row and the high-completion language of its later low register. The
cut is immediately before tick 2d. The hypothesis d>0 ensures the anchor
is already in the observed past. -/

namespace RightRayRooted

open RightRayWhiteCone RightRayProbe RightRayFollowerProbe RightRayLanguage

def Root (x : Row) : Prop :=
  (∀ i : Int, i < 0 → x i = false) ∧ x 0 = true ∧ HighFinite x

def read (x : Row) (t : Nat) : Bool := orbit x t ((t/2 : Nat) : Int)

def Follows (x : Row) (d len : Nat) (w : Nat → Bool) : Prop :=
  ∃ y, Root y ∧ (∀ t, t < 2*d → read y t = read x t) ∧
    ∀ s, s < len → read y (2*d+s) = w s

theorem orbit_add (x : Row) (T s : Nat) : orbit x (T+s) = orbit (orbit x T) s := by
  induction s with
  | zero => rfl
  | succ s ih =>
    funext i
    simp only [Nat.add_succ, orbit, ih]

theorem high_orbit {x : Row} (hf : HighFinite x) (t : Nat) : HighFinite (orbit x t) := by
  induction t with
  | zero => exact hf
  | succ t ih =>
    obtain ⟨b,hb⟩ := ih
    refine ⟨b+2, ?_⟩
    intro i hi
    rw [orbit_step x t i, hb i (by omega), hb (i-1) (by omega), hb (i-2) (by omega)]
    rfl

theorem read_cut (y : Row) (d s : Nat) :
    read y (2*d+s) = orbit (orbit y (2*d)) s (ray (d : Int) 0 s) := by
  unfold read
  rw [orbit_add]
  congr 1
  dsimp [ray]; omega

theorem low_iff_past {x y : Row} (hx : ∀ i : Int, i<0 → x i=false)
    (hy : ∀ i : Int, i<0 → y i=false) {d : Nat} (hd : 0<d) :
    AgreesBelow x y (d : Int) ↔ ∀ t, t<2*d → read y t = read x t := by
  constructor
  · intro h t ht
    exact agreed_orbit h t ((t/2 : Nat) : Int) (by omega)
  · intro h
    have he : RightRayDelay.Below (fun n : Nat => y (n:Int)) (fun n : Nat => x (n:Int)) ((d-1)+1) := by
      apply RightRayDelay.decode
      intro t ht
      have e := h t (by omega)
      simpa only [read, RightRayDelay.readRay, RightRayPeriodBridge.nat_bridge x hx,
        RightRayPeriodBridge.nat_bridge y hy] using e
    intro i hi
    by_cases hn : i<0
    · rw [hy i hn,hx i hn]
    · rw [show i = (i.toNat : Int) by omega]
      exact he i.toNat (by omega)

/-- A word can extend the observed past of a finite odd seed exactly when
its cut register permits it with unrestricted finite high completion. -/
theorem follows_iff_allowed {x : Row} (hx : Root x) (d len : Nat) (hd : 0<d) (w : Nat → Bool) :
    Follows x d len w ↔ Allowed (orbit x (2*d)) (d:Int) len w := by
  constructor
  · rintro ⟨y,hy,hpast,hw⟩
    have low := (low_iff_past hx.1 hy.1 hd).mpr hpast
    exact ⟨orbit y (2*d),agreed_orbit low _,high_orbit hy.2.2 _,fun s hs =>
      (read_cut y d s).symm.trans (hw s hs)⟩
  · rintro ⟨v,low,_,hw⟩
    -- Set the required high bits at the cut by choosing their preimages
    -- at time zero, while preserving every previously observed bit.
    obtain ⟨y,hstart,hcut,hm⟩ := place_window x v (d:Int) (2*d) low (len+1)
    have hyneg : ∀ i : Int, i<0 → y i=false := fun i hi =>
      (hstart i (by omega)).trans (hx.1 i hi)
    have hroot : Root y := ⟨hyneg,(hstart 0 (by omega)).trans hx.2.1,⟨_,hcut⟩⟩
    refine ⟨y,hroot,(low_iff_past hx.1 hyneg hd).mp hstart,?_⟩
    intro s hs
    rw [read_cut]
    exact ((agreed_orbit hm s) (ray (d:Int) 0 s) (by dsimp [ray]; omega)).trans (hw s hs)

/-- The complete movie criterion stated directly for histories of physical
finite anchored rows, allowing the two histories to have different lengths. -/
theorem rooted_same_iff_movies {x z : Row} (hx : Root x) (hz : Root z)
    {d e : Nat} (hd : 0<d) (he : 0<e) :
    (∀ len w, Follows x d len w ↔ Follows z e len w) ↔
    ∀ k, k=1 ∨ k=2 → ∀ t,
      band (orbit x (2*d)) (d:Int) k t = band (orbit z (2*e)) (e:Int) k t := by
  have hcut := same_iff_movies (orbit x (2*d)) (orbit z (2*e)) (d:Int) (e:Int)
    (RightRayPeriodBridge.left_white x hx.1 _) (RightRayPeriodBridge.left_white z hz.1 _)
  constructor
  · intro h
    apply hcut.mp
    intro len w
    exact (follows_iff_allowed hx d len hd w).symm.trans ((h len w).trans (follows_iff_allowed hz e len he w))
  · intro h len w
    exact (follows_iff_allowed hx d len hd w).trans (((hcut.mpr h) len w).trans
      (follows_iff_allowed hz e len he w).symm)

#print axioms rooted_same_iff_movies

end RightRayRooted

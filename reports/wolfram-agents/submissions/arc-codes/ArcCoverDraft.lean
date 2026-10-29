import ArcBreakSequence
import ArcDeterminantDraft

/-!
# A finite lifted cover contradicts the repeat bound at one approximation scale

UNCOMPILED integration draft. The cover is an explicit hypothesis on actual breaks. This file does not yet
construct that cover from a circular step code or discharge the approximation scale using continuants.
It connects the actual-break construction to the independently compiled real determinant inequality.
-/

namespace ArcCover

/-- Two orbit lifts in one half-open interval give a strictly close integer return. -/
theorem same_interval_return (alpha theta epsilon endpoint : ℝ) (s t : Nat) (zs zt : ℤ)
    (hst : s < t)
    (hslo : endpoint ≤ theta+(s : ℝ)*alpha-zs)
    (hshi : theta+(s : ℝ)*alpha-zs < endpoint+epsilon)
    (htlo : endpoint ≤ theta+(t : ℝ)*alpha-zt)
    (hthi : theta+(t : ℝ)*alpha-zt < endpoint+epsilon) :
    |((t-s : Nat) : ℝ)*alpha-((zt-zs : ℤ) : ℝ)| < epsilon := by
  have hd : ((t-s : Nat) : ℝ)*alpha-((zt-zs : ℤ) : ℝ) =
      (theta+(t : ℝ)*alpha-zt)-(theta+(s : ℝ)*alpha-zs) := by
    rw [Nat.cast_sub (Nat.le_of_lt hst)]
    push_cast
    ring
  rw [hd]
  exact abs_lt.2 ⟨by linarith, by linarith⟩

/-- A finite cover labels actual mismatches by half-open intervals and integer orbit lifts. -/
def LiftCover (c : Nat → Bool) (q r : Nat) (alpha theta epsilon : ℝ)
    (endpoint : Nat → ℝ) (label : Nat → Nat) (lift : Nat → ℤ) : Prop :=
  ∀ s, c (s+q) ≠ c s → label s < r ∧
    endpoint (label s) ≤ theta+(s : ℝ)*alpha-lift s ∧
    theta+(s : ℝ)*alpha-lift s < endpoint (label s)+epsilon

/-- RepeatBound and the lifted cover produce a positive short return below the counting envelope. -/
theorem short_return (c : Nat → Bool) (q C r : Nat) (alpha theta epsilon : ℝ)
    (endpoint : Nat → ℝ) (label : Nat → Nat) (lift : Nat → ℤ)
    (hr : ArcBreakSequence.RepeatBound c q C)
    (hc : LiftCover c q r alpha theta epsilon endpoint label lift) :
    ∃ m : Nat, ∃ a : ℤ, 0 < m ∧ m < 2^(r+1)*(q+C+2) ∧
      |(m : ℝ)*alpha-a| < epsilon := by
  let d := ArcBreakSequence.sequence c q C hr
  have hb (k : Nat) : c (d k+q) ≠ c (d k) := ArcBreakSequence.sequence_break c q C hr k
  have hl (k : Nat) (_ : k ≤ r) : label (d k) < r := (hc (d k) (hb k)).1
  obtain ⟨i,j,hij,hjr,he⟩ := ArcBreakBounds.label_collision r (fun k => label (d k)) hl
  have hdlt : d i < d j := ArcBreakSequence.sequence_strict c q C hr hij
  have henv := ArcBreakBounds.break_envelope q C d
    (ArcBreakSequence.sequence_first c q C hr)
    (ArcBreakSequence.sequence_step_bound c q C hr) j
  have hp : 2^(j+1) ≤ 2^(r+1) := Nat.pow_le_pow_right (by decide) (by omega)
  have hm := Nat.mul_le_mul_right (q+C+2) hp
  have hbound : d j-d i < 2^(r+1)*(q+C+2) := by omega
  have hs := hc (d i) (hb i)
  have ht := hc (d j) (hb j)
  rw [← he] at ht
  refine ⟨d j-d i,lift (d j)-lift (d i),by omega,hbound,?_⟩
  exact same_interval_return alpha theta epsilon (endpoint (label (d i)))
    (d i) (d j) (lift (d i)) (lift (d j)) hdlt hs.2.1 hs.2.2 ht.2.1 ht.2.2

/-- Conditional one-scale exclusion, retaining every geometric and approximation premise. -/
theorem no_repeat_of_cover (c : Nat → Bool) (q C r : Nat) (alpha theta : ℝ) (p u v : ℤ)
    (endpoint : Nat → ℝ) (label : Nat → Nat) (lift : Nat → ℤ)
    (hq : 0 < q) (hbezout : u*p+v*(q : ℤ) = 1)
    (hepsilon : 0 < |(q : ℝ)*alpha-p|)
    (hc : LiftCover c q r alpha theta |(q : ℝ)*alpha-p| endpoint label lift)
    (hscale : (((2^(r+1)*(q+C+2) : Nat) : ℝ)+q)*|(q : ℝ)*alpha-p| ≤ 1) :
    ¬ ArcBreakSequence.RepeatBound c q C := by
  intro hr
  obtain ⟨m,a,hm,hmB,hclose⟩ := short_return c q C r alpha theta _ endpoint label lift hr hc
  apply ArcDeterminant.no_short_return alpha p (q : ℤ) (m : ℤ) a u v
    ((2^(r+1)*(q+C+2) : Nat) : ℝ)
    (by exact_mod_cast hq) (by exact_mod_cast hm) hbezout
    (by simpa using hepsilon) (by exact_mod_cast hmB) (by simpa using hscale)
  simpa using hclose

#print axioms ArcCover.same_interval_return
#print axioms ArcCover.short_return
#print axioms ArcCover.no_repeat_of_cover

end ArcCover

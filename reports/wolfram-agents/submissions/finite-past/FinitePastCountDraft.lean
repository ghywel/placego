module
public import NormalizedFinitePastDraft

/-!
# Counting normalized finite parents without a Mathlib cardinality import

UNCOMPILED source preparation, GC2290. Reuses Rule30Jen.allLists,
length_allLists and nodup_map_of_inj. Counts are lengths of proved-exhaustive,
duplicate-free enumerations of actual physical rows, not unproved multiset
lengths. The bijection and counts are the known G121/L077 argument. Width zero
is empty, width one is a singleton, and width at least two has free interior.
No compiler acceptance, official replay or independent source read is claimed.
-/

@[expose] public section
namespace Ruliology.CellularAutomata.Rule30FinitePastDraft
open Rule30Jen Rule30Realization

/-- A Boolean interior framed by black endpoints; all exterior cells are white. -/
def framedRow (bits : List Bool) (i : Int) : Bool :=
  if i=0 ∨ i=(bits.length : Int)+1 then true
  else if 0<i ∧ i<(bits.length : Int)+1 then bits.getD (i-1).toNat false else false

def samples (x : Int → Bool) (n : Nat) : List Bool :=
  List.ofFn fun i : Fin n => x ((i.val : Int)+1)

theorem length_samples (x : Int → Bool) (n : Nat) : (samples x n).length=n := by
  simp [samples]

theorem framedRow_span (bits : List Bool) : Span (framedRow bits) 0 ((bits.length : Int)+1) := by
  refine ⟨by omega,?_,?_,?_,?_⟩
  · simp [framedRow]
  · simp [framedRow]
  · intro i hi
    have h0 : ¬(i=0 ∨ i=(bits.length : Int)+1) := by omega
    have h1 : ¬(0<i ∧ i<(bits.length : Int)+1) := by omega
    simp [framedRow,h0,h1]
  · intro i hi
    have h0 : ¬(i=0 ∨ i=(bits.length : Int)+1) := by omega
    have h1 : ¬(0<i ∧ i<(bits.length : Int)+1) := by omega
    simp [framedRow,h0,h1]

theorem framedRow_interior (bits : List Bool) {i : Nat} (hi : i<bits.length) :
    framedRow bits ((i : Int)+1)=bits[i] := by
  have h0 : ¬((i : Int)+1=0 ∨ (i : Int)+1=(bits.length : Int)+1) := by omega
  have h1 : 0<(i : Int)+1 ∧ (i : Int)+1<(bits.length : Int)+1 := by omega
  simp only [framedRow,if_neg h0,if_pos h1,
    show (((i : Int)+1)-1).toNat=i by omega,List.getD_eq_getElem?_getD,
    List.getElem?_eq_getElem hi,Option.getD_some]

theorem framedRow_injective {a b : List Bool} (hl : a.length=b.length)
    (he : framedRow a=framedRow b) : a=b := by
  apply List.ext_getElem hl
  intro i hi hj
  have e := congrFun he ((i : Int)+1)
  rw [framedRow_interior a hi,framedRow_interior b hj] at e
  exact e

theorem framedRow_samples {x : Int → Bool} {n : Nat} (hx : Span x 0 ((n : Int)+1)) :
    framedRow (samples x n)=x := by
  have hf := framedRow_span (samples x n)
  simp only [length_samples] at hf
  funext i
  by_cases h0 : i=0
  · subst i; exact hf.left_black.trans hx.left_black.symm
  by_cases hn : i=(n : Int)+1
  · subst i; exact hf.right_black.trans hx.right_black.symm
  by_cases hl : i<0
  · exact (hf.left_white i hl).trans (hx.left_white i hl).symm
  by_cases hr : (n : Int)+1<i
  · exact (hf.right_white i hr).trans (hx.right_white i hr).symm
  have hi : (i-1).toNat<(samples x n).length := by
    rw [length_samples]
    omega
  have e := framedRow_interior (samples x n) hi
  have index : (((i-1).toNat : Nat) : Int)+1=i := by omega
  simpa only [samples,List.getElem_ofFn,index] using e

/-- Converse to the kit's membership lemma: its enumeration has only the stated length. -/
theorem length_of_mem_allLists : ∀ n : Nat, ∀ bits : List Bool,
    bits ∈ allLists n → bits.length=n
  | 0,bits,h => by
    simp only [allLists,List.mem_singleton] at h
    subst bits
    rfl
  | n+1,bits,h => by
    change bits ∈ (allLists n).map (false :: ·) ++ (allLists n).map (true :: ·) at h
    rcases List.mem_append.mp h with h | h
    · obtain ⟨b,hb,rfl⟩ := List.mem_map.mp h
      simp only [List.length_cons,length_of_mem_allLists n b hb]
    · obtain ⟨b,hb,rfl⟩ := List.mem_map.mp h
      simp only [List.length_cons,length_of_mem_allLists n b hb]

theorem allLists_nodup : ∀ n : Nat, (allLists n).Nodup
  | 0 => by simp [allLists]
  | n+1 => by
    rw [allLists,List.nodup_append]
    refine ⟨?_,?_,?_⟩
    · apply nodup_map_of_inj (false :: ·) (allLists_nodup n)
      intro a _ b _ he
      exact (List.cons.inj he).2
    · apply nodup_map_of_inj (true :: ·) (allLists_nodup n)
      intro a _ b _ he
      exact (List.cons.inj he).2
    · intro a ha b hb he
      obtain ⟨a',_,rfl⟩ := List.mem_map.mp ha
      obtain ⟨b',_,rfl⟩ := List.mem_map.mp hb
      simp at he

def singleRow (i : Int) : Bool := decide (i=0)

theorem singleRow_span : Span singleRow 0 0 := by
  refine ⟨by omega,by decide,by decide,?_,?_⟩
  · intro i hi; simp [singleRow]; omega
  · intro i hi; simp [singleRow]; omega

theorem span_zero_unique {x : Int → Bool} (hx : Span x 0 0) : x=singleRow := by
  funext i
  by_cases hi : i=0
  · subst i; simpa [singleRow] using hx.left_black
  · have hz : x i=false := by
      by_cases hl : i<0
      · exact hx.left_white i hl
      · exact hx.right_white i (by omega)
    simp [singleRow,hi,hz]

def allRows : Nat → List (Int → Bool)
  | 0 => []
  | 1 => [singleRow]
  | n+2 => (allLists n).map framedRow

def widthCount : Nat → Nat
  | 0 => 0
  | 1 => 1
  | n+2 => 2^n

theorem mem_allRows (w : Nat) (x : Int → Bool) : x ∈ allRows w ↔ Normal w x := by
  cases w with
  | zero =>
    change x ∈ [] ↔ Span x 0 (-1)
    constructor
    · intro h; cases h
    · intro h; have := h.ordered; omega
  | succ w =>
    cases w with
    | zero =>
      simp only [allRows,List.mem_singleton]
      change x=singleRow ↔ Span x 0 0
      constructor
      · intro h; rw [h]; exact singleRow_span
      · exact span_zero_unique
    | succ n =>
      change x ∈ (allLists n).map framedRow ↔ Normal (n+2) x
      constructor
      · intro h
        obtain ⟨bits,hb,rfl⟩ := List.mem_map.mp h
        have hs := framedRow_span bits
        rw [length_of_mem_allLists n bits hb] at hs
        change Span (framedRow bits) 0 (((n+2 : Nat) : Int)-1)
        simpa only [show (((n+2 : Nat) : Int)-1)=(n : Int)+1 by omega] using hs
      · intro hx
        have hs : Span x 0 ((n : Int)+1) := by
          simpa only [Normal,show (((n+2 : Nat) : Int)-1)=(n : Int)+1 by omega] using hx
        apply List.mem_map.mpr
        refine ⟨samples x n,?_,framedRow_samples hs⟩
        have h := mem_allLists (samples x n)
        simpa only [length_samples] using h

theorem allRows_nodup : ∀ w : Nat, (allRows w).Nodup
  | 0 => by simp [allRows]
  | 1 => by simp [allRows]
  | n+2 => by
    apply nodup_map_of_inj framedRow (allLists_nodup n)
    intro a ha b hb he
    exact framedRow_injective
      ((length_of_mem_allLists n a ha).trans (length_of_mem_allLists n b hb).symm) he

theorem allRows_length : ∀ w : Nat, (allRows w).length=widthCount w
  | 0 => rfl
  | 1 => rfl
  | n+2 => by simp [allRows,widthCount,length_allLists]

/-- Enumerate the normalized n-step images of all width-w words. -/
def ancestorImages (w n : Nat) : List (Int → Bool) :=
  (allRows w).map (normalizedImage n)

theorem mem_ancestorImages (w n : Nat) (y : Int → Bool) :
    y ∈ ancestorImages w n ↔ Normal (w+2*n) y ∧ Past n y := by
  rw [← normalizedImage_range w n y]
  constructor
  · intro h
    obtain ⟨x,hx,he⟩ := List.mem_map.mp h
    exact ⟨x,(mem_allRows w x).mp hx,he⟩
  · rintro ⟨x,hx,he⟩
    exact List.mem_map.mpr ⟨x,(mem_allRows w x).mpr hx,he⟩

theorem ancestorImages_nodup (w n : Nat) : (ancestorImages w n).Nodup := by
  apply nodup_map_of_inj (normalizedImage n) (allRows_nodup w)
  intro x hx y hy he
  exact normalizedImage_injective ((mem_allRows w x).mp hx) ((mem_allRows w y).mp hy) he

theorem ancestorImages_length (w n : Nat) : (ancestorImages w n).length=widthCount w := by
  simp only [ancestorImages,List.length_map,allRows_length]

/-- Actual width-w finite-parent words, including the empty width-one/two cases. -/
def parentRows (w : Nat) : List (Int → Bool) :=
  if 3≤w then ancestorImages (w-2) 1 else []

theorem mem_parentRows (w : Nat) (y : Int → Bool) :
    y ∈ parentRows w ↔ Normal w y ∧ Past 1 y := by
  by_cases hw : 3≤w
  · simp only [parentRows,if_pos hw,mem_ancestorImages,
      show w-2+2*1=w by omega]
  · simp only [parentRows,if_neg hw,List.not_mem_nil,false_iff]
    intro h
    exact no_past_of_small_width h.1 (by omega) h.2

theorem parentRows_nodup (w : Nat) : (parentRows w).Nodup := by
  by_cases hw : 3≤w
  · simp only [parentRows,if_pos hw]
    exact ancestorImages_nodup (w-2) 1
  · simp [parentRows,hw]

theorem parentRows_count (w : Nat) :
    (parentRows w).length=if 3≤w then widthCount (w-2) else 0 := by
  by_cases hw : 3≤w <;> simp [parentRows,hw,ancestorImages_length]

/-- The usual one-quarter numerator, with all subtraction justified by w>=4. -/
theorem parentRows_count_ge_four {w : Nat} (hw : 4≤w) :
    (parentRows w).length=2^(w-4) := by
  obtain ⟨n,rfl⟩ : ∃ n : Nat, w=n+4 := ⟨w-4,by omega⟩
  rw [parentRows_count,if_pos (by omega),show n+4-2=n+2 by omega]
  simp [widthCount]

theorem parentRows_count_small :
    (parentRows 1).length=0 ∧ (parentRows 2).length=0 ∧ (parentRows 3).length=1 := by
  simp [parentRows_count,widthCount]

end Ruliology.CellularAutomata.Rule30FinitePastDraft
